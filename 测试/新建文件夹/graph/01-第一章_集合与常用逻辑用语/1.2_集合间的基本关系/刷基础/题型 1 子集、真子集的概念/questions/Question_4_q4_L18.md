---
question_id: "node-003:question:4:18"
question_number: "4"
context_key: "node-003"
question_source: "C:\\Mathematics-Knowledge\\Secondary-School-Mathematics-Knowledge-Map\\测试\\新建文件夹\\graph\\01-第一章_集合与常用逻辑用语\\1.2_集合间的基本关系\\1.2_集合间的基本关系.md"
question_body_sha256: df5cc1b528be50a4a9f183e511561cc1a47476200aa49d7e31c7b4f82beca246
answer_status: matched
---

# Question 4

<!-- question-source:start -->
4. 已知集合 $A = \{x \mid x^2 - 7x + 10 = 0, x \in \mathbf{R}\}$ , $B = \{x \mid 1 < x < 6, x \in \mathbf{N}\}$ , 则满足条件 $A \subseteq C \subsetneq B$ 的集合 $C$ 的个数为 ( )
A. 1    B. 2    C. 3    D. 4
<!-- question-source:end -->

## 答案与解析

<!-- answer-source:start -->
4. C 【解析】由题得 $A=\{2,5\}$ , $B=\{2,3,4,5\}$ . 因为 $A \subseteq C \not\subseteq B$ , 所以根据子集和真子集的定义, 集合 C 必须含有元素 2,5,所以 $C=\{2,5\}$ 或 $\{2,5,3\}$ 或 $\{2,5,4\}$ . 故选 C.
多种解法 由题易知 A 中有 2 个元素, B 中有 4 个元素, 且 $A \subseteq C \not\subseteq B$ , 则集合 C 有 $2^{4-2}-1=3$ (个).

二级结论 若集合 A 中有 m 个元素, 集合 B 中有 n 个元素, 且 0 < m < n.
当 $A \subseteq C \subseteq B$ 时, 集合C有 $2^{n-m}$ 个;
当 $A \subseteq C \subsetneq B$ 时, 集合C有 $(2^{n-m}-1)$ 个;
当 $A \subsetneq C \subsetneq B$ 时, 集合C有 $(2^{n-m}-1)$ 个;
当 $A \subsetneq C \subsetneq B$ 时, 集合C有 $(2^{n-m}-2)$ 个.
<!-- answer-source:end -->
