# 一类含有 $\mathbf{e}^x$ 和 $\ln x$ 问题的解决策略

# 刘选状

(广东省深圳市第二实验学校)

近年来,高考和模拟考试中经常出现同时含有 $e^{x}$ 和 $\ln x$ 的问题.这种问题往往让学生措手不及,很多学生看到题目中同时出现 $e^{x}$ 和 $\ln x$ 时就产生了畏惧心理,不知道如何下手.因此,本文结合具体实例归纳这类同时含有 $e^{x}$ 和 $\ln x$ 问题的常用解决方法,以期帮助读者更加得心应手地求解这类问题.

# 1 方法归纳

# 1.1 利用“同构”关系

![](images/bff0dc89a433b04f2e37b7f8cf77307e30d430dd965c9da9160af73bb6a16d3e.jpg)

例1 当 $a > 0$ 时，不等式 $\mathrm{e}^{ax}\geqslant \frac{\ln x}{a}$ 恒成立，则 $a$ 的取值范围为\_\_\_\_。

解法 1 当 $0 < x \leqslant 1$ 时，则 $e^{ax} > 0 \geqslant \frac{\ln x}{a}$ ，所以不等式 $e^{ax} \geqslant \frac{\ln x}{a}$ 恒成立。当 x > 1 时，有

$$
\mathrm{e} ^ {a x} \geqslant \frac {\ln x}{a} \Leftrightarrow
$$

$$
a x \cdot \mathrm{e} ^ {a x} \geqslant (\ln x) \cdot x = (\ln x) \cdot \mathrm{e} ^ {\ln x}. \tag {①}
$$

设 $f(x) = x\mathrm{e}^{x}$ ，则 $f'(x) = (x + 1)\mathrm{e}^x$ . 当 $x > 0$ 时， $f'(x) > 0, f(x)$ 单调递增. 由式①可知

$$
f (a x) \geqslant f (\ln x).
$$

因为 $a > 0, x > 1$ ，所以 $ax > 0, \ln x > 0$ ，则

$$
a x \geqslant \ln x \Leftrightarrow a \geqslant \frac {\ln x}{x} (x > 1).
$$

设 $g(x)=\frac{\ln x}{x}(x>1)$ ，则 $g'(x)=\frac{1-\ln x}{x^{2}}$ 。令 $g'(x)>0$ ，则 1<x<e；令 $g'(x)<0$ ，则 x>e。因此， $g(x)$ 在 $(1,e)$ 上单调递增，在 $(e,+\infty)$ 上单调递减，所以当 x=e 时，函数 $g(x)$ 取到最大值 $\frac{1}{e}$ ，故 $a\geqslant\frac{1}{e}$ 。

![](images/8d95fa3cd0f4e33c96319c80140fed475033296be8b471979271e2b2bbd10a19.jpg)

不等式 $\mathrm{e}^{ax}\geqslant \frac{\ln x}{a}$ 中同时含有 $\mathrm{e}^x$ 和 $\ln x$ ，因此想到将不等式两边同时乘 $ax$ ，这样就能得到同一个结构的表达式，再利用“同构”关系解决问题.

# 1.2 利用反函数的性质

解法 2 设 $h(x)=\mathrm{e}^{ax}$ ，则 $h(x)$ 为增函数，因此，

34

数理化

它存在反函数: $\varphi(x)=\frac{\ln x}{a}$ . 因此, 不等式 $e^{ax}\geqslant\frac{\ln x}{a}$ 可转化为 $h(x)\geqslant\varphi(x)$ . 因为互为反函数的两个函数的图像关于直线 y=x 对称, 所以 $h(x)\geqslant x\geqslant\varphi(x)$ , 即 $e^{ax}\geqslant x\geqslant\frac{\ln x}{a}$ .

由 $x \geqslant \frac{\ln x}{a}$ ，可得 $a \geqslant \frac{\ln x}{x}$ 。后同解法 1。

![](images/19eda24603cc9dbaf1a8839b673242bcf56407dc93192b56213eb4220be484b8.jpg)

点评

在同时含有 $e^{x}$ 和 $\ln x$ 的问题中, 可以利用反函数的性质将问题转化成只含有 $\mathrm{e}^x$ 或$\ln x$ 的问题.

# 1.3 移项作差构造函数

解法 3 由 $e^{ax} \geqslant \frac{\ln x}{a}$ ，可知 $e^{ax} - \frac{\ln x}{a} \geqslant 0$ 。设 $u(x) = e^{ax} - \frac{\ln x}{a} (x > 0)$ ，则 $u'(x) = a e^{ax} - \frac{1}{ax}$ 在 $(0, +\infty)$ 上单调递增。令 $x_{1} = \frac{1}{a^{2}e + a}$ ，则 $x_{1} < \frac{1}{a}$ ，且 $x_{1} < \frac{1}{a^{2}e}$ ，所以 $u'(x_{1}) = a e^{ax_{1}} - \frac{1}{ax_{1}} < a e^{-\frac{1}{ax_{1}}} < 0$ 。

令 $x_{2} = \frac{1}{a} +\frac{1}{a^{2}\mathrm{e}}$ ，则 $x_{2} > \frac{1}{a}$ 且 $x_{2} > \frac{1}{a^{2}\mathrm{e}}$ ，所以

$$
u ^ {\prime} \left(x _ {2}\right) = a \mathrm{e} ^ {a x _ {2}} - \frac {1}{a x _ {2}} > a \mathrm{e} - \frac {1}{a x _ {2}} > 0.
$$

由零点存在定理，可知存在 $x_0 \in (x_1, x_2)$ ，使得 $u'(x_0) = 0$ 。因此，函数 $u(x)$ 在 $(0, x_0)$ 上单调递减，在 $(x_0, +\infty)$ 上单调递增。当 $x = x_0$ 时，函数 $u(x)$ 取得最小值 $u(x_0) = \mathrm{e}^{ax_0} - \frac{\ln x_0}{a}$ 。由题意可知只需证

$$
u \left(x _ {0}\right) = \mathrm{e} ^ {a x _ {0}} - \frac {\ln x _ {0}}{a} \geqslant 0. \tag {①}
$$

因为 $u'(x_{0})=0$ ，所以 $a\mathrm{e}^{ax_{0}}=\frac{1}{ax_{0}}$ ，进一步可知 $e^{ax_{0}}=\frac{1}{a^{2}x_{0}}$ ， $\ln x_{0}=-ax_{0}-2\ln a$ 。将其代入式①可得

$$
\frac {1}{a ^ {2} x _ {0}} + x _ {0} + \frac {2 \ln a}{a} \geqslant 0.
$$

若 $a \geqslant \frac{1}{\mathrm{e}}$ ，由基本不等式得 $\frac{1}{a^2 x_0} + x_0 + \frac{2 \ln a}{a} \geqslant$

$\frac{2(1 + \ln a)}{a} \geqslant 0$ ，符合条件。若 $0 < a < \frac{1}{\mathrm{e}}$ ，令 $x = \frac{1}{a}$ ，则 $\mathrm{e}^{ax} = \mathrm{e} < \frac{1}{a} < \frac{\ln x}{a} = -\frac{\ln a}{a}$ ，与题意相矛盾。

综上, $a \geqslant \frac{1}{e}$ .

![](images/c6225b605b43b97896912ae983163012de98c39a06cad9171adbd6bb5a8d0489.jpg)

在解答同时含有 $e^{x}$ 和 $\ln x$ 的问题时, 可以通过移项, 构造函数, 将原问题转化为求函数的最值,在此过程中需求导,利用导函数的“隐零点”将 $e^{x}$ 和 $\ln x$ 替换掉.

# 1.4 利用不等式放缩

![](images/078853ed39c2b4fc0bb93119134c543c1c5075c1aa94f0ee7ca8329807c268c1.jpg)

例2 已知关于 $x$ 的不等式 $\frac{\mathrm{e}^x}{x^3} - x - a\ln x \geqslant 1$ 在 $x \in (1, +\infty)$ 上恒成立，则实数 $a$ 的取值范围为 \_\_\_\_.

引理 $e^{x} \geqslant x + 1$ ，当且仅当 x = 0 时，等号成立.

证明 设 $f(x) = \mathrm{e}^x - x - 1$ ，则 $f'(x) = \mathrm{e}^x - 1$ . 令 $f'(x) > 0$ ，则 $x > 0$ ；令 $f'(x) < 0$ ，则 $x < 0$ . 因此，函数 $f(x)$ 在 $(- \infty, 0)$ 上单调递减，在 $(0, +\infty)$ 上单调递增，所以 $f(x) \geqslant f(0) = 0$ ，则 $\mathrm{e}^x \geqslant x + 1$ ，当且仅当 $x = 0$ 时，等号成立.

![](images/7813a85db2b12a504a2f8bae42418205907af9468135d5fc443af7d1bb76433d.jpg)

由题意可知,对于任意 $x \in (1, +\infty)$ , $a \leqslant \frac{\mathrm{e}^{x}}{x^{3}} - x - 1$ $\frac{\ln x}{x^{3}}=0$ 恒成立.由引理可知

$$
\frac {\frac {\mathrm{e} ^ {x}}{x ^ {3}} - x - 1}{\ln x} = \frac {\mathrm{e} ^ {x - 3 \ln x} - x - 1}{\ln x} \geqslant
$$

$$
\frac {(x - 3 \ln x + 1) - x - 1}{\ln x} = - 3,
$$

当且仅当 $x = 3\ln x$ 时，等号成立.下面进一步说明等号可以成立，即方程 $x = 3\ln x$ 在 $(1, + \infty)$ 上有实数根.

设 $g(x)=x-3\ln x$ ，则 $g'(x)=1-\frac{3}{x}$ 。因此，函数 $g(x)$ 在 $(0,3)$ 上单调递减，在 $(3,+\infty)$ 上单调递增。因为 $g(1)=1>0$ ， $g(3)=3(1-\ln 3)<0$ ， $g(\mathrm{e}^{2})=\mathrm{e}^{2}-6>0$ ，所以由零点存在定理可知：函数 $g(x)$ 在 $(1,3)$ 和 $(3,\mathrm{e}^{2})$ 上分别有一个零点，即方程 $x=3\ln x$ 在 $(1,+\infty)$ 上有 2 个实数根。

综上， $a\leqslant -3$

![](images/128d7218f33b5bca3396ff5c70f26fcb0edd5957c869053abd5c85ca581bb3da.jpg)

在解答同时含有 $e^{x}$ 和 $\ln x$ 的问题时, 可以利用不等式 $e^{x} \geqslant x + 1$ 放缩, 这样可以减少计算量,但要注意验证等号成立的条件.

# 2 真题再现

![](images/da37c6e19db14a46e55888c7a541dad9c6a458751f07a38e13ee564e09a69962.jpg)

例3（2022年新高考I卷22）已知函数 $f(x) = ax$ 和 $g(x) = ax - \ln x$ 有相同的最小值.

(1) 求 $a$ ;

(2) 证明: 存在直线 y = b, 其与两条曲线 $y = f(x)$ 和 $y = g(x)$ 共有三个不同的交点, 并且从左到右的三个交点的横坐标成等差数列.

![](images/f5ec7c8b7a96d9f0729fef035240c9372d290adb18671e49869af6f758170c17.jpg)

(1) $a = 1$ （求解过程略）.

解析 (2)由(1)知 $f(x) = \mathrm{e}^x - x$ ，则 $f'(x) = \mathrm{e}^x - 1$ . 令 $f'(x) > 0$ ，则 $x > 0$ ; 令 $f'(x) < 0$ ，则 $x < 0$ . 因此，函数 $f(x)$ 在 $(-\infty, 0)$ 上单调递减，在 $(0, +\infty)$ 上单调递增，故 $f_{\min}(x) = f(0) = 1$ . 同理，函数 $g(x) = x - \ln x$ 在 $(0, 1)$ 上单调递减，在 $(1, +\infty)$ 上单调递增， $g_{\min}(x) = g(1) = 1$ . 不妨设这三个交点的横坐标从左到右依次为 $x_1, x_2, x_3$ ，则 $x_1 < 0 < x_2 < 1 < x_3$ ，且

$$
f \left(x _ {1}\right) = f \left(x _ {2}\right) = g \left(x _ {2}\right) = g \left(x _ {3}\right),
$$

则 $f(x_{1})=\mathrm{e}^{x_{1}}-x_{1}=x_{2}-\ln x_{2}=\mathrm{e}^{\ln x_{2}}-\ln x_{2}=f(\ln x_{2})$ . 因为 $x_{1},\ln x_{2}\in(-\infty,0)$ ，且 $f(x)$ 在 $(-∞,0)$ 上单调递减，所以

$$
x _ {1} = \ln x _ {2}. \tag {①}
$$

再由 $f(x_{2}) = g(x_{3})$ ，整理得

$$
f \left(x _ {2}\right) = \mathrm{e} ^ {x _ {2}} - x _ {2} = x _ {3} - \ln x _ {3} = \mathrm{e} ^ {\ln x _ {3}} - \ln x _ {3} = f (\ln x _ {3}).
$$

因为 $x_{2}, \ln x_{3} \in (0, +\infty)$ ，且 $f(x)$ 在 $(0, +\infty)$ 上单调递增，所以

$$
x _ {2} = \ln x _ {3} \Leftrightarrow x _ {3} = \mathrm{e} ^ {x _ {2}}. \tag {②}
$$

由①和②可知

$$
x _ {1} + x _ {3} = \ln x _ {2} + \mathrm{e} ^ {x _ {2}}, \tag {③}
$$

因为 $f(x_{2}) = g(x_{2})$ ，所以 $\mathrm{e}^{x_2} - x_2 = x_2 - \ln x_2 \Leftrightarrow \ln x_2 + \mathrm{e}^{x_2} = 2x_2.$ 结合式③可知 $x_{1} + x_{3} = 2x_{2}$ . 因此， $x_{1}, x_{2}, x_{3}$ 成等差数列.

![](images/cf119665058495326a212dc4eb1bbb1eeebe491d84e7c8ee8505260da6f3fe0c.jpg)

# 点评

本题中同时含有 $\mathrm{e}^x$ 和 $\ln x$ ，因此在第(2)问中利用“同构”得到 $x_{1}, x_{2}, x_{3}$ 的关系，进而证明其成等差数列.

分析和归纳这一类问题的解决方法,使得学生从总体上掌握解决这类问题的方法,有助于培养学生多总结、多思考的学习习惯.因此,教师应以培养学生的数学素养为目标,激发学生学习数学的兴趣,使其形成良好的数学思维品质,这样学生才能拓宽数学思维,养成举一反三的能力.

(完)