**专题34　单变量不等式能成立之最值分析法**

![](images/62a646798799cb3c683f8c21aa735e7c5fd943f574c9d3fe736f7be882c286d2.jpg)

**【方法总结】**

单变量不等式能成立之最值分析法

遇到<em>f</em>(<em>x</em>)≥<em>g</em>(<em>x</em>)型的不等式能成立问题时，一般采用作差法，构造“左减右”的函数<em>h</em>(<em>x</em>)＝<em>f</em>(<em>x</em>)－<em>g</em>(<em>x</em>)或“右减左”的函数<em>u</em>(<em>x</em>)＝<em>g</em>(<em>x</em>)－<em>f</em>(<em>x</em>)，进而只需满足<em>h</em>(<em>x</em>)<sub>max</sub>≥0或<em>u</em>(<em>x</em>)<sub>min</sub>≤0，将比较法的思想融入函数中，转化为求解函数最值的问题，适用范围较广，但是往往需要对参数进行分类讨论．

注意　“恒成立”与“存在性”问题的求解是“互补”关系，即*f*(*x*)≥*g*(*a*)对于*x*∈*D*恒成立，应求*f*(*x*)的最小值；若存在*x*∈*D*，使得*f*(*x*)≥*g*(*a*)成立，应求*f*(*x*)的最大值．在具体问题中究竟是求最大值还是最小值，可以先联想“恒成立”是求最大值还是最小值，这样也就可以解决相应的“存在性”问题是求最大值还是最小值．注意与恒成立问题的区别．特别需要关注等号是否成立问题，以免细节出错．

**【例题选讲】**

<strong>[例1]</strong>　设函数<em>f</em> (<em>x</em>)＝2ln<em>x</em>－<em>mx</em><sup>2</sup>＋1．

(1)讨论函数*f* (*x*)的单调性；

(2)当<em>f</em> (<em>x</em>)有极值时，若存在<em>x</em><sub>0</sub>，使得<em>f</em> (<em>x</em><sub>0</sub>)&gt;<em>m</em>－1成立，求实数<em>m</em>的取值范围．

解析　(1)函数*f* (*x*)的定义域为(0，＋∞)，*f* ′(*x*)＝－2*mx*＝，

当*m*≤0时，*f* ′(*x*)>0，∴*f* (*x*)在(0，＋∞)上单调递增；当*m*>0时，令*f* ′(*x*)>0，得0<*x*<，

令*f* ′(*x*)<0，得*x*>，∴*f* (*x*)在上单调递增，在上单调递减．

(2)由(1)知，当*f* (*x*)有极值时，*m*>0，且*f* (*x*)在上单调递增，在上单调递减．

∴<em>f</em> (<em>x</em>)<sub>max</sub>＝<em>f</em> ＝2ln－<em>m</em>·＋1＝－ln <em>m</em>，

若存在<em>x</em><sub>0</sub>，使得<em>f</em> (<em>x</em><sub>0</sub>)&gt;<em>m</em>－1成立，则<em>f</em> (<em>x</em>)<sub>max</sub>&gt;<em>m</em>－1．即－ln <em>m</em>&gt;<em>m</em>－1，ln<em>m</em>＋<em>m</em>－1&lt;0成立．

令*g*(*x*)＝*x*＋ln *x*－1(*x*>0)，∵*g*′(*x*)＝1＋>0，∴*g*(*x*)在(0，＋∞)上单调递增，且*g*(1)＝0，∴0<*m*<1．

∴实数*m*的取值范围是(0，1)．

<strong>[例2]</strong>　设<em>f</em>(<em>x</em>)＝<em>x</em>－－<em>a</em>ln<em>x</em>(<em>a</em>∈<strong>R</strong>)．

(1)当*a*＝1时，求曲线*y*＝*f*(*x*)在点(，*f*())处的切线方程；

(2)当<em>a</em>&lt;1时，在内是否存在一实数<em>x</em><sub>0</sub>，使<em>f</em>(<em>x</em><sub>0</sub>)&gt;e－1成立？

解析　(1)当*a*＝1时，*f*(*x*)＝*x*－ln *x*，*f*()＝＋ln 2，*f*′(*x*)＝1－，

所以曲线*y*＝*f*(*x*)在点处的切线的斜率为*f*′＝1－＝－1.

故所求切线方程为*y*－＝－，即*x*＋*y*－ln 2－1＝0.

(2)假设当<em>a</em>&lt;1时，在内存在一实数<em>x</em><sub>0</sub>，使<em>f</em>(<em>x</em><sub>0</sub>)&gt;e－1成立，

则只需证明当<em>x</em>∈时，<em>f</em>(<em>x</em>)<sub>max</sub>&gt;e－1即可．

*f*′(*x*)＝1＋－＝＝(*x*>0)，

令<em>f</em>′(<em>x</em>)＝0得，<em>x</em><sub>1</sub>＝1，<em>x</em><sub>2</sub>＝<em>a</em>－1，当<em>a</em>&lt;1时，<em>a</em>－1&lt;0，∴当<em>x</em>∈时，<em>f</em>′(<em>x</em>)&lt;0；当<em>x</em>∈(1，e)时，<em>f</em>′(<em>x</em>)&gt;0．

∴函数<em>f</em>(<em>x</em>)在上单调递减，在[1，e]上单调递增，∴<em>f</em>(<em>x</em>)<sub>max</sub>＝max{<em>f</em>()，<em>f</em>(e)}．

于是，只需证明*f*(e)>e－1或*f*()>e－1即可．

∵*f*(e)－(e－1)＝e－－*a*－(e－1)＝>0，∴*f*(e)>e－1成立．

所以假设正确，即当<em>a</em>&lt;1时，在<em>x</em>∈内至少存在一实数<em>x</em><sub>0</sub>，使<em>f</em>(<em>x</em><sub>0</sub>)&gt;e－1成立．

<strong>[例3]</strong>　已知<em>f</em>(<em>x</em>)＝<em>x</em>e<em><sup>ax</sup></em>－<em>x</em><sup>2</sup>－<em>x</em>＋1，<em>a</em>≠0．

(1)当*a*＝1时，求*f*(*x*)的单调区间；

(2)若∃<em>x</em><sub>0</sub>≥1，使<em>f</em>(<em>x</em><sub>0</sub>)＜成立，求参数<em>a</em>的取值范围．

解析　(1)当<em>a</em>＝1时，<em>f</em>(<em>x</em>)＝<em>x</em>e<em><sup>x</sup></em>－－<em>x</em>＋1，

所以<em>f</em>′(<em>x</em>)＝e<em><sup>x</sup></em>＋<em>x</em>e<em><sup>x</sup></em>－<em>x</em>－1＝(e<em><sup>x</sup></em>－1)(<em>x</em>＋1)．由<em>f</em>′(<em>x</em>)＞0，得<em>x</em>＜－1或<em>x</em>＞0；由<em>f</em>′(<em>x</em>)＜0，得－1＜<em>x</em>＜0．

所以*f*(*x*)的单调递减区间为(－1，0)，*f*(*x*)的单调递增区间为(－∞，－1)，(0，＋∞)．

(2)由题意，得<em>f</em>(<em>x</em>)<sub>min</sub>＜(<em>x</em>≥1)，

因为<em>f</em>′(<em>x</em>)＝(<em>ax</em>＋1)(e<em><sup>ax</sup></em>－1)，由<em>f</em>′(<em>x</em>)＝0，解得<em>x</em><sub>1</sub>＝－，<em>x</em><sub>2</sub>＝0．

①当<em>a</em>＞0时，因为<em>x</em>≥1，所以<em>f</em>′(<em>x</em>)＞0，所以<em>f</em>(<em>x</em>)单调递增，即<em>f</em>(<em>x</em>)<sub>min</sub>＝<em>f</em>(1)．

<em>f</em>(1)＝e<em><sup>a</sup></em>－＜，即e<em><sup>a</sup></em>－<em>a</em>＜0．设<em>g</em>(<em>a</em>)＝e<em><sup>a</sup></em>－<em>a</em>(<em>a</em>＞0)，<em>g</em>′(<em>a</em>)＝e<em><sup>a</sup></em>－1＞0．

所以<em>g</em>(<em>a</em>)<sub>min</sub>＞<em>g</em>(0)＝e<sup>0</sup>－0＝1＞0，即e<em><sup>a</sup></em>＞<em>a</em>恒成立，即<em>g</em>(<em>a</em>)＞0，所以不等式e<em><sup>a</sup></em>－<em>a</em>＜0无解；

②当*a*＜0时，当*x*∈(－∞，0)时，*f*′(*x*)>0；当*x*∈时，*f*′(*x*)<0；当*x*∈时，*f*′(*x*)>0．

∴函数*f*(*x*)在(－∞，0)上单调递增，在上单调递减，在上单调递增．

且<em>f</em>(0)＝1＞0，由①知<em>f</em>(1)＞恒成立，若∃<em>x</em><sub>0</sub>≥1，使<em>f</em>(<em>x</em><sub>0</sub>)＜，则

所以所以

解得1－＜*a*＜0．综上所述，参数*a*的取值范围为．

<strong>[例4]</strong>　已知函数<em>f</em>(<em>x</em>)＝－<em>a</em>ln<em>x</em>－＋<em>ax</em>，<em>a</em>∈<strong>R</strong>．

(1)当*a*<0时，讨论*f*(*x*)的单调性；

(2)设<em>g</em>(<em>x</em>)＝<em>f</em>(<em>x</em>)＋<em>xf</em>′(<em>x</em>)，若关于<em>x</em>的不等式<em>g</em>(<em>x</em>)≤－e<em><sup>x</sup></em>＋＋(<em>a</em>－1)<em>x</em>在[1，2]上有解，求实数<em>a</em>的取值范围．

解析　(1)依题设，*f*′(*x*)＝－－＋*a*＝(*x*>0)，

当<em>a</em>&lt;0时，<em>ax</em>－e<em><sup>x</sup></em>&lt;0恒成立，所以当<em>x</em>&gt;1时，<em>f</em>′(<em>x</em>)&lt;0，当0&lt;<em>x</em>&lt;1时，<em>f</em>′(<em>x</em>)&gt;0，

故函数*f*(*x*)在(0，1)上单调递增，在(1，＋∞)上单调递减．

(2)因为<em>g</em>(<em>x</em>)＝<em>f</em>(<em>x</em>)＋<em>xf</em>′(<em>x</em>)，所以<em>g</em>(<em>x</em>)＝－<em>a</em>ln <em>x</em>－e<em><sup>x</sup></em>＋2<em>ax</em>－<em>a</em>，

由题意知，存在<em>x</em><sub>0</sub>∈[1，2]，使得<em>g</em>(<em>x</em><sub>0</sub>)≤－e<em><sup>x</sup></em><sup>0</sup>＋＋(<em>a</em>－1)<em>x</em><sub>0</sub>成立．

则存在<em>x</em><sub>0</sub>∈[1，2]，使得－<em>a</em>ln <em>x</em><sub>0</sub>＋(<em>a</em>＋1)<em>x</em><sub>0</sub>－－<em>a</em>≤0成立，

令*h*(*x*)＝－*a*ln *x*＋(*a*＋1)*x*－－*a*，*x*∈[1，2]，

则*h*′(*x*)＝＋*a*＋1－*x*＝－，*x*∈[1，2]．

①当*a*≤1时，*h*′(*x*)≤0，所以函数*h*(*x*)在[1，2]上单调递减，

所以<em>h</em>(<em>x</em>)<sub>min</sub>＝<em>h</em>(2)＝－<em>a</em>ln 2＋<em>a</em>≤0成立，解得<em>a</em>≤0，所以<em>a</em>≤0．

②当1<*a*<2时，令*h*′(*x*)>0，解得1<*x*<*a*；令*h*′(*x*)<0，解得*a*<*x*<2．

所以函数*h*(*x*)在[1，*a*]上单调递增，在[*a*，2]上单调递减，

又因为*h*(1)＝，所以*h*(2)＝－*a*ln 2＋*a*≤0，解得*a*≤0，与1<*a*<2矛盾，故舍去．

③当<em>a</em>≥2时，<em>h</em>′(<em>x</em>)≥0，所以函数<em>h</em>(<em>x</em>)在[1，2]上单调递增，所以<em>h</em>(<em>x</em>)<sub>min</sub>＝<em>h</em>(1)＝&gt;0，不符合题意．

综上所述，实数*a*的取值范围为(－∞，0]．

<strong>[例5]</strong>　已知函数<em>f</em>(<em>x</em>)＝<em>x</em><sup>2</sup>－(<em>a</em>＋3)<em>x</em>＋3<em>a</em>ln<em>x</em>，<em>g</em>(<em>x</em>)＝<em>x</em><sup>2</sup>－(<em>a</em>＋4)<em>x</em>－＋4<em>a</em>ln<em>x</em>．

(1)当*a*＝2时，求函数*f*(*x*)的极值；

(2)当<em>a</em>＞0时，若在[1，e](e为自然对数的底数)上存在一点<em>x</em><sub>0</sub>，使得<em>f</em>(<em>x</em><sub>0</sub>)＜<em>g</em>(<em>x</em><sub>0</sub>)成立，求实数<em>a</em>的取值范围．

解析　(1)∵函数<em>f</em>(<em>x</em>)＝<em>x</em><sup>2</sup>－(<em>a</em>＋3)<em>x</em>＋3<em>a</em>ln <em>x</em>，∴<em>f</em>(<em>x</em>)定义域为(0，＋∞)，

∴*f*′(*x*)＝*x*－(*a*＋3)＋＝，

当*a*＝2时，令*f*′(*x*)＝＝0，解得*x*＝2或*x*＝3，

∴当*x*∈(0，2)∪(3，＋∞)时，*f*′(*x*)＞0；当*x*∈(2，3)时，*f*′(*x*)＜0，

∴*f*(*x*)在(0，2)，(3，＋∞)上单调递增，*f*(*x*)在(2，3)上单调递减，

∴函数*f*(*x*)的极小值为*f*(3)＝6ln 3－，函数*f*(*x*)的极大值为*f*(2)＝6ln 2－8．

(2)令*F*(*x*)＝*f*(*x*)－*g*(*x*)＝*x*＋－*a*ln *x*，

在[1，e]上存在一点<em>x</em><sub>0</sub>，使得<em>f</em>(<em>x</em><sub>0</sub>)＜<em>g</em>(<em>x</em><sub>0</sub>)成立，即在[1，e]上存在一点<em>x</em><sub>0</sub>，使得<em>F</em>(<em>x</em><sub>0</sub>)＜0，

即函数*F*(*x*)＝*x*＋－*a*ln *x*在[1，e]上的最小值小于零．

由*F*(*x*)＝*x*＋－*a*ln *x*得*F*′(*x*)＝1－－＝，

∵*a*＞0，∴*a*＋1＞1，又*x*∈(0，＋∞)，∴*x*＋1＞0，

∴当*x*∈(0，*a*＋1)时，*F*′(*x*)＜0；当*x*∈(*a*＋1，＋∞)时，*F*′(*x*)＞0，

①当1＜*a*＋1＜e，即0＜*a*＜e－1时，*F*(*x*)在[1，*a*＋1)上单调递减，在[*a*＋1，e]上单调递增，

∴<em>F</em>(<em>x</em>)<sub>min</sub>＝<em>F</em>(<em>a</em>＋1)＝<em>a</em>＋2－<em>a</em>ln(<em>a</em>＋1)，

∵0＜ln(*a*＋1)＜1，∴0＜*a*ln(*a*＋1)＜*a*，∴*a*＋2－*a*ln(*a*＋1)＞2，此时*F*(*a*＋1)＜0不成立．

②当<em>a</em>＋1≥e，即<em>a</em>≥e－1时，<em>F</em>(<em>x</em>)在[1，e]上单调递减，∴<em>F</em>(<em>x</em>)<sub>min</sub>＝<em>F</em>(e)．

由*F*(e)＝e＋－*a*＜0可得：*a*＞，∵＞e－1，∴*a*＞．

综上所述：实数*a*的取值范围为．

**【对点精练】**

1．已知函数<em>f</em>(<em>x</em>)＝<em>ax</em><sup>2</sup>＋ln<em>x</em>．

(1)讨论*f*(*x*)的单调性；

(2)若∃*x*∈(0，＋∞)使*f*(*x*)>0成立，求*a*的取值范围．

1．解析　(1)函数*f*(*x*)的定义域为(0，＋∞)，*f*′(*x*)＝2*ax*＋＝，

①*a*≥0时，*f*′(*x*)>0，函数*f*(*x*)在区间(0，＋∞)上单调递增；

②<em>a</em>＜0时，由2<em>ax</em><sup>2</sup>＋1&gt;0得0&lt;<em>x</em>&lt;．

∴函数*f*(*x*)在区间上单调递增，函数*f*(*x*)在区间上单调递减．

(2)①<em>a</em>≥0时，<em>f</em>(e)＝<em>a</em>e<sup>2</sup>＋1＞0，∴∃<em>x</em>∈(0，＋∞)使<em>f</em>(<em>x</em>)&gt;0成立；

②<em>a</em>&lt;0时，需<em>f</em>(<em>x</em>)<sub>max</sub>＝<em>f</em>＝<em>a</em>＋ln＝－＋ln&gt;0，

得*a*>－，∴*a*∈，

∴由①②得*a*∈．

2．已知函数<em>f</em> (<em>x</em>)＝<em>x</em>－<em>a</em>ln<em>x</em>，<em>g</em>(<em>x</em>)＝－(<em>a</em>∈<strong>R</strong>)．若在[1，e]上存在一点<em>x</em><sub>0</sub>，使得<em>f</em>(<em>x</em><sub>0</sub>)&lt;<em>g</em>(<em>x</em><sub>0</sub>)成立，求<em>a</em>的

取值范围．

2．解析　依题意，只需[<em>f</em> (<em>x</em><sub>0</sub>)－<em>g</em>(<em>x</em><sub>0</sub>)]<sub>min</sub>&lt;0，<em>x</em><sub>0</sub>∈[1，e]即可．

令*h*(*x*)＝*f* (*x*)－*g*(*x*)＝*x*－*a*ln *x*＋，*x*∈[1，e]，

则*h*′(*x*)＝1－－＝＝．令*h*′(*x*)＝0，得*x*＝*a*＋1．

①若<em>a</em>＋1≤1，即<em>a</em>≤0时，<em>h</em>′(<em>x</em>)≥0，<em>h</em>(<em>x</em>)单调递增，<em>h</em>(<em>x</em>)<sub>min</sub>＝<em>h</em>(1)＝<em>a</em>＋2&lt;0，得<em>a</em>&lt;－2；

②若1<*a*＋1<e，即0<*a*<e－1时，*h*(*x*)在[1，*a*＋1)上单调递减，在(*a*＋1，e]上单调递增，

故<em>h</em>(<em>x</em>)<sub>min</sub>＝<em>h</em>(<em>a</em>＋1)＝(<em>a</em>＋1)－<em>a</em>ln(<em>a</em>＋1)＋1＝<em>a</em>[1－ln(<em>a</em>＋1)]＋2&gt;2，<em>x</em>∈(0，e－1)与<em>h</em>(<em>x</em>)&lt;0不符，故舍去．

③若<em>a</em>＋1≥e，即<em>a</em>≥e－1时，<em>h</em>(<em>x</em>)在[1，e]上单调递减，则<em>h</em>(<em>x</em>)<sub>min</sub>＝<em>h</em>(e)＝e－<em>a</em>＋，

令*h*(e)<0，得*a*>>e－1成立．

综上所述，*a*的取值范围为(－∞，－2)∪．

3．已知函数*f*(*x*)＝*x*(ln*x*－1)，*g*(*x*)＝．

(1)求证：当0&lt;<em>x</em>&lt;时，<em>f</em>(<em>x</em>)&lt;<em>x</em><sup>2</sup>－<em>x</em>；

(2)若存在<em>x</em><sub>0</sub>∈(0，<em>m</em>]，使<em>f</em>(<em>x</em><sub>0</sub>)－<em>g</em>(<em>m</em>)≤0，求<em>m</em>的取值范围．

3．解析　(1)由题得<em>f</em>(<em>x</em>)的定义域为(0，＋∞)，<em>x</em>(ln <em>x</em>－1)&lt;<em>x</em><sup>2</sup>－<em>x</em>，即ln <em>x</em>－<em>x</em>＋&lt;0，

设函数*F*(*x*)＝ln *x*－*x*＋，则*F*′(*x*)＝，故函数*F*(*x*)在(0，1)上单调递增．

当0&lt;<em>x</em>&lt;时，<em>F</em>(<em>x</em>)&lt;<em>F</em>＝－&lt;0，即<em>f</em>(<em>x</em>)&lt;<em>x</em><sup>2</sup>－<em>x</em>．

(2)*f*′(*x*)＝ln*x*，故函数*f*(*x*)在(0，1)上单调递减，在(1，＋∞)上单调递增，

①当0&lt;<em>m</em>≤1时，<em>f</em>(<em>x</em>)<sub>min</sub>＝<em>f</em>(<em>m</em>)＝<em>m</em>(ln <em>m</em>－1)＝<em>m</em>ln <em>m</em>－<em>m</em>，

依题意可知<em>f</em>(<em>m</em>)－<em>g</em>(<em>m</em>)≤0⇒2<em>m</em>ln <em>m</em>＋(e<em><sup>m</sup></em>－2<em>m</em>－1)≤0．

构造函数：<em>φ</em>(<em>m</em>)＝e<em><sup>m</sup></em>－2<em>m</em>－1(0&lt;<em>m</em>≤1)，则有<em>φ</em>′(<em>m</em>)＝e<em><sup>m</sup></em>－2．

由此可得：当*m*∈(0，ln 2)时，*φ*′(*m*)<0；当*m*∈(ln 2，1)时，*φ*′(*m*)>0，

即*φ*(*m*)在*m*∈(0，ln 2)时单调递减，*m*∈(ln 2，1)单调递增，

注意到：*φ*(0)＝0，*φ*(1)＝0，因此*φ*(*m*)≤0．

同时注意到2<em>m</em>ln <em>m</em>≤0，故有2<em>m</em>ln <em>m</em>＋(e<em><sup>m</sup></em>－2<em>m</em>－1)≤0．

②当<em>m</em>&gt;1时，<em>f</em>(<em>x</em>)<sub>min</sub>＝<em>f</em>(1)＝－1，

依据题意可知<em>f</em>(<em>m</em>)－<em>g</em>(<em>m</em>)≤0⇒－1－≤0⇒e<em><sup>m</sup></em>≤3⇒1&lt;<em>m</em>≤ln 3，

综上①、②所述，所求实数*m*取值范围为(0，ln 3]．

4．已知函数<em>f</em>(<em>x</em>)＝ln<em>x</em>－<em>a</em>(<em>x</em>＋1)，<em>a</em>∈<strong>R</strong>，在点(1，<em>f</em>(1))处的切线与<em>x</em>轴平行．

(1)求*f*(*x*)的单调区间；

(2)若存在<em>x</em><sub>0</sub>＞1，当<em>x</em>∈(1，<em>x</em><sub>0</sub>)时，恒有<em>f</em>(<em>x</em>)－＋2<em>x</em>＋＞<em>k</em>(<em>x</em>－1)成立，求<em>k</em>的取值范围．

4．解析　(1)由已知可得*f*(*x*)的定义域为(0，＋∞)．

∵*f*′(*x*)＝－*a*，∴*f*′(1)＝1－*a*＝0，∴*a*＝1，∴*f*′(*x*)＝－1＝，

令*f*′(*x*)＞0，得0＜*x*＜1，令*f*′(*x*)＜0，得*x*＞1，

∴*f*(*x*)的单调递增区间为(0，1)，单调递减区间为(1，＋∞)．

(2)不等式*f*(*x*)－＋2*x*＋＞*k*(*x*－1)可化为ln *x*－＋*x*－＞*k*(*x*－1)．

令*g*(*x*)＝ln *x*－＋*x*－－*k*(*x*－1)(*x*＞1)，则*g*′(*x*)＝－*x*＋1－*k*＝，

令<em>h</em>(<em>x</em>)＝－<em>x</em><sup>2</sup>＋(1－<em>k</em>)<em>x</em>＋1(<em>x</em>＞1)，则<em>h</em>(<em>x</em>)的对称轴为<em>x</em>＝．

①当≤1，即<em>k</em>≥－1时，易知<em>h</em>(<em>x</em>)在(1，<em>x</em><sub>0</sub>)上单调递减，∴<em>h</em>(<em>x</em>)＜<em>h</em>(1)＝1－<em>k</em>．

若<em>k</em>≥1，则<em>h</em>(<em>x</em>)＜0，∴<em>g</em>′(<em>x</em>)＜0，∴<em>g</em>(<em>x</em>)在(1，<em>x</em><sub>0</sub>)上单调递减，∴<em>g</em>(<em>x</em>)＜<em>g</em>(1)＝0，不合题意；

若－1≤<em>k</em>＜1，则<em>h</em>(1)＞0，∴必存在<em>x</em><sub>0</sub>使得<em>x</em>∈(1，<em>x</em><sub>0</sub>)时<em>g</em>′(<em>x</em>)＞0，

∴<em>g</em>(<em>x</em>)在(1，<em>x</em><sub>0</sub>)上单调递增，∴<em>g</em>(<em>x</em>)＞<em>g</em>(1)＝0恒成立，符合题意．

②当＞1，即<em>k</em>＜－1时，易知必存在<em>x</em>，使得<em>h</em>(<em>x</em>)在(1，<em>x</em><sub>0</sub>)上单调递增．∴<em>h</em>(<em>x</em>)＞<em>h</em>(1)＝1－<em>k</em>＞0，∴<em>g</em>′(<em>x</em>)＞0，∴<em>g</em>(<em>x</em>)在(1，<em>x</em><sub>0</sub>)上单调递增．∴<em>g</em>(<em>x</em>)＞<em>g</em>(1)＝0恒成立，符合题意．

综上，*k*的取值范围为(－∞，1)．

5．已知函数*f*(*x*)＝2*x*－＋*k*ln*x*．

(1)当*k*＝－3时，求*f*(*x*)的极值；

(2)若存在*x*∈[1，e]，使得3*x*－*f*(*x*)<－成立，求实数*k*的取值范围．

5．解析　(1)当*k*＝－3时，*f*′(*x*)＝2＋－＝＝．

∵*x*>0，∴当*x*∈∪(1，＋∞)时，*f*′(*x*)>0；当*x*∈时，*f*′(*x*)<0．

∴*f*(*x*)的单调递增区间为，(1，＋∞)，*f*(*x*)的单调递减区间为，

∴*f*(*x*)的极大值为*f* ＝3ln 2－1，*f*(*x*)的极小值为*f*(1)＝1．

(2)若∃*x*∈[1，e]，使得3*x*－*f*(*x*)<－成立，即3*x*－2*x*＋－*k*ln *x*<－⇒*x*＋－*k*ln *x*<0有解，

设*h*(*x*)＝*x*＋－*k*ln *x*，只需*h*(*x*)在[1，e]上的最小值小于0，

*h*′(*x*)＝1－－＝．

①当*k*≤0，*x*∈[1，e]时，*h*′(*x*)≥0，*h*(*x*)在[1，e]上单调递增，

<em>h</em>(<em>x</em>)<sub>min</sub>＝<em>h</em>(1)＝1＋<em>k</em>＋1&lt;0⇒<em>k</em>&lt;－2．∵－2&lt;0，∴<em>k</em>&lt;－2．

②当1<*k*＋1<e，即0<*k*<e－1，*x*∈[1，*k*＋1)时，*h*′(*x*)<0，*x*∈(*k*＋1，e]时，*h*′(*x*)>0，

*h*(*x*)在区间[1，*k*＋1]上单调递减，在区间[*k*＋1，e]上单调递增，

∴<em>h</em>(<em>x</em>)<sub>min</sub>＝<em>h</em>(<em>k</em>＋1)＝<em>k</em>＋1＋1－<em>k</em>ln(<em>k</em>＋1)＝<em>k</em>＋2－<em>k</em>ln(<em>k</em>＋1)．

∵1<*k*＋1<e，∴0<ln(*k*＋1)<1⇒0<*k*ln(*k*＋1)<*k*，∴2＋*k*－*k*ln(*k*＋1)>2，不满足题意．

③当*k*＋1≥e，即*k*≥e－1，*x*∈[1，e]时，*h*′(*x*)≤0，*h*(*x*)在[1，e]上单调递减，

<em>h</em>(<em>x</em>)<sub>min</sub>＝<em>h</em>(e)＝e＋－<em>k</em>&lt;0⇒<em>k</em>&gt;．又∵&gt;e－1，∴<em>k</em>&gt;．

∴实数*k*的取值范围是(－∞，－2)∪．

6．已知<em>f</em>(<em>x</em>)＝<em>x</em><sup>2</sup>＋<em>ax</em>－ln <em>x</em>＋e，<em>g</em>(<em>x</em>)＝<em>x</em><sup>2</sup>＋e．

(1)若<em>a</em>＝－1，判断是否存在<em>x</em><sub>0</sub>＞0，使得<em>f</em>(<em>x</em><sub>0</sub>)＜0，并说明理由；

(2)设*h*(*x*)＝*f*(*x*)－*g*(*x*)，是否存在实数*a*，当*x*∈(0，e](e＝2.718 28…为自然常数)时，函数*h*(*x*)的最小值为3，并说明理由．

6．解析　(1)不存在<em>x</em><sub>0</sub>＞0，使得<em>f</em>(<em>x</em><sub>0</sub>)＜0．理由如下：当<em>a</em>＝－1时，<em>f</em>(<em>x</em>)＝<em>x</em><sup>2</sup>－<em>x</em>－ln <em>x</em>＋e，<em>x</em>∈(0，＋∞)，

*f*′(*x*)＝2*x*－1－＝＝．

*x*∈(0，1)，*f*′(*x*)＜0，函数*f*(*x*)单调递减；*x*∈(1，＋∞)，*f*′(*x*)＞0，函数*f*(*x*)单调递增，

当<em>x</em>＝1时，函数<em>f</em>(<em>x</em>)有极小值<em>f</em>(<em>x</em>)<sub>极小值</sub>＝<em>f</em>(1)＝e，此极小值也是最小值，

故不存在<em>x</em><sub>0</sub>＞0，使得<em>f</em>(<em>x</em><sub>0</sub>)＜0．

(2)因为<em>f</em>(<em>x</em>)＝<em>x</em><sup>2</sup>＋<em>ax</em>－ln <em>x</em>＋e，<em>g</em>(<em>x</em>)＝<em>x</em><sup>2</sup>＋e，所以<em>h</em>(<em>x</em>)＝<em>f</em>(<em>x</em>)－<em>g</em>(<em>x</em>)＝<em>ax</em>－ln <em>x</em>．

则*h*′(*x*)＝*a*－，假设存在实数*a*，使*h*(*x*)＝*ax*－ln *x*(*x*∈(0，e])有最小值3，

(ⅰ)当<em>a</em>≤0时，<em>h</em>′(<em>x</em>)＜0，所以<em>h</em>(<em>x</em>)在(0，e]上单调递减，<em>h</em>(<em>x</em>)<sub>min</sub>＝<em>h</em>(e)＝<em>a</em>e－1＝3，<em>a</em>＝，不符合题意．

(ⅱ)当*a*＞0时，

①当0＜*a*≤时，≥e，*h*′(*x*)＜0在(0，e]上恒成立，所以*h*(*x*)在(0，e]上单调递减，

<em>h</em>(<em>x</em>)<sub>min</sub>＝<em>h</em>(e)＝<em>a</em>e－1＝3，<em>a</em>＝，不符合题意．

②当*a*＞时，0＜＜e，当0＜*x*＜时，

*h*′(*x*)＜0，*h*(*x*)在上单调递减；当＜*x*＜e时，*h*′(*x*)＞0，*h*(*x*)在上单调递增，

所以<em>h</em>(<em>x</em>)<sub>min</sub>＝<em>h</em>＝1＋ln <em>a</em>＝3，解得<em>a</em>＝e<sup>2</sup>＞．

综上所述，存在<em>a</em>＝e<sup>2</sup>，使<em>x</em>∈(0，e]时，<em>h</em>(<em>x</em>)有最小值3．

