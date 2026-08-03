---
question_id: "node-036:question:1:96"
question_number: "1"
context_key: "node-036:刷能力"
question_source: "C:\\Mathematics-Knowledge\\Secondary-School-Mathematics-Knowledge-Map\\测试\\新建文件夹\\graph\\03-第三章_函数的概念与性质\\3.4_函数的应用(一)\\3.4_函数的应用(一).md"
question_body_sha256: ceba0924fe7109289d9c5a9d95535ca051c225b2b13ecdbc3fa9f3a59fb37d38
answer_status: matched
---

# Question 1

<!-- question-source:start -->
1. 一家报刊推销员从报社买进报纸的价格是每份2元, 卖出的价格是每份3元, 卖不完的还可以以每份0.8元的价格退回报社. 在一个月(以30天计算)内有20天每天可卖出400份, 其余10天每天只能卖出250份, 且每天从报社买进报纸的份数都相同, 要使推销员每月所获得的利润最大, 则应该每天从报社买进报纸 ( )
A. 215份 B. 350份
C. 400份 D. 250份
<!-- question-source:end -->

## 答案与解析

<!-- answer-source:start -->
1. C 【解析】根据题意,设每天从报社买进 $x(250 \leqslant x \leqslant 400, x \in \mathbb{N})$ 份报纸,每月所获利润为 y 元,具体情况如表.

<table><tr><td></td><td>数量/份</td><td>单价/元</td><td>金额/元</td></tr><tr><td>买进</td><td>30x</td><td>2</td><td>60x</td></tr><tr><td>卖出</td><td>20x+10×250</td><td>3</td><td>60x+7500</td></tr><tr><td>退回</td><td>10(x-250)</td><td>0.8</td><td>8x-2000</td></tr></table>

$\therefore y = \left[(60x + 7500) + (8x - 2000)\right] - 60x$ 敲黑板：收入 $=$ 卖出 $+$ 退回 $= 8x + 5500(250\leqslant x\leqslant 400,x\in \mathbf{N}).$ ∴ $y = 8x + 5500$ 在[250,400]上单调递增，
∴当 $x = 400$ 时， $y$ 取得最大值8700.即每天从报社买进400份报纸时，每月获得的利润最大，最大利润为8700元.故选C.
<!-- answer-source:end -->
