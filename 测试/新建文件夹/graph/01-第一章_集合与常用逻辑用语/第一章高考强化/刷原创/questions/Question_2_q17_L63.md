---
question_id: "node-015:question:2:63"
question_number: "2"
context_key: "node-015:刷原创"
question_source: "C:\\Mathematics-Knowledge\\Secondary-School-Mathematics-Knowledge-Map\\测试\\新建文件夹\\graph\\01-第一章_集合与常用逻辑用语\\第一章高考强化\\第一章高考强化.md"
question_body_sha256: 18d5a759e6c3f2f540f9a235da24d46a6476ec357866a91e9f4da9d1f9e6e870
answer_status: matched
---

# Question 2

<!-- question-source:start -->
2. 已知“ $r \equiv m (\bmod p)$ ”表示正整数 m 被质数 p 除的余数为 $r (0 \leqslant r \leqslant p - 1)$ . 已知质数 p 不整除正整数 a, 若 $A = \{1, 2, \cdots, p - 1\}$ , $B = \{x \mid x \equiv an (\bmod p), n \in A\}$ , 则 ( )

做人要学会敬畏，有所为必有所不为。做事要如临深渊，如履薄冰。
<!-- question-source:end -->

## 答案与解析

<!-- answer-source:start -->
2. C 【解析】先证集合 B 有 $(p-1)$ 个元素。假设 B 中不是 $(p-1)$ 个元素，则其中至少有两个数被质数 p 除的余数相同，余数设为 x，则 $x \equiv ai (\bmod p)$ ， $x \equiv aj (\bmod p)$ ， $i, j \in A, i \neq j$ ，则 $ai = pq_{1} + x, aj = pq_{2} + x (q_{1}, q_{2} \in \mathbf{N})$ ，故 $\frac{a(i-j)}{p} = q_{1} - q_{2} \in \mathbf{Z}$ ，由 p 不整除 a 知，i-j 能被 p 整除，又 $1 \leqslant i \leqslant p-1, 1 \leqslant j \leqslant p-1$ ，则必有 i = j，矛盾，故集合 B 中共有 $(p-1)$ 个元素。因为 $0 \notin B$ ，否则 a, n 中必存在一个能被 p 整除，矛盾，故 x = 1, 2, $\cdots, p-1$ ，所以 A = B。由 $x \equiv an (\bmod p)$ ， $n \in A$ 可得， $1 \cdot 2 \cdot \cdots \cdot (p-1)$ 与 $(a \cdot 1) \cdot (a \cdot 2) \cdot \cdots \cdot [a \cdot (p-1)]$ 被 p 除的余数相同，即 $1 \cdot 2 \cdot \cdots \cdot (p-1)$ 与 $a^{p-1} [1 \cdot 2 \cdot \cdots \cdot (p-1)]$ 被 p 除的余数相同，而 $1 \cdot 2 \cdot \cdots \cdot (p-1)$ 被 p 除的余数唯一且不为 0，所以 $1 \equiv a^{p-1} (\bmod p)$ ，即 $a^{p-1}$ 被 p 除余 1。故选 C。
<!-- answer-source:end -->
