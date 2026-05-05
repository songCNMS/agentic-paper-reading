# Task Knowledge

<!-- METADATA:SESSION=2 -->

## 编写规则

- 记录与本任务直接相关、可复用的知识。
- 避免粘贴大段论文原文；优先保留判断、风险和可执行建议。

## 知识条目

- Search scaffold 的关键改进方向应从单纯 answer generation 转向 trajectory、evidence、memory、termination、budget 和 rollout logging 的全链路可观测。
- 对 search agent 最有价值的论文信号不是单篇 SOTA 结果，而是多篇论文反复出现的失败模式：上下文噪声、稀疏奖励、过早停止、证据覆盖不足、live web 不可复现、外部工具长尾延迟。
