import os
from pathlib import Path
import re

root = Path(__file__).resolve().parent

def replace_in_file(path: Path):
    txt = path.read_text(encoding="utf-8")
    new = txt

    # # 删除空行（包括连续空行）
    # new = re.sub(r'(?m)^\s*$\r?\n?', '', new)

    #删除所有粗体
    new = new.replace("**", "")  

    #修正选项
    new = re.sub(r'\\mathrm{([A-D])[\.．]}', r'\1', new)
    new = re.sub(r'\$\\mathrm{([A-D])[\.．]}', r'\1.$', new)

    # 行间公式变为行内公式
    new = re.sub(r"\$\$\n([\s\S]*?)\n\$\$", r"&!\1&!", new)
    new = re.sub(r"(?m)^\$\n([\s\S]*?)\n\$", r"&!\1&!", new)
    new = new.replace("&!", "$")
    new = new.replace("$$", "$")

    # 在选项前添加换行符（如果前面没有换行符的话）
    new = re.sub(r'^([A-D].*?)(?<!\n)([A-D][\.．])', r'\1\n\2', new , flags=re.MULTILINE)
    new = re.sub(r'^([A-D].*?)(?<!\n)([A-D][\.．])', r'\1\n\2', new , flags=re.MULTILINE)
    new = re.sub(r'^([A-D].*?)(?<!\n)([A-D][\.．])', r'\1\n\2', new , flags=re.MULTILINE)
    new = re.sub(r'^([A-D].*?)(?<!\n)([A-D][\.．])', r'\1\n\2', new , flags=re.MULTILINE)
    
    #修正常见识别错误
    new = new.replace("$^{A,B,C}$", "${A,B,C}$")
    new = new.replace(r"\int_{\mathbb{R}}", r"\complement_{\mathbb{R}}")
    new = new.replace(r"\overset{⃑}", r"\overrightarrow")
    new = new.replace(r"\overset{→}", r"\overrightarrow")    
    # 填空题修正：下划线
    new = new.replace(r"$\qquad$", r"$\underline{\hspace{2cm}}$")

#教科书格式修正
    # 删除教科书特殊标题前的图片链接和空行，添加特殊标记
    new = re.sub(
        r'(?m)^[ \t]*!\[[^\]]*\]\([^\)\n]+\)[ \t]*(?:\r?\n)+(?=^[ \t]*#\s*(?:探究|思考|观察|复习巩固|综合运用|拓广探索)\b)',
        '',
        new,
        )
    new = re.sub(r'(?m)^#\s+探究\b', r'> [!explore] 探究', new)
    new = re.sub(r'(?m)^#\s+思考\b', r'> [!think] 思考', new)
    new = re.sub(r'(?m)^#\s+观察\b', r'> [!observe] 观察', new)
    new = re.sub(r'(?m)^#\s+归纳\b', r'> [!tip] 归纳', new) 
    new = re.sub(r'(?m)^#\s+复习巩固\b', r'### 复习巩固', new)
    new = re.sub(r'(?m)^#\s+综合运用\b', r'### 综合运用', new)
    new = re.sub(r'(?m)^#\s+拓广探索\b', r'### 拓广探索', new)
    new = re.sub(r'(?m)^(例\d+.*)$', r'> [!example]- \1', new)
    new = re.sub(r'(?m)^(例 \d+\b.*)$', r'> [!example]- \1', new)    

    # 删除特殊标记后面的空行
    new = re.sub(r'(?m)^(> \[!(?:explore|think|observe)\] (?:探究|思考|观察))[ \t]*\r?\n[ \t]*\r?\n', r'\1\n', new)
    new = re.sub(r'(?m)[ \t]*\r?\n[ \t]*\r?\n(?=(?:解|分析|方法|作法)[^\r\n]*$)', r'\n', new)
    new = re.sub(r'(?m)[ \t]*\r?\n[ \t]*\r?\n(?=[（(]\d+[）)][^\r\n]*$)', r'\n', new)
    new = re.sub(r'(?m)(；)[ \t]*\r?\n[ \t]*\r?\n', r'\1\n', new)
    new = re.sub(r'(?m)^(解[^\r\n]*)[ \t]*\r?\n[ \t]*\r?\n(?=(?:\|)|(?:!\[[^\]]*\]\()|(?:<center><img\b))', r'\1\n', new)
    
    # 更改标题层级：如果章节标题后直接或间隔空行接着另一个 # 标题，则合并为同一行
    new = re.sub(r'(?m)^(#\s+第[一二三四五六七八九十百]+章[^\r\n]*)\s*\r?\n\s*#\s+', r'\1 ', new)
    # 特定章节修正（保留占位以防需要扩展）
    
    new = re.sub(r'(?m)^#\s+([（(]\d+[）)].*)$', r'\1', new)
    new = re.sub(r'(?m)^#\s+(\d+[\.．]\s*)', r'#### \1', new)
    new = re.sub(r'(?m)^#\s+(习题\d+(?:\.\d+)*)', r'## \1', new)
    new = re.sub(r'(?m)^#+\s+(\d+\.\d+\.\d+\b.*)$', r'### \1', new)
    new = re.sub(r'(?m)^#+\s+(\d+\.\d+\b(?!\.\d).*)$', r'## \1', new)
    new = re.sub(r'(?m)^#\s+阅读与思考\b', r'## 阅读与思考', new)
    new = re.sub(r'(?m)^(## 阅读与思考)\s*\r?\n\s*#\s+', r'\1\n### ', new)
    new = re.sub(r'(?m)^#\s+探究与发现\b', r'## 探究与发现', new)
    new = re.sub(r'(?m)^(## 探究与发现)\s*\r?\n\s*#\s+', r'\1\n### ', new)    
    new = re.sub(r'(?m)^#\s+练习\b', r'#### 练习', new)
    new = re.sub(r'(?m)^#\s+复习参考题\s*(\d*)\b', r'## 复习参考题\1', new)
    new = re.sub(r'(?m)^#\s+小结\b', r'## 小结', new)
    new = re.sub(r'(?m)^#\s+([一二三四五六七八九十]+、)', r'### \1', new)
    new = re.sub(r'(?m)^#\s+（([一二三四五六七八九十]+)）', r'### （\1）', new)

    # 修正图像和题注被误识别为标题
    new = re.sub(r'(?m)^[ \t]*#\s*(!\[[^\]]*\]\([^\)\n]+\))[ \t]*$', r'\1', new)
    new = re.sub(r'(?m)^[ \t]*#\s*(图\s*\d+(?:\.\d+)*(?:-\d+)?)[ \t]*$', r'\1', new)
    new = re.sub(r'(?m)^[ \t]*#\s*([（(][^）)\r\n]+[）)])[ \t]*$', r'\1', new)

    def fix_misordered_image_caption_blocks(text):
        image_re = re.compile(r'^[ \t]*!\[[^\]]*\]\(([^)\r\n]+)\)[ \t]*$')
        caption_re = re.compile(
            r'^[ \t]*(?:图\s*\d+(?:\.\d+)*(?:-\d+)?|[（(][^）)\r\n]+[）)])[ \t]*$'
        )
        blank_re = re.compile(r'^[ \t]*$')
        lines = text.splitlines(True)
        out = []
        i = 0
        while i < len(lines):
            if image_re.match(lines[i]):
                imgs = []
                block_lines = []
                while i < len(lines) and (image_re.match(lines[i]) or blank_re.match(lines[i])):
                    if image_re.match(lines[i]):
                        imgs.append(image_re.match(lines[i]).group(1))
                    block_lines.append(lines[i])
                    i += 1
                while i < len(lines) and blank_re.match(lines[i]):
                    block_lines.append(lines[i])
                    i += 1
                caps = []
                cap_lines = []
                while i < len(lines) and caption_re.match(lines[i]):
                    caps.append(caption_re.match(lines[i]).group(0).strip())
                    cap_lines.append(lines[i])
                    i += 1
                if len(imgs) >= 2 and len(imgs) == len(caps):
                    table = [
                        '> <center>',
                        '> ',
                        '| ' + ' | '.join(f'![]({img})' for img in imgs) + ' |',
                        '| ' + ' | '.join(['---'] * len(imgs)) + ' |',
                        '| ' + ' | '.join(caps) + ' |',
                        '> </center>'
                    ]
                    out.append('\n'.join(table) + '\n')
                    continue
                out.extend(block_lines)
                out.extend(cap_lines)
                continue
            out.append(lines[i])
            i += 1
        return ''.join(out)

    new = fix_misordered_image_caption_blocks(new)

    #图片格式修正
    def convert_labeled_figure_table(match):
        content = match.group(0)
        pairs = re.findall(
            r'!\[[^\]]*\]\(([^)\n]+)\)[ \t]*(?:\r?\n)+[ \t]*[（(]\s*(\d+)\s*[）)]([^\r\n]*)',
            content,
        )
        caption_match = re.search(
            r'(?m)^[ \t]*((?:图\s*\d+(?:\.\d+)*(?:-\d+)?)|(?:[（(]第\s*\d+\s*题[）)]))[ \t]*$',
            content,
        )

        if len(pairs) < 2:
            return content

        image_cells = [f'![]({img})' for img, _, _ in pairs]
        label_cells = [f'（{num}）{suffix.strip()}'.strip() for _, num, suffix in pairs]
        table = [
            '> <center>',
            '> ',
            '> | ' + ' | '.join(image_cells) + ' |',
            '> | ' + ' | '.join(['---'] * len(image_cells)) + ' |',
            '> | ' + ' | '.join(label_cells) + ' |',
            '> </center>'
        ]
        if caption_match:
            table.append(f'> <center>{caption_match.group(1)}</center>')
            table.append('> ')
            return '\n'.join(table) + '\n'
        return '\n'.join(table) + '\n'

    labeled_figure_table_pattern = re.compile(
        r'(?m)'
        r'(?:'
        r'^[ \t]*!\[[^\]]*\]\([^\)\n]+\)[ \t]*(?:\r?\n)+'
        r'[ \t]*[（(]\s*\d+\s*[）)][^\r\n]*(?:[ \t]*\r?\n)+'
        r'){2,}'
        r'(?:^[ \t]*(?:图\s*\d+(?:\.\d+)*(?:-\d+)?|[（(]第\s*\d+\s*题[）)])[ \t]*$)?'
    )
    new = labeled_figure_table_pattern.sub(convert_labeled_figure_table, new)
    
    # 删除图片转换后前面的空行（只删除前面的，不删除后面的）
    new = re.sub(r'(?m)(?:\r?\n[ \t]*)+(?=> (?:\||<center>))', '\n', new)

    def convert_plain_figure_table(match):
        content = match.group(0)
        imgs = re.findall(r'!\[[^\]]*\]\(([^)\n]+)\)', content)
        caption_match = re.search(
            r'(?m)^[ \t]*图\s*(\d+(?:\.\d+)*(?:-\d+)?)[ \t]*$',
            content,
        )

        if len(imgs) < 2 or not caption_match:
            return content

        image_cells = [f'![]({img})' for img in imgs]
        table = [
            '> <center>',
            '> ',  
            '> | ' + ' | '.join(image_cells) + ' |',
            '> | ' + ' | '.join(['---'] * len(image_cells)) + ' |',
            '> </center>',
            f'> <center>图{caption_match.group(1)}</center>',
            '> '
        ]
        return '\n'.join(table) + '\n'

    plain_figure_table_pattern = re.compile(
        r'(?m)'
        r'(?:^[ \t]*!\[[^\]]*\]\([^\)\n]+\)[ \t]*(?:[ \t]*\r?\n)+){2,}'
        r'^[ \t]*图\s*\d+(?:\.\d+)*(?:-\d+)?[ \t]*$'
    )
    new = plain_figure_table_pattern.sub(convert_plain_figure_table, new)
    
    # 删除图片转换后前面的空行（只删除前面的，不删除后面的）
    new = re.sub(r'(?m)(?:\r?\n[ \t]*)+(?=> (?:\||<center>))', '\n', new)

     # 如果 <center> 图标题被错误地粘在表格最后一行，拆成单独一段
    new = re.sub(
        r'(?m)^(?P<prefix>>[ \t]*)(?P<row>\|[^\n]*\|)\s*(?P<center><center>(?:图|ͼ)\d+(?:\.\d+)*(?:-\d+)?</center>)\s*$',
        lambda m: f"{m.group('prefix')}{m.group('row')}\n\n{m.group('prefix')}{m.group('center')}",
        new,
    )

    def convert_single_figure_markdown(match):
        img = match.group(1)
        figure_num = match.group(2)
        question_num = match.group(3)
        caption = f'图{figure_num}' if figure_num else f'（第{question_num}题）'
        return '\n'.join([
            f'<center><img src="{img}" style="max-width:100%;"></center>',
            f'<center>{caption}</center>',
        ])

    single_figure_markdown_pattern = re.compile(
        r'(?m)'
        r'^[ \t]*!\[[^\]]*\]\(([^)\n]+)\)[ \t]*(?:\r?\n)+'
        r'[ \t]*(?:图\s*(\d+(?:\.\d+)*(?:-\d+)?)|[（(]第\s*(\d+)\s*题[）)])[ \t]*$'
    )
    new = single_figure_markdown_pattern.sub(convert_single_figure_markdown, new)
    

    # 删除以特定中文词语开头的行前面的空行
    new = re.sub(r'(?m)(?:\r?\n[ \t]*)+(?=(?:所以|因为|因此|当|显然|如果|由|事实上|同理|即|同理可得|又|证明|设|又|消去|这就是说|另一方面|于是|从而|进而|同样))', '\n', new)
    
    # 删除图片转换后前面的空行（只删除前面的，不删除后面的）
    new = re.sub(r'(?m)(?:\r?\n[ \t]*)+(?=<center><img)', '\n', new)

    # 删除 $ 开头的行前面的空行
    new = re.sub(r'(?m)(?:\r?\n[ \t]*)+(?=\$)', '\n', new)

    # 在 </center> 后面增加空行
    new = re.sub(r'</center>(?!\n)', '</center>\n', new)



    # 删除以 > [!example]- 开头的行后面的空行
    new = re.sub(r'(?m)^(> \[!example\]-[^\n]*)(\n[ \t]*\n)', r'\1\n', new)

    # 不要以 <center> 开头的行，将它们前面的换行符删除
    new = re.sub(r'(?:\r?\n[ \t]*)+(?=<center>)', '', new)

    # 删除连续的空行，保留单个空行
    while '\n\n\n' in new:
        new = new.replace('\n\n\n', '\n\n')
    if new != txt:
        path.write_text(new, encoding="utf-8")
        print(f"Updated {path}")

    # 将 </center> 后面跟 > 的改为只有 </center>
    new = re.sub(r'</center>\n>', '</center>', new) 

   

def main():
    for p in root.rglob("*.md"):
        try:
            replace_in_file(p)
        except Exception as e:
            print(f"Error {p}: {e}")

if __name__ == "__main__":
    main()

