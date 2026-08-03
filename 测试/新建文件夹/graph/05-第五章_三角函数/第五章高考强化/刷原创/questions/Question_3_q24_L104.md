---
question_id: "node-089:question:3:104"
question_number: "3"
context_key: "node-089:刷原创"
question_source: "C:\\Mathematics-Knowledge\\Secondary-School-Mathematics-Knowledge-Map\\测试\\新建文件夹\\graph\\05-第五章_三角函数\\第五章高考强化\\第五章高考强化.md"
question_body_sha256: 2a0b7a09fc1741cfc34332107a2c1275f5d2a6dce78a62ef72d1f5531176b9c5
answer_status: matched
---

# Question 3

<!-- question-source:start -->
3. 已知点 O 在半径为 r 的圆 E 上, 直线 $AD \perp OE$ , 且圆心 E 到 AD 的距离为 $m\left(1 < \frac{m}{r} < \frac{3}{2}\right)$ , 如图. 以 O 为顶点, 射线 OE 为始边, 角 $\alpha$ , $\beta\left(-\frac{\pi}{2} < \alpha \leqslant 0, 0 \leqslant \beta < \frac{\pi}{2}\right)$ 的终边与圆 E 分别交于点 B, C, 点 B, C 到直线 AD 的距离与到点 O 的距离相等.

(1) 求 $\cos \alpha + \cos \beta$ 的值;

(2) 求 $\sin \alpha - \sin \beta$ 的取值范围.
<!-- question-source:end -->

## 答案与解析

<!-- answer-source:start -->
3.【解】(1)以点 O 为坐标原点, 以 OE 所在直线为 x 轴建立平面直角坐标系, 如图所示, 则 $B(2r\cos^{2}\alpha, 2r\cos\alpha\sin\alpha)$ , $C(2r\cos^{2}\beta, 2r\cos\beta\sin\beta)$ .
又 $|OB| = |AB|$ , $|OC| = |CD|$ ,
则 $\left\{\begin{aligned}&2r\cos\alpha=2r\cos^{2}\alpha+m-r,\\ &2r\cos\beta=2r\cos^{2}\beta+m-r,\end{aligned}\right.$ 两式相减, 得 $\cos \alpha + \cos \beta = 1$ .

![](../../../../images/answers/part-002/a8e259d5b088108a4ec6b276f5eba928f8e82e7f0030c47b116b856d19a2e285.jpg)

(2) 因为 $(\cos \alpha + \cos \beta)^{2} + (\sin \alpha - \sin \beta)^{2} = 2 + 2(\cos \alpha \cos \beta - \sin \alpha \sin \beta) = 2 + 2\cos (\alpha + \beta)$ ，又 $-\frac{\pi}{2} < \alpha \leqslant 0, 0 \leqslant \beta < \frac{\pi}{2}$ ，所以 $0 < \cos (\alpha + \beta) \leqslant 1$ ，
故 $2<(\cos\alpha+\cos\beta)^{2}+(\sin\alpha-\sin\beta)^{2}\leqslant4,$ 所以 $1<(\sin\alpha-\sin\beta)^{2}\leqslant3$ ，所以 $\sin\alpha-\sin\beta\in[-\sqrt{3},-1)\cup(1,\sqrt{3}]$ .
又由 $-\frac{\pi}{2}<\alpha\leqslant0,0\leqslant\beta<\frac{\pi}{2}$ ，可知 $-1<\sin\alpha\leqslant0,0\leqslant\sin\beta<1$ ，故 $-2<\sin\alpha-\sin\beta\leqslant0$ ，故 $\sin\alpha-\sin\beta$ 的取值范围为 $[- \sqrt{3}, -1)$ .
<!-- answer-source:end -->
