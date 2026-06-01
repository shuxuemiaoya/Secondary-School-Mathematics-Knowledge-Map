专题21　双变量不含参不等式证明方法之换元法

![](images/e871ec06bb64e48c9d008d21695c66d880433a14db0c12ba03c0c1f59236692e.jpg)

【方法总结】

双变量不等式的证明是导数综合题的一个难点，其困难之处是如何消元，构造合适的一元函数．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

整体换元法：若两个变量存在确定的关系，可以利用其中一个变量替换另一个变量，直接消元，将两个变量转化为一个变量．若两个变量不存在确定的关系，有时可以将两个变量之间的关系看成一个整体（比如，，，)等策略将两个变量划归为一个变量整体换元，化为一元不等式．

<strong>[例1]</strong>　已知函数<em>f</em>(<em>x</em>)＝<em>ax</em><sup>2</sup>＋<em>x</em>ln<em>x</em>(<em>a</em>∈<strong>R</strong>)的图象在点(1，<em>f</em>（1）)处的切线与直线<em>x</em>＋3<em>y</em>＝0垂直．  
（1）求实数*a*的值；  
（2）求证：当*n*＞*m*＞0时，ln*n*－ln*m*＞－．

<strong>解析</strong>　（1）因为<em>f</em>(<em>x</em>)＝<em>ax</em><sup>2</sup>＋<em>x</em>ln <em>x</em>，所以<em>f</em>′(<em>x</em>)＝2<em>ax</em>＋ln <em>x</em>＋1，
因为切线与直线*x*＋3*y*＝0垂直，所以切线的斜率为3，所以*f*′（1）＝3，即2*a*＋1＝3，故*a*＝1．  
（2）要证ln*n*－ln*m*＞－，即证ln＞－，只需证ln－＋＞0．
令＝*x*，构造函数*g*(*x*)＝ln *x*－＋*x*(*x*≥1)，则*g*′(*x*)＝＋＋1．
因为*x*∈[1，＋∞)，所以*g*′(*x*)＝＋＋1＞0，故*g*(*x*)在(1，＋∞)上单调递增．
由已知*n*＞*m*＞0，得＞1，所以*g*＞*g*（1）＝0，即证得ln－＋＞0成立，所以命题得证．

总结提升　对“待证不等式”等价变形为“ln－＋＞0”后，观察可知，对“”进行换元，变为“ln*x*－＋*x*＞0”，构造函数“*g*(*x*)＝ln *x*－＋*x*(*x*≥1)”来证明不等式，可简化证明过程中的运算．

<strong>[例2]</strong>　已知函数<em>f</em>(<em>x</em>)＝ln<em>x</em>－，<em>g</em>(<em>x</em>)＝<em>x</em>ln<em>x</em>－<em>m</em>(<em>x</em><sup>2</sup>－1)(<em>m</em>∈<strong>R</strong>)．  
（1）若函数*f*(*x*)，*g*(*x*)在区间(0，1)上均单调且单调性相反，求实数*m*的取值范围；  
（2）若0＜*a*＜*b*，证明：＜＜．

<strong>解析</strong>　（1）<em>f</em>′(<em>x</em>)＝－＝＞0，所以<em>f</em>(<em>x</em>)在(0，1)上单调递增．
由已知*f*(*x*)，*g*(*x*)在(0，1)上均单调且单调性相反，得*g*(*x*)在(0，1)上单调递减．
所以*g*′(*x*)＝ln *x*＋1－2*mx*≤0在(0，1)上恒成立，即2*m*≥，
令*φ*(*x*)＝(*x*∈(0，1))，*φ*′(*x*)＝＞0，所以*φ*(*x*)在(0，1)上单调递增，*φ*(*x*)＜*φ*（1）＝1，
所以2*m*≥1，即*m*≥．  
（2）由（1）*f*(*x*)＝ln*x*－在(0，1)上单调递增，*f*(*x*)＝ln *x*－＜*f*（1）＝0，即ln *x*＜，
令*x*＝∈(0，1)得ln＜＝，∵ln＜0，∴＜．
在（1）中，令*m*＝，由*g*(*x*)在(0，1)上均单调递减得*g*(*x*)＞*g*（1）＝0，
所以<em>x</em>ln <em>x</em>－(<em>x</em><sup>2</sup>－1)＞0，即ln <em>x</em>＞，

取*x*＝∈(0，1)得ln＞，即ln *a*－ln *b*＞，
由ln*a*－ln*b*＜0得：＜，综上：＜＜．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

总结提升　两个正数和的对数平均定义：

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

对数平均与算术平均、几何平均的大小关系：（此式记为对数平均不等式）

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

取等条件：当且仅当时，等号成立．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

[例3]　已知，其中图像在处的切线平行于轴．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)  
（1）确定与的关系；
![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)  
（2）设斜率为的直线与的图像交于，求证：．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

思维引导　（2），所证不等式为即，进而可将视为一个整体进行换元，从而转变为证明一元不等式．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
解析　（1），，
![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
依题意可得：．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)  
（2）依题意得，故所证不等式等价于：

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
令，则只需证：．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

先证右边不等式：，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
令，，在单调递减，．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
即．对于左边不等式：．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
令，则，在单调递增，．

总结提升

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)  
（1）在证明不等式时，由于独立取值，无法利用等量关系消去一个变量，所以考虑构造表达式：使得不等式以为研究对象，再利用换元将多元不等式转变为一元不等式．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)  
（2）所证不等式为轮换对称式时，若独立取值，可对定序，从而增加一个可操作的条件．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

[例4]　已知函数．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)  
（1）求的单调区间和极值；
![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)  
（2）设，且，证明：．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

思维引导　所证不等式等价于证，轮换对称式可设，进而对不等式进行变形，在考虑能否换元减少变量．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
解析　（1）定义域为，，令，解得：．
![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
∴的单调增区间是，单调减区间是，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

的极小值为，无极大值．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)  
（2）不妨设，．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

，（由于定序，去分母避免了分类讨论）

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

，（观察两边同时除以，即可构造出关于的不等式）

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
两边同除以得，，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
令，则，即证：．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
令，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
令，，（再次利用整体换元）

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

，在上单调递减，所以．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
即，即恒成立，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
∴在上是减函数，所以．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
∴得证．所以成立．

总结提升

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)  
（1）本题考验不等式的变形，对于不等式而言，观察到每一项具备齐次的特征（不包括对数），所以同除以，结果为或者1，观察对数的真数，其分式也具备分子分母齐次的特点，所以分子分母同除以，结果为或者1，进而就将不等式化为以为核心的不等式．  
（2）本题进行了两次整体换元，第一次减少变量个数，第二次简化了表达式．

【对点训练】

1．已知函数*f*(*x*)＝ln *x*－．  
（1）若函数*f*(*x*)在(0，＋∞)上单调递增，求实数*a*的取值范围；  
（2）设*m*>*n*>0，求证：ln*m*－ln*n*>．

1．<strong>解析</strong>　（1）<em>f</em>′(<em>x</em>)＝－＝＝．
因为*f*(*x*)在(0，＋∞)上单调递增，所以*f*′(*x*)≥0在(0，＋∞)上恒成立，
即<em>x</em><sup>2</sup>＋(2－2<em>a</em>)<em>x</em>＋1≥0在(0，＋∞)上恒成立，所以2<em>a</em>－2≤<em>x</em>＋在(0，＋∞)上恒成立．
因为*x*＋≥2，当且仅当*x*＝1时，等号成立，所以2*a*－2≤2，解得*a*≤2．  
（2）要证ln *m*－ln *n*>，只需证ln>，即证ln－>0．
设*h*(*x*)＝ln *x*－，由（1）可知*h*(*x*)在(0，＋∞)上单调递增，
因为>1，所以*h*>*h*（1）＝0，即ln－>0，所以原不等式成立．

2．已知函数*f*(*x*)＝＋ln *x*在(1，＋∞)上是增函数，且*a*>0．  
（1）求*a*的取值范围；  
（2）若*b*>0，试证明<ln<．

2．<strong>解析</strong>　（1）<em>f</em>′(<em>x</em>)＝－＋＝，因为在(1，＋∞)上<em>f</em>′(<em>x</em>)≥0，且<em>a</em>&gt;0，所以<em>ax</em>－1≥0，即<em>x</em>≥，
所以≤1，即*a*≥1，故*a*的取值范围为[1，＋∞)．  
（2）因为*b*>0，*a*≥1，所以>1，又*f*(*x*)＝＋ln *x*在(1，＋∞)上是增函数，
所以*f*>*f*(l)，即＋ln >0，化简得<ln，

ln<等价于ln－＝ln －<0，
令*g*(*x*)＝ln(1＋*x*)－*x*(*x*∈(0，＋∞))，则*g*′(*x*)＝－1＝<0，所以函数*g*(*x*)在(0，＋∞)上为减函数，
所以*g*＝ln－＝ln－<*g*（0）＝0，即ln<．综上，<ln<．

3．设函数*f*(*x*)＝*x*ln(*ax*)(*a*>0)．  
（1）设<em>F</em>(<em>x</em>)＝<em>f</em>（1）<em>x</em><sup>2</sup>＋<em>f</em>′(<em>x</em>)，讨论函数<em>F</em>(<em>x</em>)的单调性；  
（2）过两点<em>A</em>(<em>x</em><sub>1</sub>，<em>f</em>′(<em>x</em><sub>1</sub>))，<em>B</em>(<em>x</em><sub>2</sub>，<em>f</em>′(<em>x</em><sub>2</sub>))(<em>x</em><sub>1</sub>&lt;<em>x</em><sub>2</sub>)的直线的斜率为<em>k</em>，求证：&lt;<em>k</em>&lt;．

3．<strong>解析</strong>　（1）<em>f</em>′(<em>x</em>)＝ln(<em>ax</em>)＋1，所以<em>F</em>(<em>x</em>)＝(ln <em>a</em>)<em>x</em><sup>2</sup>＋ln(<em>ax</em>)＋1，

函数*F*(*x*)的定义域为(0，＋∞)，*F*′(*x*)＝(ln *a*)*x*＋＝．

①当ln *a*≥0，即*a*≥1时，恒有*F*′(*x*)>0，函数*F*(*x*)在(0，＋∞)上是增函数；
②当ln *a*<0，即0<*a*<1时，
令<em>F</em>′(<em>x</em>)&gt;0，得(ln <em>a</em>)<em>x</em><sup>2</sup>＋1&gt;0，解得0&lt;<em>x</em>&lt;；令<em>F</em>′(<em>x</em>)&lt;0，得(ln <em>a</em>)<em>x</em><sup>2</sup>＋1&lt;0，解得<em>x</em>&gt;．
所以函数*F*(*x*)在上为增函数，在上为减函数．  
（2）因为<em>k</em>＝＝＝，<em>x</em><sub>2</sub>－<em>x</em><sub>1</sub>&gt;0，要证&lt;<em>k</em>&lt;，即证&lt;ln&lt;，
令*t*＝，则*t*>1，则只要证1－<ln *t*<*t*－1即可，

①设*g*(*t*)＝*t*－1－ln *t*，则*g*′(*t*)＝1－>0(*t*>1)，故*g*(*t*)在(1，＋∞)上是增函数．
所以当*t*>1时，*g*(*t*)＝*t*－1－ln *t*>*g*（1）＝0，即*t*－1>ln *t*成立．

②要证1－<ln t，由于*t*>1，即证*t*－1<tln *t*，设*h*(*t*)＝tln *t*－(*t*－1)，则*h*′(*t*)＝ln *t*>0(*t*>1)，
故函数*h*(*t*)在(1，＋∞)上是增函数，所以当*t*>1时，*h*(*t*)＝*t*ln *t*－(*t*－1)>*h*（1）＝0，即 *t*－1<tln *t*成立．
故由①②知<*k*<成立，得证．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

4．已知函数，．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)  
（1）讨论的单调性；
![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)  
（2）当，,为两个不相等的正数，证明：．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

4．解析　（1）函数的定义域为，．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
若，，则在区间内为增函数；
![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
若，令，得．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
则当时，，在区间内为增函数；
![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
当时，，在区间内为减函数．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)  
（2）当时，．不妨设，则原不等式等价于，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
令，则原不等式也等价于即．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

下面证明当时，恒成立．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
设，则，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
故在区间内为增函数，，即，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
所以．

5．已知函数<em>f</em>(<em>x</em>)＝ln <em>x</em>－<em>ax</em><sup>2</sup>＋<em>x</em>，<em>a</em>∈<strong>R</strong>．  
（1）当*a*＝0时，求函数*f*(*x*)的图象在(1，*f*（1）)处的切线方程；  
（2）若<em>a</em>＝－2，正实数<em>x</em><sub>1</sub>，<em>x</em><sub>2</sub>满足<em>f</em>(<em>x</em><sub>1</sub>)＋<em>f</em>(<em>x</em><sub>2</sub>)＋<em>x</em><sub>1</sub><em>x</em><sub>2</sub>＝0，证明：<em>x</em><sub>1</sub>＋<em>x</em><sub>2</sub>≥．

5．<strong>解析</strong>　（1）当<em>a</em>＝0时，<em>f</em>(<em>x</em>)＝ln <em>x</em>＋<em>x</em>，则<em>f</em>（1）＝1，所以切点为(1，1)，
又*f*′(*x*)＝＋1，则切线斜率*k*＝*f*′（1）＝2，故切线方程为*y*－1＝2(*x*－1)，即2*x*－*y*－1＝0．  
（2）当<em>a</em>＝－2时，<em>f</em>(<em>x</em>)＝ln <em>x</em>＋<em>x</em><sup>2</sup>＋<em>x</em>，<em>x</em>&gt;0．由<em>f</em>(<em>x</em><sub>1</sub>)＋<em>f</em>(<em>x</em><sub>2</sub>)＋<em>x</em><sub>1</sub><em>x</em><sub>2</sub>＝0，
得ln <em>x</em><sub>1</sub>＋<em>x</em>＋<em>x</em><sub>1</sub>＋ln <em>x</em><sub>2</sub>＋<em>x</em>＋<em>x</em><sub>2</sub>＋<em>x</em><sub>1</sub><em>x</em><sub>2</sub>＝0，从而(<em>x</em><sub>1</sub>＋<em>x</em><sub>2</sub>)<sup>2</sup>＋(<em>x</em><sub>1</sub>＋<em>x</em><sub>2</sub>)＝<em>x</em><sub>1</sub><em>x</em><sub>2</sub>－ln(<em>x</em><sub>1</sub><em>x</em><sub>2</sub>)，
令<em>t</em>＝<em>x</em><sub>1</sub><em>x</em><sub>2</sub>，则由<em>φ</em>(<em>t</em>)＝<em>t</em>－ln <em>t</em>，得<em>φ</em>′(<em>t</em>)＝1－＝，

易知*φ*(*t*)在区间(0，1)上单调递减，在区间(1，＋∞)上单调递增，
所以<em>φ</em>(<em>t</em>)≥<em>φ</em>（1）＝1，所以(<em>x</em><sub>1</sub>＋<em>x</em><sub>2</sub>)<sup>2</sup>＋(<em>x</em><sub>1</sub>＋<em>x</em><sub>2</sub>)≥1，因为<em>x</em><sub>1</sub>&gt;0，<em>x</em><sub>2</sub>&gt;0，所以<em>x</em><sub>1</sub>＋<em>x</em><sub>2</sub>≥成立．

6．已知函数<em>f</em> (<em>x</em>)＝<em>λ</em>ln <em>x</em>－e<sup>－</sup><em><sup>x</sup></em>(<em>λ</em>∈<strong>R</strong>)．  
（1）若函数*f* (*x*)是单调函数，求*λ*的取值范围；
![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)  
（2）求证：当0&lt;<em>x</em><sub>1</sub>&lt;<em>x</em><sub>2</sub>时，．

6．<strong>解析</strong>　（1）函数<em>f</em> (<em>x</em>)的定义域为(0，＋∞)，∵<em>f</em> (<em>x</em>)＝<em>λ</em>ln <em>x</em>－e<sup>－</sup><em><sup>x</sup></em>，∴<em>f</em> ′(<em>x</em>)＝＋e<sup>－</sup><em><sup>x</sup></em>＝，
∵函数*f* (*x*)是单调函数，∴*f* ′(*x*)≤0或*f* ′(*x*)≥0在(0，＋∞)上恒成立，

①当函数<em>f</em> (<em>x</em>)是单调递减函数时，<em>f</em> ′(<em>x</em>)≤0，∴≤0，即<em>λ</em>＋<em>x</em>e<sup>－</sup><em><sup>x</sup></em>≤0，<em>λ</em>≤－<em>x</em>e<sup>－</sup><em><sup>x</sup></em>＝－，
令*φ*(*x*)＝－，则*φ*′(*x*)＝，当0<*x*<1时，*φ*′(*x*)<0，当*x*>1时，*φ*′(*x*)>0，
则<em>φ</em>(<em>x</em>)在(0，1)上单调递减，在(1，＋∞)上单调递增，∴当<em>x</em>&gt;0时，<em>φ</em>(<em>x</em>)<sub>min</sub>＝<em>φ</em>（1）＝－，∴<em>λ</em>≤－．

②当函数<em>f</em> (<em>x</em>)是单调递增函数时，<em>f</em> ′(<em>x</em>)≥0，∴≥0，即<em>λ</em>＋<em>x</em>e<sup>－</sup><em><sup>x</sup></em>≥0，<em>λ</em>≥－<em>x</em>e<sup>－</sup><em><sup>x</sup></em>＝－，
由①得*φ*(*x*)＝－在(0，1)上单调递减，在(1，＋∞)上单调递增，又*φ*（0）＝0，*x*→＋∞时，*φ*(*x*)<0，∴*λ*≥0．

综上，*λ*的取值范围是∪[0，＋∞)．  
（2）由（1）可知，当<em>λ</em>＝－时，<em>f</em> (<em>x</em>)＝－ln <em>x</em>－e<sup>－</sup><em><sup>x</sup></em>在(0，＋∞)上单调递减，

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
∵0&lt;<em>x</em><sub>1</sub>&lt;<em>x</em><sub>2</sub>，∴<em>f</em> (<em>x</em><sub>1</sub>)&gt;<em>f</em> (<em>x</em><sub>2</sub>)，即－ln <em>x</em><sub>1</sub>－&gt;－ln <em>x</em><sub>2</sub>－，∴&gt;ln <em>x</em><sub>1</sub>－ln <em>x</em><sub>2</sub>．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
要证，只需证ln <em>x</em><sub>1</sub>－ln <em>x</em><sub>2</sub>&gt;1－，即证ln&gt;1－，
令*t*＝，*t*∈(0，1)，则只需证ln *t*>1－，令*h*(*t*)＝ln *t*＋－1，则*h*′(*t*)＝－＝，
当0<*t*<1时，*h*′(*t*)<0，∴*h*(*t*)在(0，1)上单调递减，又*h*（1）＝0，∴*h*(*t*)>0，即ln *t*>1－，故原不等式得证．

7．已知函数*f*(*x*)＝ln*x*＋(*a*>0)．  
（1）若函数*f*(*x*)有零点，求实数*a*的取值范围；  
（2）证明：当*a*≥，*b*>1时，*f*(ln*b*)>．

7．<strong>解析</strong>　（1）解法一　函数<em>f</em>(<em>x</em>)＝ln <em>x</em>＋的定义域为(0，＋∞)．由<em>f</em>(<em>x</em>)＝ln <em>x</em>＋，得<em>f</em>′(<em>x</em>)＝－＝．
因为*a*＞0，*x*∈(0，*a*)时，*f*′(*x*)＜0，*x*∈(*a*，＋∞)时，*f*′(*x*)＞0，
所以函数*f*(*x*)在(0，*a*)上单调递减，在(*a*，＋∞)上单调递增．
当<em>x</em>＝<em>a</em>时，<em>f</em>(<em>x</em>)<sub>min</sub>＝ln <em>a</em>＋1．又<em>f</em>（1）＝ln 1＋<em>a</em>＝<em>a</em>＞0，当ln <em>a</em>＋1≤0，即0＜<em>a</em>≤时，函数<em>f</em>(<em>x</em>)有零点．
所以实数*a*的取值范围为．
解法二　函数*f*(*x*)＝ln *x*＋的定义域为(0，＋∞)．由*f*(*x*)＝ln *x*＋＝0，得*a*＝－*x*ln *x*．
令*g*(*x*)＝－*x*ln *x*，则*g*′(*x*)＝－(ln *x*＋1)．当*x*∈时，*g*′(*x*)＞0；当*x*∈时，*g*′(*x*)＜0，
所以函数*g*(*x*)在上单调递增，在上单调递减．
故*x*＝时，函数*g*(*x*)取得最大值*g*＝－ln＝．又*a*＞0，则0＜*a*≤．
所以实数*a*的取值范围为．  
（2）要证*f*(ln *b*)>，即证ln(ln *b*)＋>，因为*b*>1，所以ln *b*>0，即证(ln *b*)ln(ln *b*)＋*a*>，
令<em>t</em>＝ln <em>b</em>，<em>t</em>&gt;0，即证<em>t</em>ln <em>t</em>＋<em>a</em>&gt;<em>t</em>e<sup>－</sup><em><sup>t</sup></em>．令<em>h</em>(<em>x</em>)＝<em>x</em>ln <em>x</em>＋<em>a</em>，则<em>h</em>′(<em>x</em>)＝ln <em>x</em>＋1．
当0<*x*<时，*h*′(*x*)<0；当*x*>时，*h*′(*x*)>0．
所以函数<em>h</em>(<em>x</em>)在上单调递减，在上单调递增．所以<em>h</em>(<em>x</em>)<sub>min</sub>＝<em>h</em>＝－＋<em>a</em>．
于是，当*a*≥时，*h*(*x*)≥－＋*a*≥．①
令<em>φ</em>(<em>x</em>)＝<em>x</em>e<sup>－</sup><em><sup>x</sup></em>，则<em>φ</em>′(<em>x</em>)＝e<sup>－</sup><em><sup>x</sup></em>－<em>x</em>e<sup>－</sup><em><sup>x</sup></em>＝e<sup>－</sup><em><sup>x</sup></em>(1－<em>x</em>)．当0&lt;<em>x</em>&lt;1时，<em>φ</em>′(<em>x</em>)&gt;0；当<em>x</em>&gt;1时，<em>φ</em>′(<em>x</em>)&lt;0．
所以函数<em>φ</em>(<em>x</em>)在(0，1)上单调递增，在(1，＋∞)上单调递减，所以<em>φ</em>(<em>x</em>)<sub>max</sub>＝<em>φ</em>（1）＝．
于是当*x*>0时，*φ*(*x*)≤．②
显然不等式①②中的等号不能同时成立，
故当<em>x</em>&gt;0，<em>a</em>≥时，<em>h</em>(<em>x</em>)&gt;<em>φ</em>(<em>x</em>)，即<em>x</em>ln <em>x</em>＋<em>a</em>&gt;<em>x</em>e<sup>－</sup><em><sup>x</sup></em>．所以<em>f</em>(ln <em>b</em>)&gt;．

