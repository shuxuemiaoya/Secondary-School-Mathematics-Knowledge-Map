```python
import os
from pathlib import Path
import re

# 权威目录标题与其预期层级的映射（1=H1, 2=H2, 3=H3）
# 注意：键必须是目录中的标题去除末尾页码和导引符（如“…… 1”、“ /2”）后的干净文本。必须原样保留标题开头的章节号和序号前缀（如“第一章”、“1”、“2”、“1.1”等），绝对不能将其剥离或删除！
TOC_HEADINGS: dict[str, int] = {
    "第七章 相交线与平行线": 1,
    "7.1 相交线": 2,
    "观察与猜想 看图时的错觉": 3,
    "7.2 平行线": 2,
    "7.3 定义、命题、定理": 2,
    "7.4 平移": 2,
    "探究与发现 利用平移设计图案": 3,
    "数学活动": 3,
    "小结": 3,
    "第八章 实数": 1,
    "8.1 平方根": 2,
    "8.2 立方根": 2,
    "8.3 实数及其简单运算": 2,
    "阅读与思考 为什么 $\\sqrt{2}$ 不是有理数": 3,
    "数学活动": 3,
    "小结": 3,
    "第九章 平面直角坐标系": 1,
    "9.1 用坐标描述平面内点的位置": 2,
    "阅读与思考 用经纬度表示地理位置": 3,
    "9.2 坐标方法的简单应用": 2,
    "数学活动": 3,
    "小结": 3,
    "第十章 二元一次方程组": 1,
    "10.1 二元一次方程组的概念": 2,
    "10.2 消元——解二元一次方程组": 2,
    "10.3 实际问题与二元一次方程组": 2,
    "\\*10.4 三元一次方程组的解法": 2,
    "图说数学史 中国古代数学的光辉成就——解多元一次方程组": 3,
    "阅读与思考 中国古代著名的一次不定方程组问题": 3,
    "数学活动": 3,
    "小结": 3,
    "第十一章 不等式与不等式组": 1,
    "11.1 不等式": 2,
    "阅读与思考 用求差法比较大小": 3,
    "11.2 一元一次不等式": 2,
    "11.3 一元一次不等式组": 2,
    "数学活动": 3,
    "小结": 3,
    "综合与实践 低碳生活": 3,
    "第十二章 数据的收集、整理与描述": 1,
    "12.1 统计调查": 2,
    "探究与发现 瓶子中有多少粒豆子": 3,
    "12.2 用统计图描述数据": 2,
    "信息技术应用 利用信息技术工具画统计图": 3,
    "图说数学史 统计学点滴": 3,
    "数学活动": 3,
    "小结": 3,
    "综合与实践 白昼时长规律的探究": 3,
}

def get_target_root() -> Path:
    """获取目标文件夹路径，留空则使用脚本所在目录。"""
    return Path(input().strip()).resolve()

def protect_blocks(text: str) -> tuple[str, list[str]]:
    """保护 YAML、代码块、数学公式等内容。"""
    return text, []

def restore_blocks(text: str, blocks: list[str]) -> str:
    """恢复被保护内容。"""
    return text

def replace_in_file(path: Path) -> None:
    """读取、程序化判定标题并写回 Markdown 文件。"""
    text = path.read_text(encoding="utf-8")
    
    lines = text.splitlines()
    new_lines = []
    merged_indices = set()
    
    in_yaml = len(lines) > 0 and lines[0].strip() == "---"
    in_code = False
    code_marker = ""
    in_math = False
    
    # 预先计算去空格和转义反斜杠后的 TOC 键值对映射
    def clean_txt(s: str) -> str:
        s = s.replace("\\*", "").replace("$", "")
        s = s.replace("：", ":").replace("，", ",").replace("；", ";").replace("（", "(").replace("）", ")")
        s = s.replace("^", "").replace("{", "").replace("}", "").replace("*", "")
        return re.sub(r"\s+", "", s)
    
    toc_no_spaces = {clean_txt(k): k for k in TOC_HEADINGS}
    
    # 编译用于提取章节/序号前缀的正则表达式
    SECTION_NUM_RE = re.compile(r"^(\d+(?:\.\d+)+)\b")
    CHINESE_CHAPTER_RE = re.compile(r"第\s*([一二三四五六七八九十百千万零〇两0-9]+)\s*章")
    ENGLISH_CHAPTER_RE = re.compile(r"\bChapter\s+([0-9]+)\b", re.IGNORECASE)
    PARENT_CONTEXT_RE = re.compile(
        r"^(?:\s*\d+(?:[.．]\d+)+\s+|"
        r"\s*第\s*[一二三四五六七八九十百千万零〇两0-9]+\s*[章节篇部单元]\s*|"
        r"\s*(?:Part|Chapter|Section)\s+[A-Z0-9IVXLC]+\b)",
        re.IGNORECASE,
    )
    
    def adds_parent_context(before: str, after: str) -> bool:
        before_has = bool(CHINESE_CHAPTER_RE.search(before) or ENGLISH_CHAPTER_RE.search(before) or PARENT_CONTEXT_RE.search(before))
        after_has = bool(CHINESE_CHAPTER_RE.search(after) or ENGLISH_CHAPTER_RE.search(after) or PARENT_CONTEXT_RE.search(after))
        return after_has and not before_has
    
    for index, line in enumerate(lines):
        if index in merged_indices:
            stripped = line.strip()
            match = re.match(r"^(#{1,6})\s+(.+?)\s*$", stripped)
            if match:
                level = len(match.group(1))
                title_text = match.group(2).strip()
                expected_level = min(6, level + 3)
                new_line = "#" * expected_level + " " + title_text
            else:
                new_line = stripped
            leading = line[:len(line) - len(line.lstrip())]
            trailing = line[len(line.rstrip()):]
            new_lines.append(leading + new_line + trailing)
            continue
            
        stripped = line.strip()
        if in_yaml:
            new_lines.append(line)
            if index > 0 and stripped == "---":
                in_yaml = False
            continue
        if in_code:
            if stripped.startswith(code_marker):
                in_code = False
            new_lines.append(line)
            continue
        if in_math:
            if stripped == "$$":
                in_math = False
            new_lines.append(line)
            continue
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_code = True
            code_marker = stripped[:3]
            new_lines.append(line)
            continue
        if stripped == "$$":
            in_math = True
            new_lines.append(line)
            continue
            
        # 判定是否是标题行
        match = re.match(r"^(#{1,6})\s+(.+?)\s*$", stripped)
        if match:
            level = len(match.group(1))
            title_text = match.group(2).strip()
            # 剥离可能残留在正文标题中的页码尾巴，仅在必要时
            title_clean = re.sub(r'(?:\s+…+|\s+\.{2,}|\s+·{2,}|\s+．{2,}|\s+)\s*\d+$', '', title_text).strip()
            title_clean_no_space = clean_txt(title_clean)
            
            matched_toc_key = None
            
            # 1. 精确匹配
            if title_clean_no_space in toc_no_spaces:
                matched_toc_key = toc_no_spaces[title_clean_no_space]
            
            # 2. 章节/序号前缀匹配
            if not matched_toc_key:
                num_match = SECTION_NUM_RE.match(title_clean)
                if num_match:
                    prefix_num = num_match.group(1)
                    # 在 TOC 中寻找具有相同序号前缀的项
                    for tk in TOC_HEADINGS:
                        tk_clean = re.sub(r'(?:\s+…+|\s+\.{2,}|\s+·{2,}|\s+．{2,}|\s+)\s*\d+$', '', tk).strip()
                        tk_num_match = SECTION_NUM_RE.match(tk_clean)
                        if tk_num_match and tk_num_match.group(1) == prefix_num:
                            matched_toc_key = tk
                            break
            
            # 3. 后缀匹配
            if not matched_toc_key:
                for tk_ns, tk in toc_no_spaces.items():
                    if tk_ns.endswith(title_clean_no_space):
                        if not adds_parent_context(title_text, tk):
                            matched_toc_key = tk
                            break
            
            # 4. 前缀与后续内容匹配
            if not matched_toc_key:
                for tk_ns, tk in toc_no_spaces.items():
                    if tk_ns.startswith(title_clean_no_space) and len(title_clean_no_space) >= 3:
                        if not adds_parent_context(title_text, tk):
                            remaining_part = tk_ns[len(title_clean_no_space):]
                            
                            is_next_part_heading = False
                            lookahead_index = index + 1
                            next_heading_text = ""
                            while lookahead_index < len(lines):
                                next_line_stripped = lines[lookahead_index].strip()
                                if next_line_stripped:
                                    if next_line_stripped.startswith("#"):
                                        is_next_part_heading = True
                                        next_heading_match = re.match(r"^(#{1,6})\s+(.+?)\s*$", next_line_stripped)
                                        if next_heading_match:
                                            next_heading_text = clean_txt(next_heading_match.group(2))
                                    break
                                lookahead_index += 1
                            
                            if is_next_part_heading:
                                # 如果下一个标题就是拆分标题的剩余部分，则匹配成功
                                if next_heading_text == remaining_part:
                                    matched_toc_key = tk
                                    merged_indices.add(lookahead_index)
                                    break
                            else:
                                lookahead_text = ""
                                lookahead_index = index + 1
                                non_empty_count = 0
                                while lookahead_index < len(lines) and non_empty_count < 3:
                                    next_line_stripped = lines[lookahead_index].strip()
                                    if next_line_stripped:
                                        non_empty_count += 1
                                        lookahead_text += clean_txt(next_line_stripped)
                                    lookahead_index += 1
                                if remaining_part and remaining_part in lookahead_text:
                                    matched_toc_key = tk
                                    break
            
            if matched_toc_key:
                expected_level = TOC_HEADINGS[matched_toc_key]
                canonical_title = matched_toc_key
                new_line = "#" * expected_level + " " + canonical_title
            else:
                # 5. 前缀匹配（忽略空格与转义符，拆分标题中的引导标题，需降级）
                is_prefix = False
                for tk_ns in toc_no_spaces:
                    if tk_ns.startswith(title_clean_no_space):
                        is_prefix = True
                        break
                
                if is_prefix or level <= 3:
                    expected_level = min(6, level + 3)
                    new_line = "#" * expected_level + " " + title_text
                else:
                    new_line = stripped
                    
            leading = line[:len(line) - len(line.lstrip())]
            trailing = line[len(line.rstrip()):]
            new_lines.append(leading + new_line + trailing)
        else:
            new_lines.append(line)
            
    path.write_text("\n".join(new_lines) + "\n", encoding="utf-8")

def main() -> None:
    """递归处理目标目录下所有 Markdown 文件。"""
    root = get_target_root()
    for path in root.rglob("*.md"):
        replace_in_file(path)

if __name__ == "__main__":
    main()
```