专题26　单变量型三角形面积最值问题

![](images/07238867ffe8ff293a97229472ea89053ea768dfbef8d4739d52e632f7c19aea.jpg)

最值问题——构造函数

最值问题的基本解法有几何法和代数法：几何法是根据已知的几何量之间的相互关系、平面几何和解析几何知识加以解决的(如抛物线上的点到某个定点和焦点的距离之和、光线反射问题等)；代数法是建立求解目标关于某个或两个变量的函数，通过求解函数的最值普通方法、基本不等式方法、导数方法等解决的．

【例题选讲】

<strong>[例1]</strong>　在平面直角坐标系中，圆<em>O</em>交<em>x</em>轴于点<em>F</em><sub>1</sub>，<em>F</em><sub>2</sub>，交<em>y</em>轴于点<em>B</em><sub>1</sub>，<em>B</em><sub>2</sub>．以<em>B</em><sub>1</sub>，<em>B</em><sub>2</sub>为顶点，<em>F</em><sub>1</sub>，<em>F</em><sub>2</sub>分别为左、右焦点的椭圆<em>E</em>恰好经过点．  
（1）求椭圆*E*的标准方程；  
（2）设经过点(－2，0)的直线<em>l</em>与椭圆<em>E</em>交于<em>M</em>，<em>N</em>两点，求△<em>F</em><sub>2</sub><em>MN</em>面积的最大值．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

<strong>[破题思路]</strong>　题干中给出直线<em>l</em>过点(－2，0)，可设出直线<em>l</em>的方程，利用弦长公式求|<em>MN</em>|，利用点到直线的距离求<em>d</em>，从而可求△<em>F</em><sub>2</sub><em>MN</em>的面积，要求△<em>F</em><sub>2</sub><em>MN</em>面积的最值，需建立相关函数模型求解．

<strong>[规范解答]</strong>　（1）由已知可得，椭圆<em>E</em>的焦点在<em>x</em>轴上．设椭圆<em>E</em>的标准方程为＋＝1(<em>a</em>&gt;<em>b</em>&gt;0)，

焦距为2<em>c</em>，则<em>b</em>＝<em>c</em>，∴<em>a</em><sup>2</sup>＝<em>b</em><sup>2</sup>＋<em>c</em><sup>2</sup>＝2<em>b</em><sup>2</sup>，∴椭圆<em>E</em>的标准方程为＋＝1．
又椭圆<em>E</em>过点，∴＋＝1，解得<em>b</em><sup>2</sup>＝1．∴椭圆<em>E</em>的标准方程为＋<em>y</em><sup>2</sup>＝1．  
（2）由于点(－2，0)在椭圆*E*外，∴直线*l*的斜率存在．
设直线<em>l</em>的斜率为<em>k</em>，则直线<em>l</em>：<em>y</em>＝<em>k</em>(<em>x</em>＋2)，设<em>M</em>(<em>x</em><sub>1</sub>，<em>y</em><sub>1</sub>)，<em>N</em>(<em>x</em><sub>2</sub>，<em>y</em><sub>2</sub>)．
由消去<em>y</em>得，(1＋2<em>k</em><sup>2</sup>)<em>x</em><sup>2</sup>＋8<em>k</em><sup>2</sup><em>x</em>＋8<em>k</em><sup>2</sup>－2＝0．由<em>Δ</em>&gt;0，得0≤<em>k</em><sup>2</sup>&lt;，
从而<em>x</em><sub>1</sub>＋<em>x</em><sub>2</sub>＝，<em>x</em><sub>1</sub><em>x</em><sub>2</sub>＝，∴|<em>MN</em>|＝|<em>x</em><sub>1</sub>－<em>x</em><sub>2</sub>|＝2·．
∵点<em>F</em><sub>2</sub>(1，0)到直线<em>l</em>的距离<em>d</em>＝，∴△<em>F</em><sub>2</sub><em>MN</em>的面积<em>S</em>＝|<em>MN</em>|·<em>d</em>＝3．
令1＋2<em>k</em><sup>2</sup>＝<em>t</em>，则<em>t</em>∈[1，2)，
∴*S*＝3＝3＝3＝3，
当＝，即<em>t</em>＝时，<em>S</em>有最大值，<em>S</em><sub>max</sub>＝，此时<em>k</em>＝±．
∴当直线<em>l</em>的斜率为±时，可使△<em>F</em><sub>2</sub><em>MN</em>的面积最大，其最大值为．

<strong>[例2]</strong>　已知<em>O</em>为坐标原点，<em>M</em>(<em>x</em><sub>1</sub>，<em>y</em><sub>1</sub>)，<em>N</em>(<em>x</em><sub>2</sub>，<em>y</em><sub>2</sub>)是椭圆＋＝1上的点，且<em>x</em><sub>1</sub><em>x</em><sub>2</sub>＋2<em>y</em><sub>1</sub><em>y</em><sub>2</sub>＝0，设动点<em>P</em>满足＝＋2．  
（1）求动点*P*的轨迹*C*的方程；  
（2）若直线*l*：*y*＝*x*＋*m*(*m*≠0)与曲线*C*交于*A*，*B*两点，求△*OAB*面积的最大值．

<strong>[规范解答]</strong>　（1）设点<em>P</em>(<em>x</em>，<em>y</em>)，则由＝＋2，得(<em>x</em>，<em>y</em>)＝(<em>x</em><sub>1</sub>，<em>y</em><sub>1</sub>)＋2(<em>x</em><sub>2</sub>，<em>y</em><sub>2</sub>)，
即<em>x</em>＝<em>x</em><sub>1</sub>＋2<em>x</em><sub>2</sub>，<em>y</em>＝<em>y</em><sub>1</sub>＋2<em>y</em><sub>2</sub>．因为点<em>M</em>，<em>N</em>在椭圆＋＝1上，所以<em>x</em>＋2<em>y</em>＝4，<em>x</em>＋2<em>y</em>＝4．
故<em>x</em><sup>2</sup>＋2<em>y</em><sup>2</sup>＝(<em>x</em>＋4<em>x</em>＋4<em>x</em><sub>1</sub><em>x</em><sub>2</sub>)＋2(<em>y</em>＋4<em>y</em>＋4<em>y</em><sub>1</sub><em>y</em><sub>2</sub>)＝(<em>x</em>＋2<em>y</em>)＋4(<em>x</em>＋2<em>y</em>)＋4(<em>x</em><sub>1</sub><em>x</em><sub>2</sub>＋2<em>y</em><sub>1</sub><em>y</em><sub>2</sub>)

＝20＋4(<em>x</em><sub>1</sub><em>x</em><sub>2</sub>＋2<em>y</em><sub>1</sub><em>y</em><sub>2</sub>)．
又因为<em>x</em><sub>1</sub><em>x</em><sub>2</sub>＋2<em>y</em><sub>1</sub><em>y</em><sub>2</sub>＝0，所以<em>x</em><sup>2</sup>＋2<em>y</em><sup>2</sup>＝20，所以动点<em>P</em>的轨迹<em>C</em>的方程为<em>x</em><sup>2</sup>＋2<em>y</em><sup>2</sup>＝20．  
（2）将曲线<em>C</em>与直线<em>l</em>的方程联立，得消去<em>y</em>得3<em>x</em><sup>2</sup>＋4<em>mx</em>＋2<em>m</em><sup>2</sup>－20＝0．
因为直线<em>l</em>与曲线<em>C</em>交于<em>A</em>，<em>B</em>两点，设<em>A</em>(<em>x</em><sub>3</sub>，<em>y</em><sub>3</sub>)，<em>B</em>(<em>x</em><sub>4</sub>，<em>y</em><sub>4</sub>)，
所以<em>Δ</em>＝16<em>m</em><sup>2</sup>－4×3×(2<em>m</em><sup>2</sup>－20)＞0．又<em>m</em>≠0，所以0＜<em>m</em><sup>2</sup>＜30，<em>x</em><sub>3</sub>＋<em>x</em><sub>4</sub>＝－，<em>x</em><sub>3</sub><em>x</em><sub>4</sub>＝．
又点*O*到直线*AB*：*x*－*y*＋*m*＝0的距离*d*＝，

|<em>AB</em>|＝|<em>x</em><sub>3</sub>－<em>x</em><sub>4</sub>|＝＝ ＝ ，
所以<em>S</em><sub>△</sub><em><sub>OAB</sub></em>＝ ×＝×≤×＝5，
当且仅当<em>m</em><sup>2</sup>＝30－<em>m</em><sup>2</sup>，即<em>m</em><sup>2</sup>＝15时取等号，且满足<em>Δ</em>&gt;0．所以△<em>OAB</em>面积的最大值为5．

<strong>[例3]</strong>　已知直线<em>l</em><sub>1</sub>：<em>ax</em>－<em>y</em>＋1＝0，直线<em>l</em><sub>2</sub>：<em>x</em>＋5<em>ay</em>＋5<em>a</em>＝0，直线<em>l</em><sub>1</sub>与<em>l</em><sub>2</sub>的交点为<em>M</em>，点<em>M</em>的轨迹为曲线<em>C</em>．  
（1）当*a*变化时，求曲线*C*的方程；  
（2）已知点*D*(2，0)，过点*E*(－2，0)的直线*l*与*C*交于*A*，*B*两点，求△*ABD*面积的最大值．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

<strong>[规范解答]</strong>　（1）由消去<em>a</em>，得曲线<em>C</em>的方程为＋<em>y</em><sup>2</sup>＝1(<em>y</em>≠－1，即点(0，－1)不在曲线<em>C</em>上)．  
（2）设<em>A</em>(<em>x</em><sub>1</sub>，<em>y</em><sub>1</sub>)，<em>B</em>(<em>x</em><sub>2</sub>，<em>y</em><sub>2</sub>)，<em>l</em>：<em>x</em>＝<em>my</em>－2，由得(<em>m</em><sup>2</sup>＋5)<em>y</em><sup>2</sup>－4<em>my</em>－1＝0，
则<em>y</em><sub>1</sub>＋<em>y</em><sub>2</sub>＝，<em>y</em><sub>1</sub><em>y</em><sub>2</sub>＝－，
故△<em>ABD</em>的面积<em>S</em>＝2|<em>y</em><sub>2</sub>－<em>y</em><sub>1</sub>|＝2＝2＝，
设*t*＝，*t*∈[1，＋∞)，则*S*＝＝≤，
当*t*＝，即*t*＝2，*m*＝±时，△*ABD*的面积取得最大值．

<strong>[例4]</strong>　(2019·全国Ⅱ)已知点<em>A</em>(－2，0)，<em>B</em>(2，0)，动点<em>M</em>(<em>x</em>，<em>y</em>)满足直线<em>AM</em>与<em>BM</em>的斜率之积为－．记<em>M</em>的轨迹为曲线<em>C</em>．  
（1）求*C*的方程，并说明*C*是什么曲线．  
（2）过坐标原点的直线交*C*于*P*，*Q*两点，点*P*在第一象限，*PE*⊥*x*轴，垂足为*E*，连接*QE*并延长交*C*于点*G*．

①证明：△*PQG*是直角三角形；
②求△*PQG*面积的最大值．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

<strong>[规范解答]</strong>　（1）由题设得·＝－，化简得＋＝1(|<em>x</em>|≠2)，
所以*C*为中心在坐标原点，焦点在*x*轴上的椭圆，不含左右顶点．  
（2）①设直线*PQ*的斜率为*k*，则其方程为*y*＝*kx*(*k*＞0)．由得*x*＝±．
设*u*＝，则*P*(*u*，*uk*)，*Q*(－*u*，－*uk*)，*E*(*u，* 0)．
于是直线*QG*的斜率为，方程为*y*＝(*x*－*u*)．由
得(2＋<em>k</em><sup>2</sup>)<em>x</em><sup>2</sup>－2<em>uk</em><sup>2</sup><em>x</em>＋<em>k</em><sup>2</sup><em>u</em><sup>2</sup>－8＝0．①
设<em>G</em>(<em>x<sub>G</sub></em>，<em>y<sub>G</sub></em>)，则－<em>u</em>和<em>x<sub>G</sub></em>是方程①的解，故<em>x<sub>G</sub></em>＝，由此得<em>y<sub>G</sub></em>＝．
从而直线*PG*的斜率为＝－．所以*PQ*⊥*PG*，即△*PQG*是直角三角形．

②由①得|*PQ*|＝2*u*，|*PG*|＝，
所以△*PQG*的面积*S*＝|*PQ*||*PG*|＝＝．
设*t*＝*k*＋，则由*k*＞0得*t*≥2，当且仅当*k*＝1时取等号．
因为*S*＝在[2，＋∞)单调递减，所以当*t*＝2，即*k*＝1时，*S*取得最大值，最大值为．
因此，△*PQG*面积的最大值为．

<strong>[例5]</strong>　已知抛物线<em>y</em><sup>2</sup>＝2<em>px</em>(<em>p</em>&gt;0)的准线经过椭圆＋＝1的一个焦点．  
（1）求抛物线的方程；  
（2）过抛物线焦点*F*的直线*l*与抛物线交于*A*，*B*两点(点*A*在*x*轴上方)，且满足＝2，若点*T*是抛物线的曲线段*AB*上的动点，求△*ABT*面积的最大值．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

<strong>[规范解答]</strong>　（1）因为椭圆＋＝1的左焦点为<em>F</em><sub>1</sub>(－1，0)，抛物线的准线为直线<em>x</em>＝－，
所以－＝－1，解得*p*＝2，
所以抛物线的方程为<em>y</em><sup>2</sup>＝4<em>x</em>．  
（2）设<em>A</em>(<em>x</em><sub>1</sub>，<em>y</em><sub>1</sub>)，<em>B</em>(<em>x</em><sub>2</sub>，<em>y</em><sub>2</sub>)，易知<em>y</em><sub>1</sub>&gt;0，<em>y</em><sub>2</sub>&lt;0，由＝2，得<em>y</em><sub>1</sub>＝－2<em>y</em><sub>2</sub>．

易知直线*l*的斜率存在且不为0．设直线*l*的方程为*x*＝*my*＋1(*m*≠0)，
由消去<em>x</em>整理，得<em>y</em><sup>2</sup>－4<em>my</em>－4＝0，易知<em>Δ</em>&gt;0，则<em>y</em><sub>1</sub>＋<em>y</em><sub>2</sub>＝4<em>m</em>，<em>y</em><sub>1</sub><em>y</em><sub>2</sub>＝－4，
所以－2<em>y</em>＝－4，即<em>y</em><sub>2</sub>＝－，则<em>y</em><sub>1</sub>＝2，所以<em>m</em>＝＝．
所以|*AB*|＝·＝× ＝×3＝．
解法一(切线法)：易知当△*ABT*面积最大时，点*T*为与直线*l*平行且与抛物线相切的切点．
设与直线<em>l</em>平行的直线方程为<em>x</em>＝<em>y</em>＋<em>t</em>，代入<em>y</em><sup>2</sup>＝4<em>x</em>得<em>y</em><sup>2</sup>－<em>y</em>－4<em>t</em>＝0．
令<em>Δ</em>＝(－)<sup>2</sup>－4(－4<em>t</em>)＝2＋16<em>t</em>＝0，解得<em>t</em>＝－，
则与直线<em>l</em>平行且与抛物线<em>y</em><sup>2</sup>＝4<em>x</em>相切的直线方程为<em>x</em>＝<em>y</em>－，即4<em>x</em>－<em>y</em>＋＝0．
又直线*l*的方程为4*x*－*y*－4＝0，
所以这两条平行直线间的距离为*d*＝＝．
所以△*ABT*面积的最大值*S*＝|*AB*|*d*＝××＝．
解法二(切点法)：设点*T*的坐标为，－<*n*<2，
则点*T*到直线*l*：4*x*－*y*－4＝0的距离为*d*＝＝，
当<em>n</em>＝时，<em>d</em><sub>max</sub>＝＝，此时点<em>T</em>的坐标为．
所以△<em>ABT</em>面积的最大值<em>S</em>＝|<em>AB</em>|<em>d</em><sub>max</sub>＝××＝．

【对点训练】

1．已知椭圆＋＝1(<em>a</em>&gt;<em>b</em>&gt;0)的左、右两个焦点分别为<em>F</em><sub>1</sub>，<em>F</em><sub>2</sub>，离心率<em>e</em>＝，短轴长为2．  
（1）求椭圆的方程；  
（2）点<em>A</em>为椭圆上的一动点(非长轴端点)，<em>AF</em><sub>2</sub>的延长线与椭圆交于<em>B</em>点，<em>AO</em>的延长线与椭圆交于<em>C</em>点，求△<em>ABC</em>面积的最大值．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

1．解析　（1）由题意得解得故椭圆的标准方程为＋<em>y</em><sup>2</sup>＝1．  
（2）①当直线*AB*的斜率不存在时，不妨取*A*，*B*，*C*，
故<em>S</em><sub>△</sub><em><sub>ABC</sub></em>＝×2×＝．

②当直线*AB*的斜率存在时，设直线*AB*的方程为*y*＝*k*(*x*－1)，联立方程消去*y*，
化简得(2<em>k</em><sup>2</sup>＋1)<em>x</em><sup>2</sup>－4<em>k</em><sup>2</sup><em>x</em>＋2<em>k</em><sup>2</sup>－2＝0，
设<em>A</em>(<em>x</em><sub>1</sub>，<em>y</em><sub>1</sub>)，<em>B</em>(<em>x</em><sub>2</sub>，<em>y</em><sub>2</sub>)，则<em>x</em><sub>1</sub>＋<em>x</em><sub>2</sub>＝，<em>x</em><sub>1</sub><em>x</em><sub>2</sub>＝，

|*AB*|＝＝ ＝2·，

点*O*到直线*kx*－*y*－*k*＝0的距离*d*＝＝，∵*O*是线段*AC*的中点，
∴点*C*到直线*AB*的距离为2*d*＝，
∴<em>S</em><sub>△</sub><em><sub>ABC</sub></em>＝|<em>AB</em>|·2<em>d</em>＝··＝2 ＝2 &lt;．

综上，△*ABC*面积的最大值为．

2．在平面直角坐标系*xOy*中，已知椭圆*C*：＋＝1(*a*＞*b*≥1)过点*P*(2，1)，且离心率*e*＝．  
（1）求椭圆*C*的方程；  
（2）直线*l*的斜率为，直线*l*与椭圆*C*交于*A*，*B*两点，求△*PAB*面积的最大值．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

2．解析　（1）∵<em>e</em><sup>2</sup>＝＝＝，∴<em>a</em><sup>2</sup>＝4<em>b</em><sup>2</sup>，又＋＝1，∴<em>a</em><sup>2</sup>＝8，<em>b</em><sup>2</sup>＝2．
故所求椭圆*C*的方程为＋＝1．  
（2）设<em>l</em>的方程为<em>y</em>＝<em>x</em>＋<em>m</em>，点<em>A</em>(<em>x</em><sub>1</sub>，<em>y</em><sub>1</sub>)，<em>B</em>(<em>x</em><sub>2</sub>，<em>y</em><sub>2</sub>)，联立消去<em>y</em>得<em>x</em><sup>2</sup>＋2<em>mx</em>＋2<em>m</em><sup>2</sup>－4＝0，

判别式<em>Δ</em>＝16－4<em>m</em><sup>2</sup>＞0，即<em>m</em><sup>2</sup>＜4，又<em>x</em><sub>1</sub>＋<em>x</em><sub>2</sub>＝－2<em>m</em>，<em>x</em><sub>1</sub>·<em>x</em><sub>2</sub>＝2<em>m</em><sup>2</sup>－4，
则|*AB*|＝×＝，

点*P*到直线*l*的距离*d*＝＝．
因此<em>S</em><sub>△</sub><em><sub>PAB</sub></em>＝<em>d</em>|<em>AB</em>|＝××＝≤＝2，
当且仅当<em>m</em><sup>2</sup>＝2即<em>m</em>＝±时上式等号成立，故△<em>PAB</em>面积的最大值为2．

3．已知椭圆<em>C</em>：＋＝1(<em>a</em>＞<em>b</em>＞0)的左、右焦点分别为<em>F</em><sub>1</sub>，<em>F</em><sub>2</sub>，点<em>P</em>(1，)在椭圆上，且有|<em>PF</em><sub>1</sub>|＋|<em>PF</em><sub>2</sub>|

＝2．  
（1）求椭圆*C*的标准方程；  
（2）过<em>F</em><sub>2</sub>的直线<em>l</em>与椭圆<em>C</em>交于<em>A</em>，<em>B</em>两点，求△<em>AOB</em>(<em>O</em>为坐标原点)面积的最大值．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

3．解析　（1）由|<em>PF</em><sub>1</sub>|＋|<em>PF</em><sub>2</sub>|＝2，得2<em>a</em>＝2，∴<em>a</em>＝，将<em>P</em>(1，)代入＋＝1，得<em>b</em><sup>2</sup>＝1．
∴椭圆<em>C</em>的标准方程为＋<em>y</em><sup>2</sup>＝1．  
（2）由已知，直线<em>l</em>的斜率为零时，不合题意，设直线<em>l</em>的方程为<em>x</em>－1＝<em>my</em>，<em>A</em>(<em>x</em><sub>1</sub>，<em>y</em><sub>1</sub>)，<em>B</em>(<em>x</em><sub>2</sub>，<em>y</em><sub>2</sub>)，
联立，得消去<em>x</em>化简整理得(<em>m</em><sup>2</sup>＋2)<em>y</em><sup>2</sup>＋2<em>my</em>－1＝0，
由根与系数的关系，得

<em>S</em><sub>△</sub><em><sub>AOB</sub></em>＝|<em>OF</em><sub>2</sub>|·|<em>y</em><sub>1</sub>－<em>y</em><sub>2</sub>|＝＝

＝×＝×＝×

≤×＝，当且仅当<em>m</em><sup>2</sup>＋1＝，即<em>m</em>＝0时，等号成立，
∴△*AOB*面积的最大值为．

4．已知抛物线<em>C</em><sub>1</sub>：<em>y</em><sup>2</sup>＝4<em>x</em>和<em>C</em><sub>2</sub>：<em>x</em><sup>2</sup>＝2<em>py</em>(<em>p</em>&gt;0)的焦点分别为<em>F</em><sub>1</sub>，<em>F</em><sub>2</sub>，点<em>P</em>(－1，－1)且<em>F</em><sub>1</sub><em>F</em><sub>2</sub>⊥<em>OP</em>(<em>O</em>为坐

标原点)．  
（1）求抛物线<em>C</em><sub>2</sub>的方程；  
（2）过点<em>O</em>的直线交<em>C</em><sub>1</sub>的下半部分于点<em>M</em>，交<em>C</em><sub>2</sub>的左半部分于点<em>N</em>，求△<em>PMN</em>面积的最小值．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

4．<strong>解析</strong>　（1）∵<em>F</em><sub>1</sub>(1，0)，<em>F</em><sub>2</sub>，∴＝，

·＝·(－1，－1)＝1－＝0，∴<em>p</em>＝2，∴抛物线<em>C</em><sub>2</sub>的方程为<em>x</em><sup>2</sup>＝4<em>y</em>．  
（2）设过点<em>O</em>的直线<em>MN</em>的方程为<em>y</em>＝<em>kx</em>(<em>k</em>&lt;0)，联立得(<em>kx</em>)<sup>2</sup>＝4<em>x</em>，解得<em>M</em>，
联立得<em>N</em>(4<em>k</em>，4<em>k</em><sup>2</sup>)，从而|<em>MN</em>|＝＝，

点*P*到直线*MN*的距离*d*＝，
所以<em>S</em><sub>△</sub><em><sub>PMN</sub></em>＝··＝＝＝2，
令<em>t</em>＝<em>k</em>＋(<em>t</em>≤－2)．则<em>S</em><sub>△</sub><em><sub>PMN</sub></em>＝2(<em>t</em>－2)(<em>t</em>＋1)，
当<em>t</em>＝－2，即<em>k</em>＝－1时，<em>S</em><sub>△</sub><em><sub>PMN</sub></em>取得最小值，最小值为8．
即当过原点的直线方程为*y*＝－*x*时，

△*PMN*的面积取得最小值8．

5．已知椭圆*M*：＋＝1(*a*>*b*>0)，其短轴的一个端点到右焦点的距离为2，且点*A*(，1)在椭圆*M*上．直

线*l*的斜率为，且与椭圆*M*交于*B*，*C*两点．  
（1）求椭圆*M*的方程：  
（2）求△*ABC*面积的最大值．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

5．解析　（1）由题意知解得*b*＝．故所求椭圆*M*的方程为＋＝1．  
（2）设直线<em>l</em>的方程为<em>y</em>＝<em>x</em>＋<em>m</em>，则<em>m</em>≠0．设<em>B</em>(<em>x</em><sub>1</sub>，<em>y</em><sub>1</sub>)，<em>C</em>(<em>x</em><sub>2</sub>，<em>y</em><sub>2</sub>)，

把直线<em>l</em>的方程代入椭圆方程并化简得<em>x</em><sup>2</sup>＋<em>mx</em>＋<em>m</em><sup>2</sup>－2＝0，
由<em>Δ</em>＝2<em>m</em><sup>2</sup>－4(<em>m</em><sup>2</sup>－2)＝2(4－<em>m</em><sup>2</sup>)&gt;0，可得0&lt;<em>m</em><sup>2</sup>&lt;4．①
∴<em>x</em><sub>1</sub>＝，<em>x</em><sub>2</sub>＝．
故|<em>BC</em>|＝|<em>x</em><sub>1</sub>－<em>x</em><sub>2</sub>|＝×＝，
又点*A*到边*BC*的距离为*d*＝，
故<em>S</em><sub>△</sub><em><sub>ABC</sub></em>＝|<em>BC</em>|·<em>d</em>＝×＝×≤×＝，
当且仅当<em>m</em><sup>2</sup>＝4－<em>m</em><sup>2</sup>，即<em>m</em>＝±时取等号，满足①式．∴△<em>ABC</em>面积的最大值为．

6．在平面直角坐标系*xOy*中，椭圆*C*：＋＝1(*a*>*b*>0)的离心率*e*＝，且点*P*(2，1)在椭圆*C*上．  
（1）求椭圆*C*的方程；  
（2）斜率为－1的直线与椭圆*C*相交于*A*，*B*两点，求△*AOB*面积的最大值．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

6．解析　（1）由题意得∴∴椭圆*C*的方程为＋＝1．  
（2）设直线<em>AB</em>的方程为<em>y</em>＝－<em>x</em>＋<em>m</em>，联立得3<em>x</em><sup>2</sup>－4<em>mx</em>＋2<em>m</em><sup>2</sup>－6＝0，
∴∴|<em>AB</em>|＝|<em>x</em><sub>1</sub>－<em>x</em><sub>2</sub>|＝，原点到直线的距离<em>d</em>＝．
∴<em>S</em><sub>△</sub><em><sub>OAB</sub></em>＝×·＝≤·＝．
当且仅当*m*＝±时，等号成立，∴△*AOB*面积的最大值为．

