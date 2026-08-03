---
question_id: "node-030:question:15:91"
question_number: "15"
context_key: "node-030"
question_source: "C:\\Mathematics-Knowledge\\Secondary-School-Mathematics-Knowledge-Map\\测试\\新建文件夹\\graph\\03-第三章_函数的概念与性质\\课时1_函数的单调性\\课时1_函数的单调性.md"
question_body_sha256: 006d7e5d4286c20474959d4327dcf87e85dccd6bb559391b3f17edee3552053d
answer_status: matched
---

# Question 15

<!-- question-source:start -->
15.[河南洛阳一高2025摸底]已知定义在R上的函数 $f(x)$ 满足 $f(x+y)=f(x)+f(y)+2$ ， $f(1)=2$ ，且当x>0时， $f(x)>-2$ ，则不等式 $f(x^{2}+x)+f(1-2x)>8$ 的解集为（）
A. $\{x \mid x < -2 \text{ 或 } x > 1\}$ B. $\{x \mid x < -1 \text{ 或 } x > 2\}$ C. $\{x \mid -1 < x < 2\}$ D. $\{x \mid -2 < x < 1\}$
<!-- question-source:end -->

## 答案与解析

<!-- answer-source:start -->
15.B 【解析】已知 $f(x + y) = f(x) + f(y) + 2$ ， $f(1) = 2$ ，令 $x = y = 1$ ，则 $f(2) = f(1) + f(1) + 2 = 6$ ，令 $x = 2, y = 1$ ，则 $f(3) = f(2) + f(1) + 2 = 10.$

令 $x = x_{2}, y = x_{1} - x_{2}$ , 且 $x_{1} > x_{2}$ , 则 $f(x_{1}) = f(x_{2}) + f(x_{1} - x_{2}) + 2$ , 整理得 $f(x_{1}) - f(x_{2}) = f(x_{1} - x_{2}) + 2$ , 因为 $x_{1} > x_{2}$ , 所以 $x_{1} - x_{2} > 0$ , 可得 $f(x_{1} - x_{2}) > -2$ , 所以 $f(x_{1}) - f(x_{2}) = f(x_{1} - x_{2}) + 2 > 0$ , 即 $f(x_{1}) > f(x_{2})$ , 可知 $f(x)$ 在 $\mathbf{R}$ 上单调递增. 又 $f(x^{2} + x) + f(1 - 2x) > 8$ , 即 $f(x^{2} + x) + f(1 - 2x) + 2 > 10$ , 可得 $f(x^{2} + x + 1 - 2x) > f(3)$ , 即 $f(x^{2} - x + 1) > f(3)$ , 结合 $f(x)$ 在定义域 $\mathbf{R}$ 上单调递增, 可得 $x^{2} - x + 1 > 3$ , 解得 $x < -1$ 或 $x > 2$ , 所以不等式 $f(x^{2} + x) + f(1 - 2x) > 8$ 的解集为 $\{x \mid x < -1$ 或 $x > 2\}$ . 故选 B.
<!-- answer-source:end -->
