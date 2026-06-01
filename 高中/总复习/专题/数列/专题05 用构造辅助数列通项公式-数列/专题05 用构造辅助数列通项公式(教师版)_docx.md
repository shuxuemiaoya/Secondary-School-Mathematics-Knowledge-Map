专题5　用构造辅助数列通项公式

![](images/8ad4e2fac21f52b9222fc2beaa66f72a9cc6cca24af1e0015bfc7e0ceca0263c.jpg)

<strong>考点一　由</strong><em><strong>a<sub>n</sub></strong></em><strong><sub>＋1</sub>＝</strong><em><strong>Aa<sub>n</sub></strong></em><strong>＋</strong><em><strong>B</strong></em><strong>(</strong><em><strong>A</strong></em><strong>≠0且</strong><em><strong>A</strong></em><strong>≠1，</strong><em><strong>B</strong></em><strong>≠0)求</strong><em><strong>a<sub>n</sub></strong></em><strong>型</strong>

【基本方法】

已知<em>a<sub>n</sub></em><sub>＋1</sub>＝<em>Aa<sub>n</sub></em>＋<em>B</em>求<em>a<sub>n</sub></em>的方法1

递推关系形如<em>a<sub>n</sub></em><sub>＋1</sub>＝<em>Aa<sub>n</sub></em>＋<em>B</em>(<em>A</em>≠0且<em>A</em>≠1，<em>B</em>≠0，<em>A</em>，<em>B</em>为常数)可化为<em>a<sub>n</sub></em><sub>＋1</sub>＋＝<em>A</em>(<em>p</em>≠1)的形式，利用是以<em>A</em>为公比的等比数列求解．

已知<em>a<sub>n</sub></em><sub>＋1</sub>＝<em>Aa<sub>n</sub></em>＋<em>B</em>求<em>a<sub>n</sub></em>的方法2

对于一个函数*f*(*x*)，我们把满足*f*(*m*)＝*m*的值*x*＝*m*称为函数*f*(*x*)的“不动点”．利用“不动点法”可以构造新数列，求数列的通项公式．
若<em>f</em>(<em>x</em>)＝<em>Ax</em>＋<em>B</em>(<em>A</em>≠0，1)，<em>p</em>是<em>f</em>(<em>x</em>)的不动点．数列{<em>a<sub>n</sub></em>}满足<em>a<sub>n</sub></em><sub>＋1</sub>＝<em>f</em>(<em>a<sub>n</sub></em>)，则<em>a<sub>n</sub></em><sub>＋1</sub>－<em>p</em>＝<em>A</em>(<em>a<sub>n</sub></em>－<em>p</em>)，即{<em>a<sub>n</sub></em>－<em>p</em>}是公比为<em>A</em>的等比数列．

【基本题型】

<strong>[例1]</strong> （1）已知数列{<em>a<sub>n</sub></em>}满足<em>a</em><sub>1</sub>＝1，<em>a<sub>n</sub></em><sub>＋1</sub>＝3<em>a<sub>n</sub></em>＋2(<em>n</em>∈<strong>N</strong><sup>\*</sup>)，则数列{<em>a<sub>n</sub></em>}的通项公式为\_\_\_\_\_\_\_\_．
答案　<em>a<sub>n</sub></em>＝2·3<em><sup>n</sup></em><sup>－1</sup>－1　解析　∵<em>a<sub>n</sub></em><sub>＋1</sub>＝3<em>a<sub>n</sub></em>＋2，∴<em>a<sub>n</sub></em><sub>＋1</sub>＋1＝3(<em>a<sub>n</sub></em>＋1)，∴＝3，∴数列{<em>a<sub>n</sub></em>＋1}为等比数列，公比<em>q</em>＝3，又<em>a</em><sub>1</sub>＋1＝2，∴<em>a<sub>n</sub></em>＋1＝2·3<em><sup>n</sup></em><sup>－1</sup>，∴<em>a<sub>n</sub></em>＝2·3<em><sup>n</sup></em><sup>－1</sup>－1．

(迭代法)<em>a<sub>n</sub></em><sub>＋1</sub>＝3<em>a<sub>n</sub></em>＋2，即<em>a<sub>n</sub></em><sub>＋1</sub>＋1＝3(<em>a<sub>n</sub></em>＋1)＝3<sup>2</sup>(<em>a<sub>n</sub></em><sub>－1</sub>＋1)＝3<sup>3</sup>(<em>a<sub>n</sub></em><sub>－2</sub>＋1)＝…＝3<em><sup>n</sup></em>(<em>a</em><sub>1</sub>＋1)＝2×3<em><sup>n</sup></em>(<em>n</em>≥1)，所以<em>a<sub>n</sub></em>＝2×3<em><sup>n</sup></em><sup>－1</sup>－1(<em>n</em>≥2)，又<em>a</em><sub>1</sub>＝1也满足上式，故数列{<em>a<sub>n</sub></em>}的一个通项公式为<em>a<sub>n</sub></em>＝2×3<em><sup>n</sup></em><sup>－1</sup>－1．  
（2）已知数列{<em>a<sub>n</sub></em>}中，<em>a</em><sub>1</sub>＝3，且点<em>P<sub>n</sub></em>(<em>a<sub>n</sub></em>，<em>a<sub>n</sub></em><sub>＋1</sub>)(<em>n</em>∈<strong>N</strong><sup>\*</sup>)在直线3<em>x</em>－<em>y</em>＋1＝0上，则数列{<em>a<sub>n</sub></em>}的通项公式为\_\_\_\_\_\_\_\_．
答案　<em>a<sub>n</sub></em>＝·3<em><sup>n</sup></em><sup>－1</sup>－　解析　因为点<em>P<sub>n</sub></em>(<em>a<sub>n</sub></em>，<em>a<sub>n</sub></em><sub>＋1</sub>)(<em>n</em>∈<strong>N</strong><sup>\*</sup>)在直线3<em>x</em>－<em>y</em>＋1＝0上，所以3<em>a<sub>n</sub></em>－<em>a<sub>n</sub></em><sub>＋1</sub>＋1＝0，即<em>a<sub>n</sub></em><sub>＋1</sub>＝3<em>a<sub>n</sub></em>＋1，所以<em>a<sub>n</sub></em><sub>＋1</sub>＋＝3，所以数列是公比为3的等比数列，首项为<em>a</em><sub>1</sub>＋＝3＋＝，所以<em>a<sub>n</sub></em>＋＝·3<em><sup>n</sup></em><sup>－1</sup>，所以<em>a<sub>n</sub></em>＝·3<em><sup>n</sup></em><sup>－1</sup>－．

<strong>[例2]</strong> （1）在数列{<em>a<sub>n</sub></em>}中，<em>a</em><sub>1</sub>＝1，<em>a<sub>n</sub></em><sub>＋1</sub>＝<em>a<sub>n</sub></em>＋1，则数列{<em>a<sub>n</sub></em>}的通项公式为\_\_\_\_\_\_\_\_．
答案　2－<em><sup>n</sup></em><sup>－1</sup>　解析　设<em>f</em>(<em>x</em>)＝<em>x</em>＋1，令<em>f</em>(<em>x</em>)＝<em>x</em>，即<em>x</em>＋1＝<em>x</em>，得<em>x</em>＝2，∴<em>x</em>＝2是函数<em>f</em>(<em>x</em>)＝<em>x</em>＋1的不动点，∴<em>a<sub>n</sub></em><sub>＋1</sub>－2＝(<em>a<sub>n</sub></em>－2)，∴数列{<em>a<sub>n</sub></em>－2}是以－1为首项，以为公比的等比数列，∴<em>a<sub>n</sub></em>－2＝－1×<em><sup>n</sup></em><sup>－1</sup>，∴<em>a<sub>n</sub></em>＝2－<em><sup>n</sup></em><sup>－1</sup>，<em>n</em>∈<strong>N</strong><sup>\*</sup>．  
（2）已知数列{<em>a<sub>n</sub></em>}满足<em>a<sub>n</sub></em><sub>＋1</sub>＝－<em>a<sub>n</sub></em>－2，<em>a</em><sub>1</sub>＝4，则数列{<em>a<sub>n</sub></em>}的通项公式为\_\_\_\_\_\_\_\_．
答案　－＋·<em><sup>n</sup></em><sup>－1</sup>　解析　设<em>f</em>(<em>x</em>)＝－<em>x</em>－2，由<em>f</em>(<em>x</em>)＝<em>x</em>，得<em>x</em>＝－．∴<em>a<sub>n</sub></em><sub>＋1</sub>＋＝－，又<em>a</em><sub>1</sub>＝4，∴是以为首项，以－为公比的等比数列，∴<em>a<sub>n</sub></em>＋＝×<em><sup>n</sup></em><sup>－1</sup>，∴<em>a<sub>n</sub></em>＝－＋·<em><sup>n</sup></em><sup>－1</sup>，<em>n</em>∈<strong>N</strong><sup>\*</sup>．

【对点精练】

1．在数列{<em>a<sub>n</sub></em>}中，若<em>a</em><sub>1</sub>＝1，<em>a<sub>n</sub></em><sub>＋1</sub>＝2<em>a<sub>n</sub></em>＋3，则通项公式<em>a<sub>n</sub></em>＝\_\_\_\_\_\_\_\_．

1．答案　2<em><sup>n</sup></em><sup>＋1</sup>－3　解析　设递推公式<em>a<sub>n</sub></em><sub>＋1</sub>＝2<em>a<sub>n</sub></em>＋3可以转化为<em>a<sub>n</sub></em><sub>＋1</sub>＋<em>t</em>＝2(<em>a<sub>n</sub></em>＋<em>t</em>)，即<em>a<sub>n</sub></em><sub>＋1</sub>＝2<em>a<sub>n</sub></em>＋<em>t</em>，解得

<em>t</em>＝3．故<em>a<sub>n</sub></em><sub>＋1</sub>＋3＝2(<em>a<sub>n</sub></em>＋3)．令<em>b<sub>n</sub></em>＝<em>a<sub>n</sub></em>＋3，则<em>b</em><sub>1</sub>＝<em>a</em><sub>1</sub>＋3＝4，且＝＝2．所以{<em>b<sub>n</sub></em>}是以4为首项，2为公比的等比数列．∴<em>b<sub>n</sub></em>＝4·2<em><sup>n</sup></em><sup>－1</sup>＝2<em><sup>n</sup></em><sup>＋1</sup>，∴<em>a<sub>n</sub></em>＝2<em><sup>n</sup></em><sup>＋1</sup>－3．

2．在数列{<em>a<sub>n</sub></em>}中，已知<em>a</em><sub>1</sub>＝1，<em>a<sub>n</sub></em><sub>＋1</sub>＝2<em>a<sub>n</sub></em>＋1，则其通项公式<em>a<sub>n</sub></em>＝\_\_\_\_\_\_\_\_．

2．答案　2<em><sup>n</sup></em>－1　解析　由题意知<em>a<sub>n</sub></em><sub>＋1</sub>＋1＝2(<em>a<sub>n</sub></em>＋1)，∴数列{<em>a<sub>n</sub></em>＋1}是以2为首项，2为公比的等比数列，
∴<em>a<sub>n</sub></em>＋1＝2<em><sup>n</sup></em>，∴<em>a<sub>n</sub></em>＝2<em><sup>n</sup></em>－1．

3．已知数列{<em>a<sub>n</sub></em>}中，<em>a</em><sub>1</sub>＝3，且点<em>P<sub>n</sub></em>(<em>a<sub>n</sub></em>，<em>a<sub>n</sub></em><sub>＋1</sub>)(<em>n</em>∈N<sup>\*</sup>)在直线4<em>x</em>－<em>y</em>＋1＝0上，则数列{<em>a<sub>n</sub></em>}的通项公式为

\_\_\_\_\_\_\_\_．

3．答案　<em>a<sub>n</sub></em>＝×4<em><sup>n</sup></em><sup>－1</sup>－　解析　因为点<em>P<sub>n</sub></em>(<em>a<sub>n</sub></em>，<em>a<sub>n</sub></em><sub>＋1</sub>)(<em>n</em>∈N<sup>\*</sup>)在直线4<em>x</em>－<em>y</em>＋1＝0上，所以4<em>a<sub>n</sub></em>－<em>a<sub>n</sub></em><sub>＋1</sub>＋1

＝0．所以<em>a<sub>n</sub></em><sub>＋1</sub>＋＝4．因为<em>a</em><sub>1</sub>＝3，所以<em>a</em><sub>1</sub>＋＝．故数列是首项为，公比为4的等比数列．所以<em>a<sub>n</sub></em>＋＝×4<em><sup>n</sup></em><sup>－1</sup>，故数列{<em>a<sub>n</sub></em>}的通项公式为<em>a<sub>n</sub></em>＝×4<em><sup>n</sup></em><sup>－1</sup>－．

<strong>考点二　由</strong><em><strong>a<sub>n</sub></strong></em><strong><sub>＋1</sub>＝</strong><em><strong>pa<sub>n</sub></strong></em><strong>＋</strong><em><strong>f</strong></em><strong>(</strong><em><strong>n</strong></em><strong>)求</strong><em><strong>a<sub>n</sub></strong></em><strong>型</strong>

【基本方法】

已知<em>a<sub>n</sub></em><sub>＋1</sub>＝<em>pa<sub>n</sub></em>＋<em>f</em>(<em>n</em>)求<em>a<sub>n</sub></em>的方法

递推关系形如<em>a<sub>n</sub></em><sub>＋1</sub>＝<em>pa<sub>n</sub></em>＋<em>f</em>(<em>n</em>)(<em>p</em>是非零常数)的数列{<em>a<sub>n</sub></em>}的通项公式，可先在两边同除以<em>f</em>(<em>n</em>)后再用累加法求得．

【基本题型】

<strong>[例3]</strong> （1）在数列{<em>a<sub>n</sub></em>}中，若<em>a</em><sub>1</sub>＝2，<em>a<sub>n</sub></em><sub>＋1</sub>＝2<em>a<sub>n</sub></em>＋2<em><sup>n</sup></em><sup>＋1</sup>，则通项公式<em>a<sub>n</sub></em>＝\_\_\_\_\_\_\_\_．
答案　<em>n</em>·2<em><sup>n</sup></em>　解析　将式子<em>a<sub>n</sub></em><sub>＋1</sub>＝2<em>a<sub>n</sub></em>＋2<em><sup>n</sup></em><sup>＋1</sup>两边同除以2<em><sup>n</sup></em><sup>＋1</sup>得，＝＋1，所以是首项、公差均为1的等差数列，所以＝<em>n</em>，<em>a<sub>n</sub></em>＝<em>n</em>·2<em><sup>n</sup></em>．  
（2）在数列{<em>a<sub>n</sub></em>}中，<em>a</em><sub>1</sub>＝1，<em>a<sub>n</sub></em><sub>＋1</sub>＝<em>a<sub>n</sub></em>＋<em><sup>n</sup></em><sup>＋1</sup>(<em>n</em>∈<strong>N</strong><sup>\*</sup>)，则通项公式<em>a<sub>n</sub></em>＝\_\_\_\_\_\_\_\_．
答案　B　解析　由题意得<em>a<sub>n</sub></em>＝<em>a<sub>n</sub></em><sub>－1</sub>＋<em><sup>n</sup></em>(<em>n</em>≥2)，∴3<em><sup>n</sup>a<sub>n</sub></em>＝3<em><sup>n</sup></em><sup>－1</sup><em>a<sub>n</sub></em><sub>－1</sub>＋1(<em>n</em>≥2)，即3<em><sup>n</sup>a<sub>n</sub></em>－3<em><sup>n</sup></em><sup>－1</sup><em>a<sub>n</sub></em><sub>－1</sub>＝1(<em>n</em>≥2)．又<em>a</em><sub>1</sub>＝1，∴3<sup>1</sup>·<em>a</em><sub>1</sub>＝3，∴数列{3<em><sup>n</sup>a<sub>n</sub></em>}是以3为首项，1为公差的等差数列，∴3<em><sup>n</sup>a<sub>n</sub></em>＝3＋(<em>n</em>－1)×1＝<em>n</em>＋2，∴<em>a<sub>n</sub></em>＝(<em>n</em>∈<strong>N</strong><sup>\*</sup>)．  
（3）已知数列{<em>a<sub>n</sub></em>}的前<em>n</em>项和为<em>S<sub>n</sub></em>，满足2<em>S<sub>n</sub></em>＝<em>a<sub>n</sub></em><sub>＋1</sub>－2<em><sup>n</sup></em><sup>＋1</sup>＋1，<em>n</em>∈<strong>N</strong><sup>\*</sup>，且<em>a</em><sub>1</sub>，<em>a</em><sub>2</sub>＋5，<em>a</em><sub>3</sub>成等差数列，则<em>a<sub>n</sub></em>＝\_\_\_\_\_\_\_\_．
答案　3<em><sup>n</sup></em>－2<em><sup>n</sup></em>　解析　由<em>a</em><sub>1</sub>，<em>a</em><sub>2</sub>＋5，<em>a</em><sub>3</sub>成等差数列可得<em>a</em><sub>1</sub>＋<em>a</em><sub>3</sub>＝2<em>a</em><sub>2</sub>＋10，由2<em>S<sub>n</sub></em>＝<em>a<sub>n</sub></em><sub>＋1</sub>－2<em><sup>n</sup></em><sup>＋1</sup>＋1，得2<em>a</em><sub>1</sub>＋2<em>a</em><sub>2</sub>＝<em>a</em><sub>3</sub>－7，即2<em>a</em><sub>2</sub>＝<em>a</em><sub>3</sub>－7－2<em>a</em><sub>1，</sub> 代入<em>a</em><sub>1</sub>＋<em>a</em><sub>3</sub>＝2<em>a</em><sub>2</sub>＋10，得<em>a</em><sub>1</sub>＝1，代入2<em>S</em><sub>1</sub>＝<em>a</em><sub>2</sub>－2<sup>2</sup>＋1，得<em>a</em><sub>2</sub>＝5．2<em>S<sub>n</sub></em>＝<em>a<sub>n</sub></em><sub>＋1</sub>－2<em><sup>n</sup></em><sup>＋1</sup>＋1，得当<em>n</em>≥2时，2<em>S<sub>n</sub></em><sub>－1</sub>＝<em>a<sub>n</sub></em>－2<em><sup>n</sup></em>＋1，两式相减，得2<em>a<sub>n</sub></em>＝<em>a<sub>n</sub></em><sub>＋1</sub>－<em>a<sub>n</sub></em>－2<em><sup>n</sup></em>，即<em>a<sub>n</sub></em><sub>＋1</sub>＝3<em>a<sub>n</sub></em>＋2<em><sup>n</sup></em>，当<em>n</em>＝1时，5＝3×1＋2<sup>1</sup>也适合<em>a<sub>n</sub></em><sub>＋1</sub>＝3<em>a<sub>n</sub></em>＋2<em><sup>n</sup></em>，所以对任意正整数<em>n</em>，<em>a<sub>n</sub></em><sub>＋1</sub>＝3<em>a<sub>n</sub></em>＋2<em><sup>n</sup></em>．上式两端同时除以2<em><sup>n</sup></em><sup>＋1</sup>，得＝·＋，两端同时加1，得＋1＝·＋＝，所以数列是首项为，公比为的等比数列，所以＋1＝<em><sup>n</sup></em>，所以＝<em><sup>n</sup></em>－1，所以<em>a<sub>n</sub></em>＝3<em><sup>n</sup></em>－2<em><sup>n</sup></em>．

【对点精练】

1．已知数列{<em>a<sub>n</sub></em>}满足<em>a</em><sub>1</sub>＝1，<em>a<sub>n</sub></em><sub>＋1</sub>－2<em>a<sub>n</sub></em>＝2<em><sup>n</sup></em>(<em>n</em>∈<strong>N</strong><sup>\*</sup>)，则数列{<em>a<sub>n</sub></em>}的通项公式为<em>a<sub>n</sub></em>＝\_\_\_\_\_\_\_\_．

1．答案　<em>n</em>·2<em><sup>n</sup></em><sup>－1</sup>　解析　<em>a<sub>n</sub></em><sub>＋1</sub>－2<em>a<sub>n</sub></em>＝2<em><sup>n</sup></em>两边同除以2<em><sup>n</sup></em><sup>＋1</sup>，可得－＝，又＝，∴数列是以为

首项，为公差的等差数列，∴＝＋(<em>n</em>－1)×＝，∴<em>a<sub>n</sub></em>＝<em>n</em>·2<em><sup>n</sup></em><sup>－1</sup>．

2．在数列{<em>a<sub>n</sub></em>}中，已知<em>a</em><sub>1</sub>＝1，<em>a<sub>n</sub></em><sub>＋1</sub>＝<em>a<sub>n</sub></em>－，则其通项公式<em>a<sub>n</sub></em>＝\_\_\_\_\_\_\_\_．

2．答案　　解析　由<em>a<sub>n</sub></em><sub>＋1</sub>＝<em>a<sub>n</sub></em>－得2<em><sup>n</sup>a<sub>n</sub></em><sub>＋1</sub>＝2<em><sup>n</sup></em><sup>－1</sup><em>a<sub>n</sub></em>－1，令<em>b<sub>n</sub></em>＝2<em><sup>n</sup></em><sup>－1</sup><em>a<sub>n</sub></em>，则<em>b<sub>n</sub></em><sub>＋1</sub>－<em>b<sub>n</sub></em>＝－1，又<em>a</em><sub>1</sub>＝1，
∴<em>b</em><sub>1</sub>＝1，∴<em>b<sub>n</sub></em>＝1＋(<em>n</em>－1)×(－1)＝－<em>n</em>＋2．即2<em><sup>n</sup></em><sup>－1</sup><em>a<sub>n</sub></em>＝－<em>n</em>＋2，∴<em>a<sub>n</sub></em>＝．

3．已知各项均不为0的数列{<em>a<sub>n</sub></em>}满足<em>a</em><sub>1</sub>＝，<em>a<sub>n</sub>a<sub>n</sub></em><sub>－1</sub>＝<em>a<sub>n</sub></em><sub>－1</sub>－<em>a<sub>n</sub></em>(<em>n</em>≥2，<em>n</em>∈<strong>N</strong><sup>\*</sup>)，则数列{<em>a<sub>n</sub></em>}的通项公式<em>a<sub>n</sub></em>

＝\_\_\_\_\_\_\_\_．

3．解　∵<em>a<sub>n</sub>a<sub>n</sub></em><sub>－1</sub>＝<em>a<sub>n</sub></em><sub>－1</sub>－<em>a<sub>n</sub></em>，且各项均不为0，∴－＝1．∴{}为首项是2，公差为1的等差数列，
∴＝<em>n</em>＋1，∴当<em>n</em>≥2时，<em>a<sub>n</sub></em>＝．∵<em>a</em><sub>1</sub>＝也符合上式，∴<em>a<sub>n</sub></em>＝(<em>n</em>∈<strong>N</strong><sup>\*</sup>)．

<strong>考点三　由</strong><em><strong>a<sub>n</sub></strong></em><strong><sub>＋2</sub>＝</strong><em><strong>pa<sub>n</sub></strong></em><strong><sub>＋1</sub>＋</strong><em><strong>qa<sub>n</sub></strong></em><strong>求</strong><em><strong>a<sub>n</sub></strong></em><strong>型</strong>

【基本方法】

已知<em>a<sub>n</sub></em><sub>＋2</sub>＝<em>pa<sub>n</sub></em><sub>＋1</sub>＋<em>qa<sub>n</sub></em>求<em>a<sub>n</sub></em>的方法

递推关系形如<em>a<sub>n</sub></em><sub>＋2</sub>＝<em>pa<sub>n</sub></em><sub>＋1</sub>＋<em>qa<sub>n</sub></em>型，可化为<em>a<sub>n</sub></em><sub>＋2</sub>＋<em>xa<sub>n</sub></em><sub>＋1</sub>＝(<em>p</em>＋<em>x</em>)，令<em>x</em>＝，求得<em>x</em>来解决．

【基本题型】

<strong>[例4]</strong> 已知数列{<em>a<sub>n</sub></em>}满足<em>a</em><sub>1</sub>＝1，<em>a</em><sub>2</sub>＝4，<em>a<sub>n</sub></em><sub>＋2</sub>＋2<em>a<sub>n</sub></em>＝3<em>a<sub>n</sub></em><sub>＋1</sub>(<em>n</em>∈N<sub>＋</sub>)，则数列{<em>a<sub>n</sub></em>}的通项公式<em>a<sub>n</sub></em>＝\_\_\_\_\_\_\_\_．
答案　3×2<em><sup>n</sup></em><sup>－1</sup>－2　解析　由<em>a<sub>n</sub></em><sub>＋2</sub>＋2<em>a<sub>n</sub></em>－3<em>a<sub>n</sub></em><sub>＋1</sub>＝0，得<em>a<sub>n</sub></em><sub>＋2</sub>－<em>a<sub>n</sub></em><sub>＋1</sub>＝2(<em>a<sub>n</sub></em><sub>＋1</sub>－<em>a<sub>n</sub></em>)，∴数列{<em>a<sub>n</sub></em><sub>＋1</sub>－<em>a<sub>n</sub></em>}是以<em>a</em><sub>2</sub>－<em>a</em><sub>1</sub>＝3为首项，2为公比的等比数列，∴<em>a<sub>n</sub></em><sub>＋1</sub>－<em>a<sub>n</sub></em>＝3×2<em><sup>n</sup></em><sup>－1</sup>，∴当<em>n</em>≥2时，<em>a<sub>n</sub></em>－<em>a<sub>n</sub></em><sub>－1</sub>＝3×2<em><sup>n</sup></em><sup>－2</sup>，…，<em>a</em><sub>3</sub>－<em>a</em><sub>2</sub>＝3×2，<em>a</em><sub>2</sub>－<em>a</em><sub>1</sub>＝3，将以上各式累加，得<em>a<sub>n</sub></em>－<em>a</em><sub>1</sub>＝3×2<em><sup>n</sup></em><sup>－2</sup>＋…＋3×2＋3＝3(2<em><sup>n</sup></em><sup>－1</sup>－1)，∴<em>a<sub>n</sub></em>＝3×2<em><sup>n</sup></em><sup>－1</sup>－2(当<em>n</em>＝1时，也满足)．

【对点精练】

1．若<em>a</em><sub>1</sub>＝5，<em>a</em><sub>2</sub>＝2，<em>a<sub>n</sub></em><sub>＋2</sub>＝2<em>a<sub>n</sub></em><sub>＋1</sub>＋3<em>a<sub>n</sub></em>，则<em>a<sub>n</sub></em>＝\_\_\_\_\_\_\_\_．

1．答案　　解析　设<em>a<sub>n</sub></em><sub>＋2</sub>＋<em>xa<sub>n</sub></em><sub>＋1</sub>＝(2＋<em>x</em>)<em>a<sub>n</sub></em><sub>＋1</sub>＋3<em>a<sub>n</sub></em>(<em>x</em>≠－2，<em>x</em>是待定系数)，即<em>a<sub>n</sub></em><sub>＋</sub>

<sub>2</sub>＋<em>xa<sub>n</sub></em><sub>＋1</sub>＝(2＋<em>x</em>)，令<em>x</em>＝，解得<em>x</em>＝－3或1．当<em>x</em>＝－3时，得<em>a<sub>n</sub></em><sub>＋2</sub>－3<em>a<sub>n</sub></em><sub>＋1</sub>＝－(<em>a<sub>n</sub></em><sub>＋1</sub>－3<em>a<sub>n</sub></em>)，所以{<em>a<sub>n</sub></em><sub>＋1</sub>－3<em>a<sub>n</sub></em>}是首项为－13、公比为－1的等比数列，得<em>a<sub>n</sub></em><sub>＋1</sub>－3<em>a<sub>n</sub></em>＝－13·(－1)<em><sup>n</sup></em><sup>－1</sup>．当<em>x</em>＝1时，同理可得<em>a<sub>n</sub></em><sub>＋1</sub>＋<em>a<sub>n</sub></em>＝7·3<em><sup>n</sup></em><sup>－1</sup>，解关于<em>a<sub>n</sub></em><sub>＋1</sub>，<em>a<sub>n</sub></em>的方程组可得<em>a<sub>n</sub></em>＝．

<strong>考点四　由</strong><em><strong>a<sub>n</sub></strong></em><strong><sub>＋1</sub>＝求</strong><em><strong>a<sub>n</sub></strong></em><strong>型</strong>

【基本方法】

已知<em>a<sub>n</sub></em><sub>＋1</sub>＝求<em>a<sub>n</sub></em>的方法1

递推关系形如<em>a<sub>n</sub></em><sub>＋1</sub>＝型可取倒数，构造新数列求解．

已知<em>a<sub>n</sub></em><sub>＋1</sub>＝求<em>a<sub>n</sub></em>的方法2

对于一个函数*f*(*x*)，我们把满足*f*(*m*)＝*m*的值*x*＝*m*称为函数*f*(*x*)的“不动点”．利用“不动点法”可以构造新数列，求数列的通项公式．
设<em>f</em>(<em>x</em>)＝(<em>c</em>≠0，<em>AD</em>－<em>BC</em>≠0)，数列{<em>a<sub>n</sub></em>}满足<em>a<sub>n</sub></em><sub>＋1</sub>＝<em>f</em>(<em>a<sub>n</sub></em>)，<em>a</em><sub>1</sub>≠<em>f</em>(<em>a</em><sub>1</sub>)．若<em>f</em>(<em>x</em>)有两个相异的不动点<em>p</em>，<em>q</em>，则＝<em>k</em>·．

【基本题型】

<strong>[例5]</strong> （1）已知数列{<em>a<sub>n</sub></em>}中，<em>a</em><sub>1</sub>＝2，<em>a<sub>n</sub></em><sub>＋1</sub>＝(<em>n</em>∈<strong>N</strong><sup>\*</sup>)，则数列{<em>a<sub>n</sub></em>}的通项公式<em>a<sub>n</sub></em>＝\_\_\_\_\_\_\_\_．
答案　　解析　∵<em>a<sub>n</sub></em><sub>＋1</sub>＝，<em>a</em><sub>1</sub>＝2，∴<em>a<sub>n</sub></em>≠0，∴＝＋，即－＝，又<em>a</em><sub>1</sub>＝2，则＝，∴是以为首项，为公差的等差数列．∴＝＋(<em>n</em>－1)×＝，∴<em>a<sub>n</sub></em>＝．  
（2）已知数列{<em>a<sub>n</sub></em>}中，<em>a</em><sub>1</sub>＝1，<em>a<sub>n</sub></em><sub>＋1</sub>＝(<em>n</em>∈<strong>N</strong><sup>\*</sup>)，则数列{<em>a<sub>n</sub></em>}的通项公式为\_\_\_\_\_\_\_\_．
答案　　解析　因为<em>a<sub>n</sub></em><sub>＋1</sub>＝(<em>n</em>∈<strong>N</strong><sup>\*</sup>)，所以＝＋1，设＋<em>t</em>＝3，所以3<em>t</em>－<em>t</em>＝1，解得<em>t</em>＝，所以＋＝3，又＋＝1＋＝，所以数列是以为首项，3为公比的等比数列，所以＋＝×3<em><sup>n</sup></em><sup>－1</sup>＝，所以＝，所以<em>a<sub>n</sub></em>＝．

<strong>[例6]</strong> （1）已知数列{<em>a<sub>n</sub></em>}满足<em>a</em><sub>1</sub>＝3，<em>a<sub>n</sub></em><sub>＋1</sub>＝，则数列{<em>a<sub>n</sub></em>}的通项公式为\_\_\_\_\_\_\_\_．
答案　　解析　由方程<em>x</em>＝，得数列{<em>a<sub>n</sub></em>}的不动点为1和2，＝＝＝·，所以是首项为＝2，公比为的等比数列，所以＝2·<em><sup>n</sup></em><sup>－1</sup>，解得<em>a<sub>n</sub></em>＝＋2＝，<em>n</em>∈<strong>N</strong><sup>\*</sup>．  
（2）已知数列{<em>a<sub>n</sub></em>}满足<em>a</em><sub>1</sub>＝2，<em>a<sub>n</sub></em>＝(<em>n</em>≥2)，则数列{<em>a<sub>n</sub></em>}的通项公式为\_\_\_\_\_\_\_\_．
答案　　解析　解方程<em>x</em>＝，化简得2<em>x</em><sup>2</sup>－2＝0，解得<em>x</em><sub>1</sub>＝1，<em>x</em><sub>2</sub>＝－1，令＝<em>c</em>·，由<em>a</em><sub>1</sub>＝2，得<em>a</em><sub>2</sub>＝，可得<em>c</em>＝－，∴数列是以＝为首项，以－为公比的等比数列，∴＝·<em><sup>n</sup></em><sup>－1</sup>，∴<em>a<sub>n</sub></em>＝．  
（3）设数列{<em>a<sub>n</sub></em>}满足8<em>a<sub>n</sub></em><sub>＋1</sub><em>a<sub>n</sub></em>－16<em>a<sub>n</sub></em><sub>＋1</sub>＋2<em>a<sub>n</sub></em>＋5＝0(<em>n</em>≥1，<em>n</em>∈<strong>N</strong><sup>\*</sup>)，且<em>a</em><sub>1</sub>＝1，记<em>b<sub>n</sub></em>＝(<em>n</em>≥1)．则数列{<em>b<sub>n</sub></em>}的通项公式为\_\_\_\_\_\_\_\_．
答案　　解析　由已知得<em>a<sub>n</sub></em><sub>＋1</sub>＝，由方程<em>x</em>＝，得不动点<em>x</em><sub>1</sub>＝，<em>x</em><sub>2</sub>＝．所以＝＝·，所以数列是首项为－2，公比为的等比数列，所以＝－2×<em><sup>n</sup></em><sup>－1</sup>＝－，解得<em>a<sub>n</sub></em>＝．故<em>b<sub>n</sub></em>＝＝，<em>n</em>∈<strong>N</strong><sup>\*</sup>．

【对点精练】

1．已知数列{<em>a<sub>n</sub></em>}中，<em>a</em><sub>1</sub>＝1，<em>a<sub>n</sub></em><sub>＋1</sub>＝(<em>n</em>∈<strong>N</strong><sub>＋</sub>)，则数列{<em>a<sub>n</sub></em>}的通项公式为\_\_\_\_\_\_\_\_．

1．答案　　解析　因为<em>a<sub>n</sub></em><sub>＋1</sub>＝，<em>a</em><sub>1</sub>＝1，所以<em>a<sub>n</sub></em>≠0，所以＝＋，即－＝．又因为

<em>a</em><sub>1</sub>＝1，则＝1，所以是以1为首项，为公差的等差数列．所以＝＋(<em>n</em>－1)×＝＋．所以<em>a<sub>n</sub></em>＝．

2．若<em>a</em><sub>1</sub>＝1，<em>a<sub>n</sub></em><sub>＋1</sub>＝，则数列{<em>a<sub>n</sub></em>}的通项公式<em>a<sub>n</sub></em>＝\_\_\_\_\_\_\_\_．

2．答案　　解析　对<em>a<sub>n</sub></em><sub>＋1</sub>＝两边取倒数，得＝＋3，所以数列是首项为＝1，公差

为3的等差数列，所以＝3<em>n</em>－2，<em>a<sub>n</sub></em>＝．

3．若<em>a</em><sub>1</sub>＝5，<em>a<sub>n</sub></em><sub>＋1</sub>＝，则<em>a<sub>n</sub></em>＝\_\_\_\_\_\_\_\_．

3．答案　　解析　令<em>a<sub>n</sub></em>＝<em>b<sub>n</sub></em>＋<em>p</em>，得<em>b<sub>n</sub></em><sub>＋1</sub>＋<em>p</em>＝<em>b<sub>n</sub></em><sub>＋1</sub>＝－<em>p</em>＝
令4<em>p</em>－4－<em>p</em><sup>2</sup>＝0，得<em>p</em>＝2，所以<em>b</em><sub>1</sub>＝3，<em>b<sub>n</sub></em><sub>＋1</sub>＝，两边取倒数，＝1＋，为首项为＝，公差为1的等差数列，可求得<em>b<sub>n</sub></em>＝，所以<em>a<sub>n</sub></em>＝．

<strong>考点五　由其他形式的递推公式求</strong><em><strong>a<sub>n</sub></strong></em><strong>型</strong>

【基本方法】

已知其他形式的递推公式求<em>a<sub>n</sub></em>的方法

对递推公式进行合理的变形，然后转化为等差数列或等比数列

【基本题型】

<strong>[例7]</strong> （1）数列{<em>a<sub>n</sub></em>}满足<em>a</em><sub>1</sub>＝2，<em>a<sub>n</sub></em><sub>＋1</sub>＝<em>a</em>(<em>a<sub>n</sub></em>＞0，<em>n</em>∈<strong>N</strong><sup>\*</sup>)，则<em>a<sub>n</sub></em>＝(　　)

A．10<em><sup>n</sup></em><sup>－2</sup>　　　　　　　
B．10<em><sup>n</sup></em><sup>－1</sup>　　　　　　　　
C．102<em><sup>n</sup></em><sup>－1</sup> 　　　　　　　　
D．22<em><sup>n</sup></em><sup>－1</sup>
答案　D　解析　因为数列{<em>a<sub>n</sub></em>}满足<em>a</em><sub>1</sub>＝2，<em>a<sub>n</sub></em><sub>＋1</sub>＝<em>a</em>(<em>a<sub>n</sub></em>＞0，<em>n</em>∈<strong>N</strong><sup>\*</sup>)，所以log<sub>2</sub><em>a<sub>n</sub></em><sub>＋1</sub>＝2log<sub>2</sub><em>a<sub>n</sub></em>，即＝2．又<em>a</em><sub>1</sub>＝2，所以log<sub>2</sub><em>a</em><sub>1</sub>＝log<sub>2</sub>2＝1．故数列{log<sub>2</sub><em>a<sub>n</sub></em>}是首项为1，公比为2的等比数列．所以log<sub>2</sub><em>a<sub>n</sub></em>＝2<em><sup>n</sup></em><sup>－1</sup>，即<em>a<sub>n</sub></em>＝22<em><sup>n</sup></em><sup>－1</sup>．故选D．  
（2）已知各项都为正数的数列{<em>a<sub>n</sub></em>}满足：<em>a</em><sub>1</sub>＝1，<em>a</em>－(2<em>a<sub>n</sub></em><sub>＋1</sub>－1)<em>a<sub>n</sub></em>－2<em>a<sub>n</sub></em><sub>＋1</sub>＝0，则数列<em>a<sub>n</sub></em>的通项公式为\_\_\_\_\_\_\_\_．
答案　<em>a<sub>n</sub></em>＝　解析　∵<em>a</em>－(2<em>a<sub>n</sub></em><sub>＋1</sub>－1)<em>a<sub>n</sub></em>－2<em>a<sub>n</sub></em><sub>＋1</sub>＝0，∴(<em>a<sub>n</sub></em>－2<em>a<sub>n</sub></em><sub>＋1</sub>)(<em>a<sub>n</sub></em>＋1)＝0．又∵数列{<em>a<sub>n</sub></em>}的各项都是正数，∴<em>a<sub>n</sub></em>－2<em>a<sub>n</sub></em><sub>＋1</sub>＝0，即＝．∴{<em>a<sub>n</sub></em>}是首项为1，公比为的等比数列，∴<em>a<sub>n</sub></em>＝．  
（3）已知数列{<em>a<sub>n</sub></em>}的首项<em>a</em><sub>1</sub>＝1，前<em>n</em>项和为<em>S<sub>n</sub></em>，且<em>S<sub>n</sub></em><sub>＋1</sub>＝4<em>a<sub>n</sub></em>＋2(<em>n</em>∈<strong>N</strong><sup>\*</sup>)，则<em>a<sub>n</sub></em>＝\_\_\_\_\_\_\_\_．
答案　(3<em>n</em>－1)2<em><sup>n</sup></em><sup>－2</sup>　解析　当<em>n</em>≥2时，<em>S<sub>n</sub></em><sub>＋1</sub>＝4<em>a<sub>n</sub></em>＋2，<em>S<sub>n</sub></em>＝4<em>a<sub>n</sub></em><sub>－1</sub>＋2．两式相减，得<em>a<sub>n</sub></em><sub>＋1</sub>＝4<em>a<sub>n</sub></em>－4<em>a<sub>n</sub></em><sub>－1</sub>，将之变形为<em>a<sub>n</sub></em><sub>＋1</sub>－2<em>a<sub>n</sub></em>＝2(<em>a<sub>n</sub></em>－2<em>a<sub>n</sub></em><sub>－1</sub>)．所以{<em>a<sub>n</sub></em><sub>＋1</sub>－2<em>a<sub>n</sub></em>}是公比为2的等比数列．又<em>a</em><sub>1</sub>＋<em>a</em><sub>2</sub>＝<em>S</em><sub>2</sub>＝4<em>a</em><sub>1</sub>＋2，<em>a</em><sub>1</sub>＝1，得<em>a</em><sub>2</sub>＝5，则<em>a</em><sub>2</sub>－2<em>a</em><sub>1</sub>＝3．所以<em>a<sub>n</sub></em><sub>＋1</sub>－2<em>a<sub>n</sub></em>＝3·2<em><sup>n</sup></em><sup>－1</sup>．两边同除以2<em><sup>n</sup></em><sup>＋1</sup>，得－＝，所以是首项为＝，公差为的等差数列．所以＝＋(<em>n</em>－1)＝<em>n</em>－，所以<em>a<sub>n</sub></em>＝(3<em>n</em>－1)2<em><sup>n</sup></em><sup>－2</sup>．

<strong>[例8]</strong>　(2016·全国Ⅲ)已知各项都为正数的数列{<em>a<sub>n</sub></em>}满足<em>a</em><sub>1</sub>＝1，<em>a</em>－(2<em>a<sub>n</sub></em><sub>＋1</sub>－1)<em>a<sub>n</sub></em>－2<em>a<sub>n</sub></em><sub>＋1</sub>＝0．  
（1）求<em>a</em><sub>2</sub>，<em>a</em><sub>3</sub>；  
（2）求{<em>a<sub>n</sub></em>}的通项公式．
解析　（1）由题意得<em>a</em><sub>2</sub>＝，<em>a</em><sub>3</sub>＝．  
（2）由<em>a</em>－(2<em>a<sub>n</sub></em><sub>＋1</sub>－1)<em>a<sub>n</sub></em>－2<em>a<sub>n</sub></em><sub>＋1</sub>＝0得，2<em>a<sub>n</sub></em><sub>＋1</sub>(<em>a<sub>n</sub></em>＋1)＝<em>a<sub>n</sub></em>(<em>a<sub>n</sub></em>＋1)．
因为{<em>a<sub>n</sub></em>}的各项都为正数，所以＝．
故{<em>a<sub>n</sub></em>}是首项为1，公比为的等比数列，因此<em>a<sub>n</sub></em>＝．

【对点精练】

1．已知数列{<em>a<sub>n</sub></em>}满足<em>a</em><sub>1</sub>＝1，(<em>a<sub>n</sub></em>＋<em>a<sub>n</sub></em><sub>＋1</sub>－1)<sup>2</sup>＝4<em>a<sub>n</sub>a<sub>n</sub></em><sub>＋1</sub>，且<em>a<sub>n</sub></em><sub>＋1</sub>＞<em>a<sub>n</sub></em>(<em>n</em>∈<strong>N</strong><sup>\*</sup>)，则数列{<em>a<sub>n</sub></em>}的通项公式<em>a<sub>n</sub></em>＝(　　)

A．2<em>n</em>　　　　　　　　
B．<em>n</em><sup>2</sup>　　　　　　　　
C．<em>n</em>＋2　　　　　　　　
D．3<em>n</em>－2

1．答案　B　解析　因为<em>a</em><sub>1</sub>＝1，<em>a<sub>n</sub></em><sub>＋1</sub>＞<em>a<sub>n</sub></em>，所以＞．由(<em>a<sub>n</sub></em>＋<em>a<sub>n</sub></em><sub>＋1</sub>－1)<sup>2</sup>＝4<em>a<sub>n</sub>a<sub>n</sub></em><sub>＋1</sub>得<em>a<sub>n</sub></em><sub>＋1</sub>＋<em>a<sub>n</sub></em>－1

＝2，所以(－)<sup>2</sup>＝1，所以－＝1，所以数列{}是首项为1，公差为1的等差数列，所以＝<em>n</em>，即<em>a<sub>n</sub></em>＝<em>n</em><sup>2</sup>，故选B．

2．已知数列{<em>a<sub>n</sub></em>}满足<em>a<sub>n</sub></em>≠0，2<em>a<sub>n</sub></em>(1－<em>a<sub>n</sub></em><sub>＋1</sub>)－2<em>a<sub>n</sub></em><sub>＋1</sub>(1－<em>a<sub>n</sub></em>)＝<em>a<sub>n</sub></em>－<em>a<sub>n</sub></em><sub>＋1</sub>＋<em>a<sub>n</sub></em>·<em>a<sub>n</sub></em><sub>＋1</sub>，且<em>a</em><sub>1</sub>＝，则数列{<em>a<sub>n</sub></em>}的通项

公式<em>a<sub>n</sub></em>＝\_\_\_\_\_\_\_\_．

2．答案　　解析　∵<em>a<sub>n</sub></em>≠0，2<em>a<sub>n</sub></em>(1－<em>a<sub>n</sub></em><sub>＋1</sub>)－2<em>a<sub>n</sub></em><sub>＋1</sub>(1－<em>a<sub>n</sub></em>)＝<em>a<sub>n</sub></em>－<em>a<sub>n</sub></em><sub>＋1</sub>＋<em>a<sub>n</sub></em>·<em>a<sub>n</sub></em><sub>＋1</sub>，∴两边同除以<em>a<sub>n</sub></em>·<em>a<sub>n</sub></em><sub>＋1</sub>，
得－＝－＋1，整理，得－＝1，即是以3为首项，1为公差的等差数列，∴＝3＋(<em>n</em>－1)×1＝<em>n</em>＋2，即<em>a<sub>n</sub></em>＝．

3．各项均不为0的数列{<em>a<sub>n</sub></em>}满足＝<em>a<sub>n</sub></em><sub>＋2</sub><em>a<sub>n</sub></em>(<em>n</em>∈<strong>N</strong><sup>\*</sup>)，且<em>a</em><sub>3</sub>＝2<em>a</em><sub>8</sub>＝，则数列{<em>a<sub>n</sub></em>}的通项公式为

\_\_\_\_\_\_\_\_．

3．答案　<em>a<sub>n</sub></em>＝　解析　因为＝<em>a<sub>n</sub></em><sub>＋2</sub><em>a<sub>n</sub></em>，所以<em>a<sub>n</sub></em><sub>＋1</sub><em>a<sub>n</sub></em>＋<em>a<sub>n</sub></em><sub>＋1</sub><em>a<sub>n</sub></em><sub>＋2</sub>＝2<em>a<sub>n</sub></em><sub>＋2</sub><em>a<sub>n</sub></em>．因为<em>a<sub>n</sub>a<sub>n</sub></em><sub>＋1</sub><em>a<sub>n</sub></em><sub>＋2</sub>

≠0，所以＋＝，所以数列为等差数列．设数列的公差为<em>d</em>，则＝＋(8－3)<em>d</em>． 因为<em>a</em><sub>3</sub>＝2<em>a</em><sub>8</sub>＝，所以<em>d</em>＝1，又＝－2<em>d</em>＝3，所以数列 是以3为首项，1为公差的等差数列．∴＝3＋(<em>n</em>－1)×1＝<em>n</em>＋2，∴<em>a<sub>n</sub></em>＝．

4．(2013·安徽)如图，互不相同的点<em>A</em><sub>1</sub>，<em>A</em><sub>2</sub>，…，<em>A<sub>n</sub></em>，…和<em>B</em><sub>1</sub>，<em>B</em><sub>2</sub>，…，<em>B<sub>n</sub></em>…分别在角<em>O</em>的两条边上，所

有<em>A<sub>n</sub>B<sub>n</sub></em>相互平行，且所有梯形<em>A<sub>n</sub>B<sub>n</sub>B<sub>n</sub></em><sub>＋1</sub><em>A<sub>n</sub></em><sub>＋1</sub>的面积均相等．设<em>OA<sub>n</sub></em>＝<em>a<sub>n</sub></em>，若<em>a</em><sub>1</sub>＝1，<em>a</em><sub>2</sub>＝2，则数列{<em>a<sub>n</sub></em>}

的通项公式是\_\_\_\_\_\_\_\_．

![](images/df4e9d887a65a12977aa14d45029aa3260a6b60fb266f3cdaf1eaec189a05e1b.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

4．答案　<em>a<sub>n</sub></em>＝　解析　由已知<em>S</em>梯形

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)
即，由相似三角形面积比是相似比的平方知<em>OA</em>＋<em>OA</em>＝2<em>OA</em>，即<em>a</em>＋<em>a</em>＝2<em>a</em>，因此{<em>a</em>}为等差数列且<em>a</em>＝<em>a</em>＋3(<em>n</em>－1)＝3<em>n</em>－2，故<em>a<sub>n</sub></em>＝．

