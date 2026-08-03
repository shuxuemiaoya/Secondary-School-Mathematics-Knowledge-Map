---
question_id: "node-054:question:17:96"
question_number: "17"
context_key: "node-054"
question_source: "C:\\Mathematics-Knowledge\\Secondary-School-Mathematics-Knowledge-Map\\测试\\新建文件夹\\graph\\04-第四章_指数函数与对数函数\\4.5.1_函数的零点与方程的解\\4.5.1_函数的零点与方程的解.md"
question_body_sha256: bd5ac5aa68059718b83b66164a0177181efb0dd737838474f2f9a93cf2bdb3ba
answer_status: matched
---

# Question 17

<!-- question-source:start -->
17. (多选) [四川成都部分学校 2025 联考] 已知函数 $f(x) = x^2 - ax + 1, g(x) = -\ln x$ . 若 $\max \{m, n\}$ 表示 $m, n$ 中的最大者, 设函数 $h(x) =$ 凯歌而行, 不以山海为远; 乘势而上, 不以日月为限。

$\max \{f(x), g(x)\} (x > 0)$ , 则下列结论正确的是 ( )
A. 若 $h(x)$ 没有零点, 则 $a$ 的取值范围为 $(- \infty, 2)$ B. 若 $h(x)$ 只有 1 个零点, 则 $a$ 的取值集合为 $\{2\}$ C. 若 $h(x)$ 有 2 个零点, 则 $a$ 的取值范围为 $(2, +\infty)$ D. $\forall a \in \mathbb{R}, h(x) \geqslant 0$
<!-- question-source:end -->

## 答案与解析

<!-- answer-source:start -->
17. ABC 【解析】 $f(x)$ 图象的对称轴方程为 $x=\frac{a}{2}$ ，开口向上，
当 $\frac{a}{2}\leqslant0$ ，即 $a\leqslant0$ 时，对任意 $x\in(0,+\infty)$ ，都有 $f(x)>f(0)=1$ ，所以 $h(x)\geqslant f(x)>0,h(x)$ 没有零点.
当 $\frac{a}{2}>0$ , 即 a>0 时, 令 $x^{2}-ax+1=0,\Delta=a^{2}-4<0$ , 解得 -2<a<2, 所以 0<a<2.

点悟：需要讨论判别式的正负，从而判断 $f(x)$ 的值域
当0<a<2时, $f(x)>0$ ,所以 $h(x)\geqslant f(x)>0$ , $h(x)$ 没有零点.
当a=2时, $f(x)=x^{2}-2x+1$ .
当 $x\neq1$ 时, $f(x)>0$ ,所以 $h(x)\geqslant f(x)>0$ ;当x=1时, $h(1)=\max\{f(1),g(1)\}=0$ ,所以 $h(x)$ 有1个零点.
当a>2时,2-a<0.
当 $x\in(0,1)$ 时, $h(x)\geqslant g(x)>0$ ;当x=1时, $h(1)=\max\{f(1),g(1)\}=\max\{2-a,0\}=0;$ 当 $x\in(1,+\infty)$ 时, $g(x)<0,f(1)=2-a<0,f(a)=1$ ,所以 $f(x)$ 在 $(1,+\infty)$ 上有1个零点，则 $h(x)$ 在 $(1,+\infty)$ 上有1个零点.所以 $h(x)$ 有2个零点.
设 $f(x)$ 在 $(1,+\infty)$ 上的零点为 $x_{1}$ ，则当 $x\in(1,x_{1})$ 时, $f(x)<0$ ,所以当 $x\in(1,x_{1})$ 时, $h(x)<0,D$ 错误.

综上, 当 a<2 时, $h(x)$ 没有零点; 当 a=2 时, $h(x)$ 有 1 个零点; 当 a>2 时, $h(x)$ 有 2 个零点, ABC 正确, 故选 ABC.

★易错点4 不能正确使用等价转化而致错
<!-- answer-source:end -->
