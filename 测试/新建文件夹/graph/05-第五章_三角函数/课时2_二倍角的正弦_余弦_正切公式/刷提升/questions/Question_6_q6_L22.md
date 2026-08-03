---
question_id: "node-080:question:6:22"
question_number: "6"
context_key: "node-080:刷提升"
question_source: "C:\\Mathematics-Knowledge\\Secondary-School-Mathematics-Knowledge-Map\\测试\\新建文件夹\\graph\\05-第五章_三角函数\\课时2_二倍角的正弦_余弦_正切公式\\课时2_二倍角的正弦_余弦_正切公式.md"
question_body_sha256: d28f66d6c924635274f87d3549d056098885ed3e0a2606438e14f6ebc67da949
answer_status: matched
---

# Question 6

<!-- question-source:start -->
6. 已知函数 $f(x)=\sin x+\sqrt{3}\cos x$ ，当 $x=\alpha$ 时，函数 $f(x)$ 取得最大值，则 $\sin\left(\alpha-\frac{\pi}{4}\right)=$ （）
A. $\frac{\sqrt{2}+\sqrt{6}}{4}$ B. $\frac{\sqrt{2}-\sqrt{6}}{4}$ C. $\frac{\sqrt{6}-\sqrt{2}}{4}$ D. $-\frac{\sqrt{2}+\sqrt{6}}{4}$
<!-- question-source:end -->

## 答案与解析

<!-- answer-source:start -->
6. ABD 【解析】显然 $f(-x)=|\sin(-x)|\cdot\cos(-x)=|\sin x|\cos x=f(x)$ ，即函数 $f(x)$ 是偶函数，又 $f(x+2\pi)=|\sin(x+2\pi)|\cdot\cos(x+2\pi)=|\sin x|\cos x=f(x)$ ，所以函数 $f(x)$ 是周期函数， $2\pi$ 是它的一个周期，B 正确.
当 $0 \leqslant x \leqslant \pi$ 时， $0 \leqslant 2x \leqslant 2\pi, f(x) = \sin x \cdot \cos x = \frac{1}{2} \sin 2x$ 的最小值为 $-\frac{1}{2}$ ，最大值为 $\frac{1}{2}$ ，即当 $0 \leqslant x \leqslant \pi$ 时， $f(x)$ 的取值范围是 $\left[-\frac{1}{2}, \frac{1}{2}\right]$ ，因为 $f(x)$ 是偶函数，所以当 $-\pi \leqslant x \leqslant 0$ 时， $f(x)$ 的取值范围也是 $\left[-\frac{1}{2}, \frac{1}{2}\right]$ ，因此当 $-\pi \leqslant x \leqslant \pi$ 时， $f(x)$ 的取值范围是 $\left[-\frac{1}{2}, \frac{1}{2}\right]$ ，而 $2\pi$ 是 $f(x)$ 的一个周期，所以 $x \in R, f(x)$ 的值域为 $\left[-\frac{1}{2}, \frac{1}{2}\right]$ ，A 正确.

因为 $f\left(\frac{\pi}{4}\right) = \frac{1}{2}, f\left(\frac{5\pi}{4}\right) = -\frac{1}{2}$ , 即函数 $f(x)$ 图象上的点 $\left(\frac{\pi}{4}, \frac{1}{2}\right)$ 关于直线 $x = \frac{3\pi}{4}$ 的对称点 $\left(\frac{5\pi}{4}, \frac{1}{2}\right)$ 不在此函数图象上, C 不正确. 当 $x > 2$ 时, 恒有 $\log_4 x > \frac{1}{2}$ 成立, 而 $f(x)$ 的值域为 $\left[-\frac{1}{2}, \frac{1}{2}\right]$ , 方程 $f(x) = \log_4 x$ 在 $(2, +\infty)$ 上无实数根, 又当 $0 < x < 1$ 或 $\frac{\pi}{2} < x < 2$ 时, $f(x)$ 的值与 $\log_4 x$ 的值异号, 即方程 $f(x) = \log_4 x$ 在 $(0, 1), \left(\frac{\pi}{2}, 2\right)$ 上都无实数根. 令 $g(x) = f(x) - \log_4 x = \frac{1}{2} \sin 2x - \log_4 x, x \in \left[1, \frac{\pi}{2}\right]$ , 显然 $g(x)$ 在 $\left[1, \frac{\pi}{2}\right]$ 上单调递减, 而 $g(1) = \frac{1}{2} \sin 2 > 0, g\left(\frac{\pi}{2}\right) = -\log_4 \frac{\pi}{2} < 0$ , 于是存在唯一 $x_0 \in \left(1, \frac{\pi}{2}\right)$ , 使得 $g(x_0) = 0$ , 因此方程

点悟：零点存在定理的应用 $f(x)=\log_{4}x$ 在 $\left[1,\frac{\pi}{2}\right]$ 上有唯一实根，则方程 $f(x)=\log_{4}x$ 在 $(0,+\infty)$ 上有唯一实根，又 $y=\log_{4}x$ 的定义域为 $(0,+\infty)$ ，所以方程 $f(x)=\log_{4}x$ 有且仅有一个实数根，D 正确。故选 ABD.

规律方法 函数 $y=f(x)$ 的定义域为 D， $\forall x \in D$ ，存在常数 a 使得 $f(x) = f(2a - x)$ ，即 $f(a + x) = f(a - x)$ ，则函数 $y = f(x)$ 的图象关于直线 x = a 对称.
<!-- answer-source:end -->
