---
question_id: "node-087:question:7:67"
question_number: "7"
context_key: "node-087"
question_source: "C:\\Mathematics-Knowledge\\Secondary-School-Mathematics-Knowledge-Map\\测试\\新建文件夹\\graph\\05-第五章_三角函数\\5.7_三角函数的应用\\5.7_三角函数的应用.md"
question_body_sha256: e80ce881143ef83500103e869b6027c11b8392c466c7832da7e187a6e5a21b8b
answer_status: matched
---

# Question 7

<!-- question-source:start -->
7. 一个大风车的半径为 8 米, 风车按逆时针方向匀速旋转, 并且每 12 分钟旋转一周, 它的最低点离地面 2 米. 设风车开始旋转时其翼片的一个端点 P 在风车的最低点, 求:
(1) 点 P 离地面距离 h (米) 与时间 t (分) 之间的函数关系式.
(2) 在第一圈的什么时间段, 点 P 离地面的高度超过 14 米?

![](../../../../../images/questions/part-002/4f84dc5de688ba824ae41ae5ab0d76b309cad9a1ed7e95e4c388dce57e88a149.jpg)
<!-- question-source:end -->

## 答案与解析

<!-- answer-source:start -->
7.【解】(1)不妨设 $h(t) = A\sin (\omega t + \varphi) + b, A > 0, \omega > 0$ ，由题意得 $\left\{ \begin{array}{l} A + b = 18, \\ -A + b = 2, \end{array} \right.$ 解得 $A = 8, b = 10$ ，又 $T = 12$ ，则 $\omega = \frac{2\pi}{T} = \frac{\pi}{6}$ .

当 $t = 0$ 时， $h(0) = 2$ ，即 $\sin \varphi = -1$ ，取 $\varphi = -\frac{\pi}{2}$ .

因此 $h(t) = 8\sin \left(\frac{\pi}{6} t - \frac{\pi}{2}\right) + 10, t \geqslant 0$ .

(2)由题意令 $h(t) > 14$ ，即 $8\sin \left(\frac{\pi}{6} t - \frac{\pi}{2}\right) + 10 > 14$ ，则 $\cos \frac{\pi}{6} t < -\frac{1}{2}$ .

又因为 $0 \leqslant t \leqslant 12$ ，所以 $4 < t < 8$ .

所以在第一圈的4分钟到8分钟内，点 $P$ 离地面的高度超过14米.

归纳总结 解三角函数应用问题的一般
步骤
第一步,阅读理解,审清题意.
读题要做到逐字逐句,读懂题中的文字叙述,理解叙述所反映的实际背景,在此基础上,分析出已知什么,求什么,从中提炼出相应的数学问题.
第二步,搜集整理数据,建立数学模型.
根据搜集到的数据,找出变化规律,运用已掌握的三角函数知识、物理知识及其他相关知识建立关系式,在此基础上将实际问题转化为三角函数问题,从而将实际问题数学化,即建立三角函数模型.
第三步,利用所学的三角函数知识对得到的三角函数模型予以解答,求得结果.
第四步,将所得结论转译成实际问题的答案.
<!-- answer-source:end -->
