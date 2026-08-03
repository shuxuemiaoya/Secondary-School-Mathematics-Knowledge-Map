---
question_id: "node-089:question:20:79"
question_number: "20"
context_key: "node-089"
question_source: "C:\\Mathematics-Knowledge\\Secondary-School-Mathematics-Knowledge-Map\\测试\\新建文件夹\\graph\\05-第五章_三角函数\\第五章高考强化\\第五章高考强化.md"
question_body_sha256: 9dac0c78497af8139a4fb437cd41c226312a83eae071aca15ef8fd32348d819c
answer_status: matched
---

# Question 20

<!-- question-source:start -->
20. [全国甲理 2021·16,5 分] 已知函数 $f(x)=2\cos(\omega x+\varphi)$ 的部分图象如图所示, 则满足条件 $(f(x)-f\left(-\frac{7\pi}{4}\right))\left(f(x)-f\left(\frac{4\pi}{3}\right)\right)>0$ 的最小正整数 $x$ 为 \_\_\_\_.

![](../../../../../images/questions/part-002/d0e7679d12d35f979153897a8b0388a2c40f8e660538f94d05ff4466e8ede187.jpg)
<!-- question-source:end -->

## 答案与解析

<!-- answer-source:start -->
20.2 【解析】设函数 $f(x)$ 的最小正周期为 T，由图象可知， $\frac{3}{4}T=\frac{13\pi}{12}-\frac{\pi}{3}=\frac{3\pi}{4}$ ，所以 $T=\pi=\frac{2\pi}{|\omega|}$ ，所以 $\omega=\pm2$ 。

避坑：题干中未给出 $\omega>0$ ，不要习惯性认为 $\omega$ 为正值，漏掉 $\omega$ 为负值的情况

当 $\omega=2$ 时，把点 $\left(\frac{13\pi}{12},2\right)$ 的坐标代入 $f(x)$ 的解析式，得 $2\cos\left(\frac{13\pi}{12}\omega+\varphi\right)=2\cos\left(\frac{13\pi}{12}\times2+\varphi\right)=2$ ，所以 $\varphi=2k\pi-\frac{\pi}{6}$ ， $k\in Z$ ，则 $f(x)=2\cos\left(2x+2k\pi-\frac{\pi}{6}\right)=2\cos\left(2x-\frac{\pi}{6}\right)$ ；

当 $\omega=-2$ 时，将点 $\left(\frac{13\pi}{12},2\right)$ 的坐标代入 $f(x)$ 的解析式，得 $2\cos\left(\frac{13\pi}{12}\omega+\varphi\right)=2\cos\left[\frac{13\pi}{12}\times(-2)+\varphi\right]=2\cos\left(\frac{13\pi}{12}\times2-\varphi\right)=2$ ，所以 $\varphi=2k\pi+\frac{\pi}{6}$ ， $k\in Z$ ，则 $f(x)=2\cos(2x-\varphi)=2\cos\left(2x-\frac{\pi}{6}\right)$ 。

综上得 $f(x)=2\cos\left(2x-\frac{\pi}{6}\right)$ ，所以 $f\left(-\frac{7\pi}{4}\right)=2\cos\left[2\times\left(-\frac{7\pi}{4}\right)-\frac{\pi}{6}\right]=1$ ， $f\left(\frac{4\pi}{3}\right)=2\cos\left(2\times\frac{4\pi}{3}-\frac{\pi}{6}\right)=0$ ，

所以 $(f(x)-1)f(x)>0$ ，

所以 $f(x)<0$ 或 $f(x)>1$ ，

所以 $\cos\left(2x-\frac{\pi}{6}\right)<0$ 或 $\cos\left(2x-\frac{\pi}{6}\right)>\frac{1}{2}$ ，所以 $\frac{\pi}{2}+2k\pi<2x-\frac{\pi}{6}<\frac{3\pi}{2}+2k\pi$ 或 $-\frac{\pi}{3}+2k\pi<2x-\frac{\pi}{6}<\frac{\pi}{3}+2k\pi, k\in Z$ ，

即 $\frac{\pi}{3}+k\pi<x<\frac{5\pi}{6}+k\pi$ 或 $-\frac{\pi}{12}+k\pi<x<\frac{\pi}{4}+k\pi, k\in Z$ ，所以当 k=0 时，x 能取到的最小正整数为 2。
<!-- answer-source:end -->
