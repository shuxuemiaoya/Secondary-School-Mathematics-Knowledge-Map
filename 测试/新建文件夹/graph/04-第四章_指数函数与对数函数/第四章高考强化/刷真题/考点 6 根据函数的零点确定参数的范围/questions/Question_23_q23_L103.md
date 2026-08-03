---
question_id: "node-059:question:23:103"
question_number: "23"
context_key: "node-059"
question_source: "C:\\Mathematics-Knowledge\\Secondary-School-Mathematics-Knowledge-Map\\测试\\新建文件夹\\graph\\04-第四章_指数函数与对数函数\\第四章高考强化\\第四章高考强化.md"
question_body_sha256: f61ddeff7ca5a661a5e0a329d50c25b211b5d6577f2582fe1d0f534d25614dce
answer_status: matched
---

# Question 23

<!-- question-source:start -->
23.[天津 2023·15,5 分]设 $a \in \mathbf{R}$ , 函数 $f(x) = ax^2 - 2x - |x^2 - ax + 1|$ . 若 $f(x)$ 恰有两个零点, 则 $a$ 的取值范围为 \_\_\_\_.
<!-- question-source:end -->

## 答案与解析

<!-- answer-source:start -->
23. $(- \infty, 0) \cup (0, 1) \cup (1, + \infty)$ 思路导引 令 $x^{2} - ax + 1 = 0$ $\xrightarrow{\text{判别式的正负}}$ 判断 $x^{2} - ax + 1$ 的正负分类讨论去绝对值，化简 $f(x)$ 的解析式 $\xrightarrow{f(x)\text{有且仅有两个零点}} a$ 的取值范围

【解析】令 $x^{2} - ax + 1 = 0$ ，则 $\Delta_{1} = a^{2} - 4$ ，

当 $-2 \leqslant a \leqslant 2$ 时， $\Delta_{1} \leqslant 0, x^{2} - ax + 1 \geqslant 0$ 恒成立，此时 $f(x) = (a - 1)x^{2} + (a - 2)x - 1$ 。

当 $a \neq 1$ 时，令 $f(x) = (a - 1)x^{2} + (a - 2)x - 1 = 0$ ，则 $\Delta_{2} = (a - 2)^{2} + 4(a - 1) = a^{2}$ ，当 $a \neq 0$ 时， $\Delta_{2} > 0, f(x)$ 有且仅有两个零点；

当 $a = 1$ 时， $f(x) = -x - 1, f(x)$ 有且仅有一个零点，不符合题意，

所以 $-2 \leqslant a < 0$ 或 $0 < a < 1$ 或 $1 < a \leqslant 2$ 。

当 $a < -2$ 或 $a > 2$ 时， $\Delta_{1} > 0$ ，方程 $x^{2} - ax + 1 = 0$ 有两个不等实根，设为 $x_{1}, x_{2}, x_{1} < x_{2}$ ,

所以 $f(x) = \begin{cases} [(a + 1)x - 1](x - 1), & x_{1} \leqslant x \leqslant x_{2}, \\ [(a - 1)x - 1](x + 1), & x < x_{1} \text{或 } x > x_{2}. \end{cases}$ 设 $g(x) = [(a + 1)x - 1](x - 1)$ ，令 $g(x) = 0$ ，解得 $x = 1$ 或 $x = \frac{1}{a + 1}$ ；设 $h(x) = [(a - 1)x - 1](x + 1)$ ，令 $h(x) = 0$ ，解得 $x = -1$ 或 $x = \frac{1}{a - 1}$ .

当 $a < -2$ 时， $x_{1} = \frac{a - \sqrt{a^{2} - 4}}{2} < -1, \frac{1}{a + 1} < x_{2} = \frac{a + \sqrt{a^{2} - 4}}{2} < \frac{1}{a - 1}$ ，所以 $f(x)$ 有且仅有两个零点，符合题意。

当 $a > 2$ 时，因为 $x_{2} = \frac{a + \sqrt{a^{2} - 4}}{2} >1$ ，且 $\frac{1}{a + 1} < x_1 = \frac{a - \sqrt{a^2 - 4}}{2} < \frac{1}{a - 1},$ 所以 $f(x)$ 有且仅有两个零点，符合题意.综上所述， $a$ 的取值范围为 $(-\infty ,0)\cup$ $(0,1)\cup (1, + \infty)$
<!-- answer-source:end -->
