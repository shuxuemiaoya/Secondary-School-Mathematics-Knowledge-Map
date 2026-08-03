---
question_id: "node-059:question:1:117"
question_number: "1"
context_key: "node-059:刷原创"
question_source: "C:\\Mathematics-Knowledge\\Secondary-School-Mathematics-Knowledge-Map\\测试\\新建文件夹\\graph\\04-第四章_指数函数与对数函数\\第四章高考强化\\第四章高考强化.md"
question_body_sha256: 0c3050dc8a051e52087d529fc043ec92a939c669210c7f3b0a9e4516818fe472
answer_status: matched
---

# Question 1

<!-- question-source:start -->
1. 已知指数函数 $f(x)=a^{x}$ 为增函数, 且图象过点 $\left(\frac{1}{2}a,m\right), (b,m^{b-1})$ , 则 $2^{a}+4^{b}$ 满足 ( )
A. 当 b>0 时, 有最大值 $25\sqrt{2}$ B. 当 b<0 时, 有最大值 5
C. 当 b>0 时, 有最小值 32
D. 当 b<0 时, 有最小值 2
<!-- question-source:end -->

## 答案与解析

<!-- answer-source:start -->
1. C 【解析】因为 $f(x) = a^x$ 为增函数，所以 $a > 1$ ，又 $a^{\frac{a}{2}} = m, a^b = m^{b-1}$ ，则 $m > 1, a^b = (a^{\frac{a}{2}})^{b-1}, b = \frac{a}{2}(b - 1), b = 1 + \frac{2}{a - 2} \in (-\infty, -1) \cup (1, +\infty)$ ，又 $b = 1 + \frac{2}{a - 2} = \frac{a}{a - 2}$ ，取倒数后整理可得 $\frac{2}{a} + \frac{1}{b} = 1$ . $a = \frac{2b}{b - 1}$ ，则 $2^a + 4^b = 4^{\frac{b}{b - 1}} + 4^b = 4(4^{\frac{1}{b - 1}} + 4^{b - 1})$ ，当 $b < 0$ 时， $b < -1, b - 1 < -2$ ，故 $2^a + 4^b = 4(4^{\frac{1}{b - 1}} + 4^{b - 1}) > 8 \times 2^{\frac{1}{b - 1} + b - 1}$ ，由对勾函数的性质知 $y = \frac{1}{b - 1} + b - 1$ 在 $(-\infty, -1)$ 上单调递增, 故 $2^{a} + 4^{b} > \sqrt{2}$ .
又由于 $y = 4^{b-1}$ 单调递增， $y = 4^{\frac{1}{b-1}}$ 单调递减，且 $0 < 4^{b-1} < \frac{1}{16}, \frac{1}{2} < 4^{\frac{1}{b-1}} < 1$ ，则 $2^{a} + 4^{b} = 4(4^{\frac{1}{b-1}} + 4^{b-1}) < 4 \times \left(1 + \frac{1}{16}\right) = \frac{17}{4}$ ，B, D 错误.
当 b > 0 时，b > 1, b - 1 > 0，故 $2^{a} + 4^{b} = 4\left(4^{\frac{1}{b-1}} + 4^{b-1}\right) \geqslant 8 \times 2^{\frac{1}{b-1} + b-1} \geqslant 8 \times 2^{2} = 32$ ，当且仅当 b = 2 时等号成立，A 错误，C 正确。故选 C.
<!-- answer-source:end -->
