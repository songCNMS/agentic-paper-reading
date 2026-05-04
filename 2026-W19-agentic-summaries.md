# Agentic LLM Paper Summaries 2026-W19

Source list: `2026-W19-agentic.md`

Process: arXiv PDFs were downloaded into `2026-W19-agentic-assets/pdfs/` and parsed into text under `2026-W19-agentic-assets/texts/`.

## 1. Learning while Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies

- **arXiv:** 2605.00416
- **Category:** Embodied / VLA agents
- **PDF:** `2026-W19-agentic-assets/pdfs/2605.00416.pdf`
- **Parsed text:** `2026-W19-agentic-assets/texts/2605.00416.txt`
- **Pages parsed:** 18
- **Parse status:** ok (downloaded)
- **Main innovation:** Fleet-scale continual post-training for generalist VLA robot policies, closing the loop between deployment, shared robot experience, human correction, value learning, and redeployment.
- **Agentic relevance:** Fleet-scale offline-to-online RL framework for continual improvement of deployed VLA robot policies using autonomous rollouts and human interventions.

### English Summary

The paper studies how a deployed fleet of robots can keep improving after offline pretraining. Learning While Deploying starts from a pretrained VLA policy, collects autonomous rollouts and human interventions from 16 dual-arm robots, then uses Distributional Implicit Value Learning and Q-learning via Adjoint Matching to update a flow-based action generator. Its agentic value is in the real deployment loop: long-horizon manipulation performance improves as the fleet accumulates experience, rather than relying only on a fixed demonstration dataset.

### 中文版本

这篇论文关注具身智能体真正上线后的持续学习问题。作者从一个预训练的 VLA 机器人策略出发，让多台双臂机器人在真实任务中收集自主执行轨迹和人工干预数据，再用价值学习和 Q-learning 方法做离线到在线的强化学习更新。它的重点不是做一个更大的离线数据集，而是把部署、收集经验、策略改进和再部署连成闭环，尤其适合长时程、分布变化明显的机器人任务。

### 中文锐评

这项工作很接近真实机器人智能体部署的核心问题，价值高于只在仿真里刷成功率的方案。但它的门槛也很高：需要机器人 fleet、人工干预流程和稳定的数据治理。论文效果如果要迁移到更开放的家庭或工业场景，关键不只是算法，还要看失败数据是否足够多样、奖励是否可扩展，以及持续更新是否会引入不可控的行为漂移。

## 2. From Skill Text to Skill Structure: The Scheduling-Structural-Logical Representation for Agent Skills

- **arXiv:** 2604.24026
- **Category:** Agent skill representation
- **PDF:** `2026-W19-agentic-assets/pdfs/2604.24026.pdf`
- **Parsed text:** `2026-W19-agentic-assets/texts/2604.24026.txt`
- **Pages parsed:** 22
- **Parse status:** ok (downloaded)
- **Main innovation:** A structured Scheduling-Structural-Logical representation for agent skills that separates invocation cues, execution structure, and concrete side effects.
- **Agentic relevance:** Structured representation for reusable agent skills, improving skill discovery and risk assessment over text-only skill artifacts.

### English Summary

The paper targets the problem that agent skills are usually stored as natural-language-heavy documents, making them hard to search, inspect, and assess for risk. It proposes SSL, a structured representation that captures scheduling signals, scene-level execution, and logic-level action/resource evidence. With an LLM-based normalizer, SSL improves skill discovery and risk assessment over text-only baselines, making skill libraries more machine-actionable for agents.

### 中文版本

这篇论文把 agent skill 从普通文本说明推进到结构化知识表示。它认为当前的 SKILL.md 或类似技能文件包含接口、控制流、约束、工具调用和副作用，但这些信息常常混在自然语言里，智能体很难可靠检索和审查。SSL 表示把调度信号、执行结构和动作/资源使用证据拆开，并用 LLM 做规范化，最终在技能发现和风险评估任务上优于纯文本方法。

### 中文锐评

方向很实用，因为技能库越大，纯文本检索和人工审查越不可控。不过 SSL 更像“技能文档的静态分析格式”，还不是完整的技能运行时。真正难点在于动态副作用、上下文依赖和工具 API 变化：如果结构化表示不能随执行反馈持续校准，它可能给人一种过度确定的安全感。

## 3. Map2World: Segment Map Conditioned Text to 3D World Generation

- **arXiv:** 2605.00781
- **Category:** Environment / world generation
- **PDF:** `2026-W19-agentic-assets/pdfs/2605.00781.pdf`
- **Parsed text:** `2026-W19-agentic-assets/texts/2605.00781.txt`
- **Pages parsed:** 31
- **Parse status:** ok (downloaded)
- **Main innovation:** Segment-map-conditioned text-to-3D world generation that improves controllability, scale consistency, and detail enhancement for large scenes.
- **Agentic relevance:** Generates controllable, scale-consistent 3D worlds that can support simulation and environment construction for embodied or autonomous agents.

### English Summary

Map2World builds 3D worlds from user-defined segment maps and text prompts, addressing limitations of grid-constrained layouts and inconsistent object scale. The system uses segment maps of arbitrary shape and scale, adds a detail enhancer network, and leverages asset-generator priors to generalize with limited data. For agentic LLM work, it is relevant as environment-building infrastructure for simulation, autonomous-driving worlds, and embodied-agent testing.

### 中文版本

Map2World 面向 3D 世界生成：用户给出任意形状和尺度的分割地图，再配合文本条件生成更一致的三维场景。论文重点解决现有方法受网格布局限制、物体尺度不一致和细节不足的问题，并通过 detail enhancer 与资产生成器先验提升场景质量。对 agentic LLM 来说，它更像环境构建工具，可用于具身智能体、自动驾驶仿真或交互式任务场景生成。

### 中文锐评

它对“环境生成”很有用，但还不是完整的智能体环境。可视一致性不等于可交互性，漂亮的 3D 世界如果缺少物理属性、任务状态、可操作对象和可验证反馈，对训练智能体的帮助有限。后续价值取决于它能否和仿真器、任务生成器、评测指标真正接起来。

## 4. Online Self-Calibration Against Hallucination in Vision-Language Models

- **arXiv:** 2605.00323
- **Category:** Agent safety / self-calibration
- **PDF:** `2026-W19-agentic-assets/pdfs/2605.00323.pdf`
- **Parsed text:** `2026-W19-agentic-assets/texts/2605.00323.txt`
- **Pages parsed:** 10
- **Parse status:** ok (downloaded)
- **Main innovation:** Online self-calibration for LVLM hallucination using Monte Carlo Tree Search, dual-granularity rewards, and iterative preference optimization.
- **Agentic relevance:** Uses Monte Carlo Tree Search, reward mechanisms, and online preference optimization to reduce hallucination in multimodal models used by autonomous agents.

### English Summary

The paper addresses hallucination in large vision-language models by exploiting the gap between stronger discriminative verification and weaker open-ended generation. OSCAR uses Monte Carlo Tree Search and a dual-granularity reward mechanism to construct preference data online, then refines the model with Direct Preference Optimization. It matters for agents because hallucinated visual state can cascade into bad plans and actions, especially in multimodal or embodied workflows.

### 中文版本

这篇论文处理 LVLM 的视觉幻觉问题。作者发现模型在判别式验证上通常比开放式生成更可靠，因此用 Monte Carlo Tree Search 和双粒度奖励机制在线构造偏好数据，再通过 DPO 迭代校准模型。它与智能体相关，因为多模态智能体如果看错环境状态，后续规划、工具调用和行动都会被错误感知放大。

### 中文锐评

MCTS 加奖励建模的自校准思路很有吸引力，但也可能把成本推高，而且奖励机制本身会决定模型学到什么。最需要警惕的是“自我验证闭环”：如果判别能力在某些视觉细节上也系统性失真，在线偏好数据可能只是把错误变得更稳定，而不是更真实。

## 5. Learning to Act and Cooperate for Distributed Black-Box Consensus Optimization

- **arXiv:** 2605.00691
- **Category:** Multi-agent systems
- **PDF:** `2026-W19-agentic-assets/pdfs/2605.00691.pdf`
- **Parsed text:** `2026-W19-agentic-assets/texts/2605.00691.txt`
- **Pages parsed:** 20
- **Parse status:** ok (reparsed with replacement for PDF surrogate text)
- **Main innovation:** LLM-guided trajectory-driven self-design for distributed multi-agent optimization, shaping both individual action behavior and cooperation patterns.
- **Agentic relevance:** LLM-guided framework for shaping internal actions and external cooperation patterns in distributed multi-agent optimization.

### English Summary

The paper studies distributed black-box consensus optimization, where agents optimize a global objective using local queries and limited neighbor communication. LAC-MAS adds adaptive swarm dynamics and uses LLMs to provide sparse high-level guidance from historical trajectories, shaping internal actions and external cooperation patterns. The result is a multi-agent optimization framework aimed at better exploration, convergence, and communication efficiency.

### 中文版本

这篇论文研究分布式黑盒共识优化：多个智能体只能做局部查询并通过有限邻居通信优化全局目标。LAC-MAS 在自适应群体动力学之上加入 LLM 的高层稀疏指导，根据历史轨迹调整智能体内部动作行为和外部协作模式。它的 agentic 价值在于把多智能体系统从固定手工规则推进到可由轨迹驱动调整的协作机制。

### 中文锐评

论文把 LLM 放进多智能体优化回路，思路新，但需要非常仔细地区分“LLM 真正在做有效策略抽象”还是“额外启发式带来的调参收益”。如果任务分布变化大，高层指导可能会变成不稳定噪声；如果任务分布固定，又要证明它比传统自适应优化规则更值得使用。

## 6. AnalogRetriever: Learning Cross-Modal Representations for Analog Circuit Retrieval

- **arXiv:** 2604.23195
- **Category:** Retrieval / domain agents
- **PDF:** `2026-W19-agentic-assets/pdfs/2604.23195.pdf`
- **Parsed text:** `2026-W19-agentic-assets/texts/2604.23195.txt`
- **Pages parsed:** 10
- **Parse status:** ok (downloaded)
- **Main innovation:** Tri-modal circuit retrieval over schematics, netlists, and functional descriptions, integrated as RAG infrastructure for the AnalogCoder agentic framework.
- **Agentic relevance:** Cross-modal retrieval dataset and model integrated into the AnalogCoder agentic framework as a retrieval-augmented generation module.

### English Summary

AnalogRetriever tackles analog circuit reuse across heterogeneous representations: SPICE netlists, schematics, and functional descriptions. It repairs and builds a higher-quality dataset, encodes schematics/descriptions with a vision-language model and netlists with a graph network, then aligns all modalities using contrastive learning. The agentic relevance is direct: when plugged into AnalogCoder as a retrieval-augmented module, it improves pass rates and helps solve tasks that were previously unsolved.

### 中文版本

AnalogRetriever 面向模拟电路设计中的跨模态检索问题，把 SPICE netlist、原理图和功能描述映射到同一嵌入空间。论文先修复并构建高质量数据集，再用视觉语言模型编码图和描述、用图神经网络编码 netlist，并通过对比学习对齐三种模态。它和智能体的关系很直接：作为 AnalogCoder agentic framework 的 RAG 模块，可以提升电路生成任务的通过率。

### 中文锐评

这是一个领域型 RAG 组件，优点是任务边界清楚、检索对象有结构。限制也明显：模拟电路设计的正确性高度依赖可编译、可仿真和工艺约束，检索相似 IP 只是第一步。真正的 agentic 系统还需要把检索、修改、仿真、错误定位和迭代修复闭环做稳。

## 7. Themis: Training Robust Multilingual Code Reward Models for Flexible Multi-Criteria Scoring

- **arXiv:** 2605.00754
- **Category:** Reward modeling / code agents
- **PDF:** `2026-W19-agentic-assets/pdfs/2605.00754.pdf`
- **Parsed text:** `2026-W19-agentic-assets/texts/2605.00754.txt`
- **Pages parsed:** 54
- **Parse status:** ok (downloaded)
- **Main innovation:** A multilingual, multi-criteria code reward-model benchmark, large preference dataset, and Themis-RM model suite for flexible scoring beyond functional correctness.
- **Agentic relevance:** Introduces code reward-model benchmarks and a large preference dataset for multi-criteria scoring, useful for training and evaluating coding agents.

### English Summary

Themis focuses on reward models for code generation, where existing work often over-relies on execution feedback and functional correctness. It introduces Themis-CodeRewardBench across five preference criteria and eight programming languages, profiles many reward models, builds a large open code-preference dataset, and trains multilingual Themis-RM models. For coding agents, this provides training and evaluation infrastructure for ranking code along dimensions such as quality, maintainability, and other non-execution criteria.

### 中文版本

Themis 研究代码生成中的奖励模型。现有代码 RM 往往只关注能否运行和功能正确性，但真实 coding agent 还需要考虑多语言、多标准偏好，例如可维护性、风格、鲁棒性和任务适配。论文提出 Themis-CodeRewardBench、构建大规模代码偏好数据集，并训练一组多语言、多标准代码奖励模型，为代码智能体的训练和测试时打分提供基础设施。

### 中文锐评

多标准代码 RM 很有必要，因为 coding agent 不能只靠测试通过率。但偏好数据也容易把主观风格固化成奖励，甚至压制简洁但不符合模板的正确方案。更关键的是，RM 如果不能和真实执行、静态分析、代码审查反馈结合，很可能只是在“看起来像好代码”的维度上打高分。
