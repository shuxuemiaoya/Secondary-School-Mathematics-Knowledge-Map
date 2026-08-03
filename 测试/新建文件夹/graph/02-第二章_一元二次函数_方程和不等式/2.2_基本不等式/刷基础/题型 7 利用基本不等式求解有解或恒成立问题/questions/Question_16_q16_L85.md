---
question_id: "node-018:question:16:85"
question_number: "16"
context_key: "node-018"
question_source: "C:\\Mathematics-Knowledge\\Secondary-School-Mathematics-Knowledge-Map\\测试\\新建文件夹\\graph\\02-第二章_一元二次函数_方程和不等式\\2.2_基本不等式\\2.2_基本不等式.md"
question_body_sha256: b96abaeb59f42c39213a90648b690777721c2bbe0ea868857c4fed5c74fd6ee8
answer_status: matched
---

# Question 16

<!-- question-source:start -->
16. 已知 $a > 0, b > 0$ ，且 $ab = 1$ ，不等式 $\frac{1}{a} + \frac{1}{b} + \frac{m}{a + b} \geqslant 4$ 恒成立，则正实数 $m$ 的取值范围是（）
A. $\{m \mid m \geqslant 2\}$ B. $\{m \mid m \geqslant 4\}$ C. $\{m \mid m \geqslant 6\}$ D. $\{m \mid m \geqslant 8\}$
<!-- question-source:end -->

## 答案与解析

<!-- answer-source:start -->
16.B 【解析】由题设得 $m \geqslant 4(a + b) - \left(\frac{1}{a} + \frac{1}{b}\right)(a + b) = 4(a + b) - (a + b)^2$ 恒成立，而 $4(a + b) - (a + b)^2 = 4 - (a + b - 2)^2$ ，又 $a + b \geqslant 2\sqrt{ab} = 2$ ，当且仅当 $a = b = 1$ 时等号成立，所以 $4(a + b) - (a + b)^2 \leqslant 4$ ，当且仅当 $a = b = 1$ 时等号成立，故 $m \geqslant$ →巧思：用换元法令 $t = a + b, t \geqslant 2$ ，得 $4t - t^2 = -(t - 2)^2 + 4 \leqslant 4$ 从而得所求范围

多种解法 不等式 $\frac{1}{a} + \frac{1}{b} + \frac{m}{a + b} \geqslant 4$ 恒成立, 即 $\frac{a + b}{ab} + \frac{m}{a + b} \geqslant 4$ 恒成立, 即 $a + b + \frac{m}{a + b} \geqslant 4$ 恒成立, 而 $a + b + \frac{m}{a + b} \geqslant 2\sqrt{m}$ , 当且仅当 $a + b = \frac{m}{a + b}$ , 即 $(a + b)^2 = m$ 时取等号, 故 $2\sqrt{m} \geqslant 4$ . 又 $m$ 是正实数, 故 $m \geqslant 4$ , 故选 B.

规律方法 含参数的不等式恒成立问题,通过分离参数,把参数的取值范围问题化归为代数式的最值问题. a>y 恒成立 $\Leftrightarrow a>y_{\max}$ , a<y 恒成立 $\Leftrightarrow a<y_{\min}$ .
<!-- answer-source:end -->
