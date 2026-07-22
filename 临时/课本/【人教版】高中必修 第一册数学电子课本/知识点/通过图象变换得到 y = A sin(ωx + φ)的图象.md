


> [!question] 思考
你能总结一下从正弦函数图象出发，通过图象变换得到 $y = A\sin (\omega x + \varphi)$ （ $A > 0, \omega > 0$ ）图象的过程与方法吗？

一般地，
>[!summary] 函数 $y = A\sin (\omega x + \varphi)(A > 0, \omega > 0)$ 的图象，可以用下面的方法得到：
>先画出函数 $y = \sin x$ 的图象；
>再把正弦曲线向左（或右）平移 $|\varphi|$ 个单位长度，得到函数 $y = \sin (x + \varphi)$ 的图象；
>然后把曲线上各点的横坐标变为原来的 $\frac{1}{\omega}$ 倍（纵坐标不变），得到函数 $y = \sin (\omega x + \varphi)$ 的图象；
>最后把曲线上各点的纵坐标变为原来的 $A$ 倍（横坐标不变），这时的曲线就是函数 $y = A\sin (\omega x + \varphi)$ 的图象.

这一过程的步骤如下：


<div align="center">
  <img src="/课本/【人教版】高中必修%20第一册数学电子课本/知识点/images/bff46328cef7496ddeb2f05da51d14c47847404b31183c663a3880067715cc3d.jpg" width="55%" />
</div>

补全步骤2和3的函数及图象.

![](课本/【人教版】高中必修%20第一册数学电子课本/知识点/images/Gemini_Generated_Image_dcpwmbdcpwmbdcpw.png)

从上述步骤可以清楚地看到，参数 $A$ ， $\omega$ ， $\varphi$ 是如何对函数图象产生影响的.

> [!example]- 例1 画出函数 $y = 2\sin \left(3x - \frac{\pi}{6}\right)$ 的简图.
>
> > [!success]- 解：
> > 先画出函数 $y = \sin x$ 的图象；再把正弦曲线向右平移 $\frac{\pi}{6}$ 个单位长度，得到函数 $y = \sin \left(x - \frac{\pi}{6}\right)$ 的图象；然后使曲线上各点的横坐标变为原来的 $\frac{1}{3}$ ，得到函数 $y = \sin \left(3x - \frac{\pi}{6}\right)$ 的图象；最后把曲线上各点的纵坐标变为原来的2倍，这时的曲线就是函数 $y = 2\sin \left(3x - \frac{\pi}{6}\right)$ 的图象，如图5.6-7所示.
> >
> > <div align="center">
> >   <img src="/课本/【人教版】高中必修%20第一册数学电子课本/知识点/images/c6c8d29a6d0720eac2df1705f28602adf08173feabb6dee4ab48e54192f324cc.jpg" width="55%" />
> >   <br />
> >   图5.6-7
> > </div>
> >
> > 下面用 “五点法” 画函数 $y=2\sin\left(3x-\frac{\pi}{6}\right)$ 在一个周期 $\left(T=\frac{2\pi}{3}\right)$ 内的图象.
> >
> > 令 $X = 3x - \frac{\pi}{6}$ ，则 $x = \frac{1}{3}\left(X + \frac{\pi}{6}\right)$ 。列表（表5.6-1），描点画图（图5.6-8）。
> >
> > 表5.6-1
> >
> > <table><tr><td>X</td><td>0</td><td> $\frac{\pi}{2}$ </td><td>π</td><td> $\frac{3\pi}{2}$ </td><td>2π</td></tr><tr><td>x</td><td> $\frac{\pi}{18}$ </td><td> $\frac{2\pi}{9}$ </td><td> $\frac{7\pi}{18}$ </td><td> $\frac{5\pi}{9}$ </td><td> $\frac{13\pi}{18}$ </td></tr><tr><td>y</td><td>0</td><td>2</td><td>0</td><td>-2</td><td>0</td></tr></table>
> >
> > <div align="center">
> >   <img src="/课本/【人教版】高中必修%20第一册数学电子课本/知识点/images/ae582031f7fb6bed3fcd7b98eca781922f3a423e87599f594868d6ef06dc8941.jpg" width="55%" />
> >   <br />
> >   图5.6-8
> > </div>

> [!example]- 例 2 摩天轮是一种大型转轮状的机械建筑设施，游客坐在摩天轮的座舱里慢慢地往上转，可以从高处俯瞰四周景色。如图 5.6-9，某摩天轮最高点距离地面高度为 120 m，转盘直径为 110 m，设置有 48 个座舱，开启后按逆时针方向匀速旋转，游客在座舱转到距离地面最近的位置进舱，转一周大约需要 30 min。
>
> <div align="center">
>   <img src="/课本/【人教版】高中必修%20第一册数学电子课本/知识点/images/bb0e703a6803eb000215afaa6475c25a9d3bdb81e55eeceb9ab470790a3ce566.jpg" width="55%" />
>   <br />
>   图5.6-9
> </div>
>
> （1）游客甲坐上摩天轮的座舱，开始转动 $t \min$ 后距离地面的高度为 $H \mathrm{~m}$ ，求在转动一周的过程中， $H$ 关于 $t$ 的函数解析式；
> （2） 求游客甲在开始转动 5 min 后距离地面的高度;
> （3）若甲、乙两人分别坐在两个相邻的座舱里，在运行一周的过程中，求两人距离地面的高度差 h （单位：m）关于 t 的函数解析式，并求高度差的最大值（精确到 0.1）.
>
> > [!tip]- 分析：
> > 摩天轮上的座舱运动可以近似地看作质点在圆周上做匀速旋转。在旋转过程中，游客距离地面的高度 $H$ 呈现周而复始的变化，因此可以考虑用三角函数来刻画。
>
> > [!success]- 解：
> > 如图 5.6-10，设座舱距离地面最近的位置为点 P，以轴心 O 为原点，与地面平行的直线为 x 轴建立直角坐标系.
> > （1）设 $t = 0\mathrm{min}$ 时，游客甲位于点 $P(0, -55)$ ，以 $OP$ 为终边的角为 $-\frac{\pi}{2}$ ；根据摩天轮转一周大约需要 $30\mathrm{min}$ ，可知座舱转动的角速度约为 $\frac{\pi}{15}\mathrm{rad / min}$ ，由题意可得
> >
> > <div align="center">
> >   <img src="/课本/【人教版】高中必修%20第一册数学电子课本/知识点/images/8a77869e70a8841a08939287801581fe2a1090585aa8c33df0d8e17103efd7c5.jpg" width="55%" />
> >   <br />
> >   图5.6-10
> > </div>
> >
> > $H = 5 5 \sin \left(\frac {\pi}{1 5} t - \frac {\pi}{2}\right) + 6 5, 0 \leqslant t \leqslant 3 0.$
> > （2） 当 t=5 时，
> > $H = 5 5 \sin \left(\frac {\pi}{1 5} \times 5 - \frac {\pi}{2}\right) + 6 5 = 3 7. 5.$
> > 所以，游客甲在开始转动 5 min 后距离地面的高度约为 37.5 m.
> > （3）如图5.6-10，设甲、乙两人的位置分别用点 $A$ ， $B$ 表示，则 $\angle AOB = \frac{2\pi}{48} = \frac{\pi}{24}$ 经过 $t\min$ 后甲距离地面的高度为 $H_{1} = 55\sin \left(\frac{\pi}{15} t - \frac{\pi}{2}\right) + 65$ ，点 $B$ 相对于点 $A$ 始终落后 $\frac{\pi}{24}\mathrm{rad}$ ，此时乙距离地面的高度为 $H_{2} = 55\sin \left(\frac{\pi}{15} t - \frac{13\pi}{24}\right) + 65.$ 则甲、乙距离地面的高度差
> > $h = \left| H _ {1} - H _ {2} \right| = 5 5 \left| \sin \left(\frac {\pi}{1 5} t - \frac {\pi}{2}\right) - \sin \left(\frac {\pi}{1 5} t - \frac {1 3 \pi}{2 4}\right) \right| = 5 5 \left| \sin \left(\frac {\pi}{1 5} t - \frac {\pi}{2}\right) + \sin \left(\frac {1 3 \pi}{2 4} - \frac {\pi}{1 5} t\right) \right|,$
> >
> > 利用 $\sin \theta +\sin \varphi = 2\sin \frac{\theta + \varphi}{2}\cos \frac{\theta - \varphi}{2}$ ，可得
> > $h = 1 1 0 \left| \sin \frac {\pi}{4 8} \sin \left(\frac {\pi}{1 5} t - \frac {\pi}{4 8}\right) \right|, 0 \leqslant t \leqslant 3 0.$
> > 当 $\frac{\pi}{15} t - \frac{\pi}{48} = \frac{\pi}{2}\left(\text{或} \frac{3\pi}{2}\right)$ ，即 $t \approx 7.8$ (或22.8)时， $h$ 的最大值为 $110\sin \frac{\pi}{48} \approx 7.2$ .
> > 所以，甲、乙两人距离地面的高度差的最大值约为 7.2 m.

#### 练习

1. 画出下列函数在长度为一个周期的闭区间上的简图，并用信息技术检验：  
（1） $y = \frac{1}{2}\sin x;$  
（2） $y = \sin 3x$ ;  
（3） $y = \sin \left( x - \frac{\pi}{3} \right)$ ;  
（4） $y = 2\sin \left(2x - \frac{\pi}{4}\right).$

2. 已知函数 $y = 3\sin \left(x + \frac{\pi}{5}\right)$ 的图象为 $C$ .  
（1）为了得到函数 $y = 3\sin \left(x - \frac{\pi}{5}\right)$ 的图象，只要把 $C$ 上所有的点（ ）.

(A) 向右平行移动 $\frac{\pi}{5}$ 个单位长度

(B) 向左平行移动 $\frac{\pi}{5}$ 个单位长度

(C) 向右平行移动 $\frac{2\pi}{5}$ 个单位长度

(D) 向左平行移动 $\frac{2\pi}{5}$ 个单位长度  
（2）为了得到函数 $y = 3\sin \left(2x + \frac{\pi}{5}\right)$ 的图象，只要把 $C$ 上所有的点（ ）.

(A) 横坐标伸长到原来的 2 倍, 纵坐标不变

(B) 横坐标缩短到原来的 $\frac{1}{2}$ , 纵坐标不变

(C) 纵坐标伸长到原来的 2 倍，横坐标不变

(D) 纵坐标缩短到原来的 $\frac{1}{2}$ , 横坐标不变  
（3）为了得到函数 $y = 4\sin \left(x + \frac{\pi}{5}\right)$ 的图象，只要把 $C$ 上所有的点（ ）.

(A) 横坐标伸长到原来的 $\frac{4}{3}$ 倍，纵坐标不变

(B) 横坐标缩短到原来的 $\frac{3}{4}$ , 纵坐标不变

(C) 纵坐标伸长到原来的 $\frac{4}{3}$ 倍，横坐标不变

(D) 纵坐标缩短到原来的 $\frac{3}{4}$ , 横坐标不变

3. 函数 $y = \frac{2}{3}\sin \left(\frac{1}{2} x - \frac{\pi}{4}\right)$ 的图象与正弦曲线有什么关系？

4. 函数 $y = \sin \left( x + \frac{\pi}{12} \right)$ ， $x \in \left[0, +\infty \right)$ 的图象与正弦曲线有什么关系？
