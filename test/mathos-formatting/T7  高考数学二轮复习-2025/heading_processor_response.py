```python
import os
from pathlib import Path
import re

# 权威目录标题与其预期层级的映射（1=H1, 2=H2, 3=H3）
# 注意：键必须是目录中的标题去除末尾页码和导引符（如“…… 1”、“ /2”）后的干净文本。必须原样保留标题开头的章节号和序号前缀（如“第一章”、“1”、“2”、“1.1”等），绝对不能将其剥离或删除！
TOC_HEADINGS: dict[str, int] = {
    "第一章 立体几何": 1,
    "第一节 空间角与射影": 2,
    "一. 射影面积定理": 3,
    "二. 三正弦定理与最大角问题": 3,
    "三. 三余弦定理": 3,
    "四. 空间余弦定理": 3,
    "第二节 静态分析": 2,
    "一. 二面角": 3,
    "二. 异面直线距离": 3,
    "三. 空间体顶点支撑": 3,
    "第三节 动态分析": 2,
    "一. 平面几何构型": 3,
    "二. 单参数变换": 3,
    "三. 多参数变换": 3,
    "四. 动态射影与翻折问题": 3,
    "第四节 球的几何学": 2,
    "一. 外接球": 3,
    "二. 内切球": 3,
    "三. 棱接球": 3,
    "第二章 数列": 1,
    "第一节 基础定义与数列外扩内容": 2,
    "一. 映射与函数": 3,
    "二. 数列的极限": 3,
    "第二节 蛛网图、不动点定理与数列不动点的应用": 2,
    "一. 数列递推生成函数与数列迭代": 3,
    "二. 数列迭代与蛛网图产生": 3,
    "三. 蛛网图的分类": 3,
    "四. 数列不动点定理": 3,
    "五. 数列不动点与数列单调性和极限": 3,
    "六. 利用一阶递推数列不动点求通项公式": 3,
    "第三节 数列与差分方程": 2,
    "一. 差分定义": 3,
    "二. 数列递推与差分方程": 3,
    "三. 阶常系数线性齐次差分方程": 3,
    "四. 阶常系数非齐次线性差分方程": 3,
    "第四节 特殊求和法与特殊求和题型": 2,
    "一. 特殊求和法": 3,
    "二. 插项、重排、公共项": 3,
    "第五节 Fibonacci斐波那契数列": 2,
    "一. Fibonacci数列的基本概念": 3,
    "二. Fibonacci数列的性质与黄金分割率": 3,
    "三. 杨辉三角形": 3,
    "第六节 判定数列放缩目标": 2,
    "一. 数列放缩基本观点": 3,
    "二. 数列放缩可依赖目标": 3,
    "第七节 数列放缩手段": 2,
    "一. 数列放缩的证明方法": 3,
    "二. 生成不等式": 3,
    "三. 递推公式与不动点性质": 3,
    "四. 改良放缩精度": 3,
    "第八节 数列放缩类型": 2,
    "一. 通项放缩型": 3,
    "二. 求和放缩型": 3,
    "第九节 数列新定义": 2,
    "第三章 统计": 1,
    "第一节 描述性统计": 2,
    "一. 样本与总体": 3,
    "二. 位置指标": 3,
    "三. 变异性指标": 3,
    "四. 分布形状、相对位置和异常值检测的测量指标": 3,
    "五. 离散度量、五数概括和箱线图": 3,
    "六. 双变量关联性指标": 3,
    "第二节 区间估计（σ已知）": 2,
    "一. 显著性水平": 3,
    "二. 置信水平": 3,
    "三. 误差幅度\\*": 3,
    "四. 区间估计\\*": 3,
    "第三节 拟合优度检验、独立性检验和多重比例检验": 2,
    "一. 零假设和备择假设\\*": 3,
    "二. 类型Ⅰ和类型Ⅱ错误": 3,
    "三. 卡方分布与卡方检验": 3,
    "四. 拟合度检验": 3,
    "五. 独立性检验": 3,
    "六. 多重比例检验\\*": 3,
    "第四节 简单线性回归": 2,
    "一. 简单线性回归模型": 3,
    "二. 残差": 3,
    "三. 最小二乘法": 3,
    "四. 决定系数": 3,
    "五. 一元非线性回归模型\\*": 3,
    "第四章 概率": 1,
    "第一节 离散概率分布": 2,
    "一. 随机变量": 3,
    "二. 概率质量函数": 3,
    "三. 离散概率分布": 3,
    "四. 双变量经验离散概率分布\\*": 3,
    "五. 二项分布": 3,
    "六. 泊松分布\\*": 3,
    "七. 超几何分布": 3,
    "第二节 连续概率分布": 2,
    "一. 均匀概率分布": 3,
    "二. 正态分布": 3,
    "三. 指数分布\\*": 3,
    "第三节 基于动态规划的递推问题": 2,
    "一. 动态规划的定义": 3,
    "二. 马尔科夫链的动态规划": 3,
    "三. 一维对称随机游走模型": 3,
    "四. 非对称随机游走": 3,
    "第五章 圆锥曲线": 1,
    "第一节 选填题专题一": 2,
    "一. 圆锥曲线三定义": 3,
    "二. 焦半径与焦点弦": 3,
    "三. 焦点三角形与性质": 3,
    "四. 中点与切线综合": 3,
    "五. 渐近线的综合问题": 3,
    "二. 离心率问题": 3,
    "三. 圆锥曲线相关圆": 3,
    "四. 新定义曲线问题": 3,
    "第二节 解答题方法专题": 2,
    "一. 常规联立的优化方法": 3,
    "二. 齐次化与仿新齐次化": 3,
    "三. 点坐标的曲线变换法": 3,
    "四. 参数方程与三角代换生成两点式": 3,
    "五. 定比点差与对偶式的调整法": 3,
    "六. 基底化向量": 3,
    "第四节 部分射影几何学背景": 2,
    "一. 拓广元素、射影变换与射影不变量": 3,
    "二. 调和集、完全四点形、极点极线与自极三角形": 3,
    "三. 二次曲线的射影性质": 3,
    "四. 特殊情况下的射影变换-对合变换": 3,
    "第六章 导数": 1,
    "第一节 不等式体系搭建": 2,
    "一. 切线不等式": 3,
    "二. 利用积分推导任意精度不等式": 3,
    "三. 复合函数类-代数变形（取等不变）": 3,
    "四. 利用复合函数改变不等式取等": 3,
    "五. 利用分式的性质构造多取等不等式": 3,
    "第二节 极值点的判定": 2,
    "一. 极值点在导数阶位上的循环与传递规律": 3,
    "二. 命题“是函数极值点”的证明问题": 3,
    "三. 命题“是函数极值点”的加参问题": 3,
    "第三节 不等式证明": 2,
    "一. 不等式之间的关系": 3,
    "二. 不等式证明的基本方法": 3,
    "第四节 动态分析与含参不等式恒成立问题": 2,
    "三. 公切取等判定与加参原理": 3,
    "四. 取等类型": 3,
    "五. 参数对函数的影响——主元定界原理": 3,
    "六. 函数定点与消参": 3,
    "七. 参数对取等点的影响——取等点的性质、取等点与参数边界值": 3,
    "八. 动态分析的步骤": 3,
    "九. 动态分析进阶——函数特殊行为命题": 3,
    "十. 指数化结构的恒成立问题（超越取等）": 3,
    "十一. 主元含参恒成立问题": 3,
    "十二. 动态参数主元分界点的恒成立问题": 3,
    "第五节 动态分析与零点问题": 2,
    "一. 零点问题基础动态分析": 3,
    "二. 零点问题进阶动态分析——复合函数结构下的伸缩变换": 3,
    "第六节 多元问题与消元": 2,
    "一.“三元”相切取等问题的消元——零点比大小、双参和积类问题": 3,
    "二. 不含参相异函数各点关系": 3,
    "三. 含参相异函数各点关系": 3,
    "第七节 偏移问题": 2,
    "一. 命题与变量内在逻辑": 3,
    "二. 偏移命题分类": 3,
    "三. 调整变量分离结构解决偏移问题": 3,
    "四. 调整变量分离结构的速率控制": 3,
    "五. 调整变量分离结构的书写过程": 3,
    "六. 高精度偏移问题调整方式": 3,
    "七. 网红方法“二次拟合”的局限性": 3,
    "八. 双参偏移问题调整方式": 3,
    "九. 和积变量分离结构的共同之处与等价命题调整法": 3,
    "十. 柯西加权的偏移问题": 3,
    "十一. 对称构造处理偏移问题": 3,
    "十二. 对称构造处与调整的结合-构造反偏函数": 3,
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