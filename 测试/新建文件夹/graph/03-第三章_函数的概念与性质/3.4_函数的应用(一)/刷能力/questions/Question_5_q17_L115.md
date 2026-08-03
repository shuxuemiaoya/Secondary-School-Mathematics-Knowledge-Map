---
question_id: "node-036:question:5:115"
question_number: "5"
context_key: "node-036:刷能力"
question_source: "C:\\Mathematics-Knowledge\\Secondary-School-Mathematics-Knowledge-Map\\测试\\新建文件夹\\graph\\03-第三章_函数的概念与性质\\3.4_函数的应用(一)\\3.4_函数的应用(一).md"
question_body_sha256: af8b169444666005617ef2de54ff58509a0a25ba9ed82da59f8e021f485122ac
answer_status: matched
---

# Question 5

<!-- question-source:start -->
5.[河北石家庄二中2025高一期中]某机械厂生产一批零件,受生产能力和技术水平的限制,会产生一些次品,其次品率p与日产量x(万件)之间满足关系: $p=\begin{cases}\frac{1}{12-x},0<x\leqslant m,\\\frac{3}{4},x>m\end{cases}$ (其中m为小于12的正整数).已知每生产1万件合格的零件该厂可以盈利30万元,但每生产1万件次品将亏损10万元,故厂方希望定出合适的日产量使得利润最大.(注:次品率=次品数/生产量,如p=0.1表示每生产10件产品,有1件为次品,其余为合格品).
(1)将生产这批零件每天的盈利额y(万元)表示为关于日产量x(万件)的函数.
(2)当日产量为多少时,该厂可获得最大利润?

视频微课

错题本
<!-- question-source:end -->

## 答案与解析

<!-- answer-source:start -->
5.【解】(1)由题意知 $y=30\cdot(1-p)x-10\cdot px=(30-40p)x$ ,
当 $0 < x \leqslant m$ 时， $p = \frac{1}{12 - x}$ ，故 $y = \left(30 - 40 \cdot \frac{1}{12 - x}\right)x = \frac{320x - 30x^2}{12 - x}$ 当 x > m 时， $p = \frac{3}{4}$ ，故 $y = \left(30 - 40 \times \frac{3}{4}\right) \cdot x = 0$ ，
所以盈利额 y（万元）与日产量 x（万件）之间的函数关系为 $y=\left\{\begin{aligned}-30x^{2}+320x\\12-x\end{aligned}\right.$ , $0<x\leqslant m$ ,
(2) 当 x > m 时, 每天的盈利额为 0 元, 则只需求当 $0 < x \leqslant m$ 时 y 的最大值.
设 $u=12-x,0<x\leqslant m$ ，则 x=12-u，且 $u\in$

[12-m,12)，
则 $y = \frac{-30(12-u)^{2}+320(12-u)}{u} = \frac{-30u^{2}+400u-480}{u}=-30\left(u+\frac{16}{u}\right)+400,$ ①当 $12 - m \leqslant 4$ ，即 $8 \leqslant m < 12$ 时， $y = -30\left(u + \frac{16}{u}\right) + 400 \leqslant -30 \times 2\sqrt{u \cdot \frac{16}{u}} +$
<!-- answer-source:end -->
