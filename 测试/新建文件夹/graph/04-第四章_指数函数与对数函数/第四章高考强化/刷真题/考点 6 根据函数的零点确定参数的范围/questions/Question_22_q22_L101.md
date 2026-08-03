---
question_id: "node-059:question:22:101"
question_number: "22"
context_key: "node-059"
question_source: "C:\\Mathematics-Knowledge\\Secondary-School-Mathematics-Knowledge-Map\\测试\\新建文件夹\\graph\\04-第四章_指数函数与对数函数\\第四章高考强化\\第四章高考强化.md"
question_body_sha256: 53750d4bab2791d2544fcc505e671a7691f384ab07500ca401c96b99c38ebc3c
answer_status: matched
---

# Question 22

<!-- question-source:start -->
22. [天津 2020 · 9, 5 分] 已知函数 $f(x) = \begin{cases} x^3, & x \geqslant 0, \\ -x, & x < 0. \end{cases}$ 若函数 $g(x) = f(x) - |kx^2 - 2x| (k \in \mathbb{R})$ 恰有 4 个零点，则 $k$ 的取值范围是（）A. $\left(-\infty, -\frac{1}{2}\right) \cup (2\sqrt{2}, +\infty)$ B. $\left(-\infty, -\frac{1}{2}\right) \cup (0, 2\sqrt{2})$ C. $(-\infty, 0) \cup (0, 2\sqrt{2})$ D. $(-\infty, 0) \cup (2\sqrt{2}, +\infty)$
<!-- question-source:end -->

## 答案与解析

<!-- answer-source:start -->
22. D 【解析】当 k=0 时， $g(x)=\left\{\begin{aligned}x^{3}-2x,x&\geqslant0,\\ x,x&<0,\end{aligned}\right.$ 令 $x^{3}-2x=0$ ，得 x=0, $x=\sqrt{2},x=-\sqrt{2}$ （舍），所以 $g(x)$ 有 2 个零点，不符合题意。当 k>0 时， $g(x)=\left\{\begin{aligned}x^{3}+(kx^{2}-2x),&0\leqslant x\leqslant\frac{2}{k},\\ x^{3}-(kx^{2}-2x),&x>\frac{2}{k},\\ -x-(kx^{2}-2x),&x<0,\end{aligned}\right.$ 即 $g(x)=\left\{\begin{aligned}x(x^{2}+kx-2),&0\leqslant x\leqslant\frac{2}{k},\\ x(x^{2}-kx+2),&x>\frac{2}{k},\\ -x(kx-1),&x<0.\end{aligned}\right.$ 当 x<0 时， $-x(kx-1)<0,g(x)$ 无零点。

当 $0\leqslant x\leqslant\frac{2}{k}$ 时，设 $h(x)=x^{2}+kx-2$ ，因为 $h(0)=-2<0,h\left(\frac{2}{k}\right)=\frac{4}{k^{2}}>0$ ，由函数零点存在定理可知， $g(x)$ 在 $\left(0,\frac{2}{k}\right)$ 上有 1 个零点，又 $g(0)=0$ ，所以 $g(x)$ 在 $\left[0,\frac{2}{k}\right]$ 上有 2 个零点。

若使 $g(x)$ 有 4 个零点，则 $x^{2}-kx+2=0$ 在 $\left(\frac{2}{k},+\infty\right)$ 上有 2 个不等实根。

设 $s(x)=x^{2}-kx+2$ ，因为 $s\left(\frac{2}{k}\right)=\frac{4}{k^{2}}>0$ ，

所以只需满足 $\left\{\begin{aligned}&k>0,\\ &\frac{k}{2}>\frac{2}{k},\\ &\Delta=k^{2}-8>0,\end{aligned}\right.$

解得 $k>2\sqrt{2}$ .
当 k<0 时， $g(x)=\left\{\begin{aligned}&x^{3}+(kx^{2}-2x),&x\geqslant0,\\&-x-(kx^{2}-2x),&\frac{2}{k}\leqslant x<0,\\&-x+(kx^{2}-2x),&x<\frac{2}{k},\end{aligned}\right.$ 即 $g(x)=\left\{\begin{aligned}&x(x^{2}+kx-2),&x\geqslant0,\\&-x(kx-1),&\frac{2}{k}\leqslant x<0,\\&x(kx-3),&x<\frac{2}{k}.\\\end{aligned}\right.$ 当 $x<\frac{2}{k}$ 时，令 kx-3=0，得 $x=\frac{3}{k}<\frac{2}{k}$ ， $g(x)$ 在 $\left(-\infty,\frac{2}{k}\right)$ 上有 1 个零点；
当 $\frac{2}{k}\leqslant x<0$ 时，令 kx-1=0，得 $x=\frac{1}{k}$ ， $\frac{2}{k}<\frac{1}{k}<0$ ，所以 $g(x)$ 在 $\left[\frac{2}{k},0\right)$ 上有 1 个零点；
当 $x \geqslant 0$ 时，令 $m(x) = x^{2} + kx - 2$ .
因为函数 $m(x)$ 图象的对称轴 $x=-\frac{k}{2}>0, \Delta=k^{2}+8>0, m(0)=-2<0,$ 所以 $g(x)$ 在 $(0,+\infty)$ 上有 1 个零点，又 $g(0)=0,$ 所以 $g(x)$ 在 $[0,+\infty)$ 上有 2 个零点.
所以当 k<0 时， $g(x)$ 有 4 个零点.
综上，若 $g(x)$ 恰有 4 个零点，则 k<0 或 $k>2\sqrt{2}$ ，故选 D.
<!-- answer-source:end -->
