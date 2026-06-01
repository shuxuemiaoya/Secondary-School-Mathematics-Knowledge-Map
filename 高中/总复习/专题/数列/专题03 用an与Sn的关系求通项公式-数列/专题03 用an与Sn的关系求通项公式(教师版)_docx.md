<strong>专题03　用</strong><em><strong>a<sub>n</sub></strong></em><strong>与</strong><em><strong>S<sub>n</sub></strong></em><strong>的关系求通项公式</strong>

![](images/fb8a33f384c4ee2af37ac35c3d7650420086072eda9f79751cee2a0172a64519.jpg)

【基本知识】

<em>S<sub>n</sub></em>与<em>a<sub>n</sub></em>的关系

已知数列{<em>a<sub>n</sub></em>}的前<em>n</em>项和为<em>S<sub>n</sub></em>，则<em>a<sub>n</sub></em>＝这个关系式对任意数列均成立．

注意：<em>S<sub>n</sub></em>与<em>a<sub>n</sub></em>关系的二重性，即用<em>S<sub>n</sub></em>与<em>a<sub>n</sub></em>关系可消去<em>a<sub>n</sub></em>，也可消去<em>S<sub>n</sub></em>．（1）正用<em>a<sub>n</sub></em>＝<em>S<sub>n</sub></em>－<em>S<sub>n</sub></em><sub>－1</sub>(<em>n</em>≥2)消去<em>a<sub>n</sub></em>转化为只含<em>S<sub>n</sub></em>，<em>S<sub>n</sub></em><sub>－1</sub>的关系式．（2）逆用<em>S<sub>n</sub></em>－<em>S<sub>n</sub></em><sub>－1</sub>＝<em>a<sub>n</sub></em>(<em>n</em>≥2)消去<em>S<sub>n</sub></em>转化为只含<em>a<sub>n</sub></em>，<em>a<sub>n</sub></em><sub>－1</sub>的关系式，再求解．

提醒：利用<em>a<sub>n</sub></em>＝<em>S<sub>n</sub></em>－<em>S<sub>n</sub></em><sub>－1</sub>求通项时，应注意<em>n</em>≥2这一前提条件，易忽视验证<em>n</em>＝1致误．

<strong>考点一　由</strong><em><strong>S<sub>n</sub></strong></em><strong>＝</strong><em><strong>f</strong></em><strong>(</strong><em><strong>n</strong></em><strong>)求</strong><em><strong>a<sub>n</sub></strong></em><strong>型</strong>

【基本方法】

已知<em><strong>S<sub>n</sub></strong></em><strong>＝</strong><em><strong>f</strong></em><strong>(</strong><em><strong>n</strong></em><strong>)</strong>求<em>a<sub>n</sub></em>的方法

已知<em>S<sub>n</sub></em>＝<em>f</em>(<em>n</em>)求<em>a<sub>n</sub></em>的常用方法是利用<em>a<sub>n</sub></em>＝主要分三个步骤完成：  
（1）当<em>n</em>＝1时，在<em>S<sub>n</sub></em>＝<em>f</em>(<em>n</em>)中，令<em>n</em>＝1，求得<em>a</em><sub>1</sub>＝<em>f</em>（1）；  
（2）当<em>n</em>≥2时，再利用<em>a<sub>n</sub></em>＝<em>S<sub>n</sub></em>－<em>S<sub>n</sub></em><sub>－1</sub>＝<em>f</em>(<em>n</em>)－<em>f</em>(<em>n</em>－1) (<em>n</em>≥2)，求出<em>a<sub>n</sub></em>＝<em>f</em>(<em>n</em>)－<em>f</em>(<em>n</em>－1)．即当<em>n</em>≥2，<em>n</em>∈<strong>N</strong><sup>\*</sup>时的通项公式；  
（3）检查<em>a</em><sub>1</sub>是否符合<em>n</em>≥2时<em>a<sub>n</sub></em>的表达式，如果符合，则可以把数列的通项公式合写成<em>a<sub>n</sub></em>＝<em>f</em>(<em>n</em>)－<em>f</em>(<em>n</em>－1)；否则应写成分段的形式，即<em>a<sub>n</sub></em>＝

【基本题型】

<strong>[例1]</strong> （1）已知数列{<em>a<sub>n</sub></em>}的前<em>n</em>项和<em>S<sub>n</sub></em>＝<em>n</em><sup>2</sup>＋2<em>n</em>，则<em>a<sub>n</sub></em>＝\_\_\_\_\_\_\_\_．
答案　2<em>n</em>＋1　解析　当<em>n</em>＝1时，<em>a</em><sub>1</sub>＝<em>S</em><sub>1</sub>＝3．当<em>n</em>≥2时，<em>a<sub>n</sub></em>＝<em>S<sub>n</sub></em>－<em>S<sub>n</sub></em><sub>－1</sub>＝<em>n</em><sup>2</sup>＋2<em>n</em>－[(<em>n</em>－1)<sup>2</sup>＋2(<em>n</em>－1)]＝2<em>n</em>＋1．由于<em>a</em><sub>1</sub>＝3适合上式，∴<em>a<sub>n</sub></em>＝2<em>n</em>＋1．  
（2）已知数列{<em>a<sub>n</sub></em>}的前<em>n</em>项和<em>S<sub>n</sub></em>＝<em>n</em><sup>2</sup>＋2<em>n</em>＋1(<em>n</em>∈<strong>N</strong><sup>\*</sup>)，则<em>a<sub>n</sub></em>＝\_\_\_\_\_\_\_\_；
答案　　解析　当<em>n</em>≥2时，<em>a<sub>n</sub></em>＝<em>S<sub>n</sub></em>－<em>S<sub>n</sub></em><sub>－1</sub>＝2<em>n</em>＋1；当<em>n</em>＝1时，<em>a</em><sub>1</sub>＝<em>S</em><sub>1</sub>＝4≠2×1＋1．因此<em>a<sub>n</sub></em>＝  
（3）已知数列{<em>a<sub>n</sub></em>}的前<em>n</em>项和<em>S<sub>n</sub></em>＝3<em><sup>n</sup></em>＋1，则<em>a<sub>n</sub></em>＝\_\_\_\_\_\_\_\_．
答案　　解析　当<em>n</em>＝1时，<em>a</em><sub>1</sub>＝<em>S</em><sub>1</sub>＝3＋1＝4；当<em>n</em>≥2时，<em>a<sub>n</sub></em>＝<em>S<sub>n</sub></em>－<em>S<sub>n</sub></em><sub>－1</sub>＝(3<em><sup>n</sup></em>＋1)－(3<em><sup>n</sup></em><sup>－1</sup>＋1)＝2×3<em><sup>n</sup></em><sup>－1</sup>．当<em>n</em>＝1时，2×3<sup>1－1</sup>＝2≠<em>a</em><sub>1</sub>，所以<em>a<sub>n</sub></em>＝

【对点精练】

1．已知数列{<em>a<sub>n</sub></em>}的前<em>n</em>项和<em>S<sub>n</sub></em>＝2<em>n</em><sup>2</sup>－3<em>n</em>，则<em>a<sub>n</sub></em>＝\_\_\_\_\_\_\_\_．

1．答案　4<em>n</em>－5　解析　<em>a</em><sub>1</sub>＝<em>S</em><sub>1</sub>＝2－3＝－1，当<em>n</em>≥2时，<em>a<sub>n</sub></em>＝<em>S<sub>n</sub></em>－<em>S<sub>n</sub></em><sub>－1</sub>＝(2<em>n</em><sup>2</sup>－3<em>n</em>)－[2(<em>n</em>－1)<sup>2</sup>－3(<em>n</em>－1)]＝

4<em>n</em>－5，由于<em>a</em><sub>1</sub>也适合此等式，∴<em>a<sub>n</sub></em>＝4<em>n</em>－5．

2．若数列{<em>a<sub>n</sub></em>}的前<em>n</em>项和<em>S<sub>n</sub></em>＝3<em>n</em><sup>2</sup>－2<em>n</em>＋1，则数列{<em>a<sub>n</sub></em>}的通项公式<em>a<sub>n</sub></em>＝\_\_\_\_\_\_\_\_．

2．答案　　解析　当<em>n</em>＝1时，<em>a</em><sub>1</sub>＝<em>S</em><sub>1</sub>＝3×1<sup>2</sup>－2×1＋1＝2；当<em>n</em>≥2时，<em>a<sub>n</sub></em>＝<em>S<sub>n</sub></em>－<em>S<sub>n</sub></em><sub>－1</sub>＝3<em>n</em><sup>2</sup>

－2<em>n</em>＋1－[3(<em>n</em>－1)<sup>2</sup>－2(<em>n</em>－1)＋1]＝6<em>n</em>－5，显然当<em>n</em>＝1时，不满足上式．故数列的通项公式为<em>a<sub>n</sub></em>＝

3．若<em>S<sub>n</sub></em>＝3<em><sup>n</sup></em>＋2<em>n</em>＋1，则数列{<em>a<sub>n</sub></em>}的通项公式为\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_．

3．答案　<em>a<sub>n</sub></em>＝　解析　因为当<em>n</em>＝1时，<em>a</em><sub>1</sub>＝<em>S</em><sub>1</sub>＝6；当<em>n</em>≥2时，<em>a<sub>n</sub></em>＝<em>S<sub>n</sub></em>－<em>S<sub>n</sub></em><sub>－1</sub>＝(3<em><sup>n</sup></em>＋2<em>n</em>

＋1)－[3<em><sup>n</sup></em><sup>－1</sup>＋2(<em>n</em>－1)＋1]＝2·3<em><sup>n</sup></em><sup>－1</sup>＋2，由于<em>a</em><sub>1</sub>不适合此式，所以<em>a<sub>n</sub></em>＝

4．已知<em>S<sub>n</sub></em>为数列{<em>a<sub>n</sub></em>}的前<em>n</em>项和，且log<sub>2</sub>(<em>S<sub>n</sub></em>＋1)＝<em>n</em>＋1，则数列{<em>a<sub>n</sub></em>}的通项公式为\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_．

4．答案　<em>a<sub>n</sub></em>＝　解析　由log<sub>2</sub>(<em>S<sub>n</sub></em>＋1)＝<em>n</em>＋1，得<em>S<sub>n</sub></em>＋1＝2<em><sup>n</sup></em><sup>＋1</sup>，当<em>n</em>＝1时，<em>a</em><sub>1</sub>＝<em>S</em><sub>1</sub>＝3；当<em>n</em>≥2

时，<em>a<sub>n</sub></em>＝<em>S<sub>n</sub></em>－<em>S<sub>n</sub></em><sub>－1</sub>＝2<em><sup>n</sup></em>，所以数列{<em>a<sub>n</sub></em>}的通项公式为<em>a<sub>n</sub></em>＝

5．已知数列{<em>a<sub>n</sub></em>}的前<em>n</em>项和<em>S<sub>n</sub></em>＝2<em>n</em><sup>2</sup>＋2<em>n</em>，数列{<em>b<sub>n</sub></em>}的前<em>n</em>项和<em>T<sub>n</sub></em>＝2－<em>b<sub>n</sub></em>．  
（1）求数列{<em>a<sub>n</sub></em>}与{<em>b<sub>n</sub></em>}的通项公式；  
（2）设<em>c<sub>n</sub></em>＝<em>a</em>·<em>b<sub>n</sub></em>，证明：当且仅当<em>n</em>≥3时，<em>c<sub>n</sub></em><sub>＋1</sub>＜<em>c<sub>n</sub></em>．

5．解析　（1）当<em>n</em>＝1时，<em>a</em><sub>1</sub>＝<em>S</em><sub>1</sub>＝4．

对于<em>n</em>≥2，有<em>a<sub>n</sub></em>＝<em>S<sub>n</sub></em>－<em>S<sub>n</sub></em><sub>－1</sub>＝2<em>n</em>(<em>n</em>＋1)－2(<em>n</em>－1)<em>n</em>＝4<em>n</em>．又当<em>n</em>＝1时，<em>a</em><sub>1</sub>＝4适合上式，
故{<em>a<sub>n</sub></em>}的通项公式<em>a<sub>n</sub></em>＝4<em>n</em>．将<em>n</em>＝1代入<em>T<sub>n</sub></em>＝2－<em>b<sub>n</sub></em>，得<em>b</em><sub>1</sub>＝2－<em>b</em><sub>1</sub>，故<em>T</em><sub>1</sub>＝<em>b</em><sub>1</sub>＝1．

对于<em>n</em>≥2，由<em>T<sub>n</sub></em><sub>－1</sub>＝2－<em>b<sub>n</sub></em><sub>－1</sub>，<em>T<sub>n</sub></em>＝2－<em>b<sub>n</sub></em>，得<em>b<sub>n</sub></em>＝<em>T<sub>n</sub></em>－<em>T<sub>n</sub></em><sub>－1</sub>＝－(<em>b<sub>n</sub></em>－<em>b<sub>n</sub></em><sub>－1</sub>)，<em>b<sub>n</sub></em>＝<em>b<sub>n</sub></em><sub>－1</sub>，
所以数列{<em>b<sub>n</sub></em>}是以1为首项，为公比的等比数列，故<em>b<sub>n</sub></em>＝2<sup>1－</sup><em><sup>n</sup></em>．  
（2）法一　由<em>c<sub>n</sub></em>＝<em>a</em>·<em>b<sub>n</sub></em>＝<em>n</em><sup>2</sup>2<sup>5－</sup><em><sup>n</sup></em>，得＝<sup>2</sup>．
当且仅当<em>n</em>≥3时，1＋≤＜，即&lt;1，即<em>c<sub>n</sub></em><sub>＋1</sub>＜<em>c<sub>n</sub></em>．

法二　由<em>c<sub>n</sub></em>＝<em>a</em>·<em>b<sub>n</sub></em>＝<em>n</em><sup>2</sup>2<sup>5－</sup><em><sup>n</sup></em>，得<em>c<sub>n</sub></em><sub>＋1</sub>－<em>c<sub>n</sub></em>＝2<sup>4－</sup><em><sup>n</sup></em>[(<em>n</em>＋1)<sup>2</sup>－2<em>n</em><sup>2</sup>]＝2<sup>4－</sup><em><sup>n</sup></em>[－(<em>n</em>－1)<sup>2</sup>＋2]．
当且仅当<em>n</em>≥3时，<em>c<sub>n</sub></em><sub>＋1</sub>－<em>c<sub>n</sub></em>＜0，即<em>c<sub>n</sub></em><sub>＋1</sub>＜<em>c<sub>n</sub></em>．

<strong>考点二　由</strong><em><strong>a</strong></em><strong><sub>1</sub>＋</strong><em><strong>a</strong></em><strong><sub>2</sub>＋</strong><em><strong>a</strong></em><strong><sub>3</sub>＋…＋</strong><em><strong>a<sub>n</sub></strong></em><strong>＝</strong><em><strong>f</strong></em><strong>(</strong><em><strong>n</strong></em><strong>)求</strong><em><strong>a<sub>n</sub></strong></em><strong>型</strong>

【基本方法】

已知<em>S<sub>n</sub></em>求<em>a<sub>n</sub></em>的方法

已知<em>a</em><sub>1</sub>＋<em>a</em><sub>2</sub>＋<em>a</em><sub>3</sub>＋…＋<em>a<sub>n</sub></em>＝<em>f</em>(<em>n</em>)求<em>a<sub>n</sub></em>的常用方法是利用<em>a<sub>n</sub></em>＝主要分三个步骤完成：  
（1）当<em>n</em>＝1时，求得<em>a</em><sub>1</sub>＝<em>f</em>（1）；  
（2）当<em>n</em>≥2时，在<em>a</em><sub>1</sub>＋<em>a</em><sub>2</sub>＋<em>a</em><sub>3</sub>＋…＋<em>a<sub>n</sub></em>＝<em>f</em>(<em>n</em>)中用<em>n</em>－1替换<em>n</em>得到一个新的关系式<em>a</em><sub>1</sub>＋<em>a</em><sub>2</sub>＋<em>a</em><sub>3</sub>＋…＋<em>a<sub>n</sub></em><sub>－1</sub>＝<em>f</em>(<em>n</em>－1)，两式相减得到<em>a<sub>n</sub></em>＝<em>f</em>(<em>n</em>)－<em>f</em>(<em>n</em>－1) (<em>n</em>≥2)，便可求出当<em>n</em>≥2，<em>n</em>∈<strong>N</strong><sup>\*</sup>时的通项公式；  
（3）检查<em>a</em><sub>1</sub>是否符合<em>n</em>≥2时<em>a<sub>n</sub></em>的表达式，如果符合，则可以把数列的通项公式合写成<em>a<sub>n</sub></em>＝<em>f</em>(<em>n</em>)－<em>f</em>(<em>n</em>－1)；否则应写成分段的形式，即<em>a<sub>n</sub></em>＝

【基本题型】

<strong>[例2]</strong> （1）已知正项数列{<em>a<sub>n</sub></em>}中，＋＋…＋＝，则数列{<em>a<sub>n</sub></em>}的通项公式为(　　)

A．<em>a<sub>n</sub></em>＝<em>n</em>　　　　　
B．<em>a<sub>n</sub></em>＝<em>n</em><sup>2</sup>　　　　　
C．<em>a<sub>n</sub></em>＝ 　　　　　
D．<em>a<sub>n</sub></em>＝
答案　B　解析　当<em>n</em>＝1时，＝＝1，<em>a</em><sub>1</sub>＝1．当<em>n</em>≥2时，∵＋＋…＋＝，∴＋＋…＋＝，两式相减得＝－＝<em>n</em>(<em>n</em>≥2)，∴<em>a<sub>n</sub></em>＝<em>n</em><sup>2</sup>(<em>n</em>≥2)，①，又当<em>n</em>＝1时，<em>a</em><sub>1</sub>＝1，适合①式，∴<em>a<sub>n</sub></em>＝<em>n</em><sup>2</sup>，<em>n</em>∈<strong>N</strong><sup>\*</sup>．故选B．  
（2）已知数列{<em>a<sub>n</sub></em>}满足<em>a</em><sub>1</sub>＋2<em>a</em><sub>2</sub>＋3<em>a</em><sub>3</sub>＋…＋<em>na<sub>n</sub></em>＝2<em><sup>n</sup></em>，则<em>a<sub>n</sub></em>＝\_\_\_\_\_\_\_\_．
答案　　解析　当<em>n</em>＝1时，<em>a</em><sub>1</sub>＝2<sup>1</sup>＝2，∵<em>a</em><sub>1</sub>＋2<em>a</em><sub>2</sub>＋3<em>a</em><sub>3</sub>＋…＋<em>na<sub>n</sub></em>＝2<em><sup>n</sup></em>，①，故<em>a</em><sub>1</sub>＋2<em>a</em><sub>2</sub>＋3<em>a</em><sub>3</sub>＋…＋(<em>n</em>－1)<em>a<sub>n</sub></em><sub>－1</sub>＝2<em><sup>n</sup></em><sup>－1</sup>(<em>n</em>≥2)，②，由①－②得<em>na<sub>n</sub></em>＝2<em><sup>n</sup></em>－2<em><sup>n</sup></em><sup>－1</sup>＝2<em><sup>n</sup></em><sup>－1</sup>，∴<em>a<sub>n</sub></em>＝(<em>n</em>≥2)．显然当<em>n</em>＝1时不满足上式，∴<em>a<sub>n</sub></em>＝

<strong>[例3]</strong>　记<em>m</em>＝，若{<em>d<sub>n</sub></em>}是等差数列，则称<em>m</em>为数列{<em>a<sub>n</sub></em>}的“<em>d<sub>n</sub></em>等差均值”；若{<em>d<sub>n</sub></em>}是等比数列，则称<em>m</em>为数列{<em>a<sub>n</sub></em>}的“<em>d<sub>n</sub></em>等比均值”．已知数列{<em>a<sub>n</sub></em>}的“2<em>n</em>－1等差均值”为2，数列{<em>b<sub>n</sub></em>}的“3<em><sup>n</sup></em><sup>－1</sup>等比均值”为3．记<em>c<sub>n</sub></em>＝＋<em>k</em>log<sub>3</sub><em>b<sub>n</sub></em>，数列{<em>c<sub>n</sub></em>}的前<em>n</em>项和为<em>S<sub>n</sub></em>，若对任意的正整数<em>n</em>都有<em>S<sub>n</sub></em>≤<em>S</em><sub>6</sub>，求实数<em>k</em>的取值范围．
解析　由题意得2＝，所以<em>a</em><sub>1</sub>＋3<em>a</em><sub>2</sub>＋…＋(2<em>n</em>－1)<em>a<sub>n</sub></em>＝2<em>n</em>，
所以<em>a</em><sub>1</sub>＋3<em>a</em><sub>2</sub>＋…＋(2<em>n</em>－3)<em>a<sub>n</sub></em><sub>－1</sub>＝2<em>n</em>－2(<em>n</em>≥2，<em>n</em>∈<strong>N</strong><sub>＋</sub>)，

两式相减得<em>a<sub>n</sub></em>＝(<em>n</em>≥2，<em>n</em>∈<strong>N</strong><sub>＋</sub>)．
当<em>n</em>＝1时，<em>a</em><sub>1</sub>＝2，符合上式，所以<em>a<sub>n</sub></em>＝(<em>n</em>∈<strong>N</strong><sub>＋</sub>)．
又由题意得3＝，所以<em>b</em><sub>1</sub>＋3<em>b</em><sub>2</sub>＋…＋3<em><sup>n</sup></em><sup>－1</sup><em>b<sub>n</sub></em>＝3<em>n</em>，
所以<em>b</em><sub>1</sub>＋3<em>b</em><sub>2</sub>＋…＋3<em><sup>n</sup></em><sup>－2</sup><em>b<sub>n</sub></em><sub>－1</sub>＝3<em>n</em>－3(<em>n</em>≥2，<em>n</em>∈<strong>N</strong><sub>＋</sub>)，

两式相减得<em>b<sub>n</sub></em>＝3<sup>2－</sup><em><sup>n</sup></em>(<em>n</em>≥2，<em>n</em>∈<strong>N</strong><sub>＋</sub>)．
当<em>n</em>＝1时，<em>b</em><sub>1</sub>＝3，符合上式，所以<em>b<sub>n</sub></em>＝3<sup>2－</sup><em><sup>n</sup></em>(<em>n</em>∈<strong>N</strong><sub>＋</sub>)．
所以<em>c<sub>n</sub></em>＝(2－<em>k</em>)<em>n</em>＋2<em>k</em>－1．
因为对任意的正整数<em>n</em>都有<em>S<sub>n</sub></em>≤<em>S</em><sub>6</sub>，所以解得≤<em>k</em>≤，
所以实数*k*的取值范围为．

【对点精练】

1．已知数列{<em>a<sub>n</sub></em>}满足<em>a</em><sub>1</sub>＋2<em>a</em><sub>2</sub>＋3<em>a</em><sub>3</sub>＋…＋<em>na<sub>n</sub></em>＝<em>n</em>＋1(<em>n</em>∈<strong>N</strong><sup>\*</sup>)，则数列{<em>a<sub>n</sub></em>}的通项公式为\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_．

1．答案　<em>a<sub>n</sub></em>＝　解析　已知<em>a</em><sub>1</sub>＋2<em>a</em><sub>2</sub>＋3<em>a</em><sub>3</sub>＋…＋<em>na<sub>n</sub></em>＝<em>n</em>＋1，将<em>n</em>＝1代入，得<em>a</em><sub>1</sub>＝2；当<em>n</em>≥2

时，将<em>n</em>－1代入得<em>a</em><sub>1</sub>＋2<em>a</em><sub>2</sub>＋3<em>a</em><sub>3</sub>＋…＋(<em>n</em>－1)<em>a<sub>n</sub></em><sub>－1</sub>＝<em>n</em>，两式相减得<em>na<sub>n</sub></em>＝(<em>n</em>＋1)－<em>n</em>＝1，∴<em>a<sub>n</sub></em>＝，∴<em>a<sub>n</sub></em>＝

2．设数列{<em>a<sub>n</sub></em>}满足<em>a</em><sub>1</sub>＋3<em>a</em><sub>2</sub>＋…＋(2<em>n</em>－1)<em>a<sub>n</sub></em>＝2<em><sup>n</sup></em>，则<em>a<sub>n</sub></em>＝\_\_\_\_\_\_\_\_．

2．答案　　解析　当<em>n</em>＝1时，<em>a</em><sub>1</sub>＝2<sup>1</sup>＝2．∵<em>a</em><sub>1</sub>＋3<em>a</em><sub>2</sub>＋…＋(2<em>n</em>－1)<em>a<sub>n</sub></em>＝2<em><sup>n</sup></em>，①，∴<em>a</em><sub>1</sub>＋3<em>a</em><sub>2</sub>

＋…＋(2<em>n</em>－3)<em>a<sub>n</sub></em><sub>－1</sub>＝2<em><sup>n</sup></em><sup>－1</sup>(<em>n</em>≥2)，②，由①－②得，(2<em>n</em>－1)·<em>a<sub>n</sub></em>＝2<em><sup>n</sup></em>－2<em><sup>n</sup></em><sup>－1</sup>＝2<em><sup>n</sup></em><sup>－1</sup>，∴<em>a<sub>n</sub></em>＝(<em>n</em>≥2)．显然<em>n</em>＝1时不满足上式，∴<em>a<sub>n</sub></em>＝

3．已知数列{<em>a<sub>n</sub></em>}满足2<em>a</em><sub>1</sub>＋2<sup>2</sup><em>a</em><sub>2</sub>＋2<sup>3</sup><em>a</em><sub>3</sub>＋…＋2<em><sup>n</sup>a<sub>n</sub></em>＝4<em><sup>n</sup></em>－1，则{<em>a<sub>n</sub></em>}的通项公式是\_\_\_\_\_\_\_\_．

3．答案　<em>a<sub>n</sub></em>＝·2<em><sup>n</sup></em>　解析　因为数列{<em>a<sub>n</sub></em>}满足2<em>a</em><sub>1</sub>＋2<sup>2</sup><em>a</em><sub>2</sub>＋2<sup>3</sup><em>a</em><sub>3</sub>＋…＋2<em><sup>n</sup>a<sub>n</sub></em>＝4<em><sup>n</sup></em>－1，所以当<em>n</em>＝1时，2<em>a</em><sub>1</sub>＝4

－1，解得<em>a</em><sub>1</sub>＝；当<em>n</em>≥2时，2<em>a</em><sub>1</sub>＋2<sup>2</sup><em>a</em><sub>2</sub>＋2<sup>3</sup><em>a</em><sub>3</sub>＋…＋2<em><sup>n</sup></em><sup>－1</sup><em>a<sub>n</sub></em><sub>－1</sub>＝4<em><sup>n</sup></em><sup>－1</sup>－1，与题目条件中的等式相减，得到2<em><sup>n</sup>a<sub>n</sub></em>＝4<em><sup>n</sup></em>－4<em><sup>n</sup></em><sup>－1</sup>，整理得<em>a<sub>n</sub></em>＝·2<em><sup>n</sup></em>，该表达式对<em>n</em>＝1也成立，所以数列{<em>a<sub>n</sub></em>}的通项公式为<em>a<sub>n</sub></em>＝·2<em><sup>n</sup></em>．

<strong>考点三　由</strong><em><strong>f</strong></em><strong>(</strong><em><strong>a<sub>n</sub></strong></em><strong>，</strong><em><strong>S<sub>n</sub></strong></em><strong>)＝0消去</strong><em><strong>S<sub>n</sub></strong></em><strong>型</strong>

【基本方法】

已知<em>S<sub>n</sub></em>求<em>a<sub>n</sub></em>的方法

已知<em>f</em>(<em>a<sub>n</sub></em>，<em>S<sub>n</sub></em>)＝0求<em>a<sub>n</sub></em>，如果能消去<em>S<sub>n</sub></em>，则利用<em>a<sub>n</sub></em>＝消去<em>S<sub>n</sub></em>，主要分四个步骤完成：  
（1）当<em>n</em>＝1时，先利用<em>a</em><sub>1</sub>＝<em>S</em><sub>1</sub>，求得<em>a</em><sub>1</sub>；  
（2）当<em>n</em>≥2时，用<em>n</em>－1替换<em>f</em>(<em>a<sub>n</sub></em>，<em>S<sub>n</sub></em>)＝0中的<em>n</em>得到一个新的关系式<em>f</em>(<em>a<sub>n</sub></em><sub>－1</sub>，<em>S<sub>n</sub></em><sub>－1</sub>)＝0，两式相减，再逆用<em>a<sub>n</sub></em>＝<em>S<sub>n</sub></em>－<em>S<sub>n</sub></em><sub>－1</sub>(<em>n</em>≥2)便可得到当<em>n</em>≥2，<em>n</em>∈<strong>N</strong><sup>\*</sup>时数列{<em>a<sub>n</sub></em>}的一个递推公式；  
（3）借助各类递推公式求通项公式的方法求出当<em>n</em>≥2，<em>n</em>∈<strong>N</strong><sup>\*</sup>时的通项公式；  
（4）看<em>a</em><sub>1</sub>是否符合<em>n</em>≥2时<em>a<sub>n</sub></em>的表达式，如果符合，则可以把数列的通项公式合写；否则应写成分段的形式．

【基本题型】

<strong>[例4]</strong> （1）已知数列{<em>a<sub>n</sub></em>}的前<em>n</em>项和为<em>S<sub>n</sub></em>，且满足<em>a<sub>n</sub></em>＋<em>S<sub>n</sub></em>＝1(<em>n</em>∈<strong>N</strong><sup>\*</sup>)，则通项<em>a<sub>n</sub></em>＝\_\_\_\_\_\_\_\_．
答案　　解析　∵<em>a<sub>n</sub></em>＋<em>S<sub>n</sub></em>＝1，①，∴<em>a</em><sub>1</sub>＝，<em>a<sub>n</sub></em><sub>－1</sub>＋<em>S<sub>n</sub></em><sub>－1</sub>＝1(<em>n</em>≥2)，②，由①－②，得<em>a<sub>n</sub></em>－<em>a<sub>n</sub></em><sub>－1</sub>＋<em>a<sub>n</sub></em>＝0，即＝(<em>n</em>≥2)，∴数列{<em>a<sub>n</sub></em>}是首项为，公比为的等比数列，则<em>a<sub>n</sub></em>＝×＝．  
（2）(2013·全国Ⅰ)若数列{<em>a<sub>n</sub></em>}的前<em>n</em>项和<em>S<sub>n</sub></em>＝<em>a<sub>n</sub></em>＋，则{<em>a<sub>n</sub></em>}的通项公式是<em>a<sub>n</sub></em>＝\_\_\_\_\_\_\_\_．
答案　(－2)<em><sup>n</sup></em><sup>－1</sup>　解析　当<em>n</em>＝1时，<em>a</em><sub>1</sub>＝1；当<em>n</em>≥2时，<em>a<sub>n</sub></em>＝<em>S<sub>n</sub></em>－<em>S<sub>n</sub></em><sub>－1</sub>＝<em>a<sub>n</sub></em>－<em>a<sub>n</sub></em><sub>－1</sub>，故＝－2，故<em>a<sub>n</sub></em>＝(－2)<em><sup>n</sup></em><sup>－1</sup>．当<em>n</em>＝1时，也符合<em>a<sub>n</sub></em>＝(－2)<em><sup>n</sup></em><sup>－1</sup>．综上，<em>a<sub>n</sub></em>＝(－2)<em><sup>n</sup></em><sup>－1</sup>．  
（3）设数列{<em>a<sub>n</sub></em>}的前<em>n</em>项和为<em>S<sub>n</sub></em>，若<em>a</em><sub>1</sub>＝1，<em>a<sub>n</sub></em><sub>＋1</sub>＝<em>S<sub>n</sub></em>(<em>n</em>∈<strong>N</strong><sup>\*</sup>)，则通项公式<em>a<sub>n</sub></em>＝\_\_\_\_\_\_\_\_\_\_\_\_．
答案　　解析　由<em>a<sub>n</sub></em><sub>＋1</sub>＝<em>S<sub>n</sub></em>①，可得<em>a<sub>n</sub></em>＝<em>S<sub>n</sub></em><sub>－1</sub>(<em>n</em>≥2)②，①－②得<em>a<sub>n</sub></em><sub>＋1</sub>－<em>a<sub>n</sub></em>＝<em>S<sub>n</sub></em>－<em>S<sub>n</sub></em><sub>－1</sub>＝<em>a<sub>n</sub></em>(<em>n</em>≥2)，即＝2(<em>n</em>≥2)，又<em>a</em><sub>2</sub>＝<em>S</em><sub>1</sub>＝1，所以＝1≠2，则数列{<em>a<sub>n</sub></em>}从第二项起是以1为首项2为公比的等比数列，所以<em>a<sub>n</sub></em>＝  
（4）已知数列{<em>a<sub>n</sub></em>}的首项<em>a</em><sub>1</sub>＝1，前<em>n</em>项和为<em>S<sub>n</sub></em>，且<em>S<sub>n</sub></em><sub>＋1</sub>＝4<em>a<sub>n</sub></em>＋2(<em>n</em>∈<strong>N</strong><sup>\*</sup>)，则数列{<em>a<sub>n</sub></em>}的通项公式是<em>a<sub>n</sub></em>＝

\_\_\_\_\_\_\_\_．
答案　(3<em>n</em>－1)2<em><sup>n</sup></em><sup>－2</sup>　解析　当<em>n</em>≥2时，<em>S<sub>n</sub></em><sub>＋1</sub>＝4<em>a<sub>n</sub></em>＋2，<em>S<sub>n</sub></em>＝4<em>a<sub>n</sub></em><sub>－1</sub>＋2．两式相减，得<em>a<sub>n</sub></em><sub>＋1</sub>＝4<em>a<sub>n</sub></em>－4<em>a<sub>n</sub></em><sub>－1</sub>，将之变形为<em>a<sub>n</sub></em><sub>＋1</sub>－2<em>a<sub>n</sub></em>＝2(<em>a<sub>n</sub></em>－2<em>a<sub>n</sub></em><sub>－1</sub>)．所以{<em>a<sub>n</sub></em><sub>＋1</sub>－2<em>a<sub>n</sub></em>}是公比为2的等比数列．又<em>a</em><sub>1</sub>＋<em>a</em><sub>2</sub>＝<em>S</em><sub>2</sub>＝4<em>a</em><sub>1</sub>＋2，<em>a</em><sub>1</sub>＝1，得<em>a</em><sub>2</sub>＝5，则<em>a</em><sub>2</sub>－2<em>a</em><sub>1</sub>＝3．所以<em>a<sub>n</sub></em><sub>＋1</sub>－2<em>a<sub>n</sub></em>＝3·2<em><sup>n</sup></em><sup>－1</sup>．两边同除以2<em><sup>n</sup></em><sup>＋1</sup>，得－＝，所以是首项为＝，公差为的等差数列．所以＝＋(<em>n</em>－1)＝<em>n</em>－，所以<em>a<sub>n</sub></em>＝(3<em>n</em>－1)2<em><sup>n</sup></em><sup>－2</sup>．  
（5）若<em>S<sub>n</sub></em>为数列{<em>a<sub>n</sub></em>}的前<em>n</em>项和，且2<em>S<sub>n</sub></em>＝<em>a<sub>n</sub></em><sub>＋1</sub><em>a<sub>n</sub></em>，<em>a</em><sub>1</sub>＝4，则数列{<em>a<sub>n</sub></em>}的通项公式为<em>a<sub>n</sub></em>＝\_\_\_\_．
答案　　解析　因为2<em>S<sub>n</sub></em>＝<em>a<sub>n</sub></em><sub>＋1</sub><em>a<sub>n</sub></em>，<em>a</em><sub>1</sub>＝4，所以<em>n</em>＝1时，2×4＝4<em>a</em><sub>2</sub>，解得<em>a</em><sub>2</sub>＝2．<em>n</em>≥2时，2<em>S<sub>n</sub></em><sub>－1</sub>＝<em>a<sub>n</sub>a<sub>n</sub></em><sub>－1</sub>，可得2<em>a<sub>n</sub></em>＝<em>a<sub>n</sub></em><sub>＋1</sub><em>a<sub>n</sub></em>－<em>a<sub>n</sub>a<sub>n</sub></em><sub>－1</sub>，所以<em>a<sub>n</sub></em>＝0(舍去)或<em>a<sub>n</sub></em><sub>＋1</sub>－<em>a<sub>n</sub></em><sub>－1</sub>＝2．<em>n</em>≥2时，<em>a<sub>n</sub></em><sub>＋1</sub>－<em>a<sub>n</sub></em><sub>－1</sub>＝2，可得数列{<em>a<sub>n</sub></em>}的奇数项与偶数项分别为等差数列．所以<em>a</em><sub>2</sub><em><sub>k</sub></em><sub>－1</sub>＝4＋2(<em>k</em>－1)＝2<em>k</em>＋2，<em>k</em>∈<strong>N</strong><sup>\*</sup>，<em>a</em><sub>2</sub><em><sub>k</sub></em>＝2＋2(<em>k</em>－1)＝2<em>k</em>，<em>k</em>∈<strong>N</strong><sup>\*</sup>．所以<em>a<sub>n</sub></em>＝

<strong>[例5]</strong>　设数列{<em>a<sub>n</sub></em>}的前<em>n</em>项和为<em>S<sub>n</sub></em>，数列{<em>S<sub>n</sub></em>}的前<em>n</em>项和为<em>T<sub>n</sub></em>，满足<em>T<sub>n</sub></em>＝2<em>S<sub>n</sub></em>－<em>n</em><sup>2</sup>，<em>n</em>∈<strong>N</strong><sup>\*</sup>．  
（1）求<em>a</em><sub>1</sub>的值；  
（2）求数列{<em>a<sub>n</sub></em>}的通项公式．
解析　（1）令<em>n</em>＝1，<em>T</em><sub>1</sub>＝2<em>S</em><sub>1</sub>－1，∵<em>T</em><sub>1</sub>＝<em>S</em><sub>1</sub>＝<em>a</em><sub>1</sub>，∴<em>a</em><sub>1</sub>＝2<em>a</em><sub>1</sub>－1，∴<em>a</em><sub>1</sub>＝1．  
（2）<em>n</em>≥2时，则<em>S<sub>n</sub></em>＝<em>T<sub>n</sub></em>－<em>T<sub>n</sub></em><sub>－1</sub>＝2<em>S<sub>n</sub></em>－<em>n</em><sup>2</sup>－[2<em>S<sub>n</sub></em><sub>－1</sub>－(<em>n</em>－1)<sup>2</sup>]＝2(<em>S<sub>n</sub></em>－<em>S<sub>n</sub></em><sub>－1</sub>)－2<em>n</em>＋1＝2<em>a<sub>n</sub></em>－2<em>n</em>＋1．
因为当<em>n</em>＝1时，<em>a</em><sub>1</sub>＝<em>S</em><sub>1</sub>＝1也满足上式，所以<em>S<sub>n</sub></em>＝2<em>a<sub>n</sub></em>－2<em>n</em>＋1(<em>n</em>∈<strong>N</strong><sup>\*</sup>)，
当<em>n</em>≥2时，<em>S<sub>n</sub></em><sub>－1</sub>＝2<em>a<sub>n</sub></em><sub>－1</sub>－2(<em>n</em>－1)＋1，两式相减得<em>a<sub>n</sub></em>＝2<em>a<sub>n</sub></em>－2<em>a<sub>n</sub></em><sub>－1</sub>－2，
所以<em>a<sub>n</sub></em>＝2<em>a<sub>n</sub></em><sub>－1</sub>＋2(<em>n</em>≥2)，所以<em>a<sub>n</sub></em>＋2＝2(<em>a<sub>n</sub></em><sub>－1</sub>＋2)，
因为<em>a</em><sub>1</sub>＋2＝3≠0，所以数列{<em>a<sub>n</sub></em>＋2}是以3为首项，2为公比的等比数列．
所以<em>a<sub>n</sub></em>＋2＝3×2<em><sup>n</sup></em><sup>－1</sup>，所以<em>a<sub>n</sub></em>＝3×2<em><sup>n</sup></em><sup>－1</sup>－2，
当<em>n</em>＝1时也成立，所以<em>a<sub>n</sub></em>＝3×2<em><sup>n</sup></em><sup>－1</sup>－2．

【对点精练】

1．记<em>S<sub>n</sub></em>为数列{<em>a<sub>n</sub></em>}的前<em>n</em>项和．若<em>S<sub>n</sub></em>＝2<em>a<sub>n</sub></em>＋1，则<em>a<sub>n</sub></em>＝\_\_\_\_\_\_\_\_．

1．答案　－2<em><sup>n</sup></em><sup>－1</sup>　解析　∵<em>S<sub>n</sub></em>＝2<em>a<sub>n</sub></em>＋1，当<em>n</em>≥2时，<em>S<sub>n</sub></em><sub>－1</sub>＝2<em>a<sub>n</sub></em><sub>－1</sub>＋1，∴<em>a<sub>n</sub></em>＝<em>S<sub>n</sub></em>－<em>S<sub>n</sub></em><sub>－1</sub>＝2<em>a<sub>n</sub></em>－2<em>a<sub>n</sub></em><sub>－1</sub>，即<em>a<sub>n</sub></em>

＝2<em>a<sub>n</sub></em><sub>－1</sub>．当<em>n</em>＝1时，<em>a</em><sub>1</sub>＝<em>S</em><sub>1</sub>＝2<em>a</em><sub>1</sub>＋1，得<em>a</em><sub>1</sub>＝－1．∴数列{<em>a<sub>n</sub></em>}是首项<em>a</em><sub>1</sub>为－1，公比<em>q</em>为2的等比数列，∴<em>a<sub>n</sub></em>＝－1×2<em><sup>n</sup></em><sup>－1</sup>＝－2<em><sup>n</sup></em><sup>－1</sup>．

2．已知数列{<em>a<sub>n</sub></em>}的前<em>n</em>项和为<em>S<sub>n</sub></em>，若<em>S<sub>n</sub></em>＝2<em>a<sub>n</sub></em>－4，(<em>n</em>∈<strong>N</strong><sup>\*</sup>)，则<em>a<sub>n</sub></em>\_\_\_\_\_\_\_\_．

2．答案　2<em><sup>n</sup></em><sup>＋1</sup>　解析　当<em>n</em>≥2时，<em>S<sub>n</sub></em><sub>＋1</sub>＝2<em>a<sub>n</sub></em><sub>＋1</sub>－4，又由<em>S<sub>n</sub></em>＝2<em>a<sub>n</sub></em>－4可得<em>a<sub>n</sub></em><sub>＋1</sub>＝2<em>a<sub>n</sub></em><sub>＋1</sub>－2<em>a<sub>n</sub></em>，即<em>a<sub>n</sub></em><sub>＋1</sub>＝2<em>a<sub>n</sub></em>，

<em>a</em><sub>1</sub>＝<em>S</em><sub>1</sub>＝2<em>a</em><sub>1</sub>－4，得<em>a</em><sub>1</sub>＝4．所以<em>a<sub>n</sub></em>＝4·2<em><sup>n</sup></em><sup>－1</sup>＝2<em><sup>n</sup></em><sup>＋1</sup>．

3．已知数列{<em>a<sub>n</sub></em>}的前<em>n</em>项和为<em>S<sub>n</sub></em>，<em>a</em><sub>1</sub>＝1，<em>a<sub>n</sub></em><sub>＋1</sub>＝2<em>S<sub>n</sub></em>＋1，<em>n</em>∈<strong>N</strong><sup>\*</sup>，则数列{<em>a<sub>n</sub></em>}的通项公式是<em>a<sub>n</sub></em>＝\_\_\_\_\_\_\_\_．

3．答案　3<em><sup>n</sup></em><sup>－1</sup>　解析　因为<em>a<sub>n</sub></em><sub>＋1</sub>＝2<em>S<sub>n</sub></em>＋1，当<em>n</em>≥2时，<em>a<sub>n</sub></em>＝2<em>S<sub>n</sub></em><sub>－1</sub>＋1，两式相减得<em>a<sub>n</sub></em><sub>＋1</sub>－<em>a<sub>n</sub></em>＝2<em>a<sub>n</sub></em>，即<em>a<sub>n</sub></em>

<sub>＋1</sub>＝3<em>a<sub>n</sub></em>，又<em>a</em><sub>1</sub>＝1，<em>a</em><sub>2</sub>＝2<em>S</em><sub>1</sub>＋1＝3，所以＝3，从而{<em>a<sub>n</sub></em>}是首项为1，公比为3的等比数列，所以<em>a<sub>n</sub></em>＝3<em><sup>n</sup></em><sup>－1</sup>．

4．已知数列{<em>a<sub>n</sub></em>}的前<em>n</em>项和为<em>S<sub>n</sub></em>，且<em>a</em><sub>1</sub>＝1，2<em>S<sub>n</sub></em>＝<em>a<sub>n</sub>a<sub>n</sub></em><sub>＋1</sub>(<em>n</em>∈<strong>N</strong><sup>\*</sup>)，则<em>a<sub>n</sub></em>＝\_\_\_\_\_\_\_\_．

4．答案　<em>n</em>　解析　由2<em>S<sub>n</sub></em>＝<em>a<sub>n</sub>a<sub>n</sub></em><sub>＋1</sub>可知2<em>S<sub>n</sub></em><sub>－1</sub>＝<em>a<sub>n</sub></em><sub>－1</sub><em>a<sub>n</sub></em>(<em>n</em>≥2)，两式相减得2<em>a<sub>n</sub></em>＝<em>a<sub>n</sub>a<sub>n</sub></em><sub>＋1</sub>－<em>a<sub>n</sub></em><sub>－1</sub><em>a<sub>n</sub></em>＝<em>a<sub>n</sub></em>(<em>a<sub>n</sub></em><sub>＋1</sub>－

<em>a<sub>n</sub></em><sub>－1</sub>)，因为<em>a</em><sub>1</sub>＝1，所以<em>a<sub>n</sub></em>≠0，2＝<em>a<sub>n</sub></em><sub>＋1</sub>－<em>a<sub>n</sub></em><sub>－1</sub>，又因为<em>a</em><sub>1</sub>＝1，2<em>S</em><sub>1</sub>＝<em>a</em><sub>1</sub><em>a</em><sub>2</sub>，所以<em>a</em><sub>2</sub>＝2，结合<em>a<sub>n</sub></em><sub>＋1</sub>－<em>a<sub>n</sub></em><sub>－1</sub>＝2，所以<em>a<sub>n</sub></em>－<em>a<sub>n</sub></em><sub>－1</sub>＝1，数列{<em>a<sub>n</sub></em>}是以1为公差，1为首项的等差数列，所以<em>a<sub>n</sub></em>＝<em>n</em>．

5．（1）已知数列{<em>a<sub>n</sub></em>}满足<em>a</em><sub>1</sub>＋2<em>a</em><sub>2</sub>＋3<em>a</em><sub>3</sub>＋4<em>a</em><sub>4</sub>＋…＋<em>na<sub>n</sub></em>＝<em>n</em>，求<em>a<sub>n</sub></em>；  
（2）已知数列{<em>a<sub>n</sub></em>}的前<em>n</em>项和为<em>S<sub>n</sub></em>，若<em>a<sub>n</sub></em>&gt;0，<em>S<sub>n</sub></em>&gt;1，且6<em>S<sub>n</sub></em>＝(<em>a<sub>n</sub></em>＋1)(<em>a<sub>n</sub></em>＋2)，求<em>a<sub>n</sub></em>．

5．解析　（1）设<em>a</em><sub>1</sub>＋2<em>a</em><sub>2</sub>＋3<em>a</em><sub>3</sub>＋4<em>a</em><sub>4</sub>＋…＋<em>na<sub>n</sub></em>＝<em>T<sub>n</sub></em>，
当<em>n</em>＝1时，<em>a</em><sub>1</sub>＝<em>T</em><sub>1</sub>＝1，当<em>n</em>≥2时，<em>na<sub>n</sub></em>＝<em>T<sub>n</sub></em>－<em>T<sub>n</sub></em><sub>－1</sub>＝<em>n</em>－(<em>n</em>－1)＝1，
因此<em>a<sub>n</sub></em>＝，而<em>a</em><sub>1</sub>＝1，也满足此等式，所以<em>a<sub>n</sub></em>＝．  
（2）当<em>n</em>＝1时，<em>a</em><sub>1</sub>＝<em>S</em><sub>1</sub>＝(<em>a</em><sub>1</sub>＋1)(<em>a</em><sub>1</sub>＋2)，即<em>a</em>－3<em>a</em><sub>1</sub>＋2＝0．解得<em>a</em><sub>1</sub>＝1或<em>a</em><sub>1</sub>＝2．
因为<em>a</em><sub>1</sub>＝<em>S</em><sub>1</sub>&gt;1，所以<em>a</em><sub>1</sub>＝2．
当<em>n</em>≥2时，<em>a<sub>n</sub></em>＝<em>S<sub>n</sub></em>－<em>S<sub>n</sub></em><sub>－1</sub>＝(<em>a<sub>n</sub></em>＋1)(<em>a<sub>n</sub></em>＋2)－(<em>a<sub>n</sub></em><sub>－1</sub>＋1)(<em>a<sub>n</sub></em><sub>－1</sub>＋2)，
所以(<em>a<sub>n</sub></em>－<em>a<sub>n</sub></em><sub>－1</sub>－3)(<em>a<sub>n</sub></em>＋<em>a<sub>n</sub></em><sub>－1</sub>)＝0．因为<em>a<sub>n</sub></em>&gt;0，所以<em>a<sub>n</sub></em>＋<em>a<sub>n</sub></em><sub>－1</sub>&gt;0，所以<em>a<sub>n</sub></em>－<em>a<sub>n</sub></em><sub>－1</sub>＝3，
所以数列{<em>a<sub>n</sub></em>}是以2为首项，3为公差的等差数列．所以<em>a<sub>n</sub></em>＝3<em>n</em>－1．

6．已知<em>S<sub>n</sub></em>为正项数列{<em>a<sub>n</sub></em>}的前<em>n</em>项和，且满足<em>S<sub>n</sub></em>＝<em>a</em>＋<em>a<sub>n</sub></em>(<em>n</em>∈<strong>N</strong><sup>\*</sup>)．  
（1）求<em>a</em><sub>1</sub>，<em>a</em><sub>2</sub>，<em>a</em><sub>3</sub>，<em>a</em><sub>4</sub>的值；  
（2）求数列{<em>a<sub>n</sub></em>}的通项公式．

6．解析　（1）由<em>S<sub>n</sub></em>＝<em>a</em>＋<em>a<sub>n</sub></em>(<em>n</em>∈<strong>N</strong><sup>\*</sup>)，可得<em>a</em><sub>1</sub>＝<em>a</em>＋<em>a</em><sub>1</sub>，解得<em>a</em><sub>1</sub>＝1，

<em>S</em><sub>2</sub>＝<em>a</em><sub>1</sub>＋<em>a</em><sub>2</sub>＝<em>a</em>＋<em>a</em><sub>2</sub>，解得<em>a</em><sub>2</sub>＝2，同理，<em>a</em><sub>3</sub>＝3，<em>a</em><sub>4</sub>＝4．  
（2）<em>S<sub>n</sub></em>＝<em>a</em>＋，①，当<em>n</em>≥2时，<em>S<sub>n</sub></em><sub>－1</sub>＝<em>a</em>＋<em>a<sub>n</sub></em><sub>－1</sub>，②

①－②得(<em>a<sub>n</sub></em>－<em>a<sub>n</sub></em><sub>－1</sub>－1)(<em>a<sub>n</sub></em>＋<em>a<sub>n</sub></em><sub>－1</sub>)＝0．由于<em>a<sub>n</sub></em>＋<em>a<sub>n</sub></em><sub>－1</sub>≠0，所以<em>a<sub>n</sub></em>－<em>a<sub>n</sub></em><sub>－1</sub>＝1，
又由（1）知<em>a</em><sub>1</sub>＝1，故数列{<em>a<sub>n</sub></em>}为首项为1，公差为1的等差数列，故<em>a<sub>n</sub></em>＝<em>n</em>．

7．若数列{<em>a<sub>n</sub></em>}的前<em>n</em>项和为<em>S<sub>n</sub></em>，且满足<em>a<sub>n</sub></em>＋2<em>S<sub>n</sub>S<sub>n</sub></em><sub>－1</sub>＝0(<em>n</em>≥2)，<em>a</em><sub>1</sub>＝．  
（1）求证：成等差数列；  
（2）求数列{<em>a<sub>n</sub></em>}的通项公式．

7．解析　（1）当<em>n</em>≥2时，由<em>a<sub>n</sub></em>＋2<em>S<sub>n</sub>S<sub>n</sub></em><sub>－1</sub>＝0，得<em>S<sub>n</sub></em>－<em>S<sub>n</sub></em><sub>－1</sub>＝－2<em>S<sub>n</sub>S<sub>n</sub></em><sub>－1</sub>，所以－＝2，
又＝＝2，故是首项为2，公差为2的等差数列．  
（2）由（1）可得＝2<em>n</em>，∴<em>S<sub>n</sub></em>＝．
当<em>n</em>≥2时，<em>a<sub>n</sub></em>＝<em>S<sub>n</sub></em>－<em>S<sub>n</sub></em><sub>－1</sub>＝－＝＝－．
当<em>n</em>＝1时，<em>a</em><sub>1</sub>＝不适合上式．故<em>a<sub>n</sub></em>＝

8．设数列{<em>a<sub>n</sub></em>}的首项<em>a</em><sub>1</sub>＝，前<em>n</em>项和为<em>S<sub>n</sub></em>，且满足2<em>a<sub>n</sub></em><sub>＋1</sub>＋<em>S<sub>n</sub></em>＝3(<em>n</em>∈<strong>N</strong><sup>\*</sup>)．  
（1）求<em>a</em><sub>2</sub>及<em>a<sub>n</sub></em>；  
（2）求证：<em>a<sub>n</sub>S<sub>n</sub></em>的最大值为．

8．解析　（1）由题意得2<em>a</em><sub>2</sub>＋<em>S</em><sub>1</sub>＝3，即2<em>a</em><sub>2</sub>＋<em>a</em><sub>1</sub>＝3，所以<em>a</em><sub>2</sub>＝＝．
当<em>n</em>≥2时，由2<em>a<sub>n</sub></em><sub>＋1</sub>＋<em>S<sub>n</sub></em>＝3，得2<em>a<sub>n</sub></em>＋<em>S<sub>n</sub></em><sub>－1</sub>＝3，两式相减得2<em>a<sub>n</sub></em><sub>＋1</sub>－<em>a<sub>n</sub></em>＝0，即<em>a<sub>n</sub></em><sub>＋1</sub>＝<em>a<sub>n</sub></em>．
因为<em>a</em><sub>1</sub>＝，<em>a</em><sub>2</sub>＝，所以<em>a</em><sub>2</sub>＝<em>a</em><sub>1</sub>，即当<em>n</em>＝1时，<em>a<sub>n</sub></em><sub>＋1</sub>＝<em>a<sub>n</sub></em>也成立．
所以{<em>a<sub>n</sub></em>}是以为首项，为公比的等比数列，所以<em>a<sub>n</sub></em>＝．  
（2）因为2<em>a<sub>n</sub></em><sub>＋1</sub>＋<em>S<sub>n</sub></em>＝3，且<em>a<sub>n</sub></em><sub>＋1</sub>＝<em>a<sub>n</sub></em>，所以<em>S<sub>n</sub></em>＝3－2<em>a<sub>n</sub></em><sub>＋1</sub>＝3－<em>a<sub>n</sub></em>．
于是，<em>a<sub>n</sub>S<sub>n</sub></em>＝<em>a<sub>n</sub></em>(3－<em>a<sub>n</sub></em>)≤<sup>2</sup>＝，当且仅当<em>a<sub>n</sub></em>＝，即<em>n</em>＝1时等号成立．
故<em>a<sub>n</sub>S<sub>n</sub></em>的最大值为．

<strong>考点四　由</strong><em><strong>f</strong></em><strong>(</strong><em><strong>a<sub>n</sub></strong></em><strong>，</strong><em><strong>S<sub>n</sub></strong></em><strong>)＝0消去</strong><em><strong>a<sub>n</sub></strong></em><strong>型</strong>

【基本方法】

已知<em>S<sub>n</sub></em>求<em>a<sub>n</sub></em>的方法

已知<em>f</em>(<em>a<sub>n</sub></em>，<em>S<sub>n</sub></em>)＝0求<em>a<sub>n</sub></em>，如果不能消去<em>S<sub>n</sub></em>，则利用<em>a<sub>n</sub></em>＝消去<em>a<sub>n</sub></em>，先求出<em>S<sub>n</sub></em>，再求<em>a<sub>n</sub></em>，主要分五个步骤完成：  
（1）当<em>n</em>＝1时，先利用<em>a</em><sub>1</sub>＝<em>S</em><sub>1</sub>，求得<em>a</em><sub>1</sub>；  
（2）当<em>n</em>≥2时，用<em>a<sub>n</sub></em>＝消去<em>a<sub>n</sub></em>，便可得到当<em>n</em>≥2，<em>n</em>∈<strong>N</strong><sup>\*</sup>时数列{<em>S<sub>n</sub></em>}的一个递推公式；  
（3）借助各类递推公式求通项公式的方法求出当<em>n</em>≥2，<em>n</em>∈<strong>N</strong><sup>\*</sup>时数列{<em>S<sub>n</sub></em>}的通项公式；  
（4）此时问题转化为由<em>S<sub>n</sub></em>＝<em>f</em>(<em>n</em>)求<em>a<sub>n</sub></em>型，求出当<em>n</em>≥2，<em>n</em>∈<strong>N</strong><sup>\*</sup>时数列{<em>a<sub>n</sub></em>}的通项公式；  
（5）看<em>a</em><sub>1</sub>是否符合<em>n</em>≥2时<em>a<sub>n</sub></em>的表达式，如果符合，则可以把数列的通项公式合写；否则应写成分段的形式．

【基本题型】

<strong>[例6]</strong> （1）设数列{<em>a<sub>n</sub></em>}的前<em>n</em>项和为<em>S<sub>n</sub></em>，若<em>a</em><sub>1</sub>＝3且当<em>n</em>≥2时，2<em>a<sub>n</sub></em>＝<em>S<sub>n</sub></em>·<em>S<sub>n</sub></em><sub>－1</sub>(<em>n</em>∈<strong>N</strong><sup>\*</sup>)，则数列{<em>a<sub>n</sub></em>}的通项公式<em>a<sub>n</sub></em>＝\_\_\_\_\_\_\_\_．
答案　　解析　当<em>n</em>≥2时，由2<em>a<sub>n</sub></em>＝<em>S<sub>n</sub></em>·<em>S<sub>n</sub></em><sub>－1</sub>可得2(<em>S<sub>n</sub></em>－<em>S<sub>n</sub></em><sub>－1</sub>)＝<em>S<sub>n</sub></em>·<em>S<sub>n</sub></em><sub>－1</sub>，∴－＝，即－＝－，∴数列是首项为，公差为－的等差数列，∴＝＋·(<em>n</em>－1)＝，∴<em>S<sub>n</sub></em>＝．当<em>n</em>≥2时，<em>a<sub>n</sub></em>＝<em>S<sub>n</sub>S<sub>n</sub></em><sub>－1</sub>＝××＝，又<em>a</em><sub>1</sub>＝3，∴<em>a<sub>n</sub></em>＝  
（2）设<em>S<sub>n</sub></em>是数列{<em>a<sub>n</sub></em>}的前<em>n</em>项和，且<em>a</em><sub>1</sub>＝－1，<em>a<sub>n</sub></em><sub>＋1</sub>＝<em>S<sub>n</sub>S<sub>n</sub></em><sub>＋1</sub>，则下列结论正确的是\_\_\_\_\_\_\_\_．

①<em>a<sub>n</sub></em>＝　　　②<em>a<sub>n</sub></em>＝　　③<em>S<sub>n</sub></em>＝－　　④数列是等差数列
答案　②③④　解析　∵<em>a<sub>n</sub></em><sub>＋1</sub>＝<em>S<sub>n</sub></em>·<em>S<sub>n</sub></em><sub>＋1</sub>＝<em>S<sub>n</sub></em><sub>＋1</sub>－<em>S<sub>n</sub></em>，两边同除以<em>S<sub>n</sub></em><sub>＋1</sub>·<em>S<sub>n</sub></em>，得－＝－1．∴是以－1为首项，<em>d</em>＝－1的等差数列，即＝－1＋(<em>n</em>－1)×(－1)＝－<em>n</em>，∴<em>S<sub>n</sub></em>＝－．当<em>n</em>≥2时，<em>a<sub>n</sub></em>＝<em>S<sub>n</sub></em>－<em>S<sub>n</sub></em><sub>－1</sub>＝－＋＝，又<em>a</em><sub>1</sub>＝－1不适合上式，∴<em>a<sub>n</sub></em>＝

【对点精练】

1．已知各项均为正数的数列{<em>a<sub>n</sub></em>}的前<em>n</em>项和为<em>S<sub>n</sub></em>，若<em>S</em><sub>1</sub>＝2，3<em>S</em>－2<em>a<sub>n</sub></em><sub>＋1</sub><em>S<sub>n</sub></em>＝<em>a</em>，则<em>a<sub>n</sub></em>＝\_\_\_\_\_\_\_\_．

1．答案　　解析　由题意可得3<em>S</em>－2<em>a<sub>n</sub></em><sub>＋1</sub><em>S<sub>n</sub></em>－<em>a</em>＝(<em>S<sub>n</sub></em>－<em>a<sub>n</sub></em><sub>＋1</sub>)·(3<em>S<sub>n</sub></em>＋<em>a<sub>n</sub></em><sub>＋1</sub>)＝0，又<em>a<sub>n</sub></em>＞0，
所以<em>S<sub>n</sub></em>＝<em>a<sub>n</sub></em><sub>＋1</sub>，则<em>S<sub>n</sub></em><sub>－1</sub>＝<em>a<sub>n</sub></em>(<em>n</em>≥2)，两式相减并移项得<em>a<sub>n</sub></em><sub>＋1</sub>＝2<em>a<sub>n</sub></em>(<em>n</em>≥2)，又<em>S</em><sub>1</sub>＝<em>a</em><sub>1</sub>＝<em>a</em><sub>2</sub>＝2，则<em>a<sub>n</sub></em>＝<em>a</em><sub>2</sub>·2<em><sup>n</sup></em><sup>－2</sup>＝2<em><sup>n</sup></em><sup>－1</sup>(<em>n</em>≥2)，故<em>a<sub>n</sub></em>＝

2．已知数列{<em>a<sub>n</sub></em>}中，<em>a</em><sub>1</sub>＝1，<em>S<sub>n</sub></em>为数列{<em>a<sub>n</sub></em>}的前<em>n</em>项和，且当<em>n</em>≥2时，有＝1成立，则<em>a<sub>n</sub></em>＝\_\_\_\_\_\_\_\_．

2．答案　　解析　当<em>n</em>≥2时，由＝1，得2(<em>S<sub>n</sub></em>－<em>S<sub>n</sub></em><sub>－1</sub>)＝(<em>S<sub>n</sub></em>－<em>S<sub>n</sub></em><sub>－1</sub>)<em>S<sub>n</sub></em>－<em>S</em>＝－<em>S<sub>n</sub>S<sub>n</sub></em>

<sub>－1</sub>，∴－＝1，又＝2，∴是以2为首项，1为公差的等差数列，∴＝<em>n</em>＋1，故<em>S<sub>n</sub></em>＝，当<em>n</em>≥2时，<em>a<sub>n</sub></em>＝<em>S<sub>n</sub></em>－<em>S<sub>n</sub></em><sub>－1</sub>＝－＝，又<em>a</em><sub>1</sub>＝－1不适合上式，∴<em>a<sub>n</sub></em>＝

