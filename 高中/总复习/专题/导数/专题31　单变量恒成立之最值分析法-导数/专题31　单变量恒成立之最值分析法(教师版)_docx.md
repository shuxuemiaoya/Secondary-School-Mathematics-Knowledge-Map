专题31　单变量恒成立之最值分析法

![](images/825b634ec44ad61d1ada59b38da5327cc3e92c1ada5bc654495f9f204c901dc7.jpg)

【方法总结】

单变量恒成立之最值分析法

遇到<em>f</em>(<em>x</em>)≥<em>g</em>(<em>x</em>)型的不等式恒成立问题时，一般采用作差法，构造“左减右”的函数<em>h</em>(<em>x</em>)＝<em>f</em>(<em>x</em>)－<em>g</em>(<em>x</em>)或“右减左”的函数<em>u</em>(<em>x</em>)＝<em>g</em>(<em>x</em>)－<em>f</em>(<em>x</em>)，进而只需满足<em>h</em>(<em>x</em>)<sub>min</sub>≥0或<em>u</em>(<em>x</em>)<sub>max</sub>≤0，将比较法的思想融入函数中，转化为求解函数最值的问题，适用范围较广，但是往往需要对参数进行分类讨论．

【例题选讲】

<strong>[例1]</strong>　已知函数<em>f</em>(<em>x</em>)＝e<em><sup>x</sup></em>(e<em><sup>x</sup></em>－<em>a</em>)－<em>a</em><sup>2</sup><em>x</em>．  
（1）讨论*f*(*x*)的单调性；  
（2）若*f*(*x*)≥0恒成立，求*a*的取值范围．

<strong>解析</strong>　（1）函数<em>f</em>(<em>x</em>)的定义域为(－∞，＋∞)，<em>f</em>′(<em>x</em>)＝2e<sup>2</sup><em><sup>x</sup></em>－<em>a</em>e<em><sup>x</sup></em>－<em>a</em><sup>2</sup>＝(2e<em><sup>x</sup></em>＋<em>a</em>)(e<em><sup>x</sup></em>－<em>a</em>)．

①若<em>a</em>＝0，则<em>f</em>(<em>x</em>)＝e<sup>2</sup><em><sup>x</sup></em>在(－∞，＋∞)上单调递增．

②若*a*＞0，则由*f*′(*x*)＝0得*x*＝ln *a*．
当*x*∈(－∞，ln *a*)时，*f*′(*x*)＜0；当*x*∈(ln *a*，＋∞)时，*f*′(*x*)＞0．
故*f*(*x*)在(－∞，ln *a*)上单调递减，在(ln *a*，＋∞)上单调递增．

③若*a*＜0，则由*f*′(*x*)＝0得*x*＝ln．
当*x*∈时，*f*′(*x*)＜0；当*x*∈时，*f*′(*x*)＞0．
故*f*(*x*)在上单调递减，在上单调递增．  
（2）①若<em>a</em>＝0，则<em>f</em>(<em>x</em>)＝e<sup>2</sup><em><sup>x</sup></em>，所以<em>f</em>(<em>x</em>)≥0．

②若<em>a</em>＞0，则由（1）得，当<em>x</em>＝ln <em>a</em>时，<em>f</em>(<em>x</em>)取得最小值，最小值为<em>f</em>(ln <em>a</em>)＝－<em>a</em><sup>2</sup>ln <em>a</em>，
从而当且仅当－<em>a</em><sup>2</sup>ln<em>a</em>≥0，即0＜<em>a</em>≤1时，<em>f</em>(<em>x</em>)≥0．

③若<em>a</em>＜0，则由（1）得，当<em>x</em>＝ln时，<em>f</em>(<em>x</em>)取得最小值，最小值为<em>f</em>＝<em>a</em><sup>2</sup>，
从而当且仅当<em>a</em><sup>2</sup>≥0，即－2e≤<em>a</em>＜0时，<em>f</em>(<em>x</em>)≥0．

综上，*a*的取值范围是[－2e，1]．

<strong>[例2]</strong>　已知函数<em>f</em>(<em>x</em>)＝<em>x</em>ln<em>x</em>－<em>ax</em>＋1(<em>a</em>∈<strong>R</strong>)．  
（1）讨论*f*(*x*)在(1，＋∞)上的零点个数；  
（2）当*a*>1时，若存在*x*∈(1，＋∞)，使得*f*(*x*)<(e－1)·(*a*－3)，求实数*a*的取值范围．
解析　（1）由*f*(*x*)＝*x*ln *x*－*ax*＋1＝0可得*a*＝ln *x*＋，
令*g*(*x*)＝ln *x*＋，易知*g*′(*x*)＝－＝．
∴*g*′(*x*)>0在(1，＋∞)上恒成立，故*g*(*x*)在(1，＋∞)上单调递增．
又*g*（1）＝1，所以当*x*∈(1，＋∞)时，*g*(*x*)>1．
故当*a*≤1时，*f*(*x*)在(1，＋∞)上无零点；当*a*>1时，*f*(*x*)在(1，＋∞)上存在一个零点．  
（2）当<em>a</em>&gt;1时，由（1）得<em>f</em>(<em>x</em>)在(1，＋∞)上存在一个零点．由<em>f</em>′(<em>x</em>)＝ln <em>x</em>＋1－<em>a</em>＝0得<em>x</em>＝e<em><sup>a</sup></em><sup>－1</sup>，
所以<em>f</em>(<em>x</em>)在(1，e<em><sup>a</sup></em><sup>－1</sup>)上单调递减，在(e<em><sup>a</sup></em><sup>－1</sup>，＋∞)上单调递增，所以<em>f</em>(<em>x</em>)<sub>min</sub>＝<em>f</em>(e<em><sup>a</sup></em><sup>－1</sup>)＝1－e<em><sup>a</sup></em><sup>－1</sup>．
若存在*x*∈(1，＋∞)，使得*f*(*x*)<(e－1)(*a*－3)成立，

只需1－e<em><sup>a</sup></em><sup>－1</sup>&lt;(e－1)(<em>a</em>－3)成立，即不等式e<em><sup>a</sup></em><sup>－1</sup>＋(e－1)(<em>a</em>－3)－1&gt;0成立．
令<em>h</em>(<em>a</em>)＝e<em><sup>a</sup></em><sup>－1</sup>＋(e－1)(<em>a</em>－3)－1，<em>a</em>&gt;1，则<em>h</em>′(<em>a</em>)＝e<em><sup>a</sup></em><sup>－1</sup>＋e－1，

易知<em>h</em>′(<em>a</em>)＝e<em><sup>a</sup></em><sup>－1</sup>＋e－1&gt;0在(1，＋∞)上恒成立，
故<em>h</em>(<em>a</em>)＝e<em><sup>a</sup></em><sup>－1</sup>＋(e－1)(<em>a</em>－3)－1在(1，＋∞)上单调递增，又<em>h</em>（2）＝0，所以<em>a</em>&gt;2，
故实数*a*的取值范围为(2，＋∞)．

<strong>[例3]</strong>　已知函数<em>f</em> (<em>x</em>)＝<em>a</em>ln<em>x</em>＋<em>x<sup>b</sup></em>(<em>a</em>≠0)．  
（1）当*b*＝2时，讨论函数*f* (*x*)的单调性；  
（2）当*a*＋*b*＝0，*b*>0时，对任意的*x*∈，恒有*f*(*x*)≤e－1成立，求实数*b*的取值范围．

<strong>思路</strong>　（2）由已知<em>a</em>＋<em>b</em>＝0消去<em>a</em>，转化为最值问题，即－<em>b</em>ln <em>x</em>＋<em>x<sup>b</sup></em>≤e－1恒成立，无法分离参数<em>b</em>，用单调性分析法解决．

<strong>解析</strong>　（1）函数<em>f</em> (<em>x</em>)的定义域为(0，＋∞)．当<em>b</em>＝2时，<em>f</em> (<em>x</em>)＝<em>a</em>ln<em>x</em>＋<em>x</em><sup>2</sup>，所以<em>f</em> ′(<em>x</em>)＝＋2<em>x</em>＝．

①当*a*>0时，*f* ′(*x*)>0，所以函数*f* (*x*)在(0，＋∞)上单调递增．

②当*a*<0时，令*f* ′(*x*)＝0，解得*x*＝(负值舍去)，
当0<*x*<时，*f* ′(*x*)<0，所以函数*f* (*x*)在上单调递减；
当*x*>时，*f* ′(*x*)>0，所以函数*f* (*x*)在上单调递增．
综上所述，当*b*＝2，*a*>0时，函数*f* (*x*)在(0，＋∞)上单调递增；
当*b*＝2，*a*<0时，函数*f* (*x*)在上单调递减，在上单调递增．  
（2）因为对任意的<em>x</em>∈，恒有<em>f</em> (<em>x</em>)≤e－1成立，所以当<em>x</em>∈时，<em>f</em> (<em>x</em>)<sub>max</sub>≤e－1．
当<em>a</em>＋<em>b</em>＝0，<em>b</em>&gt;0时，<em>f</em> (<em>x</em>)＝－<em>b</em>ln <em>x</em>＋<em>x<sup>b</sup></em>，<em>f</em> ′(<em>x</em>)＝－＋<em>bx<sup>b</sup></em><sup>－1</sup>＝．
令*f* ′(*x*)<0，得0<*x*<1；令*f* ′(*x*)>0，得*x*>1．
所以函数*f* (*x*)在上单调递减，在(1，e]上单调递增，

<em>f</em> (<em>x</em>)<sub>max</sub>为<em>f</em>()＝<em>b</em>＋e<sup>－</sup><em><sup>b</sup></em>与<em>f</em> (e)＝－<em>b</em>＋e<em><sup>b</sup></em>中的较大者．

<em>f</em> (e)－<em>f</em>()＝e<em><sup>b</sup></em>－e<sup>－</sup><em><sup>b</sup></em>－2<em>b．</em>令<em>g</em>(<em>m</em>)＝e<em><sup>m</sup></em>－e<sup>－</sup><em><sup>m</sup></em>－2<em>m</em>(<em>m</em>&gt;0)，
则当<em>m</em>&gt;0时，<em>g</em>′(<em>m</em>)＝e<em><sup>m</sup></em>＋e<sup>－</sup><em><sup>m</sup></em>－2&gt;2－2＝0，
所以*g*(*m*)在(0，＋∞)上单调递增，故*g*(*m*)>*g*（0）＝0，
所以<em>f</em> (e)&gt; <em>f</em>()，从而<em>f</em> (<em>x</em>)<sub>max</sub>＝<em>f</em> (e)＝－<em>b</em>＋e<em><sup>b</sup></em>，所以－<em>b</em>＋e<em><sup>b</sup></em>≤e－1，即e<em><sup>b</sup></em>－<em>b</em>－e＋1≤0．
设<em>φ</em>(<em>t</em>)＝e<em><sup>t</sup></em>－<em>t</em>－e＋1(<em>t</em>&gt;0)，则<em>φ</em>′(<em>t</em>)＝e<em><sup>t</sup></em>－1&gt;0，所以<em>φ</em>(<em>t</em>)在(0，＋∞)上单调递增．
又<em>φ</em>（1）＝0，所以e<em><sup>b</sup></em>－<em>b</em>－e＋1≤0的解集为(0，1]．所以<em>b</em>的取值范围为(0，1]．

<strong>悟通</strong>　（2）构造<em>f</em> (<em>x</em>)＝－<em>b</em>ln <em>x</em>＋<em>x<sup>b</sup></em>并进行单调性分析后，最大值不定或<em>f</em>()或<em>f</em>(e)，作差比较，<em>f</em>(e)－<em>f</em>()＝e<em><sup>b</sup></em>－e<sup>－</sup><em><sup>b</sup></em>－2<em>b．</em>又不能确定差值的正负，只能构造函数<em>g</em>(<em>m</em>)＝e<em><sup>m</sup></em>－e<sup>－</sup><em><sup>m</sup></em>－2<em>m</em>(<em>m</em>&gt;0)，用基本不等式求出最大值<em>g</em>(<em>m</em>)&gt;<em>g</em>（0）＝0，<em>f</em> (<em>x</em>)<sub>max</sub>＝<em>f</em> (e)＝－<em>b</em>＋e<em><sup>b</sup></em>，但又解不出<em>b</em>的不等式，再次构造函数<em>φ</em>(<em>t</em>)＝e<em><sup>t</sup></em>－<em>t</em>－e＋1(<em>t</em>&gt;0)进行处理，解不等式．构造函数，解不等式也是高考题的常用套路．

<strong>[例4]</strong>　已知<em>a</em>∈<strong>R</strong>，设函数<em>f</em>(<em>x</em>)＝<em>a</em>ln(<em>x</em>＋<em>a</em>)＋ln<em>x</em>．  
（1）讨论函数*f*(*x*)的单调性；
![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)  
（2）若*f*(*x*)≤＋ln－1恒成立，求实数*a*的取值范围．
解析　（1）*f*′(*x*)＝＋＝，*x*＞0且*x*＞－*a*，

①当*a*≥0时，*f*′(*x*)＞0，*f*(*x*)单调递增；
②当*a*≤－1时，*f*′(*x*)＜0，*f*(*x*)单调递减；
③当－1＜*a*＜0时，－＞－*a*＞0，

*x*∈时，*f*′(*x*)＜0，*f*(*x*)单调递减；*x*∈时，*f*′(*x*)＞0，*f*(*x*)单调递增．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)  
（2）*f*(*x*)＝*a*ln(*x*＋*a*)＋ln *x*≤＋ln－1，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
即*a*ln(*x*＋*a*)＋ln *x*≤＋ln*x*－ln *a*－1，*a*＞0，即*a*ln(*x*＋*a*)＋ln *a*≤－1，
令<em>g</em>(<em>x</em>)＝e<em><sup>x</sup></em>－<em>x</em>－1(<em>x</em>＞0)，则<em>g</em>′(<em>x</em>)＝e<em><sup>x</sup></em>－1＞0，
∴<em>g</em>(<em>x</em>)在(0，＋∞)上单调递增，∴<em>g</em>(<em>x</em>)＞<em>g</em>（0）＝0，即e<em><sup>x</sup></em>－<em>x</em>－1＞0，即e<em><sup>x</sup></em>－1＞<em>x</em>，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
∴e－1＞<em>a</em><sup>2</sup><em>x</em>，则原不等式等价为<em>a</em>ln(<em>x</em>＋<em>a</em>)＋ln <em>a</em>≤<em>a</em><sup>2</sup><em>x</em>，即<em>a</em>ln(<em>x</em>＋<em>a</em>)－<em>a</em><sup>2</sup><em>x</em>＋ln <em>a</em>≤0，
令<em>h</em>(<em>x</em>)＝<em>a</em>ln(<em>x</em>＋<em>a</em>)－<em>a</em><sup>2</sup><em>x</em>＋ln <em>a</em>，则<em>h</em>′(<em>x</em>)＝－<em>a</em><sup>2</sup>＝，令<em>h</em>′(<em>x</em>)＝0，可得<em>x</em>＝，
当*a*≥1时，*h*′(*x*)≤0，则*h*(*x*)在(0，＋∞)上单调递减，
则只需满足*h*（0）＝*a*ln *a*＋ln *a*≤0，∴ln *a*≤0，解得0＜*a*≤1，∴*a*＝1；
当0＜*a*＜1时，可得*h*(*x*)在上单调递增，在上单调递减，
则<em>h</em>(<em>x</em>)<sub>max</sub>＝<em>h</em>＝<em>a</em>ln－<em>a</em>(1－<em>a</em><sup>2</sup>)＋ln <em>a</em>≤0，整理可得ln <em>a</em>－<em>a</em><sup>2</sup>－<em>a</em>≤0，
令<em>φ</em>(<em>a</em>)＝ln <em>a</em>－<em>a</em><sup>2</sup>－<em>a</em>，则<em>φ</em>′(<em>a</em>)＝－2<em>a</em>－1＝，
则可得*φ*(*a*)在上单调递增，在上单调递减，
则<em>φ</em>(<em>a</em>)<sub>max</sub>＝<em>φ</em>＝－ln 2－＜0，故0＜<em>a</em>＜1时，<em>h</em>(<em>x</em>)≤0恒成立，

综上，0＜*a*≤1．

<strong>[例5]</strong>　(2017·全国Ⅲ)已知函数<em>f</em>(<em>x</em>)＝<em>x</em>－1－<em>a</em>ln <em>x</em>．  
（1）若*f*(*x*)≥0，求*a*的值；  
（2）设*m*为整数，且对于任意正整数*n*，·…·＜*m*，求*m*的最小值．
解析：（1）*f*(*x*)的定义域为(0，＋∞)，
![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

①若*a*≤0，因为＝－＋*a*ln 2＜0，所以不满足题意；
②若*a*＞0，由*f*′(*x*)＝1－＝知，当*x*∈(0，*a*)时，*f*′(*x*)＜0；当*x*∈(*a*，＋∞)时，*f*′(*x*)＞0．
所以*f*(*x*)在(0，*a*)单调递减，在(*a*，＋∞)单调递增．
故*x*＝*a*是*f*(*x*)在(0，＋∞)的唯一最小值点．由于*f*（1）＝0，所以当且仅当*a*＝1时，*f*(*x*)≥0．故*a*＝1．  
（2）由（1）知当*x*∈(1，＋∞)时，*x*－1－ln *x*＞0．令*x*＝1＋，得ln＜．
从而ln＋ln＋…＋ln＜＋＋…＋＝1－＜1．
故·…·＜e．而＞2，所以*m*的最小值为3．

<strong>[例6]</strong>　已知函数<em>f</em>(<em>x</em>)＝<em>x</em>ln<em>x</em>－<em>a</em>(<em>x</em>－1)<sup>2</sup>－<em>x</em>＋1(<em>a</em>∈<strong>R</strong>)．  
（1）当*a*＝0时，求*f*(*x*)的极值；  
（2）若*f*(*x*)<0对*x*∈(1，＋∞)恒成立，求*a*的取值范围．
解析　（1）若*a*＝0，*f*(*x*)＝*x*ln *x*－*x*＋1，*f*′(*x*)＝ln *x*，

*x*∈(0，1)时，*f*′(*x*)<0，*f*(*x*)为减函数，

*x*∈(1，＋∞)时，*f*′(*x*)>0，*f*(*x*)为增函数，
∴*f*(*x*)有极小值，*f*（1）＝0，无极大值．  
（2）<em>f</em>(<em>x</em>)＝<em>x</em>ln<em>x</em>－<em>a</em>(<em>x</em>－1)<sup>2</sup>－<em>x</em>＋1&lt;0在(1，＋∞)恒成立．

①若*a*＝0，*f*(*x*)＝*x*ln*x*－*x*＋1，*f*′(*x*)＝ln*x*，*x*∈(1，＋∞)，*f*′(*x*)>0，
∴*f*(*x*)为增函数，∴*f*(*x*)>*f*（1）＝0，即*f*(*x*)<0不成立，∴*a*＝0不成立．

②∵*x*>1，ln*x*－<0在(1，＋∞)恒成立，
不妨设*h*(*x*)＝ln*x*－，*x*∈(1，＋∞)，

*h*′(*x*)＝－，*x*∈(1，＋∞)，*h*′(*x*)＝0，*x*＝1或，
若*a*<0，则<1，*x*>1，*h*′(*x*)>0，*h*(*x*)为增函数，*h*(*x*)>*h*（1）＝0(不合题意)；
若0<*a*<，*x*∈，*h*′(*x*)>0，*h*(*x*)为增函数，*h*(*x*)>*h*（1）＝0(不合题意)；
若*a*≥，*x*∈(1，＋∞)，*h*′(*x*)<0，*h*(*x*)为减函数，*h*(*x*)<*h*（1）＝0(符合题意)．
综上所述，若*x*>1时，*f*(*x*)<0恒成立，则*a*≥．

<strong>[例7]</strong>　(2020·全国Ⅰ)已知函数<em>f</em>(<em>x</em>)＝e<em><sup>x</sup></em>＋<em>ax</em><sup>2</sup>－<em>x</em>．  
（1）当*a*＝1时，讨论*f*(*x*)的单调性；  
（2）当<em>x</em>≥0时，<em>f</em>(<em>x</em>)≥<em>x</em><sup>3</sup>＋1，求<em>a</em>的取值范围．
解析　（1）当<em>a</em>＝1时，<em>f</em>(<em>x</em>)＝e<em><sup>x</sup></em>＋<em>x</em><sup>2</sup>－<em>x</em>，<em>f</em>′(<em>x</em>)＝e<em><sup>x</sup></em>＋2<em>x</em>－1，
由于<em>f</em>″(<em>x</em>)＝e<em><sup>x</sup></em>＋2＞0，故<em>f</em>′(<em>x</em>)单调递增，注意到<em>f</em>′（0）＝0，
故当*x*∈(－∞，0)时，*f*′(*x*)＜0，*f*(*x*)单调递减，当*x*∈(0，＋∞)时，*f*′(*x*)＞0，*f*(*x*)单调递增．  
（2）方法一　<em>f</em>(<em>x</em>)≥<em>x</em><sup>3</sup>＋1等价于e<sup>－</sup><em><sup>x</sup></em>≤1．
设函数<em>g</em>(<em>x</em>)＝e<sup>－</sup><em><sup>x</sup></em>(<em>x</em>≥0)，
则<em>g</em>′(<em>x</em>)＝－e<sup>－</sup><em><sup>x</sup></em>＝－<em>x</em>[<em>x</em><sup>2</sup>－(2<em>a</em>＋3)<em>x</em>＋4<em>a</em>＋2]e<sup>－</sup><em><sup>x</sup></em>

＝－<em>x</em>(<em>x</em>－2<em>a</em>－1)(<em>x</em>－2)e<sup>－</sup><em><sup>x</sup></em>，

①若2*a*＋1≤0，即*a*≤－，则当*x*∈(0，2)时，*g*′(*x*)＞0，所以*g*(*x*)在(0，2)上单调递增，而*g*（0）＝1，
故当*x*∈(0，2)时，*g*(*x*)>1，不合题意．

②若0<2*a*＋1<2，即－<*a*<，则当*x*∈(0，2*a*＋1)∪(2，＋∞)时，*g*′(*x*)<0；当*x*∈(2*a*＋1，2)时，*g*′(*x*)>0．
所以*g*(*x*)在(0，2*a*＋1)，(2，＋∞)上单调递减，在(2*a*＋1，2)上单调递增，由于*g*（0）＝1，
所以<em>g</em>(<em>x</em>)≤1，当且仅当<em>g</em>（2）＝(7－4<em>a</em>)e<sup>－2</sup>≤1时成立，解得<em>a</em>≥．所以当≤<em>a</em>&lt;时，<em>g</em>(<em>x</em>)≤1．

③若2<em>a</em>＋1≥2，即<em>a</em>≥，则<em>g</em>(<em>x</em>)≤e<sup>－</sup><em><sup>x</sup></em>．
由于0∈，故由②可得e<sup>－</sup><em><sup>x</sup></em>≤1．故当<em>a</em>≥时，<em>g</em>(<em>x</em>)≤1．

综上，*a*的取值范围是．
方法二　当<em>x</em>≥0时，<em>f</em>(<em>x</em>)≥<em>x</em><sup>3</sup>＋1，即e<em><sup>x</sup></em>＋<em>ax</em><sup>2</sup>－<em>x</em>≥<em>x</em><sup>3</sup>＋1．
当*x*＝0时，无论*a*取何值，上式恒成立．
当*x*>0时，上式可化为*a*≥．令*g*(*x*)＝，
则*g*′(*x*)＝－－－＝，
令<em>h</em>(<em>x</em>)＝<em>x</em><sup>3</sup>－<em>x</em>－2－(<em>x</em>－2)e<em><sup>x</sup></em>，则<em>h</em>′(<em>x</em>)＝<em>x</em><sup>2</sup>－1－(<em>x</em>－1)e<em><sup>x</sup></em>，<em>h</em>″(<em>x</em>)＝3<em>x</em>－<em>x</em>e<em><sup>x</sup></em>＝<em>x</em>(3－e<em><sup>x</sup></em>)，
令<em>h</em>″(<em>x</em>)＝0，得3－e<em><sup>x</sup></em>＝0，即<em>x</em>＝ln 3．
所以在(0，ln3)上，*h*″(*x*)>0，在(ln3，＋∞)上，*h*″(*x*)<0．
所以*h*′(*x*)在(0，ln 3)上单调递增，在(ln 3，＋∞)上单调递减．
又<em>h</em>′（0）＝0，<em>h</em>′(ln 3)＝(ln 3)<sup>2</sup>－1－3(ln 3－1)＝(ln 3)<sup>2</sup>－3ln 3＋2＝(ln 3－1)<sup>2</sup>＋&gt;0，<em>h</em>′（2）＝5－e<sup>2</sup>&lt;0，
所以*h*(*x*)在(0，＋∞)上先增后减．
又*h*（0）＝0，*h*（2）＝4－2－2＝0，所以在(0，2)上，*h*(*x*)>0，在(2，＋∞)上，*h*(*x*)<0，
所以<em>g</em>(<em>x</em>)在(0,2)上单调递增，在(2，＋∞)上单调递减．所以<em>g</em>(<em>x</em>)<sub>max</sub>＝<em>g</em>（2）＝＝，
所以*a*≥．所以*a*的取值范围是．

<strong>[例8]</strong>　(2020·新高考Ⅰ)已知函数<em>f</em>(<em>x</em>)＝<em>a</em>e<em><sup>x</sup></em><sup>－1</sup>－ln<em>x</em>＋ln<em>a</em>．  
（1）当*a*＝e时，求曲线*y*＝*f*(*x*)在点(1，*f*（1）)处的切线与两坐标轴围成的三角形的面积；  
（2）若*f*(*x*)≥1，求*a*的取值范围．
解析　（1）当<em>a</em>＝e时，<em>f</em>(<em>x</em>)＝e<em><sup>x</sup></em>－ln <em>x</em>＋1，∴<em>f</em>′(<em>x</em>)＝e<em><sup>x</sup></em>－，∴<em>f</em>′（1）＝e－1．
∵*f*（1）＝e＋1，∴切点坐标为(1，1＋e)，
∴曲线*y*＝*f*(*x*)在点(1，*f*（1）)处的切线方程为*y*－e－1＝(e－1)·(*x*－1)，即*y*＝(e－1)*x*＋2，
∴切线与两坐标轴的交点坐标分别为(0，2)，，
∴所求三角形面积为×2×＝．  
（2）解法一　(隐零点法)
∵<em>f</em>(<em>x</em>)＝<em>a</em>e<em><sup>x</sup></em><sup>－1</sup>－ln <em>x</em>＋ln<em>a</em>，∴<em>f</em>′(<em>x</em>)＝<em>a</em>e<em><sup>x</sup></em><sup>－1</sup>－，且<em>a</em>&gt;0．
设<em>g</em>(<em>x</em>)＝<em>f</em>′(<em>x</em>)，则<em>g</em>′(<em>x</em>)＝<em>a</em>e<em><sup>x</sup></em><sup>－1</sup>＋&gt;0，∴<em>g</em>(<em>x</em>)在(0，＋∞)上单调递增，即<em>f</em>′(<em>x</em>)在(0，＋∞)上单调递增，
当*a*＝1时，*f*′（1）＝0，则*f*(*x*)在(0，1)上单调递减，在(1，＋∞)上单调递增，
∴<em>f</em>(<em>x</em>)<sub>min</sub>＝<em>f</em>（1）＝1，∴<em>f</em>(<em>x</em>)≥1成立；
![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
当*a*>1时，<1，∴<1，∴*f*′*f*′（1）＝，
∴存在唯一<em>x</em><sub>0</sub>&gt;0，使得<em>f</em>′(<em>x</em><sub>0</sub>)＝<em>a</em>e<em><sup>x</sup></em><sup>0－1</sup>－＝0，且当<em>x</em>∈(0，<em>x</em><sub>0</sub>)时<em>f</em>′(<em>x</em>)&lt;0，当<em>x</em>∈(<em>x</em><sub>0</sub>，＋∞)时<em>f</em>′(<em>x</em>)&gt;0，
∴<em>a</em>e <em><sup>x</sup></em><sup>0－1</sup>＝，∴ln<em>a</em>＋<em>x</em><sub>0</sub>－1＝－ln<em>x</em><sub>0</sub>，
因此<em>f</em>(<em>x</em>)<sub>min</sub>＝<em>f</em>(<em>x</em><sub>0</sub>)＝<em>a</em>e <em><sup>x</sup></em><sup>0－1</sup>－ln<em>x</em><sub>0</sub>＋ln<em>a</em>＝＋ln<em>a</em>＋<em>x</em><sub>0</sub>－1＋ln<em>a</em>≥2ln<em>a</em>－1＋2＝2ln<em>a</em>＋1&gt;1，
∴*f*(*x*)>1，∴*f*(*x*)≥1恒成立；
当0<*a*<1时，*f*（1）＝*a*＋ln*a*<*a*<1，∴*f*（1）<1，*f*(*x*)≥1不恒成立．
综上所述，*a*的取值范围是[1，＋∞)．
解法二　(同构法)

<em>f</em>(<em>x</em>)＝<em>a</em>e<em><sup>x</sup></em><sup>－1</sup>－ln<em>x</em>＋ln<em>a</em>＝e<sup>ln</sup> <em><sup>a</sup></em><sup>＋</sup><em><sup>x</sup></em><sup>－1</sup>－ln<em>x</em>＋ln<em>a</em>≥1等价于e<sup>ln</sup> <em><sup>a</sup></em><sup>＋</sup><em><sup>x</sup></em><sup>－1</sup>＋ln<em>a</em>＋<em>x</em>－1≥ln<em>x</em>＋<em>x</em>＝e<sup>ln</sup> <em><sup>x</sup></em>＋ln<em>x</em>，
令<em>g</em>(<em>x</em>)＝e<em><sup>x</sup></em>＋<em>x</em>，上述不等式等价于<em>g</em>(ln<em>a</em>＋<em>x</em>－1)≥<em>g</em>(ln<em>x</em>)，
显然*g*(*x*)为单调递增函数，∴又等价于ln*a*＋*x*－1≥ln*x*，即ln*a*≥ln*x*－*x*＋1，
令*h*(*x*)＝ln*x*－*x*＋1，则*h*′(*x*)＝－1＝，
在(0，1)上*h*′(*x*)>0，*h*(*x*)单调递增；在(1，＋∞)上*h*′(*x*)<0，*h*(*x*)单调递减，
∴<em>h</em>(<em>x</em>)<sub>max</sub>＝<em>h</em>（1）＝0，ln <em>a</em>≥0，即<em>a</em>≥1，∴<em>a</em>的取值范围是[1，＋∞)．

<strong>[例9]</strong>　已知函数<em>f</em>(<em>x</em>)＝<em>a</em>ln<em>x</em>－e<em><sup>x</sup></em>．  
（1）讨论*f*(*x*)的极值点的个数；  
（2）若<em>a</em>∈<strong>N</strong><sup>\*</sup>，且<em>f</em>(<em>x</em>)&lt;0恒成立，求<em>a</em>的最大值．

参考数据：

<table><tr><td><p><em>x</em></p></td><td><p>1.6</p></td><td><p>1.7</p></td><td><p>1.8</p></td></tr><tr><td><p>e<em><sup>x</sup></em></p></td><td><p>4.953</p></td><td><p>5.474</p></td><td><p>6.050</p></td></tr><tr><td><p>ln <em>x</em></p></td><td><p>0.470</p></td><td><p>0.531</p></td><td><p>0.588</p></td></tr></table>

<strong>思路</strong>　（1）对<em>f</em>(<em>x</em>)进行单调性分析，但导函数的零点不可求，用隐零点技术处理．（2）可对ln<em>x</em>的正负讨论后分离参数去处理如解法1，也可（1）的结果进行解决，但难度较大．

<strong>解析</strong>　（1）根据题意可得<em>f</em>′(<em>x</em>)＝－e<em><sup>x</sup></em>＝(<em>x</em>&gt;0)，
当<em>a</em>≤0时，<em>f</em>′(<em>x</em>)&lt;0，函数是减函数，无极值点；当<em>a</em>&gt;0时，令<em>f</em>′(<em>x</em>)＝0得<em>a</em>－<em>x</em>e<em><sup>x</sup></em>＝0，即<em>x</em>e<em><sup>x</sup></em>＝<em>a</em>，
又<em>y</em>＝<em>x</em>e<em><sup>x</sup></em>在(0，＋∞)上是增函数，且当<em>x</em>→＋∞时，<em>x</em>e<em><sup>x</sup></em>→＋∞，
所以<em>x</em>e<em><sup>x</sup></em>＝<em>a</em>在(0，＋∞)上存在一解，不妨设为<em>x</em><sub>0</sub>，所以函数<em>y</em>＝<em>f</em>(<em>x</em>)在(0，<em>x</em><sub>0</sub>)上单调递增，
在(<em>x</em><sub>0</sub>，＋∞)上单调递减，所以函数<em>y</em>＝<em>f</em>(<em>x</em>)有一个极大值点，无极小值点．综上，当<em>a</em>≤0时，无极值点；
当*a*>0时，函数*y*＝*f*(*x*)有一个极大值点，无极小值点．  
（2）解法1　要使<em>f</em>(<em>x</em>)&lt;0恒成立，即<em>a</em>ln <em>x</em>&lt;e<em><sup>x</sup></em>恒成立，

①当ln *x*>0时，即*x*>1时，*a*<，令*g*(*x*)＝，则*g*′(*x*)＝，
令*h*(*x*)＝ln *x*－，则*h*(*x*)在(1，＋∞)上是增函数，又*h*(1.7)＝ln 1.7－<0，*h*(1.8)＝ln 1.8－>0，
∴存在*m*∈(1.7，1.8)，*h*(*m*)＝0，即ln *m*－＝0，∴*g*(*x*)在(1，*m*)上单调递增，在(*m*，＋∞)上单调递减，
∴<em>g</em>(<em>x</em>)<sub>min</sub>＝<em>g</em>(<em>m</em>)&lt;，又因为ln <em>m</em>＝，∴<em>g</em>(<em>m</em>)＝<em>m</em> e<em><sup>m</sup></em>，<em>g</em>′(<em>m</em>)＝e<em><sup>m</sup></em>＋<em>m</em> e<em><sup>m</sup></em>&gt;0，
∴<em>g</em>(<em>m</em>)在(1.7，1.8)上是递增函数，∴<em>g</em>(<em>m</em>)<sub>max</sub>＝<em>g</em>(1.8)＝10.89，
∴<em>a</em>≤10.89，又<em>a</em>∈<strong>N</strong><sup>\*</sup>，所以<em>a</em>的最大值为10．

②当ln *x*<0时，即0<*x*<1时，，*a*>，令*g*(*x*)＝，则*g*′(*x*)＝<0，
∴<em>g</em>(<em>x</em>)在(0，1)上单调递减，∴<em>g</em>(<em>x</em>)<sub>max</sub>＝<em>g</em>（0）→0，∴<em>a</em>&gt;0．

③当ln *x*＝0时，即*x*＝1时，不等式恒成立．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
解法2　因为<em>a</em>∈<strong>N</strong><sup>\*</sup>，由（1）知，<em>f</em>(<em>x</em>)有极大值<em>f</em>(<em>x</em><sub>0</sub>)，且<em>x</em><sub>0</sub>满足<em>x</em><sub>0</sub>＝<em>a</em>，①
![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
可知<em>f</em>(<em>x</em>)<sub>max</sub>＝<em>f</em>(<em>x</em><sub>0</sub>)＝<em>a</em>ln <em>x</em><sub>0</sub>－，要使<em>f</em>(<em>x</em>)&lt;0恒成立，即<em>f</em>(<em>x</em><sub>0</sub>)＝<em>a</em>ln <em>x</em><sub>0</sub>－&lt;0，②

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
由①可得＝，代入②得<em>a</em>ln <em>x</em><sub>0</sub>－&lt;0，即<em>a</em>&lt;0，因为<em>a</em>∈<strong>N</strong><sup>\*</sup>&gt;0，所以ln <em>x</em><sub>0</sub>－&lt;0，
因为ln 1.7－&lt;0，ln 1.8－&gt;0，且<em>y</em>＝ln <em>x</em><sub>0</sub>－在(0，＋∞)上是增函数．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
设<em>m</em>为<em>y</em>＝ln <em>x</em><sub>0</sub>－的零点，则<em>m</em>∈(1.7，1.8)，可知0&lt;<em>x</em><sub>0</sub>&lt;<em>m</em>，由②可得<em>a</em>ln <em>x</em><sub>0</sub>&lt;，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
当0&lt;<em>x</em><sub>0</sub>≤1时，<em>a</em>ln <em>x</em><sub>0</sub>≤0，不等式显然恒成立；当1&lt;<em>x</em><sub>0</sub>&lt;<em>m</em>时，ln <em>x</em><sub>0</sub>&gt;0，<em>a</em>&lt;，
令*g*(*x*)＝，*x*∈(1，*m*)，则*g*′(*x*)＝<0，所以*g*(*x*)在(1，*m*)上是减函数，

且≈10.29，≈10.31，所以10.29<*g*(*m*)<10.31，所以*a*≤*g*(*m*)，
又<em>a</em>∈<strong>N</strong><sup>\*</sup>，所以<em>a</em>的最大值为10．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

<strong>悟通</strong>　（2）如不分离参数，可由（1）知，<em>f</em>(<em>x</em>)有极大值<em>f</em>(<em>x</em><sub>0</sub>)，可知<em>f</em>(<em>x</em>)<sub>max</sub>＝<em>f</em>(<em>x</em><sub>0</sub>)＝<em>a</em>ln<em>x</em><sub>0</sub>－&lt;0，难以解决，当然可解决．参见解法2．但整个思路不顺畅．如分离参数，则需分类讨论，当然此时问题主要集中到ln <em>x</em>&gt;0，即<em>x</em>&gt;1上，构造函数<em>g</em>(<em>x</em>)＝，求导后提取公因式，之后再构造函数<em>h</em>(<em>x</em>)＝ln<em>x</em>－，用到隐零点技术．但值得注意的是<em>g</em>(<em>x</em>)<sub>min</sub>＝<em>g</em>(<em>m</em>)&lt;<em>g</em>(<em>m</em>)<sub>max</sub>，因为存在<em>m</em>∈(1.7，1.8)，而不是对任意的<em>m</em>，所以<em>a</em>&lt;10.89，又<em>a</em>∈<strong>N</strong><sup>\*</sup>，所以<em>a</em>的最大值为10．

【对点训练】

1．函数<em>f</em>(<em>x</em>)＝<em>x</em><sup>2</sup>－2<em>ax</em>＋ln <em>x</em>(<em>a</em>∈<strong>R</strong>).  
（1）若函数*y*＝*f*(*x*)在点(1，*f*（1）)处的切线与直线*x*－2*y*＋1＝0垂直，求*a*的值；  
（2）若不等式2<em>x</em>ln <em>x</em>≥－<em>x</em><sup>2</sup>＋<em>ax</em>－3在区间(0，e]上恒成立，求实数<em>a</em>的取值范围．

1．解析　（1）函数*f*(*x*)的定义域为(0，＋∞)，*f*′(*x*)＝2*x*－2*a*＋，*f*′（1）＝3－2*a*，
由题意*f*′（1）·＝(3－2*a*)·＝－1，解得*a*＝*．*  
（2）不等式2<em>x</em>ln <em>x</em>≥－<em>x</em><sup>2</sup>＋<em>ax</em>－3在区间(0，e]上恒成立等价于2ln <em>x</em>≥－<em>x</em>＋<em>a</em>－，
令*g*(*x*)＝2ln *x*＋*x*－*a*＋，
则*g*′(*x*)＝＋1－＝＝，
则在区间(0，1)上，*g*′(*x*)<0，函数*g*(*x*)为减函数；
在区间(1，e]上，*g*′(*x*)>0，函数*g*(*x*)为增函数.
由题意知<em>g</em>(<em>x</em>)<sub>min</sub>＝<em>g</em>（1）＝1－<em>a</em>＋3≥0，得<em>a</em>≤4，
所以实数*a*的取值范围是(－∞，4]．

2．已知函数<em>f</em>(<em>x</em>)＝(<em>x</em>＋<em>a</em>－1)e<em><sup>x</sup></em>，<em>g</em>(<em>x</em>)＝<em>x</em><sup>2</sup>＋<em>ax</em>，其中<em>a</em>为常数．  
（1）当*a*＝2时，求函数*f*(*x*)在点(0，*f*（0）)处的切线方程；  
（2）若对任意的*x*∈[0，＋∞)，不等式*f*(*x*)≥*g*(*x*)恒成立，求实数*a*的取值范围．

2．解析　（1）因为<em>a</em>＝2，所以<em>f</em>(<em>x</em>)＝(<em>x</em>＋1)e<em><sup>x</sup></em>，所以<em>f</em>（0）＝1，

<em>f</em>′(<em>x</em>)＝(<em>x</em>＋2)e<em><sup>x</sup></em>，所以<em>f</em>′（0）＝2，所以所求切线方程为2<em>x</em>－<em>y</em>＋1＝0．  
（2）令<em>h</em>(<em>x</em>)＝<em>f</em>(<em>x</em>)－<em>g</em>(<em>x</em>)，由题意得<em>h</em>(<em>x</em>)<sub>min</sub>≥0在<em>x</em>∈[0，＋∞)上恒成立，
因为<em>h</em>(<em>x</em>)＝(<em>x</em>＋<em>a</em>－1)e<em><sup>x</sup></em>－<em>x</em><sup>2</sup>－<em>ax</em>，所以<em>h</em>′(<em>x</em>)＝(<em>x</em>＋<em>a</em>)(e<em><sup>x</sup></em>－1)．

①若*a*≥0，则当*x*∈[0，＋∞)时，*h*′(*x*)≥0，所以函数*h*(*x*)在[0，＋∞)上单调递增，
所以<em>h</em>(<em>x</em>)<sub>min</sub>＝<em>h</em>（0）＝<em>a</em>－1，则<em>a</em>－1≥0，得<em>a</em>≥1．

②若*a*＜0，则当*x*∈[0，－*a*)时，*h*′(*x*)≤0；当*x*∈(－*a*，＋∞)时，*h*′(*x*)＞0，
所以函数<em>h</em>(<em>x</em>)在[0，－<em>a</em>)上单调递减，在(－<em>a</em>，＋∞)上单调递增，所以<em>h</em>(<em>x</em>)<sub>min</sub>＝<em>h</em>(－<em>a</em>)，
又因为*h*(－*a*)＜*h*（0）＝*a*－1＜0，所以不合题意．

综上，实数*a*的取值范围为[1，＋∞)．

3．已知函数<em>f</em>(<em>x</em>)＝e<em><sup>x</sup></em>－<em>a</em>．  
（1）若函数*f*(*x*)的图象与直线*l*：*y*＝*x*－1相切，求*a*的值；  
（2）若*f*(*x*)－ln*x*>0恒成立，求整数*a*的最大值．

3．解析　（1）<em>f</em>′(<em>x</em>)＝e<em><sup>x</sup></em>，因为函数<em>f</em>(<em>x</em>)的图象与直线<em>y</em>＝<em>x</em>－1相切，所以令<em>f</em>′(<em>x</em>)＝1，
即e<em><sup>x</sup></em>＝1，得<em>x</em>＝0，即<em>f</em>（0）＝－1，解得<em>a</em>＝2．  
（2）先证明e<em><sup>x</sup></em>≥<em>x</em>＋1，设<em>F</em>(<em>x</em>)＝e<em><sup>x</sup></em>－<em>x</em>－1，则<em>F</em>′(<em>x</em>)＝e<em><sup>x</sup></em>－1，令<em>F</em>′(<em>x</em>)＝0，则<em>x</em>＝0，
当*x*∈(－∞，0)时，*F*′(*x*)<0，当*x*∈(0，＋∞)时，*F*′(*x*)>0，
所以*F*(*x*)在(－∞，0)上单调递减，在(0，＋∞)上单调递增，
所以<em>F</em>(<em>x</em>)<sub>min</sub>＝<em>F</em>（0）＝0，即<em>F</em>(<em>x</em>)≥0恒成立，即e<em><sup>x</sup></em>≥<em>x</em>＋1，即e<em><sup>x</sup></em>－2≥<em>x</em>－1，
当且仅当*x*＝0时等号成立，
同理可得ln <em>x</em>≤<em>x</em>－1，当且仅当<em>x</em>＝1时等号成立，所以e<em><sup>x</sup></em>－2&gt;ln <em>x</em>，
当<em>a</em>≤2时，ln <em>x</em>&lt;e<em><sup>x</sup></em>－2≤e<em><sup>x</sup></em>－<em>a</em>，即当<em>a</em>≤2时，<em>f</em>(<em>x</em>)－ln <em>x</em>&gt;0恒成立．
当<em>a</em>≥3时，存在<em>x</em>＝1，使e<em><sup>x</sup></em>－<em>a</em>&lt;ln <em>x</em>，即e<em><sup>x</sup></em>－<em>a</em>&gt;ln <em>x</em>不恒成立．

综上，整数*a*的最大值为2．

4．已知函数<em>f</em>(<em>x</em>)＝<em>x</em><sup>2</sup>＋(<em>a</em>＋1)<em>x</em>－ln<em>x</em>，<em>g</em>(<em>x</em>)＝<em>x</em><sup>2</sup>＋<em>x</em>＋2<em>a</em>＋1．  
（1）若*f*(*x*)在(1，＋∞)上单调递增，求实数*a*的取值范围；  
（2）当*x*∈[1，e]时，*f*(*x*)<*g*(*x*)恒成立，求实数*a*的取值范围．

4．解析　（1）<em>f</em>(<em>x</em>)＝<em>x</em><sup>2</sup>＋(<em>a</em>＋1)<em>x</em>－ln <em>x</em>，<em>f</em>′(<em>x</em>)＝2<em>x</em>＋(<em>a</em>＋1)－．
依题意知*x*∈(1，＋∞)时，2*x*＋(*a*＋1)－≥0恒成立，即*a*＋1≥－2*x*．
令*k*(*x*)＝－2*x*，*x*∈(1，＋∞)，∴*k*′(*x*)＝－－2<0，
∴*k*(*x*)在(1，＋∞)上单调递减，∴*k*(*x*)<*k*（1）＝－1，∴*a*＋1≥－1，
∴实数*a*的取值范围为{*a*|*a*≥－2}．  
（2）令<em>φ</em>(<em>x</em>)＝<em>f</em>(<em>x</em>)－<em>g</em>(<em>x</em>)＝<em>ax</em>－ln <em>x</em>－2<em>a</em>－1，<em>x</em>∈[1，e]，则只需<em>φ</em>(<em>x</em>)<sub>max</sub>&lt;0即可，
∴*φ*′(*x*)＝*a*－＝．
当<em>a</em>≤0时，<em>φ</em>′(<em>x</em>)&lt;0，∴<em>φ</em>(<em>x</em>)在[1，e]上单调递减，∴<em>φ</em>(<em>x</em>)<sub>max</sub>＝<em>φ</em>（1）＝－<em>a</em>－1，
∴－*a*－1<0，即*a*>－1，∴－1<*a*≤0．
当*a*>0时，当*x*∈时，*φ*′(*x*)<0，当*x*∈时，*φ*′(*x*)>0，
∴<em>φ</em>(<em>x</em>)在上单调递减，在上单调递增，∴要使<em>φ</em>(<em>x</em>)<sub>max</sub>&lt;0，

只需即解得0<*a*<，

综上，实数*a*的取值范围为．

5．已知函数<em>f</em>(<em>x</em>)＝(<em>x</em>－2)e<em><sup>x</sup></em>－<em>ax</em><sup>2</sup>＋<em>ax</em>(<em>a</em>∈<strong>R</strong>)．  
（1）当*a*＝0时，求曲线*y*＝*f*(*x*)在点(0，*f*（0）)处的切线方程；  
（2）当*x*≥2时，*f*(*x*)≥0恒成立，求*a*的取值范围．

5．解析　（1）当<em>a</em>＝0时，<em>f</em>(<em>x</em>)＝(<em>x</em>－2)e<em><sup>x</sup></em>，<em>f</em>（0）＝(0－2)e<sup>0</sup>＝－2，

<em>f</em>′(<em>x</em>)＝(<em>x</em>－1)e<em><sup>x</sup></em>，<em>k</em>＝<em>f</em>′（0）＝(0－1)e<sup>0</sup>＝－1，
所以切线方程为*y*＋2＝－(*x*－0)，即*x*＋*y*＋2＝0．  
（2）方法一　()<em>f</em>′(<em>x</em>)＝(<em>x</em>－1)(e<em><sup>x</sup></em>－<em>a</em>)，

①当<em>a</em>≤0时，因为<em>x</em>≥2，所以<em>x</em>－1&gt;0，e<em><sup>x</sup></em>－<em>a</em>&gt;0，所以<em>f</em>′(<em>x</em>)&gt;0，
则*f*(*x*)在[2，＋∞)上单调递增，*f*(*x*)≥*f*（2）＝0成立．

②当0&lt;<em>a</em>≤e<sup>2</sup>时，<em>f</em>′(<em>x</em>)≥0，所以<em>f</em>(<em>x</em>)在[2，＋∞)上单调递增，所以<em>f</em>(<em>x</em>)≥<em>f</em>（2）＝0成立．

③当<em>a</em>&gt;e<sup>2</sup>时，在区间(2，ln <em>a</em>)上，<em>f</em>′(<em>x</em>)&lt;0；在区间(ln<em>a</em>，＋∞)上，<em>f</em>′(<em>x</em>)&gt;0，
所以*f*(*x*)在(2，ln *a*)上单调递减，在(ln*a*，＋∞)上单调递增，*f*(*x*)≥0不恒成立，不符合题意．
综上所述，<em>a</em>的取值范围是(－∞，e<sup>2</sup>]．
方法二　当<em>x</em>≥2时，<em>f</em>(<em>x</em>)≥0恒成立，等价于当<em>x</em>≥2时，(<em>x</em>－2)e<em><sup>x</sup></em>－<em>ax</em><sup>2</sup>＋<em>ax</em>≥0恒成立．
即<em>a</em>≤(<em>x</em>－2)e<em><sup>x</sup></em>在[2，＋∞)上恒成立．
当<em>x</em>＝2时，0·<em>a</em>≤0，所以<em>a</em>∈<strong>R</strong>．
当<em>x</em>&gt;2时， <em>x</em><sup>2</sup>－<em>x</em>&gt;0，所以<em>a</em>≤＝恒成立．
设*g*(*x*)＝，则*g*′(*x*)＝，因为*x*>2，所以*g*′(*x*)>0，
所以<em>g</em>(<em>x</em>)在区间(2，＋∞)上单调递增．所以<em>g</em>(<em>x</em>)&gt;<em>g</em>（2）＝e<sup>2</sup>，所以<em>a</em>≤e<sup>2</sup>．
综上所述，<em>a</em>的取值范围是(－∞，e<sup>2</sup>]．

6．已知函数<em>f</em>(<em>x</em>)＝e<em><sup>ax</sup></em>－<em>ax</em>－1.  
（1）讨论函数*f*(*x*)的单调性；
![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)  
（2）设*m*为整数，且对于任意正整数*n*(*n*≥2)．若恒成立，求*m*的最小值．

6．解析：（1）<em>f</em>′(<em>x</em>)＝<em>a</em>e<em><sup>ax</sup></em>－<em>a</em>＝<em>a</em>(e<em><sup>ax</sup></em>－1)，
当*a*>0时，令*f*′(*x*)>0，解得*x*>0．所以*f*(*x*)在(0，＋∞)上单调递增；
当*a*＝0时，显然无单调区间；
当*a*<0时，令*f*′(*x*)>0，解得*x*>0，所以*f*(*x*)在(0，＋∞)上单调递增.

综上，当*a*＝0时，无单调区间；*a*≠0时，单调递减区间为(－∞，0)，单调递增区间为(0，＋∞).  
（2）令<em>a</em>＝1，由（1）可知<em>f</em>(<em>x</em>)的最小值为<em>f</em>（0）＝0，所以<em>f</em>(<em>x</em>)≥0．所以e<em><sup>x</sup></em>≥<em>x</em>＋1(当<em>x</em>＝0时取得“＝”).

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
令<em>x</em>＝<em>n</em>－1，则e<em><sup>n</sup></em><sup>－1</sup>&gt;<em>n</em>，所以e<sup>0</sup>·e<sup>1</sup>·e<sup>2</sup>·…·e<em><sup>n</sup></em><sup>－1</sup>&gt;1×2×3×…×<em>n</em>，即，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

两边进行次方得，所以*m*的最小值为3.

7．已知函数<em>f</em>(<em>x</em>)＝<em>x</em>ln <em>x</em>－<em>ax</em>＋1(<em>a</em>∈<strong>R</strong>)．  
（1）讨论*f*(*x*)在(1，＋∞)上的零点个数；  
（2）当*a*>1时，若存在*x*∈(1，＋∞)，使得*f*(*x*)<(e－1)·(*a*－3)，求实数*a*的取值范围．

7．解析　（1）由*f*(*x*)＝*x*ln *x*－*ax*＋1＝0可得*a*＝ln *x*＋，
令*g*(*x*)＝ln *x*＋，易知*g*′(*x*)＝－＝．
∴*g*′(*x*)>0在(1，＋∞)上恒成立，故*g*(*x*)在(1，＋∞)上单调递增．
又*g*（1）＝1，所以当*x*∈(1，＋∞)时，*g*(*x*)>1．
故当*a*≤1时，*f*(*x*)在(1，＋∞)上无零点；当*a*>1时，*f*(*x*)在(1，＋∞)上存在一个零点．  
（2）当<em>a</em>&gt;1时，由（1）得<em>f</em>(<em>x</em>)在(1，＋∞)上存在一个零点．由<em>f</em>′(<em>x</em>)＝ln <em>x</em>＋1－<em>a</em>＝0得<em>x</em>＝e<em><sup>a</sup></em><sup>－1</sup>，
所以<em>f</em>(<em>x</em>)在(1，e<em><sup>a</sup></em><sup>－1</sup>)上单调递减，在(e<em><sup>a</sup></em><sup>－1</sup>，＋∞)上单调递增，所以<em>f</em>(<em>x</em>)<sub>min</sub>＝<em>f</em>(e<em><sup>a</sup></em><sup>－1</sup>)＝1－e<em><sup>a</sup></em><sup>－1</sup>．
若存在*x*∈(1，＋∞)，使得*f*(*x*)<(e－1)(*a*－3)成立，

只需1－e<em><sup>a</sup></em><sup>－1</sup>&lt;(e－1)(<em>a</em>－3)成立，即不等式e<em><sup>a</sup></em><sup>－1</sup>＋(e－1)(<em>a</em>－3)－1&gt;0成立．
令<em>h</em>(<em>a</em>)＝e<em><sup>a</sup></em><sup>－1</sup>＋(e－1)(<em>a</em>－3)－1，<em>a</em>&gt;1，则<em>h</em>′(<em>a</em>)＝e<em><sup>a</sup></em><sup>－1</sup>＋e－1，

易知<em>h</em>′(<em>a</em>)＝e<em><sup>a</sup></em><sup>－1</sup>＋e－1&gt;0在(1，＋∞)上恒成立，
故<em>h</em>(<em>a</em>)＝e<em><sup>a</sup></em><sup>－1</sup>＋(e－1)(<em>a</em>－3)－1在(1，＋∞)上单调递增，又<em>h</em>（2）＝0，所以<em>a</em>&gt;2，
故实数*a*的取值范围为(2，＋∞)．

8．已知函数<em>f</em>(<em>x</em>)＝e<em><sup>x</sup></em><sup>－1</sup>－<em>ax</em>＋ln<em>x</em>(<em>a</em>∈<strong>R</strong>)．  
（1）若函数*f*(*x*)在*x*＝1处的切线与直线3*x*－*y*＝0平行，求*a*的值；  
（2）若不等式*f*(*x*)≥ln*x*－*a*＋1对一切*x*∈[1，＋∞)恒成立，求实数*a*的取值范围．

8．解析　（1）<em>f</em>′(<em>x</em>)＝e<em><sup>x</sup></em><sup>－1</sup>－<em>a</em>＋，∴<em>f</em>′（1）＝2－<em>a</em>＝3，∴<em>a</em>＝－1，
经检验*a*＝－1满足题意，∴*a*＝－1，  
（2）<em>f</em>(<em>x</em>)≥ln <em>x</em>－<em>a</em>＋1可化为e<em><sup>x</sup></em><sup>－1</sup>－<em>ax</em>＋<em>a</em>－1≥0，
令<em>φ</em>(<em>x</em>)＝e<em><sup>x</sup></em><sup>－1</sup>－<em>ax</em>＋<em>a</em>－1，则当<em>x</em>∈[1，＋∞)时，<em>φ</em>(<em>x</em>)<sub>min</sub>≥0，
∵<em>φ</em>′(<em>x</em>)＝e<em><sup>x</sup></em><sup>－1</sup>－<em>a</em>，

①当*a*≤0时，*φ*′(*x*)>0，∴*φ*(*x*)在[1，＋∞)上单调递增，
∴<em>φ</em>(<em>x</em>)<sub>min</sub>＝<em>φ</em>（1）＝1－<em>a</em>＋<em>a</em>－1＝0≥0恒成立，∴<em>a</em>≤0符合题意．

②当*a*>0时，令*φ*′(*x*)＝0，得*x*＝ln *a*＋1．
当*x*∈(－∞，ln *a*＋1)时，*φ*′(*x*)<0，当*x*∈(ln *a*＋1，＋∞)时，*φ*′(*x*)>0，
∴*φ*(*x*)在(－∞，ln *a*＋1)上单调递减，在(ln *a*＋1，＋∞)上单调递增．
当ln <em>a</em>＋1≤1即0&lt;<em>a</em>≤1时，<em>φ</em>(<em>x</em>)在[1，＋∞)上单调递增，<em>φ</em>(<em>x</em>)<sub>min</sub>＝<em>φ</em>（1）＝0≥0恒成立，∴0&lt;<em>a</em>≤1符合题意．
当ln *a*＋1>1，即*a*>1时，*φ*(*x*)在[1，ln *a*＋1)上单调递减，在(ln *a*＋1，＋∞)上单调递增，
∴<em>φ</em>(<em>x</em>)<sub>min</sub>＝<em>φ</em>(ln <em>a</em>＋1)&lt;<em>φ</em>（1）＝0与<em>φ</em>(<em>x</em>)≥0矛盾．故<em>a</em>&gt;1不符合题意．

综上，实数*a*的取值范围为{*a*|*a*≤1}．

9．已知正实数<em>a</em>，设函数<em>f</em>(<em>x</em>)＝<em>x</em><sup>2</sup>－<em>a</em><sup>2</sup><em>x</em>ln <em>x</em>．  
（1）若*a*＝，求实数*f*(*x*)在[1，e]的值域；  
（2）对任意实数*x*∈均有*f*(*x*)≥*a*恒成立，求实数*a*的取值范围．

9．解析　（1）当<em>a</em>＝时，函数<em>f</em>(<em>x</em>)＝<em>x</em><sup>2</sup>－2<em>x</em>ln <em>x</em>，则<em>f</em>′(<em>x</em>)＝2(<em>x</em>－1－ln <em>x</em>)．
设*F*(*x*)＝2(*x*－1－ln *x*)，*x*∈[1，e]，则*F*′(*x*)＝2≥0，
所以*F*′(*x*)在[1，e]上单调递增，*F*′(*x*)≥*F*′（1）＝0，所以*f*(*x*)在[1，e]上单调递增，
所以在[1，e]上<em>f</em>(<em>x</em>)∈[1，e<sup>2</sup>－2e]．  
（2）由题意可得*f*（1）≥*a*，即0<*a*≤1．
当0&lt;<em>a</em>≤1时，<em>x</em><sup>2</sup>－<em>a</em><sup>2</sup><em>x</em>ln <em>x</em>≥<em>a</em>，即－－<em>x</em>ln <em>x</em>≥0．

记<em>t</em>＝≥1，设<em>g</em>(<em>t</em>)＝<em>x</em><sup>2</sup><em>t</em><sup>2</sup>－<em>t</em>－<em>x</em>ln <em>x</em>，则<em>g</em>(<em>t</em>)为关于<em>t</em>的二次函数，

且定义域为[1，＋∞)，其对称轴为*t*＝．
因为当<em>x</em>∈时，4<em>x</em><sup>4</sup>＋1≥2<em>x</em>，所以&lt;1，当<em>a</em>&gt;0，<em>g</em>(<em>t</em>)≥<em>g</em>（1）＝<em>x</em>．
设函数*h*(*x*)＝*x*－－ln *x*，*x*≥，

*h*′(*x*)＝1－－＝．
当*x*∈时，*h*′(*x*)<0，*h*(*x*)在上单调递减；
当<em>x</em>∈(1，＋∞)时，<em>h</em>′(<em>x</em>)&gt;0，<em>h</em>(<em>x</em>)在(1，＋∞)上单调递增，所以<em>h</em>(<em>x</em>)<sub>min</sub>＝<em>h</em>（1）＝0，
即当*x*∈时，*h*(*x*)≥0，所以*g*(*t*)≥0，
所以0<*a*≤1．所以实数*a*的取值范围是(0，1]．

10．设函数<em>f</em>(<em>x</em>)＝<em>x</em>－，<em>g</em>(<em>x</em>)＝<em>t</em> ln <em>x</em>(<em>t</em>∈<strong>R</strong>)．  
（1）讨论函数*h*(*x*)＝*f*(*x*)＋*g*(*x*)的单调区间；  
（2）若当*x*∈(0，1)时，*f*(*x*)的图象恒在函数*g*(*x*)的图象的下方，求正实数*t*的取值范围．

10．解析　（1）*h*(*x*)＝*f*(*x*)＋*g*(*x*)＝*x*－＋*t* ln *x*(*x*>0)，则*h*′(*x*)＝1＋＋＝(*x*>0)．

①当*t*≥0时，*h*′(*x*)>0，∴*h*(*x*)的单调递增区间是(0，＋∞)，无减区间；
②当<em>t</em>＜0时，令<em>H</em>(<em>x</em>)＝<em>x</em><sup>2</sup>＋<em>tx</em>＋1，<em>Δ</em>＝<em>t</em><sup>2</sup>－4，<em>Δ</em>≤0，即－2≤<em>t</em>＜0时，<em>H</em>(<em>x</em>)≥0，即<em>h</em>′(<em>x</em>)≥0；
∴*h*(*x*)的单调递增区间是(0，＋∞)，无减区间，*Δ*＞0时，即*t*＜－2，
设<em>x</em><sub>1</sub>＝，<em>x</em><sub>2</sub>＝，
∵<em>x</em><sub>1</sub>＋<em>x</em><sub>2</sub>＝－<em>t</em>＞0，<em>x</em><sub>1</sub><em>x</em><sub>2</sub>＝1＞0，∴0＜<em>x</em><sub>1</sub>＜<em>x</em><sub>2</sub>，
∴(0，<em>x</em><sub>1</sub>)∪(<em>x</em><sub>2</sub>，＋∞)，时<em>H</em>(<em>x</em>)＞0，即<em>h</em>′(<em>x</em>)＞0，
∴<em>h</em>(<em>x</em>)的单调递增区间是(0，<em>x</em><sub>1</sub>)，(<em>x</em><sub>2</sub>，＋∞)，

同理，单调递减区间是(<em>x</em><sub>1</sub>，<em>x</em><sub>2</sub>)．

综上，①当*t*≥－2时，*h*(*x*)的单调递增区间是(0，＋∞)，无减区间，

②当<em>t</em>＜－2时，<em>h</em>(<em>x</em>)的单调递增区间是(0，<em>x</em><sub>1</sub>)，(<em>x</em><sub>2</sub>，＋∞)，单调递减区间是(<em>x</em><sub>1</sub>，<em>x</em><sub>2</sub>)，
其中<em>x</em><sub>1</sub>＝，<em>x</em><sub>2</sub>＝．  
（2）∵函数*f*(*x*)的图象恒在*g*(*x*)的图象的下方，
∴*f*(*x*)－*g*(*x*)＝*x*－－*t* ln *x*<0在区间(0，1)上恒成立．
设*F*(*x*)＝*x*－－*t* ln *x*，其中*x*∈(0，1)，
∴*F*′(*x*)＝1＋－＝，其中*t*＞0．

①当<em>t</em><sup>2</sup>－4≤0，即0＜<em>t</em>≤2时，<em>F</em>′(<em>x</em>)≥0，∴函数<em>F</em>(<em>x</em>)在(0，1)上单调递增，<em>F</em>(<em>x</em>)&lt;<em>F</em>（1）＝0，
故*f*(*x*)－*g*(*x*)＜0成立，满足题意．

②当<em>t</em><sup>2</sup>－4&gt;0，即<em>t</em>&gt;2时，设<em>φ</em>(<em>x</em>)＝<em>x</em><sup>2</sup>－<em>tx</em>＋1，
则*φ*(*x*)图象的对称轴方程为*x*＝>1，*φ*（0）＝1，*φ*（1）＝2－*t*＜0，
∴<em>φ</em>(<em>x</em>)在(0，1)上存在唯一实根，设为<em>x</em><sub>0</sub>，
则当<em>x</em>∈(<em>x</em><sub>0</sub>，1)，<em>φ</em>(<em>x</em>)＜0，<em>F</em>′(<em>x</em>)＜0，
∴<em>F</em>(<em>x</em>)在(<em>x</em><sub>0</sub>，1)上单调递减，此时<em>F</em>(<em>x</em>)＞<em>F</em>（1）＝0，不符合题意．

综上可得，正实数*t*的取值范围是(0，2]．

11．已知函数<em>f</em>(<em>x</em>)＝ln<em>x</em>＋<em>x</em>＋1，<em>g</em>(<em>x</em>)＝<em>x</em><sup>2</sup>＋2<em>x</em>．  
（1）求函数*φ*(*x*)＝*f*(*x*)－*g*(*x*)的极值；  
（2）若*m*为整数，对任意的*x*＞0都有*f*(*x*)－*mg*(*x*)≤0成立，求实数*m*的最小值．

11．<strong>解析</strong>　（1）由<em>φ</em>(<em>x</em>)＝<em>f</em>(<em>x</em>)－<em>g</em>(<em>x</em>)＝ln <em>x</em>＋<em>x</em>＋1－<em>x</em><sup>2</sup>－2<em>x</em>＝ln <em>x</em>－<em>x</em><sup>2</sup>－<em>x</em>＋1(<em>x</em>＞0)，
得*φ*′(*x*)＝－2*x*－1＝(*x*＞0)，令*φ*′(*x*)＞0，解得0＜*x*＜，令*φ*′(*x*)＜0，解得*x*＞，
所以函数*φ*(*x*)的单调递增区间是，单调递减区间是，
故函数*φ*(*x*)的极大值是*φ*＝ln－－＋1＝－ln 2，函数*φ*(*x*)无极小值．  
（2）设<em>h</em>(<em>x</em>)＝<em>f</em>(<em>x</em>)－<em>mg</em>(<em>x</em>)＝ln <em>x</em>－<em>mx</em><sup>2</sup>＋(1－2<em>m</em>)<em>x</em>＋1，
则*h*′(*x*)＝－2*mx*＋1－2*m*＝＝(*x*＞0)．
当*m*≤0时，因为*x*＞0，所以2*mx*－1＜0，*x*＋1＞0，所以*h*′(*x*)＞0，故*h*(*x*)在(0，＋∞)上单调递增，
又因为<em>h</em>（1）＝ln 1－<em>m</em>×1<sup>2</sup>＋(1－2<em>m</em>)＋1＝－3<em>m</em>＋2＞0，不满足题意，所以舍去．
当*m*＞0时，令*h*′(*x*)＞0，得0＜*x*＜，令*h*′(*x*)＜0，得*x*＞，
故*h*(*x*)在上单调递增，在上单调递减，
所以<em>h</em>(<em>x</em>)<sub>max</sub>＝<em>h</em>＝ln－<em>m</em>·<sup>2</sup>＋(1－2<em>m</em>)·＋1＝－ln(2<em>m</em>)．
令*t*(*m*)＝－ln(2*m*)(*m*＞0)，显然*t*(*m*)在(0，＋∞)上单调递减，

且*t*＝＞0，*t*（1）＝－ln 2＝(1－ln 16)＜0，
故当*m*≥1时，*t*(*m*)＜0，满足题意，故整数*m*的最小值为1．

12．设函数<em>f</em>(<em>x</em>)＝2<em>x</em>ln<em>x</em>－2<em>ax</em><sup>2</sup>(<em>a</em>∈<strong>R</strong>)．  
（1）当*a*＝时，求函数*f*(*x*)的单调区间；  
（2）若*f*(*x*)≤－ln*x*－1(*f*′(*x*)为*f*(*x*)的导函数)在(1，＋∞)上恒成立，求实数*a*的取值范围．

12．解析　（1）当<em>a</em>＝时，<em>f</em>(<em>x</em>)＝2<em>x</em>ln <em>x</em>－<em>x</em><sup>2</sup>，定义域为(0，＋∞)．∴<em>f</em>′(<em>x</em>)＝2ln <em>x</em>－2<em>x</em>＋2．
令*g*(*x*)＝*f*′(*x*)＝2ln*x*－2*x*＋2(*x*>0)，∴*g*′(*x*)＝－2．
当*x*∈(0，1)时，*g*′(*x*)>0，故*g*(*x*)为增函数；当*x*∈(1，＋∞)时，*g*′(*x*)<0，故*g*(*x*)为减函数．
∴*g*(*x*)≤*g*（1）＝2ln 1－2×1＋2＝0，即*f*′(*x*)≤0．
∴函数*f*(*x*)的单调递减区间为(0，＋∞)，无单调递增区间．  
（2）<em>f</em>(<em>x</em>)＝2<em>x</em>ln<em>x</em>－2<em>ax</em><sup>2</sup>，∴<em>f</em>′(<em>x</em>)＝2ln<em>x</em>－4<em>ax</em>＋2，且<em>x</em>&gt;0．
∴<em>f</em>(<em>x</em>)≤－ln <em>x</em>－1在(1，＋∞)上恒成立⇔2(<em>x</em>ln<em>x</em>－<em>ax</em><sup>2</sup>)≤ln<em>x</em>－2<em>ax</em>＋1－ln<em>x</em>－1在(1，＋∞)上恒成立

⇔ln*x*－*ax*＋*a*≤0在(1，＋∞)上恒成立．
令*h*(*x*)＝ln*x*－*ax*＋*a*，*x*∈(1，＋∞)．则*h*′(*x*)＝－*a*，且*h*（1）＝ln1－*a*＋*a*＝0．
当*a*≤0，*h*′(*x*)>0恒成立，故*h*(*x*)在(1，＋∞)上为增函数．
∴*h*(*x*)>*h*（1）＝0，即*a*≤0时不满足题意．当*a*>0时，由*h*′(*x*)＝0，得*x*＝．

①若*a*∈(0，1)，则∈(1，＋∞)，故*h*(*x*)在上为减函数，在上为增函数．
∴存在<em>x</em><sub>0</sub>∈，使得<em>h</em>(<em>x</em><sub>0</sub>)&gt;<em>h</em>（1）＝0．这与<em>h</em>(<em>x</em>)＝ln <em>x</em>－<em>ax</em>＋<em>a</em>≤0在(1，＋∞)上恒成立矛盾．
因此*a*∈(0，1)时不满足题意．

②若*a*∈[1，＋∞)，则∈(0，1]，故*h*(*x*)在(1，＋∞)上为减函数，
∴*h*(*x*)<*h*（1）＝0，∴*h*(*x*)≤0恒成立，故符合题意．
综上所述，实数*a*的取值范围是[1，＋∞)．

