**专题27　单变量恒成立之参变分离后导函数零点可求型**

![](images/928fefea6996f955db992285d3c4d201cfe6250880b8567279cdd6ad71c21065.jpg)

**【方法总结】**

单变量恒成立之参变分离法

参变分离法是将不等式变形成一个一端是<em>f</em>(<em>a</em>)，另一端是变量表达式<em>g</em>(<em>x</em>)的不等式后，若<em>f</em>(<em>a</em>)≥<em>g</em>(<em>x</em>)在<em>x</em>∈<em>D</em>上恒成立，则<em>f</em>(<em>a</em>)≥<em>g</em>(<em>x</em>)<sub>max</sub>；若<em>f</em>(<em>a</em>)≤<em>g</em>(<em>x</em>)在<em>x</em>∈<em>D</em>上恒成立，则<em>f</em>(<em>a</em>)≤<em>g</em>(<em>x</em>)<sub>min</sub>．特别地，经常将不等式变形成一个一端是参数<em>a</em>，另一端是变量表达式<em>g</em>(<em>x</em>)的不等式后，若<em>a</em>≥<em>g</em>(<em>x</em>)在<em>x</em>∈<em>D</em>上恒成立，则<em>a</em>≥<em>g</em>(<em>x</em>)<sub>max</sub>；若<em>a</em>≤<em>g</em>(<em>x</em>)在<em>x</em>∈<em>D</em>上恒成立，则<em>a</em>≤<em>g</em>(<em>x</em>)<sub>min</sub>．

利用分离参数法来确定不等式*f*(*x*，*a*)≥0(*x*∈*D*，*a*为实参数)恒成立问题中参数取值范围的基本步骤：

(1)将参数与变量分离，化为<em>f</em><sub>1</sub>(<em>a</em>)≥<em>f</em><sub>2</sub>(<em>x</em>)或<em>f</em><sub>1</sub>(<em>a</em>)≤<em>f</em><sub>2</sub>(<em>x</em>)的形式．

(2)求<em>f</em><sub>2</sub>(<em>x</em>)在<em>x</em>∈<em>D</em>时的最大值或最小值．

(3)解不等式<em>f</em><sub>1</sub>(<em>a</em>)≥<em>f</em><sub>2</sub>(<em>x</em>)<sub>max</sub>或<em>f</em><sub>1</sub>(<em>a</em>)≤<em>f</em><sub>2</sub>(<em>x</em>)<sub>min</sub>，得到<em>a</em>的取值范围．

**【例题选讲】**

<strong>[例1]</strong>　已知<em>f</em>(<em>x</em>)＝<em>x</em>ln<em>x</em>，<em>g</em>(<em>x</em>)＝<em>x</em><sup>3</sup>＋<em>ax</em><sup>2</sup>－<em>x</em>＋2．

(1)求函数*f*(*x*)的单调区间；

(2)若对任意*x*∈(0，＋∞)，2*f*(*x*)≤*g*′(*x*)＋2恒成立，求实数*a*的取值范围．

解析　(1)∵函数*f*(*x*)＝*x*ln *x*的定义域是(0，＋∞)，∴*f*′(*x*)＝ln *x*＋1．

令*f*′(*x*)＜0，得ln *x*＋1＜0，解得0＜*x*＜，∴*f*(*x*)的单调递减区间是．

令*f*′(*x*)＞0，得ln *x*＋1＞0，解得*x*＞，∴*f*(*x*)的单调递增区间是．

综上，*f*(*x*)的单调递减区间是，单调递增区间是．

(2)∵<em>g</em>′(<em>x</em>)＝3<em>x</em><sup>2</sup>＋2<em>ax</em>－1，2<em>f</em>(<em>x</em>)≤<em>g</em>′(<em>x</em>)＋2恒成立，∴2<em>x</em>ln<em>x</em>≤3<em>x</em><sup>2</sup>＋2<em>ax</em>＋1恒成立．

∵*x*＞0，∴*a*≥ln *x*－*x*－在*x*∈(0，＋∞)上恒成立．

设*h*(*x*)＝ln *x*－*x*－(*x*＞0)，则*h*′(*x*)＝－＋＝－．

令<em>h</em>′(<em>x</em>)＝0，得<em>x</em><sub>1</sub>＝1，<em>x</em><sub>2</sub>＝－(舍去)．

当*x*∈(0，1)时，*h*′(*x*)＞0，*h*(*x*)单调递增；当*x*∈(1，＋∞)时，*h*′(*x*)＜0，*h*(*x*)单调递减．

∴当<em>x</em>＝1时，<em>h</em>(<em>x</em>)取得极大值，也是最大值，且<em>h</em>(<em>x</em>)<sub>max</sub>＝<em>h</em>(1)＝－2，

∴若<em>a</em>≥<em>h</em>(<em>x</em>)在<em>x</em>∈(0，＋∞)上恒成立，则<em>a</em>≥<em>h</em>(<em>x</em>)<sub>max</sub>＝－2，

故实数*a*的取值范围是[－2，＋∞)．

<strong>[例2]</strong>　已知函数<em>f</em>(<em>x</em>)＝ln<em>x</em>＋<em>x</em><sup>2</sup>－(<em>a</em>＋1)<em>x</em>．

(1)若曲线*y*＝*f*(*x*)在*x*＝1处的切线方程为*y*＝－2，求*f*(*x*)的单调区间；

(2)若*x*>0时，<恒成立，求实数*a*的取值范围．

解析：(1)函数*f*(*x*)的定义域为(0，＋∞)．由已知得*f*′(*x*)＝＋*ax*－(*a*＋1)，则*f*′(1)＝0．

而*f*(1)＝－－1，∴曲线*y*＝*f*(*x*)在*x*＝1处的切线方程为*y*＝－－1．∴－－1＝－2，解得*a*＝2．

∴<em>f</em>(<em>x</em>)＝ln <em>x</em>＋<em>x</em><sup>2</sup>－3<em>x</em>，<em>f</em>′(<em>x</em>)＝＋2<em>x</em>－3，由<em>f</em>′(<em>x</em>)&gt;0，得0&lt;<em>x</em>&lt;或<em>x</em>&gt;1，由<em>f</em>′(<em>x</em>)&lt;0，得&lt;<em>x</em>&lt;1，

∴*f*(*x*)的单调递增区间为和(1，＋∞)，单调递减区间为．

(2)由<，得＋*x*－(*a*＋1)<＋*x*－，即－<在区间(0，＋∞)上恒成立．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

设*h*(*x*)＝－，则*h*′(*x*)＝＋＝，由*h*′(*x*)>0，得0<*x*<，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

因而*h*(*x*)在上单调递增，由*h*′(*x*)<0，得*x*>，因而*h*(*x*)在上单调递减．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

∴*h*(*x*)的最大值为*h*()＝，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

∴>，故*a*>2－1．从而实数*a*的取值范围为．

<strong>[例3]</strong>　(2020·全国Ⅰ)已知函数<em>f</em>(<em>x</em>)＝e<em><sup>x</sup></em>＋<em>ax</em><sup>2</sup>－<em>x</em>．

(1)当*a*＝1时，讨论*f*(*x*)的单调性；

(2)当<em>x</em>≥0时，<em>f</em>(<em>x</em>)≥<em>x</em><sup>3</sup>＋1，求<em>a</em>的取值范围．

解析　(1)当<em>a</em>＝1时，<em>f</em>(<em>x</em>)＝e<em><sup>x</sup></em>＋<em>x</em><sup>2</sup>－<em>x</em>，<em>f</em>′(<em>x</em>)＝e<em><sup>x</sup></em>＋2<em>x</em>－1，

由于<em>f</em>″(<em>x</em>)＝e<em><sup>x</sup></em>＋2＞0，故<em>f</em>′(<em>x</em>)单调递增，注意到<em>f</em>′(0)＝0，

故当*x*∈(－∞，0)时，*f*′(*x*)＜0，*f*(*x*)单调递减，当*x*∈(0，＋∞)时，*f*′(*x*)＞0，*f*(*x*)单调递增．

(2)由<em>f</em>(<em>x</em>)≥<em>x</em><sup>3</sup>＋1，得e<em><sup>x</sup></em>＋<em>ax</em><sup>2</sup>－<em>x</em>≥<em>x</em><sup>3</sup>＋1，其中<em>x</em>≥0，

①当*x*＝0时，不等式为1≥1，显然成立，符合题意；

②当*x*＞0时，分离参数*a*得*a*≥－，

记*g*(*x*)＝－，*g*′(*x*)＝－，

令<em>h</em>(<em>x</em>)＝e<em><sup>x</sup></em>－<em>x</em><sup>2</sup>－<em>x</em>－1(<em>x</em>≥0)，则<em>h</em>′(<em>x</em>)＝e<em><sup>x</sup></em>－<em>x</em>－1，<em>h</em>″(<em>x</em>)＝e<em><sup>x</sup></em>－1≥0，

故*h*′(*x*)单调递增，*h*′(*x*)≥*h*′(0)＝0，故函数*h*(*x*)单调递增，*h*(*x*)≥*h*(0)＝0，

由<em>h</em>(<em>x</em>)≥0可得e<em><sup>x</sup></em>－<em>x</em><sup>2</sup>－<em>x</em>－1≥0恒成立，

故当*x*∈(0，2)时，*g*′(*x*)＞0，*g*(*x*)单调递增；当*x*∈(2，＋∞)时，*g*′(*x*)＜0，*g*(*x*)单调递减．

因此，<em>g</em>(<em>x</em>)<sub>max</sub>＝<em>g</em>(2)＝，

综上可得，实数*a*的取值范围是．

**【对点精练】**

1．已知函数<em>f</em>(<em>x</em>)＝<em>ax</em>e<em><sup>x</sup></em>－(<em>a</em>＋1)(2<em>x</em>－1)．

(1)若*a*＝1，求函数*f*(*x*)的图象在点(0，*f*(0))处的切线方程；

(2)当*x*＞0时，函数*f*(*x*)≥0恒成立，求实数*a*的取值范围．

1．解析　(1)若<em>a</em>＝1，则<em>f</em>(<em>x</em>)＝<em>x</em>e<em><sup>x</sup></em>－2(2<em>x</em>－1)．即<em>f</em>′(<em>x</em>)＝<em>x</em>e<em><sup>x</sup></em>＋e<em><sup>x</sup></em>－4，则<em>f</em>′(0)＝－3，<em>f</em>(0)＝2，

所以所求切线方程为3*x*＋*y*－2＝0．

(2)由*f*(1)≥0，得*a*≥＞0，则*f*(*x*)≥0对任意的*x*＞0恒成立可转化为≥对任意的*x*＞0恒成立．

设函数*F*(*x*)＝(*x*＞0)，则*F*′(*x*)＝－．

当0＜*x*＜1时，*F*′(*x*)＞0；当*x*＞1时，*F*′(*x*)＜0，

所以函数<em>F</em>(<em>x</em>)在(0，1)上单调递增，在(1，＋∞)上单调递减，所以<em>F</em>(<em>x</em>)<sub>max</sub>＝<em>F</em>(1)＝．

于是≥，解得*a*≥．故实数*a*的取值范围是．

2．已知函数<em>f</em>(<em>x</em>)＝e<em><sup>x</sup></em>(<em>ax</em><sup>2</sup>＋<em>x</em>＋<em>a</em>)(<em>a</em>≥0)．

(1)求函数*f*(*x*)的单调区间；

(2)若函数<em>f</em>(<em>x</em>)≤e<em><sup>x</sup></em>(<em>ax</em><sup>2</sup>＋2<em>x</em>)＋1恒成立，求实数<em>a</em>的取值范围．

2．解析　(1)函数<em>f</em>(<em>x</em>)的定义域为<strong>R</strong>，且<em>f</em>′(<em>x</em>)＝(<em>ax</em>＋<em>a</em>＋1)(<em>x</em>＋1)e<em><sup>x</sup></em>，

①当<em>a</em>＝0时，<em>f</em>′(<em>x</em>)＝e<em><sup>x</sup></em>(<em>x</em>＋1)，当<em>x</em>&gt;－1时，<em>f</em>′(<em>x</em>)&gt;0，当<em>x</em>&lt;－1时，<em>f</em>′(<em>x</em>)&lt;0，

所以函数*f*(*x*)的单调增区间为(－1，＋∞)，单调减区间为(－∞，－1)．

②当<em>a</em>&gt;0时，<em>f</em>′(<em>x</em>)＝<em>a</em>(<em>x</em>＋1)e<em><sup>x</sup></em>，则方程<em>f</em>′(<em>x</em>)＝0有两根－1，－，且－1&gt;－．

所以函数*f*(*x*)的单调增区间为和(－1，＋∞)，单调减区间为．

综上可知，当*a*>0时，函数*f*(*x*)的单调增区间为和(－1，＋∞)，单调减区间为；当*a*＝0时，函数*f*(*x*)的单调增区间为(－1，＋∞)，单调减区间为(－∞，－1)．

(2)函数<em>f</em>(<em>x</em>)≤e<em><sup>x</sup></em>(<em>ax</em><sup>2</sup>＋2<em>x</em>)＋1恒成立转化为<em>a</em>≤<em>x</em>＋在<strong>R</strong>上恒成立．

令*h*(*x*)＝*x*＋，则*h*′(*x*)＝，易知*h*(*x*)在(0，＋∞)上为增函数，在(－∞，0)上为减函数．

所以<em>h</em>(<em>x</em>)<sub>min</sub>＝<em>h</em>(0)＝1，则<em>a</em>≤1．

又由题设*a*≥0，故实数*a*的取值范围为[0，1]．

3．已知函数*f*(*x*)＝ln*x*．

(1)求函数*g*(*x*)＝*f*(*x*＋1)－*x*的最大值；

(2)若对任意<em>x</em>&gt;0，不等式<em>f</em>(<em>x</em>)≤<em>ax</em>≤<em>x</em><sup>2</sup>＋1恒成立，求实数<em>a</em>的取值范围．

3．<strong>解析</strong>　(1)∵<em>f</em>(<em>x</em>)＝ln <em>x</em>，∴<em>g</em>(<em>x</em>)＝<em>f</em>(<em>x</em>＋1)－<em>x</em>＝ln(<em>x</em>＋1)－<em>x</em>(<em>x</em>&gt;－1)，∴<em>g</em>′(<em>x</em>)＝－1＝．

当*x*∈(－1，0)时，*g*′(*x*)>0，∴*g*(*x*)在(－1，0)上单调递增；

当*x*∈(0，＋∞)时，*g*′(*x*)<0，∴*g*(*x*)在(0，＋∞)上单调递减．

∴*g*(*x*)在*x*＝0处取得最大值*g*(0)＝0．

(2)∵对任意<em>x</em>&gt;0，不等式<em>f</em>(<em>x</em>)≤<em>ax</em>≤<em>x</em><sup>2</sup>＋1恒成立，∴在<em>x</em>&gt;0上恒成立，

进一步转化为<sub>max</sub>≤<em>a</em>≤<sub>min</sub>，设<em>h</em>(<em>x</em>)＝，则<em>h</em>′(<em>x</em>)＝，

当*x*∈(1，e)时，*h*′(*x*)>0；当*x*∈(e，＋∞)时，*h*′(*x*)<0，∴*h*(*x*)在*x*＝e处取得极大值也是最大值．

∴<em>h</em>(<em>x</em>)<sub>max</sub>＝．要使<em>f</em>(<em>x</em>)≤<em>ax</em>恒成立，必须<em>a</em>≥．

另一方面，当<em>x</em>&gt;0时，<em>x</em>＋≥2，当且仅当<em>x</em>＝1时等号成立，要使<em>ax</em>≤<em>x</em><sup>2</sup>＋1恒成立，必须<em>a</em>≤2，

∴满足条件的*a*的取值范围是．

4．已知函数<em>f</em>(<em>x</em>)＝(<em>x</em>－1)e<em><sup>x</sup></em>－<em>ax</em><sup>2</sup>(e是自然对数的底数)．

(1)讨论函数*f*(*x*)的极值点的个数，并说明理由；

(2)若对任意的<em>x</em>&gt;0，<em>f</em>(<em>x</em>)＋e<em><sup>x</sup></em>≥<em>x</em><sup>3</sup>＋<em>x</em>，求实数<em>a</em>的取值范围．

4．解析　(1)<em>f</em>′(<em>x</em>)＝<em>x</em>e<em><sup>x</sup></em>－2<em>ax</em>＝<em>x</em>(e<em><sup>x</sup></em>－2<em>a</em>)．

当*a*≤0时，由*f*′(*x*)<0得*x*<0，由*f*′(*x*)>0得*x*>0，

∴*f*(*x*)在(－∞，0)上单调递减，在(0，＋∞)上单调递增，∴*f*(*x*)有1个极值点；

当0<*a*<时，由*f*′(*x*)>0得*x*<ln (2*a*)或*x*>0，由*f*′(*x*)<0得ln (2*a*)<*x*<0，

∴*f*(*x*)在(－∞，ln (2*a*))上单调递增，在(ln (2*a*)，0)上单调递减，在(0，＋∞)上单调递增，

∴*f*(*x*)有2个极值点；

当<em>a</em>＝时，由<em>f</em>′(<em>x</em>)≥0，∴<em>f</em>(<em>x</em>)在<strong>R</strong>上单调递增，∴<em>f</em>(<em>x</em>)没有极值点；

当*a*>时，由*f*′(*x*)>0得*x*<0或*x*>ln (2*a*)，由*f*′(*x*)<0得0<*x*<ln (2*a*)，∴*f*(*x*)在(－∞，0)上单调递增，在(0，ln (2*a*))上单调递减，在(ln (2*a*)，＋∞)上单调递增，∴*f*(*x*)有2个极值点．

综上，当*a*≤0时，*f*(*x*)有1个极值点；当*a*>0且*a*≠时，*f*(*x*)有2个极值点；当*a*＝时，*f*(*x*)没有极值点．

(2)由<em>f</em>(<em>x</em>)＋e<em><sup>x</sup></em>≥<em>x</em><sup>3</sup>＋<em>x</em>得<em>x</em>e<em><sup>x</sup></em>－<em>x</em><sup>3</sup>－<em>ax</em><sup>2</sup>－<em>x</em>≥0．

当<em>x</em>&gt;0时，e<em><sup>x</sup></em>－<em>x</em><sup>2</sup>－<em>ax</em>－1≥0，即<em>a</em>≤对任意的<em>x</em>&gt;0恒成立．

设*g*(*x*)＝，则*g*′(*x*)＝．

设<em>h</em>(<em>x</em>)＝e<em><sup>x</sup></em>－<em>x</em>－1，则<em>h</em>′(<em>x</em>)＝e<em><sup>x</sup></em>－1．

∵<em>x</em>&gt;0，∴<em>h</em>′(<em>x</em>)&gt;0，∴<em>h</em>(<em>x</em>)在(0，＋∞)上单调递增，∴<em>h</em>(<em>x</em>)&gt;<em>h</em>(0)＝0，即e<em><sup>x</sup></em>－<em>x</em>－1&gt;0，

∴*g*(*x*)在(0，1)上单调递减，在(1，＋∞)上单调递增，∴*g*(*x*)≥*g*(1)＝e－2，∴*a*≤e－2，

∴实数*a*的取值范围为(－∞，e－2]．

