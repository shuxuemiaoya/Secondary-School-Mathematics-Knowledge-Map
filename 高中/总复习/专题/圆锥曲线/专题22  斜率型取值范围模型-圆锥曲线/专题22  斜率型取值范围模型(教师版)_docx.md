专题22　斜率型取值范围模型

![](images/079027907cac2fda5a0f42e1c3bcdbef82c57c6ca12f121a2a8cb41732a7f259.jpg)

1．圆锥曲线中范围问题求解的基本思路
解决有关范围问题的基本思路是建立目标函数或不等关系：

建立目标函数的关键是选用一个合适的变量，其原则是这个变量能够表达要解决的问题，利用求函数的值域的方法将待求量表示为其他变量的函数，求其值域，从而确定参数的取值范围；
建立不等关系时，先要恰当地引入变量(如点的坐标、角、斜率等)，寻找不等关系．

2．圆锥曲线中范围问题建立不等关系的基本方法  
（1）利用圆锥曲线的几何性质或判别式构造不等关系，从而确定参数的取值范围；  
（2）利用已知参数的范围，求新参数的范围，解这类问题的核心是建立两个参数之间的等量关系；  
（3）利用已知的不等关系构造不等式，从而求出参数的取值范围；  
（4）利用隐含的不等关系建立不等式，从而求出参数的取值范围．

3．圆锥曲线中范围问题的基本类型

圆锥曲线中的范围问题主要有以下四种情况：  
（1）斜率型；（2）参数及点的坐标(横或纵)型；（3）长度和距离型；（4）面积与数量积型．

【例题选讲】

<strong>[例1]</strong>　设椭圆＋＝1(<em>a</em>&gt;)的右焦点为<em>F</em>，右顶点为<em>A</em>．已知|<em>OA</em>|－|<em>OF</em>|＝1，其中<em>O</em>为原点，e为椭圆的离心率．  
（1）求椭圆的方程及离心率e的值；  
（2）设过点*A*的直线*l*与椭圆交于点*B*(*B*不在*x*轴上)，垂直于*l*的直线与*l*交于点*M*，与*y*轴交于点*H*．若*BF*⊥*HF*，且∠*MOA*≤∠*MAO*，求直线*l*的斜率的取值范围．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

<strong>[破题思路]</strong>　由题目条件垂直于直线<em>l</em>的直线与<em>l</em>交于点<em>M</em>，与<em>y</em>轴交于点<em>H</em>，利用<em>k</em>·<em>k<sub>MH</sub></em>＝－1，建立关于<em>k</em>的两条直线方程，由题目条件∠<em>MOA</em>≤∠<em>MAO</em>，利用三角形的大角对大边，建立关于<em>x<sub>M</sub></em>的不等式，利用题目条件<em>BF</em>⊥<em>HF</em>，即·＝0建立关系式．

[规范解答]  
（1）由题意可知|*OF*|＝*c*＝，又|*OA*|－|*OF*|＝1，所以*a*－＝1，解得*a*＝2，
所以椭圆的方程为＋＝1，离心率e＝＝．  
（2）设<em>M</em>(<em>x<sub>M</sub></em>，<em>y<sub>M</sub></em>)，易知<em>A</em>(2，0)，在△<em>MAO</em>中，∠<em>MOA</em>≤∠<em>MAO</em>⇔|<em>MA</em>|≤|<em>MO</em>|，
即(<em>x<sub>M</sub></em>－2)<sup>2</sup>＋<em>y</em>≤<em>x</em>＋<em>y</em>，化简得<em>x<sub>M</sub></em>≥1．
设直线*l*的斜率为*k*(*k*≠0)，则直线*l*的方程为*y*＝*k*(*x*－2)．
设<em>B</em>(<em>x<sub>B</sub></em>，<em>y<sub>B</sub></em>)，联立消去<em>y</em>，整理得(4<em>k</em><sup>2</sup>＋3)<em>x</em><sup>2</sup>－16<em>k</em><sup>2</sup><em>x</em>＋16<em>k</em><sup>2</sup>－12＝0，
解得<em>x</em>＝2或<em>x</em>＝．由题意得<em>x<sub>B</sub></em>＝，从而<em>y<sub>B</sub></em>＝．
由（1）知<em>F</em>(1，0)，设<em>H</em>(0，<em>y<sub>H</sub></em>)，则＝(－1，<em>y<sub>H</sub></em>)，＝．
由<em>BF</em>⊥<em>HF</em>，得·＝0，即＋＝0，解得<em>y<sub>H</sub></em>＝，
所以直线*MH*的方程为*y*＝－*x*＋．
由消去<em>y</em>，得<em>x<sub>M</sub></em>＝．
由<em>x<sub>M</sub></em>≥1，得≥1，解得<em>k</em>≤－或<em>k</em>≥，
所以直线*l*的斜率的取值范围为∪．

[题后悟通]　利用已知条件中的几何关系构建目标不等式的核心是用转化与化归的数学思想，将几何关系转化为代数不等式，从而构建出目标不等式．

<strong>[例2]</strong>　已知<em>A</em>是椭圆<em>E</em>：＋＝1(<em>t</em>&gt;3)的左顶点，斜率为<em>k</em>(<em>k</em>&gt;0)的直线交<em>E</em>于<em>A</em>，<em>M</em>两点，点<em>N</em>在<em>E</em>上，<em>MA</em>⊥<em>NA</em>．  
（1）当*t*＝4，|*AM*|＝|*AN*|时，求△*AMN*的面积；  
（2）当2|*AM*|＝|*AN*|时，求*k*的取值范围．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

<strong>[破题思路]</strong>　（1）求△<em>AMN</em>的面积，想到三角形的面积公式<em>S</em>＝×底×高或<em>S</em>＝<em>ab</em>sin <em>C</em>，题目条件中给出“<em>MA</em>⊥<em>NA</em>，|<em>AM</em>|＝|<em>AN</em>|”，得△<em>AMN</em>为等腰直角三角形，故可利用面积<em>S</em>＝|<em>AM</em>||<em>AN</em>|求解．到此就缺少|<em>AM</em>|，|<em>AN</em>|的值，由于<em>A</em>点已知，故想法求<em>M</em>，<em>N</em>的坐标．  
（2）题目条件中给出2|*AM*|＝|*AN*|，可利用此条件建立*t*与*k*的关系式，缺少关于*k*的不等式，想到*t*>3即可建立*k*的不等式．

[规范解答]  
（1）由|*AM*|＝|*AN*|，可得*M*，*N*关于*x*轴对称，由*MA*⊥*NA*，可得直线*AM*的斜率*k*为1．
因为*t*＝4，所以*A*(－2，0)，所以直线*AM*的方程为*y*＝*x*＋2，
代入椭圆方程＋＝1，可得7<em>x</em><sup>2</sup>＋16<em>x</em>＋4＝0，解得<em>x</em>＝－2或<em>x</em>＝－，
所以*M*，*N*，则△*AMN*的面积为××＝．  
（2）由题意知*t*>3，*k*>0，*A*(－，0)，
将直线<em>AM</em>的方程<em>y</em>＝<em>k</em>(<em>x</em>＋)代入＋＝1得(3＋<em>tk</em><sup>2</sup>)<em>x</em><sup>2</sup>＋2·<em>tk</em><sup>2</sup><em>x</em>＋<em>t</em><sup>2</sup><em>k</em><sup>2</sup>－3<em>t</em>＝0，
设<em>M</em>(<em>x</em><sub>1</sub>，<em>y</em><sub>1</sub>)，则<em>x</em><sub>1</sub>·(－)＝，即<em>x</em><sub>1</sub>＝，故|<em>AM</em>|＝|<em>x</em><sub>1</sub>＋|＝．
由题设知，直线*AN*的方程为*y*＝－(*x*＋)，故同理可得|*AN*|＝．
由2|<em>AM</em>|＝|<em>AN</em>|，得＝，即(<em>k</em><sup>3</sup>－2)<em>t</em>＝3<em>k</em>(2<em>k</em>－1)．
当*k*＝时上式不成立，因此*t*＝．由*t*>3，得>3，
所以＝<0，即<0．由此得或解得<*k*<2．
因此*k*的取值范围是(，2)．

<strong>[题后悟通]</strong>　解决本题第（2）问时，通过已知条件2|<em>AM</em>|＝|<em>AN</em>|得到参数<em>k</em>与参数<em>t</em>之间的关系，往往会忽视题目中的已知条件<em>t</em>&gt;3，不能建立关于<em>k</em>的不等式，从而导致问题无法求解．利用题目中隐藏的已知参数的范围求新参数的范围问题的核心是建立两个参数之间的等量关系，将新参数的范围转化为已知参数的范围问题．

<strong>[例3]</strong>　已知椭圆＋＝1(<em>a</em>＞<em>b</em>＞0)的左、右焦点分别为<em>F</em><sub>1</sub>，<em>F</em><sub>2</sub>，且|<em>F</em><sub>1</sub><em>F</em><sub>2</sub>|＝6，直线<em>y</em>＝<em>kx</em>与椭圆交于<em>A</em>，<em>B</em>两点．  
（1）若△<em>AF</em><sub>1</sub><em>F</em><sub>2</sub>的周长为16，求椭圆的标准方程；  
（2）若<em>k</em>＝，且<em>A</em>，<em>B</em>，<em>F</em><sub>1</sub>，<em>F</em><sub>2</sub>四点共圆，求椭圆离心率e的值；  
（3）在（2）的条件下，设<em>P</em>(<em>x</em><sub>0</sub>，<em>y</em><sub>0</sub>)为椭圆上一点，且直线<em>PA</em>的斜率<em>k</em><sub>1</sub>∈(－2，－1)，试求直线<em>PB</em>的斜率<em>k</em><sub>2</sub>的取值范围．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

<strong>[规范解答]</strong>　（1）由题意得<em>c</em>＝3，根据2<em>a</em>＋2<em>c</em>＝16，得<em>a</em>＝5．

结合<em>a</em><sup>2</sup>＝<em>b</em><sup>2</sup>＋<em>c</em><sup>2</sup>，解得<em>a</em><sup>2</sup>＝25，<em>b</em><sup>2</sup>＝16。所以椭圆的方程为＋＝1．  
（2）法一：由得<em>x</em><sup>2</sup>－<em>a</em><sup>2</sup><em>b</em><sup>2</sup>＝0．
设<em>A</em>(<em>x</em><sub>1</sub>，<em>y</em><sub>1</sub>)，<em>B</em>(<em>x</em><sub>2</sub>，<em>y</em><sub>2</sub>)．所以<em>x</em><sub>1</sub>＋<em>x</em><sub>2</sub>＝0，<em>x</em><sub>1</sub><em>x</em><sub>2</sub>＝，由<em>AB</em>，<em>F</em><sub>1</sub><em>F</em><sub>2</sub>互相平分且共圆，

易知，<em>AF</em><sub>2</sub>⊥<em>BF</em><sub>2</sub>，因为＝(<em>x</em><sub>1</sub>－3，<em>y</em><sub>1</sub>)，＝(<em>x</em><sub>2</sub>－3，<em>y</em><sub>2</sub>)，
所以·＝(<em>x</em><sub>1</sub>－3)(<em>x</em><sub>2</sub>－3)＋<em>y</em><sub>1</sub><em>y</em><sub>2</sub>＝<em>x</em><sub>1</sub><em>x</em><sub>2</sub>＋9＝0．
即<em>x</em><sub>1</sub><em>x</em><sub>2</sub>＝－8，所以有＝－8，结合<em>b</em><sup>2</sup>＋9＝<em>a</em><sup>2</sup>，解得<em>a</em><sup>2</sup>＝12(<em>a</em><sup>2</sup>＝6舍去)，
所以离心率<em>e</em>＝．(若设<em>A</em>(<em>x</em><sub>1</sub>，<em>y</em><sub>1</sub>)，<em>B</em>(－<em>x</em><sub>1</sub>，－<em>y</em><sub>1</sub>)相应给分)

法二：设<em>A</em>(<em>x</em><sub>1</sub>，<em>y</em><sub>1</sub>)，又<em>AB</em>，<em>F</em><sub>1</sub><em>F</em><sub>2</sub>互相平分且共圆，
所以<em>AB</em>，<em>F</em><sub>1</sub><em>F</em><sub>2</sub>是圆的直径，所以<em>x</em>＋<em>y</em>＝9，又由椭圆及直线方程综合可得：
由前两个方程解得<em>x</em>＝8，<em>y</em>＝1，将其代入第三个方程并结合<em>b</em><sup>2</sup>＝<em>a</em><sup>2</sup>－<em>c</em><sup>2</sup>＝<em>a</em><sup>2</sup>－9，
解得<em>a</em><sup>2</sup>＝12，故e＝．  
（3）由（2）的结论知，椭圆方程为＋＝1，由题可设<em>A</em>(<em>x</em><sub>1</sub>，<em>y</em><sub>1</sub>)，<em>B</em>(－<em>x</em><sub>1</sub>，－<em>y</em><sub>1</sub>)，

<em>k</em><sub>1</sub>＝，<em>k</em><sub>2</sub>＝，所以<em>k</em><sub>1</sub><em>k</em><sub>2</sub>＝，又＝＝－，
即<em>k</em><sub>2</sub>＝－，由－2＜<em>k</em><sub>1</sub>＜－1可知，＜<em>k</em><sub>2</sub>＜．即直线<em>PB</em>的斜率<em>k</em><sub>2</sub>的取值范围是．

<strong>[例4]</strong>　设<em>F</em><sub>1</sub>，<em>F</em><sub>2</sub>分别是椭圆<em>E</em>：＋＝1(<em>b</em>&gt;0)的左、右焦点，若<em>P</em>是该椭圆上的一个动点，且·的最大值为1．  
（1）求椭圆*E*的方程；  
（2）设直线*l*：*x*＝*ky*－1与椭圆*E*交于不同的两点*A*，*B*，且∠*AOB*为锐角(*O*为坐标原点)，求*k*的取值范围．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

<strong>[规范解答]</strong>　（1）易知<em>a</em>＝2，<em>c</em>＝，<em>b</em><sup>2</sup>&lt;4，所以<em>F</em><sub>1</sub>(－，0)，<em>F</em><sub>2</sub>(，0)，
设*P*(*x*，*y*)，则·＝(－－*x*，－*y*)·(－*x*，－*y*)

＝<em>x</em><sup>2</sup>＋<em>y</em><sup>2</sup>－4＋<em>b</em><sup>2</sup>＝<em>x</em><sup>2</sup>＋<em>b</em><sup>2</sup>－－4＋<em>b</em><sup>2</sup>＝<em>x</em><sup>2</sup>＋2<em>b</em><sup>2</sup>－4．
因为*x*∈[－2，2]，故当*x*＝±2，即点*P*为椭圆长轴端点时，·有最大值1，
即1＝×4＋2<em>b</em><sup>2</sup>－4，解得<em>b</em><sup>2</sup>＝1．故所求椭圆<em>E</em>的方程为＋<em>y</em><sup>2</sup>＝1．  
（2）设<em>A</em>(<em>x</em><sub>1</sub>，<em>y</em><sub>1</sub>)，<em>B</em>(<em>x</em><sub>2</sub>，<em>y</em><sub>2</sub>)，由得

(<em>k</em><sup>2</sup>＋4)<em>y</em><sup>2</sup>－2<em>ky</em>－3＝0，<em>Δ</em>＝(－2<em>k</em>)<sup>2</sup>＋12(4＋<em>k</em><sup>2</sup>)＝16<em>k</em><sup>2</sup>＋48&gt;0，故<em>y</em><sub>1</sub>＋<em>y</em><sub>2</sub>＝，<em>y</em><sub>1</sub>·<em>y</em><sub>2</sub>＝．
又∠<em>AOB</em>为锐角，故·＝<em>x</em><sub>1</sub><em>x</em><sub>2</sub>＋<em>y</em><sub>1</sub><em>y</em><sub>2</sub>&gt;0，又<em>x</em><sub>1</sub><em>x</em><sub>2</sub>＝(<em>ky</em><sub>1</sub>－1)(<em>ky</em><sub>2</sub>－1)＝<em>k</em><sup>2</sup><em>y</em><sub>1</sub><em>y</em><sub>2</sub>－<em>k</em>(<em>y</em><sub>1</sub>＋<em>y</em><sub>2</sub>)＋1，
所以<em>x</em><sub>1</sub><em>x</em><sub>2</sub>＋<em>y</em><sub>1</sub><em>y</em><sub>2</sub>＝(1＋<em>k</em><sup>2</sup>)<em>y</em><sub>1</sub><em>y</em><sub>2</sub>－<em>k</em>(<em>y</em><sub>1</sub>＋<em>y</em><sub>2</sub>)＋1＝(1＋<em>k</em><sup>2</sup>)·－＋1

＝＝&gt;0，所以<em>k</em><sup>2</sup>&lt;，解得－&lt;<em>k</em>&lt;，
故*k*的取值范围是．

<strong>[例5]</strong>　已知<em>C</em>为圆(<em>x</em>＋1)<sup>2</sup>＋<em>y</em><sup>2</sup>＝8的圆心，<em>P</em>是圆上的动点，点<em>Q</em>在圆的半径<em>CP</em>上，且有点<em>A</em>(1，0)和<em>AP</em>上的点<em>M</em>，满足·＝0，＝2．  
（1）当点*P*在圆上运动时，求点*Q*的轨迹方程；  
（2）若斜率为<em>k</em>的直线<em>l</em>与圆<em>x</em><sup>2</sup>＋<em>y</em><sup>2</sup>＝1相切，与（1）中所求点<em>Q</em>的轨迹交于不同的两点<em>F</em>，<em>H</em>，<em>O</em>是坐标原点，且≤·≤，求<em>k</em>的取值范围．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

<strong>[规范解答]</strong>　（1）由题意知<em>MQ</em>是线段<em>AP</em>的垂直平分线，
所以|*CP*|＝|*QC*|＋|*QP*|＝|*QC*|＋|*QA*|＝2>|*CA*|＝2，
所以点*Q*的轨迹是以点*C*，*A*为焦点，焦距为2，长轴长为2的椭圆，
所以<em>a</em>＝，<em>c</em>＝1，<em>b</em>＝＝1，故点<em>Q</em>的轨迹方程是＋<em>y</em><sup>2</sup>＝1．  
（2）设直线<em>l</em>：<em>y</em>＝<em>kx</em>＋<em>t</em>，<em>F</em>(<em>x</em><sub>1</sub>，<em>y</em><sub>1</sub>)，<em>H</em>(<em>x</em><sub>2</sub>，<em>y</em><sub>2</sub>)，直线<em>l</em>与圆<em>x</em><sup>2</sup>＋<em>y</em><sup>2</sup>＝1相切⇒＝1⇒<em>t</em><sup>2</sup>＝<em>k</em><sup>2</sup>＋1．
联立⇒(1＋2<em>k</em><sup>2</sup>)<em>x</em><sup>2</sup>＋4<em>ktx</em>＋2<em>t</em><sup>2</sup>－2＝0，
则<em>Δ</em>＝16<em>k</em><sup>2</sup><em>t</em><sup>2</sup>－4(1＋2<em>k</em><sup>2</sup>)(2<em>t</em><sup>2</sup>－2)＝8(2<em>k</em><sup>2</sup>－<em>t</em><sup>2</sup>＋1)＝8<em>k</em><sup>2</sup>&gt;0⇒<em>k</em>≠0，<em>x</em><sub>1</sub>＋<em>x</em><sub>2</sub>＝，<em>x</em><sub>1</sub><em>x</em><sub>2</sub>＝，
所以·＝<em>x</em><sub>1</sub><em>x</em><sub>2</sub>＋<em>y</em><sub>1</sub><em>y</em><sub>2</sub>＝(1＋<em>k</em><sup>2</sup>)<em>x</em><sub>1</sub><em>x</em><sub>2</sub>＋<em>kt</em>(<em>x</em><sub>1</sub>＋<em>x</em><sub>2</sub>)＋<em>t</em><sup>2</sup>＝＋<em>kt</em>＋<em>t</em><sup>2</sup>

＝－＋<em>k</em><sup>2</sup>＋1＝，
所以≤≤⇒≤<em>k</em><sup>2</sup>≤⇒≤|<em>k</em>|≤，所以－≤<em>k</em>≤－或≤<em>k</em>≤．
故*k*的取值范围是∪．

<strong>[例6]</strong>　已知<em>M</em>为椭圆<em>C</em>：＋＝1上的动点，过点<em>M</em>作<em>x</em>轴的垂线，垂足为<em>D</em>，点<em>P</em>满足＝．  
（1）求动点*P*的轨迹*E*的方程；  
（2）若<em>A</em>，<em>B</em>两点分别为椭圆<em>C</em>的左、右顶点，<em>F</em>为椭圆<em>C</em>的左焦点，直线<em>PB</em>与椭圆<em>C</em>交于点<em>Q</em>，直线<em>QF</em>，<em>PA</em>的斜率分别为<em>k<sub>QF</sub></em>，<em>k<sub>PA</sub></em>，求的取值范围．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

<strong>[规范解答]</strong>　（1）设<em>P</em>(<em>x</em>，<em>y</em>)，<em>M</em>(<em>m</em>，<em>n</em>)，依题意知<em>D</em>(<em>m，</em>0)，且<em>y</em>≠0．
由＝，得(*m*－*x*，－*y*)＝(0，－*n*)，则有⇒
又<em>M</em>(<em>m</em>，<em>n</em>)为椭圆<em>C</em>：＋＝1上的点，∴＋＝1，即<em>x</em><sup>2</sup>＋<em>y</em><sup>2</sup>＝25，
故动点<em>P</em>的轨迹<em>E</em>的方程为<em>x</em><sup>2</sup>＋<em>y</em><sup>2</sup>＝25(<em>y</em>≠0)．  
（2）依题意知<em>A</em>(－5，0)，<em>B</em>(5，0)，<em>F</em>(－4，0)，设Q(<em>x</em><sub>0</sub>，<em>y</em><sub>0</sub>)，
∵线段<em>AB</em>为圆<em>E</em>的直径，∴<em>AP</em>⊥<em>BP</em>，设直线<em>PB</em>的斜率为<em>k<sub>PB</sub></em>，
则＝＝－<em>k<sub>QF</sub>k<sub>PB</sub></em>＝－<em>k<sub>QF</sub>k<sub>QB</sub></em>＝－·＝－

＝－＝＝＝，
∵点<em>P</em>不同于<em>A</em>，<em>B</em>两点且直线<em>QF</em>的斜率存在，∴－5&lt;<em>x</em><sub>0</sub>&lt;5且<em>x</em><sub>0</sub>≠－4，
又*y*＝在(－5，－4)和(－4，5)上都是减函数，∴∈(－∞，0)∪，
故的取值范围是(－∞，0)∪．

【对点训练】

1．已知椭圆<em>C</em>的两个焦点为<em>F</em><sub>1</sub>(－1，0)，<em>F</em><sub>2</sub>(1，0)，且经过点<em>E</em>(，)．  
（1）求椭圆*C*的方程；  
（2）过点<em>F</em><sub>1</sub>的直线<em>l</em>与椭圆<em>C</em>交于<em>A</em>，<em>B</em>两点(点<em>A</em>位于<em>x</em>轴上方)，若＝<em>λ</em>，且2≤<em>λ</em>＜3，求直线<em>l</em>的斜率<em>k</em>的取值范围．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

1．解析　（1）由解得所以椭圆*C*的方程为＋＝1．  
（2）由题意得直线*l*的方程为*y*＝*k*(*x*＋1)(*k*＞0)，
联立方程，得整理得(＋4)<em>y</em><sup>2</sup>－<em>y</em>－9＝0，<em>Δ</em>＝＋144＞0，
设<em>A</em>(<em>x</em><sub>1</sub>，<em>y</em><sub>1</sub>)，<em>B</em>(<em>x</em><sub>2</sub>，<em>y</em><sub>2</sub>)，则<em>y</em><sub>1</sub>＋<em>y</em><sub>2</sub>＝，<em>y</em><sub>1</sub><em>y</em><sub>2</sub>＝，
又＝<em>λ</em>，所以<em>y</em><sub>1</sub>＝－<em>λy</em><sub>2</sub>，所以<em>y</em><sub>1</sub><em>y</em><sub>2</sub>＝(<em>y</em><sub>1</sub>＋<em>y</em><sub>2</sub>)<sup>2</sup>，则＝，<em>λ</em>＋－2＝，
因为2≤*λ*＜3，所以≤*λ*＋－2＜，即≤＜，且*k*＞0，解得0＜*k*≤．
故直线*l*的斜率*k*的取值范围是(0，]．

2．已知椭圆＋＝1(*a*＞*b*＞0)的左焦点为*F*(－*c*，0)，离心率为，点*M*在椭圆上且位于第一象限，直

线<em>FM</em>被圆<em>x</em><sup>2</sup>＋<em>y</em><sup>2</sup>＝截得的线段的长为<em>c</em>，|<em>FM</em>|＝．  
（1）求直线*FM*的斜率；  
（2）求椭圆的方程；  
（3）设动点*P*在椭圆上，若直线*FP*的斜率大于，求直线*OP*(*O*为原点)的斜率的取值范围．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

2．解析　（1）由已知，有＝，又由<em>a</em><sup>2</sup>＝<em>b</em><sup>2</sup>＋<em>c</em><sup>2</sup>，可得<em>a</em><sup>2</sup>＝3<em>c</em><sup>2</sup>，<em>b</em><sup>2</sup>＝2<em>c</em><sup>2</sup>．
设直线*FM*的斜率为*k*(*k*＞0)，*F*(－*c*，0)，则直线*FM*的方程为*y*＝*k*(*x*＋*c*)．
由已知，有＋＝，解得*k*＝．  
（2）由（1）得椭圆方程为＋＝1，直线*FM*的方程为*y*＝(*x*＋*c*)，

两个方程联立，消去<em>y</em>，整理得3<em>x</em><sup>2</sup>＋2<em>cx</em>－5<em>c</em><sup>2</sup>＝0，解得<em>x</em>＝－<em>c</em>，或<em>x</em>＝<em>c</em>．
因为点*M*在第一象限，可得*M*的坐标为．
由|*FM*|＝＝，解得*c*＝1，所以椭圆的方程为＋＝1．  
（3）设点*P*的坐标为(*x*，*y*)，直线*FP*的斜率为*t*，得*t*＝，即*y*＝*t*(*x*＋1)(*x*≠－1)，与椭圆方程联立
消去<em>y</em>，整理得2<em>x</em><sup>2</sup>＋3<em>t</em><sup>2</sup>(<em>x</em>＋1)<sup>2</sup>＝6，
又由已知，得*t*＝＞，解得－＜*x*＜－1，或－1＜*x*＜0．
设直线<em>OP</em>的斜率为<em>m</em>，得<em>m</em>＝，即<em>y</em>＝<em>mx</em>(<em>x</em>≠0)，与椭圆方程联立，整理得<em>m</em><sup>2</sup>＝－．

①当*x*∈时，有*y*＝*t*(*x*＋1)＜0，因此*m*＞0，于是*m*＝，得*m*∈．

②当*x*∈(－1，0)时，有*y*＝*t*(*x*＋1)＞0，因此*m*＜0，于是*m*＝－，得*m*∈．

综上，直线*OP*的斜率的取值范围是∪．

3．已知椭圆*C*：＋＝1(*a*＞*b*＞0)的离心率为，且椭圆*C*上的点到一个焦点的距离的最小值为－．  
（1）求椭圆*C*的方程；  
（2）已知过点*T*(0，2)的直线*l*与椭圆*C*交于*A*，*B*两点，若在*x*轴上存在一点*E*，使∠*AEB*＝90°，求直线*l*的斜率*k*的取值范围．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

3．解析　（1）设椭圆的半焦距长为*c*，则由题设有：
解得：<em>a</em>＝，<em>c</em>＝，∴<em>b</em><sup>2</sup>＝1，故椭圆<em>C</em>的方程为＋<em>x</em><sup>2</sup>＝1．  
（2）由已知可得，以<em>AB</em>为直径的圆与<em>x</em>轴有公共点．设<em>A</em>(<em>x</em><sub>1</sub>，<em>y</em><sub>1</sub>)，<em>B</em>(<em>x</em><sub>2</sub>，<em>y</em><sub>2</sub>)，<em>AB</em>中点为<em>M</em>(<em>x</em><sub>0</sub>，<em>y</em><sub>0</sub>)，
将直线<em>l</em>：<em>y</em>＝<em>kx</em>＋2代入＋<em>x</em><sup>2</sup>＝1，得(3＋<em>k</em><sup>2</sup>)<em>x</em><sup>2</sup>＋4<em>kx</em>＋1＝0，<em>Δ</em>＝12<em>k</em><sup>2</sup>－12，
∴<em>x</em><sub>0</sub>＝＝，<em>y</em><sub>0</sub>＝<em>kx</em><sub>0</sub>＋2＝，|<em>AB</em>|＝＝，
∴解得：<em>k</em><sup>4</sup>≥13，即<em>k</em>≥或<em>k</em>≤－．

4．在圆<em>x</em><sup>2</sup>＋<em>y</em><sup>2</sup>＝9上任取一点<em>P</em>，过点<em>P</em>作<em>x</em>轴的垂线段<em>PD</em>，<em>D</em>为垂足．点<em>M</em>在线段<em>DP</em>上，满足＝

．当点*P*在圆上运动时，设点*M*的轨迹为曲线*C*．  
（1）求曲线*C*的方程；  
（2）若直线*y*＝*m*(*x*＋5)上存在点*Q*，使得过点*Q*作曲线*C*的两条切线相互垂直，求实数*m*的取值范围．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

4．解析　（1）设点<em>M</em>的坐标为(<em>x</em>，<em>y</em>)，点<em>P</em>的坐标为(<em>x</em><sub>0</sub>，<em>y</em><sub>0</sub>)．由题意，得<em>x</em>＝<em>x</em><sub>0</sub>，<em>y</em>＝<em>y</em><sub>0</sub>，即<em>x</em><sub>0</sub>＝<em>x</em>，<em>y</em><sub>0</sub>＝<em>y</em>．
∵点<em>P</em>(<em>x</em><sub>0</sub>，<em>y</em><sub>0</sub>)在圆<em>x</em><sup>2</sup>＋<em>y</em><sup>2</sup>＝9上，所以<em>x</em>＋<em>y</em>＝9．
将<em>x</em><sub>0</sub>＝<em>x</em>，<em>y</em><sub>0</sub>＝<em>y</em>代入上式，得<em>x</em><sup>2</sup>＋<em>y</em><sup>2</sup>＝9，即＋＝1．∴曲线<em>C</em>的方程为＋＝1(<em>x</em>≠±3)．  
（2）①若两切线的斜率都存在，设点<em>Q</em>(<em>x</em><sub>1</sub>，<em>y</em><sub>1</sub>)，过<em>Q</em>的切线方程为<em>y</em>－<em>y</em><sub>1</sub>＝<em>k</em>(<em>x</em>－<em>x</em><sub>1</sub>)，与＋＝1联立，
消去<em>y</em>并整理，得(9<em>k</em><sup>2</sup>＋4)<em>x</em><sup>2</sup>＋18<em>k</em>(<em>y</em><sub>1</sub>－<em>kx</em><sub>1</sub>)<em>x</em>＋9[(<em>y</em><sub>1</sub>－<em>kx</em><sub>1</sub>)<sup>2</sup>－4]＝0．
由<em>Δ</em>＝0，得[18<em>k</em>(<em>y</em><sub>1</sub>－<em>kx</em><sub>1</sub>)]<sup>2</sup>－4(9<em>k</em><sup>2</sup>＋4)·9[(<em>y</em><sub>1</sub>－<em>kx</em><sub>1</sub>)<sup>2</sup>－4]＝0，36<em>k</em><sup>2</sup>－4<em>y</em>＋8<em>kx</em><sub>1</sub><em>y</em><sub>1</sub>－4<em>k</em><sup>2</sup><em>x</em>＋16＝0，
整理得(9－<em>x</em>)<em>k</em><sup>2</sup>＋2<em>x</em><sub>1</sub><em>y</em><sub>1</sub><em>k</em>＋4－<em>y</em>＝0．
设两切线的斜率分别为<em>k</em><sub>1</sub>，<em>k</em><sub>2</sub>，则<em>k</em><sub>1</sub>·<em>k</em><sub>2</sub>＝－1，即<em>k</em><sub>1</sub>·<em>k</em><sub>2</sub>＝＝－1，即<em>x</em>＋<em>y</em>＝13(<em>x</em><sub>1</sub>≠±3)．

②若两切线的斜率有一条不存在，则点*Q*的坐标为(±3，±2)，满足*x*＋*y*＝13．
即点<em>Q</em>的轨迹方程为<em>x</em><sup>2</sup>＋<em>y</em><sup>2</sup>＝13．
由题意知满足条件的点是直线<em>y</em>＝<em>m</em>(<em>x</em>＋5)与圆<em>x</em><sup>2</sup>＋<em>y</em><sup>2</sup>＝13的公共点．

圆心*O*(0，0)到直线*y*＝*m*(*x*＋5)的距离*d*＝，
由直线<em>y</em>＝<em>m</em>(<em>x</em>＋5)和圆<em>x</em><sup>2</sup>＋<em>y</em><sup>2</sup>＝13有公共点可知，距离<em>d</em>≤<em>r</em>，即≤，解得－≤<em>m</em>≤．
故实数*m*的取值范围是．

5．已知点*P*(0，－2)，点*A*，*B*分别为椭圆*E*：＋＝1(*a*>*b*>0)的左右顶点，直线*BP*交*E*于点*Q*，△*ABP*

是等腰直角三角形，且＝．  
（1）求*E*的方程；  
（2）设过点*P*的动直线*l*与*E*相交于*M*，*N*两点，当坐标原点*O*位于*MN*以为直径的圆外时，求直线*l*斜率的取值范围．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

5．解析　（1）由题意△<em>ABP</em>是等腰直角三角形，<em>a</em>＝2，<em>B</em>(2，0)，设<em>Q</em>(<em>x</em><sub>0</sub>，<em>y</em><sub>0</sub>)，由＝，则
代入椭圆方程，解得<em>b</em><sup>2</sup>＝1，∴椭圆方程为＋<em>y</em><sup>2</sup>＝1．  
（2）由题意可知，直线<em>l</em>的斜率存在，方程为<em>y</em>＝<em>kx</em>－2，<em>M</em>(<em>x</em><sub>1</sub>，<em>y</em><sub>1</sub>)，<em>N</em>(<em>x</em><sub>2</sub>，<em>y</em><sub>2</sub>)，
则整理得(1＋4<em>k</em><sup>2</sup>)<em>x</em><sup>2</sup>－16<em>kx</em>＋12＝0，
由直线<em>l</em>与<em>E</em>有两个不同的交点，则<em>Δ</em>＞0，即(－16<em>k</em>)<sup>2</sup>－4×12×(1＋4<em>k</em><sup>2</sup>)＞0，解得<em>k</em><sup>2</sup>＞，
由韦达定理可知<em>x</em><sub>1</sub>＋<em>x</em><sub>2</sub>＝，<em>x</em><sub>1</sub><em>x</em><sub>2</sub>＝，
由坐标原点<em>O</em>位于<em>MN</em>为直径的圆外，则·＞0，即<em>x</em><sub>1</sub><em>x</em><sub>2</sub>＋<em>y</em><sub>1</sub><em>y</em><sub>2</sub>＞0，则

<em>x</em><sub>1</sub><em>x</em><sub>2</sub>＋<em>y</em><sub>1</sub><em>y</em><sub>2</sub>＝<em>x</em><sub>1</sub><em>x</em><sub>2</sub>＋(<em>kx</em><sub>1</sub>－2)(<em>kx</em><sub>2</sub>－2)＝(1＋<em>k</em><sup>2</sup>)<em>x</em><sub>1</sub><em>x</em><sub>2</sub>－2<em>k</em>×(<em>x</em><sub>1</sub>＋<em>x</em><sub>2</sub>)＋4＝(1＋<em>k</em><sup>2</sup>)－2<em>k</em>×＋4＞0，
解得<em>k</em><sup>2</sup>＜4，综上可知＜<em>k</em><sup>2</sup>＜4，解得＜<em>k</em>＜2或－2＜<em>k</em>＜－，

直线*l*斜率的取值范围∪．

6．已知右焦点为<em>F</em><sub>2</sub>(<em>c</em>，0)的椭圆<em>C</em>：＋＝1(<em>a</em>&gt;<em>b</em>&gt;0)过点，且椭圆<em>C</em>关于直线<em>x</em>＝<em>c</em>对称的图形过

坐标原点．  
（1）求椭圆*C*的方程；  
（2）过点作直线*l*与椭圆*C*交于*E*，*F*两点，线段*EF*的中点为*M*，点*A*是椭圆*C*的右顶点，求直线*MA*的斜率*k*的取值范围．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

6．解析　（1）∵椭圆*C*过点，∴＋＝1，①
∵椭圆<em>C</em>关于直线<em>x</em>＝<em>c</em>对称的图形过坐标原点，∴<em>a</em>＝2<em>c</em>，∵<em>a</em><sup>2</sup>＝<em>b</em><sup>2</sup>＋<em>c</em><sup>2</sup>，∴<em>b</em><sup>2</sup>＝<em>a</em><sup>2</sup>，②
由①②得<em>a</em><sup>2</sup>＝4，<em>b</em><sup>2</sup>＝3，∴椭圆<em>C</em>的方程为＋＝1．  
（2）依题意，直线*l*过点且斜率不为零，故可设其方程为*x*＝*my*＋．
由方程组消去<em>x</em>，并整理得4(3<em>m</em><sup>2</sup>＋4)<em>y</em><sup>2</sup>＋12<em>my</em>－45＝0．
设<em>E</em>(<em>x</em><sub>1</sub>，<em>y</em><sub>1</sub>)，<em>F</em>(<em>x</em><sub>2</sub>，<em>y</em><sub>2</sub>)，<em>M</em>(<em>x</em><sub>0</sub>，<em>y</em><sub>0</sub>)，∴<em>y</em><sub>1</sub>＋<em>y</em><sub>2</sub>＝－，∴<em>y</em><sub>0</sub>＝＝－，
∴<em>x</em><sub>0</sub>＝<em>my</em><sub>0</sub>＋＝，∴<em>k</em>＝＝．

①当*m*＝0时，*k*＝0．

②当*m*≠0时，*k*＝，当*m*>0时，4*m*＋≥8，∴0<≤．∴0<*k*≤，
当*m*<0时，4*m*＋＝－(－4*m*)＋≤－8，∴－≤＝*k*<0．∴－≤*k*≤且*k*≠0．
综合①、②可知，直线*MA*的斜率*k*的取值范围是．

7．在直角坐标系<em>xOy</em>中，曲线<em>C</em><sub>1</sub>上的任意一点<em>M</em>到直线<em>y</em>＝－1的距离比<em>M</em>点到点<em>F</em>(0，2)的距离小1．  
（1）求动点<em>M</em>的轨迹<em>C</em><sub>1</sub>的方程；  
（2）若点<em>P</em>是圆<em>C</em><sub>2</sub>：(<em>x</em>－2)<sup>2</sup>＋(<em>y</em>＋2)<sup>2</sup>＝1上一动点，过点<em>P</em>作曲线<em>C</em><sub>1</sub>的两条切线，切点分别为<em>A</em>，<em>B</em>，求直线<em>AB</em>斜率的取值范围．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

7．<strong>解析</strong>　（1）法一　设点<em>M</em>(<em>x</em>，<em>y</em>)，∵点<em>M</em>到直线<em>y</em>＝－1的距离等于|<em>y</em>＋1|，
∴|<em>y</em>＋1|＝－1，化简得<em>x</em><sup>2</sup>＝8<em>y</em>，
∴动点<em>M</em>的轨迹<em>C</em><sub>1</sub>的方程为<em>x</em><sup>2</sup>＝8<em>y</em>．

法二　由题意知*M*到直线*y*＝－2的距离等于*M*到*F*(0，2)的距离，
由抛物线定义得动点<em>M</em>的轨迹方程为<em>x</em><sup>2</sup>＝8<em>y</em>．  
（2）由题意可知，<em>PA</em>，<em>PB</em>的斜率都存在，分别设为<em>k</em><sub>1</sub>，<em>k</em><sub>2</sub>，切点<em>A</em>(<em>x</em><sub>1</sub>，<em>y</em><sub>1</sub>)，<em>B</em>(<em>x</em><sub>2</sub>，<em>y</em><sub>2</sub>)，
设点*P*(*m*，*n*)，过点*P*的抛物线的切线方程为*y*＝*k*(*x*－*m*)＋*n*，
联立得<em>x</em><sup>2</sup>－8<em>kx</em>＋8<em>km</em>－8<em>n</em>＝0，
∵<em>Δ</em>＝64<em>k</em><sup>2</sup>－32<em>km</em>＋32<em>n</em>＝0，即2<em>k</em><sup>2</sup>－<em>km</em>＋<em>n</em>＝0，∴<em>k</em><sub>1</sub>＋<em>k</em><sub>2</sub>＝，<em>k</em><sub>1</sub><em>k</em><sub>2</sub>＝．
由<em>x</em><sup>2</sup>＝8<em>y</em>，得<em>y</em>′＝，∴<em>x</em><sub>1</sub>＝4<em>k</em><sub>1</sub>，<em>y</em><sub>1</sub>＝＝2<em>k</em>，<em>x</em><sub>2</sub>＝4<em>k</em><sub>2</sub>，<em>y</em><sub>2</sub>＝＝2<em>k</em>，
∴<em>k<sub>AB</sub></em>＝＝＝＝，
∵点<em>P</em>(<em>m</em>，<em>n</em>)满足(<em>x</em>－2)<sup>2</sup>＋(<em>y</em>＋2)<sup>2</sup>＝1，∴1≤<em>m</em>≤3，
∴≤≤，即直线*AB*斜率的取值范围为．

