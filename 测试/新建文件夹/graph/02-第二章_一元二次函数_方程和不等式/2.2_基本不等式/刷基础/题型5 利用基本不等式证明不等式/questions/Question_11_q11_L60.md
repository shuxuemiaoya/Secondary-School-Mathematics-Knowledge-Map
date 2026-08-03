---
question_id: "node-018:question:11:60"
question_number: "11"
context_key: "node-018"
question_source: "C:\\Mathematics-Knowledge\\Secondary-School-Mathematics-Knowledge-Map\\测试\\新建文件夹\\graph\\02-第二章_一元二次函数_方程和不等式\\2.2_基本不等式\\2.2_基本不等式.md"
question_body_sha256: 915c1b6be3dc46955092ab8873597d952a2d7273880bd415592effe312ec8d43
answer_status: matched
---

# Question 11

<!-- question-source:start -->
11.[广西桂林部分学校2025高一联考]已知a, b,c均为正实数.

(1) 证明: $a + b + c \geqslant \sqrt{2ab} + \sqrt{2bc}$ ;

(2) 证明 $\frac{a + b + c}{3} \geqslant \sqrt[3]{abc}$ , 并求 $y = 2x + \frac{1}{(x - 2)^2}$ ( $x > 2$ ) 的最小值.
<!-- question-source:end -->

## 答案与解析

<!-- answer-source:start -->
11. (1)【证明】由基本不等式得 $a + \frac{b}{2} \geqslant$

$\sqrt{2ab},\frac{b}{2}+c\geqslant\sqrt{2bc},$ 两个不等式相加得 $a+b+c\geqslant\sqrt{2ab}+\sqrt{2bc}$ ，
当且仅当 $a=\frac{b}{2}=c$ 时“=”成立，问题得证.
(2)【解】 $a^{3}+b^{3}+c^{3}-3abc=(a+b)^{3}-3a^{2}b-3ab^{2}+c^{3}-3abc$ $=(a+b)^{3}+c^{3}-3a^{2}b-3ab^{2}-3abc$ $=(a+b+c)\left[(a+b)^{2}-(a+b)c+c^{2}\right]-3ab(a+b+c)$ $=(a+b+c)(a^{2}+2ab+b^{2}-ac-bc+c^{2}-3ab)$ $=(a+b+c)(a^{2}+b^{2}+c^{2}-ab-bc-ca)$ $=\frac{1}{2}(a+b+c)\left[(a-b)^{2}+(b-c)^{2}+(c-a)^{2}\right]\geqslant0,$ 当且仅当 a=b=c 时等号成立，
所以不等式 $a^{3}+b^{3}+c^{3}\geqslant3abc$ 成立，
所以 $a+b+c=\left(\sqrt[3]{a}\right)^{3}+\left(\sqrt[3]{b}\right)^{3}+\left(\sqrt[3]{c}\right)^{3}\geqslant3\times\sqrt[3]{a}\times\sqrt[3]{b}\times\sqrt[3]{c}=3\sqrt[3]{abc}$ 所以 $\frac{a+b+c}{3}\geqslant\sqrt[3]{abc}$ ，当且仅当 a=b=c 时取等号，
故不等式 $\frac{a+b+c}{3}\geqslant\sqrt[3]{abc}$ 成立.
因为 x>2，所以 x-2>0, $y=2x+\frac{1}{(x-2)^{2}}=(x-2)+(x-2)+\frac{1}{(x-2)^{2}}+4\geqslant3\sqrt[3]{(x-2)\cdot(x-2)\cdot\frac{1}{(x-2)^{2}}}+4=7,$ 当且仅当 $x-2=\frac{1}{(x-2)^{2}}$ ，即 x=3 时，等号成立，所以 $y_{min}=7.$
<!-- answer-source:end -->
