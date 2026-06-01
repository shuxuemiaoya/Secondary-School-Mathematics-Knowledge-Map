**专题18　用导数证明数列不等式**

![](images/eda8244ecb7862b812506dbb0b73d9f86b995b993ff0b9ec34614e4992fde8d3.jpg)

**【基本方法】**

证明与数列有关的不等式的策略

利用导数证明数列不等式，一方面以函数为背景让学生探寻函数的性质，另一方面体现数列是特殊的函数，进而利用恒成立的不等式将没有规律的数列放缩为为有具体特征的数列，巧妙地将函数、导数、数列、不等式结合在一起．

证明此类问题时常根据已知的函数不等式，用关于正整数*n*的不等式替代函数不等式中的自变量．通过多次求和达到证明的目的．此类问题一般至少有两问，已知的不等式常由第一问根据待证式的特征而得到．

已知函数式为指数不等式(或对数不等式)，而待证不等式为与对数有关的不等式(或与指数有关的不等式)，还要注意指、对数式的互化，如e<em><sup>x</sup></em>＞<em>x</em>＋1可化为ln<em>x</em>≤<em>x－</em>1等．

**【基本题型】**

<strong>[例1]</strong>　已知函数<em>f</em> (<em>x</em>)＝<em>kx</em>－ln<em>x</em>－1(<em>k</em>&gt;0)．

(1)若函数*f* (*x*)有且只有一个零点，求实数*k*的值；

(2)证明：当<em>n</em>∈<strong>N</strong><sup>\*</sup>时，1＋＋＋…＋&gt;ln(<em>n</em>＋1)．

<strong>解析</strong>　(1)法一：<em>f</em> (<em>x</em>)＝<em>kx</em>－ln <em>x</em>－1，<em>f</em> ′(<em>x</em>)＝<em>k</em>－＝(<em>x</em>&gt;0，<em>k</em>&gt;0)，

当0<*x*<时，*f* ′(*x*)<0；当*x*>时，*f* ′(*x*)>0．∴*f* (*x*)在(0，)上单调递减，在(，＋∞)上单调递增．

∴<em>f</em> (<em>x</em>)<sub>min</sub>＝<em>f</em> ＝ln <em>k</em>，∵<em>f</em> (<em>x</em>)有且只有一个零点，∴ln <em>k</em>＝0，∴<em>k</em>＝1．

法二：由题意知方程*kx*－ln *x*－1＝0仅有一个实根，由*kx*－ln *x*－1＝0，得*k*＝(*x*>0)，

令*g*(*x*)＝(*x*>0)，*g*′(*x*)＝，当0<*x*<1时，*g*′(*x*)>0；当*x*>1时，*g*′(*x*)<0．

∴<em>g</em>(<em>x</em>)在(0,1)上单调递增，在(1，＋∞)上单调递减，∴<em>g</em>(<em>x</em>)<sub>max</sub>＝<em>g</em>(1)＝1，当<em>x</em>→＋∞时，<em>g</em>(<em>x</em>)→0，

∴要使*f* (*x*)仅有一个零点，则*k*＝1．

法三：函数<em>f</em> (<em>x</em>)有且只有一个零点，即直线<em>y</em>＝<em>kx</em>与曲线<em>y</em>＝ln <em>x</em>＋1相切，设切点为(<em>x</em><sub>0</sub>，<em>y</em><sub>0</sub>)，

由<em>y</em>＝ln <em>x</em>＋1，得<em>y</em>′＝，∴∴<em>k</em>＝<em>x</em><sub>0</sub>＝<em>y</em><sub>0</sub>＝1，∴实数<em>k</em>的值为1．

(2)由(1)知*x*－ln *x*－1≥0，即*x*－1≥ln *x*，当且仅当*x*＝1时取等号，

∵<em>n</em>∈<strong>N</strong><sup>\*</sup>，令<em>x</em>＝，得&gt;ln，∴1＋＋＋…＋&gt;ln＋ln＋…＋ln＝ln(<em>n</em>＋1)，

故1＋＋＋…＋>ln(*n*＋1)．

<strong>[例2]</strong>　已知函数<em>f</em>(<em>x</em>)＝ln(<em>x</em>＋1)＋．

(1)若*x*＞0时，*f*(*x*)＞1恒成立，求*a*的取值范围；

(2)求证：ln (<em>n</em>＋1)＞＋＋ ＋…＋(<em>n</em>∈<strong>N</strong><sup>\*</sup>)．

解析　(1)由ln (*x*＋1)＋＞1，得*a*＞(*x*＋2)－(*x*＋2)ln (*x*＋1)．

令*g*(*x*)＝(*x*＋2)[1－ln (*x*＋1)]，则*g*′(*x*)＝1－ln (*x*＋1)－＝－ln (*x*＋1)－．

当*x*＞0时，*g*′(*x*)＜0，所以*g*(*x*)在(0，＋∞)上单调递减．

所以*g*(*x*)＜*g*(0)＝2，故*a*的取值范围为[2，＋∞)．

(2)由(1)知ln (*x*＋1)＋＞1(*x*＞0)，所以ln (*x*＋1)＞．

令*x*＝(*k*＞0)，得ln (＋1)＞，即ln ＞．

所以ln ＋ln ＋ln ＋…＋ln ＞＋＋＋…＋，

即ln (<em>n</em>＋1)＞＋＋＋…＋(<em>n</em>∈<strong>N</strong><sup>\*</sup>)．

<strong>[例3]</strong>　已知函数<em>f</em>(<em>x</em>)＝<em>ax</em><sup>2</sup>－<em>x</em>·ln<em>x</em>＋<em>b</em>，<em>g</em>(<em>x</em>)＝<em>f</em>′(<em>x</em>)．

(1)判断函数*y*＝*g*(*x*)的单调性；

(2)若*x*∈(0，e](e≈2.718)，判断是否存在实数*a*，使函数*g*(*x*)的最小值为2？若存在，求出*a*的值；若不存在，请说明理由；

(3)证明：3>*n*－ln．

解析　(1)*g*(*x*)＝*ax*－1－ln *x*，*x*>0，∴*g*′(*x*)＝*a*－＝，

当*a*≤0时，*g*′(*x*)<0，*g*(*x*)在(0，＋∞)上单调递减，

当*a*>0时，在*x*∈，*g*′(*x*)<0，在*x*∈，*g*′(*x*)>0，

∴*g*(*x*)在上单调递减，在上单调递增．

(2)当<em>a</em>≤0时，函数<em>g</em>(<em>x</em>)在 (0，e]上单调递减，<em>g</em>(<em>x</em>)<sub>min</sub>＝<em>a</em>e－2≤－2，故不存在最小值为2；

当 0<*a*≤时，即≥e，函数*g*(*x*)在(0，e]上单调递减，

∴当<em>x</em>＝e时有最小值，<em>g</em>(<em>x</em>)<sub>min</sub>＝<em>a</em>e－1－1＝2，解得<em>a</em>＝，不合题意舍去；

当*a*>时，即0<<e，函数*g*(*x*)在上单调递减，在上单调递增，

∴当<em>x</em>＝时有最小值，<em>g</em>(<em>x</em>)<sub>min</sub>＝1－1＋ln <em>a</em>＝2，解得<em>a</em>＝e<sup>2</sup>．

综上所述，存在实数<em>a</em>＝e<sup>2</sup>，当<em>x</em>∈(0，e]时，函数<em>g</em>(<em>x</em>)的最小值是2．

(3)由(2)知，<em>g</em>(<em>x</em>)＝e<sup>2</sup><em>x</em>－1－ln <em>x</em>≥2，即e<sup>2</sup><em>x</em>≥3＋ln <em>x</em>恒成立，

即*x*≥(3＋ln *x*)恒成立，即*x*>(3＋ln *x*)，取*x*＝，

则>，则3·>1＋ln ，

∴3>*n*＋ln＝*n*＋ln＝*n*－ln ．

<strong>[例4]</strong>　已知函数<em>f</em>(<em>x</em>)＝e<em><sup>x</sup></em>，<em>h</em>(<em>x</em>)＝<em>x</em>＋ln <em>x</em>，<em>g</em>(<em>x</em>)＝(<em>x</em>－<em>a</em>＋1)e<em><sup>a</sup></em>．

(1)设*F*(*x*)＝*xf*(*x*)－*ah*(*x*)，讨论*F*(*x*)极值点的个数；

(2)判断方程<em>f</em>(<em>x</em>)＝<em>g</em>(<em>x</em>)的实数根的个数，并证明e<sup>2</sup>＋e<sup>4</sup>＋e<sup>6</sup>＋…＋e<sup>2</sup><em><sup>n</sup></em>≥e．

解析　(1)<em>F</em>(<em>x</em>)＝<em>x</em>e<em><sup>x</sup></em>－<em>a</em>(<em>x</em>＋ln <em>x</em>)，<em>x</em>＞0，∴<em>F</em>′(<em>x</em>)＝(<em>x</em>＋1)e<em><sup>x</sup></em>－<em>a</em>＝，

①当*a*≤0时，*F*′(*x*)＞0，*F*(*x*)在(0，＋∞)内单调递增，*F*(*x*)没有极值点．

②当<em>a</em>＞0时，令<em>H</em>(<em>x</em>)＝<em>x</em>e<em><sup>x</sup></em>－<em>a</em>，<em>x</em>∈[0，＋∞)，则<em>H</em>′(<em>x</em>)＝(1＋<em>x</em>)e<em><sup>x</sup></em>＞0，

∴<em>H</em>(<em>x</em>)在[0，＋∞)上单调递增．又<em>H</em>(0)＝－<em>a</em>＜0，<em>H</em>(<em>a</em>)＝<em>a</em>(e<em><sup>a</sup></em>－1)＞0，

∴∃<em>x</em><sub>0</sub>＞0，使<em>H</em>(<em>x</em><sub>0</sub>)＝0，且当<em>x</em>∈(0，<em>x</em><sub>0</sub>)时，<em>H</em>(<em>x</em>)＜0，

当<em>x</em>∈(<em>x</em><sub>0</sub>，＋∞)时，<em>H</em>(<em>x</em>)＞0，从而<em>F</em>′(<em>x</em><sub>0</sub>)＝0，当<em>x</em>∈(0，<em>x</em><sub>0</sub>)时，<em>F</em>′(<em>x</em>)＜0，<em>F</em>(<em>x</em>)单调递减，

当<em>x</em>∈(<em>x</em><sub>0</sub>，＋∞)时，<em>F</em>′(<em>x</em>)＞0，<em>F</em>(<em>x</em>)单调递增，∴<em>x</em>＝<em>x</em><sub>0</sub>是函数<em>F</em>(<em>x</em>)的极小值点．

综上，当*a*≤0时，*F*(*x*)无极值点，当*a*＞0时，*F*(*x*)有一个极值点．

(2)方程<em>f</em>(<em>x</em>)＝<em>g</em>(<em>x</em>)可化为e<em><sup>x</sup></em><sup>－</sup><em><sup>a</sup></em>＝<em>x</em>－<em>a</em>＋1．设<em>x</em>－<em>a</em>＝<em>t</em>，则原方程又可化为e<em><sup>t</sup></em>＝<em>t</em>＋1．

设<em>M</em>(<em>t</em>)＝e<em><sup>t</sup></em>－<em>t</em>－1，则<em>M</em>′(<em>t</em>)＝e<em><sup>t</sup></em>－1．

∵*M*′(0)＝0，当*t*∈(－∞，0)时，*M*′(*t*)＜0，*M*(*t*)在(－∞，0)上单调递减，

当*t*∈(0，＋∞)时，*M*′(*t*)＞0，*M*(*t*)在(0，＋∞)上单调递增；

∴<em>M</em>(<em>t</em>)<sub>min</sub>＝<em>M</em>(0)＝0，∴当<em>t</em>≠0时，<em>M</em>(<em>t</em>)＞0，

∴方程e<em><sup>t</sup></em>＝<em>t</em>＋1只有一个实数根，∴方程<em>f</em>(<em>x</em>)＝<em>g</em>(<em>x</em>)只有一个实数根．

∵对于任意的<em>t</em>∈<strong>R</strong>，e<em><sup>t</sup></em>≥<em>t</em>＋1．

∴e<sup>2－</sup>＋e<sup>4－</sup>＋…＋e<sup>2</sup><em><sup>n</sup></em><sup>－</sup>≥＋1＋＋1＋…＋＋1

＝(2＋4＋…＋2*n*)－＋*n*＝*n*(*n*＋1)－＋*n*＝，

即e<sup>－</sup>(e<sup>2</sup>＋e<sup>4</sup>＋…＋e<sup>2</sup><em><sup>n</sup></em>)≥，∴e<sup>2</sup>＋e<sup>4</sup>＋…＋e<sup>2</sup><em><sup>n</sup></em>≥e．

<strong>[例5]</strong>　已知函数<em>g</em>(<em>x</em>)＝<em>x</em>ln<em>x</em>，<em>h</em>(<em>x</em>)＝(<em>a</em>&gt;0)．

(1)若*g*(*x*)<*h*(*x*)对*x*∈(1，＋∞)恒成立，求*a*的取值范围；

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

(2)证明：不等式·…·<对于正整数*n*恒成立，其中e＝2.718 28…为自然对数的底数．

解析　(1)方法一　记<em>f</em>(<em>x</em>)＝<em>g</em>(<em>x</em>)－<em>h</em>(<em>x</em>)＝<em>x</em>ln <em>x</em>－<em>x</em><sup>2</sup>＋，令<em>φ</em>(<em>x</em>)＝<em>f</em>′(<em>x</em>)＝ln <em>x</em>＋1－<em>ax</em>，则<em>φ</em>′(<em>x</em>)＝－<em>a</em>，

①当*a*≥1时，∵*x*∈(1，＋∞)，∴*φ*′(*x*)＝－*a*<1－*a*≤0，∴*f*′(*x*)在(1，＋∞)上单调递减，又*f*′(1)＝1－*a*≤0，

∴*f*′(*x*)<0，即*f*(*x*)在(1，＋∞)上单调递减，此时，*f*(*x*)<*f*(1)＝－≤0，即*g*(*x*)<*h*(*x*)，∴*a*≥1．

②当0<*a*<1时，考虑*x*∈时，*φ*′(*x*)＝－*a*>*a*－*a*＝0，

∴*f*′(*x*)在上单调递增，又*f*′(1)＝1－*a*>0，∴*f*′(*x*)>0，即*f*(*x*)在上单调递増，

*f*(*x*)>*f*(1)＝－>0，不满足题意．综上所述，*a*∈[1，＋∞)．

方法二　当*x*∈(1，＋∞)时，*g*(*x*)<*h*(*x*)等价于*a*>，令*F*(*x*)＝(*x*>1)，

*F*′(*x*)＝(*x*>1)，记*m*(*x*)＝*x*－1－*x*ln *x*(*x*>1)，则*m*′(*x*)＝－ln *x*<0，

∴*m*(*x*)在(1，＋∞)上单调递减，∴*m*(*x*)<*m*(1)＝0，∴*F*′(*x*)<0，即*F*(*x*)在(1，＋∞)上单调递减，

*F*(*x*)<*F*(1)＝1，故*a*∈[1，＋∞)．

(2)由(1)知取*a*＝1，当*x*∈(1，＋∞)时，*g*(*x*)<*h*(*x*)恒成立，即*x*ln*x*<恒成立，即ln*x*<恒成立，

即ln(1＋*x*)<＝对于*x*∈(0，＋∞)恒成立，

由此，ln&lt;＝≤，<em>k</em>∈<strong>N</strong><sup>\*</sup>，

于是ln＝ln＋ln＋…＋ln

<＝

＝·＝＝≤，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

故·…·<．

<strong>[例6]</strong>　已知函数<em>f</em>(<em>x</em>)＝e<em><sup>x</sup></em>－<em>kx</em><sup>2</sup>，<em>x</em>∈<strong>R</strong>．

(1)若*k*＝，求证：当*x*∈(0，＋∞)时，*f*(*x*)>1；

(2)若*f*(*x*)在区间(0，＋∞)上单调递增，试求*k*的取值范围；

(3)求证：…&lt;e<sup>4</sup>(<em>n</em>∈<strong>N</strong><sup>\*</sup>)．

解析　(1) <em>f</em>(<em>x</em>)＝e<em><sup>x</sup></em>－<em>x</em><sup>2</sup>，则<em>h</em>(<em>x</em>)＝<em>f</em>′(<em>x</em>)＝e<em><sup>x</sup></em>－<em>x</em>．所以<em>h</em>′(<em>x</em>)＝e<em><sup>x</sup></em>－1&gt;0(<em>x</em>&gt;0)，

所以*h*(*x*)在(0，＋∞)上递增，所以*f*′(*x*)>*f*′(0)＝1>0．

所以<em>f</em>(<em>x</em>)＝e<em><sup>x</sup></em>－<em>x</em><sup>2</sup>在(0，＋∞)上递增，故<em>f</em>(<em>x</em>)&gt;<em>f</em>(0)＝1．

(2)由题得，<em>f</em>′(<em>x</em>)＝e<em><sup>x</sup></em>－2<em>kx</em>≥0在区间(0，＋∞)上恒成立．即2<em>k</em>≤在区间(0，＋∞)上恒成立．

设*g*(*x*)＝，*x*∈(0，＋∞)，则*g*′(*x*)＝，

故在(0，1)上，*g*′(*x*)<0，*g*(*x*)单调递减；在(1，＋∞)上，*g*′(*x*)>0，*g*(*x*)单调递增，故*g*(*x*)≥*g*(1)＝e．

故2*k*≤e，解得*k*≤．即*k*的取值范围为．

(3)由(1)知，对于<em>x</em>∈(0，＋∞)，有<em>f</em>(<em>x</em>)＝e<em><sup>x</sup></em>－<em>x</em><sup>2</sup>&gt;1，所以e<sup>2</sup><em><sup>x</sup></em>&gt;2<em>x</em><sup>2</sup>＋1，

则ln (2<em>x</em><sup>2</sup>＋1)&lt;2<em>x</em>，取<em>x</em>＝，从而有ln &lt;(<em>n</em>∈<strong>N</strong><sup>\*</sup>)，

于是ln＋ln＋ln＋…＋ln<＋＋＋…＋

<＋＋＋…＋＝2＋2[＋＋…＋]＝4－<4．

所以…&lt;e<sup>4</sup>(<em>n</em>∈<strong>N</strong><sup>\*</sup>)．

<strong>[例7]</strong>　已知函数<em>f</em>(<em>x</em>)＝ln(1＋<em>x</em>)－．

(1)若*x*≥0时，*f*(*x*)≤0，求*λ*的最小值；

(2)设数列{<em>a<sub>n</sub></em>}的通项<em>a<sub>n</sub></em>＝1＋＋＋…＋，证明：<em>a</em><sub>2</sub><em><sub>n</sub></em>－<em>a<sub>n</sub></em>＋&gt;ln2．

解析　(1)由已知可得*f*(0)＝0，∵*f*(*x*)＝ln(1＋*x*)－，

∴*f*′(*x*)＝，且*f*′(0)＝0．

①若*λ*≤0，则当*x*>0时，*f*′(*x*)>0，*f*(*x*)单调递增，∴*f*(*x*)≥*f*(0)＝0，不合题意；

②若0<*λ*<，则当0<*x*<时，*f*′(*x*)>0，*f*(*x*)单调递增，∴当0<*x*<时，*f*(*x*)>*f*(0)＝0，不合题意；

③若*λ*≥，则当*x*>0时，*f*′(*x*)<0，*f*(*x*)单调递减，当*x*≥0时，*f*(*x*)≤*f*(0)＝0，符合题意．

综上，*λ*≥．∴实数*λ*的最小值为．

(2)由于<em>a</em><sub>2</sub><em><sub>n</sub></em>－<em>a<sub>n</sub></em>＋＝＋＋＋…＋＋＋，

若*λ*＝，由(1)知，*f*(*x*)＝ln(1＋*x*)－，且当*x*>0时，*f*(*x*)<0，即>ln(1＋*x*)，

令*x*＝，则>ln ，∴＋>ln ，＋>ln ，

＋>ln ，…，＋>ln ．

以上各式两边分别相加可得

＋＋＋＋＋＋…＋＋

>ln ＋ln ＋ln ＋…＋ln ，

即＋＋＋…＋＋＋>ln ···…·＝ln ＝ln 2，

∴<em>a</em><sub>2</sub><em><sub>n</sub></em>－<em>a<sub>n</sub></em>＋&gt;ln 2．

**【对点精练】**

1．若函数<em>f</em>(<em>x</em>)＝e<em><sup>x</sup></em>－<em>ax</em>－1(<em>a</em>＞0)在<em>x</em>＝0处取极值．

(1)求*a*的值，并判断该极值是函数的最大值还是最小值；

(2)证明：1＋＋＋…＋＞ln(<em>n</em>＋1)(<em>n</em>∈<strong>N</strong><sup>\*</sup>)．

1．解析　(1)因为*x*＝0是函数极值点，所以*f*′(0)＝0，所以*a*＝1．

<em>f</em>(<em>x</em>)＝e<em><sup>x</sup></em>－<em>x</em>－1，易知<em>f</em>′(<em>x</em>)＝e<em><sup>x</sup></em>－1．当<em>x</em>∈(0，＋∞)时，<em>f</em>′(<em>x</em>)＞0，当<em>x</em>∈(－∞，0)时，<em>f</em>′(<em>x</em>)＜0，

故极值*f*(0)是函数最小值．

(2)由(1)知e<em><sup>x</sup></em>≥<em>x</em>＋1．即ln (<em>x</em>＋1)≤<em>x</em>，当且仅当<em>x</em>＝0时，等号成立，令<em>x</em>＝(<em>k</em>∈<strong>N</strong><sup>\*</sup>)，

则＞ln (1＋)，即＞ln，所以＞ln (1＋*k*)－ln *k*(*k*＝1，2，…，*n*)，

累加得1＋＋＋…＋＞ln (<em>n</em>＋1)(<em>n</em>∈<strong>N</strong><sup>\*</sup>)．

2．已知函数<em>f</em>(<em>x</em>)＝ln(<em>x</em>＋1)＋(<em>a</em>∈<strong>R</strong>)．

(1)当*a*＜0时，求*f*(*x*)的极值；

(2)求证：ln(<em>n</em>＋1)＞＋＋…＋(<em>n</em>∈<strong>N</strong><sup>\*</sup>)．

2．<strong>解析</strong>　(1)<em>f</em>(<em>x</em>)＝ln(<em>x</em>＋1)＋(<em>x</em>＞－1)，<em>f</em>′(<em>x</em>)＝，

∵*a*＜0，∴当*x*∈(－1，－*a*－1)时，*f*′(*x*)＜0，当*x*∈(－*a*－1，＋∞)时，*f*′(*x*)＞0，

∴函数*f*(*x*)的极小值为*f*(－*a*－1)＝*a*＋1＋ln(－*a*)，无极大值．

(2)由(1)知，取*a*＝－1，*f*(*x*)＝ln(*x*＋1)－≥*f*(0)＝0．

当*x*＞0时，ln(*x*＋1)＞，取*x*＝，得ln＞＞．

∴ln＋ln＋…＋ln＞＋＋…＋⇔ln＞＋＋…＋，

即ln(n＋1)＞＋＋…＋．

3．已知函数*f*(*x*)＝*x*ln*x*，*g*(*x*)＝*x*－1．

(1)求*F*(*x*)＝*g*(*x*)－*f*(*x*)的单调区间和最值；

(2)证明：对大于1的任意自然数*n*，都有＋＋＋…＋＜ln*n*．

3．解析　(1)由*F*(*x*)＝*x*－1－*x*ln *x*，*x*>0，则*F*′(*x*)＝－ln *x*，

所以当*x*＞1时，*F*′(*x*)＝－ln *x*＜0，当0＜*x*＜1时，*F*′(*x*)＝－ln *x*＞0，

所以当*x*＝1时，*F*(*x*)取最大值*F*(1)＝0.

即当*x*≠1时，*F*(*x*)＜0，当*x*＝1时，*F*(*x*)＝0，

所以*F*(*x*)在(0，1)上是单调增函数，在(1，＋∞)上是单调减函数，

当*x*＝1时，*F*(*x*)取最大值*F*(1)＝0，无最小值．

(2)由(1)可知，*x*ln *x*＞*x*－1对任意*x*＞0且*x*≠1恒成立．

故1－＜ln <em>x</em>，取<em>x</em>＝(<em>n</em>＞1且<em>n</em>∈<strong>N</strong>)得，1－＜ln⇒＜ln <em>n</em>－ln(<em>n</em>－1)，

所以＜ln *i*－ln(*i*－1)]，即＋＋＋…＋＜ln *n*，

综上，对大于1的任意自然数*n*，都有＋＋＋…＋＜ln *n*成立．

4．已知函数<em>f</em>(<em>x</em>)＝e<em><sup>x</sup></em>，<em>g</em>(<em>x</em>)＝ln(<em>x</em>＋<em>a</em>)＋<em>b</em>．

(1)若函数*f*(*x*)与*g*(*x*)的图象在点(0，1)处有相同的切线，求*a*，*b*的值；

(2)当*b*＝0时，*f*(*x*)－*g*(*x*)＞0恒成立，求整数*a*的最大值；

(3)求证：ln2＋(ln3－ln2)<sup>2</sup>＋(ln4－ln3)<sup>3</sup>＋…＋[ln(<em>n</em>＋1)－ln<em>n</em>]<em><sup>n</sup></em>＜(<em>n</em>∈<strong>N</strong><sup>\*</sup>)．

4．解析　(1)因为函数*f*(*x*)和*g*(*x*)的图象在点(0，1)处有相同的切线，所以*f*(0)＝*g*(0)且*f*′(0)＝*g*′(0)，

又因为<em>f</em>′(<em>x</em>)＝e<em><sup>x</sup></em>，<em>g</em>′(<em>x</em>)＝，所以1＝ln <em>a</em>＋<em>b，</em>1＝，解得<em>a</em>＝1，<em>b</em>＝1．

(2)现证明e<em><sup>x</sup></em>≥<em>x</em>＋1，设<em>F</em>(<em>x</em>)＝e<em><sup>x</sup></em>－<em>x</em>－1，则<em>F</em>′(<em>x</em>)＝e<em><sup>x</sup></em>－1，

当*x*∈(0，＋∞)时，*F*′(*x*)＞0，当*x*∈(－∞，0)时，*F*′(*x*)＜0，

所以*F*(*x*)在(0，＋∞)上单调递增，在(－∞，0)上单调递减，

所以<em>F</em>(<em>x</em>)<sub>min</sub>＝<em>F</em>(0)＝0，即<em>F</em>(<em>x</em>)≥0恒成立，即e<em><sup>x</sup></em>≥<em>x</em>＋1．

同理可得ln(<em>x</em>＋2)≤<em>x</em>＋1，即e<em><sup>x</sup></em>＞ln(<em>x</em>＋2)，

当<em>a</em>≤2时，ln(<em>x</em>＋<em>a</em>)≤ln(<em>x</em>＋2)＜e<em><sup>x</sup></em>，所以当<em>a</em>≤2时，<em>f</em>(<em>x</em>)－<em>g</em>(<em>x</em>)＞0恒成立．

当<em>a</em>≥3时，e<sup>0</sup>＜ln <em>a</em>，即e<em><sup>x</sup></em>－ln(<em>x</em>＋<em>a</em>)＞0不恒成立．故整数<em>a</em>的最大值为2．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

(3)由(2)知e<em><sup>x</sup></em>＞ln(<em>x</em>＋2)，令<em>x</em>＝，则＞ln，

即e<sup>－</sup><em><sup>n</sup></em><sup>＋1</sup>＞<em><sup>n</sup></em>＝[ln(<em>n</em>＋1)－ln <em>n</em>]<em><sup>n</sup></em>，

所以e<sup>0</sup>＋e<sup>－1</sup>＋e<sup>－2</sup>＋…＋e<sup>－</sup><em><sup>n</sup></em><sup>＋1</sup>＞ln 2＋(ln 3－ln 2)<sup>2</sup>＋(ln 4－ln 3)<sup>3</sup>＋…＋[ln(<em>n</em>＋1)－ln <em>n</em>]<em><sup>n</sup></em>，

又因为e<sup>0</sup>＋e<sup>－1</sup>＋e<sup>－2</sup>＋…＋e<sup>－</sup><em><sup>n</sup></em><sup>＋1</sup>＝＜＝，

所以ln2＋(ln3－ln2)<sup>2</sup>＋(ln4－ln3)<sup>3</sup>＋…＋[ln(<em>n</em>＋1)－ln <em>n</em>]<em><sup>n</sup></em>＜．

5．已知函数*f*(*x*)＝ln(1＋*x*)．

(1)求证：当*x*∈(0，＋∞)时，<*f*(*x*)<*x*；

(2)已知e为自然对数的底数，求证：∀<em>n</em>∈<strong>N</strong><sup>\*</sup>，&lt;·…·&lt;e．

5．解析　(1)令*g*(*x*)＝*f*(*x*)－＝ln(1＋*x*)－(*x*>0)，则*g*′(*x*)＝－＝>0(*x*>0)，

所以*g*(*x*)在(0，＋∞)上是增函数，所以当*x*∈(0，＋∞)时，*g*(*x*)>*g*(0)＝0，即*f*(*x*)>成立．

令*h*(*x*)＝*f*(*x*)－*x*＝ln(1＋*x*)－*x*(*x*>0)，则*h*′(*x*)＝－1＝－<0(*x*>0)，

所以*h*(*x*)在(0，＋∞)上是减函数，所以当*x*∈(0，＋∞)时，*h*(*x*)<*h*(0)＝0，即*f*(*x*)<*x*成立．

综上所述，当*x*∈(0，＋∞)时，<*f*(*x*)<*x*成立．

(2)由(1)可知，ln(1＋*x*)<*x*对*x*∈(0，＋∞)都成立，

所以ln＋ln＋…＋ln<＋＋…＋，

即ln<＝．

因为<em>n</em>∈<strong>N</strong><sup>\*</sup>，所以＝＋≤＋＝1，所以ln&lt;1，

所以 ·…·<e．又由(1)可知，ln(1＋*x*)>对*x*∈(0，＋∞)都成立，

所以ln>＝(*k*＝1，2，…，*n*)，

所以ln＝ln＋ln＋…＋ln

>＋＋…＋≥＋＋…＋＝＝，

所以ln>，所以·…·>，

所以<·…·<e．

6．(2017·全国Ⅲ改编)已知函数*f*(*x*)＝*x*－1－*a*ln *x*．

(1)若*f*(*x*)≥0，求*a*的值；

(2)证明：对于任意正整数*n*，…＜e．

6．解析　(1)*f*(*x*)的定义域为(0，＋∞)，

①若*a*≤0，因为*f* ＝－＋*a*ln 2＜0，所以不满足题意．

②若*a*＞0，由*f*′(*x*)＝1－＝知，当*x*∈(0，*a*)时，*f*′(*x*)＜0；当*x*∈(*a*，＋∞)时，*f*′(*x*)＞0；

所以*f*(*x*)在(0，*a*)单调递减，在(*a*，＋∞)单调递增，

故*x*＝*a*是*f*(*x*)在(0，＋∞)的唯一最小值点．

因为*f*(1)＝0，所以当且仅当*a*＝1时，*f*(*x*)≥0，故*a*＝1.

(2)由(1)知当*x*∈(1，＋∞)时，*x*－1－ln *x*＞0．

令*x*＝1＋，得ln＜．

从而ln＋ln＋…＋ln＜＋＋…＋＝1－＜1．

故…＜e．

7．已知函数<em>f</em>(<em>x</em>)＝ln<em>x</em>＋<em>ax</em><sup>2</sup>－(2<em>a</em>＋1)<em>x</em>．

(1)若函数*f*(*x*)的图象在点(2，*f*(2))处的切线的斜率为1，求实数*a*的值；

(2)讨论函数*f*(*x*)的单调性；

(3)证明：对任意的<em>n</em>∈<strong>N</strong><sup>\*</sup>，都有ln(1＋<em>n</em>)&gt;成立．

7．<strong>解析</strong>　由题意得<em>f</em>′(<em>x</em>)＝＋2<em>ax</em>－(2<em>a</em>＋1)＝＝，<em>x</em>∈(0，＋∞)．

(1)由题意得*f*′(2)＝1，即＝1，解得*a*＝．

(2)①当*a*≤0时，2*ax*－1<0在(0，＋∞)上恒成立，由*f*′(*x*)>0得0<*x*<1，由*f*′(*x*)<0得*x*>1，

故函数*f*(*x*)在(0，1)上单调递增，在(1，＋∞)上单调递减．

②当*a*>0时，令*f*′(*x*)＝0得*x*＝1或*x*＝，当<1，即*a*>时，由*f*′(*x*)>0得*x*>1或0<*x*<，由*f*′(*x*)<0得<*x*<1，故函数*f*(*x*)在，(1，＋∞)上单调递增，在上单调递减；

当>1，即0<*a*<时，由*f*′(*x*)>0，得*x*>或0<*x*<1，由*f*′(*x*)<0得1<*x*<，

故函数*f*(*x*)在(0，1)，上单调递增，在上单调递减；

当＝1，即*a*＝时，在(0，＋∞)上恒有*f*′(*x*)≥0，故函数*f*(*x*)在(0，＋∞)上单调递增．

综上可知，当*a*≤0时，函数*f*(*x*)在(0，1)上单调递增，在(1，＋∞)上单调递减；

当0<*a*<时，函数*f*(*x*)在(0，1)上单调递增，在上单调递减，在上单调递增；

当*a*＝时，函数*f*(*x*)在(0，＋∞)上单调递增；

当*a*>时，函数*f*(*x*)在上单调递增，在上单调递减，在(1，＋∞)上单调递增．

(3)由(2)知，当<em>a</em>＝1时，函数<em>f</em>(<em>x</em>)＝ln <em>x</em>＋<em>x</em><sup>2</sup>－3<em>x</em>在(1，＋∞)上单调递增，

∴ln <em>x</em>＋<em>x</em><sup>2</sup>－3<em>x</em>≥<em>f</em>(1)＝－2，即ln <em>x</em>≥－<em>x</em><sup>2</sup>＋3<em>x</em>－2＝－(<em>x</em>－1)(<em>x</em>－2)，

令<em>x</em>＝1＋，<em>n</em>∈<strong>N</strong><sup>\*</sup>，则ln&gt;－，

∴ln＋ln＋ln＋…＋ln>－＋－＋－＋…＋－，

∴ln>－＋－＋－＋…＋－，即ln(1＋*n*)> ．

故对任意的<em>n</em>∈<strong>N</strong><sup>\*</sup>，都有ln(1＋<em>n</em>)&gt; 成立．

