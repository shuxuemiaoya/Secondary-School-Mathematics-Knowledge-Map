---
question_id: "node-080:question:8:29"
question_number: "8"
context_key: "node-080:刷提升"
question_source: "C:\\Mathematics-Knowledge\\Secondary-School-Mathematics-Knowledge-Map\\测试\\新建文件夹\\graph\\05-第五章_三角函数\\课时2_二倍角的正弦_余弦_正切公式\\课时2_二倍角的正弦_余弦_正切公式.md"
question_body_sha256: fa888ead5a532adefa10ee9325c6156f645cc6b12d17a6287723c487d091b0b5
answer_status: matched
---

# Question 8

<!-- question-source:start -->
8. 已知函数 $f(x)=\sin\pi\omega x-\sqrt{3}\cos\pi\omega x(\omega>0)$ 在 [0,1] 内恰有 3 个最值点和 4 个零点，则实数 $\omega$ 的取值范围是
A. $\left(\frac{10}{3},\frac{23}{6}\right]$ B. $\left[\frac{10}{3},\frac{23}{6}\right)$ C. $\left[\frac{17}{6},\frac{13}{3}\right)$ D. $\left(\frac{17}{6},\frac{23}{6}\right)$
<!-- question-source:end -->

## 答案与解析

<!-- answer-source:start -->
8. $\left[\frac{1}{2}, 1\right] = \left[\frac{1}{2^{k-1}}, 1\right] (k \in \mathbb{N}^*)$ 【解析】当 $x = 2$ 时, $f(\alpha) = \sin^2\alpha + \cos^2\alpha = 1$ . 当 $x = 4$ 时, $f(\alpha) = \sin^4\alpha + \cos^4\alpha = (\sin^2\alpha + \cos^2\alpha)^2 - 2\sin^2\alpha \cos^2\alpha = 1 - \frac{1}{2}\sin^2 2\alpha = \frac{3}{4} + \frac{1}{4}\cos 4\alpha$ , 因为 $-1 \leqslant \cos 4\alpha \leqslant 1$ , 所以 $\frac{1}{2} \leqslant \frac{3}{4} + \frac{1}{4}\cos 4\alpha \leqslant 1$ , 所以当 $x = 4$ 时, $f(\alpha) \in \left[\frac{1}{2}, 1\right]$ . 当 $x = 6$ 时, $f(\alpha) = \sin^6\alpha + \cos^6\alpha = (\sin^2\alpha + \cos^2\alpha) (\sin^4\alpha - \sin^2\alpha \cos^2\alpha + \cos^4\alpha) = (\sin^2\alpha + \cos^2\alpha) [(\sin^2\alpha + \cos^2\alpha)^2 - 3\sin^2\alpha \cos^2\alpha] = 1 - 3\sin^2\alpha \cos^2\alpha = 1 - \frac{3}{4}\sin^2 2\alpha = \frac{5}{8} + \frac{3}{8}\cos 4\alpha,$ 因为 $-1 \leqslant \cos 4\alpha \leqslant 1$ , 所以 $\frac{1}{4} \leqslant \frac{5}{8} + \frac{3}{8}\cos 4\alpha \leqslant 1$ , 所以当 $x = 6$ 时, $f(\alpha) \in \left[\frac{1}{4}, 1\right]$ . 由以上规律可以猜想: 当 $x = 2k (k \in \mathbb{N}^*)$ 时, $f(\alpha)$ 的取值范围是 $\left[\frac{1}{2^{k-1}}, 1\right] (k \in \mathbb{N}^*)$ .
<!-- answer-source:end -->
