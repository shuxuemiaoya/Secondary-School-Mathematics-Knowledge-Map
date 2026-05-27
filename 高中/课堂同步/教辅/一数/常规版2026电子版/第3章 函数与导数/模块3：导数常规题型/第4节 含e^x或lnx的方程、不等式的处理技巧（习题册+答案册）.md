# 强化训练

1. (2023·全国模拟（节选）·★★☆)

证明：当 $x > 0$ 时， $(x - 2)\mathrm{e}^{x} + x + 2 > 0$

1. 证法1：（目标不等式不复杂，可考虑直接求导分析）

设 $f(x) = (x - 2)\mathrm{e}^{x} + x + 2(x > 0)$ ，则 $f^{\prime}(x) = \mathrm{e}^{x} + (x - 2)\mathrm{e}^{x} + 1$

$= (x - 1)\mathrm{e}^{x} + 1$ ，（不易直接判断正负，故二次求导）

所以 $f''(x) = \mathrm{e}^x +(x - 1)\mathrm{e}^x = x\mathrm{e}^x >0$ ，故 $f^{\prime}(x)$ 在 $(0, + \infty)$ 上

单调递增，又 $f'(0)=0$ ，所以 $f'(x)>0$ 恒成立，

故 $f(x)$ 在 $(0, +\infty)$ 上单调递增，因为 $f(0) = 0$

所以 $f(x) > 0$ ，故当 $x > 0$ 时， $(x - 2)\mathrm{e}^{x} + x + 2 > 0$

证法2：（目标不等式中含 $\mathrm{e}^x$ 这一项与后面的 $x + 2$ 是相加的，可考虑将其化为 $\varphi (x)\mathrm{e}^x$ 这种结构，再求导）

当 $x > 0$ 时， $(x - 2)\mathrm{e}^{x} + x + 2 > 0\Leftrightarrow \frac{x - 2}{x + 2}\mathrm{e}^{x} + 1 > 0$ ①，

设 $g(x) = \frac{x - 2}{x + 2}\mathrm{e}^x +1(x > 0)$ ，则 $g^{\prime}(x) = \frac{x + 2 - (x - 2)}{(x + 2)^{2}}\mathrm{e}^{x}+$

$\frac{x - 2}{x + 2}\mathrm{e}^{x} = \frac{x^{2}\mathrm{e}^{x}}{(x + 2)^{2}} >0$ ，所以 $g(x)$ 在 $(0, + \infty)$ 上单调递增，

又 $g(0) = 0$ ，所以 $g(x) > 0$ ，即 $\frac{x - 2}{x + 2}\mathrm{e}^x +1 > 0$

结合①可得当 $x > 0$ 时， $(x - 2)\mathrm{e}^{x} + x + 2 > 0$ 成立.

2. (2022·广东开学(节选)·★★☆)

已知函数 $f(x) = \frac{2(\mathrm{e}^x - x - 1)}{x^2}$ ，证明：当 $x > 0$ 时， $f(x) > 1$ .

2. 证法1: (可以想象, 若直接对 $f(x)$ 求导, 则结果较复杂,

所以先将原不等式等价转化再证. 一种转化方法是两端同乘以 $x^{2}$ 去分母, 再作差构造)

$$
f (x) > 1 \Leftrightarrow 2 (\mathrm{e} ^ {x} - x - 1) > x ^ {2} \Leftrightarrow 2 (\mathrm{e} ^ {x} - x - 1) - x ^ {2} > 0,
$$

所以只需证 $2(\mathrm{e}^{x} - x - 1) - x^{2} > 0$

设 $g(x) = 2(\mathrm{e}^{x} - x - 1) - x^{2}(x > 0)$ ，则 $g'(x) = 2(\mathrm{e}^x - 1) - 2x$

$$
= 2 \left(\mathrm{e} ^ {x} - x - 1\right), \quad g ^ {\prime \prime} (x) = 2 \left(\mathrm{e} ^ {x} - 1\right) > 0,
$$

所以 $g^{\prime}(x)$ 在 $(0, + \infty)$ 上 $\nearrow$ ，又 $g^{\prime}(0) = 0$ ，所以 $g^{\prime}(x) > 0$

故 $g(x)$ 在 $(0, +\infty)$ 上 $\nearrow$ ，因为 $g(0) = 0$ ，所以 $g(x) > 0$

即 $2(\mathrm{e}^{x} - x - 1) - x^{2} > 0$ ，故当 $x > 0$ 时， $f(x) > 1$

证法 2: (将 $f(x) > 1$ 等价转化为 $2(\mathrm{e}^{x} - x - 1) > x^{2}$ 后, 考虑到 $\mathrm{e}^{x}$ 与其余部分做乘法或除法, 更易于求导研究, 所以也可朝此方向等价转化)

$$
\begin{array}{l} f (x) > 1 \Leftrightarrow 2 \left(\mathrm{e} ^ {x} - x - 1\right) > x ^ {2} \Leftrightarrow 2 \mathrm{e} ^ {x} > x ^ {2} + 2 x + 2 \\ \Leftrightarrow \frac {x ^ {2} + 2 x + 2}{\mathrm{e} ^ {x}} <   2, \\ \end{array}
$$

所以要证 $f(x) > 1$ ，只需证 $\frac{x^2 + 2x + 2}{\mathrm{e}^x} < 2$

设 $h(x) = \frac{x^2 + 2x + 2}{\mathrm{e}^x}$ ， $x > 0$

则 $h'(x) = \frac{(2x + 2)\mathrm{e}^x - \mathrm{e}^x(x^2 + 2x + 2)}{(\mathrm{e}^x)^2} = -\frac{x^2}{\mathrm{e}^x} < 0$

所以 $h(x)$ 在 $(0, +\infty)$ 上 $\searrow$ ，又 $h(0) = 2$ ，所以 $h(x) < 2$ ，即 $\frac{x^2 + 2x + 2}{\mathrm{e}^x} < 2$ ，故当 $x > 0$ 时， $f(x) > 1$

3. (2013·北京卷·★★★)

设 l 为曲线 $C: y = \frac{\ln x}{x}$ 在点 $(1,0)$ 处的切线.

(1) 求 l 的方程;  
(2) 证明: 除切点 $(1,0)$ 之外, 曲线 $C$ 在直线 $l$ 的下方.

3. 解：（1）由题意， $y' = \frac{1 - \ln x}{x^2}$ ，所以 $y'\big|_{x=1} = 1$ ，

故切线 l 的方程为 y = x - 1.

（2）要证结论，只需证当 $x > 0$ 且 $x \neq 1$ 时， $\frac{\ln x}{x} < x - 1$

（此不等式中有 $\ln x$ ，可两端同乘以 $x$ 将其孤立，便于构造函数求导分析）

$$
\frac {\ln x}{x} <   x - 1 \Leftrightarrow \ln x <   x ^ {2} - x \Leftrightarrow \ln x - x ^ {2} + x <   0,
$$

令 $f(x) = \ln x - x^2 + x (x > 0)$ ，则 $f'(x) = \frac{1}{x} - 2x + 1$

$$
= \frac {(2 x + 1) (1 - x)}{x},
$$

所以 $f'(x)>0\Leftrightarrow0<x<1,\quad f'(x)<0\Leftrightarrow x>1$

故 $f(x)$ 在 $(0,1)$ 上单调递增，在 $(1, +\infty)$ 上单调递减，

所以当 $x > 0$ 且 $x \neq 1$ 时， $f(x) < f(1) = 0$

即 $\ln x - x^2 + x < 0$ ，故结论成立.

4. (2022·新课标Ⅰ卷（节选）·★★★)

已知函数 $f(x) = \mathrm{e}^{x} - ax$ 和 $g(x) = ax - \ln x$ 有相同的最小值，求 $a$ .

4. 解：（题干提到了最小值，所以先求导，研究单调性）

由题意， $f^{\prime}(x) = \mathfrak{e}^{x} - a(x\in \mathbf{R})$ ， $g^{\prime}(x) = a - \frac{1}{x} = \frac{ax - 1}{x} (x > 0)$

(观察可得 $f'(x)$ 和 $g'(x)$ 是否有零点，都是与 a 的正负有关，所以据此讨论)

当 $a \leq 0$ 时， $g'(x) < 0$ ，所以 $g(x)$ 在 $(0, +\infty)$ 上单调递减，

故 $g(x)$ 没有最小值，不合题意；

当 $a > 0$ 时， $f'(x) > 0 \Leftrightarrow x > \ln a$ ， $f'(x) < 0 \Leftrightarrow x < \ln a$ ，

所以 $f(x)$ 在 $(-\infty, \ln a)$ 上单调递减，在 $(\ln a, +\infty)$ 上单调递

增，故 $f(x)_{\min} = f(\ln a) = a - a\ln a$

$$
g ^ {\prime} (x) > 0 \Leftrightarrow x > \frac {1}{a}, g ^ {\prime} (x) <   0 \Leftrightarrow 0 <   x <   \frac {1}{a},
$$

所以 $g(x)$ 在 $\left(0, \frac{1}{a}\right)$ 上单调递减，在 $\left(\frac{1}{a}, +\infty\right)$ 上单调递增，

故 $g(x)_{\min} = g\left(\frac{1}{a}\right) = 1 - \ln \frac{1}{a} = 1 + \ln a$

由题意， $a - a\ln a = 1 + \ln a$ ，所以 $a - 1 - (a + 1)\ln a = 0$ ①，

(观察可得 a=1 是此方程的解，但要说明解的唯一性，还需构造函数求导分析，式①中有 $(a+1)\ln a$ ，故同除以 $a+1$ 将 $\ln a$ 孤立出来，便于求导研究)

式①等价于 $\frac{a - 1}{a + 1} -\ln a = 0$ ②，设 $h(a) = \frac{a - 1}{a + 1} -\ln a(a > 0)$

则 $h^{\prime}(a) = \frac{2}{(a + 1)^{2}} -\frac{1}{a} = -\frac{a^{2} + 1}{a(a + 1)^{2}} < 0$

所以 $h(a)$ 在 $(0, +\infty)$ 上单调递减，

又 $h(1) = 0$ ，所以 $h(a)$ 有唯一的零点1，

从而当且仅当 $a = 1$ 时，方程②成立，故 $a = 1$

# 5. (2024·全国甲卷·★★★☆)

已知函数 $f(x) = a(x - 1) - \ln x + 1$

(1) 求 $f(x)$ 的单调区间;  
(2) 若 $a \leq 2$ ，证明：当 x > 1 时， $f(x) < e^{x-1}$ 恒成立.

5. 解：（1）由题意， $f'(x)=a-\frac{1}{x}$ ，x>0，

（观察发现 $f^{\prime}(x) = 0\Rightarrow x = \frac{1}{a}$ ，但只有当 $a > 0$ 时， $\frac{1}{a}$ 才有意义，且在定义域内，故讨论 $a$ 的正负）

当 $a \leq 0$ 时， $f'(x) = a - \frac{1}{x} < 0$

所以 $f(x)$ 的单调递减区间是 $(0, +\infty)$ ，无单调递增区间；

当 $a > 0$ 时， $f'(x) > 0 \Leftrightarrow a > \frac{1}{x} \Leftrightarrow x > \frac{1}{a}$ ， $f'(x) < 0 \Leftrightarrow$

$0 < x < \frac{1}{a}$ ，所以 $f(x)$ 的单调递增区间是 $\left(\frac{1}{a}, +\infty\right)$ ，

单调递减区间是 $\left(0,\frac{1}{a}\right)$ .

(2) 证法1: (注意到 $x - 1 > 0$ , 所以可直接通过 $a \leq 2$ 将 $f(x)$ 放缩成不含参的形式, 再证明目标不等式)

当 $x > 1$ 时， $x - 1 > 0$ ，又 $a \leq 2$ ，所以 $a(x - 1) \leq 2(x - 1)$ ，

故 $f(x) = a(x - 1) - \ln x + 1\leq 2(x - 1) - \ln x + 1$ ①，

(所以要证 $f(x) < e^{x-1}$ ，只需证 $2(x-1) - \ln x + 1 < e^{x-1}$ ，此不等式不算复杂，可考虑直接移项构造函数求导分析)

设 $g(x) = 2(x - 1) - \ln x + 1 - \mathrm{e}^{x - 1}$ ， $x > 1$

则 $g^{\prime}(x) = 2 - \frac{1}{x} -\mathrm{e}^{x - 1}$ ，（不易直接判断正负，考虑二次求导）

$$
g ^ {\prime \prime} (x) = \frac {1}{x ^ {2}} - \mathrm{e} ^ {x - 1},
$$

因为 $x > 1$ ，所以 $0 < \frac{1}{x^2} < 1$ ， $\mathrm{e}^{x - 1} > \mathrm{e}^0 = 1$

从而 $g''(x) < 0$ ，故 $g'(x)$ 在 $(1, +\infty)$ 上单调递减，

又因为 $g'(1) = 2 - \frac{1}{1} - \mathrm{e}^{1 - 1} = 0$ ，所以 $g'(x) < 0$

故 $g(x)$ 在 $(1, +\infty)$ 上单调递减，

因为 $g(1) = 2 \times (1 - 1) - \ln 1 + 1 - \mathrm{e}^{1 - 1} = 0$ ，所以 $g(x) < 0$

从而 $2(x - 1) - \ln x + 1 - \mathrm{e}^{x - 1} < 0$ ，故 $2(x - 1) - \ln x + 1 < \mathrm{e}^{x - 1}$

由①可知 $f(x)\leq 2(x - 1) - \ln x + 1$ ，所以 $f(x) <   \mathrm{e}^{x - 1}$

证法2：（按解法1得到不等式①后，证明 $2(x-1)-\ln x+1<\mathrm{e}^{x-1}$ 时，注意到右边是 $e^{x-1}$ ，也可考虑将其除到左边再构造函数求导分析）

设 $h(x) = \frac{2(x - 1) - \ln x + 1}{\mathrm{e}^{x - 1}}$ ， $x > 1$ ，则 $h^{\prime}(x) =$

$$
\frac {\left(2 - \frac {1}{x}\right) \mathrm{e} ^ {x - 1} - \mathrm{e} ^ {x - 1} [ 2 (x - 1) - \ln x + 1 ]}{(\mathrm{e} ^ {x - 1}) ^ {2}} = \frac {\ln x - \frac {1}{x} - 2 x + 3}{\mathrm{e} ^ {x - 1}},
$$

(不易直接判断正负, 可考虑二次求导, 直接求显然会变得更复杂, 于是把分子单独拿出来求导分析)

设 $r(x) = \ln x - \frac{1}{x} - 2x + 3$ ， $x > 1$

则 $r'(x) = \frac{1}{x} +\frac{1}{x^2} -2 = -\frac{2x^2 - x - 1}{x^2} = -\frac{(2x + 1)(x - 1)}{x^2} < 0$

所以 $r(x)$ 在 $(1, +\infty)$ 上单调递减，

又 $r(1) = \ln 1 - \frac{1}{1} - 2 \times 1 + 3 = 0$ ，所以 $r(x) < 0$ ，

从而 $h'(x) < 0$ ，故 $h(x)$ 在 $(1, +\infty)$ 上单调递减，

结合 $h(1) = \frac{2\times(1 - 1) - \ln 1 + 1}{\mathrm{e}^{1 - 1}} = 1$ 可得 $h(x) <   1$

即 $\frac{2(x - 1) - \ln x + 1}{\mathrm{e}^{x - 1}} < 1$ ，所以 $2(x - 1) - \ln x + 1 <   \mathrm{e}^{x - 1}$

结合①可得当 $a \leq 2$ 时，对任意的 $x > 1$ ，恒有 $f(x) < \mathrm{e}^{x - 1}$ .

【反思】大部分题将 $e^{x}$ 与其余部分结合、将 $\ln x$ 孤立出来会比较简单，但也不是绝对。例如本题证法1和证法2相比，也不复杂，所以方法的运用可以灵活一点，别太死板哦。