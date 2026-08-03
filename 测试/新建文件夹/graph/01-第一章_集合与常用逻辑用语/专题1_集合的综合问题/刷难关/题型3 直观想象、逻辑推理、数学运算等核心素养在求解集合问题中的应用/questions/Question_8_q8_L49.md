---
question_id: "node-006:question:8:49"
question_number: "8"
context_key: "node-006"
question_source: "C:\\Mathematics-Knowledge\\Secondary-School-Mathematics-Knowledge-Map\\测试\\新建文件夹\\graph\\01-第一章_集合与常用逻辑用语\\专题1_集合的综合问题\\专题1_集合的综合问题.md"
question_body_sha256: 52587b3d423f3c9d85ecfd1c53ce062599258e237474e3d7c0ce700bf9a7427a
answer_status: matched
---

# Question 8

<!-- question-source:start -->
8.[重庆巴渝学校2025高一期中]已知集合 $A=\{x\mid x^{2}+2\ 024x+2\ 025=0\}$ ， $B=\{x\mid(x^{2}+ax)(x^{2}+4ax+4)=0\}$ ，记非空集合S的元素个数为 $n(S)$ ，已知 $|n(A)-n(B)|=1$ ，记实数a的所有可能取值构成的集合为M，则M的非空子集的个数是\_\_\_\_。
<!-- question-source:end -->

## 答案与解析

<!-- answer-source:start -->
8.31 【解析】对于 $x^{2}+2024x+2025=0$ ,有 $\Delta=2024^{2}-4\times2025>0$ ,
所以集合 $A=\{x|x^{2}+2024x+2025=0\}$ 中有两个元素,即 $n(A)=2$ .
因为 $|n(A)-n(B)|=1$ ,所以 $n(B)=1$ 或3.
敲黑板:从集合B的元素个数明确方程根的个数
对于 $(x^{2}+ax)(x^{2}+4ax+4)=0$ ,易知x=0

必是方程的一个解.
当 $n(B)=1$ 时, $B=\{0\}$ , 所以 $x^{2}+ax=0$ 有两个相等的实数根, 且 $x^{2}+4ax+4=0$ 无解,
则 $\left\{\begin{aligned}\Delta_{1}&=a^{2}-4\times0=0,\\ \Delta_{2}&=(4a)^{2}-4\times4<0,\end{aligned}\right.$ 解得 a=0.
当 $n(B)=3$ 时, 若 $x^{2}+ax=0$ 有两个相等的实数根, 由上述分析可知 $x^{2}+4ax+4=0$ 无解, 不满足题意.
若 $x^{2}+ax=0$ 有两个不相等的实数根, 即 $x_{1}=0, x_{2}=-a$ , 则
① $x^{2}+4ax+4=0$ 有两个相等且异于方程 $x^{2}+ax=0$ 的根, 则 $\left\{\begin{aligned}\Delta_{1}&=a^{2}-4\times0>0,\\ \Delta_{2}&=(4a)^{2}-4\times4=0,\end{aligned}\right.$ 解得 a=-1 或 1, 经检验均满足题意;
② $x^{2}+4ax+4=0$ 有两个不等的实数根, 且其中一根也是 $x^{2}+ax=0$ 的根, 则 x=-a 是方程 $x^{2}+4ax+4=0$ 的根, 代入得 $a=\pm\frac{2\sqrt{3}}{3}$ , 此时方程 $x^{2}\pm\frac{8\sqrt{3}}{3}x+4=0$ 的判别式 $\Delta_{2}>0$ , 方程 $x^{2}+ax=0$ 的判别式 $\Delta_{1}>0$ , 满足题意.
综上, 实数 a 的所有可能取值为 $-\frac{2\sqrt{3}}{3}, -1,0,1, \frac{2\sqrt{3}}{3}$ , 则 $M=\left\{-\frac{2\sqrt{3}}{3},-1,0,1,\frac{2\sqrt{3}}{3}\right\}$ ,
经检验, 均符合题意.
所以 M 的非空子集的个数为 $2^{5}-1=31$
<!-- answer-source:end -->
