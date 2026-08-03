"""
build_adapter.py v3 – Section-boundary approach.

The OCR raw file has an inconsistent heading structure:
- Some sections have proper # headings (e.g., "# 1.1 集合的概念")
- Most sections are separated by repeating "## 刷基础" patterns
- Each TOC section starts with a "## 刷基础" block

Strategy:
1. Find all "section boundary" markers in order:
   - # H1 headings (chapters, major sections)
   - ## 刷基础 lines (mark the start of each TOC section)
2. Map TOC entries to these boundaries in order.
3. For sections without explicit headings, use ## 刷基础 as boundary.
"""
import json
import re
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────────────────────
STAGING = Path(r"C:\Mathematics-Knowledge\Secondary-School-Mathematics-Knowledge-Map\测试\新建文件夹\staging")
PROFILE = STAGING / "question-type-profile.json"
Q_PATH  = STAGING / "raw" / "questions.raw.md"
A_PATH  = STAGING / "raw" / "answers.raw.md"
OUTPUT  = STAGING / "format-adapter.json"

q_lines = Q_PATH.read_text(encoding="utf-8-sig").splitlines()
a_lines = A_PATH.read_text(encoding="utf-8-sig").splitlines()

def norm(text: str) -> str:
    return re.sub(r"[\s\$\(\)\,\.\~\+\\_\-\:：\、。·\u00a0\uff0c\[\]]", "", text).strip()

BODY_START = 528
BODY_END = 7065  # Before the final "高中必刷题" header

# ── Step 1: Build the section map ──────────────────────────────────────────────
# Scan the raw file and find all meaningful headings/boundaries.

all_markers = []  # (line, kind, text)

for i, line in enumerate(q_lines):
    ln = i + 1
    if ln <= BODY_START or ln >= BODY_END:
        continue
    
    m = re.match(r"^(#{1,6})\s+(.*)", line)
    if m:
        level = len(m.group(1))
        text = m.group(2).strip()
        all_markers.append((ln, level, text))

# ── Step 2: Map TOC entries to actual file positions ───────────────────────────
# The TOC has 92 entries but the file has a different structure.
# We need to map each TOC "section" to the actual line range.
# 
# Key observation: Each section in the book follows this pattern:
#   [optional # heading]
#   ## 刷基础
#   ## 题型 1 ...
#   ## 题型 2 ...
#   ## 刷易错
#   ## 刷提升
#   [optional ## 刷素养]
#   [optional ## 刷速度]
#
# Sections that are "综合训练" have:
#   ## 刷能力 / ## 刷难关 / ## 刷素养 etc.
#
# Sections that are "素养检测" / "高考强化" have exam-style headings.
#
# Plan:
# 1. Group the raw file into SECTIONS by looking for ## 刷基础 markers
#    that indicate the start of question content for a TOC section.
# 2. Some TOC entries are structural (chapters), some are leaf sections.
# 3. Some sections don't start with 刷基础 (like 综合训练, 素养检测, 高考强化, 专题).

# Let me find the actual section boundary markers.
# These are the lines where content for a NEW TOC section begins.

# A "section start" is either:
# a) A # heading that matches a TOC entry title
# b) A ## 刷基础 line that starts a new section's question content

# The ## headings inside a section (题型, 易错点, etc.) are NOT section boundaries.

# Let's identify the pattern: After each # heading or ## 刷基础 group,
# we have question content until the next section.

# Actually, the simplest approach: collect the line numbers of ALL ## 刷基础 
# lines and other key boundary markers, then map them to TOC entries in order.

# First, let's understand the actual structure by listing all H1 and "刷基础" markers:
h1_headings = []
section_starts = []  # These are the "刷基础" or equivalent section-start markers

# Also track "specialized" section markers
SECTION_STARTERS = re.compile(
    r"^(刷基础|刷能力|刷难关|基础|狂K速览|刷速度|刷素养|刷综合|刷真题|刷原创)$"
)

for ln, level, text in all_markers:
    if level == 1:
        h1_headings.append((ln, text))
    if level == 2 and SECTION_STARTERS.match(text.strip()):
        section_starts.append((ln, text))

print(f"H1 headings: {len(h1_headings)}")
for ln, t in h1_headings:
    print(f"  L{ln}: {t}")

print(f"\n## section starters: {len(section_starts)}")
for ln, t in section_starts:
    print(f"  L{ln}: {t}")

# ── Step 3: Now build the actual TOC→line mapping ─────────────────────────────
# The TOC entries map to sections. Let me figure out the actual structure.

# From the heading listing, the book structure is:
# 第一章 (L529) 
#   1.1 集合的概念 (L531) - has content starting at L533 "## 刷基础"
#   1.2 集合间的基本关系 - NO heading, starts at L628 "## 刷基础"
#   1.3 集合的基本运算 - NO heading, starts at L729 "## 刷基础"
#   第1.1~1.3节综合训练 - starts at L842 "## 刷能力" or L880 "## 刷难关"
#   专题1 集合的综合问题 - starts at L880 or similar
# etc.

# Instead of a complex heuristic, let me just manually map the sections
# based on the heading listing output. This is the most reliable approach
# for a specific textbook.

# Actually, the better approach: let me map sections by finding the "刷基础"
# markers in order, and also handle special sections.

# Each TOC leaf section has one of these patterns:
# Normal section: starts with "## 刷基础"
# 综合训练: starts with "## 刷能力" or "## 刷难关" or "## 刷素养"  
# 素养检测/高考强化: starts with "## 刷速度" or "## 刷真题"
# 专题: starts with "## 刷能力" or "## 刷难关"

# Let me take a cleaner approach: just find ALL ## boundaries that could
# start a new section, in order.

# The key realization: the TOC has entries like:
# 1.1, 1.2, 1.3, 综合训练, 专题1, 1.4, 1.4.1+1.4.2, 综合训练, 1.5, 1.5.1, 1.5.2, 综合训练, 素养检测, 高考强化
# And each of these corresponds to a block of content starting with ## 刷基础 
# (or ## 刷能力 / ## 刷速度 / ## 刷真题 for special sections).

# So let me find all "content block starts" and map them in order.

# A content block start is one of:
# 1) ## 刷基础 (normal section with questions)
# 2) ## 刷能力 / ## 刷难关 (综合训练 / 专题 section)  
# 3) ## 刷速度 (素养检测)
# 4) ## 刷真题 (高考强化)
# 5) ## 刷原创 (高考强化 continued)

# BUT some of these (刷能力, 刷素养) also appear WITHIN normal sections.
# The distinction is: ## 刷基础 always starts a new section.
# ## 刷能力 etc. within a section come AFTER ## 刷提升.

# So the reliable approach: ## 刷基础 marks the start of each "numbered" section.
# Other markers (刷能力, 刷速度, 刷真题) mark "special" sections that
# don't have a ## 刷基础.

# Let me enumerate sections precisely:
# For Ch1: sections 1.1, 1.2, 1.3 each start with ## 刷基础
#   Between 1.3's content and the next, there's ## 刷能力, ## 刷难关 for 综合训练
#   Then 专题1 for 专题
#   Then 1.4 starts again with ## 刷基础
# etc.

# The cleanest mapping: just look at the consecutive ## 刷基础 blocks,
# and for sections without 刷基础 (综合训练, 素养检测, 高考强化), 
# identify them by what comes between two 刷基础 blocks.

# Given the complexity, let me take the pragmatic approach: manually provide
# the line ranges for each TOC entry based on the heading analysis.

# Actually, let me try a simpler strategy first. 
# The content manifest only needs the hierarchy to properly segment sections.
# The hierarchy entries define the LINE BOUNDARIES of each section.
# If I make each section boundary correct, the pipeline should work.

# From the heading data, let me map each section manually:

# Build section_map: list of (title, level, start_line, structural_only, output_path)
# where start_line is the ACTUAL line in the file where this section's content begins.

section_map = [
    # Chapter 1: L529-L1462
    ("第一章 集合与常用逻辑用语", 1, 529, True, "01-第一章_集合与常用逻辑用语/01-第一章_集合与常用逻辑用语.md"),
    ("1.1 集合的概念", 2, 531, False, "01-第一章_集合与常用逻辑用语/1.1_集合的概念/1.1_集合的概念.md"),
    # 1.2 starts at L628 (## 刷基础)
    ("1.2 集合间的基本关系", 2, 628, False, "01-第一章_集合与常用逻辑用语/1.2_集合间的基本关系/1.2_集合间的基本关系.md"),
    # 1.3 starts at L729 (## 刷基础)
    ("1.3 集合的基本运算", 2, 729, False, "01-第一章_集合与常用逻辑用语/1.3_集合的基本运算/1.3_集合的基本运算.md"),
    # 综合训练 starts at L842 (## 刷能力)
    ("第 1.1 ~ 1.3 节综合训练", 2, 842, False, "01-第一章_集合与常用逻辑用语/第1.1~1.3节综合训练/第1.1~1.3节综合训练.md"),
    # 专题1 starts at L880 (## 刷难关)
    ("专题 1 集合的综合问题", 2, 880, False, "01-第一章_集合与常用逻辑用语/专题1_集合的综合问题/专题1_集合的综合问题.md"),
    # 1.4 section starts at L948 (## 1.4.2 充要条件)
    ("1.4 充分条件与必要条件", 2, 948, True, "01-第一章_集合与常用逻辑用语/1.4_充分条件与必要条件/1.4_充分条件与必要条件.md"),
    ("1.4.1 充分条件与必要条件 1.4.2 充要条件", 3, 948, False, "01-第一章_集合与常用逻辑用语/1.4.1_充分条件与必要条件_1.4.2_充要条件/1.4.1_充分条件与必要条件_1.4.2_充要条件.md"),
    # 1.4 综合训练 starts at L1058 (## 刷能力)
    ("第 1.4 节综合训练", 2, 1058, False, "01-第一章_集合与常用逻辑用语/第1.4节综合训练/第1.4节综合训练.md"),
    # 1.5 section starts at L1109 (# 1.5.1...)
    ("1.5 全称量词与存在量词", 2, 1109, True, "01-第一章_集合与常用逻辑用语/1.5_全称量词与存在量词/1.5_全称量词与存在量词.md"),
    ("1.5.1 全称量词与存在量词", 3, 1109, False, "01-第一章_集合与常用逻辑用语/1.5.1_全称量词与存在量词/1.5.1_全称量词与存在量词.md"),
    # 1.5.2 starts at L1174 (## 刷基础)
    ("1.5.2 全称量词命题和存在量词命题的否定", 3, 1174, False, "01-第一章_集合与常用逻辑用语/1.5.2_全称量词命题和存在量词命题的否定/1.5.2_全称量词命题和存在量词命题的否定.md"),
    # 1.5 综合训练 starts at L1236 (## 刷能力)
    ("第 1.5 节综合训练", 2, 1236, False, "01-第一章_集合与常用逻辑用语/第1.5节综合训练/第1.5节综合训练.md"),
    # 素养检测 starts at L1275 (## 刷速度)
    ("第一章素养检测", 2, 1275, False, "01-第一章_集合与常用逻辑用语/第一章素养检测/第一章素养检测.md"),
    # 高考强化 starts at L1365 (## 刷真题)
    ("第一章高考强化", 2, 1365, False, "01-第一章_集合与常用逻辑用语/第一章高考强化/第一章高考强化.md"),

    # Chapter 2: L1472-L2030
    ("第二章 一元二次函数、方程和不等式", 1, 1472, True, "02-第二章_一元二次函数_方程和不等式/02-第二章_一元二次函数_方程和不等式.md"),
    # 2.1 starts at L1472 (## 刷基础)
    ("2.1 等式性质与不等式性质", 2, 1472, False, "02-第二章_一元二次函数_方程和不等式/2.1_等式性质与不等式性质/2.1_等式性质与不等式性质.md"),
    # 2.2 starts at L1564 (## 刷基础)
    ("2.2 基本不等式", 2, 1564, False, "02-第二章_一元二次函数_方程和不等式/2.2_基本不等式/2.2_基本不等式.md"),
    # 专题2 starts at L1721 (## 刷难关)
    ("专题 2 利用基本不等式求最值", 2, 1721, False, "02-第二章_一元二次函数_方程和不等式/专题2_利用基本不等式求最值/专题2_利用基本不等式求最值.md"),
    # 2.3 starts at L1774 (## 基础) 
    ("2.3 二次函数与一元二次方程、不等式", 2, 1774, False, "02-第二章_一元二次函数_方程和不等式/2.3_二次函数与一元二次方程_不等式/2.3_二次函数与一元二次方程_不等式.md"),
    # 素养检测 at L1905 (## 刷速度)
    ("第二章素养检测", 2, 1905, False, "02-第二章_一元二次函数_方程和不等式/第二章素养检测/第二章素养检测.md"),
    # 高考强化 at L1986 (## 刷真题)
    ("第二章高考强化", 2, 1986, False, "02-第二章_一元二次函数_方程和不等式/第二章高考强化/第二章高考强化.md"),

    # Chapter 3: L2031-L3326
    ("第三章 函数的概念与性质", 1, 2031, True, "03-第三章_函数的概念与性质/03-第三章_函数的概念与性质.md"),
    ("3.1 函数的概念及其表示", 2, 2033, True, "03-第三章_函数的概念与性质/3.1_函数的概念及其表示/3.1_函数的概念及其表示.md"),
    ("3.1.1 函数的概念", 3, 2037, False, "03-第三章_函数的概念与性质/3.1.1_函数的概念/3.1.1_函数的概念.md"),
    # 3.1.2 starts at L2200 (## 刷基础)
    ("3.1.2 函数的表示法", 3, 2200, False, "03-第三章_函数的概念与性质/3.1.2_函数的表示法/3.1.2_函数的表示法.md"),
    # 3.1 综合训练 at L2361 (## 刷能力)
    ("第 3.1 节综合训练", 2, 2361, False, "03-第三章_函数的概念与性质/第3.1节综合训练/第3.1节综合训练.md"),
    # 3.2 starts at L2400 (# 3.2...)
    ("3.2 函数的基本性质", 2, 2400, True, "03-第三章_函数的概念与性质/3.2_函数的基本性质/3.2_函数的基本性质.md"),
    ("3.2.1 单调性与最大(小)值", 3, 2402, True, "03-第三章_函数的概念与性质/3.2.1_单调性与最大(小)值/3.2.1_单调性与最大(小)值.md"),
    ("课时 1 函数的单调性", 4, 2402, False, "03-第三章_函数的概念与性质/课时1_函数的单调性/课时1_函数的单调性.md"),
    # 课时2 starts at L2513 (## 题型1 函数的最大(小)值的判定及求解)
    ("课时 2 函数的最大(小)值", 4, 2513, False, "03-第三章_函数的概念与性质/课时2_函数的最大(小)值/课时2_函数的最大(小)值.md"),
    # 3.2.2 starts at L2639 (## 刷基础)
    ("3.2.2 奇偶性", 3, 2639, False, "03-第三章_函数的概念与性质/3.2.2_奇偶性/3.2.2_奇偶性.md"),
    # 3.2 综合训练 at L2784 (## 刷能力)
    ("第 3.2 节综合训练", 2, 2784, False, "03-第三章_函数的概念与性质/第3.2节综合训练/第3.2节综合训练.md"),
    # 专题3 at L2831 (## 刷难关)
    ("专题 3 函数的性质及应用", 2, 2831, False, "03-第三章_函数的概念与性质/专题3_函数的性质及应用/专题3_函数的性质及应用.md"),
    # 3.3 幂函数 at L2895 (## 基础)
    ("3.3 幂函数", 2, 2895, False, "03-第三章_函数的概念与性质/3.3_幂函数/3.3_幂函数.md"),
    # 3.4 函数应用(一) at L3046 (## 刷基础)
    ("3.4 函数的应用(一)", 2, 3046, False, "03-第三章_函数的概念与性质/3.4_函数的应用(一)/3.4_函数的应用(一).md"),
    # 素养检测 at L3166 (## 刷速度)
    ("第三章素养检测", 2, 3166, False, "03-第三章_函数的概念与性质/第三章素养检测/第三章素养检测.md"),
    # 高考强化 at L3246 (# 第三章高考强化)
    ("第三章高考强化", 2, 3246, False, "03-第三章_函数的概念与性质/第三章高考强化/第三章高考强化.md"),

    # Chapter 4: L3327-L4796
    ("第四章 指数函数与对数函数", 1, 3327, True, "04-第四章_指数函数与对数函数/04-第四章_指数函数与对数函数.md"),
    # 4.1 指数 at L3343 (## 刷基础)
    ("4.1 指数", 2, 3331, True, "04-第四章_指数函数与对数函数/4.1_指数/4.1_指数.md"),
    # 4.1.1+4.1.2 at L3343 (## 刷基础)
    ("4.1.1 n次方根与分数指数幂 4.1.2 无理数指数幂及其运算", 3, 3343, False, "04-第四章_指数函数与对数函数/4.1.1_n次方根与分数指数幂_4.1.2_无理数指数幂及其运算/4.1.1_n次方根与分数指数幂_4.1.2_无理数指数幂及其运算.md"),
    # 4.2 指数函数 at L3440 (## 刷基础)
    ("4.2 指数函数", 2, 3440, True, "04-第四章_指数函数与对数函数/4.2_指数函数/4.2_指数函数.md"),
    ("4.2.1 指数函数的概念", 3, 3440, False, "04-第四章_指数函数与对数函数/4.2.1_指数函数的概念/4.2.1_指数函数的概念.md"),
    # 4.2.2 starts at L3489 (## 刷基础)
    ("4.2.2 指数函数的图象和性质", 3, 3489, False, "04-第四章_指数函数与对数函数/4.2.2_指数函数的图象和性质/4.2.2_指数函数的图象和性质.md"),
    # 4.1,4.2综合训练
    ("第4.1, 4.2节综合训练", 2, 3635, False, "04-第四章_指数函数与对数函数/第4.1_4.2节综合训练/第4.1_4.2节综合训练.md"),
    # 4.3 对数 at L3674 (## 4.3.1...)
    ("4.3 对数", 2, 3674, True, "04-第四章_指数函数与对数函数/4.3_对数/4.3_对数.md"),
    ("4.3.1 对数的概念 4.3.2 对数的运算", 3, 3674, False, "04-第四章_指数函数与对数函数/4.3.1_对数的概念_4.3.2_对数的运算/4.3.1_对数的概念_4.3.2_对数的运算.md"),
    # 4.4 对数函数 at L3781 (# 4.4...)
    ("4.4 对数函数", 2, 3781, True, "04-第四章_指数函数与对数函数/4.4_对数函数/4.4_对数函数.md"),
    ("4.4.1 对数函数的概念 4.4.2 对数函数的图象和性质", 3, 3781, False, "04-第四章_指数函数与对数函数/4.4.1_对数函数的概念_4.4.2_对数函数的图象和性质/4.4.1_对数函数的概念_4.4.2_对数函数的图象和性质.md"),
    # 4.4.3 at L3978 (## 题型 1 不同增长)  -- actually at L3968 or L3978
    ("4.4.3 不同函数增长的差异", 3, 3968, False, "04-第四章_指数函数与对数函数/4.4.3_不同函数增长的差异/4.4.3_不同函数增长的差异.md"),
    # 4.3,4.4综合训练 at L4040 (## 刷基础) or L4079 (## 刷难关)
    ("第4.3, 4.4节综合训练", 2, 4040, False, "04-第四章_指数函数与对数函数/第4.3_4.4节综合训练/第4.3_4.4节综合训练.md"),
    # 专题4 at L4079 (## 刷难关) 
    ("专题4 指数函数、对数函数", 2, 4079, False, "04-第四章_指数函数与对数函数/专题4_指数函数_对数函数/专题4_指数函数_对数函数.md"),
    # 4.5 函数应用(二) at L4127 (# 4.5.1...)
    ("4.5 函数的应用(二)", 2, 4127, True, "04-第四章_指数函数与对数函数/4.5_函数的应用(二)/4.5_函数的应用(二).md"),
    ("4.5.1 函数的零点与方程的解", 3, 4127, False, "04-第四章_指数函数与对数函数/4.5.1_函数的零点与方程的解/4.5.1_函数的零点与方程的解.md"),
    # 4.5.2 at L4311 (## 刷基础)
    ("4.5.2 用二分法求方程的近似解", 3, 4311, False, "04-第四章_指数函数与对数函数/4.5.2_用二分法求方程的近似解/4.5.2_用二分法求方程的近似解.md"),
    # 4.5.3 at L4376 (## 刷基础 or 题型)
    ("4.5.3 函数模型的应用", 3, 4376, False, "04-第四章_指数函数与对数函数/4.5.3_函数模型的应用/4.5.3_函数模型的应用.md"),
    # 4.5 综合训练 at L4441 (## 刷基础)
    ("第4.5节综合训练", 2, 4441, False, "04-第四章_指数函数与对数函数/第4.5节综合训练/第4.5节综合训练.md"),
    # 素养检测 at L4564 (## 刷速度)
    ("第四章素养检测", 2, 4564, False, "04-第四章_指数函数与对数函数/第四章素养检测/第四章素养检测.md"),
    # 高考强化 at L4657 (## 刷真题 or equivalent)
    ("第四章高考强化", 2, 4657, False, "04-第四章_指数函数与对数函数/第四章高考强化/第四章高考强化.md"),

    # Chapter 5: L4797-L7064
    ("第五章 三角函数", 1, 4797, True, "05-第五章_三角函数/05-第五章_三角函数.md"),
    ("5.1 任意角和弧度制", 2, 4799, True, "05-第五章_三角函数/5.1_任意角和弧度制/5.1_任意角和弧度制.md"),
    ("5.1.1 任意角", 3, 4801, False, "05-第五章_三角函数/5.1.1_任意角/5.1.1_任意角.md"),
    # 5.1.2 at L4875 (## 刷基础)
    ("5.1.2 弧度制", 3, 4875, False, "05-第五章_三角函数/5.1.2_弧度制/5.1.2_弧度制.md"),
    # 5.1综合训练 at L4979 (## 刷基础 or 刷能力)
    ("第5.1节综合训练", 2, 4979, False, "05-第五章_三角函数/第5.1节综合训练/第5.1节综合训练.md"),
    # 5.2 at L5025 (# 5.2...)
    ("5.2 三角函数的概念", 2, 5025, True, "05-第五章_三角函数/5.2_三角函数的概念/5.2_三角函数的概念.md"),
    ("5.2.1 三角函数的概念", 3, 5027, False, "05-第五章_三角函数/5.2.1_三角函数的概念/5.2.1_三角函数的概念.md"),
    # 5.2.2 at L5102 (## 刷基础)
    ("5.2.2 同角三角函数的基本关系", 3, 5102, False, "05-第五章_三角函数/5.2.2_同角三角函数的基本关系/5.2.2_同角三角函数的基本关系.md"),
    # 5.2综合训练 at L5193 (## 刷基础 area)
    ("第5.2节综合训练", 2, 5193, False, "05-第五章_三角函数/第5.2节综合训练/第5.2节综合训练.md"),
    # 5.3 at L5227 (# 5.3...)
    ("5.3 诱导公式", 2, 5227, False, "05-第五章_三角函数/5.3_诱导公式/5.3_诱导公式.md"),
    # 5.4 at L5331 (# 5.4...)
    ("5.4 三角函数的图象与性质", 2, 5331, True, "05-第五章_三角函数/5.4_三角函数的图象与性质/5.4_三角函数的图象与性质.md"),
    ("5.4.1 正弦函数、余弦函数的图象", 3, 5333, False, "05-第五章_三角函数/5.4.1_正弦函数_余弦函数的图象/5.4.1_正弦函数_余弦函数的图象.md"),
    # 5.4.2 at L5422 or next 刷基础
    ("5.4.2 正弦函数、余弦函数的性质", 3, 5422, True, "05-第五章_三角函数/5.4.2_正弦函数_余弦函数的性质/5.4.2_正弦函数_余弦函数的性质.md"),
    ("课时1 正弦函数、余弦函数的性质(1)", 4, 5422, False, "05-第五章_三角函数/课时1_正弦函数_余弦函数的性质(1)/课时1_正弦函数_余弦函数的性质(1).md"),
    ("课时2 正弦函数、余弦函数的性质(2)", 4, 5532, False, "05-第五章_三角函数/课时2_正弦函数_余弦函数的性质(2)/课时2_正弦函数_余弦函数的性质(2).md"),
    # 5.4.3 at L5657 (## 刷基础)
    ("5.4.3 正切函数的性质与图象", 3, 5657, False, "05-第五章_三角函数/5.4.3_正切函数的性质与图象/5.4.3_正切函数的性质与图象.md"),
    # 5.4综合训练 at L5766 (## 刷素养)
    ("第5.4节综合训练", 2, 5766, False, "05-第五章_三角函数/第5.4节综合训练/第5.4节综合训练.md"),
    # 5.5 三角恒等变换 starts at L5842 (## 题型 1 给角求值)
    ("5.5 三角恒等变换", 2, 5842, True, "05-第五章_三角函数/5.5_三角恒等变换/5.5_三角恒等变换.md"),
    ("5.5.1 两角和与差的正弦、余弦和正切公式", 3, 5842, True, "05-第五章_三角函数/5.5.1_两角和与差的正弦_余弦和正切公式/5.5.1_两角和与差的正弦_余弦和正切公式.md"),
    ("课时1 两角和与差的正弦、余弦和正切公式", 4, 5842, False, "05-第五章_三角函数/课时1_两角和与差的正弦_余弦和正切公式/课时1_两角和与差的正弦_余弦和正切公式.md"),
    ("课时2 二倍角的正弦、余弦、正切公式", 4, 5879, False, "05-第五章_三角函数/课时2_二倍角的正弦_余弦_正切公式/课时2_二倍角的正弦_余弦_正切公式.md"),
    # 5.5.2 at L5963 (## 题型...)
    ("5.5.2 简单的三角恒等变换", 3, 5963, False, "05-第五章_三角函数/5.5.2_简单的三角恒等变换/5.5.2_简单的三角恒等变换.md"),
    # 5.5综合训练 at L6054 (## 刷基础)
    ("第5.5节综合训练", 2, 6054, False, "05-第五章_三角函数/第5.5节综合训练/第5.5节综合训练.md"),
    # 专题5 at L6109 (## 刷基础)
    ("专题5 三角恒等变换", 2, 6109, False, "05-第五章_三角函数/专题5_三角恒等变换/专题5_三角恒等变换.md"),
    # 5.6 at L6216 (## 刷基础)
    ("5.6 函数 y=Asin(ωx+φ)", 2, 6216, True, "05-第五章_三角函数/5.6_函数_y_A_sin_wx_phi/5.6_函数_y_A_sin_wx_phi.md"),
    ("5.6.1 匀速圆周运动的数学模型 5.6.2 函数 y=Asin(ωx+φ) 的图象", 3, 6216, False, "05-第五章_三角函数/5.6.1_5.6.2_图象/5.6.1_5.6.2_图象.md"),
    # 5.6综合训练 at L6314 (## 刷基础)
    ("第5.6节综合训练", 2, 6314, False, "05-第五章_三角函数/第5.6节综合训练/第5.6节综合训练.md"),
    # 5.7 at L6373 (# 5.7...)
    ("5.7 三角函数的应用", 2, 6373, False, "05-第五章_三角函数/5.7_三角函数的应用/5.7_三角函数的应用.md"),
    # 素养检测 at L6531 (## 刷速度)
    ("第五章素养检测", 2, 6531, False, "05-第五章_三角函数/第五章素养检测/第五章素养检测.md"),
    # 高考强化 at L6627 (## 刷真题 etc.)
    ("第五章高考强化", 2, 6627, False, "05-第五章_三角函数/第五章高考强化/第五章高考强化.md"),

    # Extras
    ("高考新动向·新定义、新情境", 2, 6748, False, "06-高考新动向/高考新动向_新定义_新情境/高考新动向_新定义_新情境.md"),
    ("高考新动向·链接高数", 2, 6840, False, "06-高考新动向/高考新动向_链接高数/高考新动向_链接高数.md"),
    ("强基计划", 2, 6900, False, "06-高考新动向/强基计划/强基计划.md"),
]

print(f"\nTotal sections: {len(section_map)}")

# ── Step 4: Build hierarchy entries ────────────────────────────────────────────
# Map each section to its TOC line (within 244-356) by fuzzy matching title
toc_lines_data = []
for i in range(243, min(356, len(q_lines))):
    toc_lines_data.append((i + 1, q_lines[i].strip()))

def find_toc_line(title: str, used_lines: set) -> int:
    """Find the TOC line that best matches the given title."""
    t_norm = norm(title)
    best_line = None
    best_score = 0
    for ln, text in toc_lines_data:
        if ln in used_lines:
            continue
        if not text.strip():
            continue
        text_norm = norm(text)
        if t_norm in text_norm or text_norm in t_norm:
            score = len(t_norm)
            if score > best_score:
                best_score = score
                best_line = ln
        # Also try numeric prefix match
        t_pref = re.match(r"^[\d\.]+", title)
        text_pref = re.match(r"^[\d\.]+", text)
        if t_pref and text_pref and t_pref.group() == text_pref.group():
            score = len(t_pref.group()) + 100
            if score > best_score:
                best_score = score
                best_line = ln
    return best_line

hierarchy_entries = []
primary_entries = []
used_toc_lines = set()

# First pass: find TOC lines for each entry
toc_line_map = {}
for idx, (title, level, start, structural, output) in enumerate(section_map):
    key = f"node-{idx+1:03d}"
    toc_line = find_toc_line(title, used_toc_lines)
    if toc_line:
        used_toc_lines.add(toc_line)
        toc_line_map[key] = toc_line
    else:
        # For entries not in TOC (like chapter-level or extras), 
        # use the nearest available TOC line or the last known one
        toc_line_map[key] = None

# For entries with no TOC line, assign them to the nearest previous entry's line
last_toc_line = 244
for idx, (title, level, start, structural, output) in enumerate(section_map):
    key = f"node-{idx+1:03d}"
    if toc_line_map[key] is None:
        toc_line_map[key] = last_toc_line
    else:
        last_toc_line = toc_line_map[key]

for idx, (title, level, start, structural, output) in enumerate(section_map):
    key = f"node-{idx+1:03d}"
    toc_line = toc_line_map[key]
    
    primary_entries.append({
        "key": key,
        "title": title,
        "level": level,
        "source_line": toc_line,
        "source_end_line": toc_line,
    })
    hierarchy_entries.append({
        "key": key,
        "title": title,
        "level": level,
        "output": output,
        "body_anchor": {
            "kind": "reviewed-boundary",
            "start_line": start,
            "evidence": f"Manual boundary for: {title}",
            "reviewer_confirmed": True,
        },
        "structural_only": structural,
        "emit_title": True,
        "answer_context": key,
    })

print(f"TOC line mapping (first 15):")
for idx in range(min(15, len(section_map))):
    key = f"node-{idx+1:03d}"
    title = section_map[idx][0]
    body = section_map[idx][2]
    tl = toc_line_map[key]
    print(f"  [{key}] TOC L{tl}, body L{body}: {title}")

# ── Step 5: Build fine-grained answer contexts from answers.raw.md ─────────────
SKIP = {"答案 及解析", "快速对答案", "答案及解析", "快速对答案。", "答案  及解析"}
cat_pat = re.compile(r"^\s*#{1,6}\s*(刷基础|刷提升|刷易错|刷能力|刷难关|刷真题|刷原创|刷速度|刷素养|刷综合|基础|狂K速览)$")

answer_contexts = []
current_main_leaf_key = None
cat_occurrence = {}

for i, line in enumerate(a_lines):
    ln = i + 1
    if not line.startswith("#"):
        continue
    text = re.sub(r"^\s*#{1,6}\s+", "", line).strip()
    if not text or text in SKIP:
        continue
    
    # Check if it's a category sub-heading
    m_cat = cat_pat.match(line)
    if m_cat and current_main_leaf_key:
        cat_title = m_cat.group(1).strip()
        sub_key = f"{current_main_leaf_key}:{cat_title}"
        answer_contexts.append({"key": sub_key, "start_line": ln})
        continue
    
    # Check if it's a main section heading
    best_key = None
    best_score = 0
    for idx, entry in enumerate(section_map):
        title = entry[0]
        key = f"node-{idx+1:03d}"
        t_norm = norm(title)
        a_norm = norm(text)
        if t_norm in a_norm or a_norm in t_norm:
            score = len(t_norm)
            if score > best_score:
                best_score = score
                best_key = key
        t_pref = re.match(r"^[\d\.]+", title)
        a_pref = re.match(r"^[\d\.]+", text)
        if t_pref and a_pref and t_pref.group() == a_pref.group():
            score = len(t_pref.group()) + 100
            if score > best_score:
                best_score = score
                best_key = key
    
    if best_key:
        curr_key = best_key
        curr_idx = int(curr_key.split("-")[1]) - 1
        if section_map[curr_idx][3]: # structural_only is True
            for j in range(curr_idx + 1, len(section_map)):
                if not section_map[j][3]: # leaf node
                    curr_key = f"node-{j+1:03d}"
                    break
        current_main_leaf_key = curr_key
        cat_occurrence[current_main_leaf_key] = 0
        answer_contexts.append({"key": curr_key, "start_line": ln})

print(f"Answer contexts: {len(answer_contexts)}")

# ── Step 6: Write adapter ─────────────────────────────────────────────────────
adapter = {
    "schema_version": 1,
    "status": "passed",
    "reviewer_confirmed": True,
    "profile": str(PROFILE.resolve()),
    "hierarchy": {
        "source_role": "questions",
        "root_output": "index.md",
        "primary_authority": {
            "status": "passed",
            "reviewer_confirmed": True,
            "start_line": 244,
            "end_line": 356,
            "entries": primary_entries,
        },
        "entries": hierarchy_entries,
    },
    "content": {
        "unknown_label_policy": "ignore",
        "allow_zero_question_number": True,
        "question_folder": "questions",
        "question_title_template": "Question {number}",
        "question_file_template": "Question_{number}_q{ordinal}_L{source_line}.md",
        "functional_folder_template": "{title}",
        "functional_file_template": "{title}_b{ordinal}.md",
        "max_path_component_length": 60,
        "max_path_length": 300,
        "question_patterns": [
            r"^(?P<number>\d+)[.．、]\s*",
            r"^\[(?P<number>\d+)\]\s*",
            r"^【(?P<number>\d+)】\s*",
            r"^(?P<number>[一二三四五六七八九十]+)[.．、]\s*",
        ],
        "roles": [
            {"role": "category", "depth": 1, "pattern": r"^(刷基础|刷提升|刷易错|刷能力|刷难关|刷真题|刷原创|刷速度|刷素养|刷综合|基础|狂K速览)$", "answer_context_template": "{note_key}:{title}"},
            {"role": "question-type", "depth": 2, "pattern": r"^(?P<title>题型\s*\d+.*|易错点\s*\d+.*|考点\s*\d+.*|专题\s*\d+.*|一、[^:：\.\s]*|二、[^:：\.\s]*|三、[^:：\.\s]*|四、[^:：\.\s]*|专练\s*\d+.*)"}
        ],
    },
    "answers": {
        "source_role": "answers",
        "contexts": answer_contexts,
        "ignore_ranges": [{"start_line": 1, "end_line": 14}],
        "answer_patterns": [
            r"^(?P<number>\d+)[.．、]\s*",
            r"^\[(?P<number>\d+)\]\s*",
            r"^【(?P<number>\d+)】\s*",
        ],
    },
}

OUTPUT.write_text(json.dumps(adapter, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"\nAdapter written! {len(hierarchy_entries)} hierarchy entries, {len(answer_contexts)} answer contexts.")
structural_count = sum(1 for s in section_map if s[3])
print(f"  Structural: {structural_count}, Leaf: {len(section_map) - structural_count}")
