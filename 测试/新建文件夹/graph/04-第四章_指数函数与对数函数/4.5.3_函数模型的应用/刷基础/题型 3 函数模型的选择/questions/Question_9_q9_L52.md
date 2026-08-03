---
question_id: "node-056:question:9:52"
question_number: "9"
context_key: "node-056"
question_source: "C:\\Mathematics-Knowledge\\Secondary-School-Mathematics-Knowledge-Map\\测试\\新建文件夹\\graph\\04-第四章_指数函数与对数函数\\4.5.3_函数模型的应用\\4.5.3_函数模型的应用.md"
question_body_sha256: 1b219af1135666d3ae18bc872175a1e0bb52e92835927ec0befe382c7ef04d2a
answer_status: matched
---

# Question 9

<!-- question-source:start -->
9.[广西南宁2025高一期末]为践行“绿水青山,就是金山银山”的理念,某省决定净化闽江上游水域的水质.省环保局于2023年年底在闽江上游水域投入一些蒲草,这些蒲草在水中的蔓延速度越来越快,2024年2月底测得蒲草覆盖面积为 $36\ m^{2}$ ,2024年3月底测得蒲草覆盖面积为 $48\ m^{2}$ ,蒲草覆盖面积y(单位: $m^{2}$ )与月份x(单位:月)的关系有两个函数模型 $y=ka^{x}$ (k>0,a>1)与 $y=mx^{2}+n(m>0)$ 可供选择.

(1) 分别求出两个函数模型的解析式;

(2) 若 2023 年年底测得蒲草覆盖面积为 $20 \, m^{2}$ ，从上述两个函数模型中选择更合适的一个模型,说明理由,并估算至少到哪一年的几月底蒲草覆盖面积能达到 $810 \, m^{2}$ . (参考数据: $\lg 2 \approx 0.30, \lg 3 \approx 0.48$ )
<!-- question-source:end -->

## 答案与解析

<!-- answer-source:start -->
9.【解】(1)若选择模型 $y=ka^{x}(k>0,a>1)$ ，则 $\left\{\begin{aligned}ka^{2}&=36,\\ ka^{3}&=48,\end{aligned}\right.$ 解得 $a=\frac{4}{3},k=\frac{81}{4}$ ，故函数模型为 $y=\frac{81}{4}\cdot\left(\frac{4}{3}\right)^{x}$ .
若选择模型 $y = mx^{2} + n (m > 0)$ ，则 $\left\{\begin{aligned}4m+n&=36,\\ 9m+n&=48,\end{aligned}\right.$ 解得 $m=\frac{12}{5},n=\frac{132}{5}$ ，故函数模型为 $y=\frac{12}{5}x^{2}+\frac{132}{5}$ .
(2) 把 x=0 代入 $y=\frac{81}{4}\cdot\left(\frac{4}{3}\right)^{x}$ ，可得 $y=\frac{81}{4}=20.25$ ，
把 x=0 代入 $y=\frac{12}{5}x^{2}+\frac{132}{5}$ ，可得 $y=\frac{132}{5}$ ，
可知 $\frac{132}{5}$ 与20相差比较大，
故选择函数模型 $y=\frac{81}{4}\cdot\left(\frac{4}{3}\right)^{x}$ 更合适.
令 $\frac{81}{4}\cdot\left(\frac{4}{3}\right)^{x}\geqslant810$ , 可得 $\left(\frac{4}{3}\right)^{x}\geqslant40$ , 两边取常用对数可得 $x\lg\frac{4}{3}\geqslant\lg40$ ,
即 $x \geqslant \frac{\lg 40}{\lg \frac{4}{3}} = \frac{2\lg 2+1}{2\lg 2-\lg 3} \approx \frac{2 \times 0.3 + 1}{2 \times 0.3 - 0.48} \approx$ 13.33,
故至少到2025年2月底蒲草覆盖面积能达到 $810\ m^{2}$ .
<!-- answer-source:end -->
