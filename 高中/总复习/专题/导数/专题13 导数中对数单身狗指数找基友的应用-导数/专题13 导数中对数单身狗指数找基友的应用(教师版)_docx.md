专题13　导数中对数单身狗指数找基友的应用

![](images/952133273f5d2eaf0cf8943d18dccffd43567af6a928033813970d7d026d3048.jpg)

导数在高考中占据了及其重要的地位，导数是研究函数的一个重要的工具，在判断函数的单调性、求函数的极值、最值与解决函数的零点(方程的根)、不等式问题中都用到导数．而这类问题都有一条经验性规则：对数单身狗，指数找基友，指对在一起，常常要分手．

考点一　对数单身狗

【方法总结】
在证明或处理含对数函数的不等式时，如*f*(*x*)为可导函数，则有(*f*(*x*)ln*x*)′＝*f*′(*x*)ln*x*＋，若*f*(*x*)为非常数函数，求导式子中含有ln*x*，这类问题需要多次求导，烦琐复杂．通常要将对数型的函数“独立分离”出来，这样再对新函数求导时，就不含对数了，只需一次就可以求出它的极值点，从而避免了多次求导．这种相当于让对数函数“孤军奋战”的变形过程，我们形象的称之为“对数单身狗”．

1．设*f*(*x*)>0，*f*(*x*)ln*x*＋*g*(*x*)>0ln*x*＋>0，则(ln*x*＋)′＝＋()′，不含超越函数，求解过程简单．或者*f*(*x*)ln*x*＋*g*(*x*)>0*f*(*x*)(ln*x*＋)>0，即将前面部分提出，就留下ln*x*这个单身狗，然后研究剩余部分．

2．设*f*(*x*)≠0，*f*(*x*)ln*x*＋*g*(*x*)＝0ln*x*＋＝0，则(ln*x*＋)′＝＋()′，不含超越函数，求解过程简单．或者*f*(*x*)ln*x*＋*g*(*x*)＝0*f*(*x*)(ln*x*＋)＝0，即将前面部分提出，就留下ln*x*这个单身狗，然后研究剩余部分．

【例题选讲】

<strong>[例1]</strong> (2016·全国Ⅱ)已知函数<em>f</em>(<em>x</em>)＝(<em>x</em>＋1)ln<em>x</em>－<em>a</em>(<em>x</em>－1)．  
（1）当*a*＝4时，求曲线*y*＝*f*(*x*)在(1，*f*（1）)处的切线方程；  
（2）若当*x*∈(1，＋∞)时，*f*(*x*)＞0，求*a*的取值范围．
解析　（1）*f*(*x*)的定义域为(0，＋∞)．当*a*＝4时，*f*(*x*)＝(*x*＋1)ln *x*－4(*x*－1)，

*f*（1）＝0，*f*′(*x*)＝ln *x*＋－3，*f*′（1）＝－2．故曲线*y*＝*f*(*x*)在(1，*f*（1）)处的切线方程为2*x*＋*y*－2＝0．  
（2）当*x*∈(1，＋∞)时，*f*(*x*)＞0等价于ln *x*－＞0．
设*g*(*x*)＝ln *x*－，则*g*′(*x*)＝－＝，*g*（1）＝0．

①当<em>a</em>≤2，<em>x</em>∈(1，＋∞)时，<em>x</em><sup>2</sup>＋2(1－<em>a</em>)<em>x</em>＋1≥<em>x</em><sup>2</sup>－2<em>x</em>＋1＞0，
故*g*′(*x*)＞0，*g*(*x*)在(1，＋∞)上单调递增，因此*g*(*x*)＞0；
②当<em>a</em>＞2时，令<em>g</em>′(<em>x</em>)＝0得<em>x</em><sub>1</sub>＝<em>a</em>－1－，<em>x</em><sub>2</sub>＝<em>a</em>－1＋．
由<em>x</em><sub>2</sub>＞1和<em>x</em><sub>1</sub><em>x</em><sub>2</sub>＝1得0&lt;<em>x</em><sub>1</sub>＜1，故当<em>x</em>∈(1，<em>x</em><sub>2</sub>)时，<em>g</em>′(<em>x</em>)＜0，<em>g</em>(<em>x</em>)在(1，<em>x</em><sub>2</sub>)上单调递减，
因此*g*(*x*)＜*g*（1）＝0．

综上，*a*的取值范围是(－∞，2]．

<strong>[例2]</strong>已知函数<em>f</em>(<em>x</em>)＝＋，曲线<em>y</em>＝<em>f</em>(<em>x</em>)在点(1，<em>f</em>（1）)处的切线方程为<em>x</em>＋2<em>y</em>－3＝0．  
（1）求*a*，*b*的值；  
（2）证明：当*x*＞0，且*x*≠1时，*f*(*x*)＞．

<strong>解析</strong>　（1）<em>f</em>′(<em>x</em>)＝－(<em>x</em>＞0)．由于直线<em>x</em>＋2<em>y</em>－3＝0的斜率为－，且过点(1，1)，
故即解得  
（2）由（1）知*f*(*x*)＝＋(*x*＞0)，所以*f*(*x*)－＝．

考虑函数*h*(*x*)＝2ln *x*－(*x*＞0)，则*h*′(*x*)＝－＝－．
所以当*x*≠1时，*h*′(*x*)＜0．而*h*（1）＝0，故当*x*∈(0，1)时，*h*(*x*)＞0，可得*h*(*x*)＞0；
当*x*∈(1，＋∞)时，*h*(*x*)＜0，可得*h*(*x*)＞0．从而当*x*＞0，且*x*≠1时，*f*(*x*)－＞0，即*f*(*x*)＞．

【对点精练】

1．若不等式<te<te<te<text style="it*a*lic">x</text>t style="italic">x</text>t style="it*a*lic">x</text>t style="italic">x</text>ln x≥a(x－1) $)$ 对所<te<te<te<text style="it*a*lic">x</text>t style="italic">x</text>t style="it*a*lic">x</text>t style="italic">x</text>≥1有都成立，求实数a的取值范围．

1．<strong>解析</strong>　原问题等价于ln<em>x</em>－≥0对所有<em>x</em>≥1都成立，
令*h*(*x*)＝ln*x*－(*x*≥1)，则*f*′(*x*)＝．  
（1）当*a*≤1时，*f*′(*x*)＝≥0恒成立，即*f*(*x*)在[1，＋∞)上单调递增，因而*f*(*x*) ≥*f*（1）＝0恒成立；  
（2）当*a*>1时，令*f*′(*x*)＝0，则*x*＝*a*，*f*(*x*)在(0，*a*)上单调递减，在(*a*，＋∞)上单调递增，

<em>f</em>(<em>x</em>)<sub>min</sub>＝<em>f</em>(<em>a</em>)＝ln<em>a</em>－<em>a</em>＋1，不合题意．综上所述，实数<em>a</em>的取值范围是(－∞，1]．

2．(2017·全国Ⅱ)已知函数<em>f</em>(<em>x</em>)＝<em>ax</em><sup>2</sup>－<em>ax</em>－<em>x</em>ln <em>x</em>，且<em>f</em>(<em>x</em>)≥0．  
（1）求*a*；  
（2）证明：<em>f</em>(<em>x</em>)存在唯一的极大值点<em>x</em><sub>0</sub>，且e<sup>－2</sup>&lt;<em>f</em>(<em>x</em><sub>0</sub>)&lt;2<sup>－2</sup>．

2．<strong>解析</strong>　（1）<em>f</em>(<em>x</em>)的定义域为(0，＋∞)．设<em>g</em>(<em>x</em>)＝<em>ax</em>－<em>a</em>－ln <em>x</em>，则<em>f</em>(<em>x</em>)＝<em>xg</em>(<em>x</em>)，<em>f</em>(<em>x</em>)≥0等价于<em>g</em>(<em>x</em>)≥0．
因为*g*（1）＝0，*g*(*x*)≥0，故*g*′（1）＝0，而*g*′(*x*)＝*a*－，*g*′（1）＝*a*－1，得*a*＝1．
若*a*＝1，则*g*′(*x*)＝1－．当0<*x*<1时，*g*′(*x*)<0，*g*(*x*)单调递减；当*x*>1时，*g*′(*x*)>0，*g*(*x*)单调递增．
所以*x*＝1是*g*(*x*)的极小值点，故*g*(*x*)≥*g*（1）＝0．综上，*a*＝1．  
（2）由（1）知<em>f</em>(<em>x</em>)＝<em>x</em><sup>2</sup>－<em>x</em>－<em>x</em>ln <em>x</em>，<em>f</em>′(<em>x</em>)＝2<em>x</em>－2－ln <em>x</em>．
设*h*(*x*)＝2*x*－2－ln *x*，则*h*′(*x*)＝2－．当*x*∈时，*h*′(*x*)<0；当*x*∈时，*h*′(*x*)>0．
所以<em>h</em>(<em>x</em>)在单调递减，在单调递增．又<em>h</em>(e<sup>－2</sup>)&gt;0，<em>h</em>&lt;0，<em>h</em>（1）＝0，
所以<em>h</em>(<em>x</em>)在有唯一零点<em>x</em><sub>0</sub>，在有唯一零点1，

且当<em>x</em>∈(0，<em>x</em><sub>0</sub>)时，<em>h</em>(<em>x</em>)&gt;0；当<em>x</em>∈(<em>x</em><sub>0，</sub>1)时，<em>h</em>(<em>x</em>)&lt;0；当<em>x</em>∈(1，＋∞)时，<em>h</em>(<em>x</em>)&gt;0．
因为<em>f</em>′(<em>x</em>)＝<em>h</em>(<em>x</em>)，所以<em>x</em>＝<em>x</em><sub>0</sub>是<em>f</em>(<em>x</em>)的唯一极大值点．由<em>f</em>′(<em>x</em><sub>0</sub>)＝0得ln <em>x</em><sub>0</sub>＝2(<em>x</em><sub>0</sub>－1)，
故<em>f</em>(<em>x</em><sub>0</sub>)＝<em>x</em><sub>0</sub>(1－<em>x</em><sub>0</sub>)．由<em>x</em><sub>0</sub>∈(0，1)得<em>f</em>(<em>x</em><sub>0</sub>)&lt;．因为<em>x</em>＝<em>x</em><sub>0</sub>是<em>f</em>(<em>x</em>)在(0，1)的最大值点，
由e<sup>－1</sup>∈(0，1)，<em>f</em>′(e<sup>－1</sup>)≠0得<em>f</em>(<em>x</em><sub>0</sub>)&gt;<em>f</em>(e<sup>－1</sup>)＝e<sup>－2</sup>，所以e<sup>－2</sup>&lt;<em>f</em>(<em>x</em><sub>0</sub>)&lt;2<sup>－2</sup>．

3．(2018·全国Ⅲ)已知函数<em>f</em>(<em>x</em>)＝(2＋<em>x</em>＋<em>ax</em><sup>2</sup>)·ln(1＋<em>x</em>)－2<em>x</em>．  
（1）若*a*＝0，证明：当－1<*x*<0时，*f*(*x*)<0；当*x*>0时，*f*(*x*)>0；  
（2）若*x*＝0是*f*(*x*)的极大值点，求*a*．

3．解析　（1）当*a*＝0时，*f*(*x*)＝(2＋*x*)ln(1＋*x*)－2*x*，*f*′(*x*)＝ln(1＋*x*)－．
设函数*g*(*x*)＝ln(1＋*x*)－，则*g*′(*x*)＝．
当－1<*x*<0时，*g*′(*x*)<0；当*x*>0时，*g*′(*x*)>0，故当*x*>－1时，*g*(*x*)≥*g*（0）＝0，

且仅当*x*＝0时，*g*(*x*)＝0，从而*f*′(*x*)≥0，且仅当*x*＝0时，*f*′(*x*)＝0．
所以*f*(*x*)在(－1，＋∞)上单调递增．又*f*（0）＝0，
故当－1<*x*<0时，*f*(*x*)<0；当*x*>0时，*f*(*x*)>0．

另解　当*a*＝0时，*f*(*x*)＝(2＋*x*)ln(1＋*x*)－2*x*(*x*>－1)，由于2＋*x*>0．故令*g*(*x*)＝ln(1＋*x*)－，

*g*′(*x*)＝－＝，故*x*∈(－1，＋∞)，*g*′（0） >0．所以*g*(*x*)在(－1，＋∞)上单调递增．
因为*g*（0）＝0，所以，当－1<*x*<0时，*gx*)<0；当*x*>0时，*g*(*x*)>0，
故当－1<*x*<0时，*f*(*x*)<0；当*x*>0时，*f*(*x*)>0．  
（2）①若*a*≥0，由（1）知，当*x*>0时，*f*(*x*)≥(2＋*x*)ln(1＋*x*)－2*x*>0＝*f*（0），这与*x*＝0是*f*(*x*)的极大值点矛盾．

②若*a*<0，设函数*h*(*x*)＝＝ln(1＋*x*)－．
由于当|<em>x</em>|&lt;min时，2＋<em>x</em>＋<em>ax</em><sup>2</sup>&gt;0，故<em>h</em>(<em>x</em>)与<em>f</em>(<em>x</em>)符号相同．又<em>h</em>（0）＝<em>f</em>（0）＝0，
故*x*＝0是*f*(*x*)的极大值点，当且仅当*x*＝0是*h*(*x*)的极大值点．

*h*′(*x*)＝－＝．
若6*a*＋1>0，则当0<*x*<－，且|*x*|<min时，*h*′(*x*)>0，故*x*＝0不是*h*(*x*)的极大值点．
若6<em>a</em>＋1&lt;0，则<em>a</em><sup>2</sup><em>x</em><sup>2</sup>＋4<em>ax</em>＋6<em>a</em>＋1＝0存在根<em>x</em><sub>1</sub>&lt;0，
故当<em>x</em>∈(<em>x</em><sub>1</sub>，0)，且|<em>x</em>|&lt;min时，<em>h</em>′(<em>x</em>)&lt;0，所以<em>x</em>＝0不是<em>h</em>(<em>x</em>)的极大值点．
若6*a*＋1＝0，则*h*′(*x*)＝，则当*x*∈(－1，0)时，*h*′(*x*)>0；当*x*∈(0，1)时，*h*′(*x*)<0．
所以*x*＝0是*h*(*x*)的极大值点，从而*x*＝0是*f*(*x*)的极大值点．综上，*a*＝－．

考点二　指数找基友

【方法总结】
在证明或处理含指数函数的不等式时，通常要将指数型的函数“结合”起来，即让指数型的函数乘以或除以一个多项式函数，这样再对新函数求导时，只需一次就可以求出它的极值点，从而避免了多次求导．这种相当于让指数函数寻找“合作伙伴”的变形过程，我们形象的称之为“指数找基友”．

1．由e<em><sup>x</sup></em>＋<em>f</em>(<em>x</em>)&gt;01＋&gt;0，则(1＋)′＝是一个多项式函数，变形后可大大简化运算．

2．由e<em><sup>x</sup></em>＋<em>f</em>(<em>x</em>)＝01＋＝0，则(1＋)′＝是一个多项式函数，变形后可大大简化运算．

【例题选讲】

<strong>[例3]</strong> (2018·全国Ⅱ)已知函数<em>f</em>(<em>x</em>)＝e<em><sup>x</sup></em>－<em>ax</em><sup>2</sup>．  
（1）若*a*＝1，证明：当*x*≥0时，*f*(*x*)≥1；  
（2）若*f*(*x*)在(0，＋∞)只有一个零点，求*a*．

<strong>解析</strong>　（1）当<em>a</em>＝1时，<em>f</em>(<em>x</em>)≥1等价于(<em>x</em><sup>2</sup>＋1)e<sup>－</sup><em><sup>x</sup></em>－1≤0．
设函数<em>g</em>(<em>x</em>)＝(<em>x</em><sup>2</sup>＋1)e<sup>－</sup><em><sup>x</sup></em>－1，则<em>g</em>′(<em>x</em>)＝－(<em>x</em><sup>2</sup>－2<em>x</em>＋1)e<sup>－</sup><em><sup>x</sup></em>＝－(<em>x</em>－1)<sup>2</sup>e<sup>－</sup><em><sup>x</sup></em>．
当*x*≠1时，*g*′(*x*)＜0，所以*g*(*x*)在(0，＋∞)上单调递减．而*g*（0）＝0，故当*x*≥0时，*g*(*x*)≤0，即*f*(*x*)≥1．

另解　当<em>a</em>＝1时，<em>f</em>(<em>x</em>)＝e<em><sup>x</sup></em>－<em>x</em><sup>2</sup>，则<em>f</em>′(<em>x</em>)＝e<em><sup>x</sup></em>－2<em>x</em>．
令<em>g</em>(<em>x</em>)＝<em>f</em>′(<em>x</em>)，则<em>g</em>′(<em>x</em>)＝e<em><sup>x</sup></em>－2．令<em>g</em>′(<em>x</em>)＝0，解得<em>x</em>＝ln2．
当*x*∈(0，ln2)时，*g*′(*x*)<0；当*x*∈(ln2，＋∞)时，*g*′(*x*)>0．
∴当*x*≥0时，*g*(*x*)≥*g*(ln2)＝2－2ln2>0，
∴*f*(*x*)在[0，＋∞)上单调递增，∴*f*(*x*)≥*f*（0）＝1．  
（2）设函数<em>h</em>(<em>x</em>)＝1－<em>ax</em><sup>2</sup>e<sup>－</sup><em><sup>x</sup></em>．<em>f</em>(<em>x</em>)在(0，＋∞)上只有一个零点等价于<em>h</em>(<em>x</em>)在(0，＋∞)上只有一个零点．

(ⅰ)当*a*≤0时，*h*(*x*)＞0，*h*(*x*)没有零点；
(ⅱ)当<em>a</em>＞0时，<em>h</em>′(<em>x</em>)＝<em>ax</em>(<em>x</em>－2)e<sup>－</sup><em><sup>x</sup></em>．
当*x*∈(0，2)时，*h*′(*x*)＜0；当*x*∈(2，＋∞)时，*h*′(*x*)＞0．
所以*h*(*x*)在(0，2)上单调递减，在(2，＋∞)上单调递增．
故*h*（2）＝1－是*h*(*x*)在(0，＋∞)上的最小值．

①当*h*（2）＞0，即*a*＜时，*h*(*x*)在(0，＋∞)上没有零点．

②当*h*（2）＝0，即*a*＝时，*h*(*x*)在(0，＋∞)上只有一个零点．

③当*h*（2）＜0，即*a*＞时，因为*h*（0）＝1，所以*h*(*x*)在(0，2)上有一个零点．
由（1）知，当<em>x</em>＞0时，e<em><sup>x</sup></em>＞<em>x</em><sup>2</sup>，所以<em>h</em>(4<em>a</em>)＝1－＝1－＞1－＝1－＞0，
故*h*(*x*)在(2，4*a*)上有一个零点．因此*h*(*x*)在(0，＋∞)上有两个零点．

综上，当*f*(*x*)在(0，＋∞)上只有一个零点时，*a*＝．

另解(参变分离)　若<em>f</em>(<em>x</em>)在(0，＋∞)上只有一个零点，即方程e<em><sup>x</sup></em>－<em>ax</em><sup>2</sup>＝0在(0，＋∞)上只有一个解，
由*a*＝，令*φ*(*x*)＝，*x*∈(0，＋∞)，*φ*′(*x*)＝，令*φ*′(*x*)＝0，解得*x*＝2．
当*x*∈(0，2)时，*φ*′(*x*)<0；当*x*∈(2，＋∞)时，*φ*′(*x*)>0．
∴<em>φ</em>(<em>x</em>)<sub>min</sub>＝<em>φ</em>（2）＝．∴<em>a</em>＝．

<strong>[例4]</strong>(2020·全国Ⅰ)已知函数<em>f</em>(<em>x</em>)＝e<em><sup>x</sup></em>＋<em>ax</em><sup>2</sup>－<em>x</em>．  
（1）当*a*＝1时，讨论*f*(*x*)的单调性；  
（2）当<em>x</em>≥0时，<em>f</em>(<em>x</em>)≥<em>x</em><sup>3</sup>＋1，求<em>a</em>的取值范围．

<strong>解析</strong>　（1）当<em>a</em>＝1时，<em>f</em>(<em>x</em>)＝e<em><sup>x</sup></em>＋<em>x</em><sup>2</sup>－<em>x</em>，<em>f</em>′(<em>x</em>)＝e<em><sup>x</sup></em>＋2<em>x</em>－1，
由于<em>f</em>″(<em>x</em>)＝e<em><sup>x</sup></em>＋2＞0，故<em>f</em>′(<em>x</em>)单调递增，注意到<em>f</em>′（0）＝0，
故当*x*∈(－∞，0)时，*f*′(*x*)＜0，*f*(*x*)单调递减，当*x*∈(0，＋∞)时，*f*′(*x*)＞0，*f*(*x*)单调递增．  
（2） <em>f</em>(<em>x</em>)≥<em>x</em><sup>3</sup>＋1等价于(<em>x</em><sup>3</sup>－<em>ax</em><sup>2</sup>＋<em>x</em>＋1) e<sup>－</sup><em><sup>x</sup></em>≤1．
设函数<em>g</em>(<em>x</em>)＝(<em>x</em><sup>3</sup>－<em>ax</em><sup>2</sup>＋<em>x</em>＋1) e<sup>－</sup><em><sup>x</sup></em>(<em>x</em>≥0)，则<em>g</em>′(<em>x</em>)＝－(<em>x</em><sup>3</sup>－<em>ax</em><sup>2</sup>＋<em>x</em>＋1－<em>x</em><sup>2</sup>＋2<em>ax</em>－1) e<sup>－</sup><em><sup>x</sup></em>

＝－<em>x</em>[<em>x</em><sup>2</sup>－(2<em>a</em>＋3)<em>x</em>＋4<em>a</em>＋2]e<sup>－</sup><em><sup>x</sup></em>＝－<em>x</em>(<em>x</em>－2<em>a</em>－1) (<em>x</em>－2)e<sup>－</sup><em><sup>x</sup></em>．

（i）若2*a*+1≤0，即*a*≤－，则当*x*∈（0，2）时，*g*′(*x*)>0．
所以*g*（*x*）在（0，2）单调递增，而*g*（0）=1，故当*x*∈（0，2）时，*g*（*x*）>1，不合题意．

（ii）若0<2*a*+1<2，即－<*a*<，则当*x*∈(0，2*a*+1)∪(2，+∞)时，*g'*(*x*)<0；当*x*∈(2*a*+1，2)时，*g'*(*x*)>0．
所以*g*(*x*)在(0，2*a*+1)，(2，+∞)单调递减，在(2*a*+1，2)单调递增．
由于<em>g</em>（0）=1，所以<em>g</em>(<em>x</em>)≤1当且仅当<em>g</em>（2）=(7−4<em>a</em>)e<sup>−2</sup>≤1，即<em>a</em>≥．所以当≤<em>a</em>&lt;时，<em>g</em>(<em>x</em>)≤1．

（iii）若2<em>a</em>+1≥2，即<em>a</em>≥，则<em>g</em>(<em>x</em>)≤(<em>x</em><sup>3</sup>＋<em>x</em>＋1)e<sup>－</sup><em><sup>x</sup></em>．
由于0∈[，)，故由（ii）可得(<em>x</em><sup>3</sup>－<em>ax</em><sup>2</sup>＋<em>x</em>＋1) e<sup>－</sup><em><sup>x</sup></em>≤1．故当时<em>a</em>≥，<em>g</em>(<em>x</em>)≤1．

综上，*a*的取值范围是．

另解(参变分离)　由<em>f</em>(<em>x</em>)≥<em>x</em><sup>3</sup>＋1，得e<em><sup>x</sup></em>＋<em>ax</em><sup>2</sup>－<em>x</em>≥<em>x</em><sup>3</sup>＋1，其中<em>x</em>≥0，

①当*x*＝0时，不等式为1≥1，显然成立，符合题意；
②当*x*＞0时，分离参数*a*得*a*≥－，

记*g*(*x*)＝－，*g*′(*x*)＝－，
令<em>h</em>(<em>x</em>)＝e<em><sup>x</sup></em>－<em>x</em><sup>2</sup>－<em>x</em>－1(<em>x</em>≥0)，则<em>h</em>′(<em>x</em>)＝e<em><sup>x</sup></em>－<em>x</em>－1，<em>h</em>″(<em>x</em>)＝e<em><sup>x</sup></em>－1≥0，
故*h*′(*x*)单调递增，*h*′(*x*)≥*h*′（0）＝0，故函数*h*(*x*)单调递增，*h*(*x*)≥*h*（0）＝0，
由<em>h</em>(<em>x</em>)≥0可得e<em><sup>x</sup></em>－<em>x</em><sup>2</sup>－<em>x</em>－1≥0恒成立，
故当*x*∈(0，2)时，*g*′(*x*)＞0，*g*(*x*)单调递增；当*x*∈(2，＋∞)时，*g*′(*x*)＜0，*g*(*x*)单调递减．
因此，<em>g</em>(<em>x</em>)<sub>max</sub>＝<em>g</em>（2）＝，综上可得，实数<em>a</em>的取值范围是．

【对点精练】

1．已知函数<em>f</em>(<em>x</em>)＝e<em><sup>x</sup></em>－1－<em>x</em>－<em>ax</em><sup>2</sup>，当<em>x</em>≥0时，<em>f</em>(<em>x</em>)≥0恒成立，求实数<em>a</em>的取值范围．

1．解析　解法一　由<em>f</em>′(<em>x</em>)＝e<em><sup>x</sup></em>－1－2<em>ax</em>，又e<em><sup>x</sup></em>≥<em>x</em>＋1，所以<em>f</em>′(<em>x</em>)＝e<em><sup>x</sup></em>－1－2<em>ax</em>≥<em>x</em>－2<em>ax</em>＝(1－2<em>a</em>)<em>x</em>，
所以当1－2*a*≥0，即*a*≤时，*f*′(*x*)≥0(*x*≥0)，而*f*（0）＝0，于是当*x*≥0时，*f*(*x*)≥0，满足题意；
又<em>x</em>≠0时，e<em><sup>x</sup></em>＞<em>x</em>＋1，所以可得e<sup>－</sup><em><sup>x</sup></em>＞1－<em>x</em>，
从而当<em>a</em>＞时，<em>f</em>′(<em>x</em>)＝e<em><sup>x</sup></em>－1－2<em>ax</em>≤e<em><sup>x</sup></em>－e<em><sup>x</sup></em>·e<sup>－</sup><em><sup>x</sup></em>＋2<em>a</em>(e<sup>－</sup><em><sup>x</sup></em>－1)＝(1－e<sup>－</sup><em><sup>x</sup></em>)·(e<em><sup>x</sup></em>－2<em>a</em>)，
故当*x*∈(0，ln2*a*)时，*f*′(*x*)＜0，而*f*（0）＝0，于是当*x*∈(0，ln2*a*)时，*f*(*x*)＜0，不合题意．
综上所述，实数*a*的取值范围为．
解法二　因为e<em><sup>x</sup></em>≥<em>x</em>＋1，所以当<em>a</em>≤0时，e<em><sup>x</sup></em>≥<em>ax</em><sup>2</sup>＋<em>x</em>＋1恒成立，故只需讨论<em>a</em>＞0的情形．
令<em>F</em>(<em>x</em>)＝e<sup>－</sup><em><sup>x</sup></em>(1＋<em>x</em>＋<em>ax</em><sup>2</sup>)－1，问题等价于<em>F</em>(<em>x</em>)≤0，
由<em>F</em>′(<em>x</em>)＝e<sup>－</sup><em><sup>x</sup></em>[－<em>ax</em><sup>2</sup>＋(2<em>a</em>－1)<em>x</em>]＝0得<em>x</em><sub>1</sub>＝0，<em>x</em><sub>2</sub>＝．
当0＜*a*≤时，*F*(*x*)在[0，＋∞)上单调递减，所以*F*(*x*)≤*F*（0）＝0恒成立；
当<em>a</em>＞时，因为<em>F</em>(<em>x</em>)在[0，<em>x</em><sub>2</sub>]上单调递增，所以<em>F</em>(<em>x</em><sub>2</sub>)≥<em>F</em>（0）＝0恒成立，此时<em>F</em>(<em>x</em>)≤0不恒成立．
综上所述，实数*a*的取值范围是．

2．已知函数<em>f</em>(<em>x</em>)＝e<sup>－</sup><em><sup>x</sup></em>＋<em>ax</em>(<em>a</em>∈<strong>R</strong>)．  
（1）讨论*f*(*x*)的最值；  
（2）若<em>a</em>＝0，求证：<em>f</em>(<em>x</em>)&gt;－<em>x</em><sup>2</sup>＋．

2．解析：（1）依题意，得<em>f</em>′(<em>x</em>)＝－e<sup>－</sup><em><sup>x</sup></em>＋<em>a</em>．

①当<em>a</em>≤0时，<em>f</em>′(<em>x</em>)&lt;0，所以<em>f</em>(<em>x</em>)在<strong>R</strong>上单调递减，故<em>f</em>(<em>x</em>)不存在最大值和最小值；
②当*a*>0时，由*f*′(*x*)＝0得*x*＝－ln *a*．
当*x*∈(－∞，－ln *a*)时，*f*′(*x*)<0，*f*(*x*)单调递减；当*x*∈(－ln *a*，＋∞)时，*f*′(*x*) >0，*f*(*x*)单调递增．
故当*x*＝－ln *a*时，*f*(*x*)取得极小值，也是最小值，最小值为*f*(－ln *a*)＝*a*－*a*ln *a*，不存在最大值．

综上，当*a*≤0时，*f*(*x*)不存在最大值和最小值；当*a*>0时，*f*(*x*)的最小值为*a*－*a*ln *a*，不存在最大值．  
（2）当<em>a</em>＝0时，<em>f</em>(<em>x</em>)＝e<sup>－</sup><em><sup>x</sup></em>，要证<em>f</em>(<em>x</em>)&gt;－<em>x</em><sup>2</sup>＋，即证e<sup>－</sup><em><sup>x</sup></em>&gt;－<em>x</em><sup>2</sup>＋，即证(5－4<em>x</em><sup>2</sup>)e<em><sup>x</sup></em>&lt;8．
设<em>h</em>(<em>x</em>)＝(5－4<em>x</em><sup>2</sup>)e<em><sup>x</sup></em>，
当5－4<em>x</em><sup>2</sup>≤0，即<em>x</em>≤－或<em>x</em>≥时，<em>h</em>(<em>x</em>)≤0&lt;8；
当5－4<em>x</em><sup>2</sup>&gt;0，即－&lt;<em>x</em>&lt;时，<em>h</em>′(<em>x</em>)＝(－4<em>x</em><sup>2</sup>－8<em>x</em>＋5)e<em><sup>x</sup></em>＝－(2<em>x</em>－1)(2<em>x</em>＋5)e<em><sup>x</sup></em>，
所以当－<*x*<时，*h*′(*x*)>0，*h*(*x*)在上单调递增，
当<*x*<时，*h*′(*x*)<0，*h*(*x*)在上单调递减，
所以当－<*x*<时，*h*(*x*)≤*h*＝4<8．
综上所述，不等式<em>f</em>(<em>x</em>)&gt;－<em>x</em><sup>2</sup>＋成立．

3．已知函数<em>f</em>(<em>x</em>)＝<em>a</em>(<em>x</em>－1)，<em>g</em>(<em>x</em>)＝(<em>ax</em>－1)·e<em><sup>x</sup></em>，<em>a</em>∈<strong>R</strong>．  
（1）求证：存在唯一实数*a*，使得直线*y*＝*f*(*x*)和曲线*y*＝*g*(*x*)相切；  
（2）若不等式*f*(*x*)＞*g*(*x*)有且只有两个整数解，求*a*的取值范围．

3．解析　（1）<em>f</em>′(<em>x</em>)＝<em>a</em>，<em>g</em>′(<em>x</em>)＝(<em>ax</em>＋<em>a</em>－1)e<em><sup>x</sup></em>．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
设直线<em>y</em>＝<em>f</em>(<em>x</em>)和曲线<em>y</em>＝<em>g</em>(<em>x</em>)的切点的坐标为(<em>x</em><sub>0</sub>，<em>y</em><sub>0</sub>)，则<em>y</em><sub>0</sub>＝<em>a</em>(<em>x</em><sub>0</sub>－1)＝(<em>ax</em><sub>0</sub>－1)，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
得<em>a</em>(<em>x</em><sub>0</sub>－<em>x</em><sub>0</sub>＋1)＝，①

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
又因为直线<em>y</em>＝<em>f</em>(<em>x</em>)和曲线<em>y</em>＝<em>g</em>(<em>x</em>)相切，所以<em>a</em>＝<em>g</em>′(<em>x</em><sub>0</sub>)＝(<em>ax</em><sub>0</sub>＋<em>a</em>－1)，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
整理得<em>a</em>(<em>x</em><sub>0</sub>＋－1)＝，②

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

结合①②得<em>x</em><sub>0</sub>－<em>x</em><sub>0</sub>＋1＝<em>x</em><sub>0</sub>＋－1，即＋<em>x</em><sub>0</sub>－2＝0，令<em>h</em>(<em>x</em>)＝e<em><sup>x</sup></em>＋<em>x</em>－2，
则<em>h</em>′(<em>x</em>)＝e<em><sup>x</sup></em>＋1＞0，所以<em>h</em>(<em>x</em>)在<strong>R</strong>上单调递增．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
又因为<em>h</em>（0）＝－1＜0，<em>h</em>（1）＝e－1＞0，所以存在唯一实数<em>x</em><sub>0</sub>，使得＋<em>x</em><sub>0</sub>－2＝0，且<em>x</em><sub>0</sub>∈(0，1)，
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

考点三　指对在一起，常常要分手

【方法总结】
设<em>f</em>(<em>x</em>)为可导函数，则有(e<em><sup>x</sup></em>ln<em>x</em>－<em>f</em>(<em>x</em>))′＝e<em><sup>x</sup></em>ln<em>x</em>＋－<em>f</em>′(<em>x</em>)，若<em>f</em>(<em>x</em>)为非常数函数，求导式子中还是含有e<em><sup>x</sup></em>，ln<em>x</em>，针对此类型，可以采用作商的方法，构造＝ln<em>x</em>－，从而达到简化证明和求极值、最值的目的，e<em><sup>x</sup></em>ln<em>x</em>腻在一起，常常会分手．

【例题选讲】

<strong>[例5]</strong> (2014·全国Ⅰ)设函数<em>f</em>(<em>x</em>)＝<em>a</em>e<em><sup>x</sup></em>ln <em>x</em>＋，曲线<em>y</em>＝<em>f</em>(<em>x</em>)在点(1，<em>f</em>（1）)处的切线为<em>y</em>＝e(<em>x</em>－1)＋2．  
（1）求*a*，*b*；  
（2）证明：*f*(*x*)＞1．

<strong>解析</strong>　（1）<em>f</em>′(<em>x</em>)＝<em>a</em>e<em><sup>x</sup></em>＋(<em>x</em>＞0)，由于直线<em>y</em>＝e(<em>x</em>－1)＋2的斜率为e，图象过点(1，2)，所以即解得  
（2）由（1）知<em>f</em>(<em>x</em>)＝e<em><sup>x</sup></em>ln <em>x</em>＋(<em>x</em>＞0)，从而<em>f</em>(<em>x</em>)＞1等价于<em>x</em>ln <em>x</em>＞<em>x</em>e<sup>－</sup><em><sup>x</sup></em>－．

构造函数*g*(*x*)＝*x*ln *x*，则*g*′(*x*)＝1＋ln *x*，
所以当*x*∈时，*g*′(*x*)＜0，当*x*∈时，*g*′(*x*)＞0，
故*g*(*x*)在上单调递减，在上单调递增，从而*g*(*x*)在(0，＋∞)上的最小值为*g*＝－．

构造函数<em>h</em>(<em>x</em>)＝<em>x</em>e<sup>－</sup><em><sup>x</sup></em>－，则<em>h</em>′(<em>x</em>)＝e<sup>－</sup><em><sup>x</sup></em>(1－<em>x</em>)．
所以当*x*∈(0，1)时，*h*′(*x*)＞0；当*x*∈(1，＋∞)时，*h*′(*x*)＜0；
故*h*(*x*)在(0，1)上单调递增，在(1，＋∞)上单调递减，从而*h*(*x*)在(0，＋∞)上的最大值为*h*（1）＝－．

综上，当*x*＞0时，*g*(*x*)＞*h*(*x*)，即*f*(*x*)＞1．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

<strong>[例6]</strong>已知函数<em>f</em>(<em>x</em>)＝＋<em>a</em> ln <em>x</em>，<em>g</em>(<em>x</em>)＝．  
（1）讨论函数*f*(*x*)的单调性；  
（2）证明：*a*＝1时，*f*(*x*)＋*g*(*x*)－ln *x*＞e．

<strong>解析</strong>　（1）<em>f</em>(<em>x</em>)＝＋<em>a</em> ln <em>x</em>，<em>x</em>∈(0，＋∞)．<em>f</em>′(<em>x</em>)＝－＋＝．
当*a*≤0时，*f*′(*x*)＜0，函数*f*(*x*)在*x*∈(0，＋∞)上单调递减．
当*a*＞0时，由*f*′(*x*)<0，得0<*x*<，由*f*′(*x*)>0，得*x*>，
所以函数*f*(*x*)在上单调递减，在上单调递增．  
（2）*a*＝1时，要证*f*(*x*)＋*g*(*x*)－ln *x*＞e．
即要证＋－ln <em>x</em>－e＞0⇔e<em><sup>x</sup></em>－e<em>x</em>＋1&gt;，<em>x</em>∈(0，＋∞)．
令<em>F</em>(<em>x</em>)＝e<em><sup>x</sup></em>－e<em>x</em>＋1，<em>F</em>′(<em>x</em>)＝e<em><sup>x</sup></em>－e，
当*x*∈(0，1)时，*F*′(*x*)＜0，此时函数*F*(*x*)单调递减；
当*x*∈(1，＋∞)时，*F*′(*x*)＞0，此时函数*F*(*x*)单调递增．
可得当*x*＝1时，函数*F*(*x*)取得最小值*F*（1）＝1．
令*G*(*x*)＝，*G*′(*x*)＝，
当0<*x*<e时，*G*′(*x*)>0，此时*G*(*x*)为增函数，当*x*>e时，*G*′(*x*)<0，此时*G*(*x*)为减函数，
所以*x*＝e时，函数*G*(*x*)取得最大值*G*(e)＝1．

<em>x</em>＝1与<em>x</em>＝e不同时取得，因此<em>F</em>(<em>x</em>)＞<em>G</em>(<em>x</em>)，即e<em><sup>x</sup></em>－e<em>x</em>＋1&gt;，<em>x</em>∈(0，＋∞)．故原不等式成立．

【对点精练】

1．设函数*f*(*x*)＝，求证：当*x*＞1时，不等式＞．

1．解析　将不等式＞变形为·＞，
分别构造函数*g*(*x*)＝和函数*h*(*x*)＝．

对于*g*′(*x*)＝，令*φ*(*x*)＝*x*－ln *x*，则*φ*′(*x*)＝1－＝．
因为*x*＞1，所以*φ*′(*x*)＞0，所以*φ*(*x*)在(1，＋∞)上是增函数，所以*φ*(*x*)＞*φ*（1）＝1＞0，
所以*g*′(*x*)＞0，所以*g*(*x*)在(1，＋∞)上是增函数，所以当*x*＞1时，*g*(*x*)＞*g*（1）＝2，故＞．

对于<em>h</em>′(<em>x</em>)＝，因为<em>x</em>＞1，所以1－e<em><sup>x</sup></em>＜0，所以<em>h</em>′(<em>x</em>)＜0，
所以*h*(*x*)在(1，＋∞)上是减函数，所以当*x*＞1时，*h*(*x*)＜*h*（1）＝．
综上所述，当*x*＞1时，＞*h*(*x*)，即＞．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

(第1题) 　　　　　　　　　　　　　　　(第2题)

2．已知<em>f</em>(<em>x</em>)＝e<em><sup>x</sup></em>－<em>a</em>ln<em>x</em>－<em>a</em>，其中常数<em>a&gt;</em>0．  
（1）当*a>* e时，求函数*f*(*x*)的极值；  
（2）求证：e<sup>2</sup><em><sup>x</sup></em><sup>－2</sup>－e<em><sup>x</sup></em><sup>－1</sup>ln<em>x</em>－<em>x</em>≥0．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

2．解析　（1）当时，，，．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

，在单调递增．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

时，，，．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
在单调递减，在单调递增．的极小值为，无极大值．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)  
（2）由（1）得，所证不等式：．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
设，，令可解得：．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
在单调递增，在单调递减．．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

，即，．

3．已知函数*f*(*x*)＝＋*a*ln*x*，*g*(*x*)＝．  
（1）讨论函数*f*(*x*)的单调性；  
（2）证明：*a*＝1时，*f*(*x*)＋*g*(*x*)－ln*x*＞e．

3．<strong>解析</strong>　（1）<em>f</em>(<em>x</em>)＝＋<em>a</em> ln <em>x</em>，<em>x</em>∈(0，＋∞)．<em>f</em>′(<em>x</em>)＝－＋＝．
当*a*≤0时，*f*′(*x*)＜0，函数*f*(*x*)在*x*∈(0，＋∞)上单调递减．
当*a*＞0时，由*f*′(*x*)<0，得0<*x*<，由*f*′(*x*)>0，得*x*>，
所以函数*f*(*x*)在上单调递减，在上单调递增．  
（2）*a*＝1时，要证*f*(*x*)＋*g*(*x*)－ln *x*＞e．
即要证＋－ln <em>x</em>－e＞0⇔e<em><sup>x</sup></em>－e<em>x</em>＋1&gt;，<em>x</em>∈(0，＋∞)．
令<em>F</em>(<em>x</em>)＝e<em><sup>x</sup></em>－e<em>x</em>＋1，<em>F</em>′(<em>x</em>)＝e<em><sup>x</sup></em>－e，
当*x*∈(0，1)时，*F*′(*x*)＜0，此时函数*F*(*x*)单调递减；
当*x*∈(1，＋∞)时，*F*′(*x*)＞0，此时函数*F*(*x*)单调递增．
可得当*x*＝1时，函数*F*(*x*)取得最小值*F*（1）＝1．
令*G*(*x*)＝，*G*′(*x*)＝，
当0<*x*<e时，*G*′(*x*)>0，此时*G*(*x*)为增函数，当*x*>e时，*G*′(*x*)<0，此时*G*(*x*)为减函数，
所以*x*＝e时，函数*G*(*x*)取得最大值*G*(e)＝1．

<em>x</em>＝1与<em>x</em>＝e不同时取得，因此<em>F</em>(<em>x</em>)＞<em>G</em>(<em>x</em>)，即e<em><sup>x</sup></em>－e<em>x</em>＋1&gt;，<em>x</em>∈(0，＋∞)．故原不等式成立．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

