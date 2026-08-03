---
question_id: "node-006:question:5:26"
question_number: "5"
context_key: "node-006"
question_source: "C:\\Mathematics-Knowledge\\Secondary-School-Mathematics-Knowledge-Map\\测试\\新建文件夹\\graph\\01-第一章_集合与常用逻辑用语\\专题1_集合的综合问题\\专题1_集合的综合问题.md"
question_body_sha256: 0d9f628e8ebd89aeff7581192af93a10b1108210f47370030c453602f752afce
answer_status: matched
---

# Question 5

<!-- question-source:start -->
5. (多选) [广西南宁 2025 高一联考] 大数据时代, 需要对数据库进行检索, 检索过程中有时会出现笛卡尔积现象, 而笛卡尔积会产生大量的数据, 对内存、计算资源都会产生巨大压力, 为优化检索软件, 编程人员需要了解笛卡尔积. 已知两个集合 $A$ 和 $B$ , 用 $A$ 中元素为第一元素, $B$ 中元素为第二元素构成有序对, 所有这样的有序对组成的集合叫做 $A$ 与 $B$ 的笛卡尔积, 又称直积, 记为 $A \times B$ , 即 $A \times B = \{(x, y) | x \in A \text{ 且 } y \in B\}$ . 关于任意非空集合 $M, N, T$ , 下列说法错误的是 ( )

A. $M \times N = N \times M$ B. $(M \times N) \times T = M \times (N \times T)$ C. $M \times (N \cup T) \neq (M \times N) \cup (M \times T)$ D. $M \times (N \cap T) = (M \times N) \cap (M \times T)$
<!-- question-source:end -->

## 答案与解析

<!-- answer-source:start -->
5. ABC 【解析】对于 A, 若 $M=\{1\}$ , $N=\{1,2\}$ ，则 $M \times N = \{(1,1), (1,2)\}$ , $N \times M = \{(1,1), (2,1)\}$ ，所以 $M \times N \neq N \times M$ ，故 A 错误；
▶ 敲 黑板：抓住新定义集合的本质，本题中集合 $A \times B$ 是有序对
对于 B，若 $M=\{1\}$ , $N=\{2\}$ , $T=\{3\}$ ,
则 $M \times N = \{(1,2)\}, (M \times N) \times T = \{(1,2), 3\}$ ，而 $M \times (N \times T) = \{(1,2,3)\}$ ，所以 $(M \times N) \times T \neq M \times (N \times T)$ ，故 B 错误；
对于 C，若 $M = \{1\}$ , $N = \{2\}$ , $T = \{3\}$ ，则 $M \times (N \cup T) = \{(1,2), (1,3)\}$ , $M \times N = \{(1,2)\}, M \times T = \{(1,3)\}$ ，所以 $M \times$ $\therefore \Delta = 4(a + 1)^2 - 4(a^2 - 5) = 0,$ 即 $8(a + 3) = 0$ ，解得 $a = -3.$ (2) $\because A \cup B = A, \therefore B \subseteq A = \{1, 2\}$ . 对集合 $B$ 讨论：当 $\Delta < 0$ ，即 $a < -3$ 时， $B = \varnothing$ ，满足条件；当 $\Delta = 0$ ，即 $a = -3$ 时， $B = \{2\}$ ，满足条件；当 $\Delta > 0$ ，即 $a > -3$ 时，要满足条件，必有 $B = \{1, 2\}$ ，由一元二次方程根与系数的关系有 $\left\{ \begin{array}{l} 1 + 2 = -2(a + 1), \\ 1 \times 2 = a^2 - 5, \end{array} \right.$ 此方程组无解，不满足条件，舍去. 综上所述，实数 $a$ 的取值范围是 $\{a \mid a \leqslant -3\}$ .

$(N\cup T)=(M\times N)\cup(M\times T)$ ，故 C 错误；
对于 D，任取元素 $(x,y)\in M\times(N\cap T)$ ，则 $x\in M$ 且 $y\in N\cap T$ ，则 $y\in N$ 且 $y\in T$ ，
于是 $(x,y)\in M\times N$ 且 $(x,y)\in M\times T$ ，即 $(x,y)\in(M\times N)\cap(M\times T)$ ，
反之若任取元素 $(x,y)\in(M\times N)\cap(M\times T)$ ，
则 $(x,y)\in M\times N$ 且 $(x,y)\in M\times T$ ，
因此 $x\in M, y\in N$ 且 $y\in T$ ，即 $x\in M$ 且 $y\in N\cap T$ ，
所以 $(x,y)\in M\times(N\cap T)$ ，即 $M\times(N\cap T)=(M\times N)\cap(M\times T)$ ，故D正确. 故选ABC.
规律方法 集合新定义问题的处理策略
(1) 对集合新定义的理解, 可以通过简单例子及反例, 从特殊到一般来理解;
(2) 把新定义运算转化为熟悉的交、并、补运算;
(3) 利用 Venn 图或数轴将抽象变形象, 寻找突破点.
<!-- answer-source:end -->
