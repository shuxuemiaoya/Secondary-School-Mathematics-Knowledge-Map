##### 题型05 函数$\mathbf{y = A} \mathbf{\sin} \mathbf{(} \mathbf{\omega x + \varphi )}$的图象与三角恒等变换
##### 【典例1】（23-24高一下·山东临沂·期中）已知函数$f ( x ) = \sqrt{3} \text{sin} 2 x + 2 \text{co} \text{s}^{2} x + m$在区间$\left\lbrack 0 , \frac{\pi}{2} \right\rbrack$上的最大值为6，
(1)求常数$m$的值；
(2)求$f ( x )$的单调递减区间；
(3)求使$f ( x ) > 5$成立的$x$的取值集合．
<span class="fake-tag">答案</span>(1)$m = 3$
(2)$\left\lbrack k \pi + \frac{\pi}{6} , k \pi + \frac{\text{2} \text{π}}{3} \right\rbrack , k \in \mathbf{Z}$
(3)$\left( k \pi , k \pi + \frac{\pi}{3} \right) , k \in \mathbf{Z}$
<span class="fake-tag">分析</span>（1）由三角恒等变换可得$f ( x ) = 2 \sin \left( 2 x + \frac{\pi}{6} \right) + m + 1$，结合正弦函数的有界性分析求解；
（2）由（1）可知：$f ( x ) = 2 \sin \left( 2 x + \frac{\pi}{6} \right) + 4$，结合正弦函数的单调性分析求解；
（3）分析可得$\sin \left( 2 x + \frac{\pi}{6} \right) > \frac{1}{2}$，结合正弦函数性质分析求解.
<span class="fake-tag">详解</span>（1）由题意可得：$f ( x ) = \sqrt{3} \text{sin} 2 x + 2 \text{co} \text{s}^{2} x + m = \sqrt{3} \text{sin} 2 x + \text{cos} 2 x + m + 1 = 2 \sin \left( 2 x + \frac{\pi}{6} \right) + m + 1$，
因为$x \in \left\lbrack 0 , \frac{\pi}{2} \right\rbrack$，则$2 x + \frac{\pi}{6} \in \left\lbrack \frac{\pi}{6} , \frac{\text{5} \text{π}}{6} \right\rbrack$，
可知当$2 x + \frac{\pi}{6} = \frac{\pi}{2}$，即$x = \frac{\pi}{6}$时，$f ( x )$取到最大值$m + 3$，
即$m + 3 = 6$，解得$m = 3$.
（2）由（1）可知：$f ( x ) = 2 \sin \left( 2 x + \frac{\pi}{6} \right) + 4$，
令$2 k \pi + \frac{\pi}{2} \leq 2 x + \frac{\pi}{6} \leq 2 k \pi + \frac{\text{3} \text{π}}{2} , k \in \mathbf{Z}$，解得$k \pi + \frac{\pi}{6} \leq x \leq k \pi + \frac{\text{2} \text{π}}{3} , k \in \mathbf{Z}$，
所以$f ( x )$的单调递减区间为$\left\lbrack k \pi + \frac{\pi}{6} , k \pi + \frac{\text{2} \text{π}}{3} \right\rbrack , k \in \mathbf{Z}$.
（3）由（1）可知：$f ( x ) = 2 \sin \left( 2 x + \frac{\pi}{6} \right) + 4$，
令$f ( x ) > 5$，可得$\sin \left( 2 x + \frac{\pi}{6} \right) > \frac{1}{2}$，
则$2 k \pi + \frac{\pi}{6} < 2 x + \frac{\pi}{6} < 2 k \pi + \frac{\text{5} \text{π}}{6} , k \in \mathbf{Z}$，解得$k \pi < x < k \pi + \frac{\pi}{3} , k \in \mathbf{Z}$，
所以$f ( x ) > 5$的解集为$\left( k \pi , k \pi + \frac{\pi}{3} \right) , k \in \mathbf{Z}$.
##### 【典例2】（23-24高一下·湖北·期中）已知函数$f ( x ) = \sin ( 2 x + \varphi ) ( 0 < \varphi < \pi )$.
(1)设，若为偶函数，且不等式在$x \in \left\lbrack 0 , \frac{\pi}{2} \right\rbrack$上恒成立，求实数$m$的取值范围；
(2)已知函数的图象过点$\left( \frac{\pi}{6} , 1 \right)$，设$h ( x ) = \cos^{2} x + 2 a \sin x$，若对任意的$x_{1} \in \left\lbrack - \frac{\pi}{2} , \frac{\pi}{2} \right\rbrack$，$x_{2} \in \left\lbrack 0 , \frac{\pi}{2} \right\rbrack$，都有$h \left( x_{1} \right) < f \left( x_{2} \right) + 3$，求实数$a$的取值范围.
<span class="fake-tag">答案</span>(1)
(2)$\left( - \frac{5}{4} , \frac{5}{4} \right)$
<span class="fake-tag">分析</span>（1）首先求得$f ( x ) = \cos 2 x$，进一步结合三角恒等变换得$g ( x ) = \sqrt{3} \sin \left( 2 x + \frac{\pi}{3} \right)$，分析可知原不等式等价于$- m - 2 < g ( x )_{\text{min}}$且$g ( x )_{\text{max}} < 2 - m$（$x \in \left\lbrack 0 , \frac{\pi}{2} \right\rbrack$），故只需求出$g ( x )$在给定区间上的最值即可；
（2）根据已知求得$f ( x ) = \sin \left( 2 x + \frac{\pi}{6} \right)$，原题不等式等价于$h \left( x_{1} \right)_{\text{max}} < f \left( x_{2} \right)_{\text{min}} + 3$，$h \left( x_{1} \right)_{\text{max}} < - \frac{1}{2} + 3 = \frac{5}{2}$（$x_{1} \in \left\lbrack - \frac{\pi}{2} , \frac{\pi}{2} \right\rbrack$，$x_{2} \in \left\lbrack 0 , \frac{\pi}{2} \right\rbrack$），其中$h ( x )$的最值与$a$有关，由此即可求解$a$的范围.
<span class="fake-tag">详解</span>（1）因为$f ( x ) = \sin ( 2 x + \varphi ) ( 0 < \varphi < \text{π} )$为偶函数，所以$\varphi = k \pi + \frac{\pi}{2}$，$k \in \mathbf{Z}$，
$\because 0 < \varphi < \pi$，$\therefore \varphi = \frac{\pi}{2}$，所以$f ( x ) = \cos 2 x$，
所以$g ( x ) = f ( x ) - f \left( x + \frac{\pi}{3} \right) = \cos 2 x - \cos 2 \left( x + \frac{\pi}{3} \right)$= $\cos 2 x - \left( - \frac{1}{2} \cos 2 x - \frac{\sqrt{3}}{2} \sin 2 x \right) = \frac{3}{2} \cos 2 x + \frac{\sqrt{3}}{2} \sin 2 x = \sqrt{3} \sin \left( 2 x + \frac{\pi}{3} \right)$.
又因为在$x \in \left\lbrack 0 , \frac{\pi}{2} \right\rbrack$上恒成立，
即在$x \in \left\lbrack 0 , \frac{\pi}{2} \right\rbrack$上恒成立，
所以在$x \in \left\lbrack 0 , \frac{\pi}{2} \right\rbrack$上恒成立，
所以$- m - 2 < g ( x )_{\text{min}}$且$g ( x )_{\text{max}} < 2 - m$，
因为$x \in \left\lbrack 0 , \frac{\pi}{2} \right\rbrack$，所以$2 x + \frac{\pi}{3} \in \left\lbrack \frac{\pi}{3} , \frac{4 \pi}{3} \right\rbrack$，所以$g ( x ) = \sqrt{3} \sin \left( 2 x + \frac{\pi}{3} \right) \in \left\lbrack - \frac{3}{2} , \sqrt{3} \right\rbrack$，
则$\left\{ \begin{matrix}- m - 2 < - \frac{3}{2} \\ 2 - m > \sqrt{3}\end{matrix} \Rightarrow - \frac{1}{2} < m < 2 - \sqrt{3} \right.$，
所以$m$的取值范围为$\left( - \frac{1}{2} , 2 - \sqrt{3} \right)$；
（2）因为过点$\left( \frac{\pi}{6} , 1 \right)$，所以$1 = \sin \left( \frac{\pi}{3} + \varphi \right) ( 0 < \varphi < \pi )$，$\varphi = \frac{\pi}{6}$，
所以$f ( x ) = \sin \left( 2 x + \frac{\pi}{6} \right)$，
又因为$x_{2} \in \left\lbrack 0 , \frac{\pi}{2} \right\rbrack$，所以$2 x_{2} + \frac{\pi}{6} \in \left\lbrack \frac{\pi}{6} , \frac{7 \pi}{6} \right\rbrack$，
所以$f \left( x_{2} \right) = \sin \left( 2 x_{2} + \frac{\pi}{6} \right) \in \left\lbrack - \frac{1}{2} , 1 \right\rbrack$，
又因为对任意的$x_{1} \in \left\lbrack - \frac{\pi}{2} , \frac{\pi}{2} \right\rbrack$，$x_{2} \in \left\lbrack 0 , \frac{\pi}{2} \right\rbrack$，都有$h \left( x_{1} \right) < f \left( x_{2} \right) + 3$成立，
所以$h \left( x_{1} \right)_{\text{max}} < f \left( x_{2} \right)_{\text{min}} + 3$，$h \left( x_{1} \right)_{\text{max}} < - \frac{1}{2} + 3 = \frac{5}{2}$.
，
因为$x_{1} \in \left\lbrack - \frac{\pi}{2} , \frac{\pi}{2} \right\rbrack$，所以，设，
则令$G ( t ) = a^{2} + 1 - ( t - a )^{2}$，$t \in \lbrack - 1 , 1 \rbrack$，
当$a \geq 1$时，$G ( t )$在$t \in \lbrack - 1 , 1 \rbrack$上单调递增，所以$G {( t ) ( 1 )}_{\max}$，
所以，解得$a < \frac{5}{4}$，所以$1 \leq a < \frac{5}{4}$；
当$a \leq - 1$时，$G ( t )$在$t \in \lbrack - 1 , 1 \rbrack$上单调递减，$G ( t )_{\text{max}} = G ( - 1 ) = - 2 a$，
所以$- 2 a < \frac{5}{2}$，解得$a > - \frac{5}{4}$，此时$- \frac{5}{4} < a \leq - 1$；
当时，$G ( t )$在$\lbrack - 1 , a \rbrack$上单调递增，
在$\lbrack a , 1 \rbrack$上单调递减，$G {( t ) ( a )^{2}}_{\max}$，
所以$a^{2} + 1 < \frac{5}{2}$，解得$- \frac{\sqrt{6}}{2} < a < \frac{\sqrt{6}}{2}$，此时.
综上所述：$- \frac{5}{4} < a < \frac{5}{4}$.
即实数$a$的取值范围为$\left( - \frac{5}{4} , \frac{5}{4} \right)$.
##### 【变式1】（23-24高一下·四川内江·期中）已知函数$f ( x ) = \cos^{2} ( \omega x - \frac{\pi}{6} ) - \sin^{2} \omega x$（$\omega > 0$）的最小正周期为$\pi$，
(1)求$\omega$和$f ( \frac{\pi}{12} )$的值；
(2)若对任意，都有$| f ( x ) - m | \leq 1$，求实数$m$的取值范围.
<span class="fake-tag">答案</span>(1)$\omega = 1$，；
(2)$- \frac{1}{4} \leq m \leq 1 - \frac{\sqrt{3}}{2}$.
<span class="fake-tag">分析</span>（1）利用三角恒等变换化简函数，再由给定周期求出$\omega$及函数值.
（2）利用正弦函数的性质求出函数的最值，再利用恒成立的不等式求解即得.
<span class="fake-tag">详解</span>（1）依题意，$f ( x ) = \frac{1}{2} \lbrack 1 + \cos ( 2 \omega x - \frac{\pi}{3} ) \rbrack - \frac{1}{2} ( 1 - \cos 2 \omega x )$= $\frac{1}{2} ( \frac{1}{2} \cos 2 \omega x + \frac{\sqrt{3}}{2} \sin 2 \omega x + \cos 2 \omega x ) = \frac{1}{2} ( \frac{\sqrt{3}}{2} \sin 2 \omega x + \frac{3}{2} \cos 2 \omega x ) = \frac{\sqrt{3}}{2} \sin ( 2 \omega x + \frac{\pi}{3} )$，
由函数的最小正周期为$\pi$，得$\frac{2 \pi}{2 \omega} = \pi$，因此$\omega = 1$，$f ( x ) = \frac{\sqrt{3}}{2} \sin ( 2 x + \frac{\pi}{3} )$，
所以$f ( \frac{\pi}{12} ) = \frac{\sqrt{3}}{2} \sin ( 2 \times \frac{\pi}{12} + \frac{\pi}{3} ) = \frac{\sqrt{3}}{2}$.
（2）由，得$2 x + \frac{\pi}{3} \in \lbrack - \frac{\text{5} \text{π}}{6} , \frac{\pi}{3} \rbrack$，则$- 1 \leq \sin ( 2 x + \frac{\pi}{3} ) \leq \frac{\sqrt{3}}{2}$，$f ( x {) {\frac{\sqrt{3}}{2} \frac{3}{4}}_{\max}}_{\min}$，
不等式$| f ( x ) - m | \leq 1 \Leftrightarrow f ( x ) - 1 \leq m \leq f ( x ) + 1$，
由对任意，都有$| f ( x ) - m | \leq 1$，得$\lbrack f ( x ) - 1 {\rbrack m i n}_{\max}$，
而$\lbrack f ( x ) + 1 {\rbrack {\frac{\sqrt{3}}{2} \frac{1}{4}}_{\max}}_{\min}$，则$- \frac{1}{4} \leq m \leq 1 - \frac{\sqrt{3}}{2}$，
所以实数$m$的取值范围为$- \frac{1}{4} \leq m \leq 1 - \frac{\sqrt{3}}{2}$.
##### 【变式2】（23-24高一下·广西柳州·期中）已知函数${f ( x ) = \sqrt{3}} {\cos {}^{2}} \omega x + \cos \omega x \sin \omega x - \frac{\sqrt{3}}{2} ( \omega > 0 )$，若$f ( x )$的最小正周期为$\pi$．
(1)求$f ( x )$的解析式；
(2)若函数$g ( x ) = f^{2} ( x ) - a f ( x ) + \frac{a}{4}$在$\left\lbrack - \frac{\pi}{6} , \frac{\pi}{6} \right\rbrack$上有三个不同零点，求实数*a*取值范围．
<span class="fake-tag">答案</span>(1)$f ( x ) = \sin \left( 2 x + \frac{\pi}{3} \right)$；
(2)$\left. \frac{6 \sqrt{3} + 3}{11} , \frac{4}{3} \right)$
<span class="fake-tag">分析</span>（1）根据二倍角公式以及辅助角公式化简$f ( x ) = \sin \left( 2 \omega x + \frac{\pi}{3} \right)$，即可由周期求解，
（2）利用换元法，将问题转化为$t^{2} - a t + \frac{a}{4} = 0$的根的分布，结合分类讨论即可求解.
<span class="fake-tag">详解</span>（1）${f ( x ) = \sqrt{3}} {\cos {}^{2}} \omega x + \cos \omega x \sin \omega x - \frac{\sqrt{3}}{2} = \frac{\sqrt{3} ( 1 + \cos 2 \omega x )}{2} + \frac{1}{2} \sin 2 \omega x - \frac{\sqrt{3}}{2}$
$= \frac{\sqrt{3}}{2} \cos 2 \omega x + \frac{1}{2} \sin 2 \omega x = \sin \left( 2 \omega x + \frac{\pi}{3} \right)$
因为$f ( x )$的最小正周期为$\pi$，
所以$\frac{2 \pi}{2 \omega} = \pi$，即$\omega = 1$，
所以$f ( x ) = \sin \left( 2 x + \frac{\pi}{3} \right)$；
（2）①由（1）知${g ( x ) =} {\sin {}^{2}} \left( 2 x + \frac{\pi}{3} \right) - a \sin \left( 2 x + \frac{\pi}{3} \right) + \frac{a}{4}$，
由$- \frac{\pi}{6} \leq x \leq \frac{\pi}{6}$，可得$0 \leq 2 x + \frac{\pi}{3} \leq \frac{\text{2} \text{π}}{3}$，
令$t = \sin \left( 2 x + \frac{\pi}{3} \right)$，则$g ( t ) = t^{2} - a t + \frac{a}{4}$，$0 \leq t \leq 1$，
若函数${g ( x ) =} {\sin {}^{2}} \left( 2 x + \frac{\pi}{3} \right) - a \sin \left( 2 x + \frac{\pi}{3} \right) + \frac{a}{4}$在$\left\lbrack - \frac{\pi}{6} , \frac{\pi}{6} \right\rbrack$有三个零点，
即$\sin^{2} \left( 2 x + \frac{\pi}{3} \right) - a \sin \left( 2 x + \frac{\pi}{3} \right) + \frac{a}{4} = 0$在$\left\lbrack - \frac{\pi}{6} , \frac{\pi}{6} \right\rbrack$有三个不相等的实数根，
也就是关于*t*的方程$t^{2} - a t + \frac{a}{4} = 0$在区间$\left. 0 , \frac{\sqrt{3}}{2} \right)$有一个实根，另一个实根在$\left. \frac{\sqrt{3}}{2} , 1 \right)$上，或一个实根是1，另一个实根在$\left. \frac{\sqrt{3}}{2} , 1 \right)$，
当一个根在，另一个实根在$\left( \frac{\sqrt{3}}{2} , 1 \right)$，令$g ( t ) = t^{2} - a t + \frac{a}{4}$
所以$\begin{cases}g ( 0 ) > 0 \\ g \left( \frac{\sqrt{3}}{2} \right) < 0 \\ g ( 1 ) > 0\end{cases}$,即$\begin{cases}\frac{a}{4} > 0 \\ \frac{3}{4} - \frac{\sqrt{3}}{2} a + \frac{a}{4} < 0 \\ 1 - a + \frac{a}{4} > 0\end{cases}$,解得：$\frac{6 \sqrt{3} + 3}{11} < a < \frac{4}{3}$
当一个根为0时，即$\frac{a}{4} = 0$，所以$a = 0$，此时方程为$t^{2} = 0$，所以，不合题意，
当一个根是即$\frac{3}{4} - \frac{\sqrt{3}}{2} a + \frac{a}{4} = 0$，解得$a = \frac{6 \sqrt{3} + 3}{11}$，
此时可求得另一根$t = \frac{6 + \sqrt{3}}{22}$，所以符合题意，
当一个根是1，另一个实根在$\left( \frac{\sqrt{3}}{2} , 1 \right)$，由$1 - a + \frac{a}{4} = 0$得$a = \frac{4}{3}$，
此时方程为$t^{2} - \frac{4}{3} t + \frac{1}{3} = 0$，解得$t = 1$或$t = \frac{1}{3}$，这两个根都不属于$\left( \frac{\sqrt{3}}{2} , 1 \right)$，不合题意，
综上*a*的取值范围是$\left. \frac{6 \sqrt{3} + 3}{11} , \frac{4}{3} \right)$．