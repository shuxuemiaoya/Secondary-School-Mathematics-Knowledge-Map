---
question_id: "node-003:question:5:23"
question_number: "5"
context_key: "node-003"
question_source: "C:\\Mathematics-Knowledge\\Secondary-School-Mathematics-Knowledge-Map\\测试\\新建文件夹\\graph\\01-第一章_集合与常用逻辑用语\\1.2_集合间的基本关系\\1.2_集合间的基本关系.md"
question_body_sha256: c96b30b6a6fb85768f5d02202463c48d54970aaf4928424bd60fd173a76e639b
answer_status: matched
---

# Question 5

<!-- question-source:start -->
5. 教材变式已知集合 $A = \{x \mid -2 \leqslant x \leqslant 5\}$ , $B = \{x \mid m + 1 \leqslant x \leqslant 2m - 1\}$ . 若 $B \subseteq A$ , 则实数 $m$ 的取值范围为 ( )
A. $\{m \mid -3 \leqslant m \leqslant 3\}$ B. $\{m \mid 2 \leqslant m \leqslant 3\}$ C. $\{m \mid m \leqslant 3\}$ D. $\{m \mid m \geqslant 2\}$
<!-- question-source:end -->

## 答案与解析

<!-- answer-source:start -->
5.C 【解析】当 $B = \emptyset$ 时，满足 $B \subseteq A$ ，此时 $m + 1 > 2m - 1$ ，解得 $m < 2$ ；当 $B \neq \emptyset$ 时，由 $B \subseteq A$ 得 $\left\{ \begin{array}{l} m + 1 \leqslant 2m - 1, \\ -2 \leqslant m + 1, \\ 2m - 1 \leqslant 5, \end{array} \right.$ 解得 $2 \leqslant m \leqslant 3$ 。综上所述，实数 $m$ 的取值范围为 $\{m \mid m \leqslant 3\}$ 。故选 C. 链接教材 本题由教材 P9 第 5 题衍变而来，解此题需注意根据题中给出的包含关系分别讨论 $B = \emptyset$ 和 $B \neq \emptyset$ 的情况。

知 $n - 1, n + 1$ 的奇偶性相同，又 $n^2 - 1$ 为120的倍数，所以 $n - 1, n + 1$ 均为偶数，由 $120 = 2^3 \times 3 \times 5$ ，可知 $n - 1, n + 1$ 中必有一个为10的倍数，结合带余除法可知：从10开始10的倍数除以3的余数依次为1,2,0,1,2,0,…，①若10的倍数除以3的余数为1，则其加2为3的倍数，可知 $n - 1$ 为10的倍数， $n + 1$ 为3的倍数，此时 $n$ 的值是唯一的；②若10的倍数除以3的余数为2，则其减2为3的倍数，可知 $n + 1$ 为10的倍数， $n - 1$ 为3的倍数，此时 $n$ 的值是唯一的；③若10的倍数除以3的余数为0（即为30的倍数），符合题意，可知 $n - 1, n + 1$ 均可为10的倍数，此时 $n$ 的值有2个；且 $1 \leqslant n \leqslant 150$ ，即 $2 \leqslant n + 1 \leqslant 151, 0 \leqslant n - 1 \leqslant 149$ ，在1到151中，可知10的倍数有15个，30的倍数有5个，考虑到150的唯一性，所以 $S$ 的元素个数为 $(15 - 5) \times 1 + (5 - 1) \times 2 + 1 = 19.$ 特别注意为了方便，在研究因数和倍数的时候，我们所指的数是自然数（一般不包括0）.
<!-- answer-source:end -->
