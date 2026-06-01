**专题17　数列不等式的证明**

![](images/e974f9dedcada78cd3f2084d324066f26338dc1a0a5e1f75afe4b751cb4f3a41.jpg)

数列不等式的证明常用到“放缩法”，一是在求和中将通项“放缩”为“可求和数列”；二是求和后再“放缩”．

常见的放缩类型及方法

(1)分式型：①＜＝；②－＜＜－；

(2)根式型：①2(－)＜＜2(－)；

②＜＜；

③ ＞＝2(－)．

(3)分数型：＞(*b*＞*a*＞0，*m*＞0)，＜(*a*＞*b*＞0，*m*＞0)；

(4)基本不等式型：＋＞2 ＝2；

(5)二项式定理型：2<em><sup>n</sup></em>－1≥2<em>n</em>＋1(<em>n</em>≥3)．

注：在放缩法处理数列求和不等式时，放缩为等比数列和能够裂项相消的数列的情况比较多见，故优先考虑．对于数列求和不等式，要谨记“求和看通项”，从通项公式入手，结合不等号方向考虑放缩成可求和的通项公式．在放缩时要注意前几问的铺垫与提示，尤其是关于恒成立问题与最值问题所带来的恒成立不等式，往往提供了放缩数列的方向．放缩通项公式有可能会进行多次，要注意放缩的方向，朝着可求和的通项公式进行靠拢（等比数列，裂项相消等）．

**考点一　先求和(裂项相消法)再放缩**

**【基本题型】**

<strong>[例1]</strong>　设等差数列{<em>a<sub>n</sub></em>}的前<em>n</em>项和为<em>S<sub>n</sub></em>，已知<em>a</em><sub>1</sub>＝9，<em>a</em><sub>2</sub>为整数，且<em>S<sub>n</sub></em>≤<em>S</em><sub>5</sub>．

(1)求{<em>a<sub>n</sub></em>}的通项公式；

(2)设数列的前<em>n</em>项和为<em>T<sub>n</sub></em>，求证：<em>T<sub>n</sub></em>≤．

解析　(1)由<em>a</em><sub>1</sub>＝9，<em>a</em><sub>2</sub>为整数可知，等差数列{<em>a<sub>n</sub></em>}的公差<em>d</em>为整数．又<em>S<sub>n</sub></em>≤<em>S</em><sub>5</sub>，∴<em>a</em><sub>5</sub>≥0，<em>a</em><sub>6</sub>≤0，

于是9＋4*d*≥0，9＋5*d*≤0，解得－≤*d*≤－．∵*d*为整数，∴*d*＝－2．

故{<em>a<sub>n</sub></em>}的通项公式为<em>a<sub>n</sub></em>＝11－2<em>n</em>．

(2)由(1)，得＝＝，

∴<em>T<sub>n</sub></em>＝＋＋…＋＝．

令<em>b<sub>n</sub></em>＝，由函数<em>f</em>(<em>x</em>)＝的图象关于点(4.5，0)对称及其单调性，

知0&lt;<em>b</em><sub>1</sub>&lt;<em>b</em><sub>2</sub>&lt;<em>b</em><sub>3</sub>&lt;<em>b</em><sub>4</sub>，<em>b</em><sub>5</sub>&lt;<em>b</em><sub>6</sub>&lt;<em>b</em><sub>7</sub>&lt;…&lt;0，∴<em>b<sub>n</sub></em>≤<em>b</em><sub>4</sub>＝1．∴<em>T<sub>n</sub></em>≤×＝．

<strong>[例2]</strong>　在等比数列{<em>a<sub>n</sub></em>}中，首项<em>a</em><sub>1</sub>＝8，数列{<em>b<sub>n</sub></em>}满足<em>b<sub>n</sub></em>＝log<sub>2</sub><em>a<sub>n</sub></em>(<em>n</em>∈<strong>N</strong><sup>\*</sup>)，且<em>b</em><sub>1</sub>＋<em>b</em><sub>2</sub>＋<em>b</em><sub>3</sub>＝15．

(1)求数列{<em>a<sub>n</sub></em>}的通项公式；

(2)记数列{<em>b<sub>n</sub></em>}的前<em>n</em>项和为<em>S<sub>n</sub></em>，又设数列的前<em>n</em>项和为<em>T<sub>n</sub></em>，求证：<em>T<sub>n</sub></em>&lt;．

解析　(1)由<em>b<sub>n</sub></em>＝log<sub>2</sub><em>a<sub>n</sub></em>和<em>b</em><sub>1</sub>＋<em>b</em><sub>2</sub>＋<em>b</em><sub>3</sub>＝15，得log<sub>2</sub>(<em>a</em><sub>1</sub><em>a</em><sub>2</sub><em>a</em><sub>3</sub>)＝15，∴<em>a</em><sub>1</sub><em>a</em><sub>2</sub><em>a</em><sub>3</sub>＝2<sup>15</sup>，

设等比数列{<em>a<sub>n</sub></em>}的公比为<em>q</em>，∵<em>a</em><sub>1</sub>＝8，∴<em>a<sub>n</sub></em>＝8<em>q<sup>n</sup></em><sup>－1</sup>，∴8·8<em>q</em>·8<em>q</em><sup>2</sup>＝2<sup>15</sup>，解得<em>q</em>＝4，

∴<em>a<sub>n</sub></em>＝8·4<em><sup>n</sup></em><sup>－1</sup>，即<em>a<sub>n</sub></em>＝2<sup>2</sup><em><sup>n</sup></em><sup>＋1</sup>(<em>n</em>∈<strong>N</strong><sup>\*</sup>)．

(2)由(1)得<em>b<sub>n</sub></em>＝2<em>n</em>＋1，易知{<em>b<sub>n</sub></em>}为等差数列，

<em>S<sub>n</sub></em>＝3＋5＋…＋(2<em>n</em>＋1)＝<em>n</em><sup>2</sup>＋2<em>n</em>，则＝＝，

<em>T<sub>n</sub></em>＝＝，

∴<em>T<sub>n</sub></em>&lt;．

<strong>[例3]</strong>　已知数列{<em>a<sub>n</sub></em>}为等比数列，数列{<em>b<sub>n</sub></em>}为等差数列，且<em>b</em><sub>1</sub>＝<em>a</em><sub>1</sub>＝1，<em>b</em><sub>2</sub>＝<em>a</em><sub>1</sub>＋<em>a</em><sub>2</sub>，<em>a</em><sub>3</sub>＝2<em>b</em><sub>3</sub>－6．

(1)求数列{<em>a<sub>n</sub></em>}，{<em>b<sub>n</sub></em>}的通项公式；

(2)设<em>c<sub>n</sub></em>＝，数列{<em>c<sub>n</sub></em>}的前<em>n</em>项和为<em>T<sub>n</sub></em>，证明：≤<em>T<sub>n</sub></em>&lt;．

解析　(1)设数列{<em>a<sub>n</sub></em>}的公比为<em>q</em>，数列{<em>b<sub>n</sub></em>}的公差为<em>d</em>，由题意得1＋<em>d</em>＝1＋<em>q</em>，<em>q</em><sup>2</sup>＝2(1＋2<em>d</em>)－6，

解得<em>d</em>＝<em>q</em>＝2，所以<em>a<sub>n</sub></em>＝2<em><sup>n</sup></em><sup>－1</sup>，<em>b<sub>n</sub></em>＝2<em>n</em>－1．

(2)因为<em>c<sub>n</sub></em>＝＝＝，

所以<em>T<sub>n</sub></em>＝

＝＝－，

因为&gt;0，所以<em>T<sub>n</sub></em>&lt;．又因为<em>T<sub>n</sub></em>在[1，＋∞)上单调递增，

所以当<em>n</em>＝1时，<em>T<sub>n</sub></em>取最小值<em>T</em><sub>1</sub>＝，所以≤<em>T<sub>n</sub></em>&lt;．

<strong>[例4]</strong>　已知数列{<em>a<sub>n</sub></em>}的前<em>n</em>项和为<em>S<sub>n</sub></em>，且满足<em>S<sub>n</sub></em>＝(<em>a<sub>n</sub></em>－1)，<em>n</em>∈<strong>N</strong><sup>\*</sup>．

(1)求数列{<em>a<sub>n</sub></em>}的通项公式；

(2)令<em>b<sub>n</sub></em>＝log<sub>2</sub><em>a<sub>n</sub></em>，记数列的前<em>n</em>项和为<em>T<sub>n</sub></em>，证明：<em>T<sub>n</sub></em>&lt;．

解析　(1)当<em>n</em>＝1时，有<em>a</em><sub>1</sub>＝<em>S</em><sub>1</sub>＝(<em>a</em><sub>1</sub>－1)，解得<em>a</em><sub>1</sub>＝4．

当<em>n</em>≥2时，有<em>S<sub>n</sub></em><sub>－1</sub>＝(<em>a<sub>n</sub></em><sub>－1</sub>－1)，则<em>a<sub>n</sub></em>＝<em>S<sub>n</sub></em>－<em>S<sub>n</sub></em><sub>－1</sub>＝(<em>a<sub>n</sub></em>－1)－(<em>a<sub>n</sub></em><sub>－1</sub>－1)，整理得＝4，

∴数列{<em>a<sub>n</sub></em>}是以<em>q</em>＝4为公比，以<em>a</em><sub>1</sub>＝4为首项的等比数列．∴<em>a<sub>n</sub></em>＝4×4<em><sup>n</sup></em><sup>－1</sup>＝4<em><sup>n</sup></em>(<em>n</em>∈<strong>N</strong><sup>\*</sup>)

即数列{<em>a<sub>n</sub></em>}的通项公式为<em>a<sub>n</sub></em>＝4<em><sup>n</sup></em>(<em>n</em>∈<strong>N</strong><sup>\*</sup>)．

(2)由(1)得<em>b<sub>n</sub></em>＝log<sub>2</sub><em>a<sub>n</sub></em>＝log<sub>2</sub>4<em><sup>n</sup></em>＝2<em>n</em>，则＝＝

∴<em>T<sub>n</sub></em>＝＝&lt;．

<strong>[例5]</strong>　已知数列{<em>a<sub>n</sub></em>}中，<em>a</em><sub>1</sub>＝1，其前<em>n</em>项的和为<em>S<sub>n</sub></em>，且满足<em>a<sub>n</sub></em>＝(<em>n</em>≥2，<em>n</em>∈<strong>N</strong><sup>\*</sup>)．

(1)求证：数列是等差数列；

(2)证明：<em>S</em><sub>1</sub>＋<em>S</em><sub>2</sub>＋<em>S</em><sub>3</sub>＋…＋<em>S<sub>n</sub></em>&lt;．

解析　(1)当<em>n</em>≥2时，<em>S<sub>n</sub></em>－<em>S<sub>n</sub></em><sub>－1</sub>＝，<em>S<sub>n</sub></em><sub>－1</sub>－<em>S<sub>n</sub></em>＝2<em>S<sub>n</sub></em>·<em>S<sub>n</sub></em><sub>－1</sub>，－＝2，

所以数列是以1为首项，2为公差的等差数列．

(2)由(1)可知，＝＋(<em>n</em>－1)·2＝2<em>n</em>－1，所以<em>S<sub>n</sub></em>＝．

<em>S</em><sub>1</sub>＋<em>S</em><sub>2</sub>＋<em>S</em><sub>3</sub>＋…＋<em>S<sub>n</sub></em>＝＋＋＋…＋

＝×＝×<．

<strong>[例6]</strong>　设<em>S<sub>n</sub></em>为数列{<em>a<sub>n</sub></em>}的前<em>n</em>项和，已知<em>a</em><sub>1</sub>＝2，对任意<em>n</em>∈<strong>N</strong><sup>\*</sup>，都有2<em>S<sub>n</sub></em>＝(<em>n</em>＋1)<em>a<sub>n</sub></em>．

(1)求数列{<em>a<sub>n</sub></em>}的通项公式；

(2)若数列的前<em>n</em>项和为<em>T<sub>n</sub></em>，求证：≤<em>T<sub>n</sub></em>&lt;1．

解析　(1)因为2<em>S<sub>n</sub></em>＝(<em>n</em>＋1)<em>a<sub>n</sub></em>，所以2<em>S<sub>n</sub></em><sub>－1</sub>＝<em>na<sub>n</sub></em><sub>－1</sub>(<em>n</em>≥2)．

两式相减，得2<em>a<sub>n</sub></em>＝(<em>n</em>＋1)<em>a<sub>n</sub></em>－<em>na<sub>n</sub></em><sub>－1</sub>(<em>n</em>≥2)，即(<em>n</em>－1)<em>a<sub>n</sub></em>＝<em>na<sub>n</sub></em><sub>－1</sub>(<em>n</em>≥2)，

所以当<em>n</em>≥2时，＝，所以＝．因为<em>a</em><sub>1</sub>＝2，所以<em>a<sub>n</sub></em>＝2<em>n</em>．

(2)<em>a<sub>n</sub></em>＝2<em>n</em>，令<em>b<sub>n</sub></em>＝，<em>n</em>∈<strong>N</strong><sup>\*</sup>，

则<em>b<sub>n</sub></em>＝＝＝－．

所以<em>T<sub>n</sub></em>＝<em>b</em><sub>1</sub>＋<em>b</em><sub>2</sub>＋…＋<em>b<sub>n</sub></em>＝＋＋…＋＝1－．

因为&gt;0，所以1－&lt;1．因为<em>y</em>＝在<strong>N</strong><sup>\*</sup>上是递减函数，所以<em>y</em>＝1－在<strong>N</strong><sup>\*</sup>上是递增函数．

所以当<em>n</em>＝1时，<em>T<sub>n</sub></em>取得最小值．所以≤<em>T<sub>n</sub></em>&lt;1．

<strong>[例7]</strong>　(2020·浙江)已知数列{<em>a<sub>n</sub></em>}，{<em>b<sub>n</sub></em>}，{<em>c<sub>n</sub></em>}满足<em>a</em><sub>1</sub>＝<em>b</em><sub>1</sub>＝<em>c</em><sub>1</sub>＝1，<em>c<sub>n</sub></em>＝<em>a<sub>n</sub></em><sub>＋1</sub>－<em>a<sub>n</sub></em>，<em>c<sub>n</sub></em><sub>＋1</sub>＝<em>c<sub>n</sub></em>，<em>n</em>∈<strong>N</strong><sup>\*</sup>．

(1)若{<em>b<sub>n</sub></em>}为等比数列，公比<em>q</em>＞0，且<em>b</em><sub>1</sub>＋<em>b</em><sub>2</sub>＝6<em>b</em><sub>3</sub>，求<em>q</em>的值及数列{<em>a<sub>n</sub></em>}的通项公式；

(2)若{<em>b<sub>n</sub></em>}为等差数列，公差<em>d</em>＞0，证明：<em>c</em><sub>1</sub>＋<em>c</em><sub>2</sub>＋<em>c</em><sub>3</sub>＋…＋<em>c<sub>n</sub></em>＜1＋，<em>n</em>∈<strong>N</strong><sup>\*</sup>．

解析　(1)由<em>b</em><sub>1</sub>＋<em>b</em><sub>2</sub>＝6<em>b</em><sub>3</sub>，得1＋<em>q</em>＝6<em>q</em><sup>2</sup>，解得<em>q</em>＝．所以<em>b<sub>n</sub></em>＝．

由<em>c<sub>n</sub></em><sub>＋1</sub>＝4<em>c<sub>n</sub></em>，得<em>c<sub>n</sub></em>＝4<em><sup>n</sup></em><sup>－1</sup>．由<em>a<sub>n</sub></em><sub>＋1</sub>－<em>a<sub>n</sub></em>＝4<em><sup>n</sup></em><sup>－1</sup>，得<em>a<sub>n</sub></em>＝<em>a</em><sub>1</sub>＋1＋4＋…＋4<em><sup>n</sup></em><sup>－2</sup>＝．

(2)由<em>c<sub>n</sub></em><sub>＋1</sub>＝<em>c<sub>n</sub></em>，得<em>c<sub>n</sub></em>＝＝，

所以<em>c</em><sub>1</sub>＋<em>c</em><sub>2</sub>＋<em>c</em><sub>3</sub>＋…＋<em>c<sub>n</sub></em>＝．

由<em>b</em><sub>1</sub>＝1，<em>d</em>＞0，得<em>b<sub>n</sub></em><sub>＋1</sub>＞1，因此<em>c</em><sub>1</sub>＋<em>c</em><sub>2</sub>＋<em>c</em><sub>3</sub>＋…＋<em>c<sub>n</sub></em>＜1＋，<em>n</em>∈<strong>N</strong><sup>\*</sup>．

<strong>[例8]</strong>　数列{<em>a<sub>n</sub></em>}中，<em>a</em><sub>1</sub>＝，<em>a<sub>n</sub></em><sub>＋1</sub>＝(<em>n</em>∈N<sup>\*</sup>)．

(1)求证：<em>a<sub>n</sub></em><sub>＋1</sub>&lt;<em>a<sub>n</sub></em>；

(2)记数列{<em>a<sub>n</sub></em>}的前<em>n</em>项和为<em>S<sub>n</sub></em>，求证：<em>S<sub>n</sub></em>&lt;1．

解析　(1)∵<em>a</em>－<em>a<sub>n</sub></em>＋1＝<sup>2</sup>＋&gt;0，且<em>a</em><sub>1</sub>＝&gt;0，∴<em>a<sub>n</sub></em>&gt;0，

∴<em>a<sub>n</sub></em><sub>＋1</sub>－<em>a<sub>n</sub></em>＝－<em>a<sub>n</sub></em>＝&lt;0．∴<em>a<sub>n</sub></em><sub>＋1</sub>&lt;<em>a<sub>n</sub></em>．

(2)∵1－<em>a<sub>n</sub></em><sub>＋1</sub>＝1－＝，∴＝＝－<em>a<sub>n</sub></em>．

∴<em>a<sub>n</sub></em>＝－，则<em>a</em><sub>1</sub>＋<em>a</em><sub>2</sub>＋…＋<em>a<sub>n</sub></em>＝2－，由(1)可知0&lt;<em>a<sub>n</sub></em>≤，

∴<em>S<sub>n</sub></em>＝<em>a</em><sub>1</sub>＋<em>a</em><sub>2</sub>＋…＋<em>a<sub>n</sub></em>＝2－&lt;1．

<strong>[例9]</strong>　已知正项数列{<em>a<sub>n</sub></em>}的前<em>n</em>项和为<em>S<sub>n</sub></em>，且<em>a</em>＋2<em>a<sub>n</sub></em>＝4<em>S<sub>n</sub></em>－1．

(1)求数列{<em>a<sub>n</sub></em>}的通项公式；

(2)若<em>b<sub>n</sub></em>＝，数列{<em>b<sub>n</sub></em>}的前<em>n</em>项和为<em>T<sub>n</sub></em>，求证：≤<em>T<sub>n</sub></em>＜．

解析(1)由题意，当<em>n</em>＝1时，<em>a</em>＋2<em>a</em><sub>1</sub>＝4<em>S</em><sub>1</sub>－1＝4<em>a</em><sub>1</sub>－1，整理，得<em>a</em>－2<em>a</em><sub>1</sub>＋1＝0，解得<em>a</em><sub>1</sub>＝1．

当<em>n</em>≥2时，由<em>a</em>＋2<em>a<sub>n</sub></em>＝4<em>S<sub>n</sub></em>－1，得<em>a</em>＋2<em>a<sub>n</sub></em><sub>－1</sub>＝4<em>S<sub>n</sub></em><sub>－1</sub>－1，

两式相减，得<em>a</em>＋2<em>a<sub>n</sub></em>－<em>a</em>－2<em>a<sub>n</sub></em><sub>－1</sub>＝4<em>S<sub>n</sub></em>－1－4<em>S<sub>n</sub></em><sub>－1</sub>＋1＝4<em>a<sub>n</sub></em>，即<em>a</em>－<em>a</em>＝2<em>a<sub>n</sub></em>＋2<em>a<sub>n</sub></em><sub>－1</sub>，

∴(<em>a<sub>n</sub></em>＋<em>a<sub>n</sub></em><sub>－1</sub>)(<em>a<sub>n</sub></em>－<em>a<sub>n</sub></em><sub>－1</sub>)＝2(<em>a<sub>n</sub></em>＋<em>a<sub>n</sub></em><sub>－1</sub>)．∵<em>a<sub>n</sub></em>＋<em>a<sub>n</sub></em><sub>－1</sub>&gt;0，∴<em>a<sub>n</sub></em>－<em>a<sub>n</sub></em><sub>－1</sub>＝2，

∴数列{<em>a<sub>n</sub></em>}是以1为首项，2为公差的等差数列．∴<em>a<sub>n</sub></em>＝1＋2(<em>n</em>－1)＝2<em>n</em>－1．

(2)由(1)知，<em>S<sub>n</sub></em>＝<em>n</em>＋·2＝<em>n</em><sup>2</sup>，

则<em>b<sub>n</sub></em>＝＝＝·＝．

∴<em>T<sub>n</sub></em>＝<em>b</em><sub>1</sub>＋<em>b</em><sub>2</sub>＋…＋<em>b<sub>n</sub></em>＝＋＋…＋

＝＝

∴<em>T<sub>n</sub></em>&lt;．又∵<em>a<sub>n</sub></em>&gt;0，∴<em>b<sub>n</sub></em>&gt;0，易证{<em>T<sub>n</sub></em>}单调递增，∴<em>T<sub>n</sub></em>≥<em>T</em><sub>1</sub>＝<em>b</em><sub>1</sub>＝＝，∴≤<em>T<sub>n</sub></em>&lt;．

<strong>[例10]</strong>　设数列{<em>a<sub>n</sub></em>}的前<em>n</em>项的和<em>S<sub>n</sub></em>＝<em>a<sub>n</sub></em>－×2<em><sup>n</sup></em><sup>＋1</sup>＋(<em>n</em>＝1，2，…)．

(1)求首项<em>a</em><sub>1</sub>与通项<em>a<sub>n</sub></em>；

(2)设<em>T<sub>n</sub></em>＝(<em>n</em>＝1，2，…)，证明：<em><sub>i</sub></em>＜．

解析　(1)由<em>S<sub>n</sub></em>＝<em>a<sub>n</sub></em>－×2<em><sup>n</sup></em><sup>＋1</sup>＋，令<em>n</em>＝1，得<em>a</em><sub>1</sub>＝<em>a</em><sub>1</sub>－＋，解得<em>a</em><sub>1</sub>＝2．

又由<em>S<sub>n</sub></em>＝<em>a<sub>n</sub></em>－×2<em><sup>n</sup></em><sup>＋1</sup>＋得<em>S<sub>n</sub></em><sub>－1</sub>＝<em>a<sub>n</sub></em><sub>－1</sub>－×2<em><sup>n</sup></em>＋，

相减并整理得＋1＝2，所以是以＋1＝2为首项，2为公比的等比数列，

所以＋1＝2·2<em><sup>n</sup></em><sup>－1</sup>＝2<em><sup>n</sup></em>，故<em>a<sub>n</sub></em>＝2<sup>2</sup><em><sup>n</sup></em>－2<em><sup>n</sup></em>．

(2)由<em>a<sub>n</sub></em>＝2<sup>2</sup><em><sup>n</sup></em>－2<em><sup>n</sup></em>，得<em>S<sub>n</sub></em>＝(2<em><sup>n</sup></em>－1)(2<em><sup>n</sup></em><sup>＋1</sup>－1)．所以<em>T<sub>n</sub></em>＝＝，

于是<sub>i</sub>＝＝＜．

<strong>[例11]</strong>　已知数列{<em>a<sub>n</sub></em>}为单调递增数列，<em>S<sub>n</sub></em>为其前<em>n</em>项和，2<em>S<sub>n</sub></em>＝<em>a</em>＋<em>n</em>．

(1)求{<em>a<sub>n</sub></em>}的通项公式；

(2)若<em>b<sub>n</sub></em>＝，<em>T<sub>n</sub></em>为数列{<em>b<sub>n</sub></em>}的前<em>n</em>项和，证明：<em>T<sub>n</sub></em>&lt;．

解析　(1)当<em>n</em>＝1时，2<em>S</em><sub>1</sub>＝2<em>a</em><sub>1</sub>＝<em>a</em>＋1，所以(<em>a</em><sub>1</sub>－1)<sup>2</sup>＝0，即<em>a</em><sub>1</sub>＝1，

又{<em>a<sub>n</sub></em>}为单调递增数列，所以<em>a<sub>n</sub></em>≥1．

由2<em>S<sub>n</sub></em>＝<em>a</em>＋<em>n</em>得2<em>S<sub>n</sub></em><sub>＋1</sub>＝<em>a</em>＋<em>n</em>＋1，所以2<em>S<sub>n</sub></em><sub>＋1</sub>－2<em>S<sub>n</sub></em>＝<em>a</em>－<em>a</em>＋1，

整理得2<em>a<sub>n</sub></em><sub>＋1</sub>＝<em>a</em>－<em>a</em>＋1，所以<em>a</em>＝(<em>a<sub>n</sub></em><sub>＋1</sub>－1)<sup>2</sup>．所以<em>a<sub>n</sub></em>＝<em>a<sub>n</sub></em><sub>＋1</sub>－1，即<em>a<sub>n</sub></em><sub>＋1</sub>－<em>a<sub>n</sub></em>＝1．

所以{<em>a<sub>n</sub></em>}是以1为首项，1为公差的等差数列．所以<em>a<sub>n</sub></em>＝<em>n</em>．

(2)<em>b<sub>n</sub></em>＝＝＝－，

所以<em>T<sub>n</sub></em>＝＋＋…＋＝－&lt;．

**【对点精练】**

1．已知等差数列{<em>a<sub>n</sub></em>}的前<em>n</em>项和为<em>S<sub>n</sub></em>，<em>n</em>∈<strong>N</strong><sup>\*</sup>，且<em>a</em><sub>2</sub>＝3，<em>S</em><sub>5</sub>＝25．

(1)求数列{<em>a<sub>n</sub></em>}的通项公式；

(2)若数列{<em>b<sub>n</sub></em>}满足<em>b<sub>n</sub></em>＝，记数列{<em>b<sub>n</sub></em>}的前<em>n</em>项和为<em>T<sub>n</sub></em>，证明：<em>T<sub>n</sub></em>&lt;1．

1．解析　(1)设等差数列{<em>a<sub>n</sub></em>}的公差为<em>d</em>．因为所以

解得所以<em>a<sub>n</sub></em>＝2<em>n</em>－1．

(2)由(1)知，<em>a<sub>n</sub></em>＝2<em>n</em>－1，所以<em>S<sub>n</sub></em>＝＝<em>n</em><sup>2</sup>．

所以<em>b<sub>n</sub></em>＝＝＝－．

所以<em>T<sub>n</sub></em>＝<em>b</em><sub>1</sub>＋<em>b</em><sub>2</sub>＋<em>b</em><sub>3</sub>＋…＋<em>b<sub>n</sub></em>＝＋＋…＋＝1－&lt;1．

2．已知等差数列{<em>a<sub>n</sub></em>}的公差<em>d</em>≠0，<em>a</em><sub>1</sub>＝0，其前<em>n</em>项和为<em>S<sub>n</sub></em>，且<em>a</em><sub>2</sub>＋2，<em>S</em><sub>3</sub>，<em>S</em><sub>4</sub>成等比数列．

(1)求数列{<em>a<sub>n</sub></em>}的通项公式；

(2)若<em>b<sub>n</sub></em>＝，数列{<em>b<sub>n</sub></em>}的前<em>n</em>项和为<em>T<sub>n</sub></em>，求证：<em>T<sub>n</sub></em>－2<em>n</em>&lt;．

2．解析　(1)由<em>a</em><sub>1</sub>＝0得<em>a<sub>n</sub></em>＝(<em>n</em>－1)<em>d</em>，<em>S<sub>n</sub></em>＝，因为<em>a</em><sub>2</sub>＋2，<em>S</em><sub>3</sub>，<em>S</em><sub>4</sub>成等比数列，

所以<em>S</em>＝(<em>a</em><sub>2</sub>＋2)<em>S</em><sub>4</sub>，即(3<em>d</em>)<sup>2</sup>＝(<em>d</em>＋2)·6<em>d</em>，整理得3<em>d</em><sup>2</sup>－12<em>d</em>＝0，即<em>d</em><sup>2</sup>－4<em>d</em>＝0，因为<em>d</em>≠0，所以<em>d</em>＝4，

所以<em>a<sub>n</sub></em>＝(<em>n</em>－1)<em>d</em>＝4(<em>n</em>－1)＝4<em>n</em>－4．

(2)由(1)可得<em>S<sub>n</sub></em><sub>＋1</sub>＝2<em>n</em>(<em>n</em>＋1)，所以<em>b<sub>n</sub></em>＝＝＝2＋＝2＋，

所以<em>T<sub>n</sub></em>＝2<em>n</em>＋＋＋…＋＝2<em>n</em>＋1＋－－，所以<em>T<sub>n</sub></em>－2<em>n</em>&lt;．

3．设函数<em>f</em>(<em>x</em>)＝＋sin<em>x</em>的所有正的极小值点从小到大排成的数列为{<em>x<sub>n</sub></em>}．

(1)求数列{<em>x<sub>n</sub></em>}的通项公式；

(2)令<em>b<sub>n</sub></em>＝，设数列的前<em>n</em>项和为<em>S<sub>n</sub></em>，求证：<em>S<sub>n</sub></em>&lt;．

3．解析　(1)<em>f</em>(<em>x</em>)＝＋sin <em>x</em>，令<em>f</em>′(<em>x</em>)＝＋cos <em>x</em>＝0，得<em>x</em>＝2<em>k</em>π±(<em>k</em>∈<strong>Z</strong>)，

由<em>f</em>′(<em>x</em>)&gt;0⇒2<em>k</em>π－&lt;<em>x</em>&lt;2<em>k</em>π＋(<em>k</em>∈<strong>Z</strong>)，由<em>f</em>′(<em>x</em>)&lt;0⇒2<em>k</em>π＋&lt;<em>x</em>&lt;2<em>k</em>π＋(<em>k</em>∈<strong>Z</strong>)，

当<em>x</em>＝2<em>k</em>π－(<em>k</em>∈<strong>Z</strong>)时，<em>f</em>(<em>x</em>)取得极小值，∴<em>x<sub>n</sub></em>＝2<em>n</em>π－(<em>n</em>∈<strong>N</strong><sup>\*</sup>)．

(2)∵<em>b<sub>n</sub></em>＝＝<em>n</em>－＝，

∴＝·＝3，

∴<em>S<sub>n</sub></em>＝3＝3＝－，

∴<em>S<sub>n</sub></em>&lt;．

4．数列{<em>a<sub>n</sub></em>}的前<em>n</em>项和记为<em>S<sub>n</sub></em>，且4<em>S<sub>n</sub></em>＝5<em>a<sub>n</sub></em>－5，数列{<em>b<sub>n</sub></em>}满足<em>b<sub>n</sub></em>＝log<sub>5</sub><em>a<sub>n</sub></em>．

(1)求数列{<em>a<sub>n</sub></em>}，{<em>b<sub>n</sub></em>}的通项公式；

(2)设<em>c<sub>n</sub></em>＝，数列{<em>c<sub>n</sub></em>}的前<em>n</em>项和为<em>T<sub>n</sub></em>，证明<em>T<sub>n</sub></em>&lt;1．

4．解析　(1)∵4<em>S<sub>n</sub></em>＝5<em>a<sub>n</sub></em>－5，∴4<em>a</em><sub>1</sub>＝5<em>a</em><sub>1</sub>－5，∴<em>a</em><sub>1</sub>＝5．

当<em>n</em>≥2时，4<em>S<sub>n</sub></em><sub>－1</sub>＝5<em>a<sub>n</sub></em><sub>－1</sub>－5，∴4<em>a<sub>n</sub></em>＝5<em>a<sub>n</sub></em>－5<em>a<sub>n</sub></em><sub>－1</sub>，∴<em>a<sub>n</sub></em>＝5<em>a<sub>n</sub></em><sub>－1</sub>，

∴{<em>a<sub>n</sub></em>}是以5为首项，5为公比的等比数列，∴<em>a<sub>n</sub></em>＝5·5<em><sup>n</sup></em><sup>－1</sup>＝5<em><sup>n</sup></em>．∴<em>b<sub>n</sub></em>＝log<sub>5</sub>5<em><sup>n</sup></em>＝<em>n</em>．

(2)∵<em>c<sub>n</sub></em>＝＝－，∴<em>T<sub>n</sub></em>＝＋＋…＋＝1－&lt;1．

5．设数列{<em>a<sub>n</sub></em>}的前<em>n</em>项和为<em>S<sub>n</sub></em>，<em>a</em><sub>1</sub>＝2，<em>a<sub>n</sub></em><sub>＋1</sub>＝2＋<em>S<sub>n</sub></em>(<em>n</em>∈<strong>N</strong><sup>\*</sup>)．

(1)求数列{<em>a<sub>n</sub></em>}的通项公式；

(2)设<em>b<sub>n</sub></em>＝1＋log<sub>2</sub>(<em>a<sub>n</sub></em>)<sup>2</sup>，求证：数列的前<em>n</em>项和<em>T<sub>n</sub></em>&lt;．

5．解析　(1)因为<em>a<sub>n</sub></em><sub>＋1</sub>＝2＋<em>S<sub>n</sub></em>(<em>n</em>∈<strong>N</strong><sup>\*</sup>)，所以<em>a<sub>n</sub></em>＝2＋<em>S<sub>n</sub></em><sub>－1</sub>(<em>n</em>≥2)，

所以<em>a<sub>n</sub></em><sub>＋1</sub>－<em>a<sub>n</sub></em>＝<em>S<sub>n</sub></em>－<em>S<sub>n</sub></em><sub>－1</sub>＝<em>a<sub>n</sub></em>，所以<em>a<sub>n</sub></em><sub>＋1</sub>＝2<em>a<sub>n</sub></em>(<em>n</em>≥2)．

又因为<em>a</em><sub>2</sub>＝2＋<em>a</em><sub>1</sub>＝4，<em>a</em><sub>1</sub>＝2，所以<em>a</em><sub>2</sub>＝2<em>a</em><sub>1</sub>，

所以数列{<em>a<sub>n</sub></em>}是以2为首项，2为公比的等比数列，则<em>a<sub>n</sub></em>＝2·2<em><sup>n</sup></em><sup>－1</sup>＝2<em><sup>n</sup></em>(<em>n</em>∈<strong>N</strong><sup>\*</sup>)．

(2)因<em>b<sub>n</sub></em>＝1＋log<sub>2</sub>(<em>a<sub>n</sub></em>)<sup>2</sup>，则<em>b<sub>n</sub></em>＝2<em>n</em>＋1．则＝，

所以<em>T<sub>n</sub></em>＝＝＝－&lt;．

6．已知数列{<em>a<sub>n</sub></em>}的前<em>n</em>项和为<em>S<sub>n</sub></em>，且<em>S<sub>n</sub></em>＝＋．

(1)求数列{<em>a<sub>n</sub></em>}的通项公式；

(2)若数列{<em>b<sub>n</sub></em>}满足<em>b<sub>n</sub></em>＝<em>a<sub>n</sub></em><sub>＋2</sub>－<em>a<sub>n</sub></em>＋，且数列{<em>b<sub>n</sub></em>}的前<em>n</em>项和为<em>T<sub>n</sub></em>，求证：<em>T<sub>n</sub></em>&lt;2<em>n</em>＋．

6．解析　(1)因为<em>S<sub>n</sub></em>＝＋，①．所以当<em>n</em>≥2时，<em>S<sub>n</sub></em><sub>－1</sub>＝＋，②

所以由①②两式相减得<em>a<sub>n</sub></em>＝<em>S<sub>n</sub></em>－<em>S<sub>n</sub></em><sub>－1</sub>＝＋－－＝<em>n</em>＋1．

又因为<em>n</em>＝1时，<em>a</em><sub>1</sub>＝<em>S</em><sub>1</sub>＝2适合<em>a<sub>n</sub></em>＝<em>n</em>＋1，所以<em>a<sub>n</sub></em>＝<em>n</em>＋1．

(2)由(1)知<em>b<sub>n</sub></em>＝<em>n</em>＋3－(<em>n</em>＋1)＋＝2＋，

所以<em>T<sub>n</sub></em>＝<em>b</em><sub>1</sub>＋<em>b</em><sub>2</sub>＋<em>b</em><sub>3</sub>＋…＋<em>b<sub>n</sub></em>＝2<em>n</em>＋

＝2*n*＋＝2*n*＋－<2*n*＋．

7．已知数列{<em>a<sub>n</sub></em>}满足<em>a</em><sub>1</sub>＝1，<em>S<sub>n</sub></em>＝2<em>a<sub>n</sub></em><sub>＋1</sub>，其中<em>S<sub>n</sub></em>为{<em>a<sub>n</sub></em>}的前<em>n</em>项和(<em>n</em>∈<strong>N</strong><sup>\*</sup>)．

(1)求<em>S</em><sub>1</sub>，<em>S</em><sub>2</sub>及数列{<em>S<sub>n</sub></em>}的通项公式；

(2)若数列{<em>b<sub>n</sub></em>}满足<em>b<sub>n</sub></em>＝，且{<em>b<sub>n</sub></em>}的前<em>n</em>项和为<em>T<sub>n</sub></em>，求证：当<em>n</em>≥2时，≤|<em>T<sub>n</sub></em>|≤．

7．解析　(1)易知<em>S</em><sub>1</sub>＝<em>a</em><sub>1</sub>＝1，且<em>S</em><sub>1</sub>＝2<em>a</em><sub>2</sub>，所以<em>a</em><sub>2</sub>＝，<em>S</em><sub>2</sub>＝<em>a</em><sub>1</sub>＋<em>a</em><sub>2</sub>＝．

因为<em>S<sub>n</sub></em>＝2<em>a<sub>n</sub></em><sub>＋1</sub>，所以<em>S<sub>n</sub></em>＝2<em>a<sub>n</sub></em><sub>＋1</sub>＝2(<em>S<sub>n</sub></em><sub>＋1</sub>－<em>S<sub>n</sub></em>)，即3<em>S<sub>n</sub></em>＝2<em>S<sub>n</sub></em><sub>＋1</sub>，

所以＝，即数列{<em>S<sub>n</sub></em>}是以1为首项，为公比的等比数列，所以<em>S<sub>n</sub></em>＝<em><sup>n</sup></em><sup>－1</sup>(<em>n</em>∈<strong>N</strong><sup>\*</sup>)．

(2)由(1)知，<em>b<sub>n</sub></em>＝＝－1×＝－<em><sup>n</sup></em><sup>－1</sup>，

|<em>T<sub>n</sub></em>|＝－1×．

而当<em>n</em>≥2时，1－≤1＋＋＋<sup>3</sup>＋…＋<em><sup>n</sup></em><sup>－1</sup>≤1＋＋＝，

即≤|<em>T<sub>n</sub></em>|≤．

8．数列{<em>a<sub>n</sub></em>}中，前<em>n</em>项和为<em>S<sub>n</sub></em>，<em>S<sub>n</sub></em>＝(<em>a</em><sub>2</sub>是常数，且<em>a</em><sub>2</sub>≠0)．

(1)求数列{<em>a<sub>n</sub></em>}的通项公式；

(2)令<em>b<sub>n</sub></em>＝＋，证明：2<em>n</em>&lt;<em>b</em><sub>1</sub>＋<em>b</em><sub>2</sub>＋…＋<em>b<sub>n</sub></em>&lt;2<em>n</em>＋3．

8．解析　(1)由题意知<em>S<sub>n</sub></em>＝，<em>S<sub>n</sub></em><sub>－1</sub>＝(<em>n</em>≥2)，

两式相减得<em>a<sub>n</sub></em>＝－，整理得(<em>n</em>－2)<em>a<sub>n</sub></em>＝(<em>n</em>－1)<em>a<sub>n</sub></em><sub>－1</sub>．

(叠乘法)因为＝(*n*≥3)，所以＝，＝，…，＝，

上述各式相乘，得＝<em>n</em>－1，且当<em>n</em>＝1，2时，满足此式，所以<em>a<sub>n</sub></em>＝(<em>n</em>－1)<em>a</em><sub>2</sub>．

(2)<em>b<sub>n</sub></em>＝＋＝＋，

因为<em>b<sub>n</sub></em>&gt;2，所以<em>b</em><sub>1</sub>＋<em>b</em><sub>2</sub>＋…＋<em>b<sub>n</sub></em>&gt;2<em>n</em>；

<em>b<sub>n</sub></em>＝＋＝1＋＋1－＝2＋2，

<em>b</em><sub>1</sub>＋<em>b</em><sub>2</sub>＋…＋<em>b<sub>n</sub></em>＝2<em>n</em>＋2＝2<em>n</em>＋2&lt;2<em>n</em>＋3．

综上，原不等式成立．

9．已知数列{<em>a<sub>n</sub></em>}的前<em>n</em>项和<em>S<sub>n</sub></em>满足：2<em>S<sub>n</sub></em>＋<em>a<sub>n</sub></em>＝1．

(1)求数列{<em>a<sub>n</sub></em>}的通项公式；

(2)设<em>b<sub>n</sub></em>＝，数列{<em>b<sub>n</sub></em>}的前<em>n</em>项和为T<em><sub>n</sub></em>，求证：<em>T<sub>n</sub></em>＜．

9．解析　(1)因为2<em>S<sub>n</sub></em>＋<em>a<sub>n</sub></em>＝1，所以2<em>S<sub>n</sub></em><sub>＋1</sub>＋<em>a<sub>n</sub></em><sub>＋1</sub>＝1，

两式相减可得2<em>a<sub>n</sub></em><sub>＋1</sub>＋<em>a<sub>n</sub></em><sub>＋1</sub>－<em>a<sub>n</sub></em>＝0，即3<em>a<sub>n</sub></em><sub>＋1</sub>＝<em>a<sub>n</sub></em>，即＝，

又2<em>S</em><sub>1</sub>＋<em>a</em><sub>1</sub>＝1，所以<em>a</em><sub>1</sub>＝，所以数列{<em>a<sub>n</sub></em>}是首项、公比均为的等比数列．

故<em>a<sub>n</sub></em>＝·()<em><sup>n</sup></em><sup>－1</sup>＝()<em><sup>n</sup></em>，数列{<em>a<sub>n</sub></em>}的通项公式为<em>a<sub>n</sub></em>＝()<em><sup>n</sup></em>．

(2)因为<em>b<sub>n</sub></em>＝，

所以<em>b<sub>n</sub></em>＝＝＝＝－．

故<em>T<sub>n</sub></em>＝<em>b</em><sub>1</sub>＋<em>b</em><sub>2</sub>＋…＋<em>b<sub>n</sub></em>＝(－)＋(－)＋…＋(－)＝－＜．

所以<em>T<sub>n</sub></em>＜．

10．已知数列{<em>a<sub>n</sub></em>}与{<em>b<sub>n</sub></em>}满足：<em>a</em><sub>1</sub>＋<em>a</em><sub>2</sub>＋<em>a</em><sub>3</sub>＋…＋<em>a<sub>n</sub></em>＝2<em>b<sub>n</sub></em>(<em>n</em>∈<strong>N</strong><sup>\*</sup>)，若{<em>a<sub>n</sub></em>}是各项为正数的等比数列，且<em>a</em><sub>1</sub>

＝2，<em>b</em><sub>3</sub>＝<em>b</em><sub>2</sub>＋4．

(1)求数列{<em>a<sub>n</sub></em>}与{<em>b<sub>n</sub></em>}的通项公式；

(2)若数列{<em>c<sub>n</sub></em>}满足<em>c<sub>n</sub></em>＝(<em>n</em>∈<strong>N</strong><sup>\*</sup>)，<em>T<sub>n</sub></em>为数列{<em>c<sub>n</sub></em>}的前<em>n</em>项和，证明：<em>T<sub>n</sub></em>＜1．

10．解析　(1)由题意知，<em>a</em><sub>1</sub>＋<em>a</em><sub>2</sub>＋<em>a</em><sub>3</sub>＋…＋<em>a<sub>n</sub></em>＝2<em>b<sub>n</sub></em>，①

当<em>n</em>≥2时，<em>a</em><sub>1</sub>＋<em>a</em><sub>2</sub>＋<em>a</em><sub>3</sub>＋…＋<em>a<sub>n</sub></em><sub>－1</sub>＝2<em>b<sub>n</sub></em><sub>－1</sub>，②

①－②可得<em>a<sub>n</sub></em>＝2(<em>b<sub>n</sub></em>－<em>b<sub>n</sub></em><sub>－1</sub>)⇒<em>a</em><sub>3</sub>＝2(<em>b</em><sub>3</sub>－<em>b</em><sub>2</sub>)＝2×4＝8，

∵<em>a</em><sub>1</sub>＝2，<em>a<sub>n</sub></em>＞0，设{<em>a<sub>n</sub></em>}的公比为<em>q</em>，∴<em>a</em><sub>1</sub><em>q</em><sup>2</sup>＝8⇒<em>q</em>＝2，∴<em>a<sub>n</sub></em>＝2×2<em><sup>n</sup></em><sup>－1</sup>＝2<em><sup>n</sup></em>(<em>n</em>∈<strong>N</strong><sup>\*</sup>)．

∴2<em>b<sub>n</sub></em>＝2<sup>1</sup>＋2<sup>2</sup>＋2<sup>3</sup>＋…＋2<em><sup>n</sup></em>＝＝2<em><sup>n</sup></em><sup>＋1</sup>－2，∴<em>b<sub>n</sub></em>＝2<em><sup>n</sup></em>－1(<em>n</em>∈<strong>N</strong><sup>\*</sup>)．

(2)由已知<em>c<sub>n</sub></em>＝＝＝－，

∴<em>T<sub>n</sub></em>＝<em>c</em><sub>1</sub>＋<em>c</em><sub>2</sub>＋…＋<em>c<sub>n</sub></em>＝＋＋…＋＝1－，

当<em>n</em>∈<strong>N</strong><sup>\*</sup>时，2<em><sup>n</sup></em><sup>＋1</sup>＞1，∴＞0，∴1－＜1，故<em>T<sub>n</sub></em>＜1．

**考点二　先求和(错位相减法)再放缩**

**【基本题型】**

<strong>[例12]</strong>　(2021·全国乙)设{<em>a<sub>n</sub></em>}是首项为1的等比数列，数列{<em>b<sub>n</sub></em>}满足<em>b<sub>n</sub></em>＝．已知<em>a</em><sub>1</sub>，3<em>a</em><sub>2</sub>，9<em>a</em><sub>3</sub>成等差数列．

(1)求{<em>a<sub>n</sub></em>}和{<em>b<sub>n</sub></em>}的通项公式；

(2)记<em>S<sub>n</sub></em>和<em>T<sub>n</sub></em>分别为{<em>a<sub>n</sub></em>}和{<em>b<sub>n</sub></em>}的前<em>n</em>项和．证明：<em>T<sub>n</sub></em>&lt;．

解析　(1)设{<em>a<sub>n</sub></em>}的公比为<em>q</em>，则<em>a<sub>n</sub></em>＝<em>q<sup>n</sup></em><sup>－1</sup>．

因为<em>a</em><sub>1</sub>，3<em>a</em><sub>2</sub>，9<em>a</em><sub>3</sub>成等差数列，所以1＋9<em>q</em><sup>2</sup>＝2×3<em>q</em>，解得<em>q</em>＝，

故<em>a<sub>n</sub></em>＝，<em>b<sub>n</sub></em>＝．

(2)由(1)知<em>S<sub>n</sub></em>＝＝，

<em>T<sub>n</sub></em>＝＋＋＋…＋，①

<em>T<sub>n</sub></em>＝＋＋＋…＋＋，②

①－②得<em>T<sub>n</sub></em>＝＋＋＋…＋－，即<em>T<sub>n</sub></em>＝－＝－，

整理得<em>T<sub>n</sub></em>＝－，则2<em>T<sub>n</sub></em>－<em>S<sub>n</sub></em>＝2－＝－&lt;0，故<em>T<sub>n</sub></em>&lt;．

<strong>[例13]</strong>　已知数列{<em>a<sub>n</sub></em>}的首项<em>a</em><sub>1</sub>＝3，前<em>n</em>项和为<em>S<sub>n</sub></em>，<em>a<sub>n</sub></em><sub>＋1</sub>＝2<em>S<sub>n</sub></em>＋3，<em>n</em>∈<strong>N</strong><sup>\*</sup>．

(1)求数列{<em>a<sub>n</sub></em>}的通项公式；

(2)设<em>b<sub>n</sub></em>＝log<sub>3</sub><em>a<sub>n</sub></em>，求数列的前<em>n</em>项和<em>T<sub>n</sub></em>，并证明：≤<em>T<sub>n</sub></em>＜．

解析　(1)由<em>a<sub>n</sub></em><sub>＋1</sub>＝2<em>S<sub>n</sub></em>＋3，得<em>a<sub>n</sub></em>＝2<em>S<sub>n</sub></em><sub>－1</sub>＋3(<em>n</em>≥2)，

两式相减得<em>a<sub>n</sub></em><sub>＋1</sub>－<em>a<sub>n</sub></em>＝2(<em>S<sub>n</sub></em>－<em>S<sub>n</sub></em><sub>－1</sub>)＝2<em>a<sub>n</sub></em>，故<em>a<sub>n</sub></em><sub>＋1</sub>＝3<em>a<sub>n</sub></em>(<em>n</em>≥2)，

所以当<em>n</em>≥2时，{<em>a<sub>n</sub></em>}是以3为公比的等比数列．

因为<em>a</em><sub>2</sub>＝2<em>S</em><sub>1</sub>＋3＝2<em>a</em><sub>1</sub>＋3＝9，＝3，所以{<em>a<sub>n</sub></em>}是首项为3，公比为3的等比数列，<em>a<sub>n</sub></em>＝3<em><sup>n</sup></em>．

(2)<em>a<sub>n</sub></em>＝3<em><sup>n</sup></em>，故<em>b<sub>n</sub></em>＝log<sub>3</sub><em>a<sub>n</sub></em>＝log<sub>3</sub>3<em><sup>n</sup></em>＝<em>n</em>，＝＝<em>n</em>·<em><sup>n</sup></em>，

<em>T<sub>n</sub></em>＝1×＋2×<sup>2</sup>＋3×<sup>3</sup>＋…＋<em>n</em>×<em><sup>n</sup></em>，①

<em>T<sub>n</sub></em>＝1×<sup>2</sup>＋2×<sup>3</sup>＋3×<sup>4</sup>＋…＋(<em>n</em>－1)×<em><sup>n</sup></em>＋<em>n</em>×<em><sup>n</sup></em><sup>＋1</sup>．②

①－②，得<em>T<sub>n</sub></em>＝＋<sup>2</sup>＋<sup>3</sup>＋…＋<em><sup>n</sup></em>－<em>n</em>×<em><sup>n</sup></em><sup>＋1</sup>＝－<em>n</em>×<em><sup>n</sup></em><sup>＋1</sup>＝－＋<em>n<sup>n</sup></em><sup>＋1</sup>，

所以<em>T<sub>n</sub></em>＝－<em><sup>n</sup></em>．

因为<em><sup>n</sup></em>＞0，所以<em>T<sub>n</sub></em>＜．又因为<em>T<sub>n</sub></em><sub>＋1</sub>－<em>T<sub>n</sub></em>＝＞0，

所以数列{<em>T<sub>n</sub></em>}单调递增，所以(<em>T<sub>n</sub></em>)<sub>min</sub>＝<em>T</em><sub>1</sub>＝，所以≤<em>T<sub>n</sub></em>＜．

**【对点精练】**

11．已知{<em>a<sub>n</sub></em>}是等差数列，{<em>b<sub>n</sub></em>}是等比数列，<em>a</em><sub>1</sub>＝1，<em>b</em><sub>1</sub>＝2，<em>b</em><sub>2</sub>＝2<em>a</em><sub>2</sub>，<em>b</em><sub>3</sub>＝2<em>a</em><sub>3</sub>＋2．

(1)求{<em>a<sub>n</sub></em>}，{<em>b<sub>n</sub></em>}的通项公式；

(2)若的前<em>n</em>项和为<em>S<sub>n</sub></em>，求证：<em>S<sub>n</sub></em>&lt;2．

11．解析　(1)设{<em>a<sub>n</sub></em>}的公差为<em>d</em>，{<em>b<sub>n</sub></em>}的公比为<em>q</em>，由题意得

解得或(舍)，∴<em>a<sub>n</sub></em>＝<em>n</em>，<em>b<sub>n</sub></em>＝2<em><sup>n</sup></em>．

(2)由(1)知＝，

∴<em>S<sub>n</sub></em>＝＋＋＋…＋＋，

<em>S<sub>n</sub></em>＝＋＋＋…＋＋＋，

两式相减得<em>S<sub>n</sub></em>＝＋＋＋＋…＋－＝－，

∴<em>S<sub>n</sub></em>＝2－<em><sup>n</sup></em><sup>－1</sup>－，∴<em>S<sub>n</sub></em>&lt;2．

12．已知数列{<em>a<sub>n</sub></em>}是公差不为零的等差数列，<em>a</em><sub>10</sub>＝15，且<em>a</em><sub>3</sub>，<em>a</em><sub>4</sub>，<em>a</em><sub>7</sub>成等比数列．

(1)求数列{<em>a<sub>n</sub></em>}的通项公式；

(2)设<em>b<sub>n</sub></em>＝，数列{<em>b<sub>n</sub></em>}的前<em>n</em>项和为<em>T<sub>n</sub></em>，求证：－≤<em>T<sub>n</sub></em>＜－1(<em>n</em>∈<strong>N</strong><sup>\*</sup>)．

12．解析　(1)设数列{<em>a<sub>n</sub></em>}的公差为<em>d</em>(<em>d</em>≠0)，由已知得即

解得∴<em>a<sub>n</sub></em>＝2<em>n</em>－5(<em>n</em>∈<strong>N</strong><sup>\*</sup>)．

(2)∵<em>b<sub>n</sub></em>＝＝，<em>n</em>∈<strong>N</strong><sup>\*</sup>．

∴<em>T<sub>n</sub></em>＝＋＋＋…＋，①

<em>T<sub>n</sub></em>＝＋＋＋…＋＋，②

①－②得<em>T<sub>n</sub></em>＝＋2－＝－＋，

∴<em>T<sub>n</sub></em>＝－1－(<em>n</em>∈N<sup>\*</sup>)，∵＞0(<em>n</em>∈<strong>N</strong><sup>\*</sup>)，∴<em>T<sub>n</sub></em>＜－1．

<em>T<sub>n</sub></em><sub>＋1</sub>－<em>T<sub>n</sub></em>＝－＝，∴<em>T<sub>n</sub></em>＜<em>T<sub>n</sub></em><sub>＋1</sub>(<em>n</em>≥2)．

又<em>T</em><sub>1</sub>＝－1－＝－，<em>T</em><sub>2</sub>＝－1－＝－．∵<em>T</em><sub>1</sub>＞<em>T</em><sub>2</sub>，∴<em>T</em><sub>2</sub>最小，即<em>T<sub>n</sub></em>≥<em>T</em><sub>2</sub>＝－．

综上所述，－≤<em>T<sub>n</sub></em>＜－1(<em>n</em>∈<strong>N</strong><sup>\*</sup>)．

13．已知函数*f*(*x*)满足*f*(*x*＋*y*)＝*f*(*x*)·*f*(*y*)且*f*(1)＝．

(1)当<em>n</em>∈<strong>N</strong><sup>\*</sup>时，求<em>f</em>(<em>n</em>)的表达式；

(2)设<em>a<sub>n</sub></em>＝<em>n</em>·<em>f</em>(<em>n</em>)，<em>n</em>∈<strong>N</strong><sup>\*</sup>，求证：<em>a</em><sub>1</sub>＋<em>a</em><sub>2</sub>＋<em>a</em><sub>3</sub>＋…＋<em>a<sub>n</sub></em>&lt;2．

13．解析　(1)因为函数*f*(*x*)满足*f*(*x*＋*y*)＝*f*(*x*)·*f*(*y*)，

所以令*y*＝1，得*f*(*x*＋1)＝*f*(*x*)·*f*(1)，所以*f*(*n*＋1)＝*f*(*n*)·*f*(1)．又因为*f*(1)＝，

所以＝，所以<em>f</em>(<em>n</em>)＝<em><sup>n</sup></em>(<em>n</em>∈<strong>N</strong><sup>\*</sup>)．

(2)由(1)得<em>a<sub>n</sub></em>＝<em>n</em>·<em><sup>n</sup></em>，设<em>T<sub>n</sub></em>＝<em>a</em><sub>1</sub>＋<em>a</em><sub>2</sub>＋<em>a</em><sub>3</sub>＋…＋<em>a<sub>n</sub></em><sub>－1</sub>＋<em>a<sub>n</sub></em>，

则<em>T<sub>n</sub></em>＝1×＋2×<sup>2</sup>＋3×<sup>3</sup>＋…＋(<em>n</em>－1)×<em><sup>n</sup></em><sup>－1</sup>＋<em>n</em>×<em><sup>n</sup></em>，①

所以<em>T<sub>n</sub></em>＝1×<sup>2</sup>＋2×<sup>3</sup>＋…＋(<em>n</em>－2)<em><sup>n</sup></em><sup>－1</sup>＋(<em>n</em>－1)×<em><sup>n</sup></em>＋<em>n</em>×<em><sup>n</sup></em><sup>＋1</sup>，②

所以由①－②得<em>T<sub>n</sub></em>＝＋<sup>2</sup>＋<sup>3</sup>＋…＋<em><sup>n</sup></em><sup>－1</sup>＋<em><sup>n</sup></em>－<em>n</em>·<em><sup>n</sup></em><sup>＋1</sup>

＝－<em>n</em>·<em><sup>n</sup></em><sup>＋1</sup>＝1－<em><sup>n</sup></em>－<em>n</em>·<em><sup>n</sup></em><sup>＋1</sup>＝1－，

所以<em>T<sub>n</sub></em>＝2－&lt;2，即<em>a</em><sub>1</sub>＋<em>a</em><sub>2</sub>＋<em>a</em><sub>3</sub>＋…＋<em>a<sub>n</sub></em><sub>－1</sub>＋<em>a<sub>n</sub></em>&lt;2．

**考点三　先放缩再求和**

**【基本题型】**

<strong>[例14]</strong>　已知等比数列{<em>a<sub>n</sub></em>}的前<em>n</em>项和为<em>S<sub>n</sub></em>(<em>n</em>∈<strong>N</strong><sup>\*</sup>)，满足<em>S</em><sub>4</sub>＝2<em>a</em><sub>4</sub>－1，<em>S</em><sub>3</sub>＝2<em>a</em><sub>3</sub>－1．

(1)求{<em>a<sub>n</sub></em>}的通项公式；

(2)记<em>b<sub>n</sub></em>＝log<sub>2</sub>(<em>n</em>∈<strong>N</strong><sup>\*</sup>)，数列{<em>b<sub>n</sub></em>}的前<em>n</em>项和为<em>T<sub>n</sub></em>，求证：＋＋…＋&lt;2．

解析　(1)设{<em>a<sub>n</sub></em>}的公比为<em>q</em>，由<em>S</em><sub>4</sub>－<em>S</em><sub>3</sub>＝<em>a</em><sub>4</sub>，<em>S</em><sub>4</sub>＝2<em>a</em><sub>4</sub>－1得，2<em>a</em><sub>4</sub>－2<em>a</em><sub>3</sub>＝<em>a</em><sub>4</sub>，

所以＝2，所以<em>q</em>＝2．又因为<em>S</em><sub>3</sub>＝2<em>a</em><sub>3</sub>－1，

所以<em>a</em><sub>1</sub>＋2<em>a</em><sub>1</sub>＋4<em>a</em><sub>1</sub>＝8<em>a</em><sub>1</sub>－1，所以<em>a</em><sub>1</sub>＝1，所以<em>a<sub>n</sub></em>＝2<em><sup>n</sup></em><sup>－1</sup>(<em>n</em>∈<strong>N</strong><sup>\*</sup>)．

(2)由(1)知<em>b<sub>n</sub></em>＝log<sub>2</sub>(<em>a<sub>n</sub></em><sub>＋1</sub>·<em>a<sub>n</sub></em>)＝log<sub>2</sub>(2<em><sup>n</sup></em>×2<em><sup>n</sup></em><sup>－1</sup>)＝2<em>n</em>－1，所以<em>T<sub>n</sub></em>＝<em>n</em>＝<em>n</em><sup>2</sup>，

所以＋＋…＋＝＋＋…＋<1＋＋＋…＋

＝1＋1－＋－＋…＋－＝2－<2．

<strong>[例15]</strong>　已知数列{<em>a<sub>n</sub></em>}的前<em>n</em>项和为<em>S<sub>n</sub></em>，<em>a</em><sub>1</sub>＝，2<em>S<sub>n</sub></em>＝(<em>n</em>＋1)<em>a<sub>n</sub></em>＋1(<em>n</em>≥2)．

(1)求{<em>a<sub>n</sub></em>}的通项公式；

(2)设<em>b<sub>n</sub></em>＝(<em>n</em>∈<strong>N</strong><sup>\*</sup>)，数列{<em>b<sub>n</sub></em>}的前<em>n</em>项和为<em>T<sub>n</sub></em>，证明：<em>T<sub>n</sub></em>&lt;(<em>n</em>∈<strong>N</strong><sup>\*</sup>)．

解析　(1)当<em>n</em>＝2时，2(<em>a</em><sub>1</sub>＋<em>a</em><sub>2</sub>)＝3<em>a</em><sub>2</sub>＋1，解得<em>a</em><sub>2</sub>＝2．

当<em>n</em>≥3时，2<em>a<sub>n</sub></em>＝2<em>S<sub>n</sub></em>－2<em>S<sub>n</sub></em><sub>－1</sub>＝(<em>n</em>＋1)<em>a<sub>n</sub></em>－<em>na<sub>n</sub></em><sub>－1</sub>，∴(<em>n</em>－1)<em>a<sub>n</sub></em>＝<em>na<sub>n</sub></em><sub>－1</sub>，∴＝，

∴＝，＝，…，＝，将以上各式相乘得＝，∴<em>a<sub>n</sub></em>＝<em>n</em>．

显然，当<em>n</em>＝1时，上式不成立，当<em>n</em>＝2时，上式成立．∴<em>a<sub>n</sub></em>＝

(2) <em>b<sub>n</sub></em>＝＝当<em>n</em>≥2时，<em>b<sub>n</sub></em>＝&lt;＝－，

∴<em>T<sub>n</sub></em>＝＋＋＋…＋＝＋－＝－&lt;&lt;．

<strong>[例16]</strong>　(2014·全国Ⅱ)已知数列{<em>a<sub>n</sub></em>}满足<em>a</em><sub>1</sub>＝1，<em>a<sub>n</sub></em><sub>＋1</sub>＝3<em>a<sub>n</sub></em>＋1．

(1)证明是等比数列，并求{<em>a<sub>n</sub></em>}的通项公式；

(2)证明＋＋…＋<．

解析　(1)由<em>a<sub>n</sub></em><sub>＋1</sub>＝3<em>a<sub>n</sub></em>＋1得<em>a<sub>n</sub></em><sub>＋1</sub>＋＝3．

又<em>a</em><sub>1</sub>＋＝，所以是首项为，公比为3的等比数列．

<em>a<sub>n</sub></em>＋＝，因此{<em>a<sub>n</sub></em>}的通项公式为<em>a<sub>n</sub></em>＝．

(2)由(1)知＝．因为当<em>n</em>≥1时，3<em><sup>n</sup></em>－1≥2×3<em><sup>n</sup></em><sup>－1</sup>，所以≤．

于是＋＋…＋≤1＋＋…＋＝<．所以＋＋…＋<．

方法二　当*n*≥2时，<＝，

∴<em>S</em><sub>1</sub>＋<em>S</em><sub>2</sub>＋<em>S</em><sub>3</sub>＋…＋<em>S<sub>n</sub></em>&lt;＋

＝＋<＋＝<1．∴原命题得证．

<strong>[例17]</strong>　(2016·四川)已知数列{<em>a<sub>n</sub></em>}的首项为1，<em>S<sub>n</sub></em>为数列{<em>a<sub>n</sub></em>}的前<em>n</em>项和，<em>S<sub>n</sub></em><sub>＋1</sub>＝<em>qS<sub>n</sub></em>＋1，其中<em>q</em>&gt;0，<em>n</em>∈<strong>N</strong><sup>\*</sup>．

(1)若2<em>a</em><sub>2</sub>，<em>a</em><sub>3</sub>，<em>a</em><sub>2</sub>＋2成等差数列，求数列{<em>a<sub>n</sub></em>}的通项公式；

(2)设双曲线<em>x</em><sup>2</sup>－＝1的离心率为<em>e<sub>n</sub></em>，且<em>e</em><sub>2</sub>＝，证明：<em>e</em><sub>1</sub>＋<em>e</em><sub>2</sub>＋…＋<em>e<sub>n</sub></em>&gt;．

解析　(1)由已知<em>S<sub>n</sub></em><sub>＋1</sub>＝<em>qS<sub>n</sub></em>＋1，得<em>S<sub>n</sub></em><sub>＋2</sub>＝<em>qS<sub>n</sub></em><sub>＋1</sub>＋1，两式相减得到<em>a<sub>n</sub></em><sub>＋2</sub>＝<em>qa<sub>n</sub></em><sub>＋1</sub>，<em>n</em>≥1．

又由<em>S</em><sub>2</sub>＝<em>qS</em><sub>1</sub>＋1得到<em>a</em><sub>2</sub>＝<em>qa</em><sub>1</sub>，故<em>a<sub>n</sub></em><sub>＋1</sub>＝<em>qa<sub>n</sub></em>对所有<em>n</em>≥1都成立．

所以，数列{<em>a<sub>n</sub></em>}是首项为1，公比为<em>q</em>的等比数列．从而<em>a<sub>n</sub></em>＝<em>q<sup>n</sup></em><sup>－1</sup>．

由2<em>a</em><sub>2</sub>，<em>a</em><sub>3</sub>，<em>a</em><sub>2</sub>＋2成等差数列，可得2<em>a</em><sub>3</sub>＝3<em>a</em><sub>2</sub>＋2，即2<em>q</em><sup>2</sup>＝3<em>q</em>＋2，则(2<em>q</em>＋1)(<em>q</em>－2)＝0，

由已知，<em>q</em>&gt;0，故<em>q</em>＝2．所以<em>a<sub>n</sub></em>＝2<em><sup>n</sup></em><sup>－1</sup>(<em>n</em>∈<strong>N</strong><sup>\*</sup>)．

(2)由(1)可知，<em>a<sub>n</sub></em>＝<em>q<sup>n</sup></em><sup>－1</sup>．所以双曲线<em>x</em><sup>2</sup>－＝1的离心率<em>e<sub>n</sub></em>＝＝．

由<em>e</em><sub>2</sub>＝＝，解得<em>q</em>＝．

因为1＋<em>q</em><sup>2(</sup><em><sup>k</sup></em><sup>－1)</sup>&gt;<em>q</em><sup>2(</sup><em><sup>k</sup></em><sup>－1)</sup>，所以&gt;<em>q<sup>k</sup></em><sup>－1</sup>(<em>k</em>∈<strong>N</strong><sup>\*</sup>)．

于是<em>e</em><sub>1</sub>＋<em>e</em><sub>2</sub>＋…＋<em>e<sub>n</sub></em>&gt;1＋<em>q</em>＋…＋<em>q<sup>n</sup></em><sup>－1</sup>＝．故<em>e</em><sub>1</sub>＋<em>e</em><sub>2</sub>＋…＋<em>e<sub>n</sub></em>&gt;．

**【对点精练】**

14．数列{<em>a<sub>n</sub></em>}满足<em>a<sub>n</sub></em><sub>＋1</sub>＝，<em>a</em><sub>1</sub>＝1．

(1)证明：数列是等差数列；

(2)求数列的前<em>n</em>项和<em>S<sub>n</sub></em>，并证明：＋＋…＋＞．

14．解析　∵<em>a<sub>n</sub></em><sub>＋1</sub>＝，∴＝，化简得＝2＋，即－＝2，

故数列是以1为首项，2为公差的等差数列．

(2)由(1)知＝2<em>n</em>－1，所以<em>S<sub>n</sub></em>＝＝<em>n</em><sup>2</sup>．

＋＋…＋＝＋＋…＋＞＋＋…＋

＝＋＋…＋＝1－＝．

15．已知数列{<em>a<sub>n</sub></em>}中，<em>a</em><sub>1</sub>＝，其前<em>n</em>项的和为<em>S<sub>n</sub></em>，且满足<em>a<sub>n</sub></em>＝(<em>n</em>≥2)．

(1)求证：数列是等差数列；

(2)证明：<em>S</em><sub>1</sub>＋<em>S</em><sub>2</sub>＋<em>S</em><sub>3</sub>＋…＋<em>S<sub>n</sub></em>&lt;1．

15．解析　(1)当<em>n</em>≥2时，<em>S<sub>n</sub></em>－<em>S<sub>n</sub></em><sub>－1</sub>＝，整理得<em>S<sub>n</sub></em><sub>－1</sub>－<em>S<sub>n</sub></em>＝2<em>S<sub>n</sub></em>·<em>S<sub>n</sub></em><sub>－1</sub>(<em>n</em>≥2)，

∴－＝2，从而构成以2为首项，2为公差的等差数列．

(2)由(1)可知，＝＋(<em>n</em>－1)×2＝2<em>n</em>，∴<em>S<sub>n</sub></em>＝．∴当<em>n</em>＝1时，<em>S<sub>n</sub></em>＝&lt;1，

方法一　当<em>n</em>≥2时，<em>S<sub>n</sub></em>＝&lt;·＝，

∴<em>S</em><sub>1</sub>＋<em>S</em><sub>2</sub>＋<em>S</em><sub>3</sub>＋…＋<em>S<sub>n</sub></em> &lt;＋＝1－&lt;1．

∴原不等式得证．

16．已知数列{<em>a<sub>n</sub></em>}满足<em>a</em><sub>1</sub>＝2，<em>a<sub>n</sub></em><sub>＋1</sub>＝2(<em>S<sub>n</sub></em>＋<em>n</em>＋1)(<em>n</em>∈<strong>N</strong><sup>\*</sup>)，令<em>b<sub>n</sub></em>＝<em>a<sub>n</sub></em>＋1．

(1)求证：{<em>b<sub>n</sub></em>}是等比数列；

(2)记数列{<em>nb<sub>n</sub></em>}的前<em>n</em>项和为<em>T<sub>n</sub></em>，求<em>T<sub>n</sub></em>；

(3)求证：－<＋＋＋…＋<．

16．解析　(1) <em>a</em><sub>1</sub>＝2，<em>a</em><sub>2</sub>＝2(2＋2)＝8，<em>a<sub>n</sub></em><sub>＋1</sub>＝2(<em>S<sub>n</sub></em>＋<em>n</em>＋1)(<em>n</em>∈<strong>N</strong><sup>\*</sup>)，<em>a<sub>n</sub></em>＝2(<em>S<sub>n</sub></em><sub>－1</sub>＋<em>n</em>)(<em>n</em>≥2)，

两式相减，得<em>a<sub>n</sub></em><sub>＋1</sub>＝3<em>a<sub>n</sub></em>＋2(<em>n</em>≥2)．经检验，当<em>n</em>＝1时上式也成立，

即<em>a<sub>n</sub></em><sub>＋1</sub>＝3<em>a<sub>n</sub></em>＋2(<em>n</em>≥1)．所以<em>a<sub>n</sub></em><sub>＋1</sub>＋1＝3(<em>a<sub>n</sub></em>＋1)，即<em>b<sub>n</sub></em><sub>＋1</sub>＝3<em>b<sub>n</sub></em>，且<em>b</em><sub>1</sub>＝3．

故{<em>b<sub>n</sub></em>}是首项为3，公比为3的等比数列．

(2)由(1)得<em>b<sub>n</sub></em>＝3<em><sup>n</sup></em>，<em>nb<sub>n</sub></em>＝<em>n</em>·3<em><sup>n</sup></em>．

<em>T<sub>n</sub></em>＝1×3＋2×3<sup>2</sup>＋3×3<sup>3</sup>＋…＋<em>n</em>×3<em><sup>n</sup></em>，

3<em>T<sub>n</sub></em>＝1×3<sup>2</sup>＋2×3<sup>3</sup>＋3×3<sup>4</sup>＋…＋<em>n</em>×3<em><sup>n</sup></em><sup>＋1</sup>，

两式相减，得－2<em>T<sub>n</sub></em>＝3＋3<sup>2</sup>＋3<sup>3</sup>＋…＋3<em><sup>n</sup></em>－<em>n</em>×3<em><sup>n</sup></em><sup>＋1</sup>＝－<em>n</em>×3<em><sup>n</sup></em><sup>＋1</sup>，

化简得<em>T<sub>n</sub></em>＝×3<em><sup>n</sup></em>＋．

(3)由＝>，得＋＋＋…＋>＋＋…＋＝＝－×．

又＝＝<＝，

所以＋＋＋…＋<＋

＝＋＝＋－×<，

故－<＋＋＋…＋<．

17．已知数列{<em>a<sub>n</sub></em>}满足<em>a</em><sub>1</sub>＝，<em>a<sub>n</sub></em><sub>＋1</sub>＝，<em>n</em>∈<strong>N</strong><sup>\*</sup>．

(1)求<em>a</em><sub>2</sub>；

(2)求的通项公式；

(3)设{<em>a<sub>n</sub></em>}的前<em>n</em>项和为<em>S<sub>n</sub></em>，求证：≤<em>S<sub>n</sub></em>&lt;．

17．解析　(1)由条件可得<em>a</em><sub>2</sub>＝＝．

(2)由<em>a<sub>n</sub></em><sub>＋1</sub>＝得＝·－，所以－1＝，又－1＝，

所以是以首项为，公比为的等比数列，因此，＝<em><sup>n</sup></em>＋1．

(3)由(2)可得<em>a<sub>n</sub></em>＝≥＝×<em><sup>n</sup></em><sup>－1</sup>，

所以<em>S<sub>n</sub></em>＝<em>a</em><sub>1</sub>＋<em>a</em><sub>2</sub>＋…＋<em>a<sub>n</sub></em>≥＋·<sup>1</sup>＋…＋·<em><sup>n</sup></em><sup>－1</sup>＝．

又<em>a<sub>n</sub></em>＝&lt;＝<em><sup>n</sup></em>，

所以<em>S<sub>n</sub></em>＝<em>a</em><sub>1</sub>＋<em>a</em><sub>2</sub>＋<em>a</em><sub>3</sub>＋…＋<em>a<sub>n</sub></em>&lt;＋＋<sup>3</sup>＋…＋<em><sup>n</sup></em>＝＋－·<em><sup>n</sup></em><sup>－2</sup>&lt;，<em>n</em>≥3，

又<em>S</em><sub>1</sub>＝&lt;，<em>S</em><sub>2</sub>＝&lt;，因此，<em>S<sub>n</sub></em>&lt;，<em>n</em>∈<strong>N</strong><sup>\*</sup>．

综上，≤<em>S<sub>n</sub></em>&lt;．

