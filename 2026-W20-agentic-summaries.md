# Agentic LLM Paper Summaries 2026-W20

Source list: `2026-W20-agentic.md`

Process: each listed paper was read from its Hugging Face paper page when available, with `2605.11739` read from the arXiv abstract because it was supplied as a same-week supplemental seed rather than a Hugging Face W20 item. No PDFs or asset folders were downloaded for this pass.

## 1. MemPrivacy: Privacy-Preserving Personalized Memory Management for Edge-Cloud Agents

- **arXiv:** 2605.09530
- **Category:** Memory / privacy agents
- **Link:** https://arxiv.org/abs/2605.09530
- **Agentic relevance:** Agent memory system focused on privacy-preserving personalized memory across edge-cloud settings.

### English Summary

MemPrivacy targets a practical failure mode of long-term agent memory: cloud-side personalization can expose sensitive user data, while crude masking destroys the semantics needed for useful retrieval. The paper proposes an edge-cloud memory layer that detects sensitive spans locally, replaces them with type-aware placeholders, lets cloud memory systems operate on those placeholders, and restores the original values locally. It also introduces MemPrivacy-Bench and a configurable privacy taxonomy, showing that typed placeholders can preserve downstream memory utility much better than ordinary redaction.

### English Highlights

- Uses local reversible pseudonymization rather than sending raw sensitive values to cloud memory systems.
- Preserves semantic roles through typed placeholders, improving the privacy-utility trade-off over untyped masking.
- Provides a benchmark and deployable privacy extraction models for agent memory stacks.

### 中文总结

MemPrivacy 解决的是个很现实的问题：长期记忆智能体需要保存个性化信息，但云端记忆又会扩大隐私泄露面；简单打码虽然安全一些，却会破坏检索和个性化所需的语义。论文的做法是在端侧识别隐私片段，并替换成带类型的占位符，让云端只处理占位符，最终在本地恢复原值。它还构建了 MemPrivacy-Bench 和分级隐私 taxonomy，用来系统评估记忆系统里的隐私保护。

### 中文亮点

- 把隐私保护做成 memory pipeline 的架构层，而不是只靠 prompt 或事后过滤。
- 类型化占位符保留了“这是邮箱/健康信息/恢复码”等语义，减少对记忆检索的伤害。
- 评测覆盖真实 memory system，比较贴近 agent 产品部署场景。

### 中文锐评

方向非常工程实用，但系统成败高度依赖隐私抽取器的召回率。一旦端侧漏检敏感信息，后面的占位符机制就没法补救；如果过度保护，又会损害记忆质量。它更像必要的安全中间层，不是完整的 agent memory 方案。

## 2. δ-mem: Efficient Online Memory for Large Language Models

- **arXiv:** 2605.12357
- **Category:** Memory
- **Link:** https://arxiv.org/abs/2605.12357
- **Agentic relevance:** Online memory mechanism for LLMs, useful for persistent and long-horizon agents.

### English Summary

δ-mem proposes a compact online memory mechanism for frozen LLMs. Instead of extending context windows or replacing the backbone, it maintains a small associative memory state updated by delta-rule learning and injects low-rank corrections into attention during generation. The paper is relevant to agents because it offers a lightweight way to reuse historical information in long-running interactions, especially on memory-heavy benchmarks where ordinary context use becomes inefficient.

### English Highlights

- Adds memory through a compact state matrix rather than full fine-tuning or long-context expansion.
- Couples memory readout directly to attention computation.
- Improves memory-heavy tasks while largely preserving general model capability.

### 中文总结

δ-mem 关注 LLM 的在线记忆：模型在长期助手或 agent 场景中需要不断积累历史信息，但单纯扩大上下文窗口成本高、利用率也不稳定。论文在冻结的 full-attention backbone 外加入一个很小的关联记忆状态，用 delta-rule 更新，并在生成时给 attention 注入低秩修正。它的价值在于提供一种低成本、在线更新的记忆机制。

### 中文亮点

- 不需要替换 backbone，也不需要完整微调。
- 记忆状态很小，但直接参与 attention，路径比外部检索更紧。
- 对长会话、长期用户偏好、历史任务状态这类 agent 场景有参考价值。

### 中文锐评

δ-mem 很适合做“轻量长期状态”的研究原型，但它还不等同于可解释、可审计的 agent memory。真实智能体不仅要记住，还要知道哪些记忆可信、过期、冲突或不该使用；这些治理问题不一定能靠一个小型在线状态解决。

## 3. Self-Distilled Agentic Reinforcement Learning

- **arXiv:** 2605.15155
- **Category:** Agentic RL
- **Link:** https://arxiv.org/abs/2605.15155
- **Agentic relevance:** Directly targets self-distillation for agentic reinforcement learning.

### English Summary

This paper introduces SDAR, a reinforcement-learning framework for multi-turn LLM agents that uses on-policy self-distillation as an auxiliary objective. Standard RL gives sparse trajectory-level supervision, while teacher-style token guidance can destabilize multi-turn agents when negative signals come from imperfect skill use. SDAR keeps RL as the main optimizer and gates token-level distillation signals so that positive teacher guidance is amplified and unreliable negative rejections are softened. It reports gains on ALFWorld, WebShop, and Search-QA.

### English Highlights

- Combines trajectory-level RL with dense token-level self-distillation.
- Uses a sigmoid gate to control when distillation should influence policy learning.
- Targets multi-turn tool and environment agents rather than single-answer reasoning only.

### 中文总结

SDAR 面向多轮智能体强化学习。普通 RL 的奖励往往只在轨迹级别给信号，监督太粗；而直接把 on-policy self-distillation 搬到多轮 agent 中，又会因为技能检索和环境交互不稳定而引入错误负反馈。论文保留 RL 主干，把自蒸馏当作带门控的辅助目标，对有价值的 token 级正向信号加强，对不可靠的负向 teacher rejection 做软化，从而提升多轮任务表现。

### 中文亮点

- 明确处理多轮 agent 中“dense supervision”和“trajectory reward”之间的张力。
- 门控蒸馏比简单 GRPO+OPSD 更稳。
- 在 ALFWorld、WebShop、Search-QA 这类 agent benchmark 上验证，场景贴近工具/环境交互。

### 中文锐评

这篇对 agent RL 很有参考价值，但门控机制本质上是在判断 teacher 信号何时可信。真实开放任务里，teacher 的 privileged context、skill 使用和 reward verifier 都可能有偏差；如果这些偏差系统性存在，门控只能缓解，不能根治错误监督。

## 4. RubricEM: Meta-RL with Rubric-guided Policy Decomposition beyond Verifiable Rewards

- **arXiv:** 2605.10899
- **Category:** Agent training / rewards
- **Link:** https://arxiv.org/abs/2605.10899
- **Agentic relevance:** Uses rubric-guided policy decomposition for RL beyond simple verifiable rewards, relevant to agent training.

### English Summary

RubricEM tackles RL for deep-research agents whose outputs are long, tool-mediated, and hard to score with exact answers. It uses rubrics as a shared interface among policy execution, judge feedback, and memory. The framework decomposes research trajectories into stages such as planning, evidence gathering, reviewing, and synthesis, then applies stage-structured GRPO and reflection-based meta-policy evolution to turn judged trajectories into reusable experience.

### English Highlights

- Uses rubrics not only for final grading but also to structure policy stages and memory.
- Provides denser semantic feedback for long-horizon research workflows.
- Targets tasks beyond verifiable final-answer rewards.

### 中文总结

RubricEM 关注 deep research agent 的 RL 训练：这类任务没有简单标准答案，轨迹又包含规划、搜索、证据评估、报告合成等多个阶段。论文把 rubric 作为策略执行、judge 反馈和 agent memory 的共同接口，用自生成 rubric 让轨迹阶段化，再用 stage-wise 判断给 GRPO 提供更密的语义反馈，同时通过反思型 meta-policy 把经验沉淀成可复用的 rubric-grounded knowledge。

### 中文亮点

- 把 rubric 从“最终打分表”提升为训练和记忆的组织结构。
- 更适合长报告、复杂研究、开放式信息综合等不可精确验证任务。
- 对 search/research scaffold 的阶段化 reward 设计有直接启发。

### 中文锐评

rubric 是开放任务 RL 的好抓手，但也容易变成模型自我迎合的模板。关键风险是 rubric 是否真的覆盖任务质量，而不是只覆盖可描述、可评分的表面维度；否则 agent 会学会写符合 rubric 的过程，而不一定做出更可靠的研究。

## 5. MemLens: Benchmarking Multimodal Long-Term Memory in Large Vision-Language Models

- **arXiv:** 2605.14906
- **Category:** Memory benchmark
- **Link:** https://arxiv.org/abs/2605.14906
- **Agentic relevance:** Benchmark for multimodal long-term memory, a core capability for persistent agents.

### English Summary

MemLens benchmarks multimodal long-term memory for LVLMs and memory-augmented agents. It evaluates whether systems can use visual evidence across multi-session conversations, covering extraction, multi-session reasoning, temporal reasoning, knowledge updates, and refusal. The benchmark compares long-context LVLMs with memory agents and finds a trade-off: long-context models ground visual evidence well at shorter lengths but degrade as sessions grow, while memory agents are more length-stable yet often lose visual fidelity.

### English Highlights

- Tests multimodal memory rather than text-only recall.
- Uses image ablations to verify that visual evidence is actually needed.
- Exposes different failure modes in long-context LVLMs and memory-agent systems.

### 中文总结

MemLens 评测多模态长期记忆，重点不是“模型能不能背文字事实”，而是能不能在多会话中保留和使用视觉证据。它覆盖信息抽取、多会话推理、时间推理、知识更新和拒答等能力，并比较 long-context LVLM 与 memory-augmented agent。结果显示两类路线各有短板：长上下文模型短期视觉 grounding 较强，但上下文变长后退化；记忆 agent 更稳定，却容易压缩掉关键视觉细节。

### 中文亮点

- 把 memory benchmark 从文本扩展到真正需要图像证据的场景。
- 通过去图像 ablation 防止模型靠文本 shortcut 过关。
- 对多模态助手和长期观察型 agent 的记忆设计很有价值。

### 中文锐评

这个 benchmark 抓住了多模态 memory 的核心痛点：存文本摘要很容易，保留可复查的视觉证据很难。真正产品化还要继续追问：图像该存原图、embedding、caption 还是结构化对象？不同选择会直接影响隐私、成本和可解释性。

## 6. SANA-WM: Efficient Minute-Scale World Modeling with Hybrid Linear Diffusion Transformer

- **arXiv:** 2605.15178
- **Category:** World models / environment
- **Link:** https://arxiv.org/abs/2605.15178
- **Agentic relevance:** World modeling method relevant to simulated environments and embodied planning.

### English Summary

SANA-WM is an efficient open-source world model for minute-scale video generation with camera control. It combines hybrid linear attention, dual-branch camera conditioning, a two-stage generation pipeline, and a pose-annotation pipeline to synthesize long, high-resolution sequences with controlled motion. For agentic work, the relevance is environmental: such models can support simulation, imagined rollouts, and action-conditioned scene prediction for embodied or navigation agents.

### English Highlights

- Targets one-minute world generation rather than short clips.
- Emphasizes 6-DoF camera control and metric-scale pose supervision.
- Improves efficiency enough to make long video world modeling more practical.

### 中文总结

SANA-WM 是一个面向分钟级视频生成的 world model，目标是生成高质量、可控相机轨迹的长视频。它结合 hybrid linear attention、双分支相机控制、两阶段生成和姿态标注流程，提高长上下文建模和轨迹一致性。对 agent 来说，它更像环境模拟和 imagined rollout 的基础设施，可用于具身、导航、自动驾驶等需要预测场景演化的任务。

### 中文亮点

- 关注分钟级长视频，而不是几秒钟的视觉片段。
- 强调相机控制和空间一致性，适合环境建模。
- 开源高效模型有利于 agent 仿真生态复用。

### 中文锐评

视觉上能生成长视频不等于可作为 agent 环境。训练智能体还需要可交互对象、动作接口、物理约束、状态验证和奖励信号。SANA-WM 的价值取决于能否从“好看的世界预测”进一步接入可执行、可评测的环境循环。

## 7. LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling

- **arXiv:** 2605.08083
- **Category:** Agentic self-improvement
- **Link:** https://arxiv.org/abs/2605.08083
- **Agentic relevance:** Agentic discovery workflow for test-time scaling and LLM self-improvement.

### English Summary

This paper proposes AutoTTS, an environment-driven framework where LLM agents discover test-time scaling strategies rather than relying on hand-designed heuristics. It formulates width-depth test-time scaling as controller synthesis over pre-collected reasoning trajectories and probe signals. Controllers decide when to branch, continue, probe, prune, or stop, and are evaluated cheaply without repeatedly calling the base LLM. The main agentic idea is to let agents search over inference programs themselves.

### English Highlights

- Shifts design effort from manual TTS heuristics to environments for strategy discovery.
- Uses cheap trajectory/probe feedback to evaluate candidate controllers.
- Treats test-time compute allocation as an agent-discoverable program.

### 中文总结

AutoTTS 试图让 LLM 自动发现 test-time scaling 策略，而不是由研究者手写 branch、continue、probe、prune、stop 等推理启发式。它把宽度-深度 TTS 表述为 controller synthesis 问题，在预收集轨迹和 probe signal 上低成本评估控制器。这个方向的 agentic 意义在于：不仅让模型执行推理程序，还让模型参与发现更好的推理程序。

### 中文亮点

- 把 test-time compute 的调度本身变成可搜索、可优化的对象。
- 用环境反馈降低策略发现成本，避免每次都重新调用大模型。
- 对 scaffold 自动调参和搜索策略发现有直接启发。

### 中文锐评

这类工作很适合提升 search/reasoning scaffold，但要警惕过拟合到已有轨迹和 probe。真正强的 TTS 策略需要跨任务泛化；如果 discovery environment 设计得太窄，agent 发现的可能只是某个 benchmark 的省钱技巧。

## 8. World Action Models: The Next Frontier in Embodied AI

- **arXiv:** 2605.12090
- **Category:** Embodied / VLA agents
- **Link:** https://arxiv.org/abs/2605.12090
- **Agentic relevance:** Survey or framework around world-action modeling for embodied agents.

### English Summary

This survey frames World Action Models as embodied foundation models that jointly model future states and actions. It argues that current VLA policies are often reactive: they map observation to action without explicitly predicting how interventions change the world. WAMs integrate world modeling with action generation, enabling agents to reason over possible future state-action trajectories. The paper organizes the fragmented literature by architecture, conditioning, modality, and action-decoding strategy.

### English Highlights

- Defines WAMs as a bridge between VLA policies and predictive world models.
- Moves embodied agents from reactive policies toward action-conditioned forecasting.
- Provides a taxonomy useful for robotics and autonomous-driving agent design.

### 中文总结

这篇综述把 World Action Models 定义为同时建模未来状态和动作的具身基础模型。它指出许多 VLA 策略仍然偏反应式，只根据当前观察输出动作，缺少对“动作会如何改变世界”的显式建模。WAM 将世界模型和动作生成结合起来，让智能体能在未来状态-动作轨迹上做推演。论文的价值主要在统一概念和整理 taxonomy。

### 中文亮点

- 把 VLA 和 world model 两条线合并到一个更清晰的研究框架里。
- 强调 action-conditioned prediction 是具身 agent 的核心能力。
- 对设计机器人、自动驾驶、交互式环境 agent 有框架价值。

### 中文锐评

WAM 是正确方向，但综述框架离可落地系统还有距离。真正挑战在于世界模型的误差会在规划中被放大；如果模型能生成 plausible future，却不能准确预测关键 failure state，agent 反而可能更自信地犯错。

## 9. HyperEyes: Dual-Grained Efficiency-Aware Reinforcement Learning for Parallel Multimodal Search Agents

- **arXiv:** 2605.07177
- **Category:** Search agents / RL
- **Link:** https://arxiv.org/abs/2605.07177
- **Agentic relevance:** RL method for parallel multimodal search agents.

### English Summary

HyperEyes argues that multimodal search agents should search wider instead of only longer. Rather than querying one target entity at a time, it enables concurrent grounded queries by fusing visual grounding and retrieval into an atomic action. The training pipeline includes parallel-amenable data synthesis and dual-grained RL: macro-level rewards encourage efficient tool usage, while micro-level supervision improves entity-level grounding and retrieval behavior.

### English Highlights

- Treats parallel search as a first-class action design for multimodal agents.
- Optimizes both answer quality and interaction efficiency.
- Provides useful ideas for reducing redundant tool rounds in search scaffolds.

### 中文总结

HyperEyes 面向多模态搜索智能体，核心观点是：当问题能分解成多个独立子检索时，agent 应该横向并行搜索，而不是逐个目标顺序调用工具。它把视觉 grounding 和 retrieval 合成一个原子动作，并通过数据合成和双粒度 RL 训练 agent 同时优化任务结果和工具效率。对搜索类 agent 来说，这是很直接的效率优化方向。

### 中文亮点

- 把并行查询作为 action space 设计，而不是外部工程加速。
- 宏观奖励控制轨迹成本，微观训练改善实体级搜索质量。
- 对多实体、多约束、多图文证据任务有明显价值。

### 中文锐评

并行搜索能降轮数，但会增加查询规划和结果合并的复杂度。真实 web/search 环境里，过度并行可能导致噪声证据暴涨、上下文污染和更高 API 成本；关键是 agent 是否知道哪些子问题值得并行，哪些必须先后依赖。

## 10. EVA-Bench: A New End-to-end Framework for Evaluating Voice Agents

- **arXiv:** 2605.13841
- **Category:** Voice agents / evaluation
- **Link:** https://arxiv.org/abs/2605.13841
- **Agentic relevance:** End-to-end benchmark/framework for evaluating voice agents.

### English Summary

EVA-Bench evaluates voice agents end to end, covering both realistic simulated conversations and voice-specific failure modes. It runs bot-to-bot audio interactions over dynamic multi-turn tasks and validates the simulation before scoring. Its metrics separate task accuracy, faithfulness, speech fidelity, conversation progression, conciseness, and turn-taking timing. The benchmark includes enterprise scenarios plus perturbations for accents and noise.

### English Highlights

- Evaluates voice agents as spoken interactive systems, not just text chatbots.
- Includes simulation validation to catch bad user-simulator behavior.
- Measures both task success and conversation experience.

### 中文总结

EVA-Bench 是面向 voice agents 的端到端评测框架。它不仅看任务是否完成，还模拟动态多轮音频对话，并评估语音场景中特有的问题，比如语音保真、轮次衔接、表达简洁度、噪声和口音鲁棒性。指标上分成 EVA-A 和 EVA-X，分别覆盖准确性和体验质量，适合企业语音助手、客服和电话自动化场景。

### 中文亮点

- 把 voice agent 当作音频交互系统评测，而不是把 ASR 后文本扔给普通 agent benchmark。
- 同时衡量任务完成、忠实性、语音质量和对话体验。
- 企业场景和扰动测试让 benchmark 更接近真实部署。

### 中文锐评

语音 agent 评测很容易被拆成 ASR、LLM、TTS 单点指标，EVA-Bench 的端到端路线是对的。但 bot-to-bot 模拟仍然会受 simulator 偏差影响，真实用户的打断、犹豫、情绪和不规范表达可能更难覆盖。

## 11. Do Enterprise Systems Need Learned World Models? The Importance of Context to Infer Dynamics

- **arXiv:** 2605.12178
- **Category:** World models / enterprise agents
- **Link:** https://arxiv.org/abs/2605.12178
- **Agentic relevance:** Studies learned world models and dynamics inference in enterprise-system contexts relevant to operational agents.

### English Summary

This paper asks whether enterprise agents always need learned world models when the environment dynamics are encoded in readable configuration and business logic. It argues that offline-trained dynamics models are brittle under tenant-specific deployment shift, while runtime discovery can read the active system configuration and infer current transition rules. The paper introduces enterprise discovery agents and CascadeBench for reasoning over configurable enterprise cascades.

### English Highlights

- Challenges the assumption that world dynamics must always be internalized during training.
- Emphasizes runtime configuration discovery for enterprise systems.
- Provides a benchmark for cascade prediction under deployment shift.

### 中文总结

这篇论文问了一个很现实的问题：企业系统里的状态转移规则往往写在配置和业务逻辑里，agent 是否一定要靠训练学一个 world model？作者认为，企业环境高度 tenant-specific，离线学到的 dynamics 很容易在部署时失效；如果规则可读，agent 应该在运行时发现配置并推断当前实例的转移逻辑。论文提出 enterprise discovery agents 和 CascadeBench 来评估这类能力。

### 中文亮点

- 把 world model 从“模型内部记住规律”扩展到“运行时读取环境规律”。
- 适合 SaaS、工作流、审批流、CRM 等可配置企业系统。
- 对 tool-use agent 的环境发现和状态预测有直接启发。

### 中文锐评

这篇的判断很工程正确：企业 agent 最怕拿通用先验硬猜业务规则。但 runtime discovery 也不简单，配置可能分散、权限受限、文档过期或和代码不一致。真正系统需要 discovery、验证和安全边界一起做。

## 12. MemEye: A Visual-Centric Evaluation Framework for Multimodal Agent Memory

- **arXiv:** 2605.15128
- **Category:** Agent memory evaluation
- **Link:** https://arxiv.org/abs/2605.15128
- **Agentic relevance:** Evaluation framework for visual-centric memory in multimodal agents.

### English Summary

MemEye evaluates whether multimodal agents preserve the visual evidence needed for later reasoning. It varies both the granularity of decisive visual evidence, from scene-level to pixel-level, and the way evidence must be used, from single-evidence lookup to evolutionary synthesis over time. The benchmark includes validation gates to reduce shortcuts and shows that current memory methods struggle with fine-grained visual details and state changes.

### English Highlights

- Focuses on visual evidence preservation, not only textual memory.
- Tests evidence granularity and temporal/evolutionary reasoning.
- Includes shortcut-resistance checks for answerability and visual necessity.

### 中文总结

MemEye 关注多模态 agent memory 是否真正保留视觉证据。它从两个维度评测：证据粒度从场景级到像素级，证据使用方式从单次查找扩展到随时间演化的综合推理。论文构造了多个生活场景任务，并加入 answerability、shortcut resistance、visual necessity 等验证门，发现现有 memory 方法对细粒度视觉细节和状态变化仍然处理不好。

### 中文亮点

- 比普通多模态 QA 更贴近长期 agent：证据要被保存并在未来复用。
- 明确测试 pixel-level 和 state-evolution 类困难记忆。
- 对视觉日志、屏幕历史、机器人观察记忆都很有价值。

### 中文锐评

MemEye 和 MemLens 都说明了同一件事：caption 化记忆远远不够。但评测越强调视觉细节，成本和隐私压力越大。真实 agent 需要的不只是“记住更多图像”，而是决定哪些视觉证据值得长期保存。

## 13. Predicting Decisions of AI Agents from Limited Interaction through Text-Tabular Modeling

- **arXiv:** 2605.12411
- **Category:** Agent behavior modeling
- **Link:** https://arxiv.org/abs/2605.12411
- **Agentic relevance:** Models and predicts agent decisions from limited interaction traces.

### English Summary

This paper studies whether an agent can predict an unfamiliar counterpart's next decision from a small number of interactions. It frames negotiation and bargaining as target-adaptive text-tabular prediction, combining structured game-state features, dialogue history, offer history, and a small set of labeled prior games from the same counterpart. It also uses hidden states from a small frozen LLM as decision-oriented features.

### English Highlights

- Treats agent modeling as few-shot adaptation to an unknown counterpart.
- Combines tabular state, text dialogue, and LLM-observer representations.
- Relevant to negotiation, procurement, market agents, and safety monitoring.

### 中文总结

这篇论文研究如何从少量交互预测未知 AI agent 的下一步决策。它把谈判和交易场景表述为 text-tabular prediction：每个决策点包含结构化游戏状态、报价历史和自然语言对话，同时给出同一目标 agent 的少量历史样本作为适配上下文。模型还使用一个小型冻结 LLM 的 hidden state 作为“观察者特征”，帮助表示对话中的决策信号。

### 中文亮点

- 把对手 agent 建模成少样本适配问题。
- 同时利用结构化状态和语言交互。
- 对多 agent 谈判、采购、交易和风险评估有现实意义。

### 中文锐评

预测 agent 决策很有用，也很敏感。这个方向一旦变强，可以用于协商优化，也可能用于操纵对手 agent。评测如果只在受控游戏里成立，还需要谨慎外推到开放商业交互。

## 14. TMAS: Scaling Test-Time Compute via Multi-Agent Synergy

- **arXiv:** 2605.10344
- **Category:** Multi-agent systems
- **Link:** https://arxiv.org/abs/2605.10344
- **Agentic relevance:** Multi-agent approach for scaling test-time compute.

### English Summary

TMAS uses multiple specialized agents to scale test-time compute through coordinated reasoning. It addresses weaknesses in parallel trajectory methods that either coordinate weakly or reuse noisy historical information. TMAS introduces hierarchical memories: an experience bank for reliable intermediate conclusions and local feedback, and a guideline bank for higher-level strategies that prevent redundant reasoning. The result is a structured multi-agent inference process balancing exploration and exploitation.

### English Highlights

- Organizes test-time scaling as collaboration among specialized agents.
- Separates low-level reusable evidence from high-level reusable strategies.
- Targets information flow across trajectories and refinement rounds.

### 中文总结

TMAS 把 test-time scaling 组织成多智能体协作过程。现有方法常常只是并行跑多条推理轨迹，协作弱，或者复用历史信息时噪声大。TMAS 用层级记忆解决这个问题：experience bank 记录可靠中间结论和局部反馈，guideline bank 记录高层策略，帮助后续 rollout 避免重复探索。它的核心是让多条推理轨迹之间有结构化信息流。

### 中文亮点

- 把 TTS 从“多采样”推进到“多 agent 协作”。
- 层级记忆设计适合复杂推理和搜索任务。
- 对 search scaffold 的经验复用、策略复用有借鉴价值。

### 中文锐评

多 agent TTS 很容易把 token 花在“互相讨论”而不是真正解题上。TMAS 的关键不在 agent 数量，而在记忆过滤和复用质量；如果 guideline bank 记录了错误策略，系统会更高效地走错路。

## 15. Beyond Individual Intelligence: Surveying Collaboration, Failure Attribution, and Self-Evolution in LLM-based Multi-Agent Systems

- **arXiv:** 2605.14892
- **Category:** Multi-agent systems
- **Link:** https://arxiv.org/abs/2605.14892
- **Agentic relevance:** Survey on collaboration, failure attribution, and self-evolution in LLM multi-agent systems.

### English Summary

This survey connects three themes that are often studied separately in LLM multi-agent systems: collaboration, failure attribution, and self-evolution. It organizes the field through a LIFE progression: laying capability foundations, integrating agents through collaboration, finding faults through attribution, and evolving through autonomous improvement. The main value is causal framing: collaboration quality affects diagnosability, and diagnosability determines whether self-evolution can be meaningful.

### English Highlights

- Reviews multi-agent systems as a pipeline from capability to collaboration to fault attribution to evolution.
- Emphasizes error propagation and difficult diagnosis in coordinated systems.
- Useful as a map for building debuggable multi-agent architectures.

### 中文总结

这篇综述把 LLM 多智能体系统中的协作、失败归因和自我演化放进同一个框架。作者提出 LIFE progression：先建立能力基础，再通过协作整合智能体，然后进行失败归因，最后推动自主改进。它的价值在于强调因果依赖：协作结构决定错误是否能被定位，错误是否能定位又决定自我演化是否有效。

### 中文亮点

- 不只讨论“多 agent 如何合作”，还讨论合作失败后如何归因和改进。
- 关注错误传播，这是多智能体系统真正难调的地方。
- 对设计可调试、可演化的 agent team 有参考价值。

### 中文锐评

综述框架有价值，但多 agent 领域最大问题仍是实证薄弱：很多系统看起来结构复杂，实则收益来自更多 token 或更强 base model。后续需要更强的消融和失败归因 benchmark，否则“self-evolution”很容易停留在概念层。

## 16. WildClawBench: A Benchmark for Real-World, Long-Horizon Agent Evaluation

- **arXiv:** 2605.10912
- **Category:** Benchmark / long-horizon agents
- **Link:** https://arxiv.org/abs/2605.10912
- **Agentic relevance:** Real-world long-horizon benchmark for agent evaluation.

### English Summary

WildClawBench evaluates agents in native CLI runtimes rather than synthetic sandboxes or mock APIs. It contains 60 human-authored bilingual and multimodal tasks across several categories, each running inside reproducible Docker containers with actual agent harnesses and real tools. The grading combines deterministic checks, environment-state auditing, and LLM/VLM semantic judgment. The benchmark highlights that harness choice itself can strongly affect model performance.

### English Highlights

- Uses real CLI agent harnesses such as OpenClaw, Claude Code, Codex, and Hermes Agent.
- Evaluates long-horizon work with real tools and side effects.
- Combines rule checks, state audits, and semantic judging.

### 中文总结

WildClawBench 把 agent 评测放到更接近真实部署的 CLI runtime 中，而不是只用短任务、mock API 或纯 final answer。它包含 60 个双语、多模态、人工编写的长时程任务，在 Docker 中运行真实工具和真实 agent harness。评分结合规则检查、环境状态审计和 LLM/VLM 语义判断。结果也显示，harness 本身会显著影响模型表现。

### 中文亮点

- 评测真实工具调用和副作用，而不只是问答。
- 把 agent harness 作为实验变量，暴露工程框架差异。
- 对代码 agent、终端 agent、办公自动化 agent 都有强参考价值。

### 中文锐评

这是很必要的 benchmark，因为真实 agent 失败常出在环境和工具链，不是模型答题能力。但混合评分也会带来维护成本和 judge 偏差；如果 benchmark 继续扩展，任务可复现性和评分稳定性会是关键。

## 17. STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?

- **arXiv:** 2605.06527
- **Category:** Memory validity
- **Link:** https://arxiv.org/abs/2605.06527
- **Agentic relevance:** Tests whether agents can detect outdated or invalid memories.

### English Summary

STALE evaluates whether LLM agents can detect when stored memories have become invalid. It focuses on implicit conflict: later evidence invalidates an earlier memory without directly negating it. The benchmark probes state resolution, resistance to stale premises, and downstream policy adaptation. The paper finds a gap between retrieving updated evidence and actually acting on it, which is central for long-term personalized agents.

### English Highlights

- Tests memory invalidation rather than static memory recall.
- Covers implicit conflicts that require contextual and commonsense inference.
- Evaluates whether agents use updated state in later behavior.

### 中文总结

STALE 评测长期记忆 agent 是否知道旧记忆已经失效。它关注 implicit conflict：新证据并不直接说“之前是错的”，但从上下文看已经推翻了旧状态。benchmark 从三个角度测试：识别旧状态过期、拒绝带有旧前提的问题、以及在后续行为中主动应用新状态。论文指出，很多模型能检索到新证据，却不能真正据此行动。

### 中文亮点

- 从“记住什么”推进到“知道什么已经不能信”。
- implicit conflict 更接近真实长期助手场景。
- 对 memory update、belief state、personalization 都很关键。

### 中文锐评

长期 agent 最危险的不是忘记，而是带着过期记忆自信行动。STALE 方向非常重要，但还需要和 memory deletion、用户纠错、隐私策略结合起来；否则只会检测过期事实，却不解决记忆治理全链路。

## 18. MCP-Cosmos: World Model-Augmented Agents for Complex Task Execution in MCP Environments

- **arXiv:** 2605.09131
- **Category:** MCP / environment agents
- **Link:** https://arxiv.org/abs/2605.09131
- **Agentic relevance:** World-model-augmented agents for complex tasks in MCP environments.

### English Summary

MCP-Cosmos integrates world models into the Model Context Protocol ecosystem. The paper argues that MCP standardizes tool interfaces but does not solve how agents understand environment dynamics. Its Bring Your Own World Model strategy lets agents simulate state transitions and refine plans before execution. Experiments compare strategies such as ReAct and SPIRAL with multiple planning and world models on MCP-Bench tasks, reporting improvements in tool success and parameter accuracy.

### English Highlights

- Connects MCP, world models, and agent planning into a single framework.
- Uses latent simulation to improve plans before tool execution.
- Adds metrics such as execution quality for environment interaction.

### 中文总结

MCP-Cosmos 试图把 world model 接入 MCP 生态。MCP 统一了 LLM 与外部工具的接口，但 agent 仍然缺少对环境动态的建模：计划可能忽略执行时状态变化，ReAct 又缺少长程预见。论文提出 BYOWM，让 agent 在执行前用 world model 模拟状态转移并修正计划，在 MCP-Bench 上评估工具成功率、参数准确率和执行质量。

### 中文亮点

- 把 MCP 从“工具接口协议”推进到“带环境模型的执行框架”。
- 支持不同 world model 插拔，工程上有扩展性。
- 对复杂工具链 agent 的预执行仿真很有启发。

### 中文锐评

MCP+world model 是自然组合，但世界模型的可靠性会直接决定 agent 是否敢信模拟结果。对于真实工具环境，错误模拟可能比没有模拟更糟，因为它会让 agent 在执行前形成错误信心。

## 19. Rubric-based On-policy Distillation

- **arXiv:** 2605.07396
- **Category:** Agent training / OPD
- **Link:** https://arxiv.org/abs/2605.07396
- **Agentic relevance:** On-policy distillation method guided by rubrics, relevant to post-training agent policies.

### English Summary

ROPD replaces teacher logits in on-policy distillation with structured semantic rubrics, making OPD usable with black-box teachers. It induces prompt-specific rubrics from teacher-student contrasts, then uses those rubrics to score student rollouts for on-policy optimization. This is relevant to agent post-training because many strong teachers are proprietary, and agent behavior often needs semantic criteria rather than only exact labels.

### English Highlights

- Makes OPD black-box compatible by replacing logits with rubrics.
- Uses teacher-student contrast to create prompt-specific scoring criteria.
- Provides a simple baseline for scalable distillation when teacher internals are unavailable.

### 中文总结

ROPD 解决 logit-based OPD 的限制：很多 teacher 是黑盒，拿不到 logits。论文用结构化语义 rubric 代替 teacher logits，通过 teacher-student 对比为每个 prompt 生成评分标准，再用这些 rubric 给 student rollout 打分并做 on-policy 优化。对 agent 训练来说，这种方法适合无法访问 teacher 内部、但可以获得 teacher 输出和语义评价的场景。

### 中文亮点

- 把 OPD 从白盒 teacher 扩展到黑盒 teacher。
- rubric 能表达语义质量，比单一最终答案更灵活。
- 可用于 agent policy 的可解释 post-training。

### 中文锐评

rubric-based OPD 的上限取决于 rubric 质量。如果 rubric 是 teacher 输出的再包装，可能继承 teacher 偏差；如果 rubric 太粗，又无法提供真正密集的优化信号。它很实用，但不是免费午餐。

## 20. PREPING: Building Agent Memory without Tasks

- **arXiv:** 2605.13880
- **Category:** Memory construction
- **Link:** https://arxiv.org/abs/2605.13880
- **Agentic relevance:** Builds agent memory without task-specific supervision.

### English Summary

PREPING studies pre-task memory construction: can an agent build useful procedural memory before seeing tasks from a new environment? It uses self-generated synthetic practice but controls both what to practice and what to store. A proposer generates tasks conditioned on proposer memory, a solver executes them, and a validator filters trajectories for memory insertion while feeding back to future proposals. The goal is to reduce the cold-start gap for new environments.

### English Highlights

- Targets memory cold start before task-specific experience exists.
- Uses proposer-solver-validator loops to control synthetic practice.
- Filters trajectories before memory insertion to reduce memory degradation.

### 中文总结

PREPING 研究 agent 在进入新环境、还没有真实任务经验前，能否通过自生成练习构建 procedural memory。它不是随便生成 synthetic tasks，而是用 proposer memory 控制练什么、solver 执行、validator 判断哪些轨迹值得写入记忆，并把反馈传回 proposer。目标是让 agent 在冷启动时就有一些可用的环境经验。

### 中文亮点

- 关注 pre-task memory，这是许多 agent 部署时的真实需求。
- proposer-solver-validator 结构避免 synthetic practice 变成无效噪声。
- 对 AppWorld、MCP 等新环境适配有启发。

### 中文锐评

自生成练习能缓解冷启动，但也可能让 agent 在自己的想象任务里过拟合。validator 的质量非常关键：如果它筛不出真正有迁移价值的轨迹，memory bank 会被“看似合理但不可用”的经验污染。

## 21. ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents

- **arXiv:** 2605.12481
- **Category:** GUI / computer-use agents
- **Link:** https://arxiv.org/abs/2605.12481
- **Agentic relevance:** GUI-tool orchestration method for computer-use agents.

### English Summary

ToolCUA addresses a hybrid action-space problem in computer-use agents: when should an agent operate through low-level GUI actions, and when should it switch to higher-level tools? The paper synthesizes interleaved GUI-tool trajectories, trains switching behavior through tool-bootstrapped GUI reinforcement fine-tuning, and then optimizes in a high-fidelity GUI-tool environment using online agentic RL. It is about choosing execution paths, not just grounding clicks.

### English Highlights

- Treats GUI and tool use as an interleaved action path selection problem.
- Synthesizes GUI-tool trajectories without relying entirely on real tool logs.
- Uses online agentic RL to improve switching decisions in realistic environments.

### 中文总结

ToolCUA 关注 computer-use agent 的混合动作空间：有些任务适合点击、输入等 GUI 原子动作，有些任务适合调用更高层工具。agent 如果不知道何时切换，就会走低效甚至错误路径。论文通过合成 GUI-tool 交错轨迹、tool-bootstrapped GUI RFT 和在线 agentic RL，训练 agent 学会选择更优的 GUI-tool 执行路径。

### 中文亮点

- 不只做 GUI grounding，而是做 GUI 与工具之间的路径编排。
- 用合成轨迹缓解真实 GUI-tool 数据稀缺。
- 对办公自动化、浏览器 agent、桌面 agent 都很关键。

### 中文锐评

GUI-tool orchestration 是 computer-use agent 的核心问题之一。但高层工具通常有权限、副作用和状态同步风险，不能只按效率优化；需要把安全、可逆性和用户确认也纳入 path selection。

## 22. Auto-Rubric as Reward: From Implicit Preferences to Explicit Multimodal Generative Criteria

- **arXiv:** 2605.08354
- **Category:** Reward modeling
- **Link:** https://arxiv.org/abs/2605.08354
- **Agentic relevance:** Converts implicit preferences into explicit rubrics/rewards, useful for agent training and evaluation.

### English Summary

Auto-Rubric as Reward reframes multimodal reward modeling as explicit criteria generation. Instead of compressing preferences into a scalar reward or opaque pairwise model, ARR extracts prompt-specific rubrics from a VLM's internalized preference knowledge and uses them as inspectable evaluation dimensions. This is useful for agent training because rubrics can provide structured, interpretable feedback and reduce some forms of reward hacking and evaluation bias.

### English Highlights

- Converts implicit preference knowledge into explicit, prompt-specific criteria.
- Supports zero-shot and few-shot reward construction.
- Makes reward signals more inspectable for multimodal generation and agent evaluation.

### 中文总结

ARR 把多模态生成的 reward modeling 从隐式偏好拟合转向显式 rubric 生成。传统 RLHF 常把复杂偏好压成标量或 pairwise 标签，容易变成不可解释的 reward proxy。ARR 先把 VLM 内部的偏好知识外化为 prompt-specific rubric，再用这些可检查的质量维度做评价。对 agent 来说，它提供了一种结构化、可解释的 reward 设计方式。

### 中文亮点

- 用显式 criteria 代替黑盒 reward，利于调试。
- 能针对不同 prompt 生成不同评价维度。
- 对多模态 agent 的过程评价和结果评价都有参考价值。

### 中文锐评

显式 rubric 确实更透明，但也可能把评价变成“能写出来的标准”。人类偏好里很多微妙因素很难完整 rubric 化；如果 agent 学会优化文字标准，而不是实际用户满意度，reward hacking 仍然会发生。

## 23. EvolveMem:Self-Evolving Memory Architecture via AutoResearch for LLM Agents

- **arXiv:** 2605.13941
- **Category:** Agent memory
- **Link:** https://arxiv.org/abs/2605.13941
- **Agentic relevance:** Self-evolving memory architecture explicitly designed for LLM agents.

### English Summary

EvolveMem argues that adaptive memory requires co-evolution of both stored content and retrieval mechanisms. It exposes retrieval configuration as an action space optimized by an LLM-powered diagnosis module. In each evolution round, the system reads failure logs, identifies root causes, proposes configuration changes, and applies them with safeguards such as revert-on-regression and explore-on-stagnation. The memory system effectively performs AutoResearch on its own architecture.

### English Highlights

- Evolves retrieval configuration, not only memory contents.
- Uses failure diagnosis to guide memory-system changes.
- Includes safeguards to avoid degrading from bad configuration updates.

### 中文总结

EvolveMem 认为真正自适应的 agent memory 不应只更新存储内容，还要让检索机制本身随任务演化。论文把 retrieval 配置暴露为可操作空间，让 LLM 诊断模块读取失败日志、分析原因、提出配置调整，并用自动回滚和停滞探索等机制保护系统。它相当于让 memory system 对自己的架构做 AutoResearch。

### 中文亮点

- 从“记忆内容演化”推进到“检索策略演化”。
- 以失败日志为驱动，比手工调参更 agentic。
- rollback safeguard 很重要，避免自我修改越改越差。

### 中文锐评

让记忆架构自我演化很有吸引力，但也带来可控性问题。系统如果不断改检索策略，性能变化会更难归因；一旦 failure diagnosis 错了，自动优化可能把偶然噪声当成结构问题。

## 24. Towards On-Policy Data Evolution for Visual-Native Multimodal Deep Search Agents

- **arXiv:** 2605.10832
- **Category:** Multimodal search agents
- **Link:** https://arxiv.org/abs/2605.10832
- **Agentic relevance:** On-policy data evolution method for visual-native multimodal deep search agents.

### English Summary

This paper proposes a visual-native harness and on-policy data evolution pipeline for multimodal deep search agents. The harness uses an image-bank reference protocol so images returned by tools remain addressable and reusable in later steps. On-policy Data Evolution then updates the data generator using rollouts from the current policy, so each round of training data targets the capabilities the agent still lacks. The framework supports both SFT data and RL data curation.

### English Highlights

- Makes intermediate visual evidence reusable across tool calls.
- Evolves training data based on the current policy's failures.
- Targets open-world multimodal search, where text and images interact over time.

### 中文总结

这篇论文面向 visual-native multimodal deep search agent。它指出现有工具环境常把搜索、浏览或变换返回的图片当成一次性输出，后续工具不能重新引用这些视觉证据。论文提出 image bank reference protocol，让所有工具返回图片都可被地址化复用；再用 On-policy Data Evolution，根据当前 policy 的 rollout 失败不断调整数据生成器，让每轮数据更贴近当前 agent 的短板。

### 中文亮点

- 把图片变成可复用的中间证据，而不是 transient artifact。
- 数据生成跟随当前策略演化，适合持续训练。
- 对多模态 search scaffold 的工具协议设计很有启发。

### 中文锐评

image bank 是多模态 agent 必需的基础设施，但也会带来证据管理问题：哪些图片可信、哪些过期、哪些只是噪声？如果图像引用机制没有和证据评分、去重、溯源绑定，context 可能很快被视觉垃圾填满。

## 25. DecodingTrust-Agent Platform (DTap): A Controllable and Interactive Red-Teaming Platform for AI Agents

- **arXiv:** 2605.04808
- **Category:** Agent safety / red teaming
- **Link:** https://arxiv.org/abs/2605.04808
- **Agentic relevance:** Interactive red-teaming platform for AI agents.

### English Summary

DTap is a controllable red-teaming platform for AI agents operating in dynamic tool environments. It spans many real-world domains and simulated systems such as workspace, payment, and communication services. The paper also introduces an autonomous red-teaming agent to scale risk assessment. It focuses on failures that occur through actions, such as leaking secrets, deleting data, or executing unauthorized transactions, not merely unsafe final text.

### English Highlights

- Provides interactive environments for agent security evaluation.
- Covers long-horizon, tool-mediated, high-impact failure modes.
- Includes autonomous red-team generation to scale testing.

### 中文总结

DTap 是面向 AI agents 的可控交互式红队平台。它覆盖多个真实领域和模拟系统，例如工作区、支付、通信等，用来测试 agent 在动态工具环境中的安全风险。论文强调 agent 风险不是只出现在最终回复里，而是会通过工具动作发生，比如泄露 API key、删除数据或发起未授权交易。DTap-Red 则用于自动化生成攻击和风险评估。

### 中文亮点

- 把 agent safety 评测放到可交互环境和工具副作用中。
- 覆盖真实高风险动作，而不是只看文本安全。
- 自动红队 agent 可以扩大测试覆盖面。

### 中文锐评

DTap 很贴近真实安全需求，但 red-teaming 平台的难点是攻击空间持续变化。固定模拟环境很快会被模型或开发者“适配”；要保持价值，必须持续加入新工具、新权限模型和新型 prompt/tool injection 场景。

## 26. FrameSkip: Learning from Fewer but More Informative Frames in VLA Training

- **arXiv:** 2605.13757
- **Category:** Embodied / VLA training
- **Link:** https://arxiv.org/abs/2605.13757
- **Agentic relevance:** Efficient VLA training technique for embodied agents.

### English Summary

FrameSkip improves VLA training by selecting more informative frames from dense robot demonstrations. Standard training treats every frame as equally useful, causing long low-change segments to dominate while critical transitions such as alignment, contact, grasping, and release are underrepresented. FrameSkip scores frames by action variation, visual-action coherence, task progress, and gripper transitions, then resamples the dataloader without changing the architecture or inference procedure.

### English Highlights

- Solves a data imbalance problem in dense robot trajectories.
- Focuses supervision on manipulation-critical transitions.
- Works as a dataloader-level method, leaving VLA models unchanged.

### 中文总结

FrameSkip 解决 VLA 训练中的帧级数据不平衡问题。机器人演示轨迹通常很密，很多帧变化很小，却在训练中占大量权重；真正关键的对齐、接触、抓取、释放等瞬间反而稀疏。论文通过动作变化、视觉-动作一致性、任务进度和夹爪状态变化给帧打分，在 dataloader 层重采样重要帧，不改变模型结构和推理流程。

### 中文亮点

- 方法简单，落在数据层，容易和现有 VLA pipeline 结合。
- 关注 manipulation 的关键状态变化，而不是平均学习所有帧。
- 能降低训练成本并提升成功率-保留率权衡。

### 中文锐评

FrameSkip 很务实，但“重要帧”的定义仍然依赖启发式。不同机器人、不同任务的关键转折可能不一样；如果评分函数偏了，可能会丢掉看似平稳但对长程上下文很重要的帧。

## 27. The DAWN of World-Action Interactive Models

- **arXiv:** 2605.11550
- **Category:** World-action models
- **Link:** https://arxiv.org/abs/2605.11550
- **Agentic relevance:** World-action interactive modeling for agents that need action-conditioned dynamics.

### English Summary

DAWN instantiates World-Action Interactive Models for autonomous driving. The paper argues that world prediction and action generation should condition each other: a plausible scene evolution depends on the maneuver, and a good maneuver depends on the possible scene evolution. DAWN couples a world predictor with a world-conditioned action denoiser in latent space, recursively refining predicted futures and action hypotheses during inference.

### English Highlights

- Models reciprocity between future scene evolution and action choice.
- Uses compact semantic latent rollouts instead of full pixel-space rollout.
- Targets long-horizon planning in interactive driving scenes.

### 中文总结

DAWN 把 World-Action Interactive Models 落到自动驾驶场景。论文认为世界预测和动作生成不能孤立：未来场景如何演化取决于自车动作，而好动作又取决于可能的场景演化。DAWN 在语义 latent space 中耦合 world predictor 和 world-conditioned action denoiser，让预测世界和动作假设在推理时递归互相修正。

### 中文亮点

- 明确建模“动作影响世界，世界反过来约束动作”的双向关系。
- 用短 latent rollout 支持长程轨迹生成，避免全像素 rollout 的高成本。
- 对交互式自动驾驶和具身规划都有启发。

### 中文锐评

递归互相修正的框架很优雅，但交互式场景里错误也会递归放大。自动驾驶特别需要 worst-case 和安全边界评估；如果只看平均规划指标，可能掩盖低概率高风险的预测-动作耦合错误。

## 28. Useful Memories Become Faulty When Continuously Updated by LLMs

- **arXiv:** 2605.12978
- **Category:** Memory robustness
- **Link:** https://arxiv.org/abs/2605.12978
- **Agentic relevance:** Studies memory degradation under continual updates, relevant to long-running agents.

### English Summary

This paper challenges the assumption that continually consolidated LLM memories always improve agents. It distinguishes episodic traces from consolidated abstractions and finds that LLM-written consolidated memory can become faulty even when derived from useful experiences. Utility may rise initially and then degrade below a no-memory baseline. The results suggest that raw trajectories can sometimes be safer than repeated abstraction and rewriting.

### English Highlights

- Identifies degradation in continuously updated consolidated memories.
- Separates failures of memory consolidation from the usefulness of original experiences.
- Shows that update schedule can change memory quality substantially.

### 中文总结

这篇论文指出，持续更新的 LLM consolidated memory 并不总是越用越好。agent memory 常把过去轨迹总结成抽象经验，并不断重写 memory bank，但作者发现这些抽象记忆可能从有用经验中产生错误，而且随着更新，效用先升后降，甚至低于无记忆 baseline。对比结果显示，问题往往出在 consolidation 步骤，而不是原始轨迹本身。

### 中文亮点

- 挑战“记忆越总结越好”的常见假设。
- 区分 episodic traces 和 consolidated abstractions 的风险。
- 对长期 agent 的 memory update 策略有很强警示意义。

### 中文锐评

这篇很值得做 agent memory 的人认真看。很多系统急着把轨迹压缩成“经验教训”，但总结本身会引入幻觉、过度泛化和错误规则。保留可追溯原始证据，可能比追求漂亮的抽象记忆更重要。

## 29. ATLAS: Agentic or Latent Visual Reasoning? One Word is Enough for Both

- **arXiv:** 2605.15198
- **Category:** Visual reasoning agents
- **Link:** https://arxiv.org/abs/2605.15198
- **Agentic relevance:** Investigates agentic versus latent visual reasoning.

### English Summary

ATLAS tries to unify agentic visual operations and latent visual reasoning through a single discrete functional token. Instead of generating intermediate images or calling external tools for every visual reasoning step, each functional token represents an internalized visual operation while remaining a standard token generated by next-token prediction. The design aims to keep the scalability of ordinary SFT/RL training while reducing the overhead of tool-based visual reasoning.

### English Highlights

- Uses discrete functional tokens as both latent units and agentic operations.
- Avoids verbose intermediate image generation.
- Keeps compatibility with standard autoregressive training pipelines.

### 中文总结

ATLAS 试图用一个离散 functional token 同时表示 agentic visual operation 和 latent visual reasoning unit。传统视觉推理可以通过外部工具/代码执行，也可以通过 latent embedding，但前者有上下文切换成本，后者训练和泛化困难。ATLAS 把内部视觉操作绑定到标准 token 上，让模型通过 next-token prediction 生成这些操作，从而兼顾可训练性和推理效率。

### 中文亮点

- 把 agentic operation 和 latent reasoning 做成统一 token 接口。
- 避免生成大量中间视觉内容，推理更轻。
- 可能为视觉 agent 的内化工具能力提供新路线。

### 中文锐评

“一个 token 表示一个视觉操作”概念很漂亮，但可解释性会变弱：用户和开发者不一定知道这个 token 内部到底做了什么。它减少外部工具调用成本，也可能牺牲可审计性和可调试性。

## 30. FrontierSmith: Synthesizing Open-Ended Coding Problems at Scale

- **arXiv:** 2605.14445
- **Category:** Task synthesis / coding agents
- **Link:** https://arxiv.org/abs/2605.14445
- **Agentic relevance:** Scalable synthesis of open-ended coding problems, useful for coding-agent training and evaluation.

### English Summary

FrontierSmith generates open-ended coding problems from existing closed-ended competitive programming tasks. It modifies goals, output constraints, and input generality, then uses an idea-divergence metric to select problems that elicit diverse solver approaches. Agents then generate tests and verifiers for the selected tasks. The goal is to train coding models on tasks with no single known optimal solution, closer to real engineering challenges.

### English Highlights

- Scales creation of open-ended coding tasks.
- Selects tasks that induce diverse solution strategies.
- Uses agents to generate tests and verifiers for synthesized problems.

### 中文总结

FrontierSmith 面向开放式 coding problem synthesis。很多真实工程任务没有唯一最优答案，但 LLM coding 训练长期偏向 bug fixing、feature implementation、竞赛题等封闭任务。论文从竞赛题出发，通过修改目标、限制输出、泛化输入来生成开放式变体，再用 idea divergence 选择能诱导不同解法的问题，并让 agent 生成测试和 verifier。

### 中文亮点

- 补齐 coding agent 训练中开放式任务稀缺的问题。
- 用多解多样性筛选任务，而不是只看题目表面变化。
- test/verifier 生成让开放任务更可训练、更可评测。

### 中文锐评

开放式 coding 任务合成很重要，但 verifier 质量决定上限。如果测试和评价仍然覆盖有限，模型可能学会迎合合成任务的偏好，而不是真正提升软件工程能力。

## 31. Learning to Communicate Locally for Large-Scale Multi-Agent Pathfinding

- **arXiv:** 2605.07637
- **Category:** Multi-agent algorithms
- **Link:** https://arxiv.org/abs/2605.07637
- **Agentic relevance:** Multi-agent coordination algorithm for pathfinding, relevant to agent communication and planning.

### English Summary

This paper studies decentralized learning for large-scale multi-agent pathfinding. It introduces LC-MAPF, a model with learnable local communication among neighboring agents. Agents exchange features over multiple rounds to coordinate better under partial observability. Although the setting is not LLM-specific, the work is relevant to agentic systems because it tackles scalable communication, coordination, and conflict avoidance in multi-agent planning.

### English Highlights

- Adds learnable local communication to decentralized MAPF.
- Improves coordination through multi-round neighbor feature exchange.
- Addresses a core multi-agent planning abstraction used in robotics and logistics.

### 中文总结

这篇论文研究大规模多智能体路径规划中的局部通信。MAPF 常用于多机器人、物流和搜索救援等场景，最优求解很难，因此需要可扩展的去中心化方法。LC-MAPF 让相邻 agent 进行多轮特征交换，通过可学习通信模块提升协作和避障能力。它虽然不是 LLM agent 论文，但对多智能体规划和通信机制有参考价值。

### 中文亮点

- 把通信作为可学习模块，而不是固定规则。
- 关注局部通信，利于大规模扩展。
- 对多机器人和 embodied multi-agent 系统有直接意义。

### 中文锐评

MAPF 的局部通信很扎实，但和 LLM 多智能体协作仍有距离。LLM agent 的通信包含语义、目标、工具状态和不确定性，不只是邻居坐标特征；迁移时不能简单套用。

## 32. Continual Harness: Online Adaptation for Self-Improving Foundation Agents

- **arXiv:** 2605.09998
- **Category:** Continual / self-improving agents
- **Link:** https://arxiv.org/abs/2605.09998
- **Agentic relevance:** Online adaptation framework for self-improving foundation agents.

### English Summary

Continual Harness formalizes online self-improvement for embodied agents. Motivated by Gemini Plays Pokemon experiments, it removes human-in-the-loop harness refinement and lets the agent alternate between acting and refining its own prompt, sub-agents, skills, and memory using past trajectory data. Unlike prompt optimization that assumes episodic resets, the framework adapts within a single ongoing run, targeting long-horizon partial-observability environments.

### English Highlights

- Focuses on reset-free online adaptation.
- Lets the harness, not only the model answer, evolve during a run.
- Uses trajectory history to improve prompts, skills, sub-agents, and memory.

### 中文总结

Continual Harness 关注 foundation agents 的在线自我改进。论文从 Gemini Plays Pokemon 的实验出发，认为长时程、部分可观测环境中的 agent 不仅要执行动作，还要持续改进自己的 prompt、sub-agents、skills 和 memory。与需要 episode reset 的 prompt optimization 不同，Continual Harness 在单次持续运行中根据过去轨迹进行自适应，目标是减少人工 harness refinement。

### 中文亮点

- 把 self-improvement 放在运行时 harness 层，而不是只训练模型参数。
- 支持无 reset 的长时程在线适应。
- 对游戏、机器人、持续任务 agent 都有启发。

### 中文锐评

运行时自我修改 harness 很强，也很危险。prompt、skills、memory 同时变化会让失败归因变得复杂；如果没有强日志、回滚和安全边界，agent 可能在持续改进中把自己改坏。

## 33. World Model for Robot Learning: A Comprehensive Survey

- **arXiv:** 2605.00080
- **Category:** Robot world models
- **Link:** https://arxiv.org/abs/2605.00080
- **Agentic relevance:** Survey of world models for robot learning and embodied agents.

### English Summary

This survey reviews world models for robot learning, covering predictive environment representations under actions. It discusses how world models support policy learning, planning, simulation, evaluation, and data generation, especially as foundation models and video generation methods improve. The survey organizes architectures, functional roles, robotic application domains, datasets, benchmarks, and evaluation protocols.

### English Highlights

- Provides a robot-learning-centered taxonomy of world models.
- Connects world models to planning, RL, simulation, and evaluation.
- Covers navigation, autonomous driving, and robotic video world models.

### 中文总结

这篇综述从机器人学习角度系统梳理 world models。它把 world model 看作预测环境在动作下如何演化的表示，并讨论其在策略学习、规划、仿真、评估、数据生成中的作用。随着 foundation models 和视频生成发展，机器人 world model 正在从想象式生成走向可控、结构化、基础模型规模的形式。论文还整理了数据集、benchmark 和评测协议。

### 中文亮点

- 机器人视角清晰，适合具身 agent 研究者快速建立地图。
- 把 world model 的功能角色和应用域分开梳理。
- 连接了 robot learning、video generation、planning 和 evaluation。

### 中文锐评

综述价值高，但 world model for robot learning 的核心矛盾仍然是 sim-to-real 和误差累积。生成视频看起来真实，不等于动作后果可用于安全规划；评测必须更关注可控性和因果准确性。

## 34. Missing Old Logits in Asynchronous Agentic RL: Semantic Mismatch and Repair Methods for Off-Policy Correction

- **arXiv:** 2605.12070
- **Category:** Agentic RL / off-policy correction
- **Link:** https://arxiv.org/abs/2605.12070
- **Agentic relevance:** Addresses off-policy correction for asynchronous agentic RL.

### English Summary

This paper studies a systems-level issue in asynchronous RL for LLM agents. Decoupling rollout generation from policy optimization improves throughput but creates off-policy correction problems when historical training-side logits are missing. The paper argues that importance ratios mix two different effects: train-inference discrepancy and policy staleness. It analyzes exact and approximate ways to recover or repair old-logit information, including snapshots, dedicated old-logit models, and synchronization strategies.

### English Highlights

- Targets asynchronous agentic RL training infrastructure.
- Clarifies semantic mismatch in off-policy correction.
- Proposes repair routes for missing historical logits.

### 中文总结

这篇论文讨论异步 agentic RL 中的 old logits 缺失问题。异步训练能提高 rollout 吞吐，但 PPO 类 off-policy correction 需要历史策略的训练侧 logits；实际系统中，由于延迟更新和部分 rollout，这些 old logits 经常缺失。论文指出这会把训练-推理分布差异和策略陈旧性纠缠在一起，破坏 correction 语义，并研究快照、专用 old-logit model、同步机制等修复方法。

### 中文亮点

- 非常贴近大规模 agent RL 的训练系统问题。
- 把重要性比率中的两类语义差异拆清楚。
- 对异步 rollout、endpoint 训练、policy lag 管理有工程价值。

### 中文锐评

这类论文看起来“底层”，但比很多高层 agent 架构更关键。agent RL 真跑起来时，吞吐、延迟、logit 版本和 correction 语义都会影响训练稳定性。问题是修复方案会增加系统复杂度，需要权衡可靠性和成本。

## 35. On-Policy Self-Evolution via Failure Trajectories for Agentic Safety Alignment

- **arXiv:** 2605.11882
- **Category:** Agent safety alignment
- **Link:** https://arxiv.org/abs/2605.11882
- **Agentic relevance:** Uses failure trajectories for on-policy self-evolution and agentic safety alignment.

### English Summary

This paper introduces FATE, an on-policy self-evolution framework for agent safety alignment. It argues that tool-using agents fail through trajectories, not only final responses: unsafe tool calls, prompt injection, harmful compliance, and over-refusal can all occur before the final answer. FATE turns verifier-scored failures into repair supervision by letting the same policy propose candidate repairs, filtering them across security, utility, refusal control, and trajectory validity, then optimizing with Pareto-aware policy optimization.

### English Highlights

- Aligns agents at trajectory level rather than response level only.
- Uses failure trajectories as on-policy repair data.
- Balances safety and utility with Pareto-front policy optimization.

### 中文总结

FATE 面向工具型 agent 的安全对齐。论文指出 agent 的失败常发生在轨迹中，而不是最终回复里：可能执行危险工具调用、服从注入指令、满足有害请求，或对无害任务过度拒绝。FATE 将 verifier 打分的失败轨迹转化为修复监督，让同一 policy 生成候选修复，并按安全性、实用性、过拒控制和轨迹有效性过滤，再用 Pareto-aware policy optimization 优化。

### 中文亮点

- 关注 trajectory-level safety，比只看 final answer 更适合 agent。
- 用失败轨迹驱动 on-policy self-evolution。
- 同时考虑安全和任务能力，避免简单安全化导致过拒。

### 中文锐评

失败轨迹是 agent safety 的宝贵训练数据，但 verifier 决定了系统学到什么。若 verifier 对工具副作用、权限边界或用户意图理解不准，FATE 可能把错误安全策略固化进 policy。

## 36. IntentVLA: Short-Horizon Intent Modeling for Aliased Robot Manipulation

- **arXiv:** 2605.14712
- **Category:** Embodied / VLA agents
- **Link:** https://arxiv.org/abs/2605.14712
- **Agentic relevance:** Intent modeling for VLA robot manipulation under ambiguous observations.

### English Summary

IntentVLA addresses observation aliasing in robot imitation learning. Similar visual-language observations may correspond to different action chunks depending on short-horizon intent, task phase, or recent context. Frame-conditioned VLA policies can resample inconsistent intents across replanning steps, causing unstable execution. IntentVLA encodes recent visual history into a compact intent representation and conditions action chunk generation on it, improving stability across ambiguity-aware benchmarks.

### English Highlights

- Models short-horizon intent to resolve ambiguous observations.
- Uses recent visual history rather than only the current frame and instruction.
- Improves rollout stability for robot manipulation tasks.

### 中文总结

IntentVLA 处理机器人操作中的 observation aliasing：相似的视觉-语言观察，在不同短期意图、任务阶段或上下文下，可能对应不同动作片段。普通 VLA policy 如果只看当前帧和指令，可能在相邻 replanning 步骤中反复切换意图，造成动作冲突和执行不稳。IntentVLA 用近期视觉历史编码短期 intent，并用它条件化动作片段生成。

### 中文亮点

- 把短期意图作为 VLA 稳定执行的核心变量。
- 针对部分可观测和动作歧义问题。
- AliasBench 专门隔离和评估 observation aliasing。

### 中文锐评

IntentVLA 抓到了 VLA 中一个真实问题：当前观察不够决定动作。但短期 intent 也可能被错误历史带偏，尤其在环境状态突变或人类中途改变目标时；模型需要知道什么时候应该坚持 intent，什么时候应该重估。

## 37. HAGE: Harnessing Agentic Memory via RL-Driven Weighted Graph Evolution

- **arXiv:** 2605.09942
- **Category:** Agent memory / RL
- **Link:** https://arxiv.org/abs/2605.09942
- **Agentic relevance:** RL-driven graph evolution for agentic memory.

### English Summary

HAGE treats memory retrieval as query-conditioned traversal over a weighted multi-relational graph, rather than flat vector search or fixed binary relations. Memory nodes are shared across relation-specific graph views, and trainable edge features represent relational strength and relevance. An LLM classifier identifies the query's relational intent, while a routing network modulates edge dimensions. RL then evolves the graph to improve agent memory retrieval.

### English Highlights

- Moves agent memory from static lookup to adaptive graph traversal.
- Represents relation strength and query-dependent relevance.
- Uses RL-driven graph evolution to improve retrieval paths.

### 中文总结

HAGE 把 agent memory retrieval 重新表述为带权多关系图上的查询条件化遍历，而不是普通向量检索或固定二元关系图。记忆节点在不同关系视图中共享，边上有可训练关系特征，表示关系强度、置信度和相关性。LLM 分类器识别查询意图，routing network 动态调节边特征，RL 用来演化图结构和检索策略。

### 中文亮点

- 让 memory graph 的边权和检索路径可学习、可演化。
- 关系类型和查询意图结合，比 flat retrieval 更细。
- 对复杂长期记忆和事件关系推理很有价值。

### 中文锐评

graph memory 的表达力强，但维护成本也高。长期运行后，图会变得庞大、噪声多、关系过期；如果没有删边、合并、冲突检测和可解释审计，weighted graph 可能只是更复杂的污染源。

## 38. Q-RAG: Long Context Multi-step Retrieval via Value-based Embedder Training

- **arXiv:** 2511.07328
- **Category:** Retrieval / RAG agents
- **Link:** https://arxiv.org/abs/2511.07328
- **Agentic relevance:** Multi-step retrieval method relevant to research and RAG agents.

### English Summary

Q-RAG trains the embedder itself for multi-step retrieval using reinforcement learning. Traditional RAG focuses on single-step retrieval, while complex questions often require chained search over very long contexts. Rather than fine-tuning a small LLM retriever, Q-RAG learns value-based embeddings that support multi-step retrieval and reports strong results on long-context benchmarks such as BabiLong and RULER with contexts up to millions of tokens.

### English Highlights

- Optimizes the embedder for multi-step retrieval instead of relying on a retriever LLM.
- Provides a resource-efficient path for long-context RAG.
- Relevant to research agents that need chained evidence discovery.

### 中文总结

Q-RAG 关注多步检索。传统 RAG 多是单步召回，但复杂问题往往需要多轮搜索和证据链。现有多步检索常微调小 LLM 做检索器，成本高，也难利用更大模型。Q-RAG 改为用 RL 训练 embedder，让 embedding 本身具备 value-based multi-step retrieval 能力，在长上下文 benchmark 上表现较强。

### 中文亮点

- 把多步检索能力下沉到 embedder，降低资源成本。
- 适合超长上下文和开放域问答。
- 对研究型 search agent 的证据链构建有直接启发。

### 中文锐评

训练 embedder 做多步检索很优雅，但检索 agent 不只需要“找到相关块”，还要判断覆盖是否充分、证据是否冲突、何时停止搜索。Q-RAG 解决 retrieval substrate，完整 research agent 还需要更高层的策略控制。

## 39. Orchard: An Open-Source Agentic Modeling Framework

- **arXiv:** 2605.15040
- **Category:** Agent framework
- **Link:** https://arxiv.org/abs/2605.15040
- **Agentic relevance:** Open-source framework for agentic modeling.

### English Summary

Orchard is an open-source framework for scalable agentic modeling. Its core component, Orchard Env, provides reusable primitives for sandbox lifecycle management across task domains, agent harnesses, and training stages. The paper builds recipes such as Orchard-SWE for coding agents, using trajectory distillation, credit-assignment SFT, and RL. Its importance is infrastructural: open agent training needs standardized environments, harnesses, and scalable recipes, not only benchmark leaderboards.

### English Highlights

- Provides reusable environment infrastructure for agent training.
- Includes recipes for coding agents with SFT and RL.
- Focuses on open-source scalable agentic modeling rather than orchestration only.

### 中文总结

Orchard 是一个开源 agentic modeling 框架，目标是补齐开放研究中的基础设施缺口。它的核心 Orchard Env 提供 sandbox lifecycle、任务域、agent harness 和训练阶段之间可复用的环境服务。论文还给出 Orchard-SWE 等 recipe，用轨迹蒸馏、credit-assignment SFT 和 RL 训练 coding agents。它的价值在于把 agent 训练从单点 benchmark 推向可复用 pipeline。

### 中文亮点

- 关注训练基础设施，而不只是 agent orchestration。
- 环境服务、harness 和 recipe 组合适合扩展到多任务。
- 对开源 agent RL/SFT 生态很重要。

### 中文锐评

Orchard 这种框架论文最需要时间检验。真正难点不是发布一个框架，而是让环境接口、数据格式、训练 recipe 在不同 agent 任务上长期稳定复用；否则很容易变成又一个只适配自家实验的代码库。

## 40. From Web to Pixels: Bringing Agentic Search into Visual Perception

- **arXiv:** 2605.12497
- **Category:** Agentic visual search
- **Link:** https://arxiv.org/abs/2605.12497
- **Agentic relevance:** Connects web/agentic search with visual perception.

### English Summary

This paper introduces Perception Deep Research, where identifying a visible object may require external facts, recent events, long-tail entity knowledge, or multi-hop relations before localization is possible. WebEye provides object-anchored tasks with verifiable evidence, boxes, masks, and QA pairs. Pixel-Searcher is an agentic workflow that first resolves hidden target identities through search, then grounds them into pixel-level outputs.

### English Highlights

- Connects web search and pixel-level perception.
- Builds tasks where visual grounding depends on external knowledge.
- Provides search-based grounding, segmentation, and VQA views.

### 中文总结

这篇论文把 agentic search 引入视觉感知。传统视觉定位通常假设目标已经在图像或模型知识里明确，但现实中一个可见物体可能要先通过外部事实、近期事件、长尾实体或多跳关系确定身份，才能定位。论文提出 WebEye benchmark 和 Pixel-Searcher workflow：先搜索解决隐藏目标身份，再把结果绑定到 box、mask 或 grounded answer。

### 中文亮点

- 把 web evidence 和 pixel grounding 连接起来。
- 任务设计包含可验证证据、框、mask 和 QA。
- 对开放世界视觉 agent 和多模态搜索很有价值。

### 中文锐评

这个方向很有现实意义，因为很多视觉问题不是“看图”就能解决。但 search-to-pixel 的错误链很长：搜索证据错、身份解析错、视觉匹配错都会导致失败。评测需要细分错误来源，否则很难知道该改 search 还是改 vision。

## 41. Covering Human Action Space for Computer Use: Data Synthesis and Benchmark

- **arXiv:** 2605.12501
- **Category:** Computer-use dataset / benchmark
- **Link:** https://arxiv.org/abs/2605.12501
- **Agentic relevance:** Data synthesis and benchmark for computer-use agents.

### English Summary

This paper studies long-tail GUI actions in computer-use agents. It argues that a small fraction of complex, diverse interactions accounts for many failures, because training data underrepresents low-frequency action types. It introduces CUActSpot, a benchmark across GUI, text, table, canvas, and natural-image modalities with actions such as click, drag, and draw. It also proposes a renderer-based data synthesis pipeline for screenshots, coordinates, instructions, and action traces.

### English Highlights

- Expands computer-use evaluation beyond click-centric GUI widgets.
- Covers multiple modalities and diverse action types.
- Uses renderer-based synthesis to scale complex interaction data.

### 中文总结

这篇论文关注 computer-use agent 的长尾动作空间。作者发现高级模型在复杂低频交互上仍然很不可靠，而这些动作占失败比例很高。论文提出 CUActSpot，覆盖 GUI、文本、表格、画布、自然图像等模态，以及点击、拖拽、绘制等动作；同时设计 renderer-based 数据合成 pipeline，生成场景、截图、坐标、指令和动作轨迹。

### 中文亮点

- 从点击 benchmark 扩展到更完整的人类操作空间。
- 数据合成覆盖多模态和复杂动作。
- 对 CUA 的 grounding、action prediction 和训练数据构建都很有用。

### 中文锐评

CUA 的长尾动作确实是短板，但合成数据能否覆盖真实软件的不规则性是关键。渲染器生成的场景往往更干净、更规则；如果没有真实应用分布校准，模型可能在 benchmark 上进步，在真实桌面上仍然脆。

## 42. Dynamic Skill Lifecycle Management for Agentic Reinforcement Learning

- **arXiv:** 2605.10923
- **Category:** Agent skills / RL
- **Link:** https://arxiv.org/abs/2605.10923
- **Agentic relevance:** Skill lifecycle management for agentic RL.

### English Summary

SLIM treats external skills as a dynamic optimization variable in agentic RL. Existing approaches either keep accumulating skills as persistent guidance or internalize skills until inference uses none. The paper argues that the optimal active skill set is non-monotonic and stage-dependent. SLIM estimates each skill's marginal contribution, retains useful skills, retires skills with negligible value, and expands the skill bank when repeated failures reveal missing capabilities.

### English Highlights

- Models skills as lifecycle-managed external resources.
- Uses leave-one-skill-out validation to estimate marginal contribution.
- Supports retaining, retiring, and expanding skills during RL.

### 中文总结

SLIM 研究 agentic RL 中的外部 skill 生命周期管理。很多方法要么不断累积 skill，要么把 skill 内化进 policy 后最终零 skill 推理。论文认为，在有限模型容量和不同任务阶段下，最优 active skill set 不是单调增加的，而是任务和阶段相关的。SLIM 通过 leave-one-skill-out 验证估计每个 skill 的边际贡献，并执行保留、退休、扩展三类操作。

### 中文亮点

- 把 skill bank 当作动态资源，而不是越多越好。
- retirement 机制能减少过期或低价值技能干扰。
- 对 Codex/agent skill 系统和 RL 训练都有参考意义。

### 中文锐评

skill lifecycle 很实用，但边际贡献估计可能很噪。某个 skill 在当前验证集没用，不代表未来任务没用；过早退休会损害长尾能力。需要结合任务分布、成本和召回风险做保守策略。

## 43. Learning to Foresee: Unveiling the Unlocking Efficiency of On-Policy Distillation

- **arXiv:** 2605.11739
- **Category:** LLM post-training algorithm
- **Link:** https://arxiv.org/abs/2605.11739
- **Agentic relevance:** Same-week user-supplied arXiv paper on efficient on-policy distillation, relevant to agent policy post-training though not listed on the HF W20 page.

### English Summary

This paper analyzes why on-policy distillation can be efficient for LLM post-training. Instead of attributing OPD only to denser supervision, it argues that OPD has "foresight": early updates align with the final model's update trajectory. The analysis identifies module-allocation effects, where updates concentrate on reasoning-critical modules, and update-direction effects, where dominant low-rank subspaces align early. The proposed EffOPD accelerates OPD by adaptively extrapolating along the current update direction.

### English Highlights

- Provides a parameter-dynamics explanation for OPD efficiency.
- Identifies module allocation and update-direction alignment as mechanisms.
- Proposes EffOPD as a plug-and-play acceleration method.

### 中文总结

这篇论文分析 on-policy distillation 为什么高效。它认为 OPD 的优势不只是监督更密、更稳定，而是存在一种“foresight”：训练早期的更新方向已经稳定朝向最终模型。论文从两个层面解释：模块分配上，OPD 会把更新集中到对推理更关键的模块；更新方向上，OPD 的主导低秩子空间会更早对齐最终更新子空间。基于此，作者提出 EffOPD，通过自适应外推当前更新方向加速训练。

### 中文亮点

- 从参数动态角度解释 OPD，而不是只停留在经验效果。
- 把高效性归因到关键模块更新和低秩方向早期对齐。
- EffOPD 不需要额外可训练模块，适合做 post-training 加速尝试。

### 中文锐评

这篇对 agent policy post-training 有间接价值：如果 OPD 的高效性来自早期方向可预测，那么 agent RL/蒸馏也可能利用类似 early trajectory 信号加速。但它主要还是 LLM post-training 分析，离复杂多轮 agent 的环境反馈、工具调用和 credit assignment 还有距离。
