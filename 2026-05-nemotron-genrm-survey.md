# Nemotron 中 GenRM 模型技术 Survey

Checked on: 2026-05-18

说明：用户写作 `Nemontron`，这里按 NVIDIA 官方命名 `Nemotron` 理解。本文聚焦 Nemotron 3 / Nemotron-Cascade 体系中公开提到的 Generative Reward Model，尤其是 `Qwen3-Nemotron-235B-A22B-GenRM` 及其 HelpSteer3 / principle-following 训练路线。

## 一句话结论

Nemotron 的 GenRM 不是传统“最后一层 scalar head”的 Bradley-Terry reward model，而是一个会生成评价推理的 LLM-as-judge：给定对话上下文、用户请求和两个候选回答，先分析两个回答的优缺点，再输出每个回答的 helpfulness 分数和二者相对排序。它在 Nemotron 3 的 RLHF 中承担核心奖励信号，优势是可解释、可原则化、对开放任务更灵活；代价是推理成本高，并且仍然存在 LLM judge 的 reward hacking、长度/格式偏置和鲁棒性风险。

## Nemotron 里具体用的是哪个 GenRM

公开资料显示，Nemotron 3 Nano / Super 的 RLHF 使用的主力 GenRM 是：

- `Qwen3-Nemotron-235B-A22B-GenRM`
- 初始化模型：`Qwen3-235B-A22B-Thinking-2507`
- 训练数据：HelpSteer3、commercial-friendly `lmarena-140k` 子集、近期收集的人类偏好数据，以及安全偏好数据
- 模型功能：输入对话历史、最后用户请求和两个候选 assistant response，输出两个单独 helpfulness 分数和一个 pairwise ranking 分数
- 开源状态：Hugging Face 上有公开模型卡，license 标为 Apache-2.0

NVIDIA 文档还说明，在 Nemotron 3 Super 的 RLHF stage 中，GenRM 既用于 multi-environment RL 阶段，也作为最终 RLHF-only 阶段的唯一主要偏好奖励信号；RLHF 阶段额外加 KL penalty 防止 policy 偏离 reference policy。

## 技术核心

### 1. 从 scalar reward head 转向 generative judge

传统 RM 通常把 prompt/response 编码后接一个 scalar head，用 Bradley-Terry loss 学会区分 chosen/rejected。GenRM 则保留 LLM 的生成能力，让模型通过 next-token prediction 生成 critique / reasoning / verdict。

核心变化：

- 评价不再是一次前向得到一个隐式分数，而是显式生成评估过程。
- reward 可以包含多维解释，例如帮助性、事实性、安全性、语言匹配、代码风格。
- 评分可以通过文本输出结构化为 helpfulness score、ranking score、principle satisfaction 等。

这让 GenRM 更像“可训练的 judge agent”，而不是普通分类器。

### 2. Pairwise 比较是 Nemotron RLHF 的基本单元

Nemotron 的 GenRM 输入格式是：

- conversation history
- last user turn
- `response_1`
- `response_2`

输出包括：

- response 1 helpfulness：1 到 5
- response 2 helpfulness：1 到 5
- ranking score：1 到 6，其中 1 表示 response 1 明显更好，6 表示 response 2 明显更好

Nano technical report 中还给出了 GenRM 训练 reward 形式：惩罚格式错误、helpfulness 预测偏差和 ranking 预测偏差；同时通过交换两个 response 的位置来缓解 positional bias。

### 3. 先生成 critique，再给 scalar / ranking

HelpSteer3-Preference 论文和 Nemotron-Cascade 2 report 都强调，GenRM 的关键不是只输出分数，而是先生成对候选回答的优缺点分析，然后再输出 helpfulness scores 和 comparative ranking。

这个设计的意义：

- 对开放任务比单纯 scalar head 更自然。
- 能让 reward model 在评分前显式考虑任务要求和候选回答差异。
- 支持 inference-time scaling，例如采样多个 judge reasoning 后投票或平均。

HelpSteer3 结果显示，GenRM 相比最佳 Bradley-Terry RM 在 RM-Bench 和 JudgeBench 上都有提升；`voting@32` 继续提高指标，但显著增加计算成本。

### 4. Principle-following / RLBFF 是 Nemotron 新一代 GenRM 的关键升级

Nemotron 3 Super 文档称其使用的是 principle-following GenRM。这里的技术背景是 RLBFF：从自然语言反馈中抽取可以二元判断的 flexible principles，例如：

- “信息是否准确？”
- “代码可读性是否足够？”
- “是否符合安全/身份相关要求？”

然后把 reward modeling 变成 entailment-style 判断：某个 response 是否满足给定 principle。

这带来两个能力：

- 可以把人类偏好拆成更清楚的评价原则，降低黑盒偏好分数的不可解释性。
- 推理时可以指定关注原则，让 GenRM 更适合安全、身份、企业规范等可配置偏好。

### 5. RL 使用方式：GenRM 不是离线过滤器，而是在线 RL 环境的一部分

Nemotron 3 Super RLHF stage 中有 `genrm_compare` environment：对同一个 prompt 的多个 rollout 做 pairwise comparison，用 GenRM 分数聚合为训练 reward。

公开 recipe 还显示：

- prompt/step：128
- generations/prompt：16
- batch size：2048
- max sequence length：49152
- GenRM router DP size：8
- RLHF stage 使用 KL penalty

这说明 GenRM 被放进大规模 RL loop 里，而不是只在训练前做 data filtering。对于非可验证任务，如写作、开放式 chat、安全边界、identity 行为，GenRM 提供了 RLVR 无法直接提供的偏好奖励。

## 当前现状

### 模型与数据已较开放

公开可见资产包括：

- `Qwen3-Nemotron-235B-A22B-GenRM`
- `Qwen3-Nemotron-235B-A22B-GenRM-2603`
- `Qwen3-Nemotron-32B-GenRM-Principle`
- `Llama-3.3-Nemotron-Super-49B-GenRM`
- `HelpSteer3` / `HelpSteer3-Preference`
- Nemotron 3 Nano / Super technical reports
- NeMo RL / Nemotron RLHF recipe docs

这比只发布 policy checkpoint 更有价值，因为 reward model、preference data、训练 recipe 都能帮助复现实验或构建类似 pipeline。

### 主要应用场景

1. Nemotron 3 Nano / Super 的 RLHF 奖励模型
2. open-ended instruction following 质量提升
3. 安全、identity、拒答边界等原则化行为约束
4. pairwise preference data 扩展和自动标注
5. LLM-as-a-judge benchmark，例如 RM-Bench / JudgeBench
6. 长答案、复杂任务、agentic tool-use 轨迹中的非可验证部分评分

### 主要瓶颈

1. 成本高  
   GenRM 需要生成 critique 和结构化评分，远慢于 scalar RM。HelpSteer3 明确指出 GenRM 和 voting@32 更准但计算更贵。

2. 鲁棒性仍不足  
   LLM-as-judge / GenRM 可能被格式、长度、推理开头、无意义 token 等表面模式影响。相关工作如 One Token to Fool LLM-as-a-Judge 表明，生成式 judge 在 reference-based reward 场景下也可能被 trivial tokens 诱导误判。

3. reward hacking 风险没有消失  
   只要 policy 能反复查询或间接适应 GenRM，就可能学到 GenRM 的偏好漏洞，例如更长、更格式化、更像 rubric 的回答。

4. 校准困难  
   helpfulness 1-5 和 ranking 1-6 是否跨任务、跨语言、跨长度一致，是实际使用中的关键问题。

5. 与 verifiable reward 的边界需要清楚  
   数学、代码、工具调用等能验证的任务不应完全依赖 GenRM；更合理的是 verifiable reward + GenRM preference + safety principles 的混合奖励。

## 关键工作脉络

| 时间 | 工作 | 贡献 |
|---|---|---|
| 2024 | Generative Reward Models | 提出 GenRM：用 LLM 生成 reasoning traces 和 preference labels，结合 RLHF 与 RLAIF；相比零样本 LLM judge 和传统 BT RM，在 OOD preference 上更强。 |
| 2025 | HelpSteer3-Preference | NVIDIA 发布 4 万多条高质量人类偏好样本，覆盖 General/STEM/Code/Multilingual；训练的 RM 在 RM-Bench/JudgeBench 上显著超过旧 RM。 |
| 2025 | HelpSteer3 GenRM experiments | 证明生成 critique 后再打分的 GenRM 优于最佳 Bradley-Terry RM，voting@32 进一步提升但成本更高。 |
| 2025 | RLBFF | 将自然语言反馈转成二元 flexible principles，把 reward modeling 变成 principle entailment；支持推理时指定评价原则。 |
| 2025 | Nemotron 3 Nano | 使用 Qwen3-235B-A22B-Thinking-2507 初始化 GenRM，在 HelpSteer3、lmarena 子集和安全数据上训练，用于 Nano RLHF。 |
| 2026 | Nemotron 3 Super | 使用 principle-following GenRM；GenRM 贯穿 multi-environment RL 和最终 RLHF-only stage，用来增强 instruction following、robustness 和 interaction quality。 |
| 2026 | Nemotron-Cascade 2 | 沿用 Qwen3-235B-A22B-Thinking-2507 GenRM 路线，pairwise 比较所有 rollout pair，并结合 length-normalized reward 和 quality-gated conciseness bonus。 |
| 2025-2026 | LLM-as-judge robustness work | 指出 GenRM/LLM judge 容易受 superficial token、格式、长度、reward hacking 影响，推动 adversarial data augmentation、causal rubric、robust judge 等方向。 |

## 对 agentic LLM / search scaffold 的启发

### 1. Reward 应该拆成“可验证 + 可评价 + 可原则化”

对于 search agent，不能只靠最终 answer correctness，也不能只靠 LLM judge。更稳的结构是：

- exact/verifiable：引用是否存在、工具调用是否成功、答案是否包含 required fields
- preference/quality：证据覆盖、论证质量、表达清晰度
- principle/safety：是否泄露隐私、是否遵循用户约束、是否过度猜测

GenRM 最适合第二、第三类。

### 2. Pairwise comparison 比单点评分更稳

Nemotron 的 GenRM 不是简单给单个 rollout 打分，而是比较两个候选回答。这对 search scaffold 很重要：同一问题下采样多个 rollouts，做 pairwise tournament，通常比直接让 judge 给绝对分更容易校准。

### 3. 评价过程要可读、可审计

GenRM 先 critique 再评分，适合保存为训练日志。对 agent RL 来说，保留 judge rationale 能帮助：

- 分析 reward hacking
- 调试失败样本
- 识别 judge 是否偏向长度、格式或某类证据
- 构造 hard negatives / adversarial judge data

### 4. 需要显式防长度和格式偏置

Nemotron-Cascade 2 使用 length-normalized reward adjustment 和 quality-gated conciseness bonus，说明 NVIDIA 已经意识到 token usage 会在 RLHF 中快速膨胀。Search agent 也应避免 judge 总是偏好更长、更像论文的答案。

### 5. GenRM 应该和工具环境隔离

如果 policy 在训练中能学到 GenRM 的 prompt/template，很容易 reward hack。建议：

- judge prompt 多模板化
- 引入 adversarial negative examples
- 用 verifiable checks 约束 GenRM 分数上限
- 分开训练 reward model 和 policy，防止同源偏差过强
- 对高 reward 低 correctness 样本做专项审计

## 推荐阅读顺序

1. NVIDIA Nemotron 3 docs / model card：先理解实际系统里 GenRM 怎么接入 RLHF。
2. HelpSteer3-Preference：理解数据质量、偏好标注和 GenRM 评测。
3. RLBFF：理解 principle-following GenRM 的动机。
4. Generative Reward Models：理解 GenRM 相对 BT RM / LLM-as-judge 的原始方法。
5. Nemotron 3 Nano / Super / Cascade 2 reports：看工业级 RL recipe 如何把 GenRM 放进训练闭环。
6. One Token to Fool LLM-as-a-Judge、Reward Under Attack 等鲁棒性论文：理解 GenRM 作为 reward proxy 的风险。

## Sources

- NVIDIA Nemotron RLHF Stage 3 docs: https://docs.nvidia.com/nemotron/nightly/nemotron/super3/rl/rlhf.html
- Qwen3-Nemotron-235B-A22B-GenRM model card: https://huggingface.co/nvidia/Qwen3-Nemotron-235B-A22B-GenRM
- NVIDIA Nemotron 3 model page: https://research.nvidia.com/labs/nemotron/Nemotron-3/
- NVIDIA Nemotron 3 Nano technical report: https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Nano-Technical-Report.pdf
- NVIDIA Nemotron 3 Super technical report: https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Super-Technical-Report.pdf
- Nemotron-Cascade 2 technical report: https://research.nvidia.com/labs/nemotron/files/Nemotron-Cascade-2.pdf
- HelpSteer3 dataset card: https://huggingface.co/datasets/nvidia/HelpSteer3
- HelpSteer3-Preference paper: https://arxiv.org/abs/2505.11475
- Generative Reward Models paper: https://arxiv.org/abs/2410.12832
- RLBFF paper: https://arxiv.org/abs/2509.21319
- One Token to Fool LLM-as-a-Judge: https://arxiv.org/abs/2507.08794
