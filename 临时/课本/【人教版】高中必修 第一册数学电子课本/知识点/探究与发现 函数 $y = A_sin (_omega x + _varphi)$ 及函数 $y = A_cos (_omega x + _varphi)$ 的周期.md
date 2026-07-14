### 探究与发现 函数 $y = A\sin (\omega x + \varphi)$ 及函数 $y = A\cos (\omega x + \varphi)$ 的周期

函数 $y = A\sin (\omega x + \varphi)$ 及函数 $y = A\cos (\omega x + \varphi)$ 的周期

从前面的例子中可以看出，函数
$y = A \sin (\omega x + \varphi), x \in \mathbf {R}$

及函数
$y = A \cos (\omega x + \varphi), x \in \mathbf {R}$

（其中 $A, \omega, \varphi$ 为常数，且 $A \neq 0, \omega > 0$ ）的周期仅与自变量的系数有关。那么，如何用自变量的系数表示上述函数的周期呢？

事实上，令 $z = \omega x + \varphi$ ，那么由 $x\in \mathbf{R}$ 得 $z\in \mathbf{R}$ ，且函数 $y = A\sin z$ ， $z\in \mathbf{R}$ 及函数 $y = A\cos z$ ， $z\in \mathbf{R}$ 的周期都是 $2\pi$
因为
$z + 2 \pi = (\omega x + \varphi) + 2 \pi = \omega \left(x + \frac {2 \pi}{\omega}\right) + \varphi ,$
所以，对于任意 $x$ ，当自变量 $x$ 增加 $\frac{2\pi}{\omega}$ 时，函数值就重复出现；并且当增加量小于 $\frac{2\pi}{\omega}$ 时，函数值不会总重复出现。即
$T = \frac {2 \pi}{\omega}$

是使等式
$A \sin [ \omega (x + T) + \varphi ] = A \sin (\omega x + \varphi),$
$A \cos [ \omega (x + T) + \varphi ] = A \cos (\omega x + \varphi)$

成立的最小正数. 从而, 函数
$y = A \sin (\omega x + \varphi), x \in \mathbf {R}$

及函数
$y = A \cos (\omega x + \varphi), x \in \mathbf {R}$

的周期 $T = \frac{2\pi}{\omega}$

根据这个结论，我们可以由这类函数的解析式直接写出函数的周期.

想一想：上述求函数 $y = A\sin (\omega x + \varphi)$ ， $x \in \mathbf{R}$ 及函数 $y = A\cos (\omega x + \varphi)$ ， $x \in \mathbf{R}$ 周期的方法是否能推广到求一般周期函数的周期？即命题“如果函数 $y = f(x)$ 的周期是 $T$ ，那么函数 $y = f(\omega x) (\omega > 0)$ 的周期是 $\frac{T}{\omega}$ ”是否成立？

#### 3. 单调性

根据正弦函数的周期性，我们可以先在它的一个周期的区间（如 $\left[-\frac{\pi}{2}, \frac{3\pi}{2}\right]$ ）上讨论它的单调性，再利用它的周期性，将单调性扩展到整个定义域.

观察图 5.4-8，可以看到：
当 $x$ 由 $-\frac{\pi}{2}$ 增大到 $\frac{\pi}{2}$ 时，曲线逐渐上升， $\sin x$ 的值由-1增大到1；当 $x$ 由 $\frac{\pi}{2}$ 增大到 $\frac{3\pi}{2}$ 时，曲线逐渐下降， $\sin x$ 的值由1减小到-1.
$\sin x$ 的值的变化情况如表5.4-2所示：

根据三角函数的周期性，只要把握了它一个周期内的规律，就把握了整个三角函数的规律.

![](课本/【人教版】高中必修%20第一册数学电子课本/知识点/images/21caae7d707db024ab694ef5162717060e90b3929a02682238438791e127d89a.jpg)

图5.4-8

表5.4-2

<table><tr><td>x</td><td>-π/2</td><td>↗</td><td>0</td><td>↗</td><td>π/2</td><td>↗</td><td>π</td><td>↗</td><td>3π/2</td></tr><tr><td>sin x</td><td>-1</td><td>↗</td><td>0</td><td>↗</td><td>1</td><td>↘</td><td>0</td><td>↘</td><td>-1</td></tr></table>
这就是说，

正弦函数 $y = \sin x$ 在区间 $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ 上单调递增，在区间 $\left[\frac{\pi}{2}, \frac{3\pi}{2}\right]$ 上单调递减.
由正弦函数的周期性可得，

正弦函数在每一个闭区间 $\left[-\frac{\pi}{2} + 2k\pi, \frac{\pi}{2} + 2k\pi\right](k \in \mathbf{Z})$ 上都单调递增，其值从-1增大到1；在每一个闭区间 $\left[\frac{\pi}{2} + 2k\pi, \frac{3\pi}{2} + 2k\pi\right](k \in \mathbf{Z})$ 上都单调递减，其值从1减小到-1.

类似地，观察余弦函数在一个周期区间（如 $[- \pi, \pi]$ ）上函数值的变化规律，将看到的函数值的变化情况填入表5.4-3：

表5.4-3

<table><tr><td>x</td><td> $-\pi$ </td><td> $\nearrow$ </td><td> $-\frac{\pi}{2}$ </td><td> $\nearrow$ </td><td>0</td><td> $\nearrow$ </td><td> $\frac{\pi}{2}$ </td><td> $\nearrow$ </td><td> $\pi$ </td></tr><tr><td> $\cos x$ </td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>
由此可得，

函数 $y=\cos x,\quad x\in[-\pi,\quad\pi]$ 在区间 \_\_\_\_ 上单调递增，其值从 -1 增大到 1；在区间 \_\_\_\_ 上单调递减，其值从 1 减小到 -1.
由余弦函数的周期性可得，

余弦函数在每一个闭区间 \_\_\_\_ 上都单调递增，其值从 -1 增大到 1；在每一个闭区间 \_\_\_\_ 上都单调递减，其值从 1 减小到 -1.

#### 4. 最大值与最小值

从上述对正弦函数、余弦函数的单调性的讨论中容易得到，

正弦函数当且仅当 $x =$ \_\_\_\_时取得最大值1，当且仅当 $x =$ \_\_\_\_时取得最小值-1；
余弦函数当且仅当 $x =$ \_\_\_\_时取得最大值1，当且仅当 $x =$ \_\_\_\_时取得最小值-1.

> [!example]- 例 3 下列函数有最大值、最小值吗？如果有，请写出取最大值、最小值时自变量 x 的集合，并求出最大值、最小值.  
（1） $y=\cos x+1,\quad x\in R;$   
（2） $y = -3\sin 2x, x \in \mathbf{R}.$
解：容易知道，这两个函数都有最大值、最小值.  
（1）使函数 $y = \cos x + 1$ ， $x \in \mathbf{R}$ 取得最大值的 $x$ 的集合，就是使函数 $y = \cos x$ ， $x \in \mathbf{R}$ 取得最大值的 $x$ 的集合
$\{x \mid x = 2 k \pi , k \in \mathbf {Z} \};$

使函数 $y=\cos x+1,\quad x\in R$ 取得最小值的 x 的集合，就是使函数 $y=\cos x,\quad x\in R$ 取得最小值的 x 的集合
$\{x \mid x = (2 k + 1) \pi , k \in \mathbf {Z} \}.$

函数 $y=\cos x+1,\quad x\in R$ 的最大值是 $1+1=2$ ；最小值是 $-1+1=0$ .  
（2）令 $z = 2x$ ，使函数 $y = -3\sin z$ ， $z \in \mathbf{R}$ 取得最大值的 $z$ 的集合，就是使 $y = \sin z$ ， $z \in \mathbf{R}$ 取得最小值的 $z$ 的集合
$\{z \mid z = - \frac {\pi}{2} + 2 k \pi , k \in \mathbf {Z} \}.$
由 $2x = z = -\frac{\pi}{2} + 2k\pi$ ，得 $x = -\frac{\pi}{4} + k\pi$ 。所以，使函数 $y = -3\sin 2x$ ， $x \in \mathbf{R}$ 取得最大值的 $x$ 的集合是
$\{x \mid x = - \frac {\pi}{4} + k \pi , k \in \mathbf {Z} \}.$
同理，使函数 $y = -3\sin 2x$ ， $x \in \mathbf{R}$ 取得最小值的 $x$ 的集合是
$\{x \mid x = \frac {\pi}{4} + k \pi , k \in \mathbf {Z} \}.$

函数 $y = -3 \sin 2x$ ， $x \in R$ 的最大值是 3，最小值是 -3.

> [!example]- 例4 不通过求值，比较下列各组数的大小：  
（1） $\sin \left(-\frac{\pi}{18}\right)$ 与 $\sin \left(-\frac{\pi}{10}\right)$ ;  
（2） $\cos \left(-\frac{23\pi}{5}\right)$ 与 $\cos \left(-\frac{17\pi}{4}\right)$ .
分析：可利用三角函数的单调性比较两个同名三角函数值的大小．为此，先用诱导公式将已知角化为同一单调区间内的角，然后再比较大小.
解：（1）因为
$- \frac {\pi}{2} <   - \frac {\pi}{1 0} <   - \frac {\pi}{1 8} <   0,$

正弦函数 $y = \sin x$ 在区间 $\left[-\frac{\pi}{2}, 0\right]$ 上单调递增，所以
$\sin \left(- \frac {\pi}{1 8}\right) > \sin \left(- \frac {\pi}{1 0}\right).$  
（2） $\cos \left(-\frac{23\pi}{5}\right) = \cos \frac{23\pi}{5} = \cos \frac{3\pi}{5},$
$\cos \left(- \frac {1 7 \pi}{4}\right) = \cos \frac {1 7 \pi}{4} = \cos \frac {\pi}{4}.$
因为 $0 < \frac{\pi}{4} < \frac{3\pi}{5} < \pi$ ，且函数 $y = \cos x$ 在区间 $[0, \pi]$ 上单调递减，所以
$\cos \frac {\pi}{4} > \cos \frac {3 \pi}{5},$
即
$\cos \left(- \frac {1 7 \pi}{4}\right) > \cos \left(- \frac {2 3 \pi}{5}\right).$

你能借助单位圆直观地比较上述两对函数值的大小吗？试一试.

> [!example]- 例 5 求函数 $y=\sin\left(\frac{1}{2}x+\frac{\pi}{3}\right)$ ， $x\in[-2\pi,2\pi]$ 的单调递增区间.
分析：令 $z = \frac{1}{2} x + \frac{\pi}{3}$ ， $x \in [-2\pi, 2\pi]$ ，当自变量 $x$ 的值增大时， $z$ 的值也随之增大，因此若函数 $y = \sin z$ 在某个区间上单调递增，则函数 $y = \sin \left(\frac{1}{2} x + \frac{\pi}{3}\right)$ 在相应的区间上也一定单调递增.
解：令 $z = \frac{1}{2} x + \frac{\pi}{3}, x \in [-2\pi, 2\pi]$ ，则 $z \in \left[-\frac{2}{3}\pi, \frac{4}{3}\pi\right]$ .
因为 $y = \sin z, z \in \left[-\frac{2\pi}{3}, \frac{4\pi}{3}\right]$ 的单调递增区间是 $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ ，且由
$- \frac {\pi}{2} \leqslant \frac {1}{2} x + \frac {\pi}{3} \leqslant \frac {\pi}{2},$
得 $-\frac{5\pi}{3} \leqslant x \leqslant \frac{\pi}{3}$ .
所以，函数 $y = \sin \left(\frac{1}{2} x + \frac{\pi}{3}\right), x \in [-2\pi, 2\pi]$ 的单调递增区间是 $\left[-\frac{5\pi}{3}, \frac{\pi}{3}\right]$ .

> [!think] 思考
你能求出函数 $y = \sin \left(-\frac{1}{2} x + \frac{\pi}{3}\right)$ ， $x \in [-2\pi, 2\pi]$ 的单调递增区间吗？

#### 练习

1. 观察正弦曲线和余弦曲线，写出满足下列条件的 $x$ 所在的区间：  
（1） $\sin x > 0$ ;  
（2） $\sin x < 0$ ;  
（3） $\cos x > 0$ ;  
（4） $\cos x < 0$ .

2. 求使下列函数取得最大值、最小值的自变量的集合，并求出最大值、最小值.  
（1） $y = 2\sin x, x \in \mathbf{R};$  
（2） $y = 2 - \cos \frac{x}{3}, x \in \mathbf{R}.$

3. 下列关于函数 $y = 4\sin x$ ， $x \in [0, 2\pi]$ 的单调性的叙述，正确的是（）.

(A) 在 $[0, \pi]$ 上单调递增，在 $[\pi, 2\pi]$ 上单调递减  
(B) 在 $\left[0, \frac{\pi}{2}\right]$ 上单调递增，在 $\left[\frac{3\pi}{2}, 2\pi\right]$ 上单调递减  
(C) 在 $\left[0, \frac{\pi}{2}\right]$ 及 $\left[\frac{3\pi}{2}, 2\pi\right]$ 上单调递增，在 $\left[\frac{\pi}{2}, \frac{3\pi}{2}\right]$ 上单调递减  
(D) 在 $\left[\frac{\pi}{2}, \frac{3\pi}{2}\right]$ 上单调递增，在 $\left[0, \frac{\pi}{2}\right]$ 及 $\left[\frac{3\pi}{2}, 2\pi\right]$ 上单调递减

4. 不通过求值，比较下列各组中两个三角函数值的大小：  
（1） $\cos \frac{2}{7}\pi$ 与 $\cos \left(-\frac{3\pi}{5}\right)$ ;  
（2） $\sin 250^{\circ}$ 与 $\sin 260^{\circ}$ .

5. 求函数 $y = 3\sin \left(2x + \frac{\pi}{4}\right)$ ， $x \in [0, \pi]$ 的单调递减区间.

![](课本/【人教版】高中必修%20第一册数学电子课本/知识点/images/dbfa7678e4320cc27cebb6b4d1890fae68bbaa36bea576b84749aa751110feee.jpg)

##### 探究与发现

