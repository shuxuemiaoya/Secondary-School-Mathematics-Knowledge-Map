**专题17　单变量不含参不等式证明方法之虚设零点**

![](images/a089eaabaf66d5c942a2bb596ab18d1471edb52f273182c77a9e4f268055a6d8.jpg)

隐零点法本质上是最值分析法，常见形式是证明<em>h</em>(<em>x</em>)＞0或<em>f</em>(<em>x</em>)&gt;<em>g</em>(<em>x</em>)．对于<em>f</em>(<em>x</em>)&gt;<em>g</em>(<em>x</em>)，先将不等式移项，即构造函数<em>h</em>(<em>x</em>)＝<em>f</em>(<em>x</em>)－<em>g</em>(<em>x</em>)，转化为证不等式<em>h</em>(<em>x</em>)&gt;0，再转化为证明<em>h</em>(<em>x</em>)<sub>min</sub>&gt;0即可，但对函数<em>h</em>(<em>x</em>)求导后，<em>f</em>′(<em>x</em>)＝0是超越形式，我们无法利用目前所学知识求出导函数零点，但零点是存在的，我们称之为隐零点(即能确定其存在，但又无法用显性的代数表达)．用隐零点证明不等式时，先证明函数<em>f</em>′(<em>x</em>)在某区上单调，然后用零点存在性定理说明只有一个零点．此时设出零点<em>x</em><sub>0</sub>，则<em>f</em>′(<em>x</em><sub>0</sub>)＝0．<em>f</em>(<em>x</em>) <sub>min</sub>＝<em>f</em>(<em>x</em><sub>0</sub>)，而<em>f</em>(<em>x</em><sub>0</sub>)是一个超越式(含有指、对函数)和多项式函数的组合式，这时用<em>f</em>′(<em>x</em><sub>0</sub>)＝0把超越式用代数式表示，同时根据<em>x</em><sub>0</sub>的范围可进行适当的放缩．从而问题得以解决．

**【例题选讲】**

<strong>[例1]</strong>　已知函数<em>f</em>(<em>x</em>)＝<em>a</em>e<em><sup>x</sup></em>－<em>b</em>ln<em>x</em>，曲线<em>y</em>＝<em>f</em> (<em>x</em>)在点(1，<em>f</em> (1))处的切线方程为<em>y</em>＝<em>x</em>＋1．

(1)求*a*，*b*；

(2)证明：*f* (*x*)>0．

解析　(1)函数<em>f</em> (<em>x</em>)的定义域为(0，＋∞)．<em>f</em> ′(<em>x</em>)＝<em>a</em>e<em><sup>x</sup></em>－，由题意得<em>f</em> (1)＝，<em>f</em> ′(1)＝－1，

所以解得

(2)证明：由(1)知<em>f</em> (<em>x</em>)＝·e<em><sup>x</sup></em>－ln <em>x</em>(<em>x</em>&gt;0)．因为<em>f</em> ′(<em>x</em>)＝e<em><sup>x</sup></em><sup>－2</sup>－在(0，＋∞)上单调递增，又<em>f</em> ′(1)&lt;0，<em>f</em> ′(2)&gt;0，

所以<em>f</em> ′(<em>x</em>)＝0在(0，＋∞)上有唯一实根<em>x</em><sub>0</sub>，且<em>x</em><sub>0</sub>∈(1，2)．

当<em>x</em>∈(0，<em>x</em><sub>0</sub>)时，<em>f</em> ′(<em>x</em>)&lt;0，当<em>x</em>∈(<em>x</em><sub>0</sub>，＋∞)时，<em>f</em> ′(<em>x</em>)&gt;0，

从而当<em>x</em>＝<em>x</em><sub>0</sub>时，<em>f</em> (<em>x</em>)取极小值，也是最小值．由<em>f</em> ′(<em>x</em><sub>0</sub>)＝0，得e<em>x</em><sub>0</sub>－2＝，则<em>x</em><sub>0</sub>－2＝－ln <em>x</em><sub>0</sub>．

故<em>f</em> (<em>x</em>)≥<em>f</em> (<em>x</em><sub>0</sub>)＝e <em>x</em><sub>0</sub>－2－ln <em>x</em><sub>0</sub>＝＋<em>x</em><sub>0</sub>－2&gt;2－2＝0，所以<em>f</em> (<em>x</em>)&gt;0．

<strong>[例2]</strong>　(2015全国Ⅰ改编)设函数<em>f</em>(<em>x</em>)＝e<sup>2</sup><em><sup>x</sup></em>－<em>a</em>ln <em>x</em>．

(1)讨论*f*(*x*)的导函数*f*′(*x*)零点的个数；

(2)求证：当*a*＝2时，*f*(*x*)≥4．

解析　(1)法一：<em>f</em>′(<em>x</em>)＝2e<sup>2</sup><em><sup>x</sup></em>－(<em>x</em>＞0)．

当<em>a</em>≤0时，<em>f</em>′(<em>x</em>)＞0，<em>f</em>′(<em>x</em>)没有零点．当<em>a</em>＞0时，设<em>u</em>(<em>x</em>)＝e<sup>2</sup><em><sup>x</sup></em>，<em>v</em>(<em>x</em>)＝－，

因为<em>u</em>(<em>x</em>)＝e<sup>2</sup><em><sup>x</sup></em>在(0，＋∞)上单调递增，<em>v</em>(<em>x</em>)＝－在(0，＋∞)上单调递增，

所以*f*′(*x*)在(0，＋∞)上单调递增．

又因为*f*′(*a*)＞0，当*b*满足0＜*b*＜且*b*＜时，*f*′(*b*)＜0，所以当*a*＞0时，*f*′(*x*)存在唯一零点．

法二：<em>f</em>′(<em>x</em>)＝2e<sup>2</sup><em><sup>x</sup></em>－(<em>x</em>＞0)．令方程<em>f</em>′(<em>x</em>)＝0，得<em>a</em>＝2<em>x</em>e<sup>2</sup><em><sup>x</sup></em>(<em>x</em>＞0)．

因为函数<em>g</em>(<em>x</em>)＝2<em>x</em>(<em>x</em>＞0)，<em>h</em>(<em>x</em>)＝e<sup>2</sup><em><sup>x</sup></em>(<em>x</em>＞0)均是函数值为正值的增函数，

所以由增函数的定义可证得函数<em>u</em>(<em>x</em>)＝2<em>x</em>e<sup>2</sup><em><sup>x</sup></em>(<em>x</em>＞0)也是增函数，其值域是(0，＋∞)．

由此可得，当*a*≤0时，*f*′(*x*)无零点；当*a*＞0时，*f*′(*x*)有唯一零点．

(2)由(1)可设<em>f</em>′(<em>x</em>)在(0，＋∞)上的唯一零点为<em>x</em><sub>0</sub>．

当<em>x</em>∈(0，<em>x</em><sub>0</sub>)时，<em>f</em>′(<em>x</em>)＜0；当<em>x</em>∈(<em>x</em><sub>0</sub>，＋∞)时，<em>f</em>′(<em>x</em>)＞0．

所以<em>f</em>(<em>x</em>)在(0，<em>x</em><sub>0</sub>)上单调递减，在(<em>x</em><sub>0</sub>，＋∞)上单调递增，

当且仅当<em>x</em>＝<em>x</em><sub>0</sub>时，<em>f</em>(<em>x</em>)取得最小值，最小值为<em>f</em>(<em>x</em><sub>0</sub>)．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

因为－＝0，2<em>x</em><sub>0</sub>＝－ln <em>x</em><sub>0</sub>所以<em>f</em>(<em>x</em><sub>0</sub>)＝＋4<em>x</em><sub>0</sub>≥4(当且仅当<em>x</em><sub>0</sub>＝时等号成立)．

所以当*a*＝2时，*f*(*x*)≥4．

<strong>[例3]</strong>　已知函数<em>f</em>(<em>x</em>)＝<em>ax</em>＋ln<em>x</em>，函数<em>g</em>(<em>x</em>)的导函数<em>g</em>′(<em>x</em>)＝e<em><sup>x</sup></em>，且<em>g</em>(0) <em>g</em>′(1)＝e，其中e为自然对数的底数．

(1)求*f*(*x*)的极值；

(2)当*a*＝0时，对于任意的*x*∈(0，＋∞)，求证：*f*(*x*)<*g*(*x*)－2．

解析　(1)函数*f*(*x*)的定义域为(0，＋∞)，*f*′(*x*)＝*a*＋＝．

当*a*≥0时，*f*′(*x*)＞0，所以*f*(*x*)在(0，＋∞)上为增函数，*f*(*x*)没有极值；

当*a*＜0时，令*f*′(*x*)＞0，解得*x*＜－，所以*f*(*x*)在(0，－)单调增，在(－，＋∞)单调递减．

所以*f*(*x*)有极大值*f*(－)＝－1－ln(－*a*)，无极小值．

(2)当<em>a</em>＝1时，<em>f</em>(<em>x</em>)＝ln <em>x</em>，令<em>h</em>(<em>x</em>)＝<em>g</em>(<em>x</em>)－<em>f</em>(<em>x</em>)－2，即<em>h</em>(<em>x</em>)＝e<em><sup>x</sup></em>－ln <em>x</em>－2，即证<em>g</em>(<em>x</em>)<sub>min</sub>&gt;0恒成立，

<em>h</em>′(<em>x</em>)＝e<em><sup>x</sup></em>－，<em>h</em>′(<em>x</em>)(0，＋∞)在为增函数，<em>h</em>′&lt;0，<em>h</em>′(1)&gt;0，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

∴∃<em>x</em><sub>0</sub>∈，使<em>h</em>′(<em>x</em><sub>0</sub>)＝0成立，即－＝0，则当0&lt;<em>x</em>&lt;<em>x</em><sub>0</sub>时，<em>h</em>′(<em>x</em>)&lt;0，当<em>x</em>&gt;<em>x</em><sub>0</sub>时，<em>h</em>′(<em>x</em>)&gt;0，

∴<em>y</em>＝<em>h</em>(<em>x</em>)在(0，<em>x</em><sub>0</sub>)上单调递减，在(<em>x</em><sub>0</sub>，＋∞)上单调递增，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

∴<em>h</em>(<em>x</em>)<sub>min</sub>＝<em>h</em>(<em>x</em><sub>0</sub>)＝－ln <em>x</em><sub>0</sub>－2，又∵－＝0，即＝，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

∴<em>h</em>(<em>x</em><sub>0</sub>)＝－ln <em>x</em><sub>0</sub>－2＝＋ln－2＝＋<em>x</em><sub>0</sub>－2，又∵<em>x</em><sub>0</sub>∈，∴<em>x</em><sub>0</sub>＋&gt;2，

∴<em>h</em>(<em>x</em><sub>0</sub>)&gt;0，∴<em>h</em>(<em>x</em>)&gt;<em>h</em>(<em>x</em><sub>0</sub>)&gt;0，即<em>f</em>(<em>x</em>)&lt;<em>g</em>(<em>x</em>)－2．

<strong>[例4]</strong>　(2017·全国Ⅱ)已知函数<em>f</em>(<em>x</em>)＝<em>ax</em><sup>2</sup>－<em>ax</em>－<em>x</em>ln<em>x</em>，且<em>f</em>(<em>x</em>)≥0．

(1)求*a*；

(2)证明：<em>f</em>(<em>x</em>)存在唯一的极大值点<em>x</em><sub>0</sub>，且e<sup>－2</sup>&lt;<em>f</em>(<em>x</em><sub>0</sub>)&lt;2<sup>－2</sup>．

<strong>解析</strong>　(1)<em>f</em>(<em>x</em>)的定义域为(0，＋∞)．设<em>g</em>(<em>x</em>)＝<em>ax</em>－<em>a</em>－ln <em>x</em>，则<em>f</em>(<em>x</em>)＝<em>xg</em>(<em>x</em>)，<em>f</em>(<em>x</em>)≥0等价于<em>g</em>(<em>x</em>)≥0．

因为*g*(1)＝0，*g*(*x*)≥0，故*g*′(1)＝0，而*g*′(*x*)＝*a*－，*g*′(1)＝*a*－1，得*a*＝1．

若*a*＝1，则*g*′(*x*)＝1－．当0<*x*<1时，*g*′(*x*)<0，*g*(*x*)单调递减；当*x*>1时，*g*′(*x*)>0，*g*(*x*)单调递增．

所以*x*＝1是*g*(*x*)的极小值点，故*g*(*x*)≥*g*(1)＝0．综上，*a*＝1．

(2)由(1)知<em>f</em>(<em>x</em>)＝<em>x</em><sup>2</sup>－<em>x</em>－<em>x</em>ln <em>x</em>，<em>f</em>′(<em>x</em>)＝2<em>x</em>－2－ln <em>x</em>．

设*h*(*x*)＝2*x*－2－ln *x*，则*h*′(*x*)＝2－．当*x*∈时，*h*′(*x*)<0；当*x*∈时，*h*′(*x*)>0．

所以<em>h</em>(<em>x</em>)在单调递减，在单调递增．又<em>h</em>(e<sup>－2</sup>)&gt;0，<em>h</em>&lt;0，<em>h</em>(1)＝0，

所以<em>h</em>(<em>x</em>)在有唯一零点<em>x</em><sub>0</sub>，在有唯一零点1，

且当<em>x</em>∈(0，<em>x</em><sub>0</sub>)时，<em>h</em>(<em>x</em>)&gt;0；当<em>x</em>∈(<em>x</em><sub>0</sub>，1)时，<em>h</em>(<em>x</em>)&lt;0；当<em>x</em>∈(1，＋∞)时，<em>h</em>(<em>x</em>)&gt;0．

因为<em>f</em>′(<em>x</em>)＝<em>h</em>(<em>x</em>)，所以<em>x</em>＝<em>x</em><sub>0</sub>是<em>f</em>(<em>x</em>)的唯一极大值点．由<em>f</em>′(<em>x</em><sub>0</sub>)＝0得ln <em>x</em><sub>0</sub>＝2(<em>x</em><sub>0</sub>－1)，

故<em>f</em>(<em>x</em><sub>0</sub>)＝<em>x</em><sub>0</sub>(1－<em>x</em><sub>0</sub>)．由<em>x</em><sub>0</sub>∈(0，1)得<em>f</em>(<em>x</em><sub>0</sub>)&lt;．因为<em>x</em>＝<em>x</em><sub>0</sub>是<em>f</em>(<em>x</em>)在(0，1)的最大值点，

由e<sup>－1</sup>∈(0，1)，<em>f</em>′(e<sup>－1</sup>)≠0得<em>f</em>(<em>x</em><sub>0</sub>)&gt;<em>f</em>(e<sup>－1</sup>)＝e<sup>－2</sup>，所以e<sup>－2</sup>&lt;<em>f</em>(<em>x</em><sub>0</sub>)&lt;2<sup>－2</sup>．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

【**对点精练**】

1．(2013·全国Ⅱ改编)设函数<em>f</em>(<em>x</em>)＝e<em><sup>x</sup></em>－ln(<em>x</em>＋<em>m</em>)．

(1)若*x*＝0是*f*(*x*)的极值点，求*m*的值，并讨论*f*(*x*)的单调性；

(2)当*m*＝2时，求证：*f*(*x*)>0．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

1．解析　(1)*f*′(*x*)＝．由*x*＝0是*f*(*x*)的极值点得*f*′(0)＝0，所以*m*＝1．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

于是<em>f</em>(<em>x</em>)＝e<em><sup>x</sup></em>－ln(<em>x</em>＋1)，定义域为(－1，＋∞)，<em>f</em>′(<em>x</em>)＝．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

函数*f*′(*x*)＝在(－1，＋∞)单调递增，且*f*′(0)＝0．

因此当*x*∈(－1，0)时，*f*′(*x*)＜0；当*x*∈(0，＋∞)时，*f*′(*x*)＞0．

所以*f*(*x*)在(－1，0)单调递减，在(0，＋∞)单调递增．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

(2)当*m*＝2时，函数*f*′(*x*)＝在(－2，＋∞)单调递增．又*f*′(－1)＜0，*f*′(0)＞0，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

故<em>f</em>′(<em>x</em>)＝0在(－2，＋∞)有唯一实根<em>x</em><sub>0</sub>，即<em>f</em>′(<em>x</em><sub>0</sub>)＝0得＝，ln(<em>x</em><sub>0</sub>＋2)＝－<em>x</em><sub>0</sub>，且<em>x</em><sub>0</sub>∈(－1，0)．

当<em>x</em>∈(－2，<em>x</em><sub>0</sub>)时，<em>f</em>′(<em>x</em>)＜0；当<em>x</em>∈(<em>x</em><sub>0</sub>，＋∞)时，<em>f</em>′(<em>x</em>)＞0，从而当<em>x</em>＝<em>x</em><sub>0</sub>时，<em>f</em>(<em>x</em>)取得最小值．

所以<em>f</em>(<em>x</em>)在(－2，<em>x</em><sub>0</sub>)上单调递减，在(<em>x</em><sub>0</sub>，＋∞)单调递增．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

故<em>f</em>(<em>x</em>)≥<em>f</em>(<em>x</em><sub>0</sub>)＝＋<em>x</em><sub>0</sub>＝＞0．综上，当<em>m</em>＝2时，<em>f</em>(<em>x</em>)＞0．

2．已知函数<em>f</em>(<em>x</em>)＝<em>x</em><sup>2</sup>－(<em>a</em>－2)<em>x</em>－<em>a</em>ln<em>x</em>，<em>a</em>&gt;0．

(1)求函数*y*＝*f*(*x*)的单调区间；

(2)当<em>a</em>＝1时，证明：对任意的<em>x</em>&gt;0，<em>f</em>(<em>x</em>)＋e<em><sup>x</sup></em>&gt;<em>x</em><sup>2</sup>＋<em>x</em>＋2．

2．解析　(1)<em>f</em>(<em>x</em>)＝<em>x</em><sup>2</sup>－(<em>a</em>－2)<em>x</em>－<em>a</em>ln<em>x</em>，<em>a</em>&gt;0，定义域为(0，＋∞)，<em>f</em>′(<em>x</em>)＝2<em>x</em>－(<em>a</em>－2)－＝，

令*f*′(*x*)>0，得*x*>；令*f*′(*x*)<0，得0<*x*<．

∴函数*y*＝*f*(*x*)的单调递减区间为，单调递增区间为．

(2)方法一　∵<em>a</em>＝1，∴<em>f</em>(<em>x</em>)＝<em>x</em><sup>2</sup>＋<em>x</em>－ln <em>x</em>(<em>x</em>&gt;0)，即证e<em><sup>x</sup></em>－ln <em>x</em>－2&gt;0恒成立，

令<em>g</em>(<em>x</em>)＝e<em><sup>x</sup></em>－ln <em>x</em>－2，<em>x</em>∈(0，＋∞)，即证<em>g</em>(<em>x</em>)<sub>min</sub>&gt;0恒成立，

<em>g</em>′(<em>x</em>)＝e<em><sup>x</sup></em>－，<em>g</em>′(<em>x</em>)为增函数，<em>g</em>′&lt;0，<em>g</em>′(1)&gt;0，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

∴∃<em>x</em><sub>0</sub>∈，使<em>g</em>′(<em>x</em><sub>0</sub>)＝0成立，即－＝0，则当0&lt;<em>x</em>&lt;<em>x</em><sub>0</sub>时，<em>g</em>′(<em>x</em>)&lt;0，当<em>x</em>&gt;<em>x</em><sub>0</sub>时，<em>g</em>′(<em>x</em>)&gt;0，

∴<em>y</em>＝<em>g</em>(<em>x</em>)在(0，<em>x</em><sub>0</sub>)上单调递减，在(<em>x</em><sub>0</sub>，＋∞)上单调递增，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

∴<em>g</em>(<em>x</em>)<sub>min</sub>＝<em>g</em>(<em>x</em><sub>0</sub>)＝－ln <em>x</em><sub>0</sub>－2，又∵－＝0，即＝，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

∴<em>g</em>(<em>x</em><sub>0</sub>)＝－ln <em>x</em><sub>0</sub>－2＝＋ln －2＝＋<em>x</em><sub>0</sub>－2，又∵<em>x</em><sub>0</sub>∈，∴<em>x</em><sub>0</sub>＋&gt;2，

∴<em>g</em>(<em>x</em><sub>0</sub>)&gt;0，即对任意的<em>x</em>&gt;0，<em>f</em>(<em>x</em>)＋e<em><sup>x</sup></em>&gt;<em>x</em><sup>2</sup>＋<em>x</em>＋2．

方法二　令<em>φ</em>(<em>x</em>)＝e<em><sup>x</sup></em>－<em>x</em>－1，∴<em>φ</em>′(<em>x</em>)＝e<em><sup>x</sup></em>－1，

∴<em>φ</em>(<em>x</em>)在(－∞，0)上单调递减，在(0，＋∞)上单调递增，∴<em>φ</em>(<em>x</em>)<sub>min</sub>＝<em>φ</em>(0)＝0，∴e<em><sup>x</sup></em>≥<em>x</em>＋1，①

令*h*(*x*)＝ln *x*－*x*＋1(*x*>0)，∴*h*′(*x*)＝－1＝，

∴<em>h</em>(<em>x</em>)在(0,1)上单调递增，在(1，＋∞)上单调递减，∴<em>h</em>(<em>x</em>)<sub>max</sub>＝<em>h</em>(1)＝0，

∴ln *x*≤*x*－1，∴*x*＋1≥ln *x*＋2，②

要证<em>f</em>(<em>x</em>)＋e<em><sup>x</sup></em>&gt;<em>x</em><sup>2</sup>＋<em>x</em>＋2，即证e<em><sup>x</sup></em>&gt;ln <em>x</em>＋2，

由①②知e<em><sup>x</sup></em>≥<em>x</em>＋1≥ln <em>x</em>＋2，且两等号不能同时成立，

∴e<em><sup>x</sup></em>&gt;ln <em>x</em>＋2，即证原不等式成立．

3．已知函数<em>f</em>(<em>x</em>)＝e<sup>－</sup><em><sup>x</sup></em>＋<em>ax</em>(<em>a</em>∈<strong>R</strong>)．

(1)讨论*f*(*x*)的最值；

(2)若<em>a</em>＝0，证明：<em>f</em>(<em>x</em>)&gt;－<em>x</em><sup>2</sup>＋．

3．<strong>解析</strong>　(1)依题意，得<em>f</em>′(<em>x</em>)＝－e<sup>－</sup><em><sup>x</sup></em>＋<em>a</em>.

![](images/ae237c392b72c64201c018ffe89e788bd92e08e774b1ae56cc2b3a616a90ca91.png)

①当<em>a</em>≤0时，<em>f</em>′(<em>x</em>)&lt;0，所以<em>f</em>(<em>x</em>)在<strong>R</strong>单调递减，故<em>f</em>(<em>x</em>)不存在最大值和最小值；

②当*a*>0时，由*f*′(*x*)＝0得，*x*＝－ln*a*.

当*x*∈(－∞，－ln*a*)时，*f*′(*x*)<0，*f*(*x*)为减函数，当*x*∈(－ln*a*，＋∞)时，*f*′(*x*)>0，*f*(*x*)为增函数，

∴<em>f</em>(<em>x</em>)<sub>min</sub>＝<em>f</em>(<em>x</em>)<sub>极小值</sub>＝<em>f</em>(－ln<em>a</em>)＝<em>a</em>－<em>a</em>ln<em>a</em>，无最大值．

![](images/ae237c392b72c64201c018ffe89e788bd92e08e774b1ae56cc2b3a616a90ca91.png)

综上，当*a*≤0时，*f*(*x*)不存在最大值和最小值；当*a*>0时，*f*(*x*)的最小值为*a*－*a*ln*a*．无最大值．

(2)当<em>a</em>＝0，<em>f</em>(<em>x</em>)＝e<sup>－</sup><em><sup>x</sup></em>，设<em>g</em>(<em>x</em>)＝e<sup>－</sup><em><sup>x</sup></em>＋<em>x</em><sup>2</sup>－，则<em>g</em>′(<em>x</em>)＝－e<sup>－</sup><em><sup>x</sup></em>＋<em>x</em>，

设<em>p</em>(<em>x</em>)＝－e<sup>－</sup><em><sup>x</sup></em>＋<em>x</em>，由<em>p</em>′(<em>x</em>)＝e<sup>－</sup><em><sup>x</sup></em>＋1&gt;0，可知<em>g</em>′(<em>x</em>)在<strong>R</strong>上单调递增．因为<em>g</em>′()&lt;0，<em>g</em>′(1)&gt;0，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

所以存在唯一的<em>x</em><sub>0</sub>∈(，1)，使得<em>g</em>′(<em>x</em><sub>0</sub>)＝0．即＝<em>x</em><sub>0</sub>，

∴当<em>x</em>∈(－∞，，<em>x</em><sub>0</sub>)时，<em>g</em>′(<em>x</em>)&lt;0，<em>g</em>(<em>x</em>)为减函数，当<em>x</em>∈(<em>x</em><sub>0</sub>，＋∞)时，<em>g</em>′(<em>x</em>)&gt;0，<em>g</em>(<em>x</em>)为增函数，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

故当<em>x</em>＝<em>x</em><sub>0</sub>时，<em>g</em>(<em>x</em>)取得极小值，也是最小值，即<em>g</em>(<em>x</em>)<sub>min</sub>＝<em>g</em>(<em>x</em><sub>0</sub>)＝＋－.

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

由＝<em>x</em><sub>0</sub>，所以<em>g</em>(<em>x</em><sub>0</sub>)＝＋<em>x</em><sub>0</sub>－．又<em>x</em><sub>0</sub>∈(，1)，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

所以<em>g</em>(<em>x</em><sub>0</sub>)＝＋<em>x</em><sub>0</sub>－&gt;＋－＝0，所以<em>g</em>(<em>x</em>) ≥<em>g</em>(<em>x</em><sub>0</sub>)＝0，即e<sup>－</sup><em><sup>x</sup></em>&gt;－<em>x</em><sup>2</sup>＋，

所以不等式<em>f</em>(<em>x</em>)&gt;－<em>x</em><sup>2</sup>＋成立．

4．已知<em>f</em>(<em>x</em>)＝(<em>x</em>－1)e<em><sup>x</sup></em>＋<em>ax</em><sup>2</sup>．

(1)当*a*＝e时，求*f*(*x*)的极值；

(2)对∀<em>x</em>&gt;1，求证：<em>f</em>(<em>x</em>)≥<em>ax</em><sup>2</sup>＋<em>x</em>＋1＋ln(<em>x</em>－1)．

4．解析　(1)当<em>a</em>＝e时，<em>f</em>′(<em>x</em>)＝<em>x</em>(e<em><sup>x</sup></em>＋e)．

当*x*∈(－∞，0)时，*f*′(*x*)<0，*f*(*x*)为减函数，当*x*∈(0，＋∞)时，*f*′(*x*)>0，*f*(*x*)为增函数，

∴<em>f</em>(<em>x</em>)<sub>极小值</sub>＝<em>f</em>(0)＝－1，无极大值．

(2)令<em>g</em>(<em>x</em>)＝<em>f</em>(<em>x</em>)－ln(<em>x</em>－1)－<em>ax</em><sup>2</sup>－<em>x</em>－1＝(<em>x</em>－1)e<em><sup>x</sup></em>－ln(<em>x</em>－1)－<em>x</em>－1，<em>x</em>∈(1，＋∞)，

<em>g</em>′(<em>x</em>)＝<em>x</em>e<em><sup>x</sup></em>－－1＝<em>x</em>e<em><sup>x</sup></em>－＝<em>x</em>，<em>x</em>∈(1，＋∞)．

令<em>h</em>(<em>x</em>)＝e<em><sup>x</sup></em>－，<em>x</em>∈(1，＋∞)，<em>h</em>′(<em>x</em>)＝e<em><sup>x</sup></em>＋&gt;0，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

∴<em>h</em>(<em>x</em>)为(1，＋∞)上的增函数，<em>h</em>(2)＝e<sup>2</sup>－1&gt;0，取<em>x</em>－1＝e<sup>－2</sup>，<em>x</em>＝1＋e<sup>－2</sup>，<em>h</em>(1＋e<sup>－2</sup>)＝－e<sup>2</sup>&lt;0，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

∴存在唯一的<em>x</em><sub>0</sub>∈(1，2)使<em>h</em>(<em>x</em><sub>0</sub>)＝0，即＝，

∴当<em>x</em>∈(1，<em>x</em><sub>0</sub>)时，<em>h</em>(<em>x</em>)&lt;0，<em>g</em>′(<em>x</em>)&lt;0，<em>g</em>(<em>x</em>)为减函数，当<em>x</em>∈(<em>x</em><sub>0</sub>，＋∞)时，<em>h</em>(<em>x</em>)&gt;0，<em>g</em>′(<em>x</em>)&gt;0，<em>g</em>(<em>x</em>)为增函数，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

∴<em>g</em>(<em>x</em>)<sub>min</sub>＝<em>g</em>(<em>x</em><sub>0</sub>)＝(<em>x</em><sub>0</sub>－1)－ln(<em>x</em><sub>0</sub>－1)－<em>x</em><sub>0</sub>－1＝(<em>x</em><sub>0</sub>－1)×－ln－<em>x</em><sub>0</sub>－1＝1＋<em>x</em><sub>0</sub>－<em>x</em><sub>0</sub>－1＝0，

∴对∀<em>x</em>&gt;1，<em>g</em>(<em>x</em>)≥<em>g</em>(<em>x</em><sub>0</sub>)＝0，即<em>f</em>(<em>x</em>)≥<em>ax</em><sup>2</sup>＋<em>x</em>＋1＋ln(<em>x</em>－1)．

5．已知函数<em>f</em>(<em>x</em>)＝ln<em>x</em>＋<em>ax</em><sup>2</sup>＋<em>x</em>＋1．

(1)当*a*＝－2时，求*f*(*x*)的极值点；

(2)当<em>a</em>＝0时，证明：对任意的<em>x</em>&gt;0，不等式<em>x</em>e<em><sup>x</sup></em>≥<em>f</em>(<em>x</em>)恒成立．

5．解析　(1)当<em>a</em>＝－2时，<em>f</em>(<em>x</em>)＝ln<em>x</em>－<em>x</em><sup>2</sup>＋<em>x</em>＋1．

*f*′(*x*)＝－2*x*＋1＝＝－．

因为*f*(*x*)的定义域为(0，＋∞)，所以，*x*＝1．

当*x*∈(0，1)时，*f*′(*x*)>0，*f*(*x*)为增函数；当*x*∈(1，＋∞)时，*f*′(*x*) <0，*f*(*x*)为减函数．

所以，*f*(*x*)的极值点为*x*＝1．

(2)当<em>a</em>＝0时，要证对任意的<em>x</em>&gt;0，不等式<em>x</em>e<em><sup>x</sup></em>≥<em>f</em>(<em>x</em>)恒成立，

即证<em>x</em>&gt;0时，<em>x</em>e<em><sup>x</sup></em>≥ln<em>x</em>＋<em>x</em>＋1恒成立，即证<em>x</em>(e<em><sup>x</sup></em>－1)－ln<em>x</em>－1≥0恒成立，

令<em>g</em>(<em>x</em>)＝<em>x</em>(e<em><sup>x</sup></em>－1)－ln<em>x</em>－1，<em>g</em>′(<em>x</em>)＝<em>x</em>(e<em><sup>x</sup></em>＋1)－－1＝，

再令<em>h</em>(<em>x</em>)＝<em>x</em>e<em><sup>x</sup></em>－1，<em>h</em>′(<em>x</em>)＝(<em>x</em>＋1) e<em><sup>x</sup></em>&gt;0，∴<em>h</em>(<em>x</em>)为(0，＋∞)上的增函数，

又*h*(0)＝－1<0，*h*(1)＝e－1>0，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

∴存在唯一的<em>x</em><sub>0</sub>∈(0，1)使<em>h</em>(<em>x</em><sub>0</sub>)＝0，即，

∴当<em>x</em>∈(0，<em>x</em><sub>0</sub>)时，<em>h</em>(<em>x</em>)&lt;0，<em>g</em>′(<em>x</em>)&lt;0，<em>g</em>(<em>x</em>)为减函数，当<em>x</em>∈(<em>x</em><sub>0</sub>，1)时，<em>h</em>(<em>x</em>)&gt;0，<em>g</em>′(<em>x</em>)&gt;0，<em>g</em>(<em>x</em>)为增函数，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

∴<em>g</em>(<em>x</em>)<sub>min</sub>＝<em>g</em>(<em>x</em><sub>0</sub>)＝＝，由，得，－ln<em>x</em><sub>0</sub>＝<em>x</em><sub>0</sub>．

∴<em>g</em>(<em>x</em>)<sub>min</sub>＝<em>g</em>(<em>x</em><sub>0</sub>)＝1－<em>x</em><sub>0</sub>－1＋<em>x</em><sub>0</sub>＝0

∴对∀<em>x</em>&gt;0，<em>g</em>(<em>x</em>)≥<em>g</em>(<em>x</em><sub>0</sub>)＝0，<em>x</em>e<em><sup>x</sup></em>≥ln<em>x</em>＋<em>x</em>＋1恒成立，即对任意的<em>x</em>&gt;0，不等式<em>x</em>e<em><sup>x</sup></em>≥<em>f</em>(<em>x</em>)恒成立．

6．设函数<em>f</em>(<em>x</em>)＝<em>x</em>＋<em>ax</em>ln <em>x</em>(<em>a</em>∈<strong>R</strong>)．

(1)讨论函数*f*(*x*)的单调性；

(2)若函数<em>f</em>(<em>x</em>)的极大值点为<em>x</em>＝1，证明：<em>f</em>(<em>x</em>)≤e<sup>－</sup><em><sup>x</sup></em>＋<em>x</em><sup>2</sup>．

6．解析　(1)*f*(*x*)的定义域为(0，＋∞)，*f*′(*x*)＝1＋*a*ln *x*＋*a*，

当*a*＝0时，*f*(*x*)＝*x*，则函数*f*(*x*)在区间(0，＋∞)上单调递增；

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

当*a*>0时，由*f*′(*x*)>0得*x*>，由*f*′(*x*)<0得0<*x*<．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

所以*f*(*x*)在区间上单调递减，在区间上单调递增；

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

当*a*<0时，由*f*′(*x*)>0得0<*x*<，由*f*′(*x*)<0得*x*>，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

所以函数*f*(*x*)在区间上单调递增，在区间上单调递减．

综上所述，当*a*＝0时，函数*f*(*x*)在区间(0，＋∞)上单调递增；

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

当*a*>0时，函数*f*(*x*)在区间上单调递减，在区间上单调递增；

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

当*a*<0时，函数*f*(*x*)在区间上单调递增，在区间上单调递减．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

(2)由(1)知<em>a</em>&lt;0且＝1，解得<em>a</em>＝－1，<em>f</em>(<em>x</em>)＝<em>x</em>－<em>x</em>ln <em>x</em>．要证<em>f</em>(<em>x</em>)≤e<sup>－</sup><em><sup>x</sup></em>＋<em>x</em><sup>2</sup>，

即证<em>x</em>－<em>x</em>ln <em>x</em>≤e<sup>－</sup><em><sup>x</sup></em>＋<em>x</em><sup>2</sup>，即证1－ln <em>x</em>≤＋<em>x</em>．

令*F*(*x*)＝ln *x*＋＋*x*－1(*x*>0)，则*F*′(*x*)＝＋＋1＝．

令<em>g</em>(<em>x</em>)＝<em>x</em>－e<sup>－</sup><em><sup>x</sup></em>，得函数<em>g</em>(<em>x</em>)在区间(0，＋∞)上单调递增．而<em>g</em>(1)＝1－&gt;0，<em>g</em>(0)＝－1&lt;0，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

所以在区间(0，＋∞)上存在唯一的实数<em>x</em><sub>0</sub>，使得<em>g</em>(<em>x</em><sub>0</sub>)＝<em>x</em><sub>0</sub>－＝0，即<em>x</em><sub>0</sub>＝，

且<em>x</em>∈(0，<em>x</em><sub>0</sub>)时，<em>g</em>(<em>x</em>)&lt;0，<em>x</em>∈(<em>x</em><sub>0</sub>，＋∞)时，<em>g</em>(<em>x</em>)&gt;0．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

故<em>F</em>(<em>x</em>)在(0，<em>x</em><sub>0</sub>)上单调递减，在(<em>x</em><sub>0</sub>，＋∞)上单调递增．∴<em>F</em>(<em>x</em>)<sub>min</sub>＝<em>F</em>(<em>x</em><sub>0</sub>)＝ln <em>x</em><sub>0</sub> ＋＋<em>x</em><sub>0</sub>－1．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

又＝<em>x</em><sub>0</sub>，∴<em>F</em>(<em>x</em>)<sub>min</sub>＝ln <em>x</em><sub>0</sub>＋＋<em>x</em><sub>0</sub>－1＝－<em>x</em><sub>0</sub>＋1＋<em>x</em><sub>0</sub>－1＝0．∴<em>F</em>(<em>x</em>)≥<em>F</em>(<em>x</em><sub>0</sub>)＝0成立，

即<em>f</em>(<em>x</em>)≤e<sup>－</sup><em><sup>x</sup></em>＋<em>x</em><sup>2</sup>成立．

