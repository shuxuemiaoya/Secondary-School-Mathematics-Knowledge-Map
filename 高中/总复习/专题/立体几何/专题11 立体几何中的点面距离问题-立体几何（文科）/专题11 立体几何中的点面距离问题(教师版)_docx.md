**专题11　立体几何中的点面距离问题**

【**方法总结**】

应用等体积转化法求解点到平面的距离

等体积转化法就是通过变换几何体的底面，利用几何体(主要是三棱锥)体积的不同表达形式构造方程来求解相关问题的方法，主要用于立体几何中求解点到面的距离．关键是准确把握三棱锥底面的特征，选择的底面应具备两个特征：一是底面的形状规则，即面积可求；二是底面上的高比较明显，即线面垂直关系比较直接．

**【例题选讲】**

<strong>[例1]</strong>(2019·全国Ⅰ)如图，直四棱柱<em>ABCD</em>－<em>A</em><sub>1</sub><em>B</em><sub>1</sub><em>C</em><sub>1</sub><em>D</em><sub>1</sub>的底面是菱形，<em>AA</em><sub>1</sub>＝4，<em>AB</em>＝2，∠<em>BAD</em>＝60°，<em>E</em>，<em>M</em>，<em>N</em>分别是<em>BC</em>，<em>BB</em><sub>1</sub>，<em>A</em><sub>1</sub><em>D</em>的中点．

(1)证明：<em>MN</em>∥平面<em>C</em><sub>1</sub><em>DE</em>；

(2)求点<em>C</em>到平面<em>C</em><sub>1</sub><em>DE</em>的距离．

![](images/32a0b2f86b0703744a8bca7bd97ae7e48ed46b23acfe2f296f375f66d2ed5721.jpg)

解析　(1)连接<em>B</em><sub>1</sub><em>C</em>，<em>ME</em>．因为<em>M</em>，<em>E</em>分别为<em>BB</em><sub>1</sub>，<em>BC</em>的中点，所以<em>ME</em>∥<em>B</em><sub>1</sub><em>C</em>，且<em>ME</em>＝<em>B</em><sub>1</sub><em>C</em>．

![](images/994aa01c81db215fbc1a249d7af0012ddae2b6499f0d859f33f1b403720be2c5.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

又因为<em>N</em>为<em>A</em><sub>1</sub><em>D</em>的中点，所以<em>ND</em>＝<em>A</em><sub>1</sub><em>D</em>．由题设知<em>A</em><sub>1</sub><em>B</em><sub>1</sub>綊<em>DC</em>，可得<em>B</em><sub>1</sub><em>CA</em><sub>1</sub><em>D</em>，故<em>MEND</em>，

因此四边形*MNDE*为平行四边形，所以*MN*∥*ED*．

又<em>MN</em>⊄平面<em>C</em><sub>1</sub><em>DE</em>，<em>ED</em>⊂平面<em>C</em><sub>1</sub><em>DE</em>，所以<em>MN</em>∥平面<em>C</em><sub>1</sub><em>DE</em>．

(2)过点<em>C</em>作<em>C</em><sub>1</sub><em>E</em>的垂线，垂足为<em>H</em>．由已知可得<em>DE</em>⊥<em>BC</em>，<em>DE</em>⊥<em>C</em><sub>1</sub><em>C</em>，

又<em>BC</em>∩<em>C</em><sub>1</sub><em>C</em>＝<em>C</em>，<em>BC</em>，<em>C</em><sub>1</sub><em>C</em>⊂平面<em>C</em><sub>1</sub><em>CE</em>，所以<em>DE</em>⊥平面<em>C</em><sub>1</sub><em>CE</em>，

故<em>DE</em>⊥<em>CH</em>．又<em>C</em><sub>1</sub><em>E</em>∩<em>DE</em>＝<em>E</em>，所以<em>CH</em>⊥平面<em>C</em><sub>1</sub><em>DE</em>，故<em>CH</em>的长即为点<em>C</em>到平面<em>C</em><sub>1</sub><em>DE</em>的距离．

由已知可得<em>CE</em>＝1，<em>C</em><sub>1</sub><em>C</em>＝4，所以<em>C</em><sub>1</sub><em>E</em>＝，故<em>CH</em>＝．从而点<em>C</em>到平面<em>C</em><sub>1</sub><em>DE</em>的距离为．

<strong>[例2]</strong>如图，在四棱锥<em>P</em>－<em>ABCD</em>中，底面是边长为2的正方形，<em>PA</em>＝<em>PD</em>＝，<em>E</em>为<em>PA</em>的中点，点<em>F</em>在<em>PD</em>上且<em>EF</em>⊥平面<em>PCD</em>，<em>M</em>在<em>DC</em>延长线上，<em>FH</em>∥<em>DM</em>，交<em>PM</em>于点<em>H</em>，且<em>FH</em>＝1．

(1)证明：*EF*∥平面*PBM*；

(2)求点*M*到平面*ABP*的距离．

![](images/7f5e1da38856740a025c18ab6ccee861b0ff3d55ddd63132042bdbe2885062f2.jpg)

解析　(1)证明：取*PB*的中点*G*，连接*EG*，*HG*，

![](images/15faa1cf3371faf02930725c6a9e1e1ea6ec677163fd90d9ddedd38e2311b03a.jpg)

则*EG*∥*AB*，且*EG*＝1，∵*FH*∥*DM*，且*FH*＝1，又*AB*∥*DM*，∴*EG*∥*FH*，*EG*＝*FH*，

即四边形*EFHG*为平行四边形，∴*EF*∥*GH*．

又*EF*⊄平面*PBM*，*GH*⊂平面*PBM*，∴*EF*∥平面*PBM*．

(2)∵*EF*⊥平面*PCD*，*CD*⊂平面*PCD*，∴*EF*⊥*CD*．

∵*AD*⊥*CD*，*EF*和*AD*显然相交，*EF*，*AD*⊂平面*PAD*，∴*CD*⊥平面*PAD*，*CD*⊂平面*ABCD*，

∴平面*ABCD*⊥平面*PAD*．取*AD*的中点*O*，连接*PO*，

![](images/5a8144080c55e2a4ea8b8fcc02954f8d2f7a882d5d681e599c9ae2cfa413929a.jpg)

∵*PA*＝*PD*，∴*PO*⊥*AD*．又平面*ABCD*∩平面*PAD*＝*AD*，*PO*⊂平面*PAD*，∴*PO*⊥平面*ABCD*，

∵*AB*∥*CD*，∴*AB*⊥平面*PAD*，∵*PA*⊂平面*PAD*，∴*PA*⊥*AB*，

在等腰三角形*PAD*中，*PO*＝＝＝4．

设点<em>M</em>到平面<em>ABP</em>的距离为<em>h</em>，连接<em>AM</em>，利用等体积可得<em>V<sub>M</sub></em><sub>－</sub><em><sub>ABP</sub></em>＝<em>V<sub>P</sub></em><sub>－</sub><em><sub>ABM</sub></em>，

即××2××*h*＝××2×2×4，∴*h*＝＝，∴点*M*到平面*PAB*的距离为．

<strong>[例3]</strong>如图，已知四棱锥<em>P</em>－<em>ABCD</em>的底面<em>ABCD</em>为菱形，且∠<em>ABC</em>＝60°，<em>AB</em>＝<em>PC</em>＝2，<em>PA</em>＝<em>PB</em>＝．

(1)求证：平面*PAB*⊥平面*ABCD*；

(2)求点*D*到平面*APC*的距离．

![](images/ac8f4a9c8ea23a2a6af84527c4893f846765aa73c102f74fc41e9ebdd18dc6d3.jpg)

解析　(1)证明：取*AB*的中点*O*，连接*PO*，*CO*，(图略)，

由*PA*＝*PB*＝，*AB*＝2知△*PAB*为等腰直角三角形，∴*PO*⊥*AB*，*PO*＝1，

由*AB*＝*BC*＝2，∠*ABC*＝60°知△*ABC*为等边三角形，∴*CO*＝．

又由<em>PC</em>＝2得<em>PO</em><sup>2</sup>＋<em>CO</em><sup>2</sup>＝<em>PC</em><sup>2</sup>，∴<em>PO</em>⊥<em>CO</em>，又<em>AB</em>∩<em>CO</em>＝<em>O</em>，∴<em>PO</em>⊥平面<em>ABC</em>，

又*PO*⊂平面*PAB*，∴平面*PAB*⊥平面*ABCD*．

(2)由题知△*ADC*是边长为2的等边三角形，△*PAC*为等腰三角形，设点*D*到平面*APC*的距离为*h*，

由<em>V<sub>D</sub></em><sub>­</sub><em><sub>PAC</sub></em>＝<em>V<sub>P</sub></em><sub>­</sub><em><sub>ADC</sub></em>得<em>S</em><sub>△</sub><em><sub>PAC</sub></em>·<em>h</em>＝<em>S</em><sub>△</sub><em><sub>ADC</sub></em>·<em>PO</em>．∵<em>S</em><sub>△</sub><em><sub>ADC</sub></em>＝×2<sup>2</sup>＝，<em>S</em><sub>△</sub><em><sub>PAC</sub></em>＝<em>PA</em>·＝，

∴*h*＝＝＝，即点*D*到平面*APC*的距离为．

<strong>[例4]</strong>如图，在单位正方体<em>ABCD</em>­<em>A</em><sub>1</sub><em>B</em><sub>1</sub><em>C</em><sub>1</sub><em>D</em><sub>1</sub>中，<em>E</em>，<em>F</em>分别是<em>AD</em>，<em>BC</em><sub>1</sub>的中点．

![](images/1cb8e3921b916d6f2c8a50d4efc5ef5c620224c6e79c2c66079fcebeed25f7f3.jpg)

(1)求证：<em>EF</em>∥平面<em>C</em><sub>1</sub><em>CDD</em><sub>1</sub>；

(2)在线段<em>A</em><sub>1</sub><em>B</em>上是否存在点<em>G</em>，使<em>EG</em>⊥平面<em>A</em><sub>1</sub><em>BC</em><sub>1</sub>？若存在，求点<em>G</em>到平面<em>C</em><sub>1</sub><em>DF</em>的距离；若不存在，请说明理由．

解析　(1)证明：取*BC*的中点*M*，连接*EM*，*FM*，

∵<em>E</em>，<em>F</em>分别是<em>AD</em>，<em>BC</em><sub>1</sub>的中点，∴<em>EM</em>∥<em>DC</em>，<em>FM</em>∥<em>C</em><sub>1</sub><em>C</em>，

*EM*⊂平面*EFM*，*FM*⊂平面*EFM*，*EM*∩*FM*＝*M*，

<em>DC</em>⊂平面<em>C</em><sub>1</sub><em>CDD</em><sub>1</sub>，<em>C</em><sub>1</sub><em>C</em>⊂平面<em>C</em><sub>1</sub><em>CDD</em><sub>1</sub>，<em>DC</em>∩<em>C</em><sub>1</sub><em>C</em>＝<em>C</em>，

∴平面<em>EFM</em>∥平面<em>C</em><sub>1</sub><em>CDD</em><sub>1</sub>，而<em>EF</em>⊂平面<em>EFM</em>，∴<em>EF</em>∥平面<em>C</em><sub>1</sub><em>CDD</em><sub>1</sub>．

![](images/4a4ea7c9de2f8bede1f85c28e81a3768c7a0e575197c010e85f1fbd903f9e6af.jpg)

(2)取<em>A</em><sub>1</sub><em>B</em>的中点<em>G</em>，连接<em>EG</em>，<em>EA</em><sub>1</sub>，<em>EB</em>，易知<em>EA</em><sub>1</sub>＝<em>EB</em>，而<em>G</em>为中点，∴<em>EG</em>⊥<em>A</em><sub>1</sub><em>B</em>．

连接<em>FG</em>，则<em>FG</em>∥<em>A</em><sub>1</sub><em>C</em><sub>1</sub>，∵正方体棱长为1，在△<em>A</em><sub>1</sub><em>BC</em><sub>1</sub>中，<em>FG</em>＝<em>A</em><sub>1</sub><em>C</em><sub>1</sub>＝．

在Rt△*FME*中，*EF*＝，在Rt△*EAG*中，*EG*＝，

∴<em>FG</em><sup>2</sup>＋<em>EG</em><sup>2</sup>＝<em>FE</em><sup>2</sup>，即<em>EG</em>⊥<em>FG</em>，故<em>EG</em>⊥<em>A</em><sub>1</sub><em>C</em><sub>1</sub>，又<em>A</em><sub>1</sub><em>B</em>，<em>A</em><sub>1</sub><em>C</em><sub>1</sub>⊂平面<em>A</em><sub>1</sub><em>BC</em><sub>1</sub>，<em>A</em><sub>1</sub><em>B</em>∩<em>A</em><sub>1</sub><em>C</em><sub>1</sub>＝<em>A</em><sub>1</sub>，

∴<em>EG</em>⊥平面<em>A</em><sub>1</sub><em>BC</em><sub>1</sub>．点<em>G</em>到平面<em>C</em><sub>1</sub><em>DF</em>的距离就是点<em>G</em>到平面<em>C</em><sub>1</sub><em>DB</em>的距离．

∵<em>GA</em>∥<em>C</em><sub>1</sub><em>D</em>，∴<em>GA</em>∥平面<em>C</em><sub>1</sub><em>DB</em>，∴点<em>G</em>到平面<em>C</em><sub>1</sub><em>DB</em>的距离就是点<em>A</em>到平面<em>C</em><sub>1</sub><em>DB</em>的距离．

易知<em>S</em>△<em>BDC</em><sub>1</sub>＝，<em>S</em><sub>△</sub><em><sub>ABD</sub></em>＝，点<em>C</em><sub>1</sub>到平面<em>ABD</em>的距离为1，

设点<em>G</em>到平面<em>C</em><sub>1</sub><em>DF</em>的距离为<em>d</em>，由<em>V<sub>C</sub></em><sub>1­</sub><em><sub>ABD</sub></em>＝<em>V<sub>A</sub></em><sub>­</sub><em><sub>BDC</sub></em><sub>1</sub>得×1×<em>S</em><sub>△</sub><em><sub>ABD</sub></em>＝·<em>d</em>·<em>S</em><sub>△</sub><em><sub>BDC</sub></em><sub>1</sub>，

即＝<em>d</em>·，∴<em>d</em>＝，即点<em>G</em>到平面<em>C</em><sub>1</sub><em>DF</em>的距离为．

<strong>[例5]</strong>如图1，四边形<em>ABCD</em>为等腰梯形，<em>AB</em>＝2，<em>AD</em>＝<em>DC</em>＝<em>CB</em>＝1，将△<em>ADC</em>沿<em>AC</em>折起，使得平面<em>ADC</em>⊥平面<em>ABC</em>，<em>E</em>为<em>AB</em>的中点，连接<em>DE</em>，<em>DB</em>(如图2)．

(1)求证：*BC*⊥*AD*；

(2)求点*E*到平面*BCD*的距离．

![](images/b184d0ab1d97330cd42cfeb08e57d2dbb9bd8908aec21318190207ca244734b5.jpg)

解析　(1)作*CH*⊥*AB*于点*H*，则*BH*＝，*AH*＝，又*BC*＝1，∴*CH*＝，∴*CA*＝，

∴*AC*⊥*BC*，∵平面*ADC*⊥平面*ABC*，且平面*ADC*∩平面*ABC*＝*AC*，*BC*⊂平面*ABC*，

∴*BC*⊥平面*ADC*，又*AD*⊂平面*ADC*，∴*BC*⊥*AD*．

![](images/852d8e9b225bc1fcbce0a62b4ed25e6d0428942361ade1e7025f26a4db160f1f.jpg)

![](images/f5f13630db2cbb985e4708e1edc525d2066ee4ac5a1fe21fdfeb257abcf8cd38.png)

(2)∵*E*为*AB*的中点，∴点*E*到平面*BCD*的距离等于点*A*到平面*BCD*距离的一半．

而平面*ADC*⊥平面*BCD*，∴过*A*作*AQ*⊥*CD*于*Q*，又∵平面*ADC*∩平面*BCD*＝*CD*，且*AQ*⊂平面*ADC*，

∴*AQ*⊥平面*BCD*，*AQ*就是点*A*到平面*BCD*的距离．

由(1)知*AC*＝，*AD*＝*DC*＝1，∴cos∠*ADC*＝＝－，

又0<∠*ADC*<π，∴∠*ADC*＝，∴在Rt△*QAD*中，∠*QDA*＝，*AD*＝1，

∴*AQ*＝*AD*·sin∠*QDA*＝1×＝．∴点*E*到平面*BCD*的距离为．

<strong>[例6]</strong>如图，高为1的等腰梯形<em>ABCD</em>中，<em>AM</em>＝<em>CD</em>＝<em>AB</em>＝1．现将△<em>AMD</em>沿<em>MD</em>折起，使平面<em>AMD</em>⊥平面<em>MBCD</em>，连接<em>AB</em>，<em>AC</em>．

(1)在*AB*边上是否存在点*P*，使*AD*∥平面*MPC?*

(2)当点*P*为*AB*边的中点时，求点*B*到平面*MPC*的距离．

![](images/0f56ba5848ee68da809818e730417203a9ea9512c8c4409d0c20eed7da9f5b31.jpg)

解析　(1)当*AP*＝*AB*时，有*AD*∥平面*MPC*．理由如下：

连接*BD*交*MC*于点*N*，连接*NP*．在梯形*MBCD*中，*DC*∥*MB*，＝＝，

在△*ADB*中，＝，∴*AD*∥*PN*．∵*AD*⊄平面*MPC*，*PN*⊂平面*MPC*，∴*AD*∥平面*MPC*．

![](images/1209130d1bd994d382401234a05bf378260c2787d620c13a982af3dc56717fb6.png)

(2)∵平面*AMD*⊥平面*MBCD*，平面*AMD*∩平面*MBCD*＝D*M*，*AM*⊥*DM*，∴*AM*⊥平面*MBCD*．

∴<em>V<sub>P</sub></em><sub>­</sub><em><sub>MBC</sub></em>＝×<em>S</em><sub>△</sub><em><sub>MBC</sub></em>×＝××2×1×＝．在△<em>MPC</em>中，<em>MP</em>＝<em>AB</em>＝，<em>MC</em>＝，

又<em>PC</em>＝＝，∴<em>S</em><sub>△</sub><em><sub>MPC</sub></em>＝×× ＝．

∴点*B*到平面*MPC*的距离为*d*＝＝＝．

【**对点训练**】

1．(2018·全国Ⅱ)如图，在三棱锥*P－ABC*中，*AB*＝*BC*＝2，*PA*＝*PB*＝*PC*＝*AC*＝4，*O*为*AC*的中点．

(1)证明：*PO*⊥平面*ABC*；

(2)若点*M*在棱*BC*上，且*MC*＝2*MB*，求点*C*到平面*POM*的距离．

![](images/e52fed22ca67dcef1a3d48a81c4b61622c60d1ea1f7dd340e3cc0d8129bf3ccc.jpg)

1．解析　(1)证明：因为*PA*＝*PC*＝*AC*＝4，*O*为*AC*的中点，所以*PO*⊥*AC*，且*PO*＝2．连接*OB*，

因为*AB*＝*BC*＝*AC*，所以△*ABC*为等腰直角三角形，且*OB*⊥*AC*，*OB*＝*AC*＝2．

所以<em>PO</em><sup>2</sup>＋<em>OB</em><sup>2</sup>＝<em>PB</em><sup>2</sup>，所以<em>PO</em>⊥<em>OB</em>．又因为<em>AC</em>∩<em>OB</em>＝<em>O</em>，所以<em>PO</em>⊥平面<em>ABC</em>．

![](images/64df13b1c0b72b2e35db28ce9884116ec76076d2db6a1a93bf551940511af7ea.jpg)

(2)作*CH*⊥*OM*，垂足为*H*，又由(1)可得*OP*⊥*CH*，所以*CH*⊥平面*POM*．

故*CH*的长为点*C*到平面*POM*的距离．

由题设可知*OC*＝*AC*＝2，*CM*＝*BC*＝，∠*ACB*＝45°，

所以*OM*＝，*CH*＝＝．所以点*C*到平面*POM*的距离为．

2．(2013·江西)如图，直四棱柱<em>ABCD</em>－<em>A</em><sub>1</sub><em>B</em><sub>1</sub><em>C</em><sub>1</sub><em>D</em><sub>1</sub>中，<em>AB</em>∥<em>CD</em>，<em>AD</em>⊥<em>AB</em>，<em>AB</em>＝2，<em>AD</em>＝，<em>AA</em><sub>1</sub>＝3，<em>E</em>

为*CD*上一点，*DE*＝1，*EC*＝3．

(1)证明：<em>BE</em>⊥平面<em>BB</em><sub>1</sub><em>C</em><sub>1</sub><em>C</em>；

(2)求点<em>B</em><sub>1</sub>到平面<em>EA</em><sub>1</sub><em>C</em><sub>1</sub>的距离．

![](images/b850c03a9a41b9c47492ce3c7e07cc27e60fb1fa064183a23a4b6b8433713013.jpg)

2．解析　(1)过*B*作*CD*的垂线交*CD*于*F*，则*BF*＝*AD*＝，*EF*＝*AB*－*DE*＝1，*FC*＝2．

在Rt△<em>BFE</em>中，<em>BE</em>＝．在Rt△<em>CFB</em>中，<em>BC</em>＝．在△<em>BEC</em>中，因为<em>BE</em><sup>2</sup>＋<em>BC</em><sup>2</sup>＝9＝<em>EC</em><sup>2</sup>，故<em>BE</em>⊥<em>BC</em>．

由<em>BB</em><sub>1</sub>⊥平面<em>ABCD</em>得<em>BE</em>⊥<em>BB</em><sub>1</sub>，又<em>BB</em><sub>1</sub>∩<em>BC</em>＝<em>B</em>，所以<em>BE</em>⊥平面<em>BB</em><sub>1</sub><em>C</em><sub>1</sub><em>C</em>．

![](images/2ae20e86783877e0cbad09ad7a6d93398c777ad57d23512f28d5b178214d7b9c.jpg)

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

(2)三棱锥<em>E</em>－<em>A</em><sub>1</sub><em>B</em><sub>1</sub><em>C</em><sub>1</sub>的体积<em>V</em>＝<em>AA</em><sub>1</sub>·＝．在Rt△<em>A</em><sub>1</sub><em>D</em><sub>1</sub><em>C</em><sub>1</sub>中，<em>A</em><sub>1</sub><em>C</em><sub>1</sub>＝＝3．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

同理，<em>EC</em><sub>1</sub>＝＝3，<em>A</em><sub>1</sub><em>E</em>＝＝2．故＝3．

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

设点<em>B</em><sub>1</sub>到平面<em>A</em><sub>1</sub><em>C</em><sub>1</sub><em>E</em>的距离为<em>d</em>，则三棱锥<em>B</em><sub>1</sub>－<em>A</em><sub>1</sub><em>C</em><sub>1</sub><em>E</em>的体积<em>V</em>＝·<em>d</em>·＝<em>d</em>，

从而<em>d</em>＝，<em>d</em>＝．即点<em>B</em><sub>1</sub>到平面<em>EA</em><sub>1</sub><em>C</em><sub>1</sub>的距离为．

3．如图，在三棱锥*A*—*BCD*中，△*ABC*是等腰直角三角形，且*AC*⊥*BC*，*BC*＝2，*AD*⊥平面*BCD*，*AD*

＝1．

(1)求证：平面*ABC*⊥平面*ACD*；

(2)若*E*为*AB*的中点，求点*A*到平面*CED*的距离．

![](images/946e26282e698ffff54397d00c035f590df30653403b3b3095dce743746b33c5.jpg)

3．解析　(1)因为*AD*⊥平面*BCD*，*BC*⊂平面*BCD*，所以*AD*⊥*BC*，又*AC*⊥*BC*，*AC*∩*AD*＝*A*，

*AC*，*AD*⊂平面*ABCD*，所以*BC*⊥平面*ACD*，因为*BC*⊂平面*ABC*，所以平面*ABC*⊥平面*ACD*．

![](images/39a862129fc850b0a6c08535efefac413ac2d5959445f62a746cb373626bd462.jpg)

(2)由已知可得*CD*＝，取*CD*的中点*F*，连接*EF*，因为*E*为*AB*的中点，所以*ED*＝*EC*＝*AB*＝，

所以△<em>ECD</em>为等腰三角形，从而<em>EF</em>＝，所以<em>S</em><sub>△</sub><em><sub>ECD</sub></em>＝××＝．

由(1)知<em>BC</em>⊥平面<em>ACD</em>，所以<em>E</em>到平面<em>ACD</em>的距离为1，<em>S</em><sub>△</sub><em><sub>ACD</sub></em>＝××1＝．

设点<em>A</em>到平面<em>CED</em>的距离为<em>d</em>，则<em>V</em><sub>三棱锥</sub><em><sub>A</sub></em><sub>—</sub><em><sub>ECD</sub></em>＝·<em>S</em><sub>△</sub><em><sub>ECD</sub></em>·<em>d</em>＝<em>V</em><sub>三棱锥</sub><em><sub>E</sub></em><sub>—</sub><em><sub>ACD</sub></em>＝·<em>S</em><sub>△</sub><em><sub>ACD</sub></em>·1，解得<em>d</em>＝．

4．已知三棱锥*P*－*ABC*中，*AC*⊥*BC*，*AC*＝*BC*＝2，*PA*＝*PB*＝*PC*＝3，*O*是*AB*的中点， *E*是*PB*的中

点．

(1)证明：平面*PAB*⊥平面*ABC*；

(2)求点*B*到平面*OEC*的距离．

![](images/7e37405f36f412667c57e7d674babd83e70364e9dadff3727c20884b3d762ac6.jpg)

4．解析　(1)连接*PO*，在△*PAB*中， *PA*＝*PB, O*是*AB*中点，∴*PO*⊥*AB*，又∵*AC*＝*BC*＝2, *AC*⊥*BC*，

∴<em>AB</em>＝2，<em>OB</em>＝<em>OC</em>＝．∵<em>PA</em>＝<em>PB</em>＝<em>PC</em>＝3，∴<em>PO</em>＝，<em>PC</em><sup>2</sup>＝<em>PO</em><sup>2</sup>＋<em>OC</em><sup>2</sup>，∴<em>PO</em>⊥<em>OC</em>．

又*AB*∩*OC*＝*O, AB*⊂平面*ABC, OC*⊂平面*ABC*，∴*PO*⊥平面*ABC*，∵*PO*⊂平面*PAB*，

∴平面*PAB*⊥平面*ABC*．

![](images/750a95ed6e9dc584c9762b3a4090b78ab1d9dfe1c24b7cee4c8f9c1c337bd9dd.jpg)

(2)∵*OE*是△*PAB*的中位线，∴*OE*＝．∵*O*是*AB*的中点， *AC*＝*BC*，∴*OC*⊥*AB*．

又平面*PAB*⊥平面*ABC*，两平面的交线为*AB*，∴*OC*⊥平面*PAB*，∵*OE*⊂平面*PAB*，∴*OC*⊥*OE*．

设点<em>B</em>到平面<em>OEC</em>的距离为<em>d</em>，则<em>V<sub>B</sub></em><sub>－</sub><em><sub>OEC</sub></em>＝<em>V<sub>E</sub></em><sub>－</sub><em><sub>OBC</sub></em>，∴×<em>S</em><sub>△</sub><em><sub>OEC</sub></em>·<em>d</em>＝×<em>S</em><sub>△</sub><em><sub>OBC</sub></em>×<em>OP</em>，

*d*＝＝＝．

5．在如图所示的几何体中，四边形*ABCD*是直角梯形，*AD*∥*BC*，*AB*⊥*BC*，*AD*＝2，*AB*＝3，*BC*＝*BE*＝7，△*DCE*是边长为6的正三角形．

(1)求证：平面*DEC*⊥平面*BDE*；

(2)求点*A*到平面*BDE*的距离．

![](images/b4685e54806fdda3c5f2a604a5268859e58e7adc5ef8b9628cb33dfbc3879685.jpg)

5．解析　(1)因为四边形*ABCD*为直角梯形，*AD*∥*BC*，*AB*⊥*BC*，*AD*＝2，*AB*＝3，所以*BD*＝，

又因为*BC*＝7，*CD*＝6，所以根据勾股定理可得*BD*⊥*CD*，因为*BE*＝7，*DE*＝6，同理可得*BD*⊥*DE*．

因为*DE*∩*CD*＝*D*，*DE*⊂平面*DEC*，*CD*⊂平面*DEC*，所以*BD*⊥平面*DEC*.因为*BD*⊂平面*BDE*，

所以平面*DEC*⊥平面*BDE*．

![](images/c67ad619347851199247d4628e7c5970deee2ffbbd1519f5032ba1ed6bc9180b.jpg)

(2)如图，取*CD*的中点*O*，连接*OE*，因为△*DCE*是边长为6的正三角形，

所以<em>EO</em>⊥<em>CD</em>，<em>EO</em>＝3，由(1)易知<em>EO</em>⊥平面<em>ABCD</em>，则<em>V<sub>E</sub></em><sub>－</sub><em><sub>ABD</sub></em>＝××2×3×3＝3，

又因为Rt△*BDE*的面积为×6×＝3，

设点<em>A</em>到平面<em>BDE</em>的距离为<em>h</em>，则由<em>V<sub>E</sub></em><sub>－</sub><em><sub>ABD</sub></em>＝<em>V<sub>A</sub></em><sub>－</sub><em><sub>BDE</sub></em>，得×3<em>h</em>＝3，所以<em>h</em>＝，

所以点*A*到平面*BDE*的距离为．

6．如图，在四棱锥*P*－*ABCD*中，底面*ABCD*是矩形，且*AD*＝2，*AB*＝1，*PA*⊥平面*ABCD*，*E*，*F*分别

是线段*AB*，*BC*的中点．

(1)证明：*PF*⊥*FD*；

(2)若*PA*＝1，求点*E*到平面*PFD*的距离．

![](images/f869497a447fed961cb3bbe5c2d181b3952434886e13244950c0346f0e37080d.jpg)

6．解析　(1)证明：连接*AF*，则*AF*＝，又*DF*＝，*AD*＝2，

所以<em>DF</em><sup>2</sup>＋<em>AF</em><sup>2</sup>＝<em>AD</em><sup>2</sup>，所以<em>DF</em>⊥<em>AF</em>．

因为*PA*⊥平面*ABCD*，所以*DF*⊥*PA*，又*PA*∩*AF*＝*A*，所以*DF*⊥平面*PAF*，

又*PF*⊂平面*PAF*，所以*DF*⊥*PF*．

![](images/f3bd6cd94e49e1f8aa9a3e322ddddd3f722066340083487ff7cad21573612354.jpg)

(2)连接<em>EP</em>，<em>ED</em>，<em>EF</em>．因为<em>S</em><sub>△</sub><em><sub>EFD</sub></em>＝<em>S</em><sub>矩形</sub><em><sub>ABCD</sub></em>－<em>S</em><sub>△</sub><em><sub>BEF</sub></em>－<em>S</em><sub>△</sub><em><sub>ADE</sub></em>－<em>S</em><sub>△</sub><em><sub>CDF</sub></em>＝2－＝，

所以<em>V</em><sub>三棱锥</sub><em><sub>P</sub></em><sub>－</sub><em><sub>EFD</sub></em>＝<em>S</em><sub>△</sub><em><sub>EFD</sub></em>·<em>PA</em>＝××1＝．

设点<em>E</em>到平面<em>PFD</em>的距离为<em>h</em>，则由<em>V</em><sub>三棱锥</sub><em><sub>E</sub></em><sub>－</sub><em><sub>PFD</sub></em>＝<em>V</em><sub>三棱锥</sub><em><sub>P</sub></em><sub>－</sub><em><sub>EFD</sub></em>得

<em>S</em><sub>△</sub><em><sub>PFD</sub></em>·<em>h</em>＝×·<em>h</em>＝，解得<em>h</em>＝，即点<em>E</em>到平面<em>PFD</em>的距离为．

7．如图，四棱锥*P*－*ABCD*中，*PA*⊥底面*ABCD*，底面*ABCD*为梯形，*AD*∥*BC*，*CD*⊥*BC*，*AD*＝2，*AB*

＝*BC*＝3，*PA*＝4，*M*为*AD*的中点，*N*为*PC*上一点，且*PC*＝3*PN*．

(1)求证：*MN*∥平面*PAB*；

(2)求点*M*到平面*PAN*的距离．

![](images/3cd3c08ca7cd1580e5f078347461f54fbbcc85edb697bd360e4f7d48a7f5ff4e.jpg)

7．解析　(1)证明：在平面*PBC*内作*NH*∥*BC*交*PB*于点*H*，连接*AH*，

在△*PBC*中，*NH*∥*BC*，且*NH*＝*BC*＝1，*AM*＝*AD*＝1，又*AD*∥*BC*，∴*NH*∥*AM*且*NH*＝*AM*，

∴四边形*AMNH*为平行四边形，∴*MN*∥*AH*，又*AH*⊂平面*PAB*，*MN*⊄平面*PAB*，∴*MN*∥平面*PAB*．

![](images/804df89191857d78bec38ec588138da96469b021f2209c769044f19e0fe06e65.jpg)

(2)连接*AC*，*MC*，*PM*，平面*PAN*即为平面*PAC*，设点*M*到平面*PAC*的距离为*h*．

由题意可得<em>CD</em>＝2，<em>AC</em>＝2，∴<em>S</em><sub>△</sub><em><sub>PAC</sub></em>＝<em>PA</em>·<em>AC</em>＝4，<em>S</em><sub>△</sub><em><sub>AMC</sub></em>＝<em>AM</em>·<em>CD</em>＝，

由<em>V<sub>M</sub></em><sub>­</sub><em><sub>PAC</sub></em>＝<em>V<sub>P</sub></em><sub>­</sub><em><sub>AMC</sub></em>，得<em>S</em><sub>△</sub><em><sub>PAC</sub></em>·<em>h</em>＝<em>S</em><sub>△</sub><em><sub>AMC</sub></em>·<em>PA</em>，即4<em>h</em>＝×4，∴<em>h</em>＝，

∴点*M*到平面*PAN*的距离为．

8．如图，在四棱锥*P*－*ABCD*中，侧面*PAD*是边长为2的正三角形，且与底面垂直，底面*ABCD*是∠*ABC*

＝60°的菱形，*M*为*PC*的中点．

(1)求证：*PC*⊥*AD*；

(2)求点*D*到平面*PAM*的距离．

![](images/a88863b8642daa8a7fc90ef55cdba3c30c44413aad7a3f8ca923ac2598abcd4b.jpg)

8．解析　(1)证明：如图，取*AD*的中点*O*，连接*OP*，*OC*，*AC*，由题意易知△*ACD*为正三角形．

所以*OC*⊥*AD*，又△*PAD*是正三角形，*O*为*AD*的中点，所以*OP*⊥*AD*，

又*OC*∩*OP*＝*O*，所以*AD*⊥平面*POC*，又*PC*⊂平面*POC*，所以*PC*⊥*AD*．

![](images/675239a0a63bb862916d420549fc87c683d4b0e2b2f381cfbe132852f99e068c.jpg)

(2)点*D*到平面*PAM*的距离即点*D*到平面*PAC*的距离，由(1)可知，*PO*⊥*AD*，

又平面*PAD*⊥平面*ABCD*，平面*PAD*∩平面*ABCD*＝*AD*，*PO*⊂平面*PAD*，

所以*PO*⊥平面*ABCD*，即*PO*为三棱锥*P*－*ACD*的高．

在Rt△*POC*中，*PO*＝*OC*＝，*PC*＝，

在△*PAC*中，*PA*＝*AC*＝2，*PC*＝，边*PC*上的高*AM*＝＝＝，

所以<em>S</em><sub>△</sub><em><sub>PAC</sub></em>＝<em>PC</em>·<em>AM</em>＝××＝．

设点<em>D</em>到平面<em>PAC</em>的距离为<em>h</em>，由<em>V<sub>D</sub></em><sub>­</sub><em><sub>PAC</sub></em>＝<em>V<sub>P</sub></em><sub>­</sub><em><sub>ACD</sub></em>，得<em>S</em><sub>△</sub><em><sub>PAC</sub></em>·<em>h</em>＝<em>S</em><sub>△</sub><em><sub>ACD</sub></em>·<em>PO</em>，

又<em>S</em><sub>△</sub><em><sub>ACD</sub></em>＝×2×＝，所以×·<em>h</em>＝××，解得<em>h</em>＝．

故点*D*到平面*PAM*的距离为．

9．如图，在四棱锥*P*－*ABCD*中，*PC*⊥平面*ABCD*，底面*ABCD*是平行四边形，*AB*＝*BC*＝2*a*，*AC*＝2

*a*，*E*是*PA*的中点．

(1)求证：平面*BED*⊥平面*PAC*；

(2)求点*E*到平面*PBC*的距离．

![](images/450983f58c4c2054939fd98c2548b5cdc137d775e7f53babf049f58164501757.jpg)

9．解析　(1)证明：在平行四边形*ABCD*中，*AB*＝*BC*，∴四边形*ABCD*是菱形，∴*BD*⊥*AC*．

∵*PC*⊥平面*ABCD*，*BD*⊂平面*ABCD*，∴*PC*⊥*BD*，又*PC*∩*AC*＝*C*，∴*BD*⊥平面*PAC*，

∵*BD*⊂平面*BED*，∴平面*BED*⊥平面*PAC*．

![](images/35bd7a49bbc9e6e9d99438ba076c7d88acb3b38ec0e58c01029e02ff5a22ac03.jpg)

(2)设*AC*交*BD*于点*O*，连接*OE*，如图．在△*PCA*中，易知*O*为*AC*的中点，又*E*为*PA*的中点，

∴*EO*∥*PC*，∵*PC*⊂平面*PBC*，*EO*⊄平面*PBC*，∴*EO*∥平面*PBC*．

∴点*O*到平面*PBC*的距离就是点*E*到平面*PBC*的距离．∵*PC*⊥平面*ABCD*，*PC*⊂平面*PBC*，

∴平面*PBC*⊥平面*ABCD*，且两平面的交线为*BC*．在平面*ABCD*内过点*O*作*OH*⊥*BC*于点*H*，

则<em>OH</em>⊥平面<em>PBC</em>，在Rt△<em>BOC</em>中，<em>BC</em>＝2<em>a</em>，<em>OC</em>＝<em>AC</em>＝<em>a</em>，∴<em>OB</em> ＝<em>a</em>．由<em>S</em><sub>△</sub><em><sub>BOC</sub></em>＝<em>OC</em>·<em>OB</em>＝<em>BC</em>·<em>OH</em>，

得*OH*＝＝＝*a*，∴点*E*到平面*PBC*的距离为*a*．

10．如图1，在直角梯形*ABCP*中，*CP*∥*AB*，*CP*⊥*BC*，*AB*＝*BC*＝*CP*，*D*是*CP*的中点，将△*PAD*沿*AD*

折起，使点*P*到达点*P*′的位置得到图2，点*M*为棱*P*′*C*上的动点．

①当*M*在何处时，平面*ADM*⊥平面*P*′*BC*，并证明；

②若*AB*＝2，∠*P*′*DC*＝135°，证明：点*C*到平面*P*′*AD*的距离等于点*P*′到平面*ABCD*的距离，并求出该距离．

![](images/efd3217da4a5e402721f4ac8e052f5ca7bc3cb4aa088f41bac735265537468b5.jpg)

10．解析　①当点*M*为*P*′*C*的中点时，平面*ADM*⊥平面*P*′*BC*，证明如下：

∵*DP*′＝*DC*，*M*为*P*′*C*的中点，∴*P*′*C*⊥*DM*，

∵*AD*⊥*DP*′，*AD*⊥*DC*，*DP*′∩*DC*＝*D*，∴*AD*⊥平面*DP*′*C*，∴*AD*⊥*P*′*C*，

又*DM*∩*AD*＝*D*，∴*P*′*C*⊥平面*ADM*，∴平面*ADM*⊥平面*P*′*BC*．

②在平面*P*′*CD*上作*P*′*H*⊥*CD*的延长线于点*H*，

![](images/4a23f70ba88de2a9032bf081c670fb1d7f554848fdfd63be4cafd23c6caa7306.jpg)

由①中*AD*⊥平面*DP*′*C*，可知平面*P*′*CD*⊥平面*ABCD*，

又平面*P*′*CD*∩平面*ABCD*＝*CD*，*P*′*H*⊂平面*P*′*CD*，*P*′*H*⊥*CD*，∴*P*′*H*⊥平面*ABCD*，

由题意，得*DP*′＝2，∠*P*′*DH*＝45°，∴*P*′*H*＝，

又<em>V<sub>P</sub></em><sub>′－</sub><em><sub>ADC</sub></em>＝<em>V<sub>C</sub></em><sub>－</sub><em><sub>P</sub></em><sub>′</sub><em><sub>AD</sub></em>，设点<em>C</em>到平面<em>P</em>′<em>AD</em>的距离为<em>h</em>，即<em>S</em><sub>△</sub><em><sub>ADC</sub></em>×<em>P</em>′<em>H</em>＝<em>S</em><sub>△</sub><em><sub>P</sub></em><sub>′</sub><em><sub>AD</sub></em>×<em>h</em>，

由题意，知△<em>ADC</em>≌△<em>ADP</em>′，则<em>S</em><sub>△</sub><em><sub>ADC</sub></em>＝<em>S</em><sub>△</sub><em><sub>P</sub></em><sub>′</sub><em><sub>AD</sub></em>．∴<em>P</em>′<em>H</em>＝<em>h</em>，

故点*C*到平面*P*′*AD*的距离等于点*P*′到平面*ABCD*的距离，且该距离为．

11．如图1，在矩形*ABCD*中，*AB*＝12，*AD*＝6，*E*，*F*分别为*CD*，*AB*边上的点，且 *DE*＝3，*BF*＝4，

将△*BCE*沿*BE*折起来至△*PBE*的位置(如图2所示)，连接*AP*，*PF*，其中*PF*＝2．

(1)求证：*PF*⊥平面*ABED*；

(2)求点*A*到平面*PBE*的距离．

![](images/efd32d3b446f50f4cdd2738172d919c9798ea6a8289dcfce805a46be7a0aa537.jpg)  
图1　　　　　　　　　　　图2

11．解析　(1)在题图2中，连接*EF*，由题意可知*PB*＝*BC*＝*AD*＝6，*PE*＝*CE*＝*CD*－*DE*＝9，

在△<em>PBF</em>中，<em>PF</em><sup>2</sup>＋<em>BF</em><sup>2</sup>＝20＋16＝36＝<em>PB</em><sup>2</sup>，所以<em>PF</em>⊥<em>BF</em>．

在题图1中，连接*EF*，作*EH*⊥*AB*于点*H*，利用勾股定理，得*EF*＝＝，

在△<em>PEF</em>中，<em>EF</em><sup>2</sup>＋<em>PF</em><sup>2</sup>＝61＋20＝81＝<em>PE</em><sup>2</sup>，所以<em>PF</em>⊥<em>EF</em>，

又因为*BF*∩*EF*＝*F*，*BF*⊂平面*ABED*，*EF*⊂平面*ABED*，所以*PF*⊥平面*ABED*．

(2)如图，连接*AE*，由(1)知*PF*⊥平面*ABED*，

![](images/b7e650e05fff922c0ce7e878ab7a5903ed7b32df53759b593346fd565de15359.jpg)

所以*PF*为三棱锥*P*－*ABE*的高．设点*A*到平面*PBE*的距离为*h*，

因为<em>V<sub>A</sub></em><sub>－</sub><em><sub>PBE</sub></em>＝<em>V<sub>P</sub></em><sub>－</sub><em><sub>ABE</sub></em>，即××6×9×<em>h</em>＝××12×6×2，所以<em>h</em>＝，

即点*A*到平面*PBE*的距离为．

12．如图，在直角梯形*ABCD*中，*AD*∥*BC*，*AB*⊥*BC*，*BD*⊥*DC*，点*E*是*BC*边的中点，将△*ABD*沿*BD*

折起，使平面*ABD*⊥平面*BCD*，连接*AE*，*AC*，*DE*，得到如图所示的空间几何体．

(1)求证：*AB*⊥平面*ADC*；

(2)若*AD*＝1，*AB*＝，求点*B*到平面*ADE*的距离．

![](images/4312f912bd720dc6c3d4fc0ea88e5f594abe9e46803436bffef861f22b8062c6.jpg)

![](images/751227f1dd65dbbc504187544f060f00f8cbb972f7f22f96aee1b60aa24c914e.jpg)

12．解析　(1)因为平面*ABD*⊥平面*BCD*，平面*ABD*∩平面*BCD*＝*BD*，

又*BD*⊥*DC*，*DC*⊂平面*BCD*，所以*DC*⊥平面*ABD*，因为*AB*⊂平面*ABD*，所以*DC*⊥*AB*．

又*AD*⊥*AB*，*DC*∩*AD*＝*D*，*AD*，*DC*⊂平面*ADC*，所以*AB*⊥平面*ADC*．

(2)因为*AB*＝，*AD*＝1，所以*BD*＝．依题意△*ABD*∽△*DCB*，所以＝，即＝．

所以*CD*＝，故*BC*＝3，由于*AB*⊥平面*ADC*，*AB*⊥*AC*，*E*为*BC*的中点，所以*AE*＝＝．

同理<em>DE</em>＝＝，所以<em>S</em><sub>△</sub><em><sub>ADE</sub></em>＝×1× ＝，因为<em>DC</em>⊥平面<em>ABD</em>，

所以<em>V<sub>A</sub></em><sub>—</sub><em><sub>BCD</sub></em>＝<em>CD</em>·<em>S</em><sub>△</sub><em><sub>ABD</sub></em>＝，设点<em>B</em>到平面<em>ADE</em>的距离为<em>d</em>，

则<em>d</em>·<em>S</em><sub>△</sub><em><sub>ADE</sub></em>＝<em>V<sub>B</sub></em><sub>—</sub><em><sub>ADE</sub></em>＝<em>V<sub>A</sub></em><sub>—</sub><em><sub>BDE</sub></em>＝<em>V<sub>A</sub></em><sub>—</sub><em><sub>BCD</sub></em>＝，所以<em>d</em>＝，即点<em>B</em>到平面<em>ADE</em>的距离为．

