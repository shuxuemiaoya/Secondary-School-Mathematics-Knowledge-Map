---
question_id: "node-006:question:10:55"
question_number: "10"
context_key: "node-006"
question_source: "C:\\Mathematics-Knowledge\\Secondary-School-Mathematics-Knowledge-Map\\测试\\新建文件夹\\graph\\01-第一章_集合与常用逻辑用语\\专题1_集合的综合问题\\专题1_集合的综合问题.md"
question_body_sha256: 549d4e172f37a25506b21216757b14433d86e8d2e747ec54f87496b44de711bf
answer_status: matched
---

# Question 10

<!-- question-source:start -->
10. 已知集合 $A, B, A \subseteq \mathbf{Z}, B \subseteq \mathbf{Z}, A, B$ 中都至少有 3 个元素, 且 $A, B$ 满足:
① $\forall x, y \in A$ , 且 $x \neq y$ , 总有 $|x + y| \in B$ ;
② $\forall x, y \in B$ , 且 $x \neq y$ , 总有 $|x - y| \in A$ .
(1) 若集合 $B = \{1, 2, 3\}$ , 直接写出所有满足条件的集合 $A$ .
(2) 已知 $-1 \in A$ ,
(i) 若 $x, y \in A$ , 且 $y > x > 0$ , 求证: $y - x \in A$ .
(ii) 求证: $\mathbf{N}^{*} \subseteq A$ .
<!-- question-source:end -->

## 答案与解析

<!-- answer-source:start -->
10. (1)【解】因为 $B = \{1,2,3\}$ , 又 $\forall x, y \in B$ , 且 $x \neq y$ , 总有 $|x - y| \in A$ , 所以 $3 - 1 \in A, 3 - 2 \in A$ , 即 $1 \in A, 2 \in A$ . 设 $t \in A, t \neq 1, t \neq 2$ , 由 $\forall x, y \in A$ , 且 $x \neq y$ , 总有 $|x + y| \in B$ , 可得 $|t + 1| \in B$ , 且 $|t + 2| \in B$ , 所以 $t = 0$ 或 $t = -3$ 或 $t = -4$ , 但 $|-3 + (-4)| \notin B, |-4 + 0| \notin B$ , 所以满足条件的集合 $A$ 有 $\{0,1,2\}$ , $\{-3,1,2\}, \{-3,0,1,2\}, \{-4,1,2\}$ . (2)【证明】(i)已知 $-1 \in A, x, y \in A, y > x > 0, A \subseteq \mathbf{Z}$ , 由①知, $|y + (-1)| = y - 1 \in B, |x + (-1)| = x - 1 \in B$ , 由②知, $|y - 1 - (x - 1)| = y - x \in A$ .
<!-- answer-source:end -->
