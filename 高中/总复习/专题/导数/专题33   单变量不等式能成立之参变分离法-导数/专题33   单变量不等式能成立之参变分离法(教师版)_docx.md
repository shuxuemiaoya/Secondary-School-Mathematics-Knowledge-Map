专题33　单变量不等式能成立之参变分离法

![](images/9b4ae7365281eecfee3cf71904b55f0b70bb6cf384a16ea4cd857b9268dbfa82.jpg)

【方法总结】

单变量不等式能成立之参变分离法

参变分离法是将不等式变形成一个一端是<em>f</em>(<em>a</em>)，另一端是变量表达式<em>g</em>(<em>x</em>)的不等式后，若<em>f</em>(<em>a</em>)≥<em>g</em>(<em>x</em>)在<em>x</em>∈<em>D</em>上能成立，则<em>f</em>(<em>a</em>)≥<em>g</em>(<em>x</em>)<sub>min</sub>；若<em>f</em>(<em>a</em>)≤<em>g</em>(<em>x</em>)在<em>x</em>∈<em>D</em>上能成立，则<em>f</em>(<em>a</em>)≤<em>g</em>(<em>x</em>)<sub>max</sub>．特别地，经常将不等式变形成一个一端是参数<em>a</em>，另一端是变量表达式<em>g</em>(<em>x</em>)的不等式后，若<em>a</em>≥<em>g</em>(<em>x</em>)在<em>x</em>∈<em>D</em>上能成立，则<em>a</em>≥<em>g</em>(<em>x</em>)<sub>min</sub>；若<em>a</em>≤<em>g</em>(<em>x</em>)在<em>x</em>∈<em>D</em>上能成立，则<em>a</em>≤<em>g</em>(<em>x</em>)<sub>max</sub>．
利用分离参数法来确定不等式*f*(*x*，*a*)≥0(*x*∈*D*，*a*为实参数)能成立问题中参数取值范围的基本步骤：  
（1）将参数与变量分离，化为<em>f</em><sub>1</sub>(<em>a</em>)≥<em>f</em><sub>2</sub>(<em>x</em>)或<em>f</em><sub>1</sub>(<em>a</em>)≤<em>f</em><sub>2</sub>(<em>x</em>)的形式．  
（2）求<em>f</em><sub>2</sub>(<em>x</em>)在<em>x</em>∈<em>D</em>时的最大值或最小值．  
（3）解不等式<em>f</em><sub>1</sub>(<em>a</em>)≥<em>f</em><sub>2</sub>(<em>x</em>)<sub>min</sub>或<em>f</em><sub>1</sub>(<em>a</em>)≤<em>f</em><sub>2</sub>(<em>x</em>)<sub>max</sub>，得到<em>a</em>的取值范围．

注意　“恒成立”与“存在性”问题的求解是“互补”关系，即*f*(*x*)≥*g*(*a*)对于*x*∈*D*恒成立，应求*f*(*x*)的最小值；若存在*x*∈*D*，使得*f*(*x*)≥*g*(*a*)成立，应求*f*(*x*)的最大值．在具体问题中究竟是求最大值还是最小值，可以先联想“恒成立”是求最大值还是最小值，这样也就可以解决相应的“存在性”问题是求最大值还是最小值．特别需要关注等号是否成立问题，以免细节出错．

【例题选讲】

<strong>[例1]</strong>　已知函数<em>f</em>(<em>x</em>)＝3ln<em>x</em>－<em>x</em><sup>2</sup>＋<em>x</em>，<em>g</em>(<em>x</em>)＝3<em>x</em>＋<em>a</em>．  
（1）若*f*(*x*)与*g*(*x*)的图象相切，求*a*的值；  
（2）若∃<em>x</em><sub>0</sub>&gt;0，使<em>f</em>(<em>x</em><sub>0</sub>)&gt;<em>g</em>(<em>x</em><sub>0</sub>)成立，求参数<em>a</em>的取值范围．
解析　（1）由题意得，<em>f</em>′(<em>x</em>)＝－<em>x</em>＋1，设切点为(<em>x</em><sub>0</sub>，<em>f</em>(<em>x</em><sub>0</sub>))，则<em>k</em>＝<em>f</em>′(<em>x</em><sub>0</sub>)＝－<em>x</em><sub>0</sub>＋1＝3，
解得<em>x</em><sub>0</sub>＝1或<em>x</em><sub>0</sub>＝－3(舍)，所以切点为，代入<em>g</em>(<em>x</em>)＝3<em>x</em>＋<em>a</em>，得<em>a</em>＝－．  
（2）设<em>h</em>(<em>x</em>)＝3ln <em>x</em>－<em>x</em><sup>2</sup>－2<em>x</em>，∃<em>x</em><sub>0</sub>&gt;0，使<em>f</em>(<em>x</em><sub>0</sub>)&gt;<em>g</em>(<em>x</em><sub>0</sub>)成立，等价于∃<em>x</em>&gt;0，使<em>h</em>(<em>x</em>)＝3ln <em>x</em>－<em>x</em><sup>2</sup>－2<em>x</em>&gt;<em>a</em>成立，

等价于<em>a</em>&lt;<em>h</em>(<em>x</em>)<sub>max</sub>(<em>x</em>&gt;0)．
因为*h*′(*x*)＝－*x*－2＝＝－，令得0<*x*<1；令得*x*>1．
所以函数<em>h</em>(<em>x</em>)＝3ln <em>x</em>－<em>x</em><sup>2</sup>－2<em>x</em>在(0，1)上单调递增，在(1，＋∞)上单调递减，
所以<em>h</em>(<em>x</em>)<sub>max</sub>＝<em>h</em>（1）＝－，即<em>a</em>&lt;－，因此参数<em>a</em>的取值范围为．

<strong>[例2]</strong>　已知函数<em>f</em>(<em>x</em>)＝<em>ax</em>－e<em><sup>x</sup></em>(<em>a</em>∈<strong>R</strong>)，<em>g</em>(<em>x</em>)＝．  
（1）求函数*f*(*x*)的单调区间；  
（2）∃<em>x</em>∈(0，＋∞)，使不等式<em>f</em>(<em>x</em>)－<em>g</em>(<em>x</em>)＋e<em><sup>x</sup></em>≤0成立，求<em>a</em>的取值范围．
解析　（1）因为<em>f</em>′(<em>x</em>)＝<em>a</em>－e<em><sup>x</sup></em>，<em>x</em>∈<strong>R</strong>．
当<em>a</em>≤0时，<em>f</em>′(<em>x</em>)&lt;0，<em>f</em>(<em>x</em>)在<strong>R</strong>上单调递减；当<em>a</em>&gt;0时，令<em>f</em>′(<em>x</em>)＝0，得<em>x</em>＝ln <em>a</em>．
由*f*′(*x*)>0，得*f*(*x*)的单调递增区间为(－∞，ln *a*)；由*f*′(*x*)<0，得*f*(*x*)的单调递减区间为(ln *a*，＋∞)．
综上所述，当*a*≤0时，*f*(*x*)的单调递减区间为(－∞，＋∞)，无单调递增区间；
当*a*>0时，*f*(*x*)的单调递增区间为(－∞，ln *a*)，单调递减区间为(ln *a*，＋∞)．  
（2）因为∃<em>x</em>∈(0，＋∞)，使不等式<em>f</em>(<em>x</em>)－<em>g</em>(<em>x</em>)＋e<em><sup>x</sup></em>≤0成立，所以<em>ax</em>≤，即<em>a</em>≤．
设<em>h</em>(<em>x</em>)＝，则问题转化为<em>a</em>≤<sub>max</sub>．由<em>h</em>′(<em>x</em>)＝，令<em>h</em>′(<em>x</em>)＝0，得<em>x</em>＝．
当*x*∈(0，)时，*h*′(*x*)>0，当*x*∈(，＋∞)时，*h*′(*x*)<0，
所以*h*(*x*)在(0，)上单调递增，在(，＋∞)上单调递减．
当*x*＝时，函数*h*(*x*)有极大值，即最大值，为，所以*a*≤．
故*a*的取值范围是．

<strong>[例3]</strong>　已知<em>a</em>为实数，函数<em>f</em>(<em>x</em>)＝<em>a</em>ln<em>x</em>＋<em>x</em><sup>2</sup>－4<em>x</em>．  
（1）若*x*＝3是函数*f*(*x*)的一个极值点，求实数*a*的值；  
（2）设<em>g</em>(<em>x</em>)＝(<em>a</em>－2)<em>x</em>，若存在<em>x</em><sub>0</sub>∈[，e]，使得<em>f</em>(<em>x</em><sub>0</sub>)≤<em>g</em>(<em>x</em><sub>0</sub>)成立，求实数<em>a</em>的取值范围．
解析　（1）函数*f*(*x*)的定义域为(0，＋∞)，*f*′(*x*)＝＋2*x*－4＝．
∵*x*＝3是函数*f*(*x*)的一个极值点，∴*f*′（3）＝0，解得*a*＝－6．
经检验，当*a*＝－6时，*x*＝3是函数*f*(*x*)的一个极小值点，符合题意，故*a*＝－6．  
（2）由<em>f</em>(<em>x</em><sub>0</sub>)≤<em>g</em>(<em>x</em><sub>0</sub>)，得(<em>x</em><sub>0</sub>－ln <em>x</em><sub>0</sub>)<em>a</em>≥<em>x</em>－2<em>x</em><sub>0</sub>，

记*F*(*x*)＝*x*－ln *x*(*x*>0)，则*F*′(*x*)＝(*x*>0)，
∴当0<*x*<1时，*F*′(*x*)<0，*F*(*x*)单调递减．当*x*>1时，*F*′(*x*)>0，*F*(*x*)单调递增．
∴*F*(*x*)>*F*（1）＝1>0，∴*a*≥．记*G*(*x*)＝，*x*∈[，e]，
则*G*′(*x*)＝＝．
∵*x*∈[，e]，∴2－2ln *x*＝2(1－ln *x*)≥0，∴*x*－2ln *x*＋2>0，
∴当*x*∈时，*G*′(*x*)<0，*G*(*x*)单调递减；当*x*∈(1，e)时，*G*′(*x*)>0，*G*(*x*)单调递增．
∴<em>G</em>(<em>x</em>)<sub>min</sub>＝<em>G</em>（1）＝－1，∴<em>a</em>≥<em>G</em>(<em>x</em>)<sub>min</sub>＝－1，故实数<em>a</em>的取值范围为[－1，＋∞)．

<strong>[例4]</strong>　已知函数<em>f</em>(<em>x</em>)＝ln(1＋<em>x</em>)－<em>a</em>sin<em>x</em>，<em>a</em>∈<strong>R</strong>．  
（1）若*y*＝*f*(*x*)在点(0，0)处的切线为*x*－3*y*＝0，求*a*的值；  
（2）若存在*x*∈[1，2]，使得*f*(*x*)≥2*a*，求实数*a*的取值范围．
解析　（1）*f*′(*x*)＝－*a*cos *x*，则*f*′（0）＝1－*a*＝，所以*a*＝．  
（2）将不等式转化为存在*x*∈[1，2]，使得*a*≤．
令函数*g*(*x*)＝，则*g*′(*x*)＝，
令函数*h*(*x*)＝2＋sin *x*－(1＋*x*)cos *x*ln(1＋*x*)，*x*∈[1，2]，
当*x*∈时，*h*(*x*)>0；当*x*∈时，*h*(*x*)>2＋sin *x*－(1＋*x*)ln(1＋*x*)，
令函数*φ*(*x*)＝2＋sin *x*－(1＋*x*)ln(1＋*x*)，则*φ*′(*x*)＝cos *x*－ln(1＋*x*)－1<0，
故*φ*(*x*)≥*φ*＝3－ln>3－>0，则当*x*∈时，*h*(*x*)>*φ*(*x*)>0，
故函数<em>g</em>(<em>x</em>)在[1，2]上单调递增，<em>g</em>(<em>x</em>)<sub>max</sub>＝<em>g</em>（2）＝，
则当*a*≤时，存在*x*∈[1，2]，使得*f*(*x*)≥2*a*．
所以，实数*a*的取值范围是．

<strong>[例5]</strong>　已知函数<em>f</em>(<em>x</em>)＝e<em><sup>x</sup></em>(2<em>x</em>－1)－<em>ax</em>＋<em>a</em>(<em>a</em>∈<strong>R</strong>)，e为自然对数的底数．  
（1）当*a*＝1时，求函数*f*(*x*)的单调区间；  
（2）①若存在实数*x*，满足*f*(*x*)<0，求实数*a*的取值范围；
②若有且只有唯一整数<em>x</em><sub>0</sub>，满足<em>f</em>(<em>x</em><sub>0</sub>)&lt;0，求实数<em>a</em>的取值范围．
解析　（1）当<em>a</em>＝1时，<em>f</em>(<em>x</em>)＝e<em><sup>x</sup></em>(2<em>x</em>－1)－<em>x</em>＋1，<em>f</em>′(<em>x</em>)＝e<em><sup>x</sup></em>(2<em>x</em>＋1)－1，<em>f</em>′（0）＝0，<em>f</em>″(<em>x</em>)＝e<em><sup>x</sup></em>(2<em>x</em>＋3)，
由*f*″(*x*)＝0，得*x*＝－，当*x*<－时，*f*″(*x*)<0，*f*′(*x*)单调递减；当*x*>－时，*f*″(*x*)>0，*f*′(*x*)单调递增．

且当*x*<－时，*f*′(*x*)<0，即当*x*<0时，*f*′(*x*)<0，*f*(*x*)单调递减；当*x*>0时，*f*′(*x*)>0，*f*(*x*)单调递增．
所以*f*(*x*)的单调减区间为(－∞，0)，单调增区间为(0，＋∞)．  
（2）①由<em>f</em>(<em>x</em>)&lt;0，得e<em><sup>x</sup></em>(2<em>x</em>－1)&lt;<em>a</em>(<em>x</em>－1)．
当*x*＝1时，不等式显然不成立；当*x*>1时，*a*>；当*x*<1时，*a*<．

记*g*(*x*)＝，*g*′(*x*)＝＝，
所以*g*(*x*)在区间(－∞，0)和上为增函数，在(0,1)和上为减函数．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
所以当*x*>1时，*a*>*g*＝4；当*x*<1时，*a*<*g*（0）＝1．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
综上所述，实数*a*的取值范围为(－∞，1)∪(4，＋∞)．

②由①知，当<em>a</em>&lt;1时，<em>x</em><sub>0</sub>∈(－∞，1)，由<em>f</em>(<em>x</em><sub>0</sub>)&lt;0，得<em>g</em>(<em>x</em><sub>0</sub>)&gt;<em>a</em>，
又*g*(*x*)在区间(－∞，0)上单调递增，在(0,1)上单调递减，且*g*（0）＝1>*a*，
所以*g*(－1)≤*a*，即*a*≥，所以≤*a*<1．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
当<em>a</em>&gt;4时，<em>x</em><sub>0</sub>∈(1，＋∞)，由<em>f</em>(<em>x</em><sub>0</sub>)&lt;0，得<em>g</em>(<em>x</em><sub>0</sub>)&lt;<em>a</em>，
又*g*(*x*)在区间上单调递减，在上单调递增，且*g*＝4e<*a*，
所以解得3e<sup>2</sup>&lt;<em>a</em>≤．
综上所述，实数*a*的取值范围为∪．

<strong>[例6]</strong>　已知函数<em>f</em>(<em>x</em>)＝<em>a</em>(<em>x</em>－1)，<em>g</em>(<em>x</em>)＝(<em>ax</em>－1)·e<em><sup>x</sup></em>，<em>a</em>∈<strong>R</strong>．  
（1）求证：存在唯一实数*a*，使得直线*y*＝*f*(*x*)和曲线*y*＝*g*(*x*)相切；  
（2）若不等式*f*(*x*)＞*g*(*x*)有且只有两个整数解，求*a*的取值范围．
解析　（1）<em>f</em>′(<em>x</em>)＝<em>a</em>，<em>g</em>′(<em>x</em>)＝(<em>ax</em>＋<em>a</em>－1)e<em><sup>x</sup></em>．
设直线<em>y</em>＝<em>f</em>(<em>x</em>)和曲线<em>y</em>＝<em>g</em>(<em>x</em>)的切点的坐标为(<em>x</em><sub>0</sub>，<em>y</em><sub>0</sub>)，则<em>y</em><sub>0</sub>＝<em>a</em>(<em>x</em><sub>0</sub>－1)＝(<em>ax</em><sub>0</sub>－1)e<em><sup>x</sup></em><sup>0</sup>，
得<em>a</em>(<em>x</em><sub>0</sub>e<em><sup>x</sup></em><sup>0</sup>－<em>x</em><sub>0</sub>＋1)＝e<em><sup>x</sup></em><sup>0</sup>，①
又因为直线<em>y</em>＝<em>f</em>(<em>x</em>)和曲线<em>y</em>＝<em>g</em>(<em>x</em>)相切，所以<em>a</em>＝<em>g</em>′(<em>x</em><sub>0</sub>)＝(<em>ax</em><sub>0</sub>＋<em>a</em>－1)e<em><sup>x</sup></em><sup>0</sup>，
整理得<em>a</em>(<em>x</em><sub>0</sub>e<em><sup>x</sup></em><sup>0</sup>＋e<em><sup>x</sup></em><sup>0</sup>－1)＝e<em><sup>x</sup></em><sup>0</sup>，②

结合①②得<em>x</em><sub>0</sub>e<em><sup>x</sup></em><sup>0</sup>－<em>x</em><sub>0</sub>＋1＝<em>x</em><sub>0</sub>e<em><sup>x</sup></em><sup>0</sup>＋e<em><sup>x</sup></em><sup>0</sup>－1，即e<em><sup>x</sup></em><sup>0</sup>＋<em>x</em><sub>0</sub>－2＝0，令<em>h</em>(<em>x</em>)＝e<em><sup>x</sup></em>＋<em>x</em>－2，
则<em>h</em>′(<em>x</em>)＝e<em><sup>x</sup></em>＋1＞0，所以<em>h</em>(<em>x</em>)在<strong>R</strong>上单调递增．
又因为<em>h</em>（0）＝－1＜0，<em>h</em>（1）＝e－1＞0，所以存在唯一实数<em>x</em><sub>0</sub>，使得e<em><sup>x</sup></em><sup>0</sup>＋<em>x</em><sub>0</sub>－2＝0，且<em>x</em><sub>0</sub>∈(0，1)，
所以存在唯一实数*a*，使①②两式成立，故存在唯一实数*a*，使得直线*y*＝*f*(*x*)与曲线*y*＝*g*(*x*)相切．  
（2）令<em>f</em>(<em>x</em>)＞<em>g</em>(<em>x</em>)，即<em>a</em>(<em>x</em>－1)＞(<em>ax</em>－1)e<em><sup>x</sup></em>，所以<em>ax</em>e<em><sup>x</sup></em>－<em>ax</em>＋<em>a</em>＜e<em><sup>x</sup></em>，所以<em>a</em>＜1，
令*m*(*x*)＝*x*－，则*m*′(*x*)＝，
由（1）可得<em>m</em>(<em>x</em>)在(－∞，<em>x</em><sub>0</sub>)上单调递减，在(<em>x</em><sub>0</sub>，＋∞)上单调递增，且<em>x</em><sub>0</sub>∈(0，1)，
故当<em>x</em>≤0时，<em>m</em>(<em>x</em>)≥<em>m</em>（0）＝1，当<em>x</em>≥1时，<em>m</em>(<em>x</em>)≥<em>m</em>（1）＝1，所以当<em>x</em>∈<strong>Z</strong>时，<em>m</em>(<em>x</em>)≥1恒成立．

①当*a*≤0时，*am*(*x*)＜1恒成立，此时有无数个整数解，舍去；
②当0＜*a*＜1时，*m*(*x*)＜，因为＞1，*m*（0）＝*m*（1）＝1，
所以两个整数解分别为0，1，即解得*a*≥，即*a*∈；
③当<em>a</em>≥1时，<em>m</em>(<em>x</em>)＜，因为≤1，<em>m</em>(<em>x</em>)在<em>x</em>∈<strong>Z</strong>时大于或等于1，所以<em>m</em>(<em>x</em>)＜无整数解，舍去．
综上所述，*a*的取值范围为．

【对点精练】

1．已知函数<em>f</em>(<em>x</em>)＝<em>ax</em>－(2<em>a</em>＋1)ln<em>x</em>－，<em>g</em>(<em>x</em>)＝－2<em>a</em>ln<em>x</em>－，其中<em>a</em>∈<strong>R</strong>．  
（1）当*a*>0时，求*f*(*x*)的单调区间；  
（2）若存在<em>x</em>∈[，e<sup>2</sup> ] ，使得不等式<em>f</em>(<em>x</em>)≥<em>g</em>(<em>x</em>)成立，求实数<em>a</em>的取值范围．

1．解析　（1）函数*f*(*x*)的定义域为(0，＋∞)，

*f*′(*x*)＝*a*－＋＝＝．
当*a*>0时，令*f*′(*x*)＝0，可得*x*＝>0或*x*＝2．

①当＝2，即*a*＝时，对任意的*x*>0，*f*′(*x*)≥0，
此时，函数*f*(*x*)的单调递增区间为(0，＋∞)，无单调递减区间．

②当0<<2，即*a*>时，令*f*′(*x*)>0，得0<*x*<或*x*>2；令*f*′(*x*)<0，得<*x*<2．
此时，函数*f*(*x*)的单调递增区间为和(2，＋∞)，单调递减区间为．

③当>2，即0<*a*<时，令*f*′(*x*)>0，得0<*x*<2或*x*>；令*f*′(*x*)<0，得2<*x*<．
此时，函数*f*(*x*)的单调递增区间为(0，2)和，单调递减区间为．  
（2）由<em>f</em>(<em>x</em>)≥<em>g</em>(<em>x</em>)，可得<em>ax</em>－ln <em>x</em>≥0，即<em>a</em>≥，其中<em>x</em>∈[，e<sup>2</sup> ]．

构造函数<em>h</em>(<em>x</em>)＝，<em>x</em>∈[，e<sup>2</sup> ]，则<em>a</em>≥<em>h</em>(<em>x</em>)<sub>min</sub>，

<em>h</em>′(<em>x</em>)＝，令<em>h</em>′(<em>x</em>)＝0，得<em>x</em>＝e∈[，e<sup>2</sup> ]．当≤<em>x</em>&lt;e时，<em>h</em>′(<em>x</em>)&gt;0；当e&lt;<em>x</em>≤e<sup>2</sup>时，<em>h</em>′(<em>x</em>)&lt;0．
∴函数<em>h</em>(<em>x</em>)在[，e<sup>2</sup> ]上单调递增，在(e，e<sup>2</sup>]上单调递减．
∴函数<em>h</em>(<em>x</em>)在<em>x</em>＝或<em>x</em>＝e<sup>2</sup>处取得最小值．
∵<em>h</em>＝－e，<em>h</em>(e<sup>2</sup>)＝，∴<em>h</em>&lt;<em>h</em>(e)，∴<em>h</em>(<em>x</em>)<sub>min</sub>＝<em>h</em>＝－e，∴<em>a</em>≥－e．
因此，实数*a*的取值范围是[－e，＋∞)．

2．已知函数*f*(*x*)＝*x*ln*x*(*x*>0)．  
（1）求函数*f*(*x*)的极值；  
（2）若存在*x*∈(0，＋∞)，使得*f*(*x*)≤成立，求实数*m*的最小值．

2．解析　（1）由*f*(*x*)＝*x*ln *x*，得*f*′(*x*)＝1＋ln *x*，令*f*′(*x*)>0，得*x*>；令*f*′(*x*)<0，得0<*x*<．
所以*f*(*x*)在上单调递减，在上单调递增．
所以*f*(*x*)在*x*＝处取得极小值，且为*f* ＝－，无极大值．  
（2）由<em>f</em>(<em>x</em>)≤，得<em>m</em>≥．问题转化为<em>m</em>≥<sub>min</sub>．
令*g*(*x*)＝＝2ln *x*＋*x*＋(*x*>0)．则*g*′(*x*)＝＋1－＝＝．
由*g*′(*x*)>0，得*x*>1；由*g*′(*x*)<0，得0<*x*<1．所以*g*(*x*)在(0，1)上单调递减，在(1，＋∞)上单调递增．
所以<em>g</em>(<em>x</em>)<sub>min</sub>＝<em>g</em>（1）＝4，则<em>m</em>≥4．故<em>m</em>的最小值为4．

3．已知函数<em>f</em>(<em>x</em>)＝<em>x</em><sup>2</sup>－(2<em>a</em>＋1)<em>x</em>＋<em>a</em>ln<em>x</em>(<em>a</em>∈<strong>R</strong>)．  
（1）若*f*(*x*)在区间[1，2]上是单调函数，求实数*a*的取值范围；  
（2）函数<em>g</em>(<em>x</em>)＝(1－<em>a</em>)<em>x</em>，若∃<em>x</em><sub>0</sub>∈[1，e]使得<em>f</em>(<em>x</em><sub>0</sub>)≥<em>g</em>(<em>x</em><sub>0</sub>)成立，求实数<em>a</em>的取值范围．

3．解析　（1）*f*′(*x*)＝，当导函数*f*′(*x*)的零点*x*＝*a*落在区间(1，2)内时，

函数*f*(*x*)在区间[1，2]上就不是单调函数，即*a*∉(1，2)，
所以实数*a*的取值范围是(－∞，1]∪[2，＋∞)．  
（2）由题意知，不等式<em>f</em>(<em>x</em>)≥<em>g</em>(<em>x</em>)在区间[1，e]上有解，即<em>x</em><sup>2</sup>－2<em>x</em>＋<em>a</em>(ln <em>x</em>－<em>x</em>)≥0在区间[1，e]上有解．
因为当*x*∈[1，e]时，ln *x*≤1≤*x*(不同时取等号)，*x*－ln *x*>0，所以*a*≤在区间[1，e]上有解．
令*h*(*x*)＝，则*h*′(*x*)＝．
因为*x*∈[1，e]，所以*x*＋2>2≥2ln *x*，所以*h*′(*x*)≥0，*h*(*x*)在[1，e]上单调递增，
所以<em>x</em>∈[1，e]时，<em>h</em>(<em>x</em>)<sub>max</sub>＝<em>h</em>(e)＝，所以<em>a</em>≤，
所以实数*a*的取值范围是．

4．已知函数<em>f</em>(<em>x</em>)＝<em>a</em>＋<em>b</em>ln<em>x</em>(其中<em>a</em>，<em>b</em>∈<strong>R</strong>)．  
（1）当*b*＝－4时，若*f*(*x*)在其定义域内为单调函数，求*a*的取值范围；  
（2）当*a*＝－1时，是否存在实数*b*，使得当*x*∈时，不等式*f*(*x*)>0恒成立，如果存在，求*b*的取值范围，如果不存在，请说明理由．

4．解析　（1）函数*f*(*x*)的定义域是(0，＋∞)，当*b*＝－4时，*f*′(*x*)＝．
若<em>f</em>(<em>x</em>)在其定义域内单调递增，则<em>a</em>≥＝．∵<sub>max</sub>＝1，∴<em>a</em>≥1；
若*f*(*x*)在其定义域内单调递减，则*a*≤＝，
∵<sub>min</sub>在<em>x</em>＋→＋∞时取得，即→0．∴<em>a</em>≤0．综上，<em>a</em>≤0或<em>a</em>≥1．  
（2）<em>f</em>(<em>x</em>)＝－＋<em>b</em>ln <em>x</em>&gt;0在<em>x</em>∈[e，e<sup>2</sup>]上恒成立，
令<em>y</em>＝ln <em>x</em>－，<em>x</em>∈[e，e<sup>2</sup>]，<em>y</em>′＝＋&gt;0，函数<em>y</em>＝ln <em>x</em>－在<em>x</em>∈[e，e<sup>2</sup>]上单调递增，
故当<em>x</em>＝e时，<em>y</em>取最小值1－&gt;0，故<em>y</em>＝ln <em>x</em>－&gt;0在<em>x</em>∈[e，e<sup>2</sup>]上恒成立，
故问题转化为<em>b</em>&gt;在<em>x</em>∈[e，e<sup>2</sup>]上恒成立，
令<em>h</em>(<em>x</em>)＝，<em>x</em>∈[e，e<sup>2</sup>]，<em>h</em>′(<em>x</em>)＝，令<em>m</em>(<em>x</em>)＝ln <em>x</em>－－1，<em>x</em>∈[e，e<sup>2</sup>]，<em>m</em>′(<em>x</em>)＝＋&gt;0，

而<em>m</em>(e)&lt;0，<em>m</em>(e<sup>2</sup>)&gt;0，故存在<em>x</em><sub>0</sub>∈[e，e<sup>2</sup>]，使得<em>h</em>(<em>x</em>)在[e，<em>x</em><sub>0</sub>)上单调递减，在(<em>x</em><sub>0</sub>，e<sup>2</sup>]上单调递增，
∴<em>h</em>(<em>x</em>)<sub>max</sub>＝<em>h</em>(e<sup>2</sup>)或<em>h</em>(e)，∵<em>h</em>(e<sup>2</sup>)＝&lt;<em>h</em>(e)＝，∴<em>b</em>&gt;．

综上，存在*b*满足题意，此时*b*∈．

5．已知函数*f*(*x*)＝，其中*a*为实数．  
（1）当*a*＝2时，求曲线*y*＝*f*(*x*)在点(2，*f*（2）)处的切线方程；  
（2）是否存在实数*a*，使得对任意*x*∈(0，1)∪(1，＋∞)，*f*(*x*)＞恒成立？若不存在，请说明理由，若存在，求出*a*的值并加以证明．

5．解析　（1）当*a*＝2时，*f*(*x*)＝，*f*′(*x*)＝，*f*′（2）＝，又*f*（2）＝0，
所以曲线*y*＝*f*(*x*)在点(2，*f*（2）)处的切线方程为*y*＝(*x*－2)．  
（2）①当0＜*x*＜1时，ln *x*＜0，则＞⇔*a*＞*x*－ln *x*，
令*g*(*x*)＝*x*－ln *x*，则*g*′(*x*)＝，再令*h*(*x*)＝2－2－ln *x*，则*h*′(*x*)＝－＝＜0，
故当0＜*x*＜1时，*h*′(*x*)＜0，所以*h*(*x*)在(0，1)上单调递减，所以当0＜*x*＜1时，*h*(*x*)＞*h*（1）＝0，
所以*g*′(*x*)＝＞0，所以*g*(*x*)在(0，1)上单调递增，*g*(*x*)＜*g*（1）＝1，所以*a*≥1．

②当*x*＞1时，ln *x*＞0，则＞ ⇔*a*＜*x*－ln *x*．
由①知当*x*＞1时，*h*′(*x*)＞0，*h*(*x*)在(1，＋∞)上单调递增，当*x*＞1时，*h*(*x*)＞*h*（1）＝0，
所以*g*′(*x*)＝＞0，所以*g*(*x*)在(1，＋∞)上单调递增，所以*g*(*x*)＞*g*（1）＝1，所以*a*≤1．
综合①②得：*a*＝1．

6．已知函数<em>f</em>(<em>x</em>)＝ln<em>a</em><sup>2</sup><em>x</em>－2＋<em>a</em>ln<em>a</em>．  
（1）求证：<em>f</em>(<em>x</em>)≤<em>a</em><sup>2</sup>－3；  
（2）是否存在实数*k*，使得只有唯一的正整数*a*，对于*x*∈(0，＋∞)恒有：*f*(*x*)≤e*a*＋*k*，若存在，请求出*k*的范围以及正整数*a*的值；若不存在请说明理由．(下表的近似值供参考)

<table><tr><td><p>ln 2</p></td><td><p>ln 3</p></td><td><p>ln 4</p></td><td><p>ln 5</p></td><td><p>ln 6</p></td><td><p>ln 7</p></td><td><p>ln 8</p></td><td><p>ln 9</p></td></tr><tr><td><p>0．69</p></td><td><p>1．10</p></td><td><p>1．38</p></td><td><p>1．61</p></td><td><p>1．79</p></td><td><p>1．95</p></td><td><p>2．07</p></td><td><p>2．20</p></td></tr></table>

6．解析　（1）*f*′(*x*)＝－＝，当*x*<时，*f*′(*x*)>0；当*x*>时，*f*′(*x*)<0，
则函数*f*(*x*)在上单调递增，在上单调递减，所以*f*(*x*)≤*f*＝(*a*＋1)ln *a*－2．

下证：(<em>a</em>＋1)ln <em>a</em>－2≤<em>a</em><sup>2</sup>－3，

上式等价于证明ln *a*≤*a*－1．设函数*h*(*a*)＝*a*－1－ln *a*，
则*h*′(*a*)＝1－，所以函数*h*(*a*)在(0，1)上单调递减，在(1，＋∞)上单调递增，
所以<em>h</em>(<em>a</em>)＝<em>a</em>－1－ln <em>a</em>≥<em>h</em>（1）＝0，则ln <em>a</em>≤<em>a</em>－1，即<em>f</em>(<em>x</em>)≤<em>a</em><sup>2</sup>－3．  
（2）由（1）可知<em>f</em>(<em>x</em>)<sub>max</sub>＝(<em>a</em>＋1)ln <em>a</em>－2，
所以不等式(*a*＋1)ln *a*－2≤e*a*＋*k*只有唯一的正整数解，则*k*≥(*a*＋1)ln *a*－e*a*－2．
设函数*g*(*a*)＝(*a*＋1)ln *a*－e*a*－2，则*g*′(*a*)＝ln *a*＋－e，*g*′＝0，*g*′（1）＝2－e<0．
令函数*u*(*a*)＝ln *a*＋－e，则*u*′(*a*)＝－＝，
所以函数*u*(*a*)在(0，1)上单调递减，在(1，＋∞)上单调递增．
又<em>u</em>（4）&lt;0，<em>u</em>（5）&gt;0，故存在<em>a</em><sub>0</sub>∈(4，5)满足<em>u</em>(<em>a</em><sub>0</sub>)＝0，
所以函数<em>g</em>(<em>a</em>)在上单调递增，在上单调递减，(<em>a</em><sub>0</sub>，＋∞)上单调递增．

*g*（3）＝4ln 3－3e－2，*g*（4）＝5ln 4－4e－2，*g*（5）＝6ln 5－5e－2，*g*（3）>*g*（5）>*g*（4），
所以*k*∈[5ln 4－4e－2，6ln 5－5e－2]，此时*a*＝4．

7．已知函数*f*(*x*)＝*x*ln*x*，*g*(*x*)＝，直线l：*y*＝(*k*－3)*x*－*k*＋2．  
（1）曲线*y*＝*f*(*x*)在*x*＝e处的切线与直线l平行，求实数*k*的值；  
（2）若至少存在一个<em>x</em><sub>0</sub>∈[1，e]，使<em>f</em>(<em>x</em><sub>0</sub>)＜<em>g</em>(<em>x</em><sub>0</sub>)成立，求实数<em>a</em>的取值范围；  
（3）设<em>k</em>∈<strong>Z</strong>，当<em>x</em>＞1时，函数<em>f</em>(<em>x</em>)的图象恒在直线l的上方，求<em>k</em>的最大值．

7．解析　（1）由已知得*f*′(*x*)＝ln *x*＋1，且*f*′(e)＝ln e＋1＝2＝*k*－3，解得*k*＝5．  
（2）因为至少存在一个<em>x</em><sub>0</sub>∈[1，e]，使<em>f</em>(<em>x</em><sub>0</sub>)＜<em>g</em>(<em>x</em><sub>0</sub>)成立，
所以至少存在一个<em>x</em><sub>0</sub>∈[1，e]，使<em>x</em><sub>0</sub>ln <em>x</em><sub>0</sub>＜成立，即至少存在一个<em>x</em><sub>0</sub>∈[1，e]，使<em>a</em>＞成立．
令*h*(*x*)＝，当*x*∈[1，e]时，*h*′(*x*)＝≥0恒成立，因此*h*(*x*)＝在[1，e]上单调递增．
故当<em>x</em>＝1时，<em>h</em>(<em>x</em>)<sub>min</sub>＝0，故实数<em>a</em>的取值范围为(0，＋∞)．  
（3）由已知得，*x*ln *x*＞(*k*－3)*x*－*k*＋2在(1，＋∞)上恒成立，即*k*＜在(1，＋∞)上恒成立，
令*F*(*x*)＝，则*F*′(*x*)＝，
令*m*(*x*)＝*x*－ln *x*－2，则*m*′(*x*)＝1－＝＞0在(1，＋∞)上恒成立，
所以*m*(*x*)在(1，＋∞)上单调递增，且*m*（3）＝1－ln 3＜0，*m*（4）＝2－ln 4＞0，
所以在(1，＋∞)上存在唯一实数<em>x</em><sub>0</sub>(<em>x</em><sub>0</sub>∈(3，4))使<em>m</em>(<em>x</em><sub>0</sub>)＝0，即<em>x</em><sub>0</sub>－ln <em>x</em><sub>0</sub>－2＝0．
当1＜<em>x</em>＜<em>x</em><sub>0</sub>时，<em>m</em>(<em>x</em>)＜0，即<em>F</em>′(<em>x</em>)＜0，当<em>x</em>＞<em>x</em><sub>0</sub>时，<em>m</em>(<em>x</em>)＞0，即<em>F</em>′(<em>x</em>)＞0，
所以<em>F</em>(<em>x</em>)在(1，<em>x</em><sub>0</sub>)上单调递减，在(<em>x</em><sub>0</sub>，＋∞)上单调递增，
故<em>F</em>(<em>x</em>)<sub>min</sub>＝<em>F</em>(<em>x</em><sub>0</sub>)＝＝＝<em>x</em><sub>0</sub>＋2∈(5，6)．
故<em>k</em>＜<em>x</em><sub>0</sub>＋2(<em>k</em>∈<strong>Z</strong>)，所以<em>k</em>的最大值为5．

