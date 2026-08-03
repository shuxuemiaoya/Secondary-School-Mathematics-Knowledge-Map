---
question_id: "node-056:question:2:12"
question_number: "2"
context_key: "node-056"
question_source: "C:\\Mathematics-Knowledge\\Secondary-School-Mathematics-Knowledge-Map\\测试\\新建文件夹\\graph\\04-第四章_指数函数与对数函数\\4.5.3_函数模型的应用\\4.5.3_函数模型的应用.md"
question_body_sha256: 8cc9ac11c2a78f860b42af09341f9973f898007e4c17ef134a69a85d98d2137e
answer_status: matched
---

# Question 2

<!-- question-source:start -->
2.[重庆一中2024高一期中]宇宙之大,粒子之微,无处不用到数学.2023年诺贝尔物理学奖颁给了“阿秒光脉冲”,光速约为 $3\times10^{8}$ m/s,1阿秒等于 $10^{-18}$ s.现有一条50cm的线段,第一次截去总长的一半,以后每次截去剩余长度的一半,若要使其长度小于光在1阿秒内走的距离,则需要截(参考数据:lg5≈0.70,lg3≈0.48)
() A.30次 B.31次 C.32次 D.33次
<!-- question-source:end -->

## 答案与解析

<!-- answer-source:start -->
2.B【解析】根据已知可得,光在1阿秒内走的距离为 $10^{-18}\times3\times10^{8}=3\times10^{-10}$ m.
设截 x 次后,剩余的长度为 $f(x)$ (单位: m), 则 $f(x)=0.5\times\left(\frac{1}{2}\right)^{x}=\left(\frac{1}{2}\right)^{x+1}$ .
令 $f(x)<3\times10^{-10}$ ，可得 $\left(\frac{1}{2}\right)^{x+1}<3\times10^{-10}$ 点悟：解与指数相关的不等式时，两边同时取对数后再计算结合函数 $y=\left(\frac{1}{2}\right)^{x}$ 的单调性，两边同时取对数可得 $x + 1 > \log_{\frac{1}{2}}(3 \times 10^{-10}) = \frac{\lg(3 \times 10^{-10})}{\lg\frac{1}{2}} = \frac{-10 + \lg 3}{-\lg 2} = \frac{-10 + \lg 3}{\lg 5 - 1} \approx \frac{-10 + 0.48}{0.70 - 1} \approx 31.73,$ 所以 x > 30.73 > 30. 所以应当截 31 次. 故选 B.
<!-- answer-source:end -->
