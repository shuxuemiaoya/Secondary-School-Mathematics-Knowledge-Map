---
question_id: "node-031:question:8:121"
question_number: "8"
context_key: "node-031:刷提升"
question_source: "C:\\Mathematics-Knowledge\\Secondary-School-Mathematics-Knowledge-Map\\测试\\新建文件夹\\graph\\03-第三章_函数的概念与性质\\课时2_函数的最大(小)值\\课时2_函数的最大(小)值.md"
question_body_sha256: 8780ae93b99977a5d76ca4168c0397b372ec7c5f91a7cde3c09c915126e9d6a8
answer_status: matched
---

# Question 8

<!-- question-source:start -->
8.[辽宁鞍山一中2025高一月考]已知函数 $f(x)=\frac{x+b}{x^{2}+a}$ ，且满足 $f(0)=0,f(1)=\frac{1}{5}$ .
(1) 判断 $f(x)$ 在 $[-2,2]$ 上的单调性，并用定义证明；
(2) 设 $g(x)=kx^{2}+2kx+1(k\neq0)$ ，若对任意的 $x_{1}\in[-2,2]$ ，总存在 $x_{2}\in[-1,2]$ ，使得 $f(x_{1})=g(x_{2})$ 成立，求实数 k 的取值范围.
<!-- question-source:end -->

## 答案与解析

<!-- answer-source:start -->
8.【解】(1)由函数 $f(x)=\frac{x+b}{x^{2}+a}$ 满足 $f(0)=0,f(1)=\frac{1}{5},$ 可得 $\left\{\begin{aligned}\frac{0+b}{0^{2}+a}&=0,\\ \frac{1+b}{1^{2}+a}&=\frac{1}{5},\end{aligned}\right.$ 解得 $\left\{\begin{aligned}b&=0,\\ a&=4,\end{aligned}\right.$ 则 $f(x)=\frac{x}{x^{2}+4}.$ $f(x)$ 在 $[-2,2]$ 上单调递增，证明如下：
任取 $x_{1},x_{2}\in[-2,2]$ ，且 $x_{1}<x_{2}$ ，则 $f(x_{1})-f(x_{2})=\frac{x_{1}}{x_{1}^{2}+4}-\frac{x_{2}}{x_{2}^{2}+4}=$ $=\frac{x_{1}(x_{2}^{2}+4)-x_{2}(x_{1}^{2}+4)}{(x_{1}^{2}+4)(x_{2}^{2}+4)}=\frac{(x_{1}-x_{2})(4-x_{1}x_{2})}{(x_{1}^{2}+4)(x_{2}^{2}+4)},$ 由 $-2\leqslant x_{1}<x_{2}\leqslant2$ ，可得 $x_{1}x_{2}<4$ 又 $x_{1}-x_{2}<0,x_{1}^{2}+4>0,x_{2}^{2}+4>0,$ 则 $\frac{(x_{1}-x_{2})(4-x_{1}x_{2})}{(x_{1}^{2}+4)(x_{2}^{2}+4)}<0$ ，即 $f(x_{1})<f(x_{2})$ 所以 $f(x)$ 在 $[-2,2]$ 上单调递增.
(2)对任意的 $x_{1}\in[-2,2]$ ，由 $f(x)$ 在 $[-2,2]$ 上单调递增，
可得 $f(-2)\leqslant f(x_{1})\leqslant f(2)$ ，即 $-\frac{1}{4}\leqslant f(x_{1})\leqslant\frac{1}{4},$ 则 $f(x)$ 在 $[-2,2]$ 上的值域 $A=\left[-\frac{1}{4},\frac{1}{4}\right].$ 函数 $y=kx^{2}+2kx+1(k\neq0)$ 图象的对称轴为直线x=-1，
当k>0时， $g(x)=kx^{2}+2kx+1$ 在 $[-1,2]$ 上单调递增，
值域 $B=[-k+1,8k+1]$ ，
由题意可得 $A\subseteq B$ ，则 $\left\{\begin{aligned}k&>0,\\ -k&+1\leqslant-\frac{1}{4},\\ 8k&+1\geqslant\frac{1}{4},\end{aligned}\right.$ 解得 $k\geqslant\frac{5}{4};$ 当k<0时， $g(x)=kx^{2}+2kx+1$ 在 $[-1,2]$ 上单调递减，
值域 $B=[8k+1,-k+1]$

由题意可得 $A \subseteq B$ ，则 $\left\{ \begin{array}{l} k < 0, \\ 8k + 1 \leqslant -\frac{1}{4}, \\ -k + 1 \geqslant \frac{1}{4}, \end{array} \right.$ 解得 $k \leqslant -\frac{5}{32}$ . 综上，实数 $k$ 的取值范围为 $\left(-\infty, -\frac{5}{32}\right] \cup \left[\frac{5}{4}, +\infty\right)$ .
<!-- answer-source:end -->
