---
question_id: "node-087:question:7:127"
question_number: "7"
context_key: "node-087:刷能力"
question_source: "C:\\Mathematics-Knowledge\\Secondary-School-Mathematics-Knowledge-Map\\测试\\新建文件夹\\graph\\05-第五章_三角函数\\5.7_三角函数的应用\\5.7_三角函数的应用.md"
question_body_sha256: 26c35ee74c3c69c914f8e9fadb9ee3c9a2c7e60f8228d745e8cc99f8984e738e
answer_status: matched
---

# Question 7

<!-- question-source:start -->
7.[河北石家庄2025高一月考]主动降噪耳机工作的原理是先通过微型麦克风采集周围的噪声,然后降噪芯片生成与噪声振幅相同、相位相反的声波来抵消噪声(如图所示).已知某噪声声波曲线 $f(x)=A\sin\left(\frac{2\pi}{3}x+\varphi\right)$ ( $A>0,0\leqslant\varphi<\pi$ ),其振幅为2,且经过点(1,-2).

(1) 求该噪声声波曲线 $f(x)$ 的解析式以及降噪芯片生成的降噪声波曲线 $g(x)$ 的解析式；

(2) 证明: $g(x) + g(x + 1) + g(x + 2)$ 为定值.

![](../../../../images/questions/part-002/9060b65edbcdea1423d50e47f3c607fb45693f00fe5dd069d44e793e16feb288.jpg)
<!-- question-source:end -->

## 答案与解析

<!-- answer-source:start -->
7.（1）【解】由振幅为2，A>0，可得A=2， $f(x)=2\sin\left(\frac{2\pi}{3}x+\varphi\right)$ 由噪声声波曲线经过点(1,-2)，得-2= $2\sin\left(\frac{2\pi}{3}+\varphi\right)\Rightarrow\sin\left(\frac{2\pi}{3}+\varphi\right)=-1,$ 而 $0 \leqslant \varphi < \pi, \frac{2\pi}{3} + \varphi \in \left[\frac{2\pi}{3}, \frac{5\pi}{3}\right)$ ,
则 $\frac{2\pi}{3}+\varphi=\frac{3\pi}{2}\Rightarrow\varphi=\frac{5\pi}{6}$ ,
则 $f(x)=2\sin\left(\frac{2\pi}{3}x+\frac{5\pi}{6}\right)$ .
又降噪声波曲线与噪声声波曲线的振幅相同、相位相反，
所以 $g(x)=-2\sin\left(\frac{2\pi}{3}x+\frac{5\pi}{6}\right)$ .
(2)【证明】由(1) $g(x)=-2\sin\left(\frac{2\pi}{3}x+\frac{5\pi}{6}\right)$ $=-2\sin\left(\frac{2\pi}{3}x+\frac{\pi}{3}+\frac{\pi}{2}\right)$ $=-2\cos\left(\frac{2\pi}{3}x+\frac{\pi}{3}\right)$ 则 $g(x)+g(x+1)+g(x+2)$ $=-2\cos\left(\frac{2\pi}{3}x+\frac{\pi}{3}\right)-2\cos\left(\frac{2\pi}{3}x+\pi\right)-2\cos\left(\frac{2\pi}{3}x+\frac{2\pi}{3}+\pi\right)$ $= -2\cos\left(\frac{2\pi}{3}x+\frac{\pi}{3}\right) + 2\cos\frac{2\pi x}{3} + 2\cos\left(\frac{2\pi}{3}x+\frac{2\pi}{3}\right)$

$= -2\left(\cos \frac{2\pi x}{3}\cdot \frac{1}{2} -\sin \frac{2\pi x}{3}\cdot \frac{\sqrt{3}}{2}\right) +$ $2\cos \frac{2\pi x}{3} +2\left[\cos \frac{2\pi x}{3}\cdot \left(-\frac{1}{2}\right) - \sin \frac{2\pi x}{3}\cdot$ $\frac{\sqrt{3}}{2} ]$ $= -\cos \frac{2\pi x}{3} +\sqrt{3}\sin \frac{2\pi x}{3} +2\cos \frac{2\pi x}{3}-$ $\cos \frac{2\pi x}{3} -\sqrt{3}\sin \frac{2\pi x}{3} = 0,$ 即 $g(x) + g(x + 1) + g(x + 2)$ 为定值0.

![](../../../../images/answers/part-002/9dd20732f73e26fd08959630275b555717dbd5116b169557ef727d7a00120bea.jpg)
<!-- answer-source:end -->
