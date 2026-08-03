---
question_id: "node-031:question:9:127"
question_number: "9"
context_key: "node-031:刷素养"
question_source: "C:\\Mathematics-Knowledge\\Secondary-School-Mathematics-Knowledge-Map\\测试\\新建文件夹\\graph\\03-第三章_函数的概念与性质\\课时2_函数的最大(小)值\\课时2_函数的最大(小)值.md"
question_body_sha256: f7955bbbdc8f0efaf243362c554dcb2e41eff8759c1dbc629184da8f3bba2fd5
answer_status: matched
---

# Question 9

<!-- question-source:start -->
9.[北京大学2022强基计划]已知 $f(x)$ 是二次函数, $f(-2)=0$ ,且 $2x\leqslant f(x)\leqslant\frac{x^{2}+4}{2}$ ,则 $f(10)=$ \_\_\_\_.
<!-- question-source:end -->

## 答案与解析

<!-- answer-source:start -->
9.36 【解析】由 $f(-2)=0$ ，可设 $f(x)=(x+2)(ax+b)=ax^{2}+(2a+b)x+2b(a\neq0)$ ，则由 $f(x)\geqslant2x$ 得 $ax^{2}+(2a+b-2)x+2b\geqslant0$ ，所以a>0，且 $(2a+b-2)^{2}\leqslant8ab$ ，整理后即为 $4a^{2}+b^{2}\leqslant4ab+8a+4b-4$ 。
由 $f(x)\leqslant\frac{x^{2}+4}{2}$ 得 $(2a-1)x^{2}+(4a+2b)x+4b-4\leqslant0$ .
若2a-1=0，则必有4a+2b=0，此时与 $(2a+b-2)^{2}\leqslant8ab$ 矛盾，
所以2a-1<0且 $(4a+2b)^{2}\leqslant4(2a-1)\cdot(4b-4)$ ,
整理后为 $4a^{2}+b^{2}\leqslant4ab-8a-4b+4$ ,
与 $4a^{2}+b^{2}\leqslant4ab+8a+4b-4$ 相加即得 $4a^{2}+b^{2}\leqslant4ab$ ,
即 $(2a-b)^{2}\leqslant0$ ，所以2a=b，所以 $f(x)=(x+2)(ax+2a)=a(x+2)^{2}$ .
又由于在原不等式中令x=2可得 $4\leqslant f(2)\leqslant4$ 所以 $f(2)=4$ ，由此解得 $a=\frac{1}{4}$ .
所以 $f(x)=\frac{1}{4}(x+2)^{2}$ ，所以 $f(10)=36$
<!-- answer-source:end -->
