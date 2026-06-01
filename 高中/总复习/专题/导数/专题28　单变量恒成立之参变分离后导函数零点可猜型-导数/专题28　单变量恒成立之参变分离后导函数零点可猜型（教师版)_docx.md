专题28　单变量恒成立之参变分离后导函数零点可猜型

![](images/079027907cac2fda5a0f42e1c3bcdbef82c57c6ca12f121a2a8cb41732a7f259.jpg)

【方法总结】

单变量恒成立之参变分离法

参变分离法是将不等式变形成一个一端是<em>f</em>(<em>a</em>)，另一端是变量表达式<em>g</em>(<em>x</em>)的不等式后，若<em>f</em>(<em>a</em>)≥<em>g</em>(<em>x</em>)在<em>x</em>∈<em>D</em>上恒成立，则<em>f</em>(<em>a</em>)≥<em>g</em>(<em>x</em>)<sub>max</sub>；若<em>f</em>(<em>a</em>)≤<em>g</em>(<em>x</em>)在<em>x</em>∈<em>D</em>上恒成立，则<em>f</em>(<em>a</em>)≤<em>g</em>(<em>x</em>)<sub>min</sub>．特别地，经常将不等式变形成一个一端是参数<em>a</em>，另一端是变量表达式<em>g</em>(<em>x</em>)的不等式后，若<em>a</em>≥<em>g</em>(<em>x</em>)在<em>x</em>∈<em>D</em>上恒成立，则<em>a</em>≥<em>g</em>(<em>x</em>)<sub>max</sub>；若<em>a</em>≤<em>g</em>(<em>x</em>)在<em>x</em>∈<em>D</em>上恒成立，则<em>a</em>≤<em>g</em>(<em>x</em>)<sub>min</sub>．
利用分离参数法来确定不等式*f*(*x*，*a*)≥0(*x*∈*D*，*a*为实参数)恒成立问题中参数取值范围的基本步骤：  
（1）将参数与变量分离，化为<em>f</em><sub>1</sub>(<em>a</em>)≥<em>f</em><sub>2</sub>(<em>x</em>)或<em>f</em><sub>1</sub>(<em>a</em>)≤<em>f</em><sub>2</sub>(<em>x</em>)的形式．  
（2）求<em>f</em><sub>2</sub>(<em>x</em>)在<em>x</em>∈<em>D</em>时的最大值或最小值．  
（3）解不等式<em>f</em><sub>1</sub>(<em>a</em>)≥<em>f</em><sub>2</sub>(<em>x</em>)<sub>max</sub>或<em>f</em><sub>1</sub>(<em>a</em>)≤<em>f</em><sub>2</sub>(<em>x</em>)<sub>min</sub>，得到<em>a</em>的取值范围．

【例题选讲】

<strong>[例1]</strong>　已知函数<em>f</em>(<em>x</em>)＝e<em>x</em>－<em>x</em>ln<em>x</em>，<em>g</em>(<em>x</em>)＝e<em><sup>x</sup></em>－<em>tx</em><sup>2</sup>＋<em>x</em>，<em>t</em>∈<strong>R</strong>，其中e为自然对数的底数．  
（1）求函数*f*(*x*)的图象在点(1，*f*（1）)处的切线方程；  
（2）若*g*(*x*)≥*f*(*x*)对任意的*x*∈(0，＋∞)恒成立，求*t*的取值范围．

<strong>解析</strong>　（1）由<em>f</em>(<em>x</em>)＝e<em>x</em>－<em>x</em>ln <em>x</em>，知<em>f</em>′(<em>x</em>)＝e－ln <em>x</em>－1，则<em>f</em>′（1）＝e－1，而<em>f</em>（1）＝e，
则所求切线方程为*y*－e＝(e－1)(*x*－1)，即*y*＝(e－1)*x*＋1．  
（2）∵<em>f</em>(<em>x</em>)＝e<em>x</em>－<em>x</em>ln <em>x</em>，<em>g</em>(<em>x</em>)＝e<em><sup>x</sup></em>－<em>tx</em><sup>2</sup>＋<em>x</em>，<em>t</em>∈<strong>R</strong>，
∴<em>g</em>(<em>x</em>)≥<em>f</em>(<em>x</em>)对任意的<em>x</em>∈(0，＋∞)恒成立等价于e<em><sup>x</sup></em>－<em>tx</em><sup>2</sup>＋<em>x</em>－e<em>x</em>＋<em>x</em>ln <em>x</em>≥0对任意的<em>x</em>∈(0，＋∞)恒成立，
即*t*≤对任意的*x*∈(0，＋∞)恒成立．
令*F*(*x*)＝，则*F*′(*x*)＝＝，
令<em>G</em>(<em>x</em>)＝e<em><sup>x</sup></em>＋e－－ln <em>x</em>，
则<em>G</em>′(<em>x</em>)＝e<em><sup>x</sup></em>－－＝＞0对任意的<em>x</em>∈(0，＋∞)恒成立．
∴<em>G</em>(<em>x</em>)＝e<em><sup>x</sup></em>＋e－－ln <em>x</em>在(0，＋∞)上单调递增，且<em>G</em>（1）＝0，
∴当*x*∈(0，1)时，*G*(*x*)＜0，当*x*∈(1，＋∞)时，*G*(*x*)＞0，
即当*x*∈(0，1)时，*F*′(*x*)＜0，当*x*∈(1，＋∞)时，*F*′(*x*)＞0，
∴*F*(*x*)在(0，1)上单调递减，在(1，＋∞)上单调递增，∴*F*(*x*)≥*F*（1）＝1，∴*t*≤1，
即*t*的取值范围是(－∞，1]．

<strong>[例2]</strong>　已知函数<em>f</em>(<em>x</em>)＝(<em>x</em>－2)e<em><sup>x</sup></em>－<em>ax</em><sup>2</sup>＋<em>ax</em>(<em>a</em>∈<strong>R</strong>)．  
（1）当*a*＝0时，求曲线*y*＝*f*(*x*)在点(0，*f*（0）)处的切线方程；  
（2）当*x*≥2时，*f*(*x*)≥0恒成立，求*a*的取值范围．
解析　（1）当<em>a</em>＝0时，<em>f</em>(<em>x</em>)＝(<em>x</em>－2)e<em><sup>x</sup></em>，<em>f</em>（0）＝(0－2)e<sup>0</sup>＝－2，

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

【对点精练】

1．已知函数<em>f</em>(<em>x</em>)＝(<em>a</em>∈<strong>R</strong>)．  
（1）讨论*f*(*x*)的单调区间；  
（2）若<em>f</em>(<em>x</em>)≤e<em><sup>x</sup></em><sup>－1</sup>＋－1恒成立，求实数<em>a</em>的取值范围．

1．解析　（1）*f*(*x*)的定义域为(0，＋∞)，且*f*′(*x*)＝．
令<em>f</em>′(<em>x</em>)&gt;0，得1－<em>a</em>－ln <em>x</em>&gt;0，解得0&lt;<em>x</em>&lt;e<sup>1－</sup><em><sup>a</sup></em>．
令<em>f</em>′(<em>x</em>)&lt;0，得1－<em>a</em>－ln <em>x</em>&lt;0，解得<em>x</em>&gt;e<sup>1－</sup><em><sup>a</sup></em>．
故<em>f</em>(<em>x</em>)的单调递增区间为(0，e<sup>1－</sup><em><sup>a</sup></em>)，单调递减区间为(e<sup>1－</sup><em><sup>a</sup></em>，＋∞)．  
（2）因为<em>f</em>(<em>x</em>)≤e<em><sup>x</sup></em><sup>－1</sup>＋－1恒成立，即≤e<em><sup>x</sup></em><sup>－1</sup>＋－1对(0，＋∞)恒成立，
所以<em>a</em>≤<em>x</em>e<em><sup>x</sup></em><sup>－1</sup>－<em>x</em>－ln <em>x</em>＋1对(0，＋∞)恒成立，
令<em>g</em>(<em>x</em>)＝<em>x</em>e<em><sup>x</sup></em><sup>－1</sup>－<em>x</em>－ln <em>x</em>＋1，则<em>g</em>′(<em>x</em>)＝e<em><sup>x</sup></em><sup>－1</sup>＋<em>x</em>e<em><sup>x</sup></em><sup>－1</sup>－1－＝(<em>x</em>＋1)．
当*x*∈(0，1)时，*g*′(*x*)<0，所以*g*(*x*)在(0，1)上单调递减．
当*x*∈(1，＋∞)时，*g*′(*x*)>0，所以*g*(*x*)在(1，＋∞)上单调递增．
故当*x*＝1时，*g*(*x*)取到最小值*g*（1）＝1，所以*a*≤1．
故实数*a*的取值范围是(－∞，1]．

2．函数<em>f</em>(<em>x</em>)＝ln<em>x</em>＋<em>x</em><sup>2</sup>＋<em>ax</em>(<em>a</em>∈<strong>R</strong>)，<em>g</em>(<em>x</em>)＝e<em><sup>x</sup></em>＋<em>x</em><sup>2</sup>．  
（1）讨论*f*(*x*)的极值点的个数；  
（2）若对于任意*x*∈(0，＋∞)，总有*f*(*x*)≤*g*(*x*)成立，求实数*a*的取值范围．

2．解析：（1）由题意得<em>f</em>′(<em>x</em>)＝＋<em>x</em>＋<em>a</em>＝(<em>x</em>&gt;0)，令<em>f</em>′(<em>x</em>)＝0，即<em>x</em><sup>2</sup>＋<em>ax</em>＋1＝0，<em>Δ</em>＝<em>a</em><sup>2</sup>－4．

①当<em>Δ</em>＝<em>a</em><sup>2</sup>－4≤0，即－2≤<em>a</em>≤2时，<em>x</em><sup>2</sup>＋<em>ax</em>＋1≥0对<em>x</em>&gt;0恒成立，
即*f*′(*x*)＝≥0对*x*>0恒成立，此时*f*(*x*)没有极值点．

②当<em>Δ</em>＝<em>a</em><sup>2</sup>－4&gt;0，即<em>a</em>&lt;－2或<em>a</em>&gt;2时，若<em>a</em>&lt;－2，设方程<em>x</em><sup>2</sup>＋<em>ax</em>＋1＝0的两个不同实根为<em>x</em><sub>1</sub>，<em>x</em><sub>2</sub>，
不妨设<em>x</em><sub>1</sub>&lt;<em>x</em><sub>2</sub>，则<em>x</em><sub>1</sub>＋<em>x</em><sub>2</sub>＝－<em>a</em>&gt;0，<em>x</em><sub>1</sub><em>x</em><sub>2</sub>＝1&gt;0，故<em>x</em><sub>2</sub>&gt;<em>x</em><sub>1</sub>&gt;0，
∴当0&lt;<em>x</em>&lt;<em>x</em><sub>1</sub>或<em>x</em>&gt;<em>x</em><sub>2</sub>时，<em>f</em>′(<em>x</em>)&gt;0；当<em>x</em><sub>1</sub>&lt;<em>x</em>&lt;<em>x</em><sub>2</sub>时<em>f</em>′(<em>x</em>)&lt;0，故<em>x</em><sub>1</sub>，<em>x</em><sub>2</sub>是函数<em>f</em>(<em>x</em>)的两个极值点．
若<em>a</em>&gt;2，设方程<em>x</em><sup>2</sup>＋<em>ax</em>＋1＝0的两个不同实根为<em>x</em><sub>3</sub>，<em>x</em><sub>4</sub>，
则<em>x</em><sub>3</sub>＋<em>x</em><sub>4</sub>＝－<em>a</em>&lt;0，<em>x</em><sub>3</sub><em>x</em><sub>4</sub>＝1&gt;0，故<em>x</em><sub>3</sub>&lt;0，<em>x</em><sub>4</sub>&lt;0，∴当<em>x</em>&gt;0时，<em>f</em>′(<em>x</em>)&gt;0，故函数<em>f</em>(<em>x</em>)没有极值点．

综上，当*a*<－2时，函数*f*(*x*)有两个极值点；当*a*≥－2时，函数*f*(*x*)没有极值点．  
（2）<em>f</em>(<em>x</em>)≤<em>g</em>(<em>x</em>)⇔e<em><sup>x</sup></em>－ln <em>x</em>＋<em>x</em><sup>2</sup>≥<em>ax</em>，因为<em>x</em>&gt;0，所以<em>a</em>≤对于∀<em>x</em>&gt;0恒成立，
设*φ*(*x*)＝(*x*>0)，*φ*′(*x*)＝＝，
∵*x*>0，∴当*x*∈(0，1)时，*φ*′(*x*)<0，*φ*(*x*)单调递减，当*x*∈(1，＋∞)时，*φ*′(*x*)>0，*φ*(*x*)单调递增，
∴*φ*(*x*)≥*φ*（1）＝e＋1，∴*a*≤e＋1，即实数*a*的取值范围是(－∞，e＋1]．

3．设函数*f*(*x*)＝ln*x*＋(*a*为常数)．  
（1）讨论函数*f*(*x*)的单调性；  
（2）不等式*f*(*x*)≥1在*x*∈(0，1]上恒成立，求实数*a*的取值范围．

3．解析　（1）*f*(*x*)的定义域为(0，＋∞)，*f*′(*x*)＝－＋＝，
当*a*≤0时，又*x*>0，∴*x*－*a*>0，∴*f*′(*x*)>0，∴*f*(*x*)在定义域(0，＋∞)上单调递增；
当*a*>0时，若*x*>*a*，则*f*′(*x*)>0，∴*f*(*x*)单调递增；
若0<*x*<*a*，则*f*′(*x*)<0，∴*f*(*x*)单调递减．

综上可知，当*a*≤0时，*f*(*x*)在(0，＋∞)上单调递增；当*a*>0时，*f*(*x*)在区间(0，*a*)上单调递减，在区间(*a*，＋∞)上单调递增．  
（2）*f*(*x*)≥1⇔＋ln*x*≥1⇔≥－ln *x*＋1⇔*a*≥－*x*ln *x*＋*x*对任意*x*∈(0，1]恒成立．
令*g*(*x*)＝－*x*ln *x*＋*x*，*x*∈(0，1]．则*g*′(*x*)＝－ln *x*－*x*·＋1＝－ln *x*≥0，*x*∈(0，1]，
∴<em>g</em>(<em>x</em>)在(0，1]上单调递增，∴<em>g</em>(<em>x</em>)<sub>max</sub>＝<em>g</em>（1）＝1，∴<em>a</em>≥1，故<em>a</em>的取值范围为[1，＋∞)．

4．已知函数*f*(*x*)＝．  
（1）若函数*f*(*x*)在区间上存在极值，求正实数*a*的取值范围；  
（2）当*x*≥1时，不等式*f*(*x*)≥恒成立，求实数*k*的取值范围．

4．<strong>解析</strong>　（1）函数<em>f</em>(<em>x</em>)的定义域为(0，＋∞)，<em>f</em>′(<em>x</em>)＝＝－，令<em>f</em>′(<em>x</em>)＝0，得<em>x</em>＝1．
当*x*∈(0，1)时，*f*′(*x*)＞0，*f*(*x*)单调递增；当*x*∈(1，＋∞)时，*f*′(*x*)＜0，*f*(*x*)单调递减．
所以*x*＝1为函数*f*(*x*)的极大值点，且是唯一的极值点，所以0＜*a*＜1＜*a*＋，故＜*a*＜1，
即实数*a*的取值范围为．  
（2）由题意得，当*x*≥1时，*k*≤恒成立，
令*g*(*x*)＝(*x*≥1)，则*g*′(*x*)＝＝．
再令*h*(*x*)＝*x*－ln *x*(*x*≥1)，则*h*′(*x*)＝1－≥0，所以*h*(*x*)≥*h*（1）＝1，所以*g*′(*x*)＞0，
所以*g*(*x*)在[1，＋∞)上单调递增，所以*g*(*x*)≥*g*（1）＝2，
故*k*≤2，即实数*k*的取值范围是(－∞，2]．

