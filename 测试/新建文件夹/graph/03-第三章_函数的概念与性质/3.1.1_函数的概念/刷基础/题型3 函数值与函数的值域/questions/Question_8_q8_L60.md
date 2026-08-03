---
question_id: "node-025:question:8:60"
question_number: "8"
context_key: "node-025"
question_source: "C:\\Mathematics-Knowledge\\Secondary-School-Mathematics-Knowledge-Map\\测试\\新建文件夹\\graph\\03-第三章_函数的概念与性质\\3.1.1_函数的概念\\3.1.1_函数的概念.md"
question_body_sha256: f93efd0370e512e1e0dd55679af28475a294eab579db1bb8376ebb66321ea72c
answer_status: matched
---

# Question 8

<!-- question-source:start -->
8.[浙江杭州2025高一月考]下列函数中,值域为[0,4]的是
A. $f(x)=x-1,x\in\{1,2,3,4,5\}$ B. $f(x)=-x^{2}+4$ C. $f(x)=\sqrt{16-x^{2}}$ D. $f(x)=x+\frac{1}{x}-2(x>0)$
<!-- question-source:end -->

## 答案与解析

<!-- answer-source:start -->
8. C 【解析】对于 A, $f(x)$ 的值域为 $\{0,1,2,3,4\}$ , A 错误；

$\left(x - \frac{1}{x^2}\right)\Big| + \frac{8}{x} = 2\left(x + \frac{4}{x}\right) \geqslant 8$ ，当且仅当 $x = 2$ 时等号成立，故 $a \leqslant 8$ .
若 $x < 0$ ，则 $-a \leqslant \left|x + \frac{1}{x^2}\right| + \left|x - \frac{1}{x^2}\right| + \frac{8}{|x|}$ 恒成立，
因为 $\left|x + \frac{1}{x^2}\right| + \left|x - \frac{1}{x^2}\right| + \frac{8}{|x|} \geqslant \left(x + \frac{1}{x^2}\right) + \left(x - \frac{1}{x^2}\right)\Big| + \frac{8}{|x|} = 2\left(|x| + \frac{4}{|x|}\right) \geqslant 8$ ，当且仅当 $x = -2$ 时等号成立，故 $-a \leqslant 8$ ，即 $a \geqslant -8$ .
综上，实数 $a$ 的取值范围为 $\{a | -8 \leqslant a \leqslant 8\}$ .

对于 B, $f(x)$ 的值域为 $(-∞,4]$ , B 错误；
对于 C, 由 $16-x^{2} \geqslant 0$ 得 $-4 \leqslant x \leqslant 4$ ，即 $f(x)$ 的定义域为 $[-4,4]$ ，当 $x \in [-4,4]$ 时，

避坑：此题要先确定函数的定义域，不可看到根号认为值域就是 $[0, +\infty)$ $16 - x^{2} \in [0, 16], \therefore f(x) \in [0, 4]$ ，C 正确；对于 D，当 $x > 0$ 时， $x + \frac{1}{x} \geqslant 2$ ，当且仅当 $x = 1$ 时取等号， $\therefore f(x) \in [0, +\infty)$ ，D 错误。故选 C.
<!-- answer-source:end -->
