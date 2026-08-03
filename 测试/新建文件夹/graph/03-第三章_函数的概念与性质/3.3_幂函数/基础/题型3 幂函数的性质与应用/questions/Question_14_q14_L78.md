---
question_id: "node-035:question:14:78"
question_number: "14"
context_key: "node-035"
question_source: "C:\\Mathematics-Knowledge\\Secondary-School-Mathematics-Knowledge-Map\\测试\\新建文件夹\\graph\\03-第三章_函数的概念与性质\\3.3_幂函数\\3.3_幂函数.md"
question_body_sha256: 6aa0e4df238ea3327e790a65682a1586c659a95ad2287fe1ede320791432b1a7
answer_status: matched
---

# Question 14

<!-- question-source:start -->
14.[河北衡水中学2025高一期中]幂函数 $f(x) = (k^2 -5k + 7)x^{k - 1}$ 为偶函数， $g(x) = mf(x) - x - 1.$ （1）求函数 $f(x)$ 的解析式；(2)若 $g(x)\geqslant m(x - 1)$ 对于 $x\in [0,2]$ 恒成立，求 $m$ 的取值范围.
<!-- question-source:end -->

## 答案与解析

<!-- answer-source:start -->
14.【解】(1)因为函数 $f(x)=(k^{2}-5k+7)x^{k-1}$ 为幂函数，
所以 $k^{2}-5k+7=1$ ，解得k=2或k=3。
当k=3时， $f(x)=x^{2}$ ，定义域为R，且 $f(-x)=(-x)^{2}=x^{2}=f(x)$ ，
所以 $f(x)$ 为偶函数，符合题意；
当k=2时， $f(x)=x$ ，定义域为R，且 $f(-x)=-x=-f(x)$ ，
所以 $f(x)$ 为奇函数，不符合题意。
所以 $f(x)=x^{2}$ .
(2)因为 $g(x)=mf(x)-x-1=mx^{2}-x-1$ 所以 $g(x)\geqslant m(x-1)$ 对于 $x\in[0,2]$ 恒成立，即 $m(x^{2}-x+1)\geqslant x+1$ 对于 $x\in[0,2]$ 恒成立，又 $x^{2}-x+1=\left(x-\frac{1}{2}\right)^{2}+\frac{3}{4}\geqslant\frac{3}{4}$ 则 $m\geqslant\frac{x+1}{x^{2}-x+1}$ 对于 $x\in[0,2]$ 恒成立，所以 $m\geqslant\left(\frac{x+1}{x^{2}-x+1}\right)_{\max}$ 设 $x+1=t$ ，则 $t\in[1,3]$ ， $\frac{x+1}{x^{2}-x+1}=\frac{t}{(t-1)^{2}-(t-1)+1}=\frac{t}{t^{2}-3t+3}=\frac{1}{t-3+\frac{3}{t}}$ 因为 $t+\frac{3}{t}\geqslant2\sqrt{t\cdot\frac{3}{t}}=2\sqrt{3}$ ，当且仅当 $t=\frac{3}{t}$ ，即 $t=\sqrt{3}$ ，即 $x=\sqrt{3}-1$ 时等号成立，
所以 $t+\frac{3}{t}-3\geqslant2\sqrt{3}-3,\frac{1}{t+\frac{3}{t}-3}\leqslant\frac{1}{2\sqrt{3}-3}=\frac{2\sqrt{3}+3}{3}$

所以 $\left(\frac{x + 1}{x^2 - x + 1}\right)_{\max} = \frac{2\sqrt{3} + 3}{3},$ 故 $m$ 的取值范围为 $\left[\frac{2\sqrt{3} + 3}{3}, + \infty\right).$
<!-- answer-source:end -->
