---
question_id: "node-022:question:1:23"
question_number: "1"
context_key: "node-022:刷原创"
question_source: "C:\\Mathematics-Knowledge\\Secondary-School-Mathematics-Knowledge-Map\\测试\\新建文件夹\\graph\\02-第二章_一元二次函数_方程和不等式\\第二章高考强化\\第二章高考强化.md"
question_body_sha256: 5e63c3547d13dc4c302f69fa578313f91105c641936c787db9573de65ee8adb7
answer_status: matched
---

# Question 1

<!-- question-source:start -->
1. 已知二次函数 $y=x^{2}+ax+b(a,b\in\mathbb{R})$ 的图象过点 $(-2,m),(t,0)$ ，且 $4\leqslant m\leqslant5,-1\leqslant t\leqslant1$ ，则（）
A. $-3 \leqslant b \leqslant -\frac{2}{3}$ B. $-3 \leqslant b \leqslant 0$ C. $-\frac{2}{3} \leqslant b \leqslant 9 - 4\sqrt{5}$ D. $-3 \leqslant b \leqslant 9 - 4\sqrt{5}$
<!-- question-source:end -->

## 答案与解析

<!-- answer-source:start -->
1. D 【解析】由题意, $m=4-2a+b$ , 令 $y=(x-c)(x-t)$ , 则由根与系数的关系知, $c+t=$ $p = \frac{ab + 2b}{a^2 + b^2 + 1} = \frac{ab + 2b}{a^2 + \frac{1}{5}b^2 + \frac{4}{5}b^2 + 1} \leqslant$ $\frac{ab + 2b}{2\sqrt{\frac{1}{5}}ab + 2\sqrt{\frac{4}{5}}b} = \frac{\sqrt{5}}{2},$ 当且仅当 $\begin{cases} a^2 = \frac{1}{5}b^2, \\ \frac{4}{5}b^2 = 1, \end{cases}$ 即 $\begin{cases} a = \frac{1}{2}, \\ b = \frac{\sqrt{5}}{2} \end{cases}$ 时，等号成立.

因为 $p \leqslant \frac{\sqrt{5}}{2} < \sqrt{2} < \sqrt{3}$ ，所以由(2)可知 $p$ 比 $\sqrt{2}$ 更远离 $\sqrt{3}$ ，即得证.

$-a, ct = b$ ，故 $m = 4 + 2(c + t) + ct$ ，又 $4 \leqslant m \leqslant 5$ ，则 $-2t \leqslant c(2 + t) \leqslant 1 - 2t.$ 因为 $-1 \leqslant t \leqslant 1$ ，所以 $-\frac{2t}{2 + t} \leqslant c \leqslant \frac{1 - 2t}{2 + t}$ ,

当 $-1 \leqslant t < 0$ 时， $\frac{(1 - 2t)t}{2 + t} \leqslant ct \leqslant -\frac{2t^2}{2 + t}$ ，即存

→ 点悟：因为 $-1 \leqslant t \leqslant 1$ ，有正有负，乘负值时不等号方向改变，乘正值时不等号方向不变，故需分开讨论

在 $-1 \leqslant t < 0$ 使 $\frac{(1 - 2t)t}{2 + t} \leqslant b \leqslant -\frac{2t^2}{2 + t}$ ,

记 $u = t + 2, 1 \leqslant u < 2$ ，则 $\frac{(1 - 2t)t}{2 + t} = -\left(2u + \frac{10}{u} - 9\right), -\frac{2t^2}{2 + t} = -2\left(u + \frac{4}{u} - 4\right)$ ，又 $y = 2u + \frac{10}{u}$ 与 $y = u + \frac{4}{u}$ 在 $\{u \mid 1 \leqslant u < 2\}$ 上均随 $u$ 的增大而减小，故 $0 > \frac{(1 - 2t)t}{2 + t} \geqslant -3,$ → 避坑：等号取不到时不能应用基本不等式求最值 $-2 \leqslant -\frac{2t^2}{2 + t} < 0$ ，故 $-3 \leqslant b < 0.$ 当 $0 \leqslant t \leqslant 1$ 时， $-\frac{2t^2}{2 + t} \leqslant b \leqslant \frac{(1 - 2t)t}{2 + t}$ ，同理可得 $0 \geqslant -\frac{2t^2}{2 + t} \geqslant -\frac{2}{3}, -\frac{1}{3} \leqslant \frac{(1 - 2t)t}{2 + t} \leqslant 9 - 4\sqrt{5}$ ，故 $-\frac{2}{3} \leqslant b \leqslant 9 - 4\sqrt{5}$ .

综上所述， $-3 \leqslant b \leqslant 9 - 4\sqrt{5}$ . 故选 D.
<!-- answer-source:end -->
