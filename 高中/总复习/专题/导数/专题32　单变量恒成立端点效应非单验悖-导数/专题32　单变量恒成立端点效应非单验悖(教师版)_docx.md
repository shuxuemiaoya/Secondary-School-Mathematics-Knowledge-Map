**专题32　单变量恒成立之端点效应非单验悖**

![](images/89b0fd2f70d50691b027154ae8e093a316edf5457576dfd9e5955732e59032cd.jpg)

**考点一　单变量恒成立端点效应非单验悖之含端点**

**【例题选讲】**

<strong>[例1]</strong>　已知函数<em>f</em>(<em>x</em>)＝e<sup>－</sup><em><sup>x</sup></em>－<em>ax</em>(<em>x</em>∈<strong>R</strong>)．

(1)当*a*＝－1时，求函数*f*(*x*)的最小值；

(2)若*x*≥0时，*f*(－*x*)＋ln(*x*＋1)≥1恒成立，求实数*a*的取值范围．

<strong>思路</strong>　(1)先判断<em>f</em>(<em>x</em>)的单调性，再求最小值，(2)端点值等于临界值，令<em>F</em>(<em>x</em>)＝<em>f</em>(<em>x</em>－1)－<em>ax</em>＋<em>x</em><sup>2</sup>＝(<em>x</em>－1)ln(<em>x</em>－1)＋<em>x</em><sup>2</sup>－<em>ax</em>(<em>x</em>≥2)，<em>F</em>(2)＝0，所以用“端点效应＋非单验悖”解决．

<strong>解析</strong>　(1)当<em>a</em>＝－1时，<em>f</em>(<em>x</em>)＝e<sup>－</sup><em><sup>x</sup></em>＋<em>x</em>，则<em>f</em>′(<em>x</em>)＝－＋1＝．令<em>f</em>′(<em>x</em>)＝0，得<em>x</em>＝0

当*x*＜0时，*f*′(*x*)＜0；当*x*＞0时，*f*′(*x*)＞0．

所以函数*f*(*x*)在(－∞，0)上单调递减，在(0，＋∞)上单调递增．

所以当*x*＝0时，函数*f*(*x*)取得最小值，且最小值为*f*(0)＝1.

(2)因为<em>x</em>≥0时，<em>f</em>(－<em>x</em>)＋ln(<em>x</em>＋1)≥1恒成立，即e<em><sup>x</sup></em>＋<em>ax</em>＋ln(<em>x</em>＋1)－1≥0.(\*)

令<em>g</em>(<em>x</em>)＝e<em><sup>x</sup></em>＋<em>ax</em>＋ln(<em>x</em>＋1)－1，则

又<em>g</em>″(<em>x</em>)＝e<em><sup>x</sup></em>－≥0，当且仅当<em>x</em>＝0时取等号，所以<em>g</em>′(<em>x</em>)＝e<em><sup>x</sup></em>＋＋<em>a</em>在[0，＋∞)上单调递增．

①若*a*≥－2，则当且仅当*x*＝0，*a*＝－2时取等号，

所以*g*(*x*)在[0，＋∞)上单调递增，有*g*(*x*)≥*g*(0)＝0，(\*)式恒成立．

②若*a*＜－2，由于*g*′(0)＝2＋*a*＜0，*x*→＋∞时，*g*′(*x*)→＋∞，

所以必存在唯一的<em>x</em><sub>0</sub>∈(0，＋∞)，使得<em>g</em>′(<em>x</em><sub>0</sub>)＝0，

当0＜<em>x</em>＜<em>x</em><sub>0</sub>时，<em>g</em>′(<em>x</em>)＜0，<em>g</em>(<em>x</em>)单调递减；当<em>x</em>＞<em>x</em><sub>0</sub>时，<em>g</em>′(<em>x</em>)＞0，<em>g</em>(<em>x</em>)单调递增．

所以当<em>x</em>∈(0，<em>x</em><sub>0</sub>)时，<em>g</em>(<em>x</em>)＜<em>g</em>(0)＝0，(\*)式不恒成立．

综上所述，实数*a*的取值范围是[－2，＋∞)．

**悟通**　考虑端点值，直入问题本质，抓住端点值展开讨论．分析端点值，明确函数图象走势．

<strong>[例2]</strong>　已知函数<em>f</em>(<em>x</em>)＝e<em><sup>x</sup></em>－<em>x</em><sup>2</sup>－<em>ax</em>－1，<em>g</em>(<em>x</em>)＝cos<em>x</em>＋<em>x</em><sup>2</sup>－1．

(1)当*a*＝1时，求证：当*x*≥0时，*f*(*x*)≥0；

(2)若*f*(*x*)＋*g*(*x*)≥0在[0，＋∞)上恒成立，求*a*的取值范围．

<strong>解析</strong>　(1)当<em>a</em>＝1时，<em>f</em>(<em>x</em>)＝e<em><sup>x</sup></em>－<em>x</em><sup>2</sup>－<em>x</em>－1，

∴<em>f</em>′(<em>x</em>)＝e<em><sup>x</sup></em>－<em>x</em>－1，令<em>u</em>(<em>x</em>)＝e<em><sup>x</sup></em>－<em>x</em>－1，则<em>u</em>′(<em>x</em>)＝e<em><sup>x</sup></em>－1≥0在[0，＋∞)上恒成立，

故*f*′(*x*)在[0，＋∞)上单调递增，∴*f*′(*x*)≥*f*′(0)＝0，∴*f*(*x*)在[0，＋∞)上单调递增，

∴*f*(*x*)≥*f*(0)＝0，从而原不等式得证．

(2)∵<em>f</em>(<em>x</em>)＋<em>g</em>(<em>x</em>)＝e<em><sup>x</sup></em>＋cos <em>x</em>－<em>ax</em>－2，

令<em>h</em>(<em>x</em>)＝e<em><sup>x</sup></em>＋cos <em>x</em>－<em>ax</em>－2，则<em>h</em>′(<em>x</em>)＝e<em><sup>x</sup></em>－sin <em>x</em>－<em>a</em>，

令<em>t</em>(<em>x</em>)＝e<em><sup>x</sup></em>－sin <em>x</em>－<em>a</em>，则<em>t</em>′(<em>x</em>)＝e<em><sup>x</sup></em>－cos <em>x</em>，∵e<em><sup>x</sup></em>≥1，－1≤cos <em>x</em>≤1，故<em>t</em>′(<em>x</em>)≥0，

∴*h*′(*x*)在[0，＋∞)上单调递增，∴*h*′(*x*)≥*h*′(0)＝1－*a*，

①当1－*a*≥0，即*a*≤1时，*h*′(*x*)≥0，故*h*(*x*)在[0，＋∞)上单调递增，故*h*(*x*)≥*h*(0)＝0，满足题意；

②当1－*a*<0，即*a*>1时，∵*h*′(0)<0，又*x*→＋∞时，*h*′(*x*)→＋∞，

∴∃<em>x</em><sub>0</sub>∈(0，＋∞)，使得<em>h</em>′(<em>x</em><sub>0</sub>)＝0，∴当<em>x</em>∈(0，<em>x</em><sub>0</sub>)时，<em>h</em>′(<em>x</em>)&lt;0，

∴<em>h</em>(<em>x</em>)在(0，<em>x</em><sub>0</sub>)上单调递减，此时<em>h</em>(<em>x</em>)&lt;<em>h</em>(0)＝0，不符合题意．

综上所述，实数*a*的取值范围是(－∞，1]．

<strong>[例3]</strong>　已知函数<em>f</em>(<em>x</em>)＝<em>ax</em>ln(<em>x</em>＋1)＋<em>x</em>＋1(<em>x</em>&gt;－1，<em>a</em>∈<strong>R</strong>)．

(1)若*a*＝，求函数*f*(*x*)的单调区间；

(2)当<em>x</em>≥0时，<em>f</em>(<em>x</em>)≤e<em><sup>x</sup></em>恒成立，求实数<em>a</em>的取值范围．

解析：(1)*a*＝时，*f*(*x*)＝*x*ln(*x*＋1)＋*x*＋1，

*f*′(*x*)＝＋1＝＋1．

易得*f*′(*x*)在(－1，＋∞)上是增函数，且*f*′＝0，

∴当*x*∈时，*f*′(*x*)<0，*f*(*x*)是减函数；当*x*∈时，*f*′(*x*)>0，*f*(*x*)是增函数．

∴函数*f*(*x*)的单调递减区间是，单调递增区间是．

(2)记<em>g</em>(<em>x</em>)＝<em>f</em>(<em>x</em>)－e<em><sup>x</sup></em>(<em>x</em>≥0)，则<em>g</em>(0)＝0，<em>g</em>′(<em>x</em>)＝<em>a</em>＋1－e<em><sup>x</sup></em>．

记<em>h</em>(<em>x</em>)＝<em>a</em>＋1－e<em><sup>x</sup></em>(<em>x</em>≥0)，<em>h</em>′(<em>x</em>)＝<em>a</em>－e<em><sup>x</sup></em>，<em>h</em>′(0)＝2<em>a</em>－1．

①当<em>a</em>≤时，∵＋∈(0，2]，e<em><sup>x</sup></em>≥1，∴<em>h</em>′(<em>x</em>)≤0，<em>h</em>(<em>x</em>)在[0，＋∞)上是减函数，

则*h*(*x*)≤*h*(0)＝0，即*g*′(*x*)≤0，∴*g*(*x*)在[0，＋∞)上是减函数，∴*g*(*x*)≤*g*(0)＝0恒成立，

即<em>f</em>(<em>x</em>)≤e<em><sup>x</sup></em>恒成立，满足题设；

②当<em>a</em>&gt;时，<em>h</em>′(<em>x</em>)＝<em>a</em>－e<em><sup>x</sup></em>在[0，＋∞)上是减函数，

又<em>h</em>′(0)＝2<em>a</em>－1&gt;0，当<em>x</em>→＋∞时，<em>h</em>′(<em>x</em>)→－∞，则必存在<em>x</em><sub>0</sub>∈(0，＋∞)，使<em>h</em>′(<em>x</em><sub>0</sub>)＝0，

则当<em>x</em>∈(0，<em>x</em><sub>0</sub>)时，<em>h</em>′(<em>x</em>)&gt;0，<em>h</em>(<em>x</em>)在(0，<em>x</em><sub>0</sub>)上是增函数，此时<em>h</em>(<em>x</em>)&gt;<em>h</em>(0)＝0，

即当<em>x</em>∈(0，<em>x</em><sub>0</sub>)时，<em>g</em>′(<em>x</em>)&gt;0，∴<em>g</em>(<em>x</em>)在(0，<em>x</em><sub>0</sub>)上是增函数，∴<em>g</em>(<em>x</em>)&gt;<em>g</em>(0)＝0，即<em>f</em>(<em>x</em>)&gt;e<em><sup>x</sup></em>，不符合题意．

综合①②，得*a*≤，即实数*a*的取值范围为．

**【对点训练】**

1．(2017·全国Ⅱ)设函数<em>f</em>(<em>x</em>)＝(1－<em>x</em><sup>2</sup>)e<em><sup>x</sup></em>．

(1)讨论*f*(*x*)的单调性；

(2)当*x*≥0时，*f*(*x*)≤*ax*＋1，求实数*a*的取值范围．

1．解析　(1)<em>f</em>′(<em>x</em>)＝(1－2<em>x</em>－<em>x</em><sup>2</sup>)e<em><sup>x</sup></em>，令<em>f</em>′(<em>x</em>)＝0，得<em>x</em>＝－1±，

当*x*∈(－∞，－1－)时，*f*′(*x*)＜0；当*x*∈(－1－，－1＋)时，*f*′(*x*)＞0；

当*x*∈(－1＋，＋∞)时，*f*′(*x*)＜0．

所以*f*(*x*)在(－∞，－1－)，(－1＋，＋∞)上单调递减，在(－1－，－1＋)上单调递增．

(2)令<em>g</em>(<em>x</em>)＝<em>f</em>(<em>x</em>)－<em>ax</em>－1＝(1－<em>x</em><sup>2</sup>)e<em><sup>x</sup></em>－(<em>ax</em>＋1)，令<em>x</em>＝0，可得<em>g</em>(0)＝0．

<em>g</em>′(<em>x</em>)＝(1－<em>x</em><sup>2</sup>－2<em>x</em>)e<em><sup>x</sup></em>－<em>a</em>，<em>g</em>′(0)＝1－<em>a</em>，

又<em>g</em>′′(<em>x</em>)＝－(<em>x</em><sup>2</sup>＋4<em>x</em>＋1)e<em><sup>x</sup></em>，<em>g</em>′′(<em>x</em>)＜0，<em>g</em>′(<em>x</em>)在[0，＋∞)上单调递减，

①当1－*a*≤0时，即*a*≥1，则*g*(*x*)在[0，＋∞)上单调递减，所以*g*(*x*) ≤*g*(0)＝0．

②当1－*a*>0时，即*a*<1，*x*→＋∞时，*g*′(*x*)→－∞，

所以必存在唯一的<em>x</em><sub>0</sub>∈(0，＋∞)，使得<em>g</em>′(<em>x</em><sub>0</sub>)＝0，

当0＜<em>x</em>＜<em>x</em><sub>0</sub>时，<em>g</em>′(<em>x</em>)&gt;0，<em>g</em>(<em>x</em>)单调递增；当<em>x</em>＞<em>x</em><sub>0</sub>时，<em>g</em>′(<em>x</em>)&lt;0，<em>g</em>(<em>x</em>)单调递减．

所以当<em>x</em>∈(0，<em>x</em><sub>0</sub>)时，<em>g</em>(<em>x</em>)&gt;<em>g</em>(0)＝0，(\*)式不恒成立．

综上所述，实数*a*的取值范围是[1，＋∞)．

2．已知点<em>P</em>，<em>Q</em>(<em>x</em>，<em>mx</em>＋sin <em>x</em>)(<em>m</em>∈<strong>R</strong>)，<em>O</em>为坐标原点，设函数<em>f</em>(<em>x</em>)＝·．

(1)当*m*＝－2时，判断函数*f*(*x*)在(－∞，0)上的单调性；

(2)当*x*≥0时，不等式*f*(*x*)≥1恒成立，求实数*m*的取值范围．

2．解析　(1)<em>f</em>(<em>x</em>)＝·＝·(<em>x</em>，<em>mx</em>＋sin <em>x</em>)＝e<em><sup>x</sup></em>＋<em>mx</em>＋sin <em>x</em>，

当<em>m</em>＝－2时，<em>f</em>(<em>x</em>)＝e<em><sup>x</sup></em>－2<em>x</em>＋sin <em>x</em>，<em>f</em>′(<em>x</em>)＝e<em><sup>x</sup></em>－2＋cos <em>x</em>，

当<em>x</em>&lt;0时，e<em><sup>x</sup></em>&lt;1，且cos <em>x</em>≤1．所以<em>f</em>′(<em>x</em>)＝e<em><sup>x</sup></em>－2＋cos <em>x</em>&lt;0，

所以函数*f*(*x*)在(－∞，0)上单调递减．

(2)当<em>x</em>＝0时，<em>f</em>(0)＝1≥1，对于<em>m</em>∈<strong>R</strong>，<em>f</em>(<em>x</em>)≥1恒成立．

当<em>x</em>&gt;0时，<em>f</em>′(<em>x</em>)＝e<em><sup>x</sup></em>＋<em>m</em>＋cos <em>x</em>，设<em>g</em>(<em>x</em>)＝e<em><sup>x</sup></em>＋<em>m</em>＋cos <em>x</em>，

则<em>g</em>′(<em>x</em>)＝e<em><sup>x</sup></em>－sin <em>x</em>，因为e<em><sup>x</sup></em>&gt;1，sin <em>x</em>≤1，

所以<em>g</em>′(<em>x</em>)＝e<em><sup>x</sup></em>－sin <em>x</em>&gt;0，则<em>g</em>(<em>x</em>)在(0，＋∞)上单调递增，所以<em>g</em>(<em>x</em>)&gt;<em>g</em>(0)＝<em>m</em>＋2，

所以*f*′(*x*)在(0，＋∞)上单调递增，且*f*′(*x*)>*m*＋2．

①当*m*≥－2时，*f*′(*x*)>0，则*f*(*x*)在(0，＋∞)上单调递增，所以*f*(*x*)>1恒成立．

②当*m*<－2时，*f*′(0)＝*m*＋2<0，因为*f*′(*x*)在(0，＋∞)上单调递增，且当*x*＝ln(2－*m*)时，

<em>f</em>′(<em>x</em>)＝e<sup>ln(2－</sup><em><sup>m</sup></em><sup>)</sup>＋<em>m</em>＋cos[ln(2－<em>m</em>)]＝2＋cos[ln(2－<em>m</em>)]&gt;0，

所以存在<em>x</em><sub>0</sub>∈(0，＋∞)，使得<em>f</em>′(<em>x</em><sub>0</sub>)＝0，所以当<em>x</em>∈(0，<em>x</em><sub>0</sub>)时，<em>f</em>′(<em>x</em>)&lt;0恒成立，

故<em>f</em>(<em>x</em>)在区间(0，<em>x</em><sub>0</sub>)上单调递减．所以当<em>x</em>∈(0，<em>x</em><sub>0</sub>)时，<em>f</em>(<em>x</em>)&lt;1，不符合题意．

综上，实数*m*的取值范围为[－2，＋∞)．

3．设函数<em>f</em> (<em>x</em>)＝(1＋<em>x</em>－<em>x</em><sup>2</sup>)e<em><sup>x</sup></em>(e＝2.718 28…是自然对数的底数)．

(1)讨论*f* (*x*)的单调性；

(2)当<em>x</em>≥0时，<em>f</em> (<em>x</em>)≤<em>ax</em>＋1＋2<em>x</em><sup>2</sup>恒成立，求实数<em>a</em>的取值范围．

3．解析：(1)<em>f</em> ′(<em>x</em>)＝(2－<em>x</em>－<em>x</em><sup>2</sup>)e<em><sup>x</sup></em>＝－(<em>x</em>＋2)(<em>x</em>－1)e<em><sup>x</sup></em>．

当*x*<－2或*x*>1时，*f* ′(*x*)<0；当－2<*x*<1时，*f* ′(*x*)>0．

所以*f* (*x*)在(－∞，－2)，(1，＋∞)上单调递减，在(－2，1)上单调递增．

(2)设<em>F</em>(<em>x</em>)＝<em>f</em> (<em>x</em>)－(<em>ax</em>＋1＋2<em>x</em><sup>2</sup>)，<em>F</em>(0)＝0，<em>F</em>′(<em>x</em>)＝(2－<em>x</em>－<em>x</em><sup>2</sup>)e<em><sup>x</sup></em>－4<em>x</em>－<em>a</em>，<em>F</em>′(0)＝2－<em>a</em>，

当<em>a</em>≥2时，<em>F</em>′(<em>x</em>)＝(2－<em>x</em>－<em>x</em><sup>2</sup>)e<em><sup>x</sup></em>－4<em>x</em>－<em>a</em>≤－(<em>x</em>＋2)·(<em>x</em>－1)e<em><sup>x</sup></em>－4<em>x</em>－2

≤－(<em>x</em>＋2)(<em>x</em>－1)e<em><sup>x</sup></em>－<em>x</em>－2＝－(<em>x</em>＋2)[(<em>x</em>－1)e<em><sup>x</sup></em>＋1]，

设<em>h</em>(<em>x</em>)＝(<em>x</em>－1)e<em><sup>x</sup></em>＋1，<em>h</em>′(<em>x</em>)＝<em>x</em>e<em><sup>x</sup></em>≥0，所以<em>h</em>(<em>x</em>)在[0，＋∞)上单调递增，<em>h</em>(<em>x</em>)＝(<em>x</em>－1)e<em><sup>x</sup></em>＋1≥<em>h</em>(0)＝0，

即*F*′(*x*)≤0在[0，＋∞)上恒成立，*F*(*x*)在[0，＋∞)上单调递减，*F*(*x*)≤*F*(0)＝0，

所以<em>f</em> (<em>x</em>)≤<em>ax</em>＋1＋2<em>x</em><sup>2</sup>在[0，＋∞)上恒成立．

当*a*<2时，*F*′(0)＝2－*a*>0，而函数*F*′(*x*)的图象在(0，＋∞)上连续且*x*→＋∞，*F*′(*x*)逐渐趋近负无穷，

必存在正实数<em>x</em><sub>0</sub>使得<em>F</em>′(<em>x</em><sub>0</sub>)＝0且在(0，<em>x</em><sub>0</sub>)上<em>F</em>′(<em>x</em>)&gt;0，

所以<em>F</em>(<em>x</em>)在(0，<em>x</em><sub>0</sub>)上单调递增，此时<em>F</em>(<em>x</em>)&gt;<em>F</em>(0)＝0，<em>f</em> (<em>x</em>)&gt;<em>ax</em>＋1＋2<em>x</em><sup>2</sup>有解，不满足题意．

综上，*a*的取值范围是[2，＋∞)．

4．已知函数*f*(*x*)＝*x*ln*x*．

(1)求*f*(*x*)在上的值域；

(2)对任意<em>x</em>∈[2，＋∞)，都有<em>f</em>(<em>x</em>－1)≤<em>ax</em>－<em>x</em><sup>2</sup>成立，求实数<em>a</em>的取值范围．

4．<strong>解析</strong>　(1)∵<em>f</em>(<em>x</em>)＝<em>x</em>ln <em>x</em>(<em>x</em>&gt;0)，∴<em>f</em>′(<em>x</em>)＝1＋ln <em>x</em>，令<em>f</em>′(<em>x</em>)＝0，得<em>x</em>＝，

∴当*x*∈时，*f*′(*x*)<0，*f*(*x*)单调递减；当*x*∈时，*f*′(*x*)>0，*f*(*x*)单调递增，

∴当<em>x</em>∈时，<em>f</em>(<em>x</em>)<sub>min</sub>＝<em>f</em>＝－．又<em>f</em>＝－ln 3&lt;－ln 2＝<em>f</em>，

∴*f*(*x*)在上的值域为．

(2)设<em>F</em>(<em>x</em>)＝<em>f</em>(<em>x</em>－1)－<em>ax</em>＋<em>x</em><sup>2</sup>＝(<em>x</em>－1)ln(<em>x</em>－1)＋<em>x</em><sup>2</sup>－<em>ax</em>(<em>x</em>≥2)，

则*F*′(*x*)＝ln(*x*－1)＋1＋*a*(*x*－1)(*x*≥2)，*F*″(*x*)＝＋*a*(*x*≥2)，

①当<em>a</em>≥0时，在<em>x</em>∈[2，＋∞)上，<em>F</em>′(<em>x</em>)&gt;0，∴<em>F</em>(<em>x</em>)在[2，＋∞)上单调递增，<em>F</em>(<em>x</em>)<sub>min</sub>＝<em>F</em>(2)＝0，

不可能有<em>f</em>(<em>x</em>－1)≤<em>ax</em>－<em>x</em><sup>2</sup>在[2，＋∞)上恒成立．

②当*a*≤－1时，令*F*″(*x*)＝＋*a*＝0，解得*x*＝1－，此时2≥1－，∴*F*″(*x*)≤0，

∴*F*′(*x*)在[2，＋∞)上单调递减，∴*F*′(*x*)的最大值为*F*′(2)＝*a*＋1≤0，

∴*F*′(*x*)≤0，*F*(*x*)在[2，＋∞)上单调递减，∴*F*(*x*)在[2，＋∞)上的最大值为*F*(2)＝0，

即<em>f</em>(<em>x</em>－1)≤<em>ax</em>－<em>x</em><sup>2</sup>在[2，＋∞)上恒成立．

③当－1<*a*<0时，2<1－，

当*x*∈时，*F*″(*x*)>0，*F*′(*x*)单调递增；当*x*∈时，*F*″(*x*)<0，*F*′(*x*)单调递减，

∴<em>F</em>′(<em>x</em>)<sub>max</sub>＝<em>F</em>′＝－ln(－<em>a</em>)&gt;0，又<em>F</em>′(2)＝<em>a</em>＋1&gt;0，∴当<em>x</em>∈时，<em>F</em>′(<em>x</em>)&gt;0，<em>F</em>(<em>x</em>)单调递增，

又*F*(2)＝0，∴当*x*∈时，*F*(*x*)≥0，不符合题意．

综上所述，*a*≤－1，即实数*a*的取值范围为(－∞，－1]．

**考点二　单变量恒成立端点效应非单验悖之不含端点**

**【例题选讲】**

<strong>[例4]</strong>　设函数<em>f</em>(<em>x</em>)＝<em>x</em>(e<em><sup>x</sup></em>－1)－<em>ax</em><sup>2</sup>．

(1)若*a*＝，求*f*(*x*)的单调区间；

(2)若当*x*＞0时，*f*(*x*)＞0恒成立，求实数*a*的取值范围．

解析　(1)若<em>a</em>＝，则<em>f</em>(<em>x</em>)＝<em>x</em>(e<em><sup>x</sup></em>－1)－<em>x</em><sup>2</sup>，

<em>f</em>′(<em>x</em>)＝e<em><sup>x</sup></em>－1＋<em>x</em>e<em><sup>x</sup></em>－<em>x</em>＝(e<em><sup>x</sup></em>－1)(<em>x</em>＋1)，

当*x*∈(－∞，－1)时，*f*′(*x*)＞0；

当*x*∈(－1，0)时，*f*′(*x*)＜0；

当*x*∈(0，＋∞)时，*f*′(*x*)＞0．

故*f*(*x*)的单调递增区间是(－∞，－1)，(0，＋∞)，单调递减区间是(－1，0)．

(2)<em>f</em>(<em>x</em>)＝<em>x</em>(e<em><sup>x</sup></em>－1)－<em>ax</em><sup>2</sup>＝<em>x</em>(e<em><sup>x</sup></em>－1－<em>ax</em>)．

令<em>g</em>(<em>x</em>)＝e<em><sup>x</sup></em>－1－<em>ax</em>，则<em>g</em>′(<em>x</em>)＝e<em><sup>x</sup></em>－<em>a</em>，

若*a*≤1，则当*x*∈(0，＋∞)时，*g*′(*x*)＞0，*g*(*x*)为增函数，而*g*(0)＝0，

从而当*x*＞0时，*g*(*x*)＞0，则*f*(*x*)＞0．

若*a*＞1，则当*x*∈(0，ln *a*)时，*g*′(*x*)＜0，*g*(*x*)为减函数，而*g*(0)＝0．

从而当*x*∈(0，ln *a*)时，*g*(*x*)＜0，即*f*(*x*)＜0不符合题意．

综上可得*a*的取值范围是(－∞，1]．

<strong>[例5]</strong>　(2016·全国Ⅱ)已知函数<em>f</em>(<em>x</em>)＝(<em>x</em>＋1)ln<em>x</em>－<em>a</em>(<em>x</em>－1)．

(1)当*a*＝4时，求曲线*y*＝*f*(*x*)在(1，*f*(1))处的切线方程；

(2)若当*x*∈(1，＋∞)时，*f*(*x*)＞0，求*a*的取值范围．

解析：(1)*f*(*x*)的定义域为(0，＋∞)．当*a*＝4时，*f*(*x*)＝(*x*＋1)ln *x*－4(*x*－1)，

*f*(1)＝0，*f*′(*x*)＝ln *x*＋－3，*f*′(1)＝－2．故曲线*y*＝*f*(*x*)在(1，*f*(1))处的切线方程为2*x*＋*y*－2＝0.

(2)当*x*∈(1，＋∞)时，*f*(*x*)＞0等价于ln *x*－＞0.

设*g*(*x*)＝ln *x*－，

则*g*′(*x*)＝－＝，*g*(1)＝0.

①当<em>a</em>≤2，<em>x</em>∈(1，＋∞)时，<em>x</em><sup>2</sup>＋2(1－<em>a</em>)<em>x</em>＋1≥<em>x</em><sup>2</sup>－2<em>x</em>＋1＞0，

故*g*′(*x*)＞0，*g*(*x*)在(1，＋∞)上单调递增，因此*g*(*x*)＞0；

②当<em>a</em>＞2时，令<em>g</em>′(<em>x</em>)＝0得<em>x</em><sub>1</sub>＝<em>a</em>－1－，<em>x</em><sub>2</sub>＝<em>a</em>－1＋.

由<em>x</em><sub>2</sub>＞1和<em>x</em><sub>1</sub><em>x</em><sub>2</sub>＝1得0&lt;<em>x</em><sub>1</sub>＜1，故当<em>x</em>∈(1，<em>x</em><sub>2</sub>)时，<em>g</em>′(<em>x</em>)＜0，<em>g</em>(<em>x</em>)在(1，<em>x</em><sub>2</sub>)上单调递减，

因此*g*(*x*)＜*g*(1)＝0.

综上，*a*的取值范围是(－∞，2]．

<strong>[例6]</strong>　已知函数<em>f</em>(<em>x</em>)＝(<em>x</em>≠0)．

(1)判断函数*f*(*x*)在区间上的单调性；

(2)若*f*(*x*)<*a*在区间上恒成立，求实数*a*的最小值．

解析　(1)*f*′(*x*)＝，令*g*(*x*)＝*x*cos *x*－sin *x*，*x*∈，则*g*′(*x*)＝－*x*sin *x*，

显然，当*x*∈时，*g*′(*x*)＝－*x*sin *x*<0，即函数*g*(*x*)在区间上单调递减，且*g*(0)＝0．

从而*g*(*x*)在区间上恒小于零，所以*f*′(*x*)在区间上恒小于零，

所以函数*f*(*x*)在区间上单调递减．

(2)不等式*f*(*x*)<*a*，*x*∈恒成立，即sin *x*－*ax*<0恒成立．

令*φ*(*x*)＝sin *x*－*ax*，*x*∈，则*φ*′(*x*)＝cos *x*－*a*，且*φ*(0)＝0．

当*a*≥1时，在区间上*φ*′(*x*)<0，即函数*φ*(*x*)单调递减，所以*φ*(*x*)<*φ*(0)＝0，故sin *x*－*ax*<0恒成立．

当0&lt;<em>a</em>&lt;1时，<em>φ</em>′(<em>x</em>)＝cos <em>x</em>－<em>a</em>＝0在区间上存在唯一解<em>x</em><sub>0</sub>，

当<em>x</em>∈(0，<em>x</em><sub>0</sub>)时，<em>φ</em>′(<em>x</em>)&gt;0，故<em>φ</em>(<em>x</em>)在区间(0，<em>x</em><sub>0</sub>)上单调递增，且<em>φ</em>(0)＝0，

从而<em>φ</em>(<em>x</em>)在区间(0，<em>x</em><sub>0</sub>)上大于零，这与sin <em>x</em>－<em>ax</em>&lt;0恒成立相矛盾．

当*a*≤0时，在区间上*φ*′(*x*)>0，即函数*φ*(*x*)单调递增，且*φ*(0)＝0，

得sin *x*－*ax*>0恒成立，这与sin *x*－*ax*<0恒成立相矛盾．

故实数*a*的最小值为1．

**【对点训练】**

5．已知<em>f</em>(<em>x</em>)＝e<em><sup>x</sup></em>－<em>a</em>ln<em>x</em>(<em>a</em>∈<strong>R</strong>)．

(1)求函数*f*(*x*)在点(1，*f*(1))处的切线方程；

(2)当*a*＝－1时，若不等式*f*(*x*)＞e＋*m*(*x*－1)对任意*x*∈(1，＋∞)恒成立，求实数*m*的取值范围．

5．解析　(1)由<em>f</em>(<em>x</em>)＝e<em><sup>x</sup></em>－<em>a</em>ln<em>x</em>，得<em>f</em>′(<em>x</em>)＝e<em><sup>x</sup></em>－，<em>f</em>′(1)＝e－<em>a</em>，切点为(1，e)，

所求切线方程为*y*－e＝(e－*a*)(*x*－1)，即(e－*a*)*x*－*y*＋*a*＝0．

(2)由<em>a</em>＝－1得<em>f</em>(<em>x</em>)＝e<em><sup>x</sup></em>－ln<em>x</em>，原不等式即为e<em><sup>x</sup></em>＋ln<em>x</em>－e－<em>m</em>(<em>x</em>－1)＞0，

记<em>F</em>(<em>x</em>)＝e<em><sup>x</sup></em>＋ln<em>x</em>－e－<em>m</em>(<em>x</em>－1)，<em>F</em>(1)＝0，

依题意有*F*(*x*)＞0对任意*x*∈[1，＋∞)恒成立，

求导得<em>F</em>′(<em>x</em>)＝e<em><sup>x</sup></em>＋－<em>m</em>，<em>F</em>′(1)＝e＋1－<em>m</em>，<em>F</em>″(<em>x</em>)＝e<em><sup>x</sup></em>－，当<em>x</em>&gt;1时，<em>F</em>″(<em>x</em>)&gt;0，

则*F*′(*x*)在(1，＋∞)上单调递增，有*F*′(*x*)＞*F*′(1)＝e＋1－*m*，

若*m*≤e＋1，则*F*′(*x*)＞0，若*F*(*x*)在(1，＋∞)上单调递增，且*F*(*x*)＞*F*(1)＝0，适合题意；

若<em>m</em>＞e＋1，则<em>F</em>′(1)＜0，又<em>F</em>′(ln <em>m</em>)＝&gt;0，故存在<em>x</em><sub>1</sub>∈(1，ln <em>m</em>)使<em>F</em>′(<em>x</em>)＝0，

当1＜<em>x</em>＜<em>x</em><sub>1</sub>时，<em>F</em>'(<em>x</em>)＜0，得<em>F</em>(<em>x</em>)在(1，<em>x</em><sub>1</sub>)上单调递减，在<em>F</em>(<em>x</em>)＜<em>F</em>(1)＝0，舍去，

综上，实数*m*的取值范围是*m*≤e＋1．

6．已知函数*f*(*x*)＝ln*x*(*ax*＋1－*a*)(*a*＞0)．

(1)当*a*＝时，设*g*(*x*)＝*f*(*x*)－*x*＋1，讨论*g*(*x*)的导函数*g*′(*x*)的单调性；

(2)当*x*＞1时，*f*(*x*)＞*x*－1，求*a*的取值范围．

6．解析　(1)当*a*＝时，*g*(*x*)＝(*x*＋1)ln *x*－*x*＋1，*x*＞0，

∴*g*′(*x*)＝ln *x*＋－，∴*g*″(*x*)＝－＝，

当0＜*x*＜1时，*g*″(*x*)＜0，当*x*＞1时，*g*″(*x*)＞0，

∴*g*′(*x*)在(0，1)上单调递减，在(1，＋∞)上单调递增；

(2)当*x*＞1时，*f*(*x*)＞*x*－1，∴ln*x*(*ax*＋1－*a*)＝ln*x*＋*a*(*x*－1)ln*x*＞*x*－1，

即ln*x*＋*a*(*x*－1)ln*x*－(*x*－1)＞0，

设*h*(*x*)＝ln*x*＋*a*(*x*－1)ln*x*－(*x*－1)，∵*h*(1)＝0，∴*h*(*x*)在(0，＋∞)上单调递增，

∵*h*′(*x*)＝＋*a*ln*x*＋*a*－－1，∵*h*′(1)＝1＋*a*－*a*－1＝0，

设*φ*(*x*)＝＋*a*ln*x*＋*a*－－1，∴*φ*′(*x*)＝－＋＋＝，令*φ*′(*x*)＝0，解得*x*＝，

当≤1时，即*a*≥时，函数*φ*′(*x*)＞0，*φ*(*x*)在(1，＋∞)上单调递增，∴*φ*(*x*)＞*φ*(1)＝0，

∴函数*h*′(*x*)＞0，*h*(*x*)在(1，＋∞)上单调递增，

当0＜*a*＜时，函数*φ*(*x*)在上单调递减，在上单调递增，

∴<em>φ</em>(<em>x</em>)<sub>min</sub>＝<em>φ</em>＜<em>φ</em>(1)＝0，∴<em>h</em>(<em>x</em>)在(1，＋∞)上不单调，

综上所述*a*的取值范围为．

7．设函数<em>f</em> (<em>x</em>)＝<em>ax</em><sup>2</sup>－<em>a</em>－ln<em>x</em>，其中<em>a</em>∈<strong>R</strong>．

(1)讨论*f* (*x*)的单调性；

(2)确定<em>a</em>的所有可能取值，使得<em>f</em> (<em>x</em>)&gt;－e<sup>1－</sup><em><sup>x</sup></em>在区间(1，＋∞)内恒成立(e＝2.718…为自然对数的底数)．

7．解析　(1)由题意，*f* ′(*x*)＝2*ax*－＝，*x*>0，

①当<em>a</em>≤0时，2<em>ax</em><sup>2</sup>－1≤0，<em>f</em> ′(<em>x</em>)≤0，<em>f</em> (<em>x</em>)在(0，＋∞)上单调递减．

②当*a*>0时，*f* ′(*x*)＝，当*x*∈时，*f* ′(*x*)<0；

当*x*∈时，*f* ′(*x*)>0．故*f* (*x*)在上单调递减，在上单调递增．

综上所述，当*a*≤0时，*f*(*x*)在(0，＋∞)上单调递减；当*a*>0时，*f*(*x*)在上单调递减，在上单调递增．

(2)原不等式等价于<em>f</em> (<em>x</em>)－＋e<sup>1－</sup><em><sup>x</sup></em>&gt;0在(1，＋∞)上恒成立．

一方面，令<em>g</em>(<em>x</em>)＝<em>f</em> (<em>x</em>)－＋e<sup>1－</sup><em><sup>x</sup></em>＝<em>ax</em><sup>2</sup>－ln <em>x</em>－＋e<sup>1－</sup><em><sup>x</sup></em>－<em>a</em>，只需<em>g</em>(<em>x</em>)在(1，＋∞)上恒大于0即可．

又<em>g</em>(1)＝0，故<em>g</em>′(<em>x</em>)在<em>x</em>＝1处必大于等于0．令<em>F</em>(<em>x</em>)＝<em>g</em>′(<em>x</em>)＝2<em>ax</em>－＋－e<sup>1－</sup><em><sup>x</sup></em>，由<em>g</em>′(1)≥0，可得<em>a</em>≥．

另一方面，当<em>a</em>≥时，<em>F</em>′(<em>x</em>)＝2<em>a</em>＋－＋e<sup>1－</sup><em><sup>x</sup></em>≥1＋－＋e<sup>1－</sup><em><sup>x</sup></em>＝＋e<sup>1－</sup><em><sup>x</sup></em>，

因为<em>x</em>∈(1，＋∞)，故<em>x</em><sup>3</sup>＋<em>x</em>－2&gt;0．又e<sup>1－</sup><em><sup>x</sup></em>&gt;0，故<em>F</em>′(<em>x</em>)在<em>a</em>≥时恒大于0．

所以当*a*≥时，*F*(*x*)在(1，＋∞)上单调递增．所以*F*(*x*)>*F*(1)＝2*a*－1≥0，

故*g*(*x*)也在(1，＋∞)上单调递增．所以*g*(*x*)>*g*(1)＝0，即*g*(*x*)在(1，＋∞)上恒大于0．

综上所述，*a*≥．故实数*a*的取值范围为．

8．设函数<em>f</em>(<em>x</em>)＝<em>x</em>ln <em>x</em>－<em>ax</em><sup>2</sup>＋(<em>b</em>－1)<em>x</em>，<em>g</em>(<em>x</em>)＝e<em><sup>x</sup></em>－e<em>x</em>．

(1)当*b*＝0时，函数*f*(*x*)有两个极值点，求*a*的取值范围；

(2)若*y*＝*f*(*x*)在点(1，*f*(1))处的切线与*x*轴平行，且函数*h*(*x*)＝*f*(*x*)＋*g*(*x*)在*x*∈(1，＋∞)时，其图象上每一点处切线的倾斜角均为锐角，求*a*的取值范围．

8．解析：(1)当<em>b</em>＝0时，<em>f</em>(<em>x</em>)＝<em>x</em>ln <em>x</em>－<em>ax</em><sup>2</sup>－<em>x</em>，<em>f</em>′(<em>x</em>)＝ln <em>x</em>－2<em>ax</em>，

∴<em>f</em>(<em>x</em>)＝<em>x</em>ln <em>x</em>－<em>ax</em><sup>2</sup>－<em>x</em>有2个极值点就是方程ln <em>x</em>－2<em>ax</em>＝0有2个解，

即*y*＝2*a*与*m*(*x*)＝的图象的交点有2个．∵*m*′(*x*)＝，

当*x*∈(0，e)时，*m*′(*x*)>0，*m*(*x*)单调递增；当*x*∈(e，＋∞)时，*m*′(*x*)<0，*m*(*x*)单调递减．*m*(*x*)有极大值，

又∵*x*∈(0，1]时，*m*(*x*)≤0；当*x*∈(1，＋∞)时，0<*m*(*x*)<．

当*a*∈时，*y*＝2*a*与*m*(*x*)＝的图象的交点有0个；

当*a*∈(－∞，0]或*a*＝时，*y*＝2*a*与*m*(*x*)＝的图象的交点有1个；

当*a*∈时，*y*＝2*a*与*m*(*x*)＝的图象的交点有2个．

综上，*a*的取值范围为．

(2)函数*y*＝*f*(*x*)在点(1，*f*(1))处的切线与*x*轴平行，∴*f*′(1)＝0且*f*(1)≠0，

∵<em>f</em>′(<em>x</em>)＝ln <em>x</em>－2<em>ax</em>＋<em>b</em>，∴<em>b</em>＝2<em>a</em>且<em>a</em>≠1．<em>h</em>(<em>x</em>)＝<em>x</em>ln <em>x</em>－<em>ax</em><sup>2</sup>＋(<em>b</em>－1)<em>x</em>＋e<em><sup>x</sup></em>－e<em>x</em>在<em>x</em>∈(1，＋∞)时，

其图象的每一点处的切线的倾斜角均为锐角，即当*x*>1时，*h*′(*x*)＝*f*′(*x*)＋*g*′(*x*)>0恒成立，

即ln <em>x</em>＋e<em><sup>x</sup></em>－2<em>ax</em>＋2<em>a</em>－e&gt;0恒成立，令<em>t</em>(<em>x</em>)＝ln <em>x</em>＋e<em><sup>x</sup></em>－2<em>ax</em>＋2<em>a</em>－e，∴<em>t</em>′(<em>x</em>)＝＋e<em><sup>x</sup></em>－2<em>a</em>，

设<em>φ</em>(<em>x</em>)＝＋e<em><sup>x</sup></em>－2<em>a</em>，<em>φ</em>′(<em>x</em>)＝e<em><sup>x</sup></em>－，∵<em>x</em>&gt;1，∴e<em><sup>x</sup></em>&gt;e，&lt;1，∴<em>φ</em>′(<em>x</em>)&gt;0，

∴*φ*(*x*)在(1，＋∞)上单调递增，即*t*′(*x*)在(1，＋∞)上单调递增，∴*t*′(*x*)>*t*′(1)＝1＋e－2*a*，

当<em>a</em>≤且<em>a</em>≠1时，<em>t</em>′(<em>x</em>)≥0，∴<em>t</em>(<em>x</em>)＝ln <em>x</em>＋e<em><sup>x</sup></em>－2<em>ax</em>＋2<em>a</em>－e在(1，＋∞)上单调递增，

∴*t*(*x*)>*t*(1)＝0成立，当*a*>时，∵*t*′(1)＝1＋e－2*a*<0，*t*′(ln 2*a*)＝＋2*a*－2*a*>0，

∴存在<em>x</em><sub>0</sub>∈(1，ln 2<em>a</em>)，满足<em>t</em>′(<em>x</em><sub>0</sub>)＝0．∵<em>t</em>′(<em>x</em>)在(1，＋∞)上单调递增，

∴当<em>x</em>∈(1，<em>x</em><sub>0</sub>)时，<em>t</em>′(<em>x</em>)&lt;0，<em>t</em>(<em>x</em>)单调递减，∴<em>t</em>(<em>x</em><sub>0</sub>)&lt;<em>t</em>(1)＝0，<em>t</em>(<em>x</em>)&gt;0不恒成立．

∴实数*a*的取值范围为(－∞，1)∪．

