---
question_id: "node-087:question:8:135"
question_number: "8"
context_key: "node-087:刷能力"
question_source: "C:\\Mathematics-Knowledge\\Secondary-School-Mathematics-Knowledge-Map\\测试\\新建文件夹\\graph\\05-第五章_三角函数\\5.7_三角函数的应用\\5.7_三角函数的应用.md"
question_body_sha256: c51cfefa0914beca13aa59d933c5e385a4f0c919a25279fd94b6b6233ad6116f
answer_status: matched
---

# Question 8

<!-- question-source:start -->
8.[安徽名校联盟2024高一开学考试]近年来,我国逐渐用风能等清洁能源替代传统能源,目前利用风能发电的主要手段是风车发电.如图,风车由一座塔和三个叶片组成,每两个叶片之间的夹角均为 $\frac{2\pi}{3}$ ,现有一个风车,塔高100米,叶片长40米.叶片按照逆时针方向匀速转动,并且每5秒旋转一圈,风车开始旋转时某叶片的一个端点 P 在风车的最低点(此时 P 离地面 60 米). 设点 P 转动 t(秒) 后离地面的距离为 S(米), 则 S 关于 t 的函数关系式为 $S(t) = A \sin(\omega t + \varphi) + B (A > 0, \omega > 0, |\varphi| < \pi)$ .

(1) 求 $S(t)$ 的解析式;

(2)求叶片旋转一圈内点 P 离地面的高度不低于 80 米的时长.

![](../../../../images/questions/part-002/6b3534cf8a1745e19394b6b94c5c5590db7193e14dee0cfe4bb5ffb7d72bd61e.jpg)
<!-- question-source:end -->

## 答案与解析

<!-- answer-source:start -->
8.【解】(1)以风车塔底为坐标原点建立如图所示平面直角坐标系，
当 t=0 时，风车开始旋转时某叶片的一个端点 P 在风车的最低点，设为 $P_{0}$ ，则 $P_{0}(0,60)$ ，
由题意得 $\omega=\frac{2\pi}{5}$ ,
且 $\left\{\begin{aligned}&A+B=100+40,\\ &-A+B=100-40,\\ &S(0)=A\sin\varphi+B=60,\end{aligned}\right.$ 解得 $\left\{\begin{aligned}A&=40,\\ B&=100,\\ \varphi&=-\frac{\pi}{2},\end{aligned}\right.$ 所以 $S(t)=40\sin\left(\frac{2\pi}{5}t-\frac{\pi}{2}\right)+100,t\in[0,+\infty)$ .
(2)令 $S(t)\geqslant80$ ,
则 $S(t)=40\sin\left(\frac{2\pi}{5}t-\frac{\pi}{2}\right)+100\geqslant80$ ,
即 $\cos\frac{2\pi}{5}t\leqslant\frac{1}{2}$ ,
所以 $2k\pi+\frac{\pi}{3}\leqslant\frac{2\pi}{5}t\leqslant2k\pi+\frac{5\pi}{3}(k\in\mathbf{Z})$ ,
解得 $\frac{5}{6}+5k\leqslant t\leqslant\frac{25}{6}+5k(k\in\mathbf{Z})$ .
当 k=0 时， $\frac{5}{6}\leqslant t\leqslant\frac{25}{6},\frac{25}{6}-\frac{5}{6}=\frac{10}{3}$ 所以叶片旋转一圈内点 P 离地面的高度不低于80米的时长为 $\frac{10}{3}$ 秒.
<!-- answer-source:end -->
