---
question_id: "node-055:question:8:58"
question_number: "8"
context_key: "node-055"
question_source: "C:\\Mathematics-Knowledge\\Secondary-School-Mathematics-Knowledge-Map\\测试\\新建文件夹\\graph\\04-第四章_指数函数与对数函数\\4.5.2_用二分法求方程的近似解\\4.5.2_用二分法求方程的近似解.md"
question_body_sha256: fbda9145fd548f0345cfe03c011579ad2cf8516119f34ef10094de978c8f6075
answer_status: matched
---

# Question 8

<!-- question-source:start -->
8. 已知函数 $f(x) = \frac{1}{3} x^3 - x^2 + 1$ .

(1) 证明方程 $f(x) = 0$ 在区间 (0,2) 内有实数解；

(2) 使用二分法, 取区间的中点三次, 指出方程 $f(x)=0 (x \in [0,2])$ 的实数解 $x_{0}$ 在哪个较小的区间内.

视频微课

错题本
<!-- question-source:end -->

## 答案与解析

<!-- answer-source:start -->
8.(1)【证明】因为函数 $f(x)$ 在定义域上连续,且 $f(0)=1>0,f(2)=-\frac{1}{3}<0$ ,所以 $f(0)\cdot f(2)<0$ ,由函数零点存在定理可得
→ 敬 黑板: 证明方程在一个区间内有实根,只需证明在区间端点处取值的乘积小于0方程 $f(x)=0$ 在区间 $(0,2)$ 内有实数解.
(2)【解】取 $x_{1}=\frac{1}{2}\times(0+2)=1$ , 得 $f(1)=\frac{1}{3}>0$ , 由此可得 $f(1)\cdot f(2)<0$ , 下一个有解区间为 $(1,2)$ .
再取 $x_{2}=\frac{1}{2}\times(1+2)=\frac{3}{2}$ ,
得 $f\left(\frac{3}{2}\right)=-\frac{1}{8}<0$ , 所以 $f(1)\cdot f\left(\frac{3}{2}\right)<0$ , 下一个有解区间为 $\left(1,\frac{3}{2}\right)$ .
再取 $x_{3}=\frac{1}{2}\times\left(1+\frac{3}{2}\right)=\frac{5}{4}$ ，得 $f\left(\frac{5}{4}\right)=\frac{17}{192}>0$ ，所以 $f\left(\frac{5}{4}\right)\cdot f\left(\frac{3}{2}\right)<0$ ，下一个有解区间为 $\left(\frac{5}{4},\frac{3}{2}\right)$ .
综上所述，所求的实数解 $x_{0}$ 在区间 $\left(\frac{5}{4},\frac{3}{2}\right)$ 内.
<!-- answer-source:end -->
