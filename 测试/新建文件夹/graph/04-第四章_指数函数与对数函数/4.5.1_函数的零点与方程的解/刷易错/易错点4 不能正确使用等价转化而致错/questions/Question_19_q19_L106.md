---
question_id: "node-054:question:19:106"
question_number: "19"
context_key: "node-054"
question_source: "C:\\Mathematics-Knowledge\\Secondary-School-Mathematics-Knowledge-Map\\测试\\新建文件夹\\graph\\04-第四章_指数函数与对数函数\\4.5.1_函数的零点与方程的解\\4.5.1_函数的零点与方程的解.md"
question_body_sha256: af53cc0f96f7dcf4f1366d2221d1bcc83ccc83a16d0f777ad105e0eb9d40a504
answer_status: matched
---

# Question 19

<!-- question-source:start -->
19. 已知函数 $f(x)=\left\{\begin{aligned}x+2,x&\leqslant0,\\ x+\frac{1}{x},&x>0,\end{aligned}\right.$ 若函数 $g(x)=$ $[f(x)]^{2}+4f(x)+a(a\in\mathbb{R})$ 有三个不同的零点，则实数 a 的取值范围为 ( )

A. $(-∞,4)$ B. $(-∞,4]$ C. $(-∞,-12)$ D. $(-∞,-12]$
<!-- question-source:end -->

## 答案与解析

<!-- answer-source:start -->
19. D
思路导引 根据给定条件,先尝试画出函数 $y=f(x)$ 的图象. 再令 $f(x)=t$ , 则转化为 $h(t)=t^{2}+4t+a$ 关于 t 有两个零点, 其中一个零点 $t_{1}$ 满足 $f(x)=t_{1}$ 只有一根, 且 $t_{1}<2$ ; 而另一零点 $t_{2}$ 满足 $f(x)=t_{2}$ 有两根, 且 $t_{2}\geqslant2$ , 从而满足题意, 再根据二次函数零点分布的规律和函数零点存在定理求出实数 a 的取值范围.
【解析】当 $x \leqslant 0$ 时, 函数 $f(x) = x + 2$ 在 $(-\infty, 0]$ 上单调递增, $f(x) \leqslant f(0) = 2$ .
当 x > 0 时, 函数 $f(x) = x + \frac{1}{x} \geqslant 2 \cdot \sqrt{x \cdot \frac{1}{x}} = 2$ , 当且仅当 x = 1 时取等号, 函数 $y = f(x)$ 的大致图象如图所示.

![](../../../../../images/answers/part-002/9c35992f12b7ee231e63964baba0c31fe84c58c2f623fb9be0e0ed872867b68a.jpg)

令 $f(x) = t$ ，观察图象知，当 $t < 2$ 时，方程 $f(x) = t$ 有一个根，当 $t\geqslant 2$ 时，方程 $f(x) = t$ 有两个不等根.函数 $g(x) = [f(x)]^2 +4f(x) + a(a\in \mathbf{R})$ 有三个零点，等价于函数 $h(t) = t^2 +4t + a$ 有两个零点 $t_1,t_2$ ，并满足 $t_1 < 2,t_2\geqslant 2$ ，而函数 $h(t)$ 图象的对称轴为直线 $t = -2$ ，于是得 $h(2) = a + 12\leqslant 0$ ，解得 $a\leqslant -12$ ，所以实数 $a$ 的取值范围为 $(- \infty , - 12]$ .故选D.

易错警示 对分段函数 $y=f(x)$ 的函数值分布、零点分布情况, 可以尝试画出图象, 借助图象分析, 掌握好 $t=f(x)$ 作为一个基本元, 分析出符合题意的取值, 并会区分 $f(x)=t$ 和 $h(t)=0$ 之间的联系与区别, 从而求出参数 a 的取值范围.

★易错点5 不能正确理解题意而致错
<!-- answer-source:end -->
