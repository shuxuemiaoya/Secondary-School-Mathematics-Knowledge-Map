---
question_id: "node-015:question:1:58"
question_number: "1"
context_key: "node-015:刷原创"
question_source: "C:\\Mathematics-Knowledge\\Secondary-School-Mathematics-Knowledge-Map\\测试\\新建文件夹\\graph\\01-第一章_集合与常用逻辑用语\\第一章高考强化\\第一章高考强化.md"
question_body_sha256: ec43af70a23efc9c1b189cb29603ee3f980b02eaeb8c2d21404c062a77593282
answer_status: matched
---

# Question 1

<!-- question-source:start -->
1. (多选)任取集合 $A = \{x \in \mathbb{N} \mid 1 \leqslant x \leqslant n, n \in \mathbb{N}, n \geqslant 2\}$ 的 $n$ 个非空子集 $A_{1}, A_{2}, \cdots, A_{n}$ , 定义 $a_{ij}(i, j \in A)$ 为 $a_{ij} = \begin{cases} 0, & A_{i} \cap A_{j} = \varnothing, \\ 1, & A_{i} \cap A_{j} \neq \varnothing, \end{cases}$ 记所得 $a_{ij}$ 的 $n^{2}$ 个值之和为 $S$ , 则 ( )
A. $S$ 与 $n$ 的奇偶性相同
B. $S$ 是 $n$ 的一个倍数
C. $S$ 的最小值为 $n$ D. $S$ 的最大值为 $n^{2}$
<!-- question-source:end -->

## 答案与解析

<!-- answer-source:start -->
1. ACD 【解析】由定义知, 当 $i = j$ 时, $A_i \cap A_j = A_i$ , 则 $a_{ii} = 1 (i = 1, 2, \cdots, n)$ , 故 $S \geqslant n$ . 显然取 $A$ 的单元素子集 $A_i = \{i\}, A_j = \{j\}$ , 则 $i \neq j$ 时, $a_{ij} = 0$ , 所以 $S_{\min} = n$ . 考虑 $S = n$ 的情况下, 若改变集合 $A_k, A_m (1 \leqslant k, m \leqslant n, k \neq m)$ 中的一个, 使 $A_k \cap A_m \neq \emptyset$ , 则 $a_{km} = a_{mk} = 1$ , 如取 $A_1 = \{1, 2\}, A_k = \{k\} (k \in \mathbf{N}, 2 \leqslant k \leqslant n)$ , 则 $S = n + 2$ , 即 $S$ 的值由 $n$ 增

- 敲黑板: $a_{12} = 1 (A_1 \cap A_2 = \{2\}), a_{21} = 1$ , 而原来 $a_{12} = a_{21} = 0$ , 这样就增加了 2

大为 $n + 2$ , 因此, $A_1, A_2, \cdots, A_n$ 中每增加一对集合的交集非空, 则 $S$ 的值增加 2, 故 $S$ 与 $n$ - 点悟: $S = n + 2t (t \in \mathbf{N})$ 具有相同的奇偶性, 但 $S$ 不一定是 $n$ 的倍数. 又由定义可知, $S \leqslant n^2$ . 若对任意的 $i$ , $j \in A, A_i \cap A_j \neq \emptyset$ , 如取 $A_i = \{1, 2, \cdots, i\} (i = 1, 2, \cdots, n), a_{ij} = 1 (i, j = 1, 2, \cdots, n)$ , 则 $S = n^2$ , 即 $S_{\max} = n^2$ . 故选 ACD.
<!-- answer-source:end -->
