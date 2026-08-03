---
question_id: "node-038:question:3:64"
question_number: "3"
context_key: "node-038:刷原创"
question_source: "C:\\Mathematics-Knowledge\\Secondary-School-Mathematics-Knowledge-Map\\测试\\新建文件夹\\graph\\03-第三章_函数的概念与性质\\第三章高考强化\\第三章高考强化.md"
question_body_sha256: 1915b09b1f15ac0ede8716e896a2843a2204b7080a95bba26ee090593109d2ec
answer_status: matched
---

# Question 3

<!-- question-source:start -->
3. 已知定义在 $(- \infty, 0) \cup (0, +\infty)$ 上的函数 $f(x)$ 满足 $f(x) = f(-x) + \frac{2}{x}$ , 对任意的 $x_1, x_2 > 0$ 且 $x_1 \neq x_2$ , 都有 $\frac{f(x_1) - f(x_2)}{x_1 - x_2} < -\frac{1}{x_1 x_2}$ .

(1)试判断函数 $f(x)-\frac{1}{x}$ 的奇偶性,并证明你的结论;

(2) 解不等式 $f(x - 3) > f(x + 2) + \frac{5}{x^2 - x - 6}$ .
<!-- question-source:end -->

## 答案与解析

<!-- answer-source:start -->
3.【解】(1) $f(x)-\frac{1}{x}$ 为偶函数,理由如下:
记 $g(x)=f(x)-\frac{1}{x}$ ，因为函数 $g(x)$ 的定义域为 $D=\{x \mid x \neq 0\}$ ，所以 $\forall x \in D$ ，有 $-x \in D$ .
又 $f(x)=f(-x)+2\cdot\frac{1}{x}$ ，所以 $f(x)-\frac{1}{x}=$ $f(-x)-\frac{1}{-x}$ ，即 $g(x)=g(-x)$ ，所以函数 $g(x)=f(x)-\frac{1}{x}$ 为偶函数.
(2) 因为 $f(x-3)>f(x+2)+\frac{5}{x^{2}-x-6}$ ，即 $f(x-3)>f(x+2)+\frac{(x+2)-(x-3)}{(x-3)(x+2)}$ ，则 $f(x-3)-\frac{1}{x-3}>f(x+2)-\frac{1}{x+2}$ ，所以 $g(x-3)>g(x+2)$ .
又对任意的 $x_{1}, x_{2} > 0$ 且 $x_{1} \neq x_{2}$ $\frac{\left[f(x_1) - \frac{1}{x_1}\right] - \left[f(x_2) - \frac{1}{x_2}\right]}{x_1 - x_2} = \frac{f(x_1) - f(x_2)}{x_1 - x_2} - \frac{\frac{1}{x_1} - \frac{1}{x_2}}{x_1 - x_2} = \frac{f(x_1) - f(x_2)}{x_1 - x_2} + \frac{1}{x_1 x_2}.$ 因为 $\frac{f(x_1) - f(x_2)}{x_1 - x_2} < -\frac{1}{x_1 x_2}$ ，所以 $\frac{\left[f(x_1) - \frac{1}{x_1}\right] - \left[f(x_2) - \frac{1}{x_2}\right]}{x_1 - x_2} < 0$ ，故偶函数 $g(x) = f(x) - \frac{1}{x}$ 在 $(0, +\infty)$ 上单调递减。 $g(x - 3) > g(x + 2)$ 等价于 $g(|x - 3|) > g(|x + 2|)$ ，所以 $\begin{cases} x - 3 \neq 0, \\ x + 2 \neq 0, \\ |x - 3| < |x + 2|, \end{cases}$ 解得 $x >$ 避坑：注意分母不能为0 $\frac{1}{2}$ 且 $x \neq 3$ ，故所求不等式的解集为 $\left(\frac{1}{2}, 3\right) \cup (3, +\infty)$ .
<!-- answer-source:end -->
