**专题30　单变量恒成立之同构或放缩后参变分离**

![](images/28d455bbd0c13713699b5e14189f843aaa321c3726d396a8adbac098af51495a.jpg)

**【方法总结】**

单变量恒成立之参变分离法

参变分离法是将不等式变形成一个一端是<em>f</em>(<em>a</em>)，另一端是变量表达式<em>g</em>(<em>x</em>)的不等式后，若<em>f</em>(<em>a</em>)≥<em>g</em>(<em>x</em>)在<em>x</em>∈<em>D</em>上恒成立，则<em>f</em>(<em>a</em>)≥<em>g</em>(<em>x</em>)<sub>max</sub>；若<em>f</em>(<em>a</em>)≤<em>g</em>(<em>x</em>)在<em>x</em>∈<em>D</em>上恒成立，则<em>f</em>(<em>a</em>)≤<em>g</em>(<em>x</em>)<sub>min</sub>．特别地，经常将不等式变形成一个一端是参数<em>a</em>，另一端是变量表达式<em>g</em>(<em>x</em>)的不等式后，若<em>a</em>≥<em>g</em>(<em>x</em>)在<em>x</em>∈<em>D</em>上恒成立，则<em>a</em>≥<em>g</em>(<em>x</em>)<sub>max</sub>；若<em>a</em>≤<em>g</em>(<em>x</em>)在<em>x</em>∈<em>D</em>上恒成立，则<em>a</em>≤<em>g</em>(<em>x</em>)<sub>min</sub>．

利用分离参数法来确定不等式*f*(*x*，*a*)≥0(*x*∈*D*，*a*为实参数)恒成立问题中参数取值范围的基本步骤：

(1)将参数与变量分离，化为<em>f</em><sub>1</sub>(<em>a</em>)≥<em>f</em><sub>2</sub>(<em>x</em>)或<em>f</em><sub>1</sub>(<em>a</em>)≤<em>f</em><sub>2</sub>(<em>x</em>)的形式．

(2)求<em>f</em><sub>2</sub>(<em>x</em>)在<em>x</em>∈<em>D</em>时的最大值或最小值．

(3)解不等式<em>f</em><sub>1</sub>(<em>a</em>)≥<em>f</em><sub>2</sub>(<em>x</em>)<sub>max</sub>或<em>f</em><sub>1</sub>(<em>a</em>)≤<em>f</em><sub>2</sub>(<em>x</em>)<sub>min</sub>，得到<em>a</em>的取值范围．

**【例题选讲】**

<strong>[例1]</strong>　(2020·新高考Ⅰ)已知函数<em>f</em>(<em>x</em>)＝<em>a</em>e<em><sup>x</sup></em><sup>－1</sup>－ln<em>x</em>＋ln<em>a</em>．

(1)当*a*＝e时，求曲线*y*＝*f*(*x*)在点(1，*f*(1))处的切线与两坐标轴围成的三角形的面积；

(2)若*f*(*x*)≥1，求*a*的取值范围．

解析　(1)当<em>a</em>＝e时，<em>f</em>(<em>x</em>)＝e<em><sup>x</sup></em>－ln <em>x</em>＋1，∴<em>f</em>′(<em>x</em>)＝e<em><sup>x</sup></em>－，∴<em>f</em>′(1)＝e－1．

∵*f*(1)＝e＋1，∴切点坐标为(1，1＋e)，

∴曲线*y*＝*f*(*x*)在点(1，*f*(1))处的切线方程为*y*－e－1＝(e－1)·(*x*－1)，即*y*＝(e－1)*x*＋2，

∴切线与两坐标轴的交点坐标分别为(0，2)，，

∴所求三角形面积为×2×＝．

(2)解法一　(同构后参变分离)

<em>f</em>(<em>x</em>)＝<em>a</em>e<em><sup>x</sup></em><sup>－1</sup>－ln<em>x</em>＋ln<em>a</em>＝e<sup>ln</sup> <em><sup>a</sup></em><sup>＋</sup><em><sup>x</sup></em><sup>－1</sup>－ln<em>x</em>＋ln<em>a</em>≥1等价于e<sup>ln</sup> <em><sup>a</sup></em><sup>＋</sup><em><sup>x</sup></em><sup>－1</sup>＋ln<em>a</em>＋<em>x</em>－1≥ln<em>x</em>＋<em>x</em>＝e<sup>ln</sup> <em><sup>x</sup></em>＋ln<em>x</em>，

令<em>g</em>(<em>x</em>)＝e<em><sup>x</sup></em>＋<em>x</em>，上述不等式等价于<em>g</em>(ln<em>a</em>＋<em>x</em>－1)≥<em>g</em>(ln<em>x</em>)，

显然*g*(*x*)为单调递增函数，∴又等价于ln*a*＋*x*－1≥ln*x*，即ln*a*≥ln*x*－*x*＋1，

令*h*(*x*)＝ln*x*－*x*＋1，则*h*′(*x*)＝－1＝，

在(0，1)上*h*′(*x*)>0，*h*(*x*)单调递增；在(1，＋∞)上*h*′(*x*)<0，*h*(*x*)单调递减，

∴<em>h</em>(<em>x</em>)<sub>max</sub>＝<em>h</em>(1)＝0，ln <em>a</em>≥0，即<em>a</em>≥1，∴<em>a</em>的取值范围是[1，＋∞)．

解法二　(最值分析法＋隐零点法)

∵<em>f</em>(<em>x</em>)＝<em>a</em>e<em><sup>x</sup></em><sup>－1</sup>－ln <em>x</em>＋ln<em>a</em>，∴<em>f</em>′(<em>x</em>)＝<em>a</em>e<em><sup>x</sup></em><sup>－1</sup>－，且<em>a</em>&gt;0．

设<em>g</em>(<em>x</em>)＝<em>f</em>′(<em>x</em>)，则<em>g</em>′(<em>x</em>)＝<em>a</em>e<em><sup>x</sup></em><sup>－1</sup>＋&gt;0，∴<em>g</em>(<em>x</em>)在(0，＋∞)上单调递增，即<em>f</em>′(<em>x</em>)在(0，＋∞)上单调递增，

当*a*＝1时，*f*′(1)＝0，则*f*(*x*)在(0，1)上单调递减，在(1，＋∞)上单调递增，

∴<em>f</em>(<em>x</em>)<sub>min</sub>＝<em>f</em>(1)＝1，∴<em>f</em>(<em>x</em>)≥1成立；

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

当*a*>1时，<1，∴<1，∴*f*′*f*′(1)＝，

∴存在唯一<em>x</em><sub>0</sub>&gt;0，使得<em>f</em>′(<em>x</em><sub>0</sub>)＝<em>a</em>e<em><sup>x</sup></em><sup>0－1</sup>－＝0，且当<em>x</em>∈(0，<em>x</em><sub>0</sub>)时<em>f</em>′(<em>x</em>)&lt;0，当<em>x</em>∈(<em>x</em><sub>0</sub>，＋∞)时<em>f</em>′(<em>x</em>)&gt;0，

∴<em>a</em>e <em><sup>x</sup></em><sup>0－1</sup>＝，∴ln<em>a</em>＋<em>x</em><sub>0</sub>－1＝－ln<em>x</em><sub>0</sub>，

因此<em>f</em>(<em>x</em>)<sub>min</sub>＝<em>f</em>(<em>x</em><sub>0</sub>)＝<em>a</em>e <em><sup>x</sup></em><sup>0－1</sup>－ln<em>x</em><sub>0</sub>＋ln<em>a</em>＝＋ln<em>a</em>＋<em>x</em><sub>0</sub>－1＋ln<em>a</em>≥2ln<em>a</em>－1＋2＝2ln<em>a</em>＋1&gt;1，

∴*f*(*x*)>1，∴*f*(*x*)≥1恒成立；

当0<*a*<1时，*f*(1)＝*a*＋ln*a*<*a*<1，∴*f*(1)<1，*f*(*x*)≥1不恒成立．

综上所述，*a*的取值范围是[1，＋∞)．

<strong>[例2]</strong>　已知函数<em>f</em>(<em>x</em>)＝<em>x</em>－<em>a</em>ln<em>x</em>．

(1)若曲线<em>y</em>＝<em>f</em>(<em>x</em>)＋<em>b</em>(<em>a</em>，<em>b</em>∈<strong>R</strong>)在<em>x</em>＝1处的切线方程为<em>x</em>＋<em>y</em>－3＝0，求<em>a</em>，<em>b</em>的值；

(2)求函数<em>g</em>(<em>x</em>)＝<em>f</em>(<em>x</em>)＋(<em>a</em>∈<strong>R</strong>)的极值点；

(3)设<em>h</em>(<em>x</em>)＝<em>f</em>(<em>x</em>)＋<em>a</em>e<em><sup>x</sup></em>－＋ln <em>a</em>(<em>a</em>&gt;0)，若当<em>x</em>&gt;<em>a</em>时，不等式<em>h</em>(<em>x</em>)≥0恒成立，求<em>a</em>的最小值．

解析　(1)由*f*(*x*)＝*x*－*a*ln *x*，得*y*＝*x*－*a*ln *x*＋*b*，∴*y*′＝*f*′(*x*)＝1－．

由已知可得即∴*a*＝2，*b*＝1．

(2)*g*(*x*)＝*f*(*x*)＋＝*x*－*a*ln *x*＋，

∴*g*′(*x*)＝1－－＝(*x*>0)，

当*a*＋1≤0，即*a*≤－1时，*g*′(*x*)>0，*g*(*x*)在(0，＋∞)上为增函数，无极值点．

当*a*＋1>0，即*a*>－1时，则有，当0<*x*<*a*＋1时，*g*′(*x*)<0，当*x*>*a*＋1时，*g*′(*x*)>0，

∴*g*(*x*)在(0，*a*＋1)上为减函数，在(*a*＋1，＋∞)上为增函数，

∴*x*＝*a*＋1是*g*(*x*)的极小值点，无极大值点．

综上可知，当*a*≤－1时，函数*g*(*x*)无极值点，

当*a*>－1时，函数*g*(*x*)的极小值点是*a*＋1，无极大值点．

(3)　(同构后参变分离)

<em>h</em>(<em>x</em>)＝<em>f</em>(<em>x</em>)＋<em>a</em>e<em><sup>x</sup></em>－＋ln <em>a</em>＝<em>a</em>e<em><sup>x</sup></em>－ln <em>x</em>＋ln<em>a</em>(<em>a</em>&gt;0)，

由题意知，当<em>x</em>&gt;<em>a</em>时，<em>a</em>e<em><sup>x</sup></em>－ln <em>x</em>＋ln<em>a</em>≥0恒成立，

又不等式<em>a</em>e<em><sup>x</sup></em>－ln <em>x</em>＋ln <em>a</em>≥0等价于<em>a</em>e<em><sup>x</sup></em>≥ln，即e<em><sup>x</sup></em>≥ln，即<em>x</em>e<em><sup>x</sup></em>≥ln．①

①式等价于<em>x</em>e<em><sup>x</sup></em>≥ln·eln，由<em>x</em>&gt;<em>a</em>&gt;0知，&gt;1，ln&gt;0．

令<em>φ</em>(<em>x</em>)＝<em>x</em>e<em><sup>x</sup></em>(<em>x</em>&gt;0)，则原不等式即为<em>φ</em>(<em>x</em>)≥<em>φ</em>，

又<em>φ</em>(<em>x</em>)＝<em>x</em>e<em><sup>x</sup></em>(<em>x</em>&gt;0)在(0，＋∞)上为增函数，∴原不等式等价于<em>x</em>≥ln ，②

又②式等价于e<em><sup>x</sup></em>≥，即<em>a</em>≥(<em>x</em>&gt;<em>a</em>&gt;0)，

设*F*(*x*)＝(*x*>0)，则*F*′(*x*)＝，

∴*F*(*x*)在(0，1)上为增函数，在(1，＋∞)上为减函数，又*x*>*a*>0，

∴当0<*a*<1时，*F*(*x*)在(*a，* 1)上为增函数，在(1，＋∞)上为减函数．

∴*F*(*x*)≤*F*(1)＝．要使原不等式恒成立，须使≤*a*<1，

当*a*≥1时，*F*(*x*)在(*a*，＋∞)上为减函数，*F*(*x*)<*F*(1)＝．

要使原不等式恒成立，须使*a*≥，∴当*a*≥1时，原不等式恒成立．

综上可知，*a*的取值范围是[，＋∞)，*a*的最小值为．

<strong>[例3]</strong>　已知实数<em>a</em>∈<strong>R</strong>，设函数<em>f</em>(<em>x</em>)＝ln<em>x</em>－<em>ax</em>＋1．

(1)求函数*f*(*x*)的单调区间；

(2)若*f*(*x*)≥＋1恒成立，求实数*a*的取值范围．

解析　(1)由题意得定义域为(0，＋∞)，*f*′(*x*)＝－*a*＝．

当*a*≤0时，*f*′(*x*)>0恒成立，所以函数*f*(*x*)在(0，＋∞)上单调递增；当*a*>0时，令*f*′(*x*)＝0，解得*x*＝，

所以当时，*f*′(*x*)>0，函数*f*(*x*)单调递增；当时，*f*′(*x*)<0，函数*f*(*x*)单调递减．

(2)因为*x*>0，所以*f*(*x*)≥＋1恒成立等价于*x*ln *x*≥*a*恒成立．

设*h*(*x*)＝ln *x*－，则*h*′(*x*)＝－＝，

所以函数*h*(*x*)在(0，1)上单调递减，在(1，＋∞)上单调递增，

所以<em>h</em>(<em>x</em>)<sub>min</sub>＝<em>h</em>(1)＝0．即ln <em>x</em>≥1－，所以<em>x</em>ln <em>x</em>≥<em>x</em>＝<em>x</em>－1恒成立，

问题等价于*x*－1－*a*≥0恒成立，分离参数得*a*≤恒成立．

设*t*＝∈(1，＋∞)，函数*g*(*t*)＝，则*g*′(*t*)＝1＋>0，

所以函数*g*(*t*)在(1，＋∞)上单调递增，所以*g*(*t*)>*g*(1)＝－1，

所以*a*≤－1，故实数*a*的取值范围为(－∞，－1]．

**【对点精练】**

1．已知函数<em>f</em>(<em>x</em>)＝e<em><sup>ax</sup></em>－<em>x</em>．

(1)若曲线*y*＝*f*(*x*)在点(0，*f*(0))处切线的斜率为1，求*f*(*x*)的单调区间；

(2)若不等式<em>f</em>(<em>x</em>)≥e<em><sup>ax</sup></em>ln <em>x</em>－<em>ax</em><sup>2</sup>对<em>x</em>∈(0，e]恒成立，求<em>a</em>的取值范围．

1．解析　(1)<em>f</em>′(<em>x</em>)＝<em>a</em>e<em><sup>ax</sup></em>－1，则<em>f</em>′(0)＝<em>a</em>－1＝1，即<em>a</em>＝2．

∴<em>f</em>′(<em>x</em>)＝2e<sup>2</sup><em><sup>x</sup></em>－1，令<em>f</em>′(<em>x</em>)＝0，得<em>x</em>＝－．

当*x*<－时，*f*′(*x*)<0；当*x*>－时，*f*′(*x*)>0．

故*f*(*x*)的单调递减区间为，单调递增区间为．

(2)(同构后参变分离)　由<em>f</em>(<em>x</em>)≥e<em><sup>ax</sup></em>ln <em>x</em>－<em>ax</em><sup>2</sup>，即<em>ax</em><sup>2</sup>－<em>x</em>≥e<em><sup>ax</sup></em>(ln <em>x</em>－1)，有≥，

故仅需≥即可．

设函数<em>g</em>(<em>x</em>)＝，则≥等价于<em>g</em>(e<em><sup>ax</sup></em>)≥<em>g</em>(<em>x</em>)．

∵*g*′(*x*)＝，∴当*x*∈(0，e]时，*g*′(*x*)>0，则*g*(*x*)在(0，e]上单调递增，

∴当<em>x</em>∈(0，e]时，<em>g</em>(e<em><sup>ax</sup></em>)≥<em>g</em>(<em>x</em>)等价于e<em><sup>ax</sup></em>≥<em>x</em>，即<em>a</em>≥恒成立．

设函数*h*(*x*)＝，*x*∈(0，e]，则*h*′(*x*)＝≥0，即*h*(*x*)在(0，e]上单调递增，

∴<em>h</em>(<em>x</em>)<sub>max</sub>＝<em>h</em>(e)＝，则<em>a</em>≥即可，∴<em>a</em>的取值范围为．

2．已知函数<em>f</em>(<em>x</em>)＝1＋<em>a</em>e<em><sup>x</sup></em>ln<em>x</em>．

(1)当*a*＝1时，讨论函数*f*(*x*)的单调性；

(2)若不等式<em>f</em>(<em>x</em>)≥e<em><sup>x</sup></em>(<em>x<sup>a</sup></em>－<em>x</em>)(<em>a</em>&lt;0)，对<em>x</em>∈(1，＋∞)恒成立，求实数<em>a</em>的取值范围．

2．解析　(1)<em>f</em>(<em>x</em>)的定义域为(0，＋∞)，当<em>a</em>＝1时，<em>f</em>′(<em>x</em>)＝e<em><sup>x</sup></em>，

令*g*(*x*)＝ln *x*＋，则*g*′(*x*)＝－＝，

当*x*∈(0，1)时，*g*′(*x*)<0，*g*(*x*)单调递减，当*x*∈(1，＋∞)时，*g*′(*x*)>0，*g*(*x*)单调递增，

∴当*x*＝1时，*g*(*x*)取得极小值即最小值*g*(1)＝1，

∴*f*′(*x*)>0在(0，＋∞)上恒成立，∴*f*(*x*)在(0，＋∞)上单调递增．

(2)(同构后参变分离)　不等式<em>f</em>(<em>x</em>)≥e<em><sup>x</sup></em>(<em>x<sup>a</sup></em>－<em>x</em>)⇔e<sup>－</sup><em><sup>x</sup></em>＋<em>x</em>≥<em>x<sup>a</sup></em>－<em>a</em>ln <em>x</em>⇔e<sup>－</sup><em><sup>x</sup></em>－ln e<sup>－</sup><em><sup>x</sup></em>≥<em>x<sup>a</sup></em>－ln <em>x<sup>a</sup></em>，

设<em>k</em>(<em>t</em>)＝<em>t</em>－ln <em>t</em>，即<em>k</em>(e<sup>－</sup><em><sup>x</sup></em>)≥<em>k</em>(<em>x<sup>a</sup></em>)，(\*)

∵*k*′(*t*)＝1－＝，∴当*t*∈(0，1)时，*k*′(*t*)<0，*k*(*t*)在(0，1)上单调递减；

当*t*∈(1，＋∞)时，*k*′(*t*)>0，*k*(*t*)在(1，＋∞)上单调递增，

∵<em>x</em>∈(1，＋∞)，0&lt;e<sup>－</sup><em><sup>x</sup></em>&lt;e<sup>－1</sup>&lt;1，当<em>a</em>&lt;0时，0&lt;<em>x<sup>a</sup></em>&lt;1，且<em>k</em>(<em>t</em>)在(0，1)上单调递减，

则(\*)式⇔e<sup>－</sup><em><sup>x</sup></em>≤<em>x<sup>a</sup></em>⇒－<em>a</em>≤，令<em>h</em>(<em>x</em>)＝(<em>x</em>&gt;1)，则<em>h</em>′(<em>x</em>)＝，

当*x*∈(1，e)时，*h*′(*x*)<0，*h*(*x*)单调递减；当*x*∈(e，＋∞)时，*h*′(*x*)>0，*h*(*x*)单调递增，

∴<em>h</em>(<em>x</em>)<sub>min</sub>＝<em>h</em>(e)＝e，则－<em>a</em>≤e，∴<em>a</em>≥－e，又<em>a</em>&lt;0，∴<em>a</em>的取值范围是[－e，0)．

3．已知函数<em>f</em>(<em>x</em>)＝e<sup>－</sup><em><sup>x</sup></em>－<em>ax</em>，<em>g</em>(<em>x</em>)＝ln(<em>x</em>＋<em>m</em>)＋<em>ax</em>＋1．

(1)当*a*＝－1时，求函数*f*(*x*)的最小值；

(2)若对任意的*x*∈(－*m*，＋∞)，恒有*f*(－*x*)≥*g*(*x*)成立，求实数*m*的取值范围．

3．解析　(1)当<em>a</em>＝－1时，<em>f</em>(<em>x</em>)＝e<sup>－</sup><em><sup>x</sup></em>＋<em>x</em>，则<em>f</em>′(<em>x</em>)＝－＋1．令<em>f</em>′(<em>x</em>)＝0，得<em>x</em>＝0．

当*x*＜0时，*f*′(*x*)＜0，当*x*＞0时，*f*′(*x*)＞0，

∴函数*f*(*x*)在区间(－∞，0)上单调递减，在区间(0，＋∞)上单调递增．

∴当*x*＝0时，函数*f*(*x*)取得最小值，最小值为*f*(0)＝1．

(2)由(1)得e<em><sup>x</sup></em>≥<em>x</em>＋1恒成立．<em>f</em>(－<em>x</em>)≥<em>g</em>(<em>x</em>)⇔e<em><sup>x</sup></em>＋<em>ax</em>≥ln(<em>x</em>＋<em>m</em>)＋<em>ax</em>＋1⇔e<em><sup>x</sup></em>≥ln(<em>x</em>＋<em>m</em>)＋1．

故<em>x</em>＋1≥ln(<em>x</em>＋<em>m</em>)＋1，即<em>m</em>≤e<em><sup>x</sup></em>－<em>x</em>在(－<em>m</em>，＋∞)上恒成立．

当<em>m</em>＞0时，在(－<em>m</em>，＋∞)上，e<em><sup>x</sup></em>－<em>x</em>≥1，得0＜<em>m</em>≤1；

当<em>m</em>≤0时，在 (－<em>m</em>，＋∞)上，e<em><sup>x</sup></em>－<em>x</em>＞1，<em>m</em>≤e<em><sup>x</sup></em>－<em>x</em>恒成立．于是<em>m</em>≤1．

∴实数*m*的取值范围为(－∞，1]．

