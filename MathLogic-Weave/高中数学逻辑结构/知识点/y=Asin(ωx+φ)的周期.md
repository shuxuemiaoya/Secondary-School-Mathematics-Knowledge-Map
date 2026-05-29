## 探究与发现
函数  $y = A\sin (\omega x + \varphi)$  及函数  $y = A\cos (\omega x + \varphi)$  的周期
从前面的例子中可以看出,函数
$y = A\sin (\omega x + \varphi),x\in \mathbf{R}$
及函数
$y = A\cos (\omega x + \varphi),x\in \mathbf{R}$
(其中  $A$ ,  $\omega$ ,  $\varphi$  为常数,且  $A\neq 0$ ,  $\omega >0$ ) 的周期仅与自变量的系数有关. 那么,如何用自变量的系数表示上述函数的周期呢?
事实上,令  $z = \omega x + \varphi$ ,那么由  $x\in \mathbf{R}$  得  $z\in \mathbf{R}$ ,且函数  $y = A\sin z$ ,  $z\in \mathbf{R}$  及函数  $y = A\cos z$ ,  $z\in \mathbf{R}$  的周期都是  $2\pi$ .
因为
$z + 2\pi = (\omega x + \varphi) + 2\pi = \omega \left(x + \frac{2\pi}{\omega}\right) + \varphi ,$
所以,自变量  $x$  增加  $\frac{2\pi}{\omega}$ ,函数值就重复出现;并且增加量小于  $\frac{2\pi}{\omega}$  时,函数值不会重复出现. 即
$T = \frac{2\pi}{\omega}$
是使等式
$\begin{array}{r}{A\sin [\omega (x + T) + \varphi ] = A\sin (\omega x + \varphi),}\\ {A\cos [\omega (x + T) + \varphi ] = A\cos (\omega x + \varphi)} \end{array}$
成立的最小正数,从而,函数
$y = A\sin (\omega x + \varphi), x \in \mathbf{R}$
及函数
$y = A\cos (\omega x + \varphi), x \in \mathbf{R}$
的周期  $T = \frac{2\pi}{\omega}$ .
根据这个结论,我们可以由这类函数的解析式直接写出函数的周期.

想一想:上述求函数  $y = A\sin (\omega x + \varphi)$ ,  $x \in \mathbf{R}$  及函数  $y = A\cos (\omega x + \varphi)$ ,  $x \in \mathbf{R}$  周期的方法是否能推广到求一般周期函数的周期?即命题"如果函数  $y = f(x)$  的周期是  $T$ ,那么函数  $y = f(\omega x)$  ( $\omega > 0$ ) 的周期是  $\frac{T}{\omega}$  是否成立?