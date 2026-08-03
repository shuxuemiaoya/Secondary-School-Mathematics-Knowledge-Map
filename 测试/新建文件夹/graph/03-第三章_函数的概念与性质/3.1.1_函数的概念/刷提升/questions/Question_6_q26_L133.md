---
question_id: "node-025:question:6:133"
question_number: "6"
context_key: "node-025:刷提升"
question_source: "C:\\Mathematics-Knowledge\\Secondary-School-Mathematics-Knowledge-Map\\测试\\新建文件夹\\graph\\03-第三章_函数的概念与性质\\3.1.1_函数的概念\\3.1.1_函数的概念.md"
question_body_sha256: bd4cb37234ba1f10aab8c07386db6d6d943af8fc46563d32c64ff2b991fbdda3
answer_status: matched
---

# Question 6

<!-- question-source:start -->
6. (多选) 若某函数的定义域与其值域的交集是 $[a, b]$ , 则称该函数为“[a, b] 交汇函数”. 下列函数是“[0,1] 交汇函数”的是 ( )
A. $y = \sqrt{1 - x}$ B. $y = 2\sqrt{x} - x$ C. $y = \frac{1}{x^2 - 2x + 2}$ D. $y = \sqrt{1 - x^2} - |x|$
<!-- question-source:end -->

## 答案与解析

<!-- answer-source:start -->
6. AB 【解析】由“[a,b]交汇函数”的定义可知“[0,1]交汇函数”表示函数的定义域与其值域的交集为[0,1].
对于选项 A, $y = \sqrt{1 - x}$ 的定义域 $A = (-\infty, 1]$ ，值域 $B = [0, +\infty)$ ，则 $A \cap B = [0, 1]$ ，A 正确；
对于选项 B, $y = 2\sqrt{x} - x$ 的定义域 $A = [0, +\infty)$ ，令 $t = \sqrt{x} \geqslant 0$ ，则 $y = 2t - t^{2} = -(t - 1)^{2} + 1 \leqslant 1$ ，值域 $B = (-\infty, 1]$ ，则 $A \cap B = [0, 1]$ ，B 正确；
对于选项 C, $y = \frac{1}{x^{2} - 2x + 2} = \frac{1}{(x - 1)^{2} + 1}$ , $\because (x-1)^{2} \geqslant 0, \therefore (x-1)^{2} + 1 \geqslant 1, \therefore 0 < \frac{1}{(x-1)^{2}+1} \leqslant 1$ ，定义域 A=R，值域 B=(0,1)，则 $A \cap B = (0,1]$ ，C 错误；
对于选项 D, $y = \sqrt{1 - x^{2}} - |x|$ 的定义域 A = [-1, 1]，由题可得 $y^{2} = 1 - x^{2} + x^{2} - 2|x|\sqrt{1-x^{2}} = 1 - 2\sqrt{x^{2}(1-x^{2})}$ , $\because -1 \leqslant [174]$

$x \leqslant 1, \therefore 0 \leqslant x^{2}(1 - x^{2}) \leqslant \frac{1}{4}$ , 即 $0 \leqslant y^{2} \leqslant 1$ , 点悟: $0 \leqslant x^{2} \leqslant 1$ , 利用 $ab \leqslant \left(\frac{a + b}{2}\right)^{2}$ , 得 $x^{2}(1 - x^{2}) \leqslant \left(\frac{x^{2} + 1 - x^{2}}{2}\right)^{2} = \frac{1}{4}$ $\therefore -1 \leqslant y \leqslant 1$ , 即值域 $B = [-1, 1]$ , 则 $A \cap B = [-1, 1]$ , D 错误. 故选 AB.

归纳总结 求函数的定义域,主要包括:偶次根式中被开方数不小于0、分母不为0、自变量的实际意义等;求函数的值域实际上就是求函数的最值问题(如无最值则为无穷大或无穷小),但要注意值域是否连续.
<!-- answer-source:end -->
