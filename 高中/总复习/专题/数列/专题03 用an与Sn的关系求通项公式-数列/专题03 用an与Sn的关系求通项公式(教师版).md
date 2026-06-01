# 专题03 用 $a_{n}$ 与 $S_{n}$ 的关系求通项公式

# 【基本知识】
$S_{n}$ 与 $a_{n}$ 的关系

已知数列 $\{a_{n}\}$ 的前 $n$ 项和为 $S_{n}$ ，则 $a_{n} = \begin{cases} S_{1}, & n = 1, \\ S_{n} - S_{n-1}, & n \geq 2, \end{cases}$ 这个关系式对任意数列均成立.

注意： $S_{n}$ 与 $a_{n}$ 关系的二重性，即用 $S_{n}$ 与 $a_{n}$ 关系可消去 $a_{n}$ ，也可消去 $S_{n}$ 。（1）正用 $a_{n}=S_{n}-S_{n-1}(n\geq2)$ 消去 $a_{n}$ 转化为只含 $S_{n}$ ， $S_{n-1}$ 的关系式。（2）逆用 $S_{n}-S_{n-1}=a_{n}(n\geq2)$ 消去 $S_{n}$ 转化为只含 $a_{n}$ ， $a_{n-1}$ 的关系式，再求解。

提醒：利用 $a_{n}=S_{n}-S_{n-1}$ 求通项时，应注意 $n\geq2$ 这一前提条件，易忽视验证 n=1 致误.

# 考点一 由 $S_{n} = f(n)$ 求 $a_{n}$ 型

# 【基本方法】

已知 $S_{n} = f(n)$ 求 $a_{n}$ 的方法

已知 $S_{n}=f(n)$ 求 $a_{n}$ 的常用方法是利用 $a_{n}=\left\{\begin{aligned}&S_{1},&n=1,\\ &S_{n}-S_{n-1},&n\geq2.\end{aligned}\right.$ 主要分三个步骤完成：  
（1）当 $n = 1$ 时，在 $S_{n} = f(n)$ 中，令 $n = 1$ ，求得 $a_1 = f(1)$   
（2）当 $n \geqslant 2$ 时，再利用 $a_{n} = S_{n} - S_{n-1} = f(n) - f(n-1) (n \geq 2)$ ，求出 $a_{n} = f(n) - f(n-1)$ 。即当 $n \geq 2$ ， $n \in \mathbf{N}^{*}$ 时的通项公式；  
（3）检查 $a_{1}$ 是否符合 $n \geq 2$ 时 $a_{n}$ 的表达式，如果符合，则可以把数列的通项公式合写成 $a_{n} = f(n) - f(n - 1)$ ;
否则应写成分段的形式，即 $a_{n}=\left\{\begin{aligned}&f(1),&n=1,\\ &f(n)-f(n-1),&n\geq2.\end{aligned}\right.$

# 【基本题型】

[例 1] （1） 已知数列 $\{a_{n}\}$ 的前 n 项和 $S_{n}=n^{2}+2n$ ，则 $a_{n}=$ \_\_\_\_.
答案 $2n + 1$ 解析 当 $n = 1$ 时， $a_1 = S_1 = 3$ 。当 $n \geqslant 2$ 时， $a_n = S_n - S_{n-1} = n^2 + 2n - [(n - 1)^2 + 2(n - 1)] = 2n + 1$ 。由于 $a_1 = 3$ 适合上式， $\therefore a_n = 2n + 1$ 。  
（2）已知数列 $\{a_{n}\}$ 的前 $n$ 项和 $S_{n} = n^{2} + 2n + 1(n\in \mathbf{N}^{*})$ ，则 $a_{n} =$
答案 $\left\{\begin{aligned}4,&n=1,\\ 2n+1,&n\geq2\end{aligned}\right.$ 解析 当 $n\geq2$ 时， $a_{n}=S_{n}-S_{n-1}=2n+1$ ；当 n=1 时， $a_{1}=S_{1}=4\neq2\times1+1$ 。因此 $a_{n}=\left\{\begin{aligned}4,&n=1,\\ 2n+1,&n\geq2.\end{aligned}\right.$  
（3）已知数列 $\{a_{n}\}$ 的前n项和 $S_{n}=3^{n}+1$ ，则 $a_{n}=$ \_\_\_\_.
答案 $\left\{ \begin{array}{l} 4, n = 1, \\ 2 \times 3^{n - 1}, n \geq 2 \end{array} \right.$ 解析 当 $n = 1$ 时， $a_1 = S_1 = 3 + 1 = 4$ ；当 $n \geq 2$ 时， $a_n = S_n - S_{n-1} = (3^n + 1) - (3^n - 1) = 2 \times 3^{n - 1}$ . 当 $n = 1$ 时， $2 \times 3^{1 - 1} = 2 \neq a_1$ ，所以 $a_n = \left\{ \begin{array}{l} 4, n = 1, \\ 2 \times 3^{n - 1}, n \geq 2. \end{array} \right.$

# 【对点精练】

1. 已知数列 $\{a_{n}\}$ 的前 $n$ 项和 $S_{n} = 2n^{2} - 3n$ ，则 $a_{n} =$

1. 答案 $4n - 5$ 解析 $a_1 = S_1 = 2 - 3 = -1$ ，当 $n \geq 2$ 时， $a_n = S_n - S_{n-1} = (2n^2 - 3n) - [2(n - 1)^2 - 3(n - 1)] = 4n - 5$ ，由于 $a_1$ 也适合此等式， $\therefore a_n = 4n - 5$ .

2. 若数列 $\{a_{n}\}$ 的前 $n$ 项和 $S_{n} = 3n^{2} - 2n + 1$ ，则数列 $\{a_{n}\}$ 的通项公式 $a_{n} =$

2. 答案 $\left\{\begin{aligned}&2, n=1,\\ &6n-5, n\geqslant2\end{aligned}\right.$ 解析 当 n=1 时， $a_{1}=S_{1}=3\times1^{2}-2\times1+1=2$ ；当 $n\geqslant2$ 时， $a_{n}=S_{n}-S_{n-1}=3n^{2}-2n+1-[3(n-1)^{2}-2(n-1)+1]=6n-5$ ，显然当 n=1 时，不满足上式．故数列的通项公式为 $a_{n}=\left\{\begin{aligned}&2, n=1,\\ &6n-5, n\geqslant2.\end{aligned}\right.$

3. 若 $S_{n} = 3^{n} + 2n + 1$ ，则数列 $\{a_n\}$ 的通项公式为

3. 答案 $a_{n}=\left\{\begin{aligned}&6,&n=1,\\ &2\cdot3^{n-1}+2,&n\geq2.\end{aligned}\right.$ 解析 因为当 n=1 时， $a_{1}=S_{1}=6$ ；当 $n\geq2$ 时， $a_{n}=S_{n}-S_{n-1}=(3^{n}+2n+1)-[3^{n-1}+2(n-1)+1]=2\cdot3^{n-1}+2$ ，由于 $a_{1}$ 不适合此式，所以 $a_{n}=\left\{\begin{aligned}&6,&n=1,\\ &2\cdot3^{n-1}+2,&n\geq2.\end{aligned}\right.$

4. 已知 $S_{n}$ 为数列 $\{a_{n}\}$ 的前 $n$ 项和，且 $\log_2(S_n + 1) = n + 1$ ，则数列 $\{a_{n}\}$ 的通项公式为

4. 答案 $a_{n}=\left\{\begin{aligned}&3,&n=1,\\ &2^{n},&n\geqslant2.\end{aligned}\right.$ 解析 由 $\log_{2}(S_{n}+1)=n+1$ ，得 $S_{n}+1=2^{n+1}$ ，当 n=1 时， $a_{1}=S_{1}=3$ ；当 $n\geqslant2$ 时， $a_{n}=S_{n}-S_{n-1}=2^{n}$ ，所以数列 $\{a_{n}\}$ 的通项公式为 $a_{n}=\left\{\begin{aligned}&3,&n=1,\\ &2^{n},&n\geqslant2.\end{aligned}\right.$

5. 已知数列 $\{a_{n}\}$ 的前 $n$ 项和 $S_{n} = 2n^{2} + 2n$ ，数列 $\{b_{n}\}$ 的前 $n$ 项和 $T_{n} = 2 - b_{n}$ .  
（1）求数列 $\{a_{n}\}$ 与 $\{b_{n}\}$ 的通项公式;  
（2）设 $c_{n} = a_{n}^{2}\cdot b_{n}$ ，证明：当且仅当 $n\geqslant 3$ 时， $c_{n + 1} <   c_n$

5. 解析 （1） 当 n=1 时， $a_{1}=S_{1}=4$ .

对于 $n > 2$ ，有 $a_{n} = S_{n} - S_{n - 1} = 2n(n + 1) - 2(n - 1)n = 4n$ ，又当 $n = 1$ 时， $a_1 = 4$ 适合上式，
故 $\{a_{n}\}$ 的通项公式 $a_{n} = 4n$ ，将 $n = 1$ 代入 $T_{n} = 2 - b_{n}$ ，得 $b_{1} = 2 - b_{1}$ ，故 $T_{1} = b_{1} = 1$

对于 $n \geq 2$ ，由 $T_{n-1} = 2 - b_{n-1}$ ， $T_{n} = 2 - b_{n}$ ，得 $b_{n} = T_{n} - T_{n-1} = -(b_{n} - b_{n-1})$ ， $b_{n} = \frac{1}{2} b_{n-1}$ ，
所以数列 $\{b_{n}\}$ 是以1为首项， $\frac{1}{2}$ 为公比的等比数列，故 $b_{n}=2^{1-n}$ .  
（2）法一 由 $c_{n} = a_{n}^{2}\cdot b_{n} = n^{2}2^{5 - n}$ ，得 $\frac{c_{n + 1}}{c_n} = \frac{1}{2}\left(1 + \frac{1}{n}\right)^2.$
当且仅当 $n \geq 3$ 时， $1 + \frac{1}{n} \leq \frac{4}{3} < \sqrt{2}$ ，即 $\frac{c_{n+1}}{c_n} < 1$ ，即 $c_{n+1} < c_n$ .

法二 由 $c_{n} = a_{n}^{2}\cdot b_{n} = n^{2}2^{5 - n}$ ，得 $c_{n + 1} - c_n = 2^{4 - n}[(n + 1)^2 -2n^2 ] = 2^{4 - n}[-(n - 1)^2 +2].$
当且仅当 $n > 3$ 时， $c_{n+1} - c_n < 0$ ，即 $c_{n+1} < c_n$ .

考点二 由 $a_1 + a_2 + a_3 + \ldots + a_n = f(n)$ 求 $a_n$ 型

# 【基本方法】

# 已知 $S_{n}$ 求 $a_{n}$ 的方法

已知 $a_{1}+a_{2}+a_{3}+\ldots+a_{n}=f(n)$ 求 $a_{n}$ 的常用方法是利用 $a_{n}=\left\{\begin{aligned}&S_{1},&n=1,\\ &S_{n}-S_{n-1},&n\geq2.\end{aligned}\right.$ 主要分三个步骤完成：  
（1）当 n=1 时，求得 $a_{1}=f(1)$ ;  
（2）当 $n \geqslant 2$ 时，在 $a_1 + a_2 + a_3 + \ldots + a_n = f(n)$ 中用 $n - 1$ 替换 $n$ 得到一个新的关系式 $a_1 + a_2 + a_3 + \ldots + a_n - 1 = f(n - 1)$ ，两式相减得到 $a_n = f(n) - f(n - 1) (n \geq 2)$ ，便可求出当 $n \geq 2$ ， $n \in \mathbb{N}^*$ 时的通项公式；  
（3）检查 $a_1$ 是否符合 $n \geq 2$ 时 $a_n$ 的表达式，如果符合，则可以把数列的通项公式合写成 $a_n = f(n) - f(n - 1)$ ；否则应写成分段的形式，即 $a_n = \begin{cases} f(1), & n = 1, \\ f(n) - f(n - 1), & n \geq 2. \end{cases}$

# 【基本题型】

[例2] （1）已知正项数列 $\{a_{n}\}$ 中， $\sqrt{a_1} + \sqrt{a_2} + \ldots + \sqrt{a_n} = \frac{n(n + 1)}{2}$ ，则数列 $\{a_{n}\}$ 的通项公式为（）

A. $a_{n} = n$

B. $a_{n} = n^{2}$

C. $a_{n}=\frac{n}{2}$

D. $a_{n}=\frac{n^{2}}{2}$
答案 B 解析 当 n=1 时， $\sqrt{a_{1}}=\frac{1\times2}{2}=1,\ a_{1}=1$ 。当 $n\geq2$ 时， $\because\sqrt{a_{1}}+\sqrt{a_{2}}+\ldots+\sqrt{a_{n}}=\frac{n(n+1)}{2},\ \therefore\sqrt{a_{1}}+\sqrt{a_{2}}+\ldots+\sqrt{a_{n-1}}=\frac{n(n-1)}{2}$ ，两式相减得 $\sqrt{a_{n}}=\frac{n(n+1)}{2}-\frac{n(n-1)}{2}=n(n\geq2),\ \therefore a_{n}=n^{2}(n\geq2)$ ，①，又当 n=1 时， $a_{1}=1$ ，适合①式， $\therefore a_{n}=n^{2},\ n\in N^{*}$ 。故选 B.  
（2）已知数列 $\{a_{n}\}$ 满足 $a_{1}+2a_{2}+3a_{3}+\ldots+na_{n}=2^{n}$ ，则 $a_{n}=$ \_\_\_\_.
答案 $\left\{\begin{aligned}&2, &n=1,\\&\frac{2^{n-1}}{n}, &n\geq2.\end{aligned}\right.$ 解析 当 n=1 时， $a_{1}=2^{1}=2,\quad\because a_{1}+2a_{2}+3a_{3}+\ldots+na_{n}=2^{n},\quad①$ ，故 $a_{1}+2a_{2}+3a_{3}+\ldots+(n-1)a_{n-1}=2^{n-1}(n\geq2),\quad②$ ，由①-②得 $na_{n}=2^{n}-2^{n-1}=2^{n-1},\quad\therefore a_{n}=\frac{2^{n-1}}{n}(n\geq2).$ 显然当 n=1 时不满足上式， $\therefore a_{n}=\left\{\begin{aligned}&2, &n=1,\\&\frac{2^{n-1}}{n}, &n\geq2.\end{aligned}\right.$

[例 3] 记 $m=\frac{d_{1}a_{1}+d_{2}a_{2}+\ldots+d_{n}a_{n}}{n}$ ，若 $\{d_{n}\}$ 是等差数列，则称 m 为数列 $\{a_{n}\}$ 的“ $d_{n}$ 等差均值”；若 $\{d_{n}\}$ 是等比数列，则称 m 为数列 $\{a_{n}\}$ 的“ $d_{n}$ 等比均值”。已知数列 $\{a_{n}\}$ 的“2n-1 等差均值”为 2，数列 $\{b_{n}\}$ 的“ $3^{n-1}$ 等比均值”为 3。记 $c_{n}=\frac{2}{a_{n}}+k\log_{3}b_{n}$ ，数列 $\{c_{n}\}$ 的前 n 项和为 $S_{n}$ ，若对任意的正整数 n 都有 $S_{n}\leq S_{6}$ ，求实数 k 的取值范围。
解析 由题意得 $2=\frac{a_{1}+3a_{2}+\ldots+(2n-1)a_{n}}{n}$ ，所以 $a_{1}+3a_{2}+\ldots+(2n-1)a_{n}=2n$ ，
所以 $a_{1}+3a_{2}+\ldots+(2n-3)a_{n-1}=2n-2(n\geq2,\ n\in\mathbf{N}_{+})$ ,

两式相减得 $a_{n}=\frac{2}{2n-1}(n\geq2,\ n\in\mathbf{N}_{+})$ .
当 n=1 时， $a_{1}=2$ ，符合上式，所以 $a_{n}=\frac{2}{2n-1}(n\in\mathbf{N}_{+})$ .
又由题意得 $3=\frac{b_{1}+3b_{2}+\ldots+3^{n-1}b_{n}}{n}$ ，所以 $b_{1}+3b_{2}+\ldots+3^{n-1}b_{n}=3n$ ，
所以 $b_{1}+3b_{2}+\ldots+3^{n-2}b_{n-1}=3n-3(n\geq2,\ n\in\mathbf{N}_{+})$ ,

两式相减得 $b_{n}=3^{2^{-n}}(n\geq2,\ n\in\mathbf{N}_{+})$ .
当 n=1 时， $b_{1}=3$ ，符合上式，所以 $b_{n}=3^{2-n}(n\in\mathbf{N}_{+})$ .
所以 $c_{n}=(2-k)n+2k-1$ .
因为对任意的正整数 n 都有 $S_{n} \leq S_{6}$ ，所以 $\left\{\begin{aligned} c_{6} &\geq 0, \\ c_{7} &\leq 0, \end{aligned}\right.$ 解得 $\frac{13}{5} \leq k \leq \frac{11}{4}$ ,
所以实数 k 的取值范围为 $\left[\frac{13}{5}, \frac{11}{4}\right]$ .

# 【对点精练】

1. 已知数列 $\{a_{n}\}$ 满足 $a_{1} + 2a_{2} + 3a_{3} + \ldots + na_{n} = n + 1 (n \in \mathbb{N}^{*})$ ，则数列 $\{a_{n}\}$ 的通项公式为 \_\_\_\_.

1. 答案 $a_{n}=\left\{\begin{aligned}&2,&n=1,\\ &\frac{1}{n},&n\geq2\end{aligned}\right.$ 解析 已知 $a_{1}+2a_{2}+3a_{3}+\ldots+na_{n}=n+1$ ，将 n=1 代入，得 $a_{1}=2$ ；当 $n\geq2$ 时，将 n-1 代入得 $a_{1}+2a_{2}+3a_{3}+\ldots+(n-1)a_{n-1}=n$ ，两式相减得 $na_{n}=(n+1)-n=1,\therefore a_{n}=\frac{1}{n},\therefore a_{n}=2,$ $=\left\{\begin{aligned}&2,&n=1,\\ &\frac{1}{n},&n\geq2.\end{aligned}\right.$

2. 设数列 $\{a_{n}\}$ 满足 $a_{1}+3a_{2}+\cdots+(2n-1)a_{n}=2^{n}$ ，则 $a_{n}=$ \_\_\_\_.

2. 答案 $\left\{\begin{aligned}&2, &n=1,\\&\frac{2^{n-1}}{2n-1}, &n\geqslant2\end{aligned}\right.$ 解析 当 n=1 时， $a_{1}=2^{1}=2.\quad\because a_{1}+3a_{2}+\cdots+(2n-1)a_{n}=2^{n},\quad①,\quad\therefore a_{1}+3a_{2}+\cdots+(2n-1)a_{n}=2^{n}$
$+\cdots+(2n-3)a_{n-1}=2^{n-1}(n\geqslant2)$ ，②，由①-②得， $(2n-1)\cdot a_{n}=2^{n}-2^{n-1}=2^{n-1}$ ， $\therefore a_{n}=\frac{2^{n-1}}{2n-1}(n\geqslant2)$ 。显然n=1时不满足上式， $\therefore a_{n}=\left\{\begin{aligned}&2, &n=1,\\&\frac{2^{n-1}}{2n-1}, &n\geqslant2.\end{aligned}\right.$

3. 已知数列 $\{a_{n}\}$ 满足 $2a_{1} + 2^{2}a_{2} + 2^{3}a_{3} + \ldots + 2^{n}a_{n} = 4^{n} - 1$ ，则 $\{a_{n}\}$ 的通项公式是 \_\_\_\_.

3. 答案 $a_{n} = \frac{3}{4} \cdot 2^{n}$ 解析 因为数列 $\{a_{n}\}$ 满足 $2a_{1} + 2^{2}a_{2} + 2^{3}a_{3} + \ldots + 2^{n}a_{n} = 4^{n} - 1$ ，所以当 $n = 1$ 时， $2a_{1} = 4 - 1$ ，解得 $a_{1} = \frac{3}{2}$ ；当 $n \geq 2$ 时， $2a_{1} + 2^{2}a_{2} + 2^{3}a_{3} + \ldots + 2^{n-1}a_{n-1} = 4^{n-1} - 1$ ，与题目条件中的等式相减，得到 $2^{n}a_{n} = 4^{n} - 4^{n-1}$ ，整理得 $a_{n} = \frac{3}{4} \cdot 2^{n}$ ，该表达式对 $n = 1$ 也成立，所以数列 $\{a_{n}\}$ 的通项公式为 $a_{n} = \frac{3}{4} \cdot 2^{n}$ .

# 考点三 由 $f(a_{n}, S_{n}) = 0$ 消去 $S_{n}$ 型

# 【基本方法】

# 已知 $S_{n}$ 求 $a_{n}$ 的方法

已知 $f(a_{n}, S_{n})=0$ 求 $a_{n}$ ，如果能消去 $S_{n}$ ，则利用 $a_{n}=\left\{\begin{aligned}&S_{1},&n=1,\\ &S_{n}-S_{n-1},&n\geq2.\end{aligned}\right.$ 消去 $S_{n}$ ，主要分四个步骤完成：  
（1）当 $n = 1$ 时，先利用 $a_1 = S_1$ ，求得 $a_1$  
（2）当 $n \geq 2$ 时，用 $n - 1$ 替换 $f(a_{n}, S_{n}) = 0$ 中的 $n$ 得到一个新的关系式 $f(a_{n-1}, S_{n-1}) = 0$ ，两式相减，再逆用 $a_{n} = S_{n} - S_{n-1}(n \geq 2)$ 便可得到当 $n \geq 2$ ， $n \in \mathbf{N}^{*}$ 时数列 $\{a_{n}\}$ 的一个递推公式；  
（3）借助各类递推公式求通项公式的方法求出当 $n \geq 2, n \in \mathbf{N}^{*}$ 时的通项公式；  
（4）看 $a_1$ 是否符合 $n \geq 2$ 时 $a_n$ 的表达式，如果符合，则可以把数列的通项公式合写；否则应写成分段的形式.

# 【基本题型】

[例 4] （1） 已知数列 $\{a_{n}\}$ 的前 n 项和为 $S_{n}$ ，且满足 $a_{n} + S_{n} = 1 (n \in \mathbf{N}^{*})$ ，则通项 $a_{n} =$ \_\_\_\_ .
答案 $\frac{1}{2^n}$ 解析 $\because a_{n} + S_{n} = 1$ ，①， $\therefore a_{1} = \frac{1}{2},a_{n - 1} + S_{n - 1} = 1(n\geqslant 2)$ ，②，由 $① - ②$ ，得 $a_{n} - a_{n - 1} + a_{n}$ $= 0$ ，即 $\frac{a_n}{a_{n - 1}} = \frac{1}{2} (n\geqslant 2)$ ，∴数列 $\{a_n\}$ 是首项为 $\frac{1}{2}$ ，公比为 $\frac{1}{2}$ 的等比数列，则 $a_{n} = \frac{1}{2}\times \left(\frac{1}{2}\right)^{n - 1} = \frac{1}{2^{n}}.$  
（2）(2013·全国 I) 若数列 $\{a_{n}\}$ 的前 n 项和 $S_{n}=\frac{2}{3}a_{n}+\frac{1}{3}$ ，则 $\{a_{n}\}$ 的通项公式是 $a_{n}=$ \_\_\_\_.
答案 $(-2)^{n - 1}$ 解析 当 $n = 1$ 时， $a_1 = 1$ ；当 $n \geqslant 2$ 时， $a_n = S_n - S_{n-1} = \frac{2}{3} a_n - \frac{2}{3} a_{n-1}$ ，故 $\frac{a_n}{a_{n-1}} = -2$ ，故 $a_n = (-2)^{n-1}$ 。当 $n = 1$ 时，也符合 $a_n = (-2)^{n-1}$ 。综上， $a_n = (-2)^{n-1}$ 。  
（3）设数列 $\{a_{n}\}$ 的前n项和为 $S_{n}$ ，若 $a_{1}=1,\quad a_{n+1}=S_{n}(n\in\mathbf{N}^{*})$ ，则通项公式 $a_{n}=$ \_\_\_\_.
答案 $\left\{ \begin{array}{l} 1, n = 1, \\ 2^{n - 2}, n \geqslant 2. \end{array} \right.$ 解析 由 $a_{n + 1} = S_n$ ①，可得 $a_{n} = S_{n - 1}(n \geqslant 2)$ ②，①-②得 $a_{n + 1} - a_{n} = S_{n} - S_{n - 1} = a_{n}(n \geqslant 2)$ ，即 $\frac{a_{n + 1}}{a_n} = 2(n \geqslant 2)$ ，又 $a_{2} = S_{1} = 1$ ，所以 $\frac{a_2}{a_1} = 1 \neq 2$ ，则数列 $\{a_n\}$ 从第二项起是以1为首项2为公比的等比数列，所以 $a_{n} = \left\{ \begin{array}{ll} 1, & n = 1, \\ 2^{n - 2}, & n \geqslant 2. \end{array} \right.$  
（4）已知数列 $\{a_{n}\}$ 的首项 $a_1 = 1$ ，前 $n$ 项和为 $S_{n}$ ，且 $S_{n + 1} = 4a_{n} + 2(n\in \mathbf{N}^{*})$ ，则数列 $\{a_{n}\}$ 的通项公式是 $a_{n}$ $=$ \_\_\_\_.
答案 $(3n - 1)2^{n - 2}$ 解析 当 $n\geq 2$ 时， $S_{n + 1} = 4a_{n} + 2$ ， $S_{n} = 4a_{n - 1} + 2$ 。两式相减，得 $a_{n + 1} = 4a_n - 4a_{n - 1}$ 将之变形为 $a_{n + 1} - 2a_{n} = 2(a_{n} - 2a_{n - 1})$ 。所以 $\{a_{n + 1} - 2a_n\}$ 是公比为2的等比数列。又 $a_1 + a_2 = S_2 = 4a_1 + 2$ ， $a_1 = 1$ ，得 $a_2 = 5$ ，则 $a_2 - 2a_1 = 3$ 。所以 $a_{n + 1} - 2a_n = 3\cdot 2^{n - 1}$ 。两边同除以 $2^{n + 1}$ ，得 $\frac{a_{n + 1}}{2^{n + 1}} -\frac{a_n}{2^n} = \frac{3}{4}$ ，所以 $\left\{\frac{a_n}{2^n}\right\}$ 是首项为 $\frac{a_1}{2} = \frac{1}{2}$ ，公差为 $\frac{3}{4}$ 的等差数列。所以 $\frac{a_n}{2^n} = \frac{1}{2} +\frac{3}{4} (n - 1) = \frac{3}{4} n - \frac{1}{4}$ ，所以 $a_{n} = (3n - 1)2^{n - 2}$  
（5）若 $S_{n}$ 为数列 $\{a_{n}\}$ 的前 n 项和，且 $2S_{n}=a_{n+1}a_{n},\quad a_{1}=4$ ，则数列 $\{a_{n}\}$ 的通项公式为 $a_{n}=$ \_\_\_\_.
答案 $\left\{\begin{aligned}n+3,&n\text{为奇数,}\\ n,&n\text{为偶数.}\end{aligned}\right.$ 解析 因为 $2S_{n}=a_{n+1}a_{n},\quad a_{1}=4$ ，所以 n=1 时， $2\times4=4a_{2}$ ，解得 $a_{2}=$

2. $n \geqslant 2$ 时， $2S_{n-1} = a_n a_{n-1}$ ，可得 $2a_n = a_{n+1}a_n - a_na_{n-1}$ ，所以 $a_n = 0$ （舍去）或 $a_{n+1} - a_{n-1} = 2$ 。 $n \geqslant 2$ 时， $a_{n+1} - a_{n-1} = 2$ ，可得数列 $\{a_n\}$ 的奇数项与偶数项分别为等差数列。所以 $a_{2k-1} = 4 + 2(k-1) = 2k + 2$ ， $k \in \mathbf{N}^*$ ， $a_{2k} = 2 + 2(k-1) = 2k$ ， $k \in \mathbf{N}^*$ 。所以 $a_n = \begin{cases} n + 3, & n \text{为奇数}, \\ n, & n \text{为偶数}. \end{cases}$

[例 5] 设数列 $\{a_{n}\}$ 的前 n 项和为 $S_{n}$ ，数列 $\{S_{n}\}$ 的前 n 项和为 $T_{n}$ ，满足 $T_{n}=2S_{n}-n^{2}$ ， $n\in N^{*}$ .  
（1）求 $a_{1}$ 的值;  
（2）求数列 $\{a_{n}\}$ 的通项公式.
解析 （1）令 $n = 1$ ， $T_{1} = 2S_{1} - 1$ ， $\because T_{1} = S_{1} = a_{1}$ ， $\therefore a_1 = 2a_1 - 1$ ， $\therefore a_1 = 1$  
（2） $n \geq 2$ 时，则 $S_{n} = T_{n} - T_{n-1} = 2S_{n} - n^{2} - [2S_{n-1} - (n - 1)^{2}] = 2(S_{n} - S_{n-1}) - 2n + 1 = 2a_{n} - 2n + 1$ .
因为当 $n = 1$ 时， $a_1 = S_1 = 1$ 也满足上式，所以 $S_n = 2a_n - 2n + 1 (n \in \mathbf{N}^*)$ .
当 $n \geq 2$ 时， $S_{n-1} = 2a_{n-1} - 2(n-1) + 1$ ，两式相减得 $a_n = 2a_n - 2a_{n-1} - 2$
所以 $a_{n} = 2a_{n - 1} + 2(n > 2)$ ，所以 $a_{n} + 2 = 2(a_{n - 1} + 2)$
因为 $a_1 + 2 = 3 \neq 0$ ，所以数列 $\{a_n + 2\}$ 是以3为首项，2为公比的等比数列.
所以 $a_{n}+2=3\times2^{n-1}$ ，所以 $a_{n}=3\times2^{n-1}-2$ 。
当 n=1 时也成立，所以 $a_{n}=3\times2^{n-1}-2$ .

# 【对点精练】

1. 记 $S_{n}$ 为数列 $\{a_{n}\}$ 的前 $n$ 项和．若 $S_{n} = 2a_{n} + 1$ ，则 $a_{n} =$

1. 答案 $-2^{n-1}$ 解析 $\because S_n = 2a_n + 1$ , 当 $n \geq 2$ 时, $S_{n-1} = 2a_{n-1} + 1$ , $\therefore a_n = S_n - S_{n-1} = 2a_n - 2a_{n-1}$ , 即 $a_n = 2a_{n-1}$ . 当 $n = 1$ 时, $a_1 = S_1 = 2a_1 + 1$ , 得 $a_1 = -1$ . $\therefore$ 数列 $\{a_n\}$ 是首项 $a_1$ 为 $-1$ , 公比 $q$ 为 2 的等比数列, $\therefore a_n = -1 \times 2^{n-1} = -2^{n-1}$ .

2. 已知数列 $\{a_{n}\}$ 的前 $n$ 项和为 $S_{n}$ ，若 $S_{n} = 2a_{n} - 4$ ， $(n \in \mathbf{N}^{*})$ ，则 $a_{n}$

2. 答案 $2^{n+1}$ 解析 当 $n \geq 2$ 时， $S_{n+1} = 2a_{n+1} - 4$ ，又由 $S_n = 2a_n - 4$ 可得 $a_{n+1} = 2a_{n+1} - 2a_n$ ，即 $a_{n+1} = 2a_n$ ， $a_1 = S_1 = 2a_1 - 4$ ，得 $a_1 = 4$ ，所以 $a_n = 4 \cdot 2^{n-1} = 2^{n+1}$ .

3. 已知数列 $\{a_{n}\}$ 的前 $n$ 项和为 $S_{n}, a_{1} = 1, a_{n+1} = 2S_{n} + 1, n \in \mathbf{N}^{*}$ ，则数列 $\{a_{n}\}$ 的通项公式是 $a_{n} =$

3. 答案 $3^{n-1}$ 解析 因为 $a_{n+1} = 2S_n + 1$ ，当 $n \geqslant 2$ 时， $a_n = 2S_{n-1} + 1$ ，两式相减得 $a_{n+1} - a_n = 2a_n$ ，即 $a_n + 1 = 3a_n$ ，又 $a_1 = 1$ ， $a_2 = 2S_1 + 1 = 3$ ，所以 $\frac{a_2}{a_1} = 3$ ，从而 $\{a_n\}$ 是首项为 1，公比为 3 的等比数列，所以 $a_n = 3^{n-1}$ .

4. 已知数列 $\{a_{n}\}$ 的前 $n$ 项和为 $S_{n}$ ，且 $a_{1} = 1$ ， $2S_{n} = a_{n}a_{n + 1}(n\in \mathbf{N}^{*})$ ，则 $a_{n} =$

4. 答案 $n$ 解析 由 $2S_{n} = a_{n}a_{n + 1}$ 可知 $2S_{n - 1} = a_{n - 1}a_{n}(n\geqslant 2)$ ，两式相减得 $2a_{n} = a_{n}a_{n + 1} - a_{n - 1}a_{n} = a_{n}(a_{n + 1}-$ $a_{n - 1})$ ，因为 $a_1 = 1$ ，所以 $a_{n}\neq 0$ ， $2 = a_{n + 1} - a_{n - 1}$ ，又因为 $a_1 = 1$ ， $2S_1 = a_1a_2$ ，所以 $a_2 = 2$ ，结合 $a_{n + 1} - a_{n - 1}$ $= 2$ ，所以 $a_{n} - a_{n - 1} = 1$ ，数列 $\{a_n\}$ 是以1为公差，1为首项的等差数列，所以 $a_{n} = n$ 。

5. （1）已知数列 $\{a_{n}\}$ 满足 $a_{1}+2a_{2}+3a_{3}+4a_{4}+\cdots+na_{n}=n$ ，求 $a_{n}$ ;  
（2）已知数列 $\{a_{n}\}$ 的前n项和为 $S_{n}$ ，若 $a_{n}>0,\quad S_{n}>1$ ，且 $6S_{n}=(a_{n}+1)(a_{n}+2)$ ，求 $a_{n}$ .

5. 解析 （1） 设 $a_{1} + 2a_{2} + 3a_{3} + 4a_{4} + \ldots + na_{n} = T_{n}$ ,
当 n=1 时， $a_{1}=T_{1}=1$ ，当 $n\geq2$ 时， $na_{n}=T_{n}-T_{n-1}=n-(n-1)=1$ ，
因此 $a_{n}=\frac{1}{n}$ ，而 $a_{1}=1$ ，也满足此等式，所以 $a_{n}=\frac{1}{n}$ .  
（2）当 $n = 1$ 时， $a_1 = S_1 = \frac{1}{6} (a_1 + 1)(a_1 + 2)$ ，即 $a_1^2 - 3a_1 + 2 = 0$ 。解得 $a_1 = 1$ 或 $a_1 = 2$ 。
因为 $a_{1}=S_{1}>1$ ，所以 $a_{1}=2$ 。
当 $n \geq 2$ 时， $a_{n} = S_{n} - S_{n-1} = \frac{1}{6}(a_{n} + 1)(a_{n} + 2) - \frac{1}{6}(a_{n-1} + 1)(a_{n-1} + 2)$ ，
所以 $(a_{n} - a_{n - 1} - 3)(a_{n} + a_{n - 1}) = 0$ ，因为 $a_{n} > 0$ ，所以 $a_{n} + a_{n - 1} > 0$ ，所以 $a_{n} - a_{n - 1} = 3$ 所以数列 $\{a_n\}$ 是以2为首项，3为公差的等差数列．所以 $a_{n} = 3n - 1$

6. 已知 $S_{n}$ 为正项数列 $\{a_{n}\}$ 的前 $n$ 项和，且满足 $S_{n} = \frac{1}{2} a_{n}^{2} + \frac{1}{2} a_{n}(n \in \mathbf{N}^{*})$ .  
（1）求 $a_{1}$ ， $a_{2}$ ， $a_{3}$ ， $a_{4}$ 的值；  
（2）求数列 $\{a_{n}\}$ 的通项公式.

6. 解析 （1） 由 $S_{n} = \frac{1}{2} a_{n}^{2} + \frac{1}{2} a_{n} (n \in \mathbf{N}^{*})$ ，可得 $a_{1} = \frac{1}{2} a_{1}^{2} + \frac{1}{2} a_{1}$ ，解得 $a_{1} = 1$
$S_{2}=a_{1}+a_{2}=\frac{1}{2}a_{2}^{2}+\frac{1}{2}a_{2}$ ，解得 $a_{2}=2$ ，同理， $a_{3}=3$ ， $a_{4}=4$ .  
（2） $S_{n}=\frac{1}{2}a_{n}^{2}+\frac{a_{n}}{2}$ ，①，当 $n\geq2$ 时， $S_{n-1}=\frac{1}{2}a_{n-1}^{2}+\frac{1}{2}a_{n-1}$ ，②

①-②得 $(a_{n} - a_{n - 1} - 1)(a_{n} + a_{n - 1}) = 0$ ，由于 $a_{n} + a_{n - 1}\neq 0$ ，所以 $a_{n} - a_{n - 1} = 1$
又由（1）知 $a_1 = 1$ ，故数列 $\{a_n\}$ 为首项为1，公差为1的等差数列，故 $a_{n} = n$

7. 若数列 $\{a_{n}\}$ 的前 $n$ 项和为 $S_{n}$ ，且满足 $a_{n} + 2S_{n}S_{n - 1} = 0(n\geqslant 2)$ ， $a_1 = \frac{1}{2}$ .  
（1）求证： $\left\{\frac{1}{S_{n}}\right\}$ 成等差数列；  
（2）求数列 $\{a_{n}\}$ 的通项公式.

7. 解析 （1） 当 $n \geq 2$ 时，由 $a_{n} + 2S_{n}S_{n-1} = 0$ ，得 $S_{n} - S_{n-1} = -2S_{n}S_{n-1}$ ，所以 $\frac{1}{S_n} - \frac{1}{S_{n-1}} = 2$
又 $\frac{1}{S_1} = \frac{1}{a_1} = 2$ ，故 $\left\{\frac{1}{S_n}\right\}$ 是首项为2，公差为2的等差数列.  
（2）由（1）可得 $\frac{1}{S_{n}}=2n,\quad\therefore S_{n}=\frac{1}{2n}.$
当 $n \geq 2$ 时， $a_n = S_n - S_{n-1} = \frac{1}{2n} - \frac{1}{2(n-1)} = \frac{n-1-n}{2n(n-1)} = -\frac{1}{2n(n-1)}$ .
当 n=1 时， $a_{1}=\frac{1}{2}$ 不适合上式．故 $a_{n}=\left\{\begin{aligned}\frac{1}{2},&n=1,\\ -\frac{1}{2n(n-1)},&n\geq2.\end{aligned}\right.$

8. 设数列 $\{a_{n}\}$ 的首项 $a_1 = \frac{3}{2}$ ，前 $n$ 项和为 $S_{n}$ ，且满足 $2a_{n + 1} + S_n = 3(n\in \mathbf{N}^*)$  
（1）求 $a_2$ 及 $a_n$ ;  
（2）求证： $a_{n}S_{n}$ 的最大值为 $\frac{9}{4}$ .

8. 解析 （1）由题意得 $2a_{2} + S_{1} = 3$ ，即 $2a_{2} + a_{1} = 3$ ，所以 $a_{2} = \frac{3 - a_{1}}{2} = \frac{3}{4}$ .
当 $n \geqslant 2$ 时，由 $2a_{n+1} + S_n = 3$ ，得 $2a_n + S_{n-1} = 3$ ，两式相减得 $2a_{n+1} - a_n = 0$ ，即 $a_{n+1} = \frac{1}{2}a_n$ .
因为 $a_{1}=\frac{3}{2}$ ， $a_{2}=\frac{3}{4}$ ，所以 $a_{2}=\frac{1}{2}a_{1}$ ，即当 n=1 时， $a_{n+1}=\frac{1}{2}a_{n}$ 也成立.
所以 $\{a_{n}\}$ 是以 $\frac{3}{2}$ 为首项， $\frac{1}{2}$ 为公比的等比数列，所以 $a_{n}=\frac{3}{2^{n}}$ .  
（2）因为 $2a_{n + 1} + S_n = 3$ ，且 $a_{n + 1} = \frac{1}{2} a_n$ ，所以 $S_{n} = 3 - 2a_{n + 1} = 3 - a_{n}$
于是， $a_{n}S_{n} = a_{n}(3 - a_{n})\leqslant \left[\frac{a_{n} + (3 - a_{n})}{2}\right]^{2} = \frac{9}{4},$ 当且仅当 $a_{n} = \frac{3}{2}$ ，即 $n = 1$ 时等号成立.
故 $a_{n}S_{n}$ 的最大值为 $\frac{9}{4}$ .

考点四 由 $f(a_{n}, S_{n}) = 0$ 消去 $a_{n}$ 型

# 【基本方法】

已知 $S_{n}$ 求 $a_{n}$ 的方法

已知 $f(a_{n}, S_{n}) = 0$ 求 $a_{n}$ ，如果不能消去 $S_{n}$ ，则利用 $a_{n} = \begin{cases} S_{1}, & n = 1, \\ S_{n} - S_{n-1}, & n \geq 2. \end{cases}$ 消去 $a_{n}$ ，先求出 $S_{n}$ ，再求 $a_{n}$ ，主要分五个步骤完成：  
（1）当 n=1 时，先利用 $a_{1}=S_{1}$ ，求得 $a_{1}$ ;  
（2）当 $n \geq 2$ 时，用 $a_{n} = \begin{cases} S_{1}, & n = 1, \\ S_{n} - S_{n-1}, & n \geq 2. \end{cases}$ 消去 $a_{n}$ ，便可得到当 $n \geq 2$ ， $n \in \mathbf{N}^{*}$ 时数列 $\{S_{n}\}$ 的一个递推公式；  
（3）借助各类递推公式求通项公式的方法求出当 $n \geq 2$ ， $n \in N^{*}$ 时数列 $\{S_{n}\}$ 的通项公式；  
（4）此时问题转化为由 $S_{n}=f(n)$ 求 $a_{n}$ 型，求出当 $n\geq2,\quad n\in N^{*}$ 时数列 $\{a_{n}\}$ 的通项公式；  
（5）看 $a_1$ 是否符合 $n \geq 2$ 时 $a_n$ 的表达式，如果符合，则可以把数列的通项公式合写；否则应写成分段的形式.

# 【基本题型】

[例6] （1）设数列 $\{a_{n}\}$ 的前 $n$ 项和为 $S_{n}$ ，若 $a_{1} = 3$ 且当 $n \geqslant 2$ 时， $2a_{n} = S_{n} \cdot S_{n-1}(n \in \mathbf{N}^{*})$ ，则数列 $\{a_{n}\}$ 的通项

公式 $a_{n} =$
答案 $\left\{ \begin{array}{l}3, n = 1,\\ \frac{18}{(5 - 3n)(8 - 3n)}, n\geqslant 2 \end{array} \right.$ 解析 当 $n\geqslant 2$ 时，由 $2a_{n} = S_{n}\cdot S_{n - 1}$ 可得 $2(S_{n} - S_{n - 1}) = S_{n}\cdot S_{n - 1},\therefore \frac{1}{S_{n - 1}}$ $-\frac{1}{S_n} = \frac{1}{2}$ 即 $\frac{1}{S_n} -\frac{1}{S_{n - 1}} = -\frac{1}{2},\therefore$ 数列 $\left\{\frac{1}{S_n}\right\}$ 是首项为 $\frac{1}{3}$ ，公差为 $-\frac{1}{2}$ 的等差数列， $\therefore \frac{1}{S_n} = \frac{1}{3} +\left(-\frac{1}{2}\right)\cdot (n - 1) = \frac{5 - 3n}{6},$ $\therefore S_n = \frac{6}{5 - 3n}.$ 当 $n\geqslant 2$ 时， $a_{n} = \frac{1}{2} S_{n}S_{n - 1} = \frac{1}{2}\times \frac{6}{5 - 3n}\times \frac{6}{5 - 3(n - 1)} = \frac{18}{(5 - 3n)(8 - 3n)}$ 又 $a_1 = 3,\therefore a_n =$ $\left\{ \begin{array}{ll}3,n = 1,\\ \frac{18}{(5 - 3n)(8 - 3n)}, & n\geqslant 2. \end{array} \right.$  
（2）设 $S_{n}$ 是数列 $\{a_{n}\}$ 的前 n 项和，且 $a_{1}=-1,\quad a_{n+1}=S_{n}S_{n+1}$ ，则下列结论正确的是 \_\_\_\_.

① $a_{n}=\frac{1}{n(n-1)}$

② $a_{n}=\begin{cases}-1,\ n=1,\\\frac{1}{n(n-1)},\ n\geqslant2\end{cases}$

③ $S_{n} = -\frac{1}{n}$

④数列 $\left\{\frac{1}{S_{n}}\right\}$ 是等差数列
答案 ②③④ 解析 $\because a_{n+1} = S_n \cdot S_{n+1} = S_{n+1} - S_n$ ，两边同除以 $S_{n+1} \cdot S_n$ ，得 $\frac{1}{S_{n+1}} - \frac{1}{S_n} = -1$ 。 $\therefore \left\{\frac{1}{S_n}\right\}$ 是以 -1 为首项， $d = -1$ 的等差数列，即 $\frac{1}{S_n} = -1 + (n-1) \times (-1) = -n$ ， $\therefore S_n = -\frac{1}{n}$ 。当 $n \geqslant 2$ 时， $a_n = S_n - S_{n-1} = -\frac{1}{n} + \frac{1}{n-1} = \frac{1}{n(n-1)}$ ，又 $a_1 = -1$ 不适合上式， $\therefore a_n = \begin{cases} -1, & n = 1, \\ \frac{1}{n(n-1)}, & n \geqslant 2. \end{cases}$

# 【对点精练】

1. 已知各项均为正数的数列 $\{a_{n}\}$ 的前 $n$ 项和为 $S_{n}$ ，若 $S_{1} = 2$ ， $3S_{n}^{2} - 2a_{n + 1}S_{n} = a_{n + 1}^{2}$ ，则 $a_{n} = \underline{\quad}$ .

1. 答案 $\left\{\begin{aligned}&2 & n=1 \\ &2^{n-1} & n\geq2\end{aligned}\right.$ 解析 由题意可得 $3S_{n}^{2}-2a_{n+1}S_{n}-a_{n+1}^{2}=(S_{n}-a_{n+1})\cdot(3S_{n}+a_{n+1})=0$ ，又 $a_{n}>0$ ，
所以 $S_{n}=a_{n+1}$ ，则 $S_{n-1}=a_{n}(n\geq2)$ ，两式相减并移项得 $a_{n+1}=2a_{n}(n\geq2)$ ，又 $S_{1}=a_{1}=a_{2}=2$ ，则 $a_{n}=a_{2}\cdot2^{n-2}=2^{n-1}(n\geq2)$ ，故 $a_{n}=\left\{\begin{aligned}&2, & n=1,\\ &2^{n-1}, & n\geq2.\end{aligned}\right.$

2. 已知数列 $\{a_{n}\}$ 中， $a_{1} = 1$ ， $S_{n}$ 为数列 $\{a_{n}\}$ 的前 $n$ 项和，且当 $n \geq 2$ 时，有 $\frac{2a_{n}}{a_{n}S_{n} - S_{n}^{2}} = 1$ 成立，则 $a_{n} =$ \_\_\_\_.

2. 答案 $\left\{ \begin{array}{l} 1, n = 1, \\ \frac{-2}{n(n + 1)}, n \geqslant 2. \end{array} \right.$ 解析 当 $n \geqslant 2$ 时，由 $\frac{2a_n}{a_nS_n - S_n^2} = 1$ ，得 $2(S_n - S_{n-1}) = (S_n - S_{n-1})S_n - S_n^2 = -S_nS_n$ 当 $n \geqslant 2$ 时，又 $\frac{2}{S_1} = 2$ ， $\therefore \left\{\frac{2}{S_n}\right\}$ 是以2为首项，1为公差的等差数列， $\therefore \frac{2}{S_n} = n + 1$ ，故 $S_n = \frac{2}{n + 1}$ ，当 $n \geqslant 2$ 时， $a_n = S_n - S_{n-1} = \frac{2}{n + 1} - \frac{2}{n} = \frac{-2}{n(n + 1)}$ ，又 $a_1 = -1$ 不适合上式， $\therefore a_n = \left\{\begin{array}{l} 1, n = 1, \\ \frac{-2}{n(n + 1)}, n \geqslant 2. \end{array}\right.$

