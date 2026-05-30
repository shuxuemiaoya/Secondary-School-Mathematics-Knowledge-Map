含指、对数混合形式的不等式证明之所以难，其根本原因在于指数与对数是水火不容的，其导函数的零点一般不可求

## 分离  $\mathrm{e}^x$  和  $\ln x$  
分离  $\mathrm{e}^x$  和  $\ln x$  以便于求导，但分离还不足以解决所有问题，常需要与幂函数配对，将  $\mathrm{e}^x$  与含有幂函数的代数式配对为  $f(x)$ ，将  $\ln x$  与含有幂函数的代数式配对为  $g(x)$ ，将  $\mathrm{e}^x$  与  $\ln x$  分离在两边，也使两部分  $f(x)$  和  $g(x)$  的函数极值容易求解，从而证明更强的结论  $f(x)_{\min} \geq g(x)_{\max}$ ，则有  $F(x) = f(x) - g(x) \geq 0$ . 

## 不分离  $\mathrm{e}^x$  和  $\ln x$  
含指数、对数混合形式的不等式证明之所以难，其根本原因在于指数与对数是“水火不容”的，其导函数的零点一般不可求，我们称此种情况为“零点不可求——隐零点”问题，隐零点虽然不能求出，但是有价值，令导函数值为0，利用这一等式，将隐零点代回到原函数中后，我们往往可以进行整体代换，将不便操作的指数或对数函数，转化为我们熟悉并容易把握的幂函数。用隐零点转化上要注意三点：
### 1. 隐零点对应的方程
这个方程的目的是作为中间桥梁去转化求最值，一般有三种形式：①幂函数、指数混合；②幂函数、对数混合；③指数、对数混合。前两者直接利用隐零点的方程将指、对幂上转，但对于第3种形式，不能直接将指数、对数向幂函数的方向上转化，如何实现指数、对数形式向幂函数形式转化，第3种形式需要进行同构降阶，如隐零点对应方程为
$x_0^2\mathrm{e}^{x_0} + \ln x_0 = 0\Longleftrightarrow x_0\mathrm{e}^{x_0} + \frac{1}{x_0}\ln x_0 = 0\Longleftrightarrow x_0\mathrm{e}^{x_0} = \frac{1}{x_0}\ln \frac{1}{x_0} = \ln \frac{1}{x_0}\mathrm{e}^{\ln \frac{1}{x_0}}$  ，构造函数  $f(x) = x\mathrm{e}^{x}$  ，则 $f(x_{0}) = f\left(\ln \frac{1}{x_{0}}\right)$  ，再通过单调性降阶为  $x_0 = \ln \frac{1}{x_0} = -\ln x_0$  ，此时可简洁地将  $\ln x_0$  和  $\mathrm{e}^{x_0}$  向幂函数形式转化，如  $\ln x_0 = -x_0,\mathrm{e}^{x_0} = \frac{1}{x_0}.$
还有一类情况也需要注意操作的方法：若隐零点对应的方程是含参数的情形，要运用处理代数问题的一般方法：消参。消参是将二元（含隐零点  $x_0$  和参数的形式）问题转化为只含有隐零点的形式。
### 2. 隐零点所在的区间
隐零点虽不能直接解出，但对隐零点区间的估计是证明不等式的关键，常需要根据所证
明的目标对隐零点的区间作合理的限定.
### 3.转化路径：指、对幂上转
指、对幂上转，即将指数和对数形式向幂函数转化，转化的本质在于将指、对复杂形式转化为熟悉且易于求导的幂函数形式。

##### 例5.3 证明：  $\mathrm{e}^x -\ln x > 2$
分析思路一（分而治之）：含指数、对数函数形式的不等式证明常分离指、对函数，分离  $\mathrm{e}^x$  和  $\ln x$  后  $\mathrm{e}^x >\ln x + 2$  ，两边分别再与幂函数配对，使其函数极值点可求，证明左边函数的最小值大于等于右边函数的最大值即可.
思路二（合而歼之）：不分离  $\mathrm{e}^x$  和  $\ln x$  ，由于对  $\mathrm{e}^x -\ln x$  求导后  $\mathrm{e}^x -\frac{1}{x} = 0$  是超越方程，求不出具体的解，通过虚设零点可以将  $\mathrm{e}^x$  和  $\ln x$  转化成  $\frac{1}{x_0}$  和  $-x_0$  ，再使用基本不等式即可证明.
另外，本题也可以使用切线不等式放缩来证明

<span class="fake-tag">解析</span> 从数与形的数学观来分析和求解.
解法一（数的观点：分而治之）：分离  $\mathrm{e}^x$  和  $\ln x$  ，即  $\mathrm{e}^x >\ln x + 2,\mathrm{e}^x -x > \ln x - x + 2.$
令  $f_{1}(x) = \mathrm{e}^{x} - x, f_{2}(x) = \ln x - x + 2, f_{1}'(x) = \mathrm{e}^{x} - 1 > 0$ ，函数  $f_{1}(x)$  在  $(0, +\infty)$  上单调递增，则  $f_{1}(x) > f_{1}(0) = 1$ .
$f_{2}^{\prime}(x) = \frac{1}{x} - 1 = \frac{1 - x}{x}$ , 函数  $f_{2}(x)$  在  $(0,1)$  上单调递增, 在  $(1, +\infty)$  上单调递减,  $f_{2}(x)_{\max} = f_{2}(1) = 1$ , 因此  $f_{1}(x) > f_{2}(x)$ , 即  $\mathrm{e}^{x} > \ln x + 2$ .
也可在不等式  $\mathrm{e}^x >\ln x + 2$  两边同除以  $x$  ，即  $\frac{\mathrm{e}^x}{x} >\frac{\ln x + 2}{x}$
令  $g_{1}(x) = \frac{\mathrm{e}^{x}}{x}, g_{2}(x) = \frac{\ln x + 2}{x}$ ，则  $g^{\prime}_{1}(x) = \frac{\mathrm{e}^{x} \cdot x - \mathrm{e}^{x}}{x^{2}} = \frac{\mathrm{e}^{x}(x - 1)}{x^{2}}, g_{1}(x)$  在(0,1)上单调递减，在 $(1, + \infty)$ 上单调递增，于是  $g_{1}(x)_{\min} = g_{1}(1) = \mathrm{e.} g^{\prime}_{2}(x) = \frac{\frac{1}{x} \cdot x - (\ln x + 2)}{x^{2}} = \frac{-\ln x - 1}{x^{2}}$ ，令  $g^{\prime}_{2}(x) = 0$  得  $x = \frac{1}{\mathrm{e}}$ ，所以函数  $g_{2}(x)$  在  $\left(0, \frac{1}{\mathrm{e}}\right)$  上单调递增，在  $\left(\frac{1}{\mathrm{e}}, + \infty\right)$  上单调递减，则  $g_{2}(x)_{\max} = g_{2}\left(\frac{1}{\mathrm{e}}\right) = \mathrm{e}$ . 故  $g_{1}(x) > g_{2}(x)$ ，即  $\frac{\mathrm{e}^{x}}{x} > \frac{\ln x + 2}{x}$ ，因此  $\mathrm{e}^{x} > \ln x + 2$
解法二（数的观点：合而歼之. 虚设零点，设而不求，整体代换）：
令  $g(x) = \mathrm{e}^{x} - \ln x$  ，则  $g^{\prime}(x) = \mathrm{e}^{x} - \frac{1}{x}$  显然  $g^{\prime}(x)$  单调递增，且易知  $g^{\prime}(x)$  有且仅有一个零点  $x_0$  .则  $\mathrm{e}^{x_0} = \frac{1}{x_0}$  ，两边取对数，得  $x_0 = -\ln x_0,x_0\neq 1.$
由单调性可知  $g^{\prime}(x)$  在  $(0,x_0)$  上小于0，在  $(x_0, + \infty)$  上大于0，所以  $g(x)$  在  $(0,x_0)$  上单调递减，在  $(x_0, + \infty)$  上单调递增， $g(x)_{\min} = g(x_0) = e^{x_0} - \ln x_0 = \frac{1}{x_0} +x_0.$
因为  $x_0 \neq 1$  且  $x_0 > 0$ , 所以  $\frac{1}{x_0} + x_0 > 2$ , 即证  $\mathrm{e}^x - \ln x > 2$ .
解法三（形的观点：切线放缩）：由经典不等式  $\mathrm{e}^x\geqslant x + 1,\ln x\leqslant x - 1$  可得  $\mathrm{e}^x -\ln x\geqslant x + 1-$ $(x - 1) = 2$  ，且等号不同时取得，所以  $\mathrm{e}^x -\ln x > 2$
### 回注
解法三的几何直观是切线分割.如图所示，在证明本题时，因为  $\mathrm{e}^x > x + 1, \ln x \leqslant x - 1, \mathrm{e}^x - \ln x \geqslant (x + 1) - (x - 1) = 2$  （等号不能取得），则  $\mathrm{e}^x - \ln x > 2$ .
无论是从代数角度还是从几何角度，本质是反映数学问题的不同方面.
![](高中习题/高考/高考数学培优40讲/Attachments/e9d65f183b40b685ae071a152f260399ed52a21ec0fe02d5fc24570ed944ad67.jpg)



## 分离  $\mathrm{e}^x$  和  $\ln x$  
### 1、通过证明更强的结论  $f(x)_{\min} \geq g(x)_{\max}$  来证明原不等式.$f(x)_{\min} \geq g(x)_{\max}$  来证明原不等式.（凹凸反转）

##### 例5.4 已知函数  $f(x) = \frac{x + 1}{\mathrm{e}^x} (1 - x - x\ln x)$ ，证明： $f(x) < 1 + \mathrm{e}^{-2}$ .
分析 函数中既有  $\mathrm{e}^x$ ，又有  $\ln x$ ，而且还是分式的形式，给求导带来极大的困难，为此考虑分离函数，将  $\mathrm{e}^x$  与  $\ln x$  分离在不等式两边，即  $1 - x - x\ln x < \frac{\mathrm{e}^x}{x + 1} (1 + \mathrm{e}^{-2})$ ，只需证明  $(1 - x -$
$x \ln x) _ {\max } <   \left[ \frac {e ^ {x}}{x + 1} (1 + e ^ {- 2}) \right] _ {\min }.$

<span class="fake-tag">解析</span> 由于  $\frac{x + 1}{\mathrm{e}^x}(1 - x - x\ln x) < 1 + \mathrm{e}^{-2} \Leftrightarrow 1 - x - x\ln x < \frac{\mathrm{e}^x}{x + 1}(1 + \mathrm{e}^{-2})$ ，因此猜想证明  $(1 - x - x\ln x)_{\max} < \left[\frac{\mathrm{e}^x}{x + 1}(1 + \mathrm{e}^{-2})\right]_{\min}, x > 0.$
令  $g(x) = 1 - x - x\ln x$  ，则  $g^{\prime}(x) = -2 - \ln x$  ，可知  $g^{\prime}(x)$  在  $(0,\mathrm{e}^{-2})$  上大于0，在  $(\mathrm{e}^{-2}, + \infty)$  上小于0，所以  $g(x)$  在  $(0,\mathrm{e}^{-2})$  上单调递增，在  $(\mathrm{e}^{-2}, + \infty)$  上单调递减，即  $g(x)_{\max} = g(\mathrm{e}^{-2}) = 1 + \mathrm{e}^{-2}$
令  $t(x) = \frac{\mathrm{e}^x}{x + 1} (1 + \mathrm{e}^{-2})$  ，则  $t^\prime (x) = \frac{\mathrm{e}^x x}{(x + 1)^2} (1 + \mathrm{e}^{-2}) > 0$  ，所以  $t(x)$  在  $(0, + \infty)$  上单调递增，则  $t(x)_{\min} = t(0) = 1 + \mathrm{e}^{-2}$  ，且因为  $x > 0$  ，所以  $t(x) > 1 + \mathrm{e}^{-2}$
综上所述，  $1 - x - x\ln x\leqslant 1 + \mathrm{e}^{-2} <   \frac{\mathrm{e}^{x}}{x + 1} (1 + \mathrm{e}^{-2})$  ，所以  $f(x) <   1 + \mathrm{e}^{-2}$
#### 评注
本题函数形式复杂，既有指数函数，又有对数函数，此时我们可以采用分离函数的方法，将原本不便求导、隐零点无法利用的函数，分拆为两个易求导，且可以求出极值的形式，从而破解这道高考压轴题.

##### 变式 已知函数  $f(x) = \frac{\frac{1}{2}x^2 + x + 1}{\mathrm{e}^x}\left(1 - x - x\ln x\right)$ ，证明： $f(x) < 1 + \mathrm{e}^{-2}$ .

<span class="fake-tag">解析</span> (1) 当  $1 - x - x \ln x \leqslant 0$  时，有  $f(x) < 1 + \mathrm{e}^{-2}$ .
(2) 当  $1 - x - x \ln x > 0$  时，注意到当  $x > 0$  时， $\mathrm{e}^x > 1 + x + \frac{x^2}{2}$ （由麦克劳林公式易得），所以  $f(x) < 1 - x - x \ln x$ ，故只需证  $1 - x - x \ln x \leqslant 1 + \mathrm{e}^{-2}$ ，由上面例题知  $(1 - x - x \ln x)_{\max} = 1 + \mathrm{e}^{-2}$ ，所以  $f(x) < 1 + \mathrm{e}^{-2}$ .
综上可知，  $f(x) <   1 + \mathrm{e}^{-2}$
##### 例5.5 已知函数  $f(x) = \mathrm{e}^{x}\ln x + \frac{2\mathrm{e}^{x - 1}}{x}$ ，证明： $f(x) > 1$
分析 函数中既有  $\mathrm{e}^x$  ，又有  $\ln x$  ，而且有分式的形式，求导以后结构非常复杂，为此考虑将  $\mathrm{e}^x$  与  $\ln x$  分离，将原不等式进行变形.
$\mathrm{e}^{x}\ln x + \frac{2\mathrm{e}^{x - 1}}{x} > 1 \Leftrightarrow \ln x > \mathrm{e}^{-x} - \frac{2}{\mathrm{e}x}$ , 两边的函数都没有极值点, 继续进行变形, 两边同时乘以  $x$ , 即  $x\ln x > x\mathrm{e}^{-x} - \frac{2}{\mathrm{e}}$ , 只需证明  $(x\ln x)_{\min} > \left(x\mathrm{e}^{-x} - \frac{2}{\mathrm{e}}\right)_{\max}$ .

<span class="fake-tag">解析</span> 解法一（凹凸反转）：  $\mathrm{e}^x\ln x + \frac{2\mathrm{e}^{x - 1}}{x} > 1 \Leftrightarrow \ln x > \mathrm{e}^{-x} - \frac{2}{\mathrm{e}x} \Leftrightarrow x\ln x > x\mathrm{e}^{-x} - \frac{2}{\mathrm{e}}.$
猜想  $(x\ln x)_{\min} > \left(x\mathrm{e}^{-x} - \frac{2}{\mathrm{e}}\right)_{\max},x > 0.$
证明：令  $g(x) = x\ln x$ ，则  $g'(x) = 1 + \ln x$ ，可知  $g'(x)$  在  $(0, \mathrm{e}^{-1})$  上小于 0，在  $(\mathrm{e}^{-1}, +\infty)$  上大于 0，
所以  $g(x)$  在  $(0, e^{-1})$  上单调递减，在  $(e^{-1}, +\infty)$  上单调递增，则有  $g(x)_{\min} = g(e^{-1}) = -e^{-1}$ .
令  $t(x) = x\mathrm{e}^{-x} - \frac{2}{\mathrm{e}}$  则  $t^{\prime}(x) = \mathrm{e}^{-x}(1 - x)$  ，可知  $t^\prime (x)$  在(0,1)上大于0，在(1，十）上小于0，所以  $g(x)$  在(0,1)上单调递增，在(1，十）上单调递减，则有  $t(x)_{\max} = t(1) = -\mathrm{e}^{-1}$
所以  $g(x) \geq g(x)_{\min} = -\mathrm{e}^{-1} = t(x)_{\max} \geqslant t(x)$ ，等号不同时取得， $x \ln x > x \mathrm{e}^{-x} - \frac{2}{\mathrm{e}}$ ，即证  $f(x) > 1$ 。
解法二（不等式放缩）：由  $\ln x\leqslant x - 1$  得  $\ln {\frac{x}{e}}\leqslant {\frac{x}{e}} - 1$  ，即  $\ln x - 1\leqslant \frac{x}{e} -1$  ，亦即  $\ln x\leqslant \frac{x}{e}$
因此  $\ln \frac{1}{x} \leqslant \frac{1}{\mathrm{e}x}, -\ln x \leqslant \frac{1}{\mathrm{e}x}$ ，即  $\ln x \geqslant -\frac{1}{\mathrm{e}x}$ ，所以  $\mathrm{e}^x \ln x > -\frac{\mathrm{e}^{x-1}}{x}$ ，则  $\mathrm{e}^x \ln x + \frac{2\mathrm{e}^{x-1}}{x} > \frac{\mathrm{e}^{x-1}}{x} > 1$
#### 评注
遇到难题，不要自乱阵脚，往往越是复杂的题目，其解题思路越是清楚。本题函数形式复杂多样，直接求导研究极值走不通。为此，我们自然想到分离函数法。

##### 例5.6（1）已知函数  $f(x) = 2\mathrm{e}^{x^2} - x\ln x$ ，证明：  $f(x) > 0$
(2)已知函数  $f(x) = 4\mathrm{e}^{x - 3} - x\ln x$  ，证明：  $f(x) > 0$
分析 拆分为两个函数使其凹凸性相反，且凹函数能找到最小值，凸函数能找到最大值.若是无法实现凹凸反转，还得变形，以产生凹凸性相反.

<span class="fake-tag">解析</span> (1) 要证明  $2\mathrm{e}^{x - 2} > x \ln x$ ，在不等式两端同除以  $x^2, \frac{2\mathrm{e}^{x - 2}}{x^2} > \frac{\ln x}{x}$ .
令  $h(x) = \frac{2\mathrm{e}^{x - 2}}{x^2}$ , 则  $h'(x) = 2 \cdot \frac{\mathrm{e}^{x - 2} \cdot x^2 - \mathrm{e}^{x - 2} \cdot 2x}{x^4} = \frac{2\mathrm{e}^{x - 2}(x - 2)}{x^3}, h(x)$  在  $(0, 2)$  上单调递减, 在  $(2, +\infty)$  上单调递增,  $h(x)_{\min} = h(2) = \frac{1}{2}$ .
令  $g(x) = \frac{\ln x}{x}$ ，则  $g'(x) = \frac{1 - \ln x}{x^2} = 0$ ，得  $x = e, g(x)$  在  $(0, e)$  上单调递增，在  $(e, +\infty)$  上单调递减， $g(x)_{\max} = g(e) = \frac{1}{e}$ ，显然  $h(x)_{\min} > g(x)_{\max}$ ，因此  $\frac{2e^{x - 2}}{x^2} > \frac{\ln x}{x}$ ，即  $2e^{x - 2} - x\ln x > 0$ 。
若本题在不等式  $2\mathrm{e}^{x - 2} > x\ln x$  的两端同除以  $x^3$  是否可以证明呢？试一试.
(2)  $f(x) > 0 \Leftrightarrow 4\mathrm{e}^{x - 3} - x\ln x > 0 \Leftrightarrow 4\mathrm{e}^{x - 3} > x\ln x \Leftrightarrow \frac{4\mathrm{e}^{x - 3}}{x^2} > \frac{\ln x}{x}$ .
令  $g(x) = \frac{4\mathrm{e}^{x - 3}}{x^2}$ ，则  $g'(x) = \frac{4\mathrm{e}^{x - 3}(x - 2)}{x^3}$ ， $x > 0$
可知  $g^{\prime}(x)$  在  $(0,2)$  上小于0，在  $(2, + \infty)$  上大于0，所以  $g(x)$  在(0,2)上单调递减，在 $(2, + \infty)$  上单调递增，所以有  $g(x)_{\min} = g(2) = e^{-1}$
令  $t(x) = \frac{\ln x}{x}$ ，则  $t'(x) = \frac{1 - \ln x}{x^2}$ 。可知  $t'(x)$  在  $(0, e)$  上大于 0，在  $(e, +\infty)$  上小于 0。
所以  $t(x)$  在  $(0, \mathrm{e})$  上单调递增，在  $(\mathrm{e}, + \infty)$  上单调递减， $t(x)_{\max} = t(\mathrm{e}) = \mathrm{e}^{-1}$ .
综上所述，有  $g(x) \geqslant \mathrm{e}^{-1} \geqslant t(x)$ ，又等号不同时取得，则  $g(x) > t(x)$ ，所以  $f(x) > 0$
#### 解后反用
#### 拆分函数实现凹凸反转的再思
本题中分离函数后，左右两侧的  $4\mathrm{e}^{x - 3}$  和  $x\ln x$  不便比较，为此左右两侧同时除以  $x^2$  ，这是一个常用的技巧，改变了函数的凹凸性，使之出现极值.但我们不仅要知其然，更要知其所以然，为什么除以  $x^2$  ，可不可以除以  $x^3,x^4$  ？为什么是同时除以，可不可以作加法、减法、乘法？能不能不变形，直接用隐零点的方法做？这些错路或弯路，是参考答案中所没有的，但只有亲自走过这些错路弯路，才能研究明白细微之处，才能理解分离函数的本质，比较得出分离函数法和隐零点法的适用情形，才能在解题时心中有数，胸有成竹.
为此，笔者提出如下几个问题：
问题1：为什么要分离函数？最正常最本质的解法，难道不是研究  $f^{\prime}(x)$  ，得出极值点，求出  $f(x)_{\min}$  ，证明  $f(x)_{\min} > 0$  吗？
问题2：分离函数后，为什么想到左右同时除以  $x^{2}$ ，为什么不是左右同时加上一个数，或者减去一个数？为什么是除以  $x^{2}$ ，而不是除以  $x^{3}$ ，不是除以  $x^{4}$ ？
问题3：我们将此题进行一般化处理，将  $4\mathrm{e}^{-3}$  视为  $a(a > 0)$ ，就有  $a\mathrm{e}^x - x\ln x > 0$ 。那么  $a$  的范围能不能再强化，有没有比  $4\mathrm{e}^{-3}$  更小的  $a$ ，也满足  $a\mathrm{e}^x - x\ln x > 0$  恒成立？
问题4: 问题的最终形式, 如果  $f(x) = m\mathrm{e}^{ax} - x^b\ln x (m > 0)$ , 这里  $a, b$  是给定的正实数, 且  $f(x) > 0$ , 我们能不能研究一下  $m$  的取值范围?
下面依次来回答这些问题.
对于问题1，我们不妨先按照最正常，最本质的解法，来做一遍。
$f(x) = 4\mathrm{e}^{x - 3} - x\ln x$  ，则  $f^{\prime}(x) = 4\mathrm{e}^{x - 3} - 1 - \ln x.$
这里出现了两个大障碍：
(1)  $f^{\prime}(x)$  有两个零点（读者自证），意味着  $f(x)$  有两个极值点；
(2)  $f^{\prime}(x)$  的零点为隐零点，设为  $x_0$  ，有  $4\mathrm{e}^{r_0 - 3} - 1 - \ln x_0 = 0$  ，则  $f(x_0) = 4\mathrm{e}^{r_0 - 3} - x_0\ln x_0 = 1 + \ln x_0 - x_0\ln x_0$  ，下面无法处理.
（其实这也启示了我们，隐零点的设而不求法，只能在其满足的等式较为简单时有用，一旦等式稍为复杂，例如这里，  $4\mathrm{e}^{x_0 - 3} - 1 - \ln x_0 = 0$  ，就很难利用了。）
所以问题1解决了，我们暂时无法证明  $f(x)_{\min} > 0$
对于问题2，我们先看分离后的形式，  $4\mathrm{e}^{x - 3} > x\ln x$  ，首先明确一点，我们之所以分离函数，是希望证明一个更强的结论：  $(4\mathrm{e}^{x - 3})_{\min} > (x\ln x)_{\max}$
但现在， $(x \ln x)_{\max}$  是不存在的，所以需要变形，那么为什么想到除以  $x^2$ ，而不是除以别的数，也不是加上别的数，减去别的数？
事实上, 这是由于高等数学中阶的概念,  $x \ln x$  的阶大于  $x$  但小于  $x^{1 + r}$ , 这里  $r$  为任意一个给定的正实数, 简而言之, 就是当  $x \to +\infty$  时,  $\frac{x \ln x}{x} \to +\infty$ ,  $\frac{x \ln x}{x^{1 + r}} \to 0$ .
所以，这就解释了为什么想到除以  $x^{2}$ ，因为这样  $\frac{x\ln x}{x^2}$  就不再像  $x\ln x$  可以任意大，而会出现极大值，同时说明，除以一切  $x^{1 + r}$  是可以做的，但得出的结果，其精度不一样。
在处理形如  $x^{\alpha}\mathrm{e}^{x} > \ln x + k$  的不等式，两边往往可以同时除以  $x^{\beta}$  ，其原理如下：
设常数  $k \in \mathbb{R}, n > 0$ ，那么函数  $f(x) = \frac{\ln x + k}{x^n}$  有唯一的极大值点（同时也是最大值点）.
由  $f^{\prime}(x) = \frac{\frac{1}{x} \cdot x^{n} - (\ln x + k) \cdot nx^{n-1}}{(x^{n})^{2}} = \frac{1 - n(\ln x + k)}{x^{n+1}}$ ，令  $f^{\prime}(x) = 0$  得  $x = e^{\frac{1}{n} - k}$ ，显然这个极大值点随着  $n$  的增大而减小.
设常数  $m > 0$  ，那么函数  $g(x) = \frac{\mathrm{e}^x}{x^m} (x > 0)$  有唯一的极小值点（同时也是最小值点）.由 $g^{\prime}(x) = \frac{\mathrm{e}^{x}\bullet x^{m} - \mathrm{e}^{x}\bullet mx^{m - 1}}{(x^{m})^{2}} = \frac{\mathrm{e}^{x}(x - m)}{x^{m + 1}}$  ，令  $g^{\prime}(x) = 0$  ，得  $x = m$  显然这个极小值点随着  $m$  的增大而增大，选取的  $m$  应该让两个极值点尽量靠近.
现在再看问题3，我们便可以理解，要使  $a$  更小，关键就在于  $ae^{x} > x\ln x$  的两端除以  $x^{1 + r}$  的幂次的选择，对此，我们可以进行研究  $ae^{x} > x\ln x \Leftrightarrow \frac{ae^{x}}{x^{1 + r}} > \frac{x\ln x}{x^{1 + r}} \Leftrightarrow \frac{ae^{x}}{x^{1 + r}} > \frac{\ln x}{x^{r}}$ ， $r$  为正实数， $\left(\frac{ae^{x}}{x^{1 + r}}\right)' = \frac{ae^{x}x^{1 + r} - (1 + r)x^{r}ae^{x}}{x^{2 + 2r}} = \frac{ae^{x}x^{r}(x - r - 1)}{x^{2 + 2r}}$ ，易知当  $x = r + 1$  时， $\frac{ae^{x}}{x^{1 + r}}$  取得最小值为  $\frac{ae^{r + 1}}{(1 + r)^{1 + r}}$ .
由  $\left(\frac{\ln x}{x^r}\right)' = \frac{x^{r-1} - rx^{r-1}\ln x}{x^{2r}} = \frac{x^{r-1}(1 - r\ln x)}{x^{2r}}$ ，易知  $x = \mathrm{e}^{\frac{1}{r}}$  时， $\frac{\ln x}{x^r}$  取得最大值  $\frac{1}{re}$ . 所以只需  $\frac{ae^{r+1}}{(1+r)^{1+r}}> \frac{1}{re} \Leftrightarrow a>\frac{(1+r)^{1+r}}{re^{r+2}}$ .
所以，任意  $r > 0$  ，只要  $a > \frac{(1 + r)^{1 + r}}{r\mathrm{e}^{r + 2}}$  就有  $a\mathrm{e}^x > x\ln x.$  特别地，取  $r = 1$  ，只要  $a > 4\mathrm{e}^{-3}$  ，就有  $a\mathrm{e}^x > x\ln x$  ，且等号显然取不到，所以  $a \geqslant 4\mathrm{e}^{-3}$  即可，这就是我们的结论.
研究  $\frac{(1 + r)^{1 + r}}{r\mathrm{e}^{r + 2}}$  换元，令  $x = r + 1$  ，则  $x > 1$
令  $g(x) = \frac{x^x}{(x - 1)\mathrm{e}^{x + 1}}$ .  $g'(x) = \frac{x^x(1 + \ln x)(x - 1)\mathrm{e}^{x + 1} - x^x x\mathrm{e}^{x + 1}}{(x - 1)^2\mathrm{e}^{2x + 2}} = \mathrm{e}^{x + 1}x^x\frac{(1 + \ln x)(x - 1) - x}{(x - 1)^2\mathrm{e}^{2x + 2}}.$
（注：  $x^{x}$  的导数为  $x^{x}(1 + \ln x)$  ，方法为令  $t(x) = x^x$  ，左右取对数，  $\ln t(x) = x\ln x$  ，两边求导，由复合函数求导法则，得  $t^\prime (x)\frac{1}{t(x)} = 1 + \ln x$  ，所以  $t^{\prime}(x) = x^{x}(1 + \ln x).)$
易知  $(1 + \ln x)(x - 1) - x$  单调递增，有唯一零点  $x_0\approx 2.3$  且  $g(x)_{\min} = g(x_0)$
综上，用分离函数的方法，能得出  $a$  的最好下界，为  $g(x)_{\min} = g(x_0)\approx g(2.3)$
由于已经有了问题3的经验，问题4也就不难了，简要分析如下：
$m\mathrm{e}^{ar} - x^b\ln x > 0\Leftrightarrow \frac{m\mathrm{e}^{ar}}{x^{b + r}} >\frac{x^b\ln x}{x^{b + r}}\Leftrightarrow \frac{m\mathrm{e}^{ar}}{x^{b + r}} >\frac{\ln x}{x^r},r$ $x = \mathrm{e}^{\frac{1}{r}}$  时，  $\frac{\ln x}{x^r}$  取得最大值  $\frac{1}{re}$  又  $\left(\frac{me^{ar}}{x^{b + r}}\right)' = \frac{ame^{ar}x^{b + r} - (b + r)x^{b + r - 1}me^{ar}}{x^{2b + 2r}} = \frac{me^{ax}x^{b + r - 1}(ax - b - r)}{x^{2b + 2r}},$
可知当  $x = \frac{b + r}{a}$  时， $\frac{m e^{ar}}{x^{b + r}}$  取得最小值  $\frac{m e^{b + r}}{\left(\frac{b + r}{a}\right)^{b + r}} = \frac{m(a e)^{b + r}}{(b + r)^{b + r}}.$
所以只需  $\frac{m(a\mathrm{e})^{b + r}}{(b + r)^{b + r}}\geqslant \frac{1}{re}\Leftrightarrow m\geqslant \frac{1}{re}\left(\frac{b + r}{a\mathrm{e}}\right)^{b + r}.$
于题得出结论：给定正实数  $a, b$ ，对任意的  $r > 0$ ，只要  $m \geqslant \frac{1}{re} \left( \frac{b + r}{ae} \right)^{b + r}$  就有  $m e^{ax} > x^b \ln x$ 。希望同学们从上面的内容中能有所启发，了解数学研究的起点与过程，并在今后的数学学习中，可以开展自己的研究，去发掘数学的无穷奥秘。


## 分离  $\mathrm{e}^x$  和  $\ln x$ 
### 2、同构法
#### 1. “指”“对”跨阶想同构，同左同右取对数
同构基本模式：
（1）积型：  $a\mathrm{e}^{\alpha}\leqslant b\mathrm{ln}b$  三种同构方式
同右：  $\mathrm{e}^{\alpha}\mathrm{ln}\mathrm{e}^{\alpha}\leqslant b\mathrm{ln}b\dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots f(x) = x\mathrm{ln}x$  ，不等式等价于  $f(\mathrm{e}^{a})\leqslant f(b)$
同左：  $a\mathrm{e}^{a}\leqslant (\ln b)\mathrm{e}^{\ln b}\dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots f(x) = x\mathrm{e}^{x}$  ，不等式等价于  $f(a)\leqslant f(\ln b)$
取对数：  $a + \ln a\leqslant \ln b + \ln (\ln b)\dots \dots \dots \rightarrow f(x) = x + \ln x$  ，不等式等价于  $f(a)\leqslant f(\ln b)$
如：  $2x^{3}\ln x\geqslant me^{\frac{m}{x}}\Leftrightarrow x^{2}\ln x^{2}\geqslant \frac{m}{x} e^{\frac{m}{x}}$  ，后面的转化同（1）.
说明：在对“积型”进行同构时，取对数是最快捷的，同构出的函数，其单调性一看便知.
（2）商型：  $\frac{\mathrm{e}^a}{a} < \frac{b}{\ln b}$  三种同构方式
同左：  $\frac{\mathrm{e}^a}{a} <  \frac{\mathrm{e}^{\ln b}}{\ln b}$  →f（x）=，不等式等价于f(a）<f(lnb)
同右：  $\frac{\mathrm{e}^a}{\ln\mathrm{e}^a} <  \frac{b}{\ln b}\dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots f(x) = \frac{x}{\ln x}$  不等式等价于  $f(\mathrm{e}^{a}) <   f(b)$
取对数：  $a - \ln a <   \ln b - \ln (\ln b)\dots \dots \rightarrow f(x) = x - \ln x$  ，不等式等价于  $f(a) <   f(\ln b)$
(3)和差型：  $\mathrm{e}^a\pm a < b\pm \ln b$  两种同构方式
同左：  $\mathrm{e}^a\pm a <   \mathrm{e}^{\ln b}\pm \ln b\dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \to f(x) = \mathrm{e}^x\pm x$  ，不等式等价于  $f(a) <   f(\ln b)$
同右：  $\mathrm{e}^a\pm \mathrm{ln}\mathrm{e}^a <  b\pm \mathrm{ln}b\dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots f(x) = x\pm \ln x$  ，不等式等价于  $f(\mathrm{e}^{a}) <   f(b)$
如：  $\mathrm{e}^{ar} + ax > \ln (x + 1) + x + 1\Longleftrightarrow \mathrm{e}^{ar} + ax > \mathrm{e}^{\ln (x + 1)} + \ln (x + 1)\Longleftrightarrow ax > \ln (x + 1).$
#### 2.“无中生有”去同构，凑好形式是关键，凑常数或凑参数，如有必要凑变量
(1)  $a\mathrm{e}^{ar} > \ln x \xrightarrow{\text{同乘} x \text{（无中生有）}} a x \mathrm{e}^{ar} > x \ln x$ ，转化为  $\mathrm{e}^{ax}\ln \mathrm{e}^{ar} > x\ln x$ ，构造  $f(x) = x\ln x$ ，或转化为  $a x \mathrm{e}^{ax} > \ln x \cdot \mathrm{e}^{\ln x}$ ，构造  $g(x) = x\mathrm{e}^x$ 。
(2)  $\mathrm{e}^{x} > a\ln (ax - a) - a \Leftrightarrow \frac{1}{a}\mathrm{e}^{x} > \ln a(x - 1) - 1 \Leftrightarrow \mathrm{e}^{x - \ln a} - \ln a > \ln (x - 1) - 1$  同加  $x$  （无中生有）  $\mathrm{e}^{x - \ln a} + x - \ln a > \ln (x - 1) + x - 1 = \mathrm{e}^{\ln (x - 1)} + \ln (x - 1)$ ，构造  $f(x) = \mathrm{e}^{x} + x$
转化为  $x - \ln a > \ln (x - 1)$
(3)  $a^x > \log_a x \Leftrightarrow \mathrm{e}^{x\ln a} > \frac{\ln x}{\ln a} \Leftrightarrow (x\ln a)\mathrm{e}^{x\ln a} > x\ln x (a > 1)$ . 后面的转化同 2(1).
说明：由于  $a^x > \log_a x$  两边互为反函数，所以还可以这样转化： $a^x > \log_a x \Rightarrow a^x > x \Rightarrow \ln a > \frac{\ln x}{x}$ 。对于某些不等式，两边互为反函数是比较隐蔽的，若能发现，则难者亦易矣。
如： $\frac{1}{a} \mathrm{e}^x + 1 > \ln a (x - 1)$ ，左右两边互为反函数，所以只需  $\frac{1}{a} \mathrm{e}^x + 1 > x$ ，即  $\frac{1}{a} > \frac{x - 1}{\mathrm{e}^x}$ ，所以若原不等式恒成立，可得  $\frac{1}{a} > \frac{1}{\mathrm{e}^2}$ 。
#### 3. 同构放缩需有方，“切放”同构一起上
(1) 放缩也是一种能力, 利用切线放缩, 往往需要局部同构. 切线放缩是对同构思想方法的一个灵活运用. 另外需注意, 利用切线放缩如同用均值不等式, 只要取等号的条件成立即可.
(2) 掌握常见放缩（注意取等号的条件，以及常见变形）
$\begin{array}{l} \text {①} \mathrm {e} ^ {x} \geqslant x + 1 \Rightarrow \mathrm {e} ^ {x - 1} \geqslant x \Rightarrow \mathrm {e} ^ {x} \geqslant \mathrm {e} x \Rightarrow \mathrm {e} ^ {x} \geqslant \frac {\mathrm {e} ^ {2}}{4} x ^ {2}, \mathrm {e} ^ {x} \geqslant 1 + x + \frac {x ^ {2}}{2} (x \geqslant 0), \mathrm {e} ^ {x} \leqslant \frac {2 + x}{2 - x} (0 \leqslant x <   2), \\ \mathrm {e} ^ {x} \geqslant a x + 1 (x \geqslant 0, a \leqslant 1). \end{array}$
（变形：  $x\mathrm{e}^{x} = \mathrm{e}^{x + \ln x}\geqslant x + \ln x + 1,\frac{\mathrm{e}^{x}}{x} = \mathrm{e}^{x - \ln x}\geqslant x - \ln x + 1,\frac{x}{\mathrm{e}^{x}} = \mathrm{e}^{\ln x - x}\geqslant \ln x - x + 1,$
$x ^ {2} \mathrm {e} ^ {x} = \mathrm {e} ^ {r + 2 \ln r} \geqslant x + 2 \ln x + 1, x ^ {2} \mathrm {e} ^ {x} = \mathrm {e} ^ {x + 2 \ln x} \geqslant \mathrm {e} (x + 2 \ln x).)$
$② \ln x \leqslant x - 1 \Rightarrow \ln \mathrm {e} x \leqslant x \Rightarrow \ln x \leqslant \frac {x}{\mathrm {e}}, \ln x \leqslant x - 1 \Rightarrow \ln x \leqslant \mathrm {e} ^ {x} - 2,$
$\ln x \geqslant 1 - \frac {1}{x} \Rightarrow x \ln x \geqslant x - 1, \ln x \leqslant \frac {1}{2} \left(x - \frac {1}{x}\right) (x \geqslant 1), \ln x \geqslant \frac {2 (x - 1)}{x + 1} (x \geqslant 1),$
$\ln x \leqslant a (x - 1) (x \geqslant 1, a \geqslant 1)$ . （变形： $x + \ln x = \ln x e^{x}, x - \ln x = \ln \frac{e^{x}}{x}$ .）
说明:  $x \mathrm{e}^{x} = \mathrm{e}^{x + \ln x}, \frac{\mathrm{e}^{x}}{x} = \mathrm{e}^{x - \ln x}, \frac{x}{\mathrm{e}^{x}} = \mathrm{e}^{\ln x - x}, x + \ln x = \ln x \mathrm{e}^{x}, x - \ln x = \ln \frac{\mathrm{e}^{x}}{x}$  等, 这些变形对解决指对混合不等式问题, 如恒成立求参数取值范围, 或证明不等式, 都带来极大的便利. 当然, 在具体使用中, 往往要结合切线放缩或换元法. 可以说掌握了这些变形常见切线型不等式, 就大大降低了这类问题的难度. (会推广到关于  $x$  与  $a^{x}$  或  $\log_{a} x$  的各种组合的变形.)
同构变形在不等式恒成立问题中应用很广, 恒成立问题有很大一部分题目是命题者利用函数单调性构造出来的, 那么我们只要找到函数, 无疑就是找到了题目的命门. 在寻找函数时, 进行分组整理是一种常见的变形. 如果整理 (即同构) 后不等式两边具有结构的一致性, 则可构造函数, 然后利用此函数的单调性解题.
##### 例5.11 若对任意  $x > 0$  ，恒有  $a(\mathrm{e}^{ax} + 1) \geqslant 2\left(x + \frac{1}{x}\right)\ln x$  ，则实数  $a$  的最小值为
分析 观察不等式形式，需“无中生有”两边同乘以  $x$  ，将不等式变形为积型同构模型  $ax(\mathrm{e}^{ax} + 1) \geqslant (x^2 + 1)\ln x^2$  ，右边不变，变形  $ax = \ln \mathrm{e}^{ax}$  ，这样不等式两边结构一致，从中构造出函数，根据单调性简化不等式.

<span class="fake-tag">解析</span>  $a(\mathrm{e}^{ar} + 1)\geqslant 2\left(x + \frac{1}{x}\right)\ln x\Leftrightarrow ax(\mathrm{e}^{ar} + 1)\geqslant (x^2 +1)\ln x^2\Leftrightarrow (\mathrm{e}^{ar} + 1)\ln \mathrm{e}^{ar}\geqslant (x^2 +$  1)  $\ln x^2$  .（积型同构）
令  $f(x) = (x + 1)\ln x$ ，则  $f'(x) = \ln x + \frac{x + 1}{x}$ ， $f''(x) = \frac{1}{x} - \frac{1}{x^2} = \frac{x - 1}{x^2}$ ，易知  $f'(x)$  在  $(0,1)$  上单调递减，在  $(1, +\infty)$  上单调递增，所以  $f'(x) \geq f'(1) = 2 > 0$ ，所以  $f(x)$  在  $(0, +\infty)$  上单调递增，则  $\left(\mathrm{e}^{ax} + 1\right)\ln \mathrm{e}^{ax} \geqslant (x^2 + 1)\ln x^2 \Leftrightarrow f\left(\mathrm{e}^{ar}\right) \geqslant f\left(x^2\right) \Leftrightarrow \mathrm{e}^{ar} \geqslant x^2 \Leftrightarrow ax \geqslant 2\ln x \Leftrightarrow a \geqslant \frac{2\ln x}{x}$ .
令  $g(x) = \frac{2\ln x}{x}$ , 由导数法易得  $\left(\frac{2\ln x}{x}\right)_{\max} = \frac{2\ln e}{e} = \frac{2}{e}$ , 所以  $a \geqslant \frac{2}{e}$ .
故实数  $a$  的最小值为  $\frac{2}{e}$
##### 变式若  $x\in \left(0,\frac{1}{\mathrm{e}}\right)$  时，关于  $x$  的不等式  $ax^3\mathrm{e}^{ax} + 2\ln x\leqslant 0$  恒成立，则  $a$  的最大值是

<span class="fake-tag">解析</span> 由  $ax^3 e^{ar} + 2 \ln x \leqslant 0$ ，得  $a x e^{a r} + \frac{2}{x^2} \ln x \leqslant 0 \Leftrightarrow a x e^{a r} \leqslant -\frac{2}{x^2} \ln x = \frac{1}{x^2} \ln \frac{1}{x^2} = \ln \frac{1}{x^2} e^{\ln \frac{1}{x^2}}, x \in (0, \frac{1}{e})$ .
上述不等式对于  $a \leqslant 0$  显然成立.
当  $a > 0$  时，构造函数  $f(x) = x\mathrm{e}^{x},x > 0,f^{\prime}(x) = (x + 1)\mathrm{e}^{x} > 0$  ，函数  $f(x)$  在  $(0, + \infty)$  上单调递增，故  $f(ax)\leqslant f\left(\ln {\frac{1}{x^2}}\right)$  ，得  $ax\leqslant \ln \frac{1}{x^2} = -2\ln x.$  因此  $a\leqslant \frac{-2\ln x}{x},0 <   x <   \frac{1}{\mathrm{e}}.$
令  $g(x) = \frac{-2\ln x}{x}, g'(x) = -2 \cdot \frac{1 - \ln x}{x^2} = \frac{2(\ln x - 1)}{x^2}$ .
当  $0 < x < e$  时， $g'(x) < 0, g(x)$  单调递减；当  $x > e$  时， $g'(x) > 0, g(x)$  单调递增.
又  $0 < x < \frac{1}{\mathrm{e}}$  ，则  $g(x)_{\min} > g\left(\frac{1}{\mathrm{e}}\right) = \frac{-2\ln\frac{1}{\mathrm{e}}}{\frac{1}{\mathrm{e}}} = 2\mathrm{e}$  因此  $a \leqslant 2\mathrm{e}$  ，故  $a$  的最大值是  $2\mathrm{e}$ .
##### 变式2 对任意  $x > 0$  ，不等式  $2ae^{2x} - \ln x + \ln a\geqslant 0$  恒成立，则实数  $a$  的最小值为
分析 将指对分列两侧，不等式变形为积型同构模型  $2x\mathrm{e}^{2x}\geqslant \frac{x}{a}\ln \frac{x}{a}$  ，两边取对数，得
$2x + \ln 2x\geqslant \ln {\frac{x}{a}} + \ln \left(\ln {\frac{x}{a}}\right)(x > a)$  ，从中构造出函数，根据其单调性简化不等式.

<span class="fake-tag">解析</span>  $2ae^{2x} - \ln x + \ln a\geqslant 0\Leftrightarrow 2ae^{2x}\geqslant \ln \frac{x}{a}\Leftrightarrow 2xe^{2x}\geqslant \frac{x}{a}\ln \frac{x}{a} (x > 0)$  （积型同构）
$\Leftrightarrow 2 x + \ln 2 x \geqslant \ln \frac {x}{a} + \ln \left(\ln \frac {x}{a}\right) (x > a).$
设  $f(x) = x + \ln x$  ，由于  $f(x)$  为增函数，所以由  $f(2x) \geqslant f\left(\ln \frac{x}{a}\right)$ ，得  $2x \geqslant \ln \frac{x}{a}$ ，即  $a \geqslant \frac{x}{e^{2x}}$  恒成立. 令  $g(x) = \frac{x}{e^{2x}}$ ，则  $g'(x) = \frac{1 - 2x}{e^{2x}}$ ，易得  $g(x)_{\max} = g\left(\frac{1}{2}\right) = \frac{1}{2e}$ ，所以  $a \geqslant \frac{1}{2e}$ ，即实数  $a$  的最小值为  $\frac{1}{2e}$ .
##### 例5.12 已知函数  $f(x) = x(\mathrm{e}^x - a) - 2\ln x + 2\ln 2 - 2(a \in \mathbb{R})$ .
（1）当  $a = 2$  时，若  $f(x)$  的一条切线垂直于  $y$  轴，证明：该切线为  $x$  轴；
(2) 若  $f(x) \geq 0$ ，求  $a$  的取值范围.
分析 (1) 证明该切线为  $x$  轴即证切线方程为  $y = 0$ , 为此用设而不求也就是隐零点的方法得出一个关于该切点横坐标  $x_0$  的方程, 代入切线方程化简即可; (2) 把不等式变形整理, 根据恒成立得出  $a$  的取值范围, 再进一步证明其补集不满足; 另外本问也可以将参变量分离, 转化为最值问题来解.

<span class="fake-tag">解析</span> (1) 当  $a = 2$  时,  $f(x) = x(\mathrm{e}^x - 2) - 2\ln x + 2\ln 2 - 2$  ，则
$\begin{array}{l} f ^ {\prime} (x) = \mathrm {e} ^ {x} - 2 + x \mathrm {e} ^ {x} - \frac {2}{x} = \mathrm {e} ^ {x} (x + 1) - 2 \left(\frac {1}{x} + 1\right) = \mathrm {e} ^ {x} (x + 1) - \frac {2 (x + 1)}{x} \\ = (x + 1) \left(\mathrm {e} ^ {x} - \frac {2}{x}\right) (x > 0). \\ \end{array}$
令  $f^{\prime}(x_0) = 0$  得  $\mathrm{e}^{x_0} = \frac{2}{x_0}$ ，即  $x_0\mathrm{e}^{x_0} = 2$ ，亦即  $x_0 + \ln x_0 = \ln 2$ .
曲线  $y = f(x)$  在点  $(x_0, f(x_0))$  处的切线方程为  $y - f(x_0) = f'(x_0)(x - x_0)$ ，即  $y - [x_0(\mathrm{e}^{x_0} - 2) - 2\ln x_0 + 2\ln 2 - 2] = 0$ ，亦即  $y = x_0(\mathrm{e}^{x_0} - 2) - 2\ln x_0 + 2\ln 2 - 2$ ，故  $y = x_0\left(\frac{2}{x_0} - 2\right) - 2(\ln 2 - x_0) + 2\ln 2 - 2 = 2 - 2x_0 - 2\ln 2 + 2x_0 + 2\ln 2 - 2 = 0$ ，则该切线为  $x$  轴.
(2) 解法一（同构，经典不等式放缩）：若  $f(x) \geqslant 0$ ，得  $x(\mathrm{e}^x - a) - 2\ln x + 2\ln 2 - 2 \geqslant 0$ ，得  $\frac{1}{2} x(\mathrm{e}^x - a) - \ln x + \ln 2 - 1 \geqslant 0$ ，即  $\frac{1}{2} x\mathrm{e}^x - \frac{1}{2} ax - \ln x + \ln 2 - 1 \geqslant 0, \frac{1}{2}\mathrm{e}^{\ln x + x} - \frac{1}{2} ax - \ln x + \ln 2 - 1 \geqslant 0, \mathrm{e}^{\ln x + x - \ln 2} - x - \ln x + \ln 2 - \frac{1}{2} ax + x - 1 \geqslant 0$ ，即  $\mathrm{e}^{\ln x + x - \ln 2} - (x + \ln x - \ln 2) - 1 \geqslant \left(\frac{a}{2} - 1\right)x.$
由  $\mathrm{e}^x\geqslant x + 1$  （当且仅当  $x = 0$  时取“  $=$  ”），则  $\mathrm{e}^{\ln x + x - \ln 2}\geqslant \ln x + x - \ln 2 + 1$  （当且仅当  $\ln x + x-$ $\ln 2 = 0$  时取“  $=$  ”），故当  $\frac{a}{2} -1\leqslant 0$  即  $a\leqslant 2$  时，  $f(x)\geqslant 0$  恒成立.
下面证明当  $a > 2$  时， $f(x) \geqslant 0$  不恒成立，取  $x_0$ ，使  $\ln x_0 + x_0 - \ln 2 = 0$ .
此时  $f(x_0) = \mathrm{e}^{\ln x_0 + x_0 - \ln 2} - (x_0 + \ln x_0 - \ln 2) - 1 - \left(\frac{a}{2} - 1\right)x_0 = \left(1 - \frac{a}{2}\right)x_0 < 0$ ，与题意不符.
综上所述，  $a$  的取值范围为  $(-\infty ,2]$
解法二（分离参数）：由  $\forall x\geqslant 0,f(x)\geqslant 0$  得  $a\leqslant \frac{x\mathrm{e}^x - 2\ln x + 2\ln 2 - 2}{x} = \mathrm{e}^x -\frac{2\ln x + 2 - 2\ln 2}{x}.$
构造  $g(x) = \mathrm{e}^{x} - \frac{2\ln x + 2 - 2\ln 2}{x}$ ，则
$g ^ {\prime} (x) = \mathrm {e} ^ {x} - \frac {\frac {2}{x} \cdot x - (2 \ln x + 2 - 2 \ln 2)}{x ^ {2}} = \mathrm {e} ^ {x} - \frac {2 - 2 \ln x - 2 + 2 \ln 2}{x ^ {2}} = \mathrm {e} ^ {x} - \frac {2 \ln \frac {2}{x}}{x ^ {2}} = \frac {x ^ {2} \mathrm {e} ^ {x} - 2 \ln \frac {2}{x}}{x ^ {2}}.$
令  $g^{\prime}(x_0) = 0$  ，得  $x_0^2\mathrm{e}^{x_0} = 2\ln \frac{2}{x_0} (x_0 > 0)$  ，即  $x_0\mathrm{e}^{x_0} = \frac{2}{x_0}\ln \frac{2}{x_0} = \mathrm{e}^{\ln \frac{2}{x_0}}\cdot \ln \frac{2}{x_0}.$  （同构）
令  $u(x) = x\mathrm{e}^{x}(x > 0),u^{\prime}(x) = \mathrm{e}^{x}(x + 1) > 0,u(x)$  在  $(0, + \infty)$  上单调递增，又  $u(x_0) = u\left(\ln \frac{2}{x_0}\right)$  ，则  $x_0 = \ln \frac{2}{x_0}$  故  $\mathrm{e}^{x_0} = \frac{2}{x_0}$  即  $x_0\mathrm{e}^{x_0} = 2$
因为  $g^{\prime}(x) = \mathrm{e}^{x} - \frac{2}{x^{2}}\ln \frac{2}{x}$  在  $(0, + \infty)$  上单调递增，  $g^{\prime}(x_0) = 0$  ，所以  $g(x)$  在  $(0,x_0)$  上单调递减，在  $(x_0, + \infty)$  上单调递增.
$g (x) _ {\min } = g (x _ {0}) = \mathrm {e} ^ {x _ {0}} - \frac {2 \ln x _ {0} + 2 - 2 \ln 2}{x _ {0}}, \text {代 入} \mathrm {e} ^ {x _ {0}} = \frac {2}{x _ {0}} \text {和} \ln \frac {2}{x _ {0}} = x _ {0}, \text {则} g (x _ {0}) = \frac {2}{x _ {0}} - \frac {2}{x _ {0}} -$
$\frac {2 \ln x _ {0} - 2 \ln 2}{x _ {0}} = \frac {2 \ln 2 - 2 \ln x _ {0}}{x _ {0}} = \frac {2 \ln \frac {2}{x _ {0}}}{x _ {0}} = \frac {2 x _ {0}}{x _ {0}} = 2.$
故  $g(x)_{\min} = g(x_0) = 2$  ，故  $a \leqslant 2$  ，即  $a$  的取值范围为  $(- \infty, 2]$ .




## 不分离  $\mathrm{e}^x$  和  $\ln x$  
##### 例5.7 已知函数  $f(x) = x\mathrm{e}^{x} - x - \ln x - 1$ ，证明：  $f(x)\geqslant 0$
分析 不分离  $\mathrm{e}^x$  和  $\ln x$ , 由于对  $f(x) = x\mathrm{e}^{x} - x - \ln x - 1$  求导后  $\mathrm{e}^x - \frac{1}{x} = 0$  是超越方程, 求不出具体的解, 根据单调性判断  $\mathrm{e}^x - \frac{1}{x} = 0$  有唯一零点, 通过虚设零点, 得到隐零点对应的方程来实现简化函数的目的, 得到要证明的结论.

<span class="fake-tag">解析</span>  $f^{\prime}(x) = \mathrm{e}^{x} + x\mathrm{e}^{x} - 1 - \frac{1}{x} = (x + 1)\left(\mathrm{e}^{x} - \frac{1}{x}\right)$  ，注意到函数定义域为  $(0, + \infty)$
所以  $x + 1 > 0$  ，令  $g(x) = \mathrm{e}^x -\frac{1}{x}$  显然  $g(x)$  单调递增.
而  $g\left(\frac{1}{2}\right) = \sqrt{\mathrm{e}} - 2 < 0, g(1) = \mathrm{e} - 1 > 0$ ，所以  $g(x)$  在  $\left(\frac{1}{2}, 1\right)$  上有一个零点  $x_0$ ，结合单调性，可知  $g(x)$  仅有这一个零点，则  $g(x_0) = 0$ ，即  $\mathrm{e}^{x_0} - \frac{1}{x_0} = 0 \Leftrightarrow x_0 = -\ln x_0$ ，且可知  $g(x)$  在  $(0, x_0)$  上小于 0，在  $(x_0, +\infty)$  上大于 0，所以  $f(x)$  在  $(0, x_0)$  上单调递减，在  $(x_0, +\infty)$  上单调递增。
又  $f(x)_{\min} = f(x_0) = x_0 \mathrm{e}^{x_0} - x_0 - \ln x_0 - 1 = 1 - x_0 + x_0 - 1 = 0$  ，故  $f(x) \geqslant 0$
### 评注
本题中零点满足  $\mathrm{e}^{x_0} = \frac{1}{x_0}$ , 两边取对数, 即  $x_0 = -\ln x_0$ , 尽管我们不能解出  $x_0$  的值, 但我们可以虚设隐零点  $x_0$ , 利用其满足的上述两个等式, 遵循指数、对数函数向幂函数转化的原则, 就可以巧妙化简原函数, 得到要证的结论.
##### 变式（1）（2017新课标全国Ⅱ卷理21)已知函数  $f(x) = ax^{2} - ax - x\ln x$  ，且  $f(x)\geqslant 0$
(1)求  $a$  的值；  
(2) 证明:  $f(x)$  存在唯一的极大值点  $x_0$ , 且  $\mathrm{e}^{-2} < f(x_0) < 2^{-2}$ .

<span class="fake-tag">解析</span> (1) 解法一（分类讨论）：因为  $f(x) = x(ax - a - \ln x) \geqslant 0, x > 0$ ，所以  $ax - a - \ln x \geqslant 0$ . 令  $g(x) = ax - a - \ln x$ ，则  $g(1) = 0, g'(x) = a - \frac{1}{x} = \frac{ax - 1}{x}$ .
当  $a \leqslant 0$  时， $g'(x) < 0, g(x)$  单调递减，但  $g(1) = 0$  ，当  $x > 1$  时， $g(x) < 0$  ，不满足题意.
当  $a > 0$  时，令  $g^{\prime}(x) = 0$  ，得  $x = \frac{1}{a}$  当  $0 <   x <   \frac{1}{a}$  时，  $g^{\prime}(x) <   0$  ，此时  $g(x)$  单调递减；当  $x > \frac{1}{a}$
时，  $g^{\prime}(x) > 0$  ，此时  $g(x)$  单调递增
若  $0 < a < 1$ ，则  $g(x)$  在  $\left(1, \frac{1}{a}\right)$  上单调递减， $g\left(\frac{1}{a}\right) < g(1) = 0$ ，不满足题意；
若  $a > 1$  ，则  $g(x)$  在  $\left(\frac{1}{a}, 1\right)$  上单调递增， $g\left(\frac{1}{a}\right) < g(1) = 0$  ，不满足题意；
若  $a = 1$  ，则  $g(x)_{\min} = g\left(\frac{1}{a}\right) = g(1) = 0$  ，则  $g(x)\geqslant 0$
综上所述，  $a = 1$
解法二（极值点定义）：由  $f(x) \geqslant 0 \Leftrightarrow f(x) \geqslant f(1)$ ，则  $f'(1) = 0$ ，又  $f'(x) = 2ax - a - 1 - \ln x, f'(1) = a - 1 = 0$ ，得  $a = 1$ .
再证：当  $a = 1$  时， $f(x) = x^2 - x - x \ln x \geqslant 0$ ，即  $x - 1 - \ln x \geqslant 0 \Leftrightarrow \ln x \leqslant x - 1$ ，易证。所以  $a = 1$
(2)  $f(x) = x^{2} - x - x \ln x, f^{\prime}(x) = 2x - 2 - \ln x, x > 0.$
令  $h(x) = 2x - 2 - \ln x$  ，则  $h^{\prime}(x) = 2 - \frac{1}{x} = \frac{2x - 1}{x},x > 0.$  令  $h^\prime (x) = 0$  ，得  $x = \frac{1}{2}$
当  $0 < x < \frac{1}{2}$  时， $h'(x) < 0$ ，此时  $h(x)$  单调递减；当  $x > \frac{1}{2}$  时， $h'(x) > 0$ ，此时  $h(x)$  单调递增，所以  $h(x)_{\min} = h\left(\frac{1}{2}\right) = 1 - 2 + \ln 2 < 0$ .
因为  $h(\mathrm{e}^{-2}) = 2\mathrm{e}^{-2} > 0,h(2) = 2 - \ln 2 > 0$  ，且  $\mathrm{e}^{-2}\in \left(0,\frac{1}{2}\right),2\in \left(\frac{1}{2}, + \infty\right)$  ，所以在  $\left(0,\frac{1}{2}\right)$  和 $\left(\frac{1}{2}, + \infty\right)$  上，  $h(x)$  即  $f^{\prime}(x)$  各有一个零点.
设  $f^{\prime}(x)$  在  $\left(0, \frac{1}{2}\right)$  和  $\left(\frac{1}{2}, +\infty\right)$  上的零点分别为  $x_0, x_2$ ，因为  $f^{\prime}(x)$  在  $\left(0, \frac{1}{2}\right)$  上单调递减，所以当  $0 < x < x_0$  时， $f^{\prime}(x) > 0$ ，此时  $f(x)$  单调递增；当  $x_0 < x < \frac{1}{2}$  时， $f^{\prime}(x) < 0$ ，此时  $f(x)$  单调递减，因此  $x_0$  是  $f(x)$  的极大值点。
因为  $f^{\prime}(x)$  在  $\left(\frac{1}{2}, + \infty\right)$  上单调递增，所以当  $\frac{1}{2} < x < x_2$  时， $f^{\prime}(x) < 0$  ，此时  $f(x)$  单调递减，当  $x > x_2$  时， $f^{\prime}(x) > 0, f(x)$  单调递增，因此  $x_2$  是  $f(x)$  的极小值点.
所以  $f(x)$  有唯一的极大值点  $x_0$
由前面的证明可知，  $x_0\in \left(\mathrm{e}^{-2},\frac{1}{2}\right)$  ，则  $f(x_0) > f(\mathrm{e}^{-2}) = \mathrm{e}^{-4} + \mathrm{e}^{-2} > \mathrm{e}^{-2}.$
因为  $f^{\prime}(x_0) = 2x_0 - 2 - \ln x_0 = 0$ ，所以  $\ln x_0 = 2x_0 - 2$ ，又  $f(x_0) = x_0^2 - x_0 - x_0(2x_0 - 2) = x_0 - x_0^2, 0 < x_0 < \frac{1}{2}$ ，所以  $f(x_0) < \frac{1}{4}$ .
因此  $\mathrm{e}^{-2} < f(x_0) < \frac{1}{4}$ . 即  $\mathrm{e}^{-2} < f(x_0) < 2^{-2}$ .
##### 变式2 已知函数  $f(x) = x\mathrm{e}^{x} - a\mathrm{e}^{2x}(a\in \mathbb{R})$  恰有两个极值点  $x_{1},x_{2}(x_{1} <   x_{2})$
(1)求实数  $a$  的取值范围；  
(2) 求证:  $f(x_{2}) > -\frac{1}{2}$ .

<span class="fake-tag">解析</span>  $\Rightarrow (1)f^{\prime}(x) = \mathrm{e}^{x}(x + 1 - 2ae^{x})$  ，要使得  $f(x)$  恰有两个极值点，则方程  $x + 1 - 2ae^{x} = 0$  有2个不相等的实根，令  $g(x) = x + 1 - 2ae^{x},g^{\prime}(x) = 1 - 2ae^{x}$
（i）当  $a \leqslant 0$  时， $g'(x) > 0, g(x)$  在  $\mathbf{R}$  上单调递增，不合题意.
（ii）当  $a > 0$  时，令  $g'(x) = 0$  ，解得  $x = \ln \frac{1}{2a}$ ，且当  $x < \ln \frac{1}{2a}$  时， $g(x)$  单调递增；当  $x > \ln \frac{1}{2a}$  时， $g(x)$  单调递减.
若  $g(x)$  有2个不同实根，则  $g\left(\ln \frac{1}{2a}\right) > 0 \Leftrightarrow \ln \frac{1}{2a} + 1 - 1 > 0$  ，即  $0 < a < \frac{1}{2}$ .
且当  $0 < a < \frac{1}{2}$  时， $\ln \frac{1}{2a} > 0, g(-1) = -2ae^{-1} < 0$ ，所以  $g(x)$  在  $(-1, -\ln 2a)$  上有一个零点.
当  $x > -\ln (2a)$  时，  $\mathrm{e}^x = (\mathrm{e}^{\frac{x}{2}})^2 >\left(\frac{x}{2} +1\right)^2 >\frac{(x + 1)^2}{4}$  则  $g(x) = x + 1 - 2ae^{x} <   (x + 1) -$ $\frac{a(x + 1)^2}{2} = (x + 1)\left[1 - \frac{a(x + 1)}{2}\right].$
令  $a(\xi + 1) = 2$ ，得  $\xi = \frac{2}{a} - 1$ 。以下证明  $\frac{2}{a} - 1$  在  $(- \ln 2a, +\infty)$  上，即证  $\frac{2}{a} - 1 + \ln 2a > 0$ 。令  $h(a) = \frac{2}{a} - 1 + \ln (2a), 0 < a < \frac{1}{2}, h'(a) = -\frac{2}{a^2} + \frac{1}{a} = \frac{a - 2}{a^2} < 0, h(a)$  在  $(0, \frac{1}{2})$  上单调递减，因此  $h(a) > h\left(\frac{1}{2}\right) > 0$ ，则  $\frac{2}{a} - 1 > \ln \frac{1}{2a}$ 。所以  $g(x)$  在  $(- \ln 2a, +\infty)$  上有一个零点。
综上所述，若  $f(x)$  有两个极值点，则  $a$  的取值范围是  $\left(0, \frac{1}{2}\right)$ .
(2) 由 (1) 知  $f(x)$  有极值点  $x_1, x_2, x_1 < \ln \frac{1}{2a} < x_2$ ，且  $x_1, x_2$  满足  $x + 1 - 2ae^x = 0$ ，则  $x_2 + 1 - 2ae^{x_2} = 0$ ，即  $2ae^{x_2} = x_2 + 1$ ，所以  $f(x_2) = x_2e^{x_2} - ae^{2x_2} = e^{x_2}(x_2 - ae^{x_2}) = \frac{e^{x_2}}{2}(x_2 - 1)$ ，其中  $x_2 > \ln \frac{1}{2a} > 0$ ，即令  $m(x) = \frac{e^x}{2}(x - 1)\left(x > \ln \frac{1}{2a} > 0\right)$ .
又  $m'(x) = \frac{1}{2} \mathrm{e}^x (x - 1) + \frac{\mathrm{e}^x}{2} = \frac{x \mathrm{e}^x}{2} > 0, m(x)$  在  $\left(\ln \frac{1}{2a}, +\infty\right)$  上单调递增，所以  $m(x) > m\left(\ln \frac{1}{2a}\right) = \frac{1}{4a}\left(\ln \frac{1}{2a} - 1\right) = -\frac{1 + \ln 2a}{4a}, 0 < a < \frac{1}{2}$ .
	令  $n(a) = -\frac{1 + \ln 2a}{4a}, 0 < a < \frac{1}{2}, n'(a) = -\frac{\frac{1}{a} \cdot 4a - [1 + \ln(2a)] \cdot 4}{16a^2} = -\frac{4 - 4 - 4\ln(2a)}{16a^2} = \frac{\ln(2a)}{4a^2} < 0$ ，所以  $n(a)$  在  $\left(0, \frac{1}{2}\right)$  上单调递减， $n(a) > n\left(\frac{1}{2}\right) = -\frac{1}{2}$ ，即  $m(x) > n(a) > -\frac{1}{2}$ ，即  $f(x_2) > -\frac{1}{2}$ .





## 切线放缩
切线放缩就是根据凹凸性, 把函数恰当变形, 用相应的切线不等式放缩求出函数的最值或证明不等式, 常用的切线放缩及其衍生放缩公式为  $\mathrm{e}^x \geqslant x + 1, \mathrm{e}^x \geqslant \mathrm{e}x, \ln x \leqslant x - 1 (x > 0), \ln x \leqslant \frac{x}{\mathrm{e}} (x > 0)$ .
### 1. 利用切线放缩求函数最值
### 研究密钥
含指对混合形式的不等式通过等价变形、取对数等方法变化形式，然后利用两个重要的切线不等式  $(\mathrm{e}^x \geqslant x + 1$  和  $\ln x \leqslant x - 1)$  进行放缩，不等式取等号时即为相应函数的最值.
其中，常见的同构变形有  $x\mathrm{e}^{x} = \mathrm{e}^{x + \ln x},\frac{\mathrm{e}^{x}}{x} = \mathrm{e}^{x - \ln x},x^{2}\mathrm{e}^{x} = \mathrm{e}^{x + 2\ln x},\frac{x}{\mathrm{e}^{x}} = \mathrm{e}^{\ln x - x},x + \ln x = \ln x\mathrm{e}^{x},x - \ln x = \ln \frac{\mathrm{e}^{x}}{x}.$
##### 例5.8 运用切线放缩，求函数最值
(1)函数  $f(x) = \mathrm{e}^{x} - \frac{\ln x + 1}{x}$  的最小值是  
(2)函数  $f(x) = \frac{x^2\mathrm{e}^x - 2\ln x}{x + 1}$  的最小值是  
(3) 已知函数  $f(x) = x \mathrm{e}^{x} - \ln x - x - 2, g(x) = \frac{\mathrm{e}^{x - 2}}{x} + \ln x - x$  的最小值分别为  $a, b$ ，判断  $a, b$  之间的大小关系.
分析 观察函数形式，发现函数解析式或通分后出现常见的变形形式，如  $x\mathrm{e}^x$  ， $x^{2}\mathrm{e}^{x},\frac{\mathrm{e}^{x}}{x}$  等，先将其指数化，然后将指数函数放缩为它的切线，不等式取等号时即为所求函数的最值.

<span class="fake-tag">解析</span>  $\gg (1) f(x) = \mathrm{e}^x - \frac{\ln x + 1}{x} = \frac{x\mathrm{e}^x - \ln x - 1}{x} = \frac{\mathrm{e}^{x + \ln x} - \ln x - 1}{x} \geqslant \frac{x + \ln x + 1 - \ln x - 1}{x} = 1$  （当且仅当  $x + \ln x = 0$  时取“=”），故  $f(x)$  的最小值为 1.
(2)  $f(x) = \frac{x^2 \mathrm{e}^x - 2 \ln x}{x + 1} = \frac{\mathrm{e}^{x + 2 \ln x} - 2 \ln x}{x + 1} \geqslant \frac{x + 2 \ln x + 1 - 2 \ln x}{x + 1} = 1$  (当且仅当  $x + 2 \ln x = 0$  时取 “=”), 故  $f(x)$  的最小值为 1.
(3)  $f(x) = x \mathrm{e}^{x} - \ln x - x - 2 = \mathrm{e}^{x + \ln x} - (x + \ln x) - 2 \geqslant x + \ln x + 1 - (x + \ln x) - 2 = -1$  （当且仅当  $x + \ln x = 0$  时取“=”），故  $f(x)$  的最小值为-1.
$g(x) = \frac{\mathrm{e}^{x - 2}}{x} +\ln x - x = \mathrm{e}^{x - 2 - \ln x} - (x - \ln x)\geqslant x - \ln x - 1 - (x - \ln x) = -1$  （当且仅当  $x-$ $\ln x = 2$  时取“  $=$  ”），故  $g(x)$  的最小值为-1.
因此，  $a = b = -1$
### 2. 切线放缩解不等式恒成立问题
### 研究密码
利用切线放缩解不等式恒成立时参数的取值范围问题, 多将指数、对数、无理根式等统一到一阶幂函数的形式, 即转化为曲线与直线的位置关系, 难点是寻找切线放缩的位置, 移动曲线或切线找到那个重合处的分界点 (临界点), 通常于端点处进行放缩, 使得问题得以简化.
##### 例5.9 运用切线放缩，求解下列不等式恒成立问题
（1）已知函数  $f(x) = x^{b}\mathrm{e}^{x} - a\ln x - x - 1(x > 1)$  ，其中  $b > 0$  .若  $f(x)\geqslant 0$  恒成立，则实数  $a$  与 $b$  的大小关系是  
(2) 若对任意的  $x \in (0, +\infty), \mathrm{e}^{2t} - a - \frac{\ln x}{x} \geqslant \frac{1}{x}$  恒成立，则  $a$  的取值范围为 ______；  
(3)已知  $x^{3} \mathrm{e}^{2x} - 1 \geqslant mx + 3 \ln x$  对  $x \in (0, +\infty)$  恒成立，则实数  $m$  的取值范围为
分析 对于指、对混合型的不等式恒成立问题，通常参变量分离，把问题转化为求指、对混合型函数的最值问题，运用切线放缩  $(\mathrm{e}^x\geqslant x + 1,\mathrm{e}^x\geqslant \mathrm{e}x,\ln x\leqslant x - 1)$  ，将对数函数或指数函数放缩成易于处理的幂函数的形式，便于研究函数的最值.

<span class="fake-tag">解析</span>  $\Rightarrow (1) f(x) \geqslant 0 \Leftrightarrow x^b e^x \geqslant a \ln x + x + 1 \Leftrightarrow e^{x + b \ln x} - x - 1 \geqslant a \ln x \Leftrightarrow a \leqslant \frac{e^{x + b \ln x} - x - 1}{\ln x}$ , 其中  $x > 1$ .
因为  $\frac{\mathrm{e}^{x + b\ln x} - x - 1}{\ln x}\geqslant \frac{x + b\ln x + 1 - x - 1}{\ln x} = b$  ，当且仅当  $x + b\ln x = 0$  时等号成立，所以  $a\leqslant b$
(2) 依题意,  $\mathrm{e}^{2x} - a - \frac{\ln x}{x} \geqslant \frac{1}{x}$  对任意的  $x \in (0, +\infty)$  恒成立, 则  $a \leqslant \mathrm{e}^{2x} - \frac{\ln x + 1}{x} = \frac{x \mathrm{e}^{2x} - \ln x - 1}{x} = \frac{\mathrm{e}^{2x + \ln x} - \ln x - 1}{x}$ .
又  $\mathrm{e}^{2x + \ln x} \geqslant 2x + \ln x + 1$  （当且仅当  $2x + \ln x = 0$  时取“ $=$ ”），因此  $\frac{\mathrm{e}^{2x + \ln x} - \ln x - 1}{x} \geqslant \frac{2x + \ln x + 1 - \ln x - 1}{x} = 2$ ，所以  $a \leqslant 2$ ，因此实数  $a$  的取值范围是  $(- \infty, 2]$ .
(3) 分离自变量和参变量.  $m \leqslant \frac{x^3 \mathrm{e}^{2x} - 3 \ln x - 1}{x} = \frac{\mathrm{e}^{2x + 3 \ln x} - (3 \ln x + 1)}{x}$ , 又  $\mathrm{e}^{2x + 3 \ln r} \geqslant 2x + 3 \ln x + 1$  (当且仅当  $2x + 3 \ln x = 0$  时取“=”), 则  $\frac{\mathrm{e}^{2x + 3 \ln x} - 3 \ln x - 1}{x} \geqslant \frac{2x + 3 \ln x + 1 - 3 \ln x - 1}{x} = 2$ . 因此  $m$  的取值范围是  $(- \infty, 2]$ .
### 3. 切线放缩证明不等式
### 研究密钥
切线法证明不等式是从“形”的角度入手思考问题, 将所证的不等式转化为相应曲线与直线、曲线与曲线的位置关系问题, 利用切线实现分而治之的策略.
① 曲直模型：利用切线型不等式进行放缩，证明函数  $f(x)$  的图像总在切线  $y = ax + b$  的上方或下方.  
②曲曲模型：利用公切线隔离法，证明两个函数图像分别在它们切线的上方或下方，适用于凹函数与凸函数且它们的凹凸性相反的问题（拆成两个函数）.
当两函数有斜率相同的切线, 这是切线放缩的本质. 引入一个中间量, 分别证明两个不等式成立, 然后利用不等式的传递性就可以了. 这个方法的难点在于合理拆分函数, 寻找它们斜率相等的切线隔板.
##### 例5.10 设函数  $f(x) = \mathrm{e}^{mx} - \ln x - 2$ . 证明: 当  $x > 0, m > \mathrm{e}^{-\frac{1}{2}}$  时,  $f(x) > -\frac{1}{2}$ .
本题思路较多，可根据参数的范围进行放缩消掉参数，然后利用指数函数或对数函数放缩为其切线来证明；也可利用一些常用不等式的结论来证明，或通过设隐零点的方法得证.

<span class="fake-tag">解析</span> 证法一（指数切线放缩）：
$f(x) = \mathrm{e}^{mx} - \ln x - 2\geqslant \mathrm{em}x - \ln x - 2 > \mathrm{e}^{\frac{1}{2}}x - \ln x - 2 = \mathrm{e}^{\frac{1}{2} +\ln x} - \ln x - 2\geqslant \frac{1}{2} +\ln x + 1 - \ln x -$ $2 = -\frac{1}{2}$  ，所以  $f(x) > - \frac{1}{2}$
证法二（对数切线放缩）：  $f(x) = \mathrm{e}^{mx} - \ln x - 2\geqslant \mathrm{em}x - \ln x - 2 > \mathrm{e}^{\frac{1}{2}}x - \ln x - 2.$
又  $\ln x\leqslant x - 1$  ，则  $\ln \sqrt{\mathrm{e}} x\leqslant \sqrt{\mathrm{e}} x - 1$  ，即  $\frac{1}{2} +\ln x\leqslant \sqrt{\mathrm{e}} x - 1$  ，亦即  $\ln x\leqslant \sqrt{\mathrm{e}} x - \frac{3}{2}$
所以  $f(x) > \mathrm{e}^{\frac{1}{2}}x - \ln x - 2 \geqslant \mathrm{e}^{\frac{1}{2}}x - \sqrt{\mathrm{e}} x + \frac{3}{2} - 2 = -\frac{1}{2}$ .
证法三（常用不等式的放缩）：利用例5.3所证明的不等式，即  $\mathrm{e}^x -\ln x > 2$
所以  $\mathrm{e}^{mx} - \ln x - 2 > \ln (mx) + 2 - \ln x - 2 = \ln m > -\frac{1}{2}$ .
证法四（合而歼之，隐零点）：  $f^{\prime}(x) = m\mathrm{e}^{mx} - \frac{1}{x} = \frac{mx\mathrm{e}^{mx} - 1}{x}.$
令  $f^{\prime}(x_0) = 0$  得  $mx_0\mathrm{e}^{mx_0} = 1$ ，且  $f(x)$  在  $(0,x_0)$  上单调递减，在  $(x_0, + \infty)$  上单调递增，因此  $f(x)_{\min} = f(x_0) = \mathrm{e}^{mx_0} - \ln x_0 - 2.$
又  $\mathrm{e}^{mx_0} = \frac{1}{mx_0}, \ln (mx_0) + mx_0 = 0$ ，即  $\ln x_0 + \ln m + mx_0 = 0$ ，所以  $f(x_0) = \frac{1}{mx_0} + \ln m + mx_0 - 2 \geqslant 2\sqrt{mx_0 \cdot \frac{1}{mx_0}} - 2 + \ln m = \ln m > -\frac{1}{2}$ .
##### 变式 1 已知函数  $f(x) = \mathrm{e}^{2x - 1}\left(\mathrm{eln}2x + \frac{1}{x}\right)$ ，证明： $f(x) > 1$
分析  $\gg$  函数  $f(x)$  中有  $\mathrm{e}^{2x - 1}$ ，如果求导，只会更加复杂；函数中既有指数函数，又有对数函数，可以考虑使用经典不等式向幂函数的方向放缩，根据结论中不等号的方向可以考虑经典不等式中的  $\ln x \geqslant -\frac{1}{\mathrm{e}x}$ ，代入化简即可证明。

<span class="fake-tag">解析</span>  $f(x)$  的定义域为  $(0, +\infty)$ . 由经典不等式  $\ln x \geqslant \frac{1}{-\mathrm{e}x}$  和  $\mathrm{e}^{x - 1} \geqslant x$  可得  $\ln 2x \geqslant \frac{1}{-2\mathrm{e}x}, \mathrm{e}^{2x - 1} \geqslant 2x$ , 所以有  $f(x) = \mathrm{e}^{2x - 1}\left(\mathrm{e}\ln 2x + \frac{1}{x}\right) = \mathrm{e}^{2x}\ln 2x + \frac{\mathrm{e}^{2x - 1}}{x} \geqslant \mathrm{e}^{2x}\frac{1}{-2\mathrm{e}x} + \frac{\mathrm{e}^{2x - 1}}{x} = \frac{\mathrm{e}^{2x - 1}}{2x} \geqslant 1$ , 等号不同时取得, 即证  $f(x) > 1$ .
### 译注
高考命题人为了掩盖经典不等式的痕迹, 往往会作一系列的变形, 比如本题中, 用  $2x$  来替换  $x$ , 从而隐藏真实的结构, 来考查同学们的解题能力. 那么越是遇到此类形式复杂的问题, 其实思路越是清晰, 只要把相关的经典不等式及引申, 一一尝试, 很快就能发现哪条是正确的道路. 比如本题, 我们需要的是  $\ln 2x \geqslant \text{?}$ , 也就是得将  $\ln 2x$  缩小, 那么只有  $\ln x \geqslant 1 - \frac{1}{x}$  和  $\ln x \geqslant -\frac{1}{\mathrm{ex}}$  这两种, 分别尝试, 发现后者为我们所需, 难题就迎刃而解了.