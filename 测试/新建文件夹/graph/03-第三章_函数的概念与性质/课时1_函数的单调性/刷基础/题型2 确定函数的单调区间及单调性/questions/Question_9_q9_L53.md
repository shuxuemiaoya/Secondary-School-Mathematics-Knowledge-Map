---
question_id: "node-030:question:9:53"
question_number: "9"
context_key: "node-030"
question_source: "C:\\Mathematics-Knowledge\\Secondary-School-Mathematics-Knowledge-Map\\测试\\新建文件夹\\graph\\03-第三章_函数的概念与性质\\课时1_函数的单调性\\课时1_函数的单调性.md"
question_body_sha256: 1d9d27dd045aa52b64e38269d7e0395e2f841acf6fd98071de452cc241d2e107
answer_status: matched
---

# Question 9

<!-- question-source:start -->
9.[山东曲阜部分学校2025高一质量检测]已知函数 $f(x)=\frac{ax+b}{x^{2}+1}$ 且经过 $(-1,-1),\left(\frac{1}{2},\frac{4}{5}\right)$ 两点.
在实数里,负数永远比零小;在生活里,没有思想比无知更糟。

(1) 求函数 $f(x)$ 的解析式;

(2) 利用单调性的定义证明: $f(x)$ 在 $(-1,1)$ 上单调递增.
<!-- question-source:end -->

## 答案与解析

<!-- answer-source:start -->
9.（1）【解】将点 $(-1, - 1),\left(\frac{1}{2},\frac{4}{5}\right)$ 的坐标代入解析式得 $\left\{ \begin{array}{l} \frac{-a + b}{1 + 1} = -1,\\  \frac{\frac{1}{2}a + b}{\left(\frac{1}{2}\right)^2 + 1} = \frac{4}{5}, \end{array} \right.$ 解得 $\left\{ \begin{array}{l} a = 2,\\ b = 0, \end{array} \right.$ 故 $f(x) = \frac{2x}{x^2 + 1}$ （2）【证明】任取 $x_{1},x_{2}\in (-1,1)$ ，且 $x_{1} <   x_{2}$ 则 $f(x_{1}) - f(x_{2}) = \frac{2x_{1}}{x_{1}^{2} + 1} -\frac{2x_{2}}{x_{2}^{2} + 1}$ $= \frac{2x_1x_2^2 + 2x_1 - 2x_2x_1^2 - 2x_2}{(x_1^2 + 1)(x_2^2 + 1)}$ $= \frac{2x_1x_2(x_2 - x_1) - 2(x_2 - x_1)}{(x_1^2 + 1)(x_2^2 + 1)}$

$= \frac{2(x_1x_2 - 1)(x_2 - x_1)}{(x_1^2 + 1)(x_2^2 + 1)},$ 因为 $x_{1},x_{2}\in (-1,1),x_{1} <   x_{2}$ ，所以 $x_{1}x_{2} - 1<$ $0,x_{2} - x_{1} > 0,$ 故 $f(x_{1}) - f(x_{2}) = \frac{2(x_{1}x_{2} - 1)(x_{2} - x_{1})}{(x_{1}^{2} + 1)(x_{2}^{2} + 1)} <  0,$ 故 $f(x_{1}) <   f(x_{2})$ ，所以 $f(x)$ 在(-1,1)上单调递增.

规律方法 利用定义判断函数单调性的步骤
(1) 在定义域内任取 $x_{1}<x_{2}$ .
(2) 计算 $f(x_{1})-f(x_{2})$ 并化简整理.
(3) 判断 $f(x_{1})-f(x_{2})$ 的正负.
(4) 得出结论, 若 $f(x_{1})-f(x_{2})<0$ , 则 $f(x)$ 单调递增; 若 $f(x_{1})-f(x_{2})>0$ , 则 $f(x)$ 单调递减.
<!-- answer-source:end -->
