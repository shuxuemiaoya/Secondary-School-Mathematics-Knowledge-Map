**专题20　单变量含参不等式证明方法之合理消参**

![](images/dfa3bd3da35318f9831f94eb3685b97ff1219c49e183f9fe362b8304bd5d3bac.jpg)

**【例题选讲】**

<strong>[例1]</strong> (2018·全国Ⅰ)已知函数<em>f</em>(<em>x</em>)＝<em>a</em>e<em><sup>x</sup></em>－ln<em>x</em>－1．

(1)设*x*＝2是*f*(*x*)的极值点，求*a*，并求*f*(*x*)的单调区间；

(2)证明：当*a*≥时，*f*(*x*)≥0．

<strong>解析</strong>　(1)<em>f</em>(<em>x</em>)的定义域为(0，＋∞)，<em>f</em>′(<em>x</em>)＝<em>a</em>e<em><sup>x</sup></em>－．由题设知，<em>f</em>′(2)＝0，所以<em>a</em>＝．

从而<em>f</em>(<em>x</em>)＝e<em><sup>x</sup></em>－ln <em>x</em>－1，<em>f</em>′(<em>x</em>)＝e<em><sup>x</sup></em>－．当0＜<em>x</em>＜2时，<em>f</em>′(<em>x</em>)＜0；当<em>x</em>＞2时，<em>f</em>′(<em>x</em>)＞0．

所以*f*(*x*)在(0，2)单调递减，在(2，＋∞)单调递增．

(2)证明：当*a*≥时，*f*(*x*)≥－ln *x*－1．设*g*(*x*)＝－ln *x*－1，则*g*′(*x*)＝－．

当0＜*x*＜1时，*g*′(*x*)＜0；当*x*＞1时，*g*′(*x*)＞0．所以*x*＝1是*g*(*x*)的最小值点．

故当*x*＞0时，*g*(*x*)≥*g*(1)＝0．因此，当*a*≥时，*f*(*x*)≥0．

<strong>[例2]</strong>　设<em>a</em>为实数，函数<em>f</em> (<em>x</em>)＝e<em><sup>x</sup></em>－2<em>x</em>＋2<em>a</em>，<em>x</em>∈<strong>R</strong>．

(1)求*f* (*x*)的单调区间与极值；

(2)求证：当<em>a</em>&gt;ln2－1且<em>x</em>&gt;0时，e<em><sup>x</sup></em>&gt;<em>x</em><sup>2</sup>－2<em>ax</em>＋1．

<strong>解析</strong>　(1)由<em>f</em> (<em>x</em>)＝e<em><sup>x</sup></em>－2<em>x</em>＋2<em>a</em>(<em>x</em>∈<strong>R</strong>)，知<em>f</em> ′(<em>x</em>)＝e<em><sup>x</sup></em>－2．令<em>f</em> ′(<em>x</em>)＝0，得<em>x</em>＝ln 2．

当*x*<ln 2时，*f* ′(*x*)<0，故函数*f* (*x*)在区间(－∞，ln 2)上单调递减；

当*x*>ln 2时，*f* ′(*x*)>0，故函数*f* (*x*)在区间(ln 2，＋∞)上单调递增．

所以*f* (*x*)的单调递减区间是(－∞，ln 2)，单调递增区间是(ln 2，＋∞)，

<em>f</em> (<em>x</em>)在<em>x</em>＝ln 2处取得极小值<em>f</em> (ln 2)＝e<sup>ln 2</sup>－2ln 2＋2<em>a</em>＝2－2ln 2＋2<em>a</em>，无极大值．

(2)证明：要证当<em>a</em>&gt;ln 2－1且<em>x</em>&gt;0时，e<em><sup>x</sup></em>&gt;<em>x</em><sup>2</sup>－2<em>ax</em>＋1，即证当<em>a</em>&gt;ln 2－1且<em>x</em>&gt;0时，e<em><sup>x</sup></em>－<em>x</em><sup>2</sup>＋2<em>ax</em>－1&gt;0．

设<em>g</em>(<em>x</em>)＝e<em><sup>x</sup></em>－<em>x</em><sup>2</sup>＋2<em>ax</em>－1(<em>x</em>≥0)．则<em>g</em>′(<em>x</em>)＝e<em><sup>x</sup></em>－2<em>x</em>＋2<em>a</em>，

由(1)知<em>g</em>′(<em>x</em>)<sub>min</sub>＝<em>g</em>′(ln 2)＝2－2ln 2＋2<em>a</em>．又<em>a</em>&gt;ln 2－1，则<em>g</em>′(<em>x</em>)<sub>min</sub>&gt;0．

于是对∀<em>x</em>∈<strong>R</strong>，都有<em>g</em>′(<em>x</em>)&gt;0，所以<em>g</em>(<em>x</em>)在<strong>R</strong>上单调递增．

于是对∀<em>x</em>&gt;0，都有<em>g</em>(<em>x</em>)&gt;<em>g</em>(0)＝0．即e<em><sup>x</sup></em>－<em>x</em><sup>2</sup>＋2<em>ax</em>－1&gt;0，故e<em><sup>x</sup></em>&gt;<em>x</em><sup>2</sup>－2<em>ax</em>＋1．

<strong>[例3]</strong>　设函数<em>f</em>(<em>x</em>)＝e<sup>2</sup><em><sup>x</sup></em>－<em>a</em>ln <em>x</em>．

(1)讨论*f*(*x*)的导函数*f*′(*x*)零点的个数；

(2)证明：当*a*>0时，*f*(*x*)≥2*a*＋*a*ln．

<strong>解析</strong>　(1)<em>f</em>(<em>x</em>)的定义域为(0，＋∞)，<em>f</em>′(<em>x</em>)＝2e<sup>2</sup><em><sup>x</sup></em>－(<em>x</em>&gt;0)．

当<em>a</em>≤0时，<em>f</em>′(<em>x</em>)&gt;0，<em>f</em>′(<em>x</em>)没有零点；当<em>a</em>&gt;0时，设<em>u</em>(<em>x</em>)＝e<sup>2</sup><em><sup>x</sup></em>，<em>v</em>(<em>x</em>)＝－，

因为<em>u</em>(<em>x</em>)＝e<sup>2</sup><em><sup>x</sup></em>在(0，＋∞)上单调递增，<em>v</em>(<em>x</em>)＝－

在(0，＋∞)上单调递增，所以*f*′(*x*)在(0，＋∞)上单调递增．

又当*x*→0时，*f*′(*x*) →－∞，当*x*→＋∞时．*f*′(*x*)→＋∞．

故当*a*>0时，*f*′(*x*)存在唯一零点．

(2)由(1)，可设<em>f</em>′(<em>x</em>)在(0，＋∞)上的唯一零点为<em>x</em><sub>0</sub>，当<em>x</em>∈(0，<em>x</em><sub>0</sub>)时，<em>f</em>′(<em>x</em>)&lt;0；

当<em>x</em>∈(<em>x</em><sub>0</sub>，＋∞)时，<em>f</em>′(<em>x</em>)&gt;0．故<em>f</em>(<em>x</em>)在(0，<em>x</em><sub>0</sub>)上单调递减，在(<em>x</em><sub>0</sub>，＋∞)上单调递增，

所以当<em>x</em>＝<em>x</em><sub>0</sub>时，<em>f</em>(<em>x</em>)取得最小值，最小值为<em>f</em>(<em>x</em><sub>0</sub>)．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

由于－＝0，所以<em>f</em>(<em>x</em><sub>0</sub>)＝－<em>a</em>ln <em>x</em><sub>0</sub>＝＋2<em>ax</em><sub>0</sub>－2<em>ax</em><sub>0</sub>－<em>a</em>ln <em>x</em><sub>0</sub>＝＋2<em>ax</em><sub>0</sub>＋<em>a</em>ln≥2<em>a</em>＋<em>a</em>ln．

当且仅当<em>x</em><sub>0</sub>＝时，取等号．故当<em>a</em>&gt;0时，<em>f</em>(<em>x</em>)≥2<em>a</em>＋<em>a</em>ln．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

**[例4]**　已知函数，（为自然对数的底数）．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

(1)当时，求曲线在点处的切线方程；

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

(2)证明：当时，不等式成立．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

**解析**　(1)由题意知，当时，，解得，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

又，，即曲线在点处的切线方程为．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

(2)证明：当时，得，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

要证明不等式成立，即证成立，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

即证成立，即证成立，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

令，，易知，，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/a122932c15d2036a7fd89a605e89499624b44f6dbd139bf379b9367ed627b95c.png)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

由，知在上单调递增，上单调递减，，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

所以成立，即原不等式成立．

【**对点精练**】

1．已知函数<em>f</em>(<em>x</em>)＝(<em>x</em>＋<em>b</em>)(e<em><sup>x</sup></em>－<em>a</em>)(<em>b</em>&gt;0)，在(－1，<em>f</em>(－1))处的切线方程为(e－1)<em>x</em>＋e<em>y</em>＋e－1＝0．

(1)求*a*，*b*；

(2)若<em>m</em>≤0，证明：<em>f</em>(<em>x</em>)≥<em>mx</em><sup>2</sup>＋<em>x</em>．

1．解析　(1)<em>f</em>′(<em>x</em>)＝(<em>x</em>＋<em>b</em>＋1)e<em><sup>x</sup></em>－<em>a</em>，由于切线(e－1)<em>x</em>＋e<em>y</em>＋e－1＝0的斜率为－1，图象过点(－1，0)，

所以解得

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

(2)由(1)可知，，由，可得，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

令，则，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

当时，，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

当时，设，则，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

故函数在上单调递增，又，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

所以当时，，当时，，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

所以函数在区间上单调递减，在区间上单调递增，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

故，即．故．

2．已知*f*(*x*)＝ln *x*－*x*＋*a*＋1．

(1)若存在*x*∈(0，＋∞)，使得*f*(*x*)≥0成立，求实数*a*的取值范围；

(2)求证：当<em>x</em>＞1时，在(1)的条件下，<em>x</em><sup>2</sup>＋<em>ax</em>－<em>a</em>＞<em>x</em>ln<em>x</em>＋成立．

2．<strong>解析</strong>　<em>f</em>(<em>x</em>)＝ln <em>x</em>－<em>x</em>＋<em>a</em>＋1(<em>x</em>＞0)．

(1)原题即为存在*x*∈(0，＋∞)，使得ln *x*－*x*＋*a*＋1≥0，所以*a*≥－ln *x*＋*x*－1，

令*g*(*x*)＝－ln *x*＋*x*－1，则*g*′(*x*)＝－＋1＝．令*g*′(*x*)＝0，解得*x*＝1．

因为当0＜*x*＜1时，*g*′(*x*)＜0，所以*g*(*x*)为减函数，当*x*＞1时，*g*′(*x*)＞0，所以*g*(*x*)为增函数，

所以<em>g</em>(<em>x</em>)<sub>min</sub>＝<em>g</em>(1)＝0，所以<em>a</em>≥<em>g</em>(1)＝0．所以<em>a</em>的取值范围为[0，＋∞)．

(2)证明：原不等式可化为<em>x</em><sup>2</sup>＋<em>ax</em>－<em>x</em>ln <em>x</em>－<em>a</em>－＞0(<em>x</em>＞1，<em>a</em>≥0)．

令<em>G</em>(<em>x</em>)＝<em>x</em><sup>2</sup>＋<em>ax</em>－<em>x</em>ln <em>x</em>－<em>a</em>－，则<em>G</em>(1)＝0．由(1)可知<em>x</em>－ln <em>x</em>－1＞0，

则*G*′(*x*)＝*x*＋*a*－ln *x*－1≥*x*－ln *x*－1＞0，所以*G*(*x*)在(1，＋∞)上单调递增．

所以当<em>x</em>＞1时，<em>G</em>(<em>x</em>)＞<em>G</em>(1)＝0．所以当<em>x</em>＞1时，<em>x</em><sup>2</sup>＋<em>ax</em>－<em>x</em>ln <em>x</em>－<em>a</em>－＞0成立，

即当<em>x</em>＞1时，<em>x</em><sup>2</sup>＋<em>ax</em>－<em>a</em>＞<em>x</em>ln <em>x</em>＋成立．

3．(2017·全国Ⅲ)已知函数<em>f</em>(<em>x</em>)＝ln <em>x</em>＋<em>ax</em><sup>2</sup>＋(2<em>a</em>＋1)<em>x</em>．

(1)讨论*f*(*x*)的单调性；

(2)当*a*<0时，证明*f*(*x*)≤－－2．

3．<strong>解析</strong>　(1)<em>f</em>(<em>x</em>)的定义域为(0，＋∞)，<em>f</em>′(<em>x</em>)＝＋2<em>ax</em>＋2<em>a</em>＋1＝．

若*a*≥0，则当*x*∈(0，＋∞)时，*f*′(*x*)>0，故*f*(*x*)在(0，＋∞)上单调递增．

若*a*<0，则当*x*∈时，*f*′(*x*)>0；当*x*∈时，*f*′(*x*)<0．

故*f*(*x*)在上单调递增，在上单调递减．

综上，当*a*≥0，*f*(*x*)在(0，＋∞)上单调递增；当*a*<0时，*f*(*x*)在上单调递增，在上单调递减．

(2)证明　由(1)知，当*a*<0时，*f*(*x*)在*x*＝－处取得最大值，最大值为*f* ＝ln－1－，

所以*f*(*x*)≤－－2等价于ln－1－≤－－2，即ln＋＋1≤0．

设*g*(*x*)＝ln *x*－*x*＋1(*x*>0)，则*g*′(*x*)＝－1．

当*x*∈(0，1)时，*g*′(*x*)>0；当*x*∈(1，＋∞)时，*g*′(*x*)<0．

所以*g*(*x*)在(0，1)上单调递增，在(1，＋∞)上单调递减．

故当*x*＝1时，*g*(*x*)取得最大值，最大值为*g*(1)＝0．所以当*x*>0时，*g*(*x*)≤0．

从而当*a*<0时，ln＋＋1≤0，即*f*(*x*)≤－－2．

4．已知函数<em>f</em>(<em>x</em>)＝e<em><sup>x</sup></em><sup>＋</sup><em><sup>m</sup></em>－<em>x</em><sup>3</sup>，<em>g</em>(<em>x</em>)＝ln(<em>x</em>＋1)＋2．

(1)若曲线*y*＝*f*(*x*)在点(0，*f*(0))处的切线斜率为1，求实数*m*的值；

(2)当<em>m</em>≥1时，证明：<em>f</em>(<em>x</em>)＞<em>g</em>(<em>x</em>)－<em>x</em><sup>3</sup>．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

4．**解析**　(1)因为，所以

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

因为曲线在点处的切线斜率为，所以，解得

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

(2)因为，，所以等价于．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

当时，．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

要证，只需证明

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

以下给出两种思路证明**．**

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

思路1(隐零点法)：设，则．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

设，则，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

所以函数在上单调递增．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

因为，，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

所以函数在上有唯一零点，且．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

因为，所以，即．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

当时，；当时，，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

所以当时，取得最小值．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

所以．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

综上可知，当时，．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

思路2(切线放缩法)：先证明，设，则．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

因为当时，，当时，，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

所以当时，函数单调递减，当时，函数单调递增．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

所以．所以（当且仅当时取等号）

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

所以要证明，只需证明

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

下面证明．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

设，则**．** 当时，，当时，，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

所以当时，函数单调递减，当时，函数单调递增．所以．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

所以（当且仅当时取等号）**．** 由于取等号的条件不同，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

所以．综上可知，当时，．

5．已知函数<em>f</em>(<em>x</em>)＝e<em><sup>x</sup></em><sup>＋</sup><em><sup>a</sup></em>－ln<em>x</em>(其中e＝2.718 28…，是自然对数的底数)．

(1)当*a*＝0时，求函数*f*(*x*)的图象在(1，*f*(1))处的切线方程；

(2)求证：当*a*>1－时，*f*(*x*)>e＋1．

5．解析　(1)∵<em>a</em>＝0时，∴<em>f</em>(<em>x</em>)＝e<em><sup>x</sup></em>－ln <em>x</em>，<em>f</em>′(<em>x</em>)＝e<em><sup>x</sup></em>－(<em>x</em>&gt;0)，∴<em>f</em>(1)＝e，<em>f</em>′(1)＝e－1，

∴函数*f*(*x*)的图象在(1，*f*(1))处的切线方程为：*y*－e＝(e－1)(*x*－1)，即(e－1)*x*－*y*＋1＝0.

(2)∵<em>f</em>′(<em>x</em>)＝e<em><sup>x</sup></em><sup>＋</sup><em><sup>a</sup></em>－(<em>x</em>&gt;0)，设<em>g</em>(<em>x</em>)＝<em>f</em>′(<em>x</em>)，则<em>g</em>′(<em>x</em>)＝e<em><sup>x</sup></em><sup>＋</sup><em><sup>a</sup></em>＋&gt;0，∴<em>g</em>(<em>x</em>)是增函数，

∵e<em><sup>x</sup></em><sup>＋</sup><em><sup>a</sup></em>&gt;e<em><sup>a</sup></em>，∴由e<em><sup>a</sup></em>&gt;<em>x</em>&gt;e<sup>－</sup><em><sup>a</sup></em>，∴当<em>x</em>&gt;e<sup>－</sup><em><sup>a</sup></em>时，<em>f</em>′(<em>x</em>)&gt;0；

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

若0&lt;<em>x</em>&lt;1e<em><sup>x</sup></em><sup>＋</sup><em><sup>a</sup></em>&lt;e<em><sup>a</sup></em><sup>＋1</sup>，由e<em><sup>a</sup></em><sup>＋1</sup>&lt;<em>x</em>&lt;e<sup>－</sup><em><sup>a</sup></em><sup>－1</sup>，∴当0&lt;<em>x</em>&lt;min{1，e<sup>－</sup><em><sup>a</sup></em><sup>－1</sup>}时，<em>f</em>′(<em>x</em>)&lt;0，

故<em>f</em>′(<em>x</em>)＝0仅有一解，记为<em>x</em><sub>0</sub>，则当0&lt;<em>x</em>&lt;<em>x</em><sub>0</sub>时，<em>f</em>′(<em>x</em>)&lt;0，<em>f</em>(<em>x</em>)递减；当<em>x</em>&gt;<em>x</em><sub>0</sub>时，<em>f</em>′(<em>x</em>)&gt;0，<em>f</em>(<em>x</em>)递增；

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

∴<em>f</em>(<em>x</em>)<sub>min</sub>＝<em>f</em>(<em>x</em><sub>0</sub>)＝e<em><sup>x</sup></em><sup>0＋</sup><em><sup>a</sup></em>－ln <em>x</em><sub>0</sub>，而<em>f</em>′(<em>x</em><sub>0</sub>)＝e<em><sup>x</sup></em><sub>0</sub><sup>＋</sup><em><sup>a</sup></em>－＝0e<em><sup>x</sup></em><sup>0＋</sup><em><sup>a</sup></em>＝<em>a</em>＝－ln <em>x</em><sub>0</sub>－<em>x</em><sub>0</sub>，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

记<em>h</em>(<em>x</em>)＝ln <em>x</em>＋<em>x</em>，则<em>f</em>(<em>x</em><sub>0</sub>)＝－ln <em>x</em><sub>0</sub>＝<em>h</em>，<em>a</em>&gt;1－－<em>a</em>&lt;－1<em>h</em>(<em>x</em><sub>0</sub>)&lt;<em>h</em>，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

而<em>h</em>(<em>x</em>)显然是增函数，∴0&lt;<em>x</em><sub>0</sub>&lt;&gt;e，∴<em>h</em>&gt;<em>h</em>(e)＝e＋1．综上，当<em>a</em>&gt;1－时，<em>f</em>(<em>x</em>)&gt;e＋1．

6．已知函数*f*(*x*)＝*ax*－ln *x*．

(1)讨论*f*(*x*)的单调性；

(2)若<em>a</em>∈，求证：<em>f</em>(<em>x</em>)≥2<em>ax</em>－<em>x</em>e<em><sup>ax</sup></em><sup>－1</sup>．

6．<strong>解析</strong>　(1)由题意得<em>f</em>′(<em>x</em>)＝<em>a</em>－＝(<em>x</em>&gt;0)，

①当*a*≤0时，则*f*′(*x*)<0在(0，＋∞)上恒成立，∴*f*(*x*)在(0，＋∞)上单调递减．

②当*a*>0时，则当*x*∈时，*f*′(*x*)>0，*f*(*x*)单调递增，当*x*∈时，*f*′(*x*)<0，*f*(*x*)单调递减．

综上当*a*≤0时，*f*(*x*)在(0，＋∞)上单调递减；当*a*>0时，*f*(*x*)在上单调递减，在上单调递增．

(2)令<em>g</em>(<em>x</em>)＝<em>f</em>(<em>x</em>)－2<em>ax</em>＋<em>x</em>e<em><sup>ax</sup></em><sup>－1</sup>＝<em>x</em>e<em><sup>ax</sup></em><sup>－1</sup>－<em>ax</em>－ln <em>x</em>，

则<em>g</em>′(<em>x</em>)＝e<em><sup>ax</sup></em><sup>－1</sup>＋<em>ax</em>e<em><sup>ax</sup></em><sup>－1</sup>－<em>a</em>－＝(<em>ax</em>＋1)＝(<em>x</em>&gt;0)，

设<em>r</em>(<em>x</em>)＝<em>x</em>e<em><sup>ax</sup></em><sup>－1</sup>－1(<em>x</em>&gt;0)，则<em>r</em>′(<em>x</em>)＝(1＋<em>ax</em>)e<em><sup>ax</sup></em><sup>－1</sup>(<em>x</em>&gt;0)，

∵e<em><sup>ax</sup></em><sup>－1</sup>&gt;0，∴当<em>x</em>∈时，<em>r</em>′(<em>x</em>)&gt;0，<em>r</em>(<em>x</em>)单调递增；当<em>x</em>∈时，<em>r</em>′(<em>x</em>)&lt;0，<em>r</em>(<em>x</em>)单调递减．

∴<em>r</em>(<em>x</em>)<sub>max</sub>＝<em>r</em>＝－≤0，

∴当0<*x*<－时，*g*′(*x*)<0，当*x*>－时，*g*′(*x*)>0，

∴<em>g</em>(<em>x</em>)在上单调递减，在上单调递增，∴<em>g</em>(<em>x</em>)<sub>min</sub>＝<em>g</em>，

设<em>t</em>＝－∈，则<em>g</em>＝<em>h</em>(<em>t</em>)＝－ln <em>t</em>＋1(0&lt;<em>t</em>≤e<sup>2</sup>)，<em>h</em>′(<em>t</em>)＝－≤0，<em>h</em>(<em>t</em>)在上单调递减，

∴<em>h</em>(<em>t</em>)≥<em>h</em>(e<sup>2</sup>)＝0；∴<em>g</em>(<em>x</em>)≥0，故<em>f</em>(<em>x</em>)≥2<em>ax</em>－<em>x</em>e<em><sup>ax</sup></em><sup>－1</sup>.

