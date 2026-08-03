---
question_id: "node-031:question:4:104"
question_number: "4"
context_key: "node-031:刷提升"
question_source: "C:\\Mathematics-Knowledge\\Secondary-School-Mathematics-Knowledge-Map\\测试\\新建文件夹\\graph\\03-第三章_函数的概念与性质\\课时2_函数的最大(小)值\\课时2_函数的最大(小)值.md"
question_body_sha256: c3187842b71121530ada7580d63260acd85577db80fadc46cb09e77abf6f18b4
answer_status: matched
---

# Question 4

<!-- question-source:start -->
4. 对于定义域为 I 的函数, 如果存在区间 $[m, n] \subseteq I$ , 同时满足下列两个条件:
① $f(x)$ 在区间 $[m,n]$ 上是单调的;
②当定义域是 $[m,n]$ 时, $f(x)$ 的值域也是 $[m,n]$ ,
则称 $[m,n]$ 是函数 $y=f(x)$ 的一个“黄金区间”.如果 $[m,n]$ 是函数 $f(x)=\frac{(a^{2}+a)x-1}{a^{2}x}(a\neq0)$ 的一个“黄金区间”,则n-m的最大值为( )
A. $\frac{\sqrt{3}}{3}$ B.1 C. $\frac{2\sqrt{3}}{3}$ D.2
<!-- question-source:end -->

## 答案与解析

<!-- answer-source:start -->
4.C
思路导引 利用函数单调性得 $\left\{\begin{aligned}f(m)=m,\\ f(n)=n,\end{aligned}\right.$ 利用这个同构方程得 $m,n$ 为
方程 $a^{2}x^{2}-(a^{2}+a)x+1=0$ 的两个同号的
实数根，由 $\Delta>0$ 得出 $a$ 的取值范围，再
由根与系数的关系表示出 $n-m$ ，进而求
出 $n-m$ 的最值.
【解析】由题意， $f(x)=\frac{(a^{2}+a)x-1}{a^{2}x}=\frac{a+1}{a}-\frac{1}{a^{2}x}$ 在 $(-∞,0),(0,+∞)$ 上均单调递增，而函
数 $f(x)$ 在“黄金区间” $[m,n]$ 上单调，所以 $[m,n]\subseteq(-∞,0)$ 或 $[m,n]\subseteq(0,+∞)$ ，且 $f(x)$ 在 $[m,n]$ 上单调递增，故 $\left\{\begin{aligned}f(m)=m,\\ f(n)=n,\end{aligned}\right.$ 即 $m,n$ 为方程 $\frac{a+1}{a}-\frac{1}{a^{2}x}=x$ 的

两个同号实数根，
即方程 $a^{2}x^{2}-(a^{2}+a)x+1=0$ 有两个同号的实数根，因为 $mn=\frac{1}{a^{2}}>0$ ，所以只需要 $\Delta=(a^{2}+a)^{2}-4a^{2}>0\Rightarrow a<-3$ 或 a>1，
又 $\left\{\begin{aligned}&m+n=\frac{a^{2}+a}{a^{2}}=\frac{a+1}{a},\\ &mn=\frac{1}{a^{2}},\end{aligned}\right.$ 所以 n-m = $\sqrt{(m+n)^{2}-4mn}=\sqrt{\left(\frac{a+1}{a}\right)^{2}-\frac{4}{a^{2}}}=\sqrt{-3\left(\frac{1}{a}-\frac{1}{3}\right)^{2}+\frac{4}{3}}$ ，则当 a=3 时，n-m 有最大值 $\frac{2\sqrt{3}}{3}$ . 故选 C.
<!-- answer-source:end -->
