# 形如 $y = A \sin(\omega x + \varphi)$ 的函数图象互相转化的新方法

湖北省十堰市丹江口市六里坪镇实验学校 段昌华

# 1 教材习题解法

人教 A 版普通高中教科书《数学》必修第一册第 254 页第 8 题：

画出下列函数在长度为一个周期的闭区间上的简图,并指出分别由函数 $y=\sin x, x\in R$ 的图象经过怎样的变换得到:

(1) $y=\frac{1}{2}\sin\left(3x-\frac{\pi}{3}\right),\cdots\cdots$

根据教科书中把 $y=\sin x$ 的图象变换成为 $y=A\sin(\omega x+\varphi)$ 图象的方法来做本题的第(1)小题: 先把 $y=\sin x$ 的图象向右平移 $\frac{\pi}{3}$ 个单位长度, 得到 $y=\sin\left(x-\frac{\pi}{3}\right)$ 的图象; 再把 $y=\sin\left(x-\frac{\pi}{3}\right)$ 图象上每一点横坐标变为原来的 $\frac{1}{3}$ 倍, 得到 $y=\sin\left(3x-\frac{\pi}{3}\right)$ 的图象; 最后再把图象上每一点的纵坐标变为原来的 $\frac{1}{2}$ 倍, 就得到 $y=\frac{1}{2}\sin\left(3x-\frac{\pi}{3}\right)$ 的图象.

这种方法需要学生记住将 $y = \sin x$ 的图象变换成 $y = \sin(\omega x + \varphi)$ 图象的口诀，若不理解口诀的实质，则不容易记住，并且容易混淆.

# 2 一种不需要记忆的新方法

下面介绍一种函数 $y = \sin x, x \in \mathbf{R}$ 的图象经过变换得到 $y = \frac{1}{2}\sin \left(3x - \frac{\pi}{3}\right)$ 图象的方法：

把函数 $y = \frac{1}{2}\sin \left(3x - \frac{\pi}{3}\right)$ 的 $x, y$ 依次换成 $X$ ， $Y$ ，则有 $Y = \frac{1}{2}\sin \left(3X - \frac{\pi}{3}\right)$ ，则 $y = \frac{1}{2}\sin \left(3x - \frac{\pi}{3}\right)$ 和 $Y = \frac{1}{2}\sin \left(3X - \frac{\pi}{3}\right)$ 是同一个函数.

对于 $y=\sin x$ 和 $Y=\frac{1}{2}\sin\left(3X-\frac{\pi}{3}\right)$ ，有方程组

$$
\left\{ \begin{array}{l} \sin x = \sin \left(3 X - \frac {\pi}{3}\right), \\ x = 3 X - \frac {\pi}{3}, \\ y = \sin x, \\ Y = \frac {1}{2} \sin \left(3 X - \frac {\pi}{3}\right), \end{array} \text {解得} \right.
$$

$$
\left\{ \begin{array}{l l} \frac {x + \frac {\pi}{3}}{3} = X, & ① \\ \frac {1}{2} y = Y. & ② \end{array} \right.
$$

由①②知, 把 $y = \sin x$ 图象上每一点向右平移 $\frac{\pi}{3}$ 个单位长度, 再把每一点的横坐标变为原来的 $\frac{1}{3}$ 倍, 最后把每一点的纵坐标变为原来的 $\frac{1}{2}$ 倍, 就得到了 $Y = \frac{1}{2} \sin \left(3X - \frac{\pi}{3}\right)$ 的图象.

根据上面的方法, 函数 $y=\frac{1}{2}\sin\left(3x-\frac{\pi}{3}\right)$ 的图象经过怎样的变换能够得到 $y=\sin x, x \in R$ 的图象?

解: $y=\frac{1}{2}\sin\left(3x-\frac{\pi}{3}\right)$ 和 $Y=\frac{1}{2}\sin\left(3X-\frac{\pi}{3}\right)$ 是同一个函数.

对于 $y=\sin x$ 和 $Y=\frac{1}{2}\sin\left(3X-\frac{\pi}{3}\right)$ ，有方程组 $\left\{\begin{aligned}&\sin x=\sin\left(3X-\frac{\pi}{3}\right),\\&x=3X-\frac{\pi}{3},\\&y=\sin x,\end{aligned}\right.$ 解得 $Y=\frac{1}{2}\sin\left(3X-\frac{\pi}{3}\right)$ ,

$$
\left\{ \begin{array}{l l} 3 X - \frac {\pi}{3} = x, & \\ 2 Y = y. & \end{array} \right. \tag {③}
$$

由③④两式得，先把 $Y = \frac{1}{2}\sin \left(3X - \frac{\pi}{3}\right)$ 这个函数图象上每一点的横坐标扩大到原来的3倍，再把图

象上每一点的横坐标向左平移 $\frac{\pi}{3}$ 个单位长度，同时每一点的纵坐标变为原来的2倍，就可得到 $y = \sin x$ 这个函数的图象.

# 3 方法总结

# 3.1 $y = \sin x$ 和 $y = A\sin (\omega x + \varphi)$ 图象间的转化

把 $y=A\sin(\omega x+\varphi)$ 中的 x,y 依次换成 X,Y, 则有 $Y=A\sin(\omega X+\varphi)$ .

对于 $Y = A \sin(\omega X + \varphi)$ 和 $y = \sin x$ ，有方程组 $\left\{\begin{aligned}\sin(\omega X+\varphi)=\sin x,\\ \omega X+\varphi=x,\\ Y=A\sin(\omega X+\varphi),\\ y=\sin x,\end{aligned}\right.$ 解得

$$
\left\{ \begin{array}{l l} \omega X + \varphi = x, & ⑤ \\ \frac {Y}{A} = y, & ⑥ \\ \frac {x - \varphi}{\omega} = X, & ⑦ \\ A y = Y. & ⑧ \end{array} \right.
$$

由⑤⑥知，把 $Y = A\sin (\omega X + \varphi)$ 图象上每一点的横坐标扩大到原来的 $\omega$ 倍，再把图象上每一点向左（或右）平移 $|\varphi|$ 个单位长度，最后把每一点的纵坐标变为原来的 $\frac{1}{A}$ 倍，就得到 $y = \sin x$ 的图象.由⑦⑧知，把 $y = \sin x$ 图象上每一点向左(或右)平移 $|\varphi|$ 个单位长度，再把每一点的横坐标变为原来的 $\frac{1}{\omega}$ 倍，最后把每一点的纵坐标变为原来的 $A$ 倍，就可以得到 $Y = A\sin (\omega X + \varphi)$ 的图象.

# 3.2 $y = A_{1}\sin (\omega_{1}x + \varphi_{1})$ 和 $y = A_{2}\sin (\omega_{2}x + \varphi_{2})$ 图象间的转化

探求 $y=A_{1}\sin(\omega_{1}x+\varphi_{1})$ 和 $y=A_{2}\sin(\omega_{2}x+\varphi_{2})$ （其中 $\omega_{1}>0,\omega_{2}>0,A_{1}>0,A_{2}>0,A_{1},A_{2},\omega_{1},\omega_{2},\varphi_{1},\varphi_{2}$ 都是常数）图象之间相互转化的方法：

把 $y=A_{1}\sin(\omega_{1}x+\varphi_{1})$ 中的 x,y 依次换成 X,Y，则有 $Y=A_{1}\sin(\omega_{1}X+\varphi_{1})$ .

对于 $Y=A_{1}\sin(\omega_{1}X+\varphi_{1})$ 和 $y=A_{2}\sin(\omega_{2}x+\varphi_{2})$ ，有方程组.

$$
\left\{ \begin{array}{l l} \sin (\omega_ {1} X + \varphi_ {1}) = \sin (\omega_ {2} x + \varphi_ {2}), \\ \omega_ {1} X + \varphi_ {1} = \omega_ {2} x + \varphi_ {2}, \\ Y = A _ {1} \sin (\omega_ {1} X + \varphi_ {1}), \\ y = A _ {2} \sin (\omega_ {2} x + \varphi_ {2}), \end{array} \right. \text {解得}
$$

$$
\left\{ \begin{array}{l l} \frac {\omega_ {1} X + \varphi_ {1} - \varphi_ {2}}{\omega_ {2}} = x, & ⑨ \\ Y \cdot \frac {A _ {2}}{A _ {1}} = y, & ⑩ \\ \frac {\omega_ {2} x + \varphi_ {2} - \varphi_ {1}}{\omega_ {1}} = X, & ⑪ \\ y \cdot \frac {A _ {1}}{A _ {2}} = Y. & ⑫ \end{array} \right.
$$

由⑨可知，把 $Y = A_{1}\sin (\omega_{1}X + \varphi_{1})$ 图象上每一点的横坐标经过 $\frac{\omega_1X + \varphi_1 - \varphi_2}{\omega_2}$ 的变换，即先把 $Y = A_{1}\sin (\omega_{1}X + \varphi_{1})$ 图象上每一点的横坐标变为原来的 $\omega_{1}$ 倍，再把图象上每一点向左(或右)平移 $|\varphi_1 - \varphi_2|$ 个单位长度，然后再把每点横坐标变为原来的 $\frac{1}{\omega_2}$ 倍；同时由⑩知把图象上每点纵坐标变为原来的 $\frac{A_2}{A_1}$ 倍，可以得到 $y = A_{2}\sin (\omega_{2}x + \varphi_{2})$ 的图象.同理，由⑪和⑫可以得到把 $y = A_{2}\sin (\omega_{2}x + \varphi_{2})$ 图象变换成为 $Y = A_{1}\sin (\omega_{1}X + \varphi_{1})$ 图象的方法.

# 4 应用举例

例题 函数 $y=\frac{2}{3}\sin\left(3x+\frac{\pi}{8}\right)$ 的图象经过怎样的变换可以得到函数 $y=5\sin\left(6x-\frac{\pi}{3}\right)$ 的图象？

解: $y=5\sin\left(6x-\frac{\pi}{3}\right)$ 和 $Y=5\sin\left(6X-\frac{\pi}{3}\right)$ 是同一个函数.

对于 $y=\frac{2}{3}\sin\left(3x+\frac{\pi}{8}\right)$ 和 $Y=5\sin\left(6X-\frac{\pi}{3}\right)$ ,

$$
\text {有方程组} \left\{ \begin{array}{l l} \sin \left(3 x + \frac {\pi}{8}\right) = \sin \left(6 X - \frac {\pi}{3}\right), \\ 3 x + \frac {\pi}{8} = 6 X - \frac {\pi}{3}, \\ y = \frac {2}{3} \sin \left(3 x + \frac {\pi}{8}\right), \\ Y = 5 \sin \left(6 X - \frac {\pi}{3}\right), \end{array} \right. \quad \text {解得}
$$

$$
\left\{ \begin{array}{l} \frac {3 x + \frac {\pi}{8} + \frac {\pi}{3}}{6} = X, \\ \frac {3}{2} \times 5 y = Y. \end{array} \right. \tag {③}
$$

由⑬可知，把 $y = \frac{2}{3}\sin \left(3x + \frac{\pi}{8}\right)$ 的图象上每一点的横坐标变为原来的3倍，再把图象上每一点向右平移 $\left(\frac{\pi}{8} +\frac{\pi}{3}\right)$ 个单位长度，然后把每一点的横坐标变为原来的 $\frac{1}{6}$ 倍，最后由⑭可知，把每一点的纵坐标扩大到原来的 $\left(\frac{3}{2}\times 5\right)$ 倍，就能得到 $Y = 5\sin \left(6X - \frac{\pi}{3}\right)$ 的图象.Z