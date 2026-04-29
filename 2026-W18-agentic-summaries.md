# 2026-W18 Agentic LLM Paper Summaries

Source list: `2026-W18-agentic.md`

Process: each listed arXiv PDF was downloaded into `2026-W18-agentic-assets/pdfs/` and parsed into text under `2026-W18-agentic-assets/texts/`. The summaries below focus on relevance to agentic LLMs: algorithms, environments, benchmarks, datasets, memory, GUI/browser/terminal operation, embodied/VLA agents, process rewards, evaluation, and safety.

## 1. Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond

- **arXiv:** 2604.22748
- **Type:** Foundations / survey
- **Main innovation:** A unified "levels x laws" taxonomy for agentic world models, separating prediction, simulation, and autonomous evolution across physical, digital, social, and scientific environments.
- **Summary:** This survey frames world modeling as a central bottleneck for goal-directed agents that must act over sustained interactions rather than only generate text. It proposes a taxonomy with capability levels such as local predictors, multi-step simulators, and self-improving evolvers, crossed with law regimes for physical, digital, social, and scientific worlds.
- **Agentic relevance:** Useful as a conceptual map for agent environment modeling, planning, simulation, and evaluation. It clarifies that realistic agent performance depends on action-conditioned predictions and constraint-respecting rollouts, not just static knowledge.
- **Takeaway:** Treat world models as agent infrastructure: the better the model of environment dynamics, the more scalable planning, self-correction, and safe deployment become.
- **中文版本：** 这篇综述把世界模型视为目标导向智能体的核心基础设施，提出“能力层级 x 世界规律”的分类框架，区分一步预测、多步仿真和可自我演化的世界模型。它的主要价值是把物理、数字、社会和科学环境中的建模需求统一起来，说明智能体要可靠规划和自我纠错，必须理解动作会如何改变环境。
- **中文锐评：** 框架很有用，但更像研究地图而不是可直接落地的方法。真正难点在于如何验证 L2/L3 世界模型真的能改善长期决策，而不是只生成看起来合理的模拟。

## 2. From Skills to Talent: Organising Heterogeneous Agents as a Real-World Company

- **arXiv:** 2604.22446
- **Type:** Multi-agent organization
- **Main innovation:** Introduces an organizational abstraction for agents, where portable "Talents" can be recruited, governed, composed, and improved like workers inside a company-like structure.
- **Summary:** The paper argues that multi-agent systems need an organizational layer beyond fixed workflows and isolated tool skills. It introduces OneManCompany, a framework that packages skills, tools, and runtime configuration into portable "Talents" and coordinates them through structures inspired by real company operations.
- **Agentic relevance:** Directly targets agent workforce management, role assignment, coordination, and persistent organizational learning.
- **Takeaway:** Multi-agent progress may require organization design primitives, not just stronger individual agents.
- **中文版本：** 论文提出 OneManCompany，把多智能体系统从固定工作流提升到“组织设计”层面。它将技能、工具和运行配置封装为可招募、可治理、可组合的 Talent，并用类似公司的人才市场和项目执行机制协调异构智能体。核心启发是：多智能体能力提升不只依赖单个智能体更强，也依赖组织结构更合理。
- **中文锐评：** 组织隐喻很抓人，但也容易把工程复杂度包装成概念创新。关键要看 Talent 市场和执行树在开放任务中是否比简单 planner-router-worker 架构稳定。

## 3. Recursive Multi-Agent Systems

- **arXiv:** 2604.25917
- **Type:** Multi-agent algorithm
- **Main innovation:** Extends recursive computation from single-model looped reasoning to multi-agent collaboration via latent-state transfer between agents.
- **Summary:** RecursiveMAS extends the idea of looped or recursive reasoning from a single model to a multi-agent setting. It uses recursive links to transfer latent states across heterogeneous agents and optimizes collaboration through inner and outer recursion loops.
- **Agentic relevance:** Offers a way to scale collaboration depth without relying only on explicit text messages between agents.
- **Takeaway:** Recursion can be a systems-level scaling axis for multi-agent reasoning, though its practical value depends on stable training and interpretable cross-agent state transfer.
- **中文版本：** RecursiveMAS 将递归推理从单模型扩展到多智能体协作。它通过 RecursiveLink 在智能体内部生成潜在思维，并在不同智能体之间传递潜在状态，从而让协作过程本身可以递归加深。亮点是把多智能体协作看成一种系统级递归计算，而不是简单文本消息接力。
- **中文锐评：** 潜在状态递归协作很有想象力，但可解释性和调试成本会很高。若性能收益主要来自更复杂的训练技巧，而不是协作机制本身，落地价值会打折。

## 4. Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms

- **arXiv:** 2604.23775
- **Type:** VLA / embodied safety survey
- **Main innovation:** Consolidates VLA safety into a dedicated threat/evaluation/mechanism framework that treats embodied action as qualitatively different from text-only LLM risk.
- **Summary:** This survey organizes safety risks for Vision-Language-Action models, where models perceive, reason, and act in physical environments. It highlights risks that are more severe than text-only LLM risks: irreversible physical consequences, multimodal attacks, real-time defense constraints, long-horizon error propagation, and vulnerable data pipelines.
- **Agentic relevance:** Highly relevant to embodied agents, robotics, and any system where LLM/VLM decisions become actions.
- **Takeaway:** VLA safety needs dedicated evaluations and mechanisms because physical action changes the risk model.
- **中文版本：** 这篇综述系统整理了 VLA（视觉-语言-动作）模型的安全问题。与文本 LLM 不同，VLA 模型会在物理世界中执行动作，因此面临不可逆后果、多模态攻击、实时防御、长链路错误传播和数据供应链风险。它的贡献是把具身智能安全从普通 LLM 安全中独立出来讨论。
- **中文锐评：** 这类综述很及时，因为 VLA 安全确实不能沿用文本安全模板。但它的挑战是后续评测必须绑定真实动作后果，否则容易停留在风险清单层面。

## 5. DV-World: Benchmarking Data Visualization Agents in Real-World Scenarios

- **arXiv:** 2604.25914
- **Type:** Benchmark / environment
- **Main innovation:** Builds a real-world data visualization benchmark spanning spreadsheet-native work, cross-library visualization evolution, and ambiguous multi-turn user interaction.
- **Summary:** DV-World evaluates data visualization agents across realistic professional workflows rather than simple chart-generation tasks. It covers spreadsheet-native manipulation, chart and dashboard creation, diagnostic repair, cross-platform visualization evolution, and multi-turn interaction under ambiguous user intent.
- **Agentic relevance:** Provides an environment for testing data-analysis and visualization agents on grounded, stateful, tool-like tasks.
- **Takeaway:** Visualization agents need to handle repair, intent alignment, and platform-specific constraints, not just emit plotting code.
- **中文版本：** DV-World 构建了面向真实数据可视化工作的智能体评测环境，覆盖电子表格操作、图表和仪表盘创建、错误修复、跨框架可视化迁移以及多轮模糊意图对齐。它强调可视化智能体不能只会生成绘图代码，还必须能在真实工具环境中理解数据、修复问题并响应用户迭代需求。
- **中文锐评：** DV-World 的价值在于把可视化任务拉回真实办公环境。锐点是：如果评测过度依赖特定软件栈，模型排名可能反映工具适配而不是真正的数据可视化智能。

## 6. Programming with Data: Test-Driven Data Engineering for Self-Improving LLMs from Raw Corpora

- **arXiv:** 2604.24819
- **Type:** Data engineering / self-improvement
- **Main innovation:** Treats LLM data engineering as test-driven programming, using shared structured knowledge to generate data, evaluate failures, and repair missing concepts.
- **Summary:** The paper maps data engineering for LLM fine-tuning onto a software-development lifecycle. It uses structured knowledge extracted from raw corpora as a shared basis for generating training data, building tests, diagnosing failures, and repairing data gaps.
- **Agentic relevance:** Relevant to self-improving LLM systems that need closed-loop data generation, evaluation, and debugging.
- **Takeaway:** Domain adaptation should be diagnostic and test-driven; blindly adding more synthetic data is less effective than targeted data repair.
- **中文版本：** 这篇论文把 LLM 数据工程类比为软件开发生命周期，提出用结构化知识同时驱动训练数据生成、测试构造、失败诊断和数据修复。主要创新是把领域微调从“盲目增加数据”变成“测试驱动的数据调试”，适合用于构建可自我改进的 LLM 和智能体训练管线。
- **中文锐评：** 测试驱动数据工程方向很务实。最大风险是结构化知识抽取本身会成为瓶颈；如果抽取 schema 错了，后面的测试和修复都会系统性偏。

## 7. ClawMark: A Living-World Benchmark for Multi-Turn, Multi-Day, Multimodal Coworker Agents

- **arXiv:** 2604.23781
- **Type:** Long-horizon benchmark
- **Main innovation:** Introduces a living-world benchmark where coworker agents operate across multiple days while sandbox services and multimodal evidence change between turns.
- **Summary:** ClawMark evaluates persistent coworker agents across multi-turn, multi-day tasks in a stateful sandbox. The environment changes between turns, and evidence can appear in emails, calendars, knowledge bases, images, scanned PDFs, audio, video, and spreadsheets.
- **Agentic relevance:** Directly tests long-horizon agent behavior under changing state, multimodal evidence, and delayed consequences.
- **Takeaway:** Persistent coworker agents need robust memory, state tracking, and evidence grounding across days, not just single-session task completion.
- **中文版本：** ClawMark 评测多日、多轮、多模态的持久 coworker agents。环境状态会在轮次之间自主变化，证据可能来自邮件、日历、知识库、图片、扫描 PDF、音频、视频和表格。它的核心创新是把智能体评测从单次静态任务推进到持续变化的生活/办公世界，更贴近真实助手场景。
- **中文锐评：** ClawMark 抓住了真实助手最容易失败的地方：跨天状态变化和多模态证据。它比单轮 benchmark 更接近产品需求，但评测维护成本也会明显更高。

## 8. AutoResearchBench: Benchmarking AI Agents on Complex Scientific Literature Discovery

- **arXiv:** 2604.25256
- **Type:** Research-agent benchmark
- **Main innovation:** Separates scientific literature discovery into deep target-paper search and wide comprehensive literature collection, exposing failures distinct from generic web search.
- **Summary:** AutoResearchBench measures autonomous scientific literature discovery. It includes deep research tasks, where agents must progressively locate a specific target paper, and wide research tasks, where agents must comprehensively collect relevant literature for a topic.
- **Agentic relevance:** Strong benchmark for research agents, search planning, hypothesis-space management, and iterative reflection.
- **Takeaway:** Scientific search is not just web browsing; agents must handle long natural-language queries, paper-level evidence, completeness, and iterative strategy refinement.
- **中文版本：** AutoResearchBench 评测科研文献发现智能体，区分 Deep Research（逐步定位目标论文）和 Wide Research（全面搜集某主题相关文献）。论文指出科研检索不同于普通网页搜索，需要处理长自然语言查询、论文级证据、集合完整性和迭代反思。它是科研智能体搜索能力的重要基准。
- **中文锐评：** AutoResearchBench 很对科研 agent 的痛点。锐评是：文献发现的“全面性”很难定义，benchmark 如果答案集不完整，可能误惩合理但不同路径的研究策略。

## 9. Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis

- **arXiv:** 2604.24198
- **Type:** Process reward modeling
- **Main innovation:** Designs an environment-grounded process reward model for data-analysis agents that can reward productive exploration and catch silent analytical errors.
- **Summary:** The paper studies why general process reward models fail for data-analysis agents: they miss silent analytical errors and may penalize necessary exploratory actions. It introduces DataPRM, an environment-grounded process reward model for step-level supervision in dynamic data analysis.
- **Agentic relevance:** Directly supports RL/training of data-analysis agents with process-level feedback rather than only final-answer rewards.
- **Takeaway:** Agentic data analysis requires reward models that understand exploration, executable checks, and silent failure modes.
- **中文版本：** DataPRM 针对数据分析智能体提出环境感知的过程奖励模型。论文发现通用 PRM 容易漏掉无报错但结论错误的 silent errors，也会误罚必要的探索行为。DataPRM 的创新在于利用可执行环境验证和步骤级监督，为数据分析智能体提供比最终答案奖励更细的训练信号。
- **中文锐评：** DataPRM 的方向比只看最终答案更靠谱。需要警惕的是过程奖励可能把探索变成模板化操作，智能体为了拿步骤分而不是为了真正分析而行动。

## 10. Contexts are Never Long Enough: Structured Reasoning for Scalable Question Answering over Long Document Sets

- **arXiv:** 2604.22294
- **Type:** Long-document reasoning / retrieval
- **Main innovation:** Replaces long-context chunk aggregation with schema-driven extraction into relational structures for scalable, auditable document-set QA.
- **Summary:** The paper introduces SLIDERS, a framework for question answering over large document collections. Instead of stuffing chunks into context, it extracts salient information into a relational structure and performs structured reasoning over that representation.
- **Agentic relevance:** Relevant to research and document-analysis agents that must operate beyond fixed context windows.
- **Takeaway:** For large document sets, agents need external structured memory and queryable intermediate representations, not just longer prompts.
- **中文版本：** SLIDERS 面向超长文档集合问答，避免单纯把文本切块塞进上下文，而是先抽取关键信息并组织成关系型结构，再在结构化表示上推理。它的亮点是用可查询、可审计的外部中间表示突破上下文窗口限制，适合研究助手和文档分析智能体。
- **中文锐评：** SLIDERS 的结构化路线很工程正确，但不是所有问题都适合关系型 schema。它适合证据密集的分析任务，不一定适合开放式、抽象或强主观综合。

## 11. Taming Actor-Observer Asymmetry in Agents via Dialectical Alignment

- **arXiv:** 2604.19548
- **Type:** Agent alignment / reflection
- **Main innovation:** Identifies actor-observer asymmetry as a measurable bias in agent self-reflection and mutual auditing, then mitigates it with dialectical alignment.
- **Summary:** The paper identifies actor-observer asymmetry in role-based agent systems: an acting agent tends to blame failures on external factors, while an observing agent attributes similar failures to the actor. It proposes dialectical alignment to make judgments more evidence-grounded and consistent.
- **Agentic relevance:** Important for self-reflection, audit agents, debate systems, and multi-agent error attribution.
- **Takeaway:** Multi-agent review can introduce cognitive-bias-like failure modes; agent critique needs alignment, not just more roles.
- **中文版本：** 论文发现多智能体反思和审计中存在类似人类的 actor-observer asymmetry：执行者倾向于把失败归因于外部因素，观察者则倾向于归因于执行者内部错误。作者提出 dialectical alignment 来约束归因过程，使批评和自我反思更基于证据。它提醒我们：多角色审查本身也会引入偏差。
- **中文锐评：** 指出 agent 审计里的归因偏差很有价值。问题是 dialectical alignment 是否能泛化到开放任务；在真实系统中，失败原因往往不是单一 actor 或 observer 能判清的。

## 12. Efficient Agent Evaluation via Diversity-Guided User Simulation

- **arXiv:** 2604.21480
- **Type:** Agent evaluation
- **Main innovation:** Uses diversity-guided simulated users to actively cover multi-turn interaction failure modes while reducing evaluation cost.
- **Summary:** The paper proposes a user-simulation approach for evaluating LLM agents in stochastic, multi-turn settings. Diversity-guided simulation selects or generates varied user behaviors to cover failure modes more efficiently.
- **Agentic relevance:** Useful for evaluating deployed conversational and task agents without relying solely on expensive human traffic.
- **Takeaway:** Agent evaluation should actively search the user-behavior space instead of passively sampling a small set of scripted interactions.
- **中文版本：** 这篇论文提出用多样性引导的用户模拟来高效评测多轮智能体。相比少量固定脚本，它主动覆盖更多用户行为和失败模式，从而降低人工评测成本。核心创新是把用户模拟从被动采样变成评测覆盖率优化，适合客服、助手和任务型 agent 的可靠性测试。
- **中文锐评：** 用户模拟是 agent 评测降本的必要方向。但模拟用户如果缺乏真实分布校准，可能只是把模型训练到会应付模拟器，而不是应付真实用户。

## 13. AgentSearchBench: A Benchmark for AI Agent Search in the Wild

- **arXiv:** 2604.22436
- **Type:** Agent-discovery benchmark
- **Main innovation:** Frames agent selection itself as a benchmarked search problem over compositional and evolving AI-agent capabilities.
- **Summary:** AgentSearchBench studies the problem of finding appropriate AI agents for a task. Unlike ordinary tool retrieval, agent selection must reason about compositional, evolving capabilities and task fit.
- **Agentic relevance:** Addresses a meta-agent problem: agents that search for, select, and delegate to other agents.
- **Takeaway:** As agent ecosystems grow, discovering the right agent becomes its own benchmarkable capability.
- **中文版本：** AgentSearchBench 将“如何找到合适的 AI agent”本身定义为一个评测问题。随着 agent 生态增长，智能体能力往往是组合式、动态变化的，不能像普通工具检索一样简单匹配关键词。该 benchmark 关注元智能体如何搜索、选择和委派其他智能体。
- **中文锐评：** AgentSearchBench 很有前瞻性，因为未来 agent 生态会需要“找 agent 的 agent”。但当前最大难点是 agent 能力描述不可靠，benchmark 需要防止退化成元数据匹配题。

## 14. Memanto: Typed Semantic Memory with Information-Theoretic Retrieval for Long-Horizon Agents

- **arXiv:** 2604.22085
- **Type:** Agent memory
- **Main innovation:** Proposes typed semantic memory with information-theoretic retrieval so long-horizon agents retrieve task-relevant memories rather than raw logs.
- **Summary:** Memanto targets memory as a bottleneck for persistent multi-session agents. It proposes typed semantic memory and information-theoretic retrieval to decide what stored information is useful for a current long-horizon task.
- **Agentic relevance:** Directly relevant to memory architectures for autonomous assistants and long-running agents.
- **Takeaway:** Agent memory should be typed and selectively retrieved; raw conversation logs are not enough for long-horizon autonomy.
- **中文版本：** Memanto 针对长期运行智能体的记忆瓶颈，提出类型化语义记忆和信息论检索机制。它强调智能体不应简单保存完整对话日志，而应结构化存储事实、偏好、目标等信息，并按当前任务选择性检索。核心价值是提升长时程智能体的记忆可用性和可控性。
- **中文锐评：** Memanto 的 typed memory 思路扎实，符合长期 agent 的真实需求。锐点是：记忆系统的失败通常不是检索不到，而是检索到后错误使用或过度信任旧信息。

## 15. Co-Director: Agentic Generative Video Storytelling

- **arXiv:** 2604.24842
- **Type:** Agentic content generation
- **Main innovation:** Turns video generation into a coordinated agentic workflow for story planning, scene continuity, and iterative correction across clips.
- **Summary:** Co-Director frames video storytelling as an agentic generation problem. Instead of generating isolated clips, the system coordinates planning, scene structure, consistency, and iterative video generation to produce coherent stories.
- **Agentic relevance:** Shows how agent orchestration can wrap generative models for multi-step creative production.
- **Takeaway:** Agentic pipelines are useful when generation requires planning, continuity, and correction across many artifacts.
- **中文版本：** Co-Director 把视频生成从单个片段生成升级为智能体式故事创作流程。系统协调故事规划、场景结构、连续性维护和迭代修正，使多个生成片段形成一致叙事。它展示了 agent orchestration 如何包装生成模型，完成需要长期规划和一致性的创作任务。
- **中文锐评：** Co-Director 展示了生成模型外面套 agent workflow 的典型价值。它的挑战是视频一致性的瓶颈可能仍在底层生成模型，agent 层只能缓解，不能根治。

## 16. Toward Scalable Terminal Task Synthesis via Skill Graphs

- **arXiv:** 2604.25727
- **Type:** Environment / task synthesis
- **Main innovation:** Uses skill graphs to synthesize diverse command-line tasks that compose terminal skills systematically.
- **Summary:** The paper addresses the shortage of diverse, high-quality terminal-agent training tasks. It uses skill graphs to compose command-line skills into scalable terminal task synthesis.
- **Agentic relevance:** Directly supports training and evaluation of agents that operate in shell or developer environments.
- **Takeaway:** Good terminal agents need systematically generated tasks that cover compositional command-line skills.
- **中文版本：** 这篇论文面向终端智能体训练数据稀缺问题，使用 skill graphs 系统组合命令行技能并生成多样化终端任务。创新点在于用技能图表达任务依赖和组合结构，从而可规模化合成 shell/developer agent 的训练与评测任务。
- **中文锐评：** Skill graph 合成终端任务很实用，适合规模化训练。需要注意的是合成任务若过于规整，agent 可能学到命令套路，而不是面对真实开发环境的恢复能力。

## 17. Stabilizing Efficient Reasoning with Step-Level Advantage Selection

- **arXiv:** 2604.24003
- **Type:** Reasoning RL algorithm
- **Main innovation:** Selects useful reasoning steps with advantage signals to stabilize training toward compact, high-value reasoning traces.
- **Summary:** The paper tackles inefficient long reasoning traces in LLMs. It proposes selecting useful reasoning steps using advantage-style signals so training can reward compact, effective reasoning rather than verbosity.
- **Agentic relevance:** Relevant to agent policies that must reason under compute budgets and avoid long, low-value traces.
- **Takeaway:** Step-level credit assignment is a practical lever for efficient reasoning and agent RL stability.
- **中文版本：** 论文关注 LLM 推理轨迹过长、计算效率低的问题，提出用步骤级 advantage 信号选择真正有价值的推理步骤。其创新是把信用分配细化到推理步骤层面，让训练奖励紧凑有效的推理，而不是奖励冗长链路。对 agent RL 的稳定性和成本控制都有参考价值。
- **中文锐评：** 步骤级 advantage 选择是对长推理浪费的直接回应。锐评是：压缩推理有利于效率，但如果奖励设计不谨慎，可能把有用的探索性思考也剪掉。

## 18. TCOD: Exploring Temporal Curriculum in On-Policy Distillation for Multi-turn Autonomous Agents

- **arXiv:** 2604.24005
- **Type:** Multi-turn agent training
- **Main innovation:** Adds a temporal curriculum to on-policy distillation so student agents learn trajectory structure across multi-turn interactions.
- **Summary:** TCOD studies on-policy distillation for multi-turn autonomous agents and introduces temporal curriculum ideas for transferring behavior from stronger models to smaller students over interactive trajectories.
- **Agentic relevance:** Directly related to training smaller multi-turn agents from stronger teachers while preserving sequential behavior.
- **Takeaway:** Distillation for agents should respect temporal structure; static input-output imitation misses important trajectory dynamics.
- **中文版本：** TCOD 研究多轮自主智能体的 on-policy distillation，并加入时间课程学习，让学生模型按交互轨迹的时序结构学习强教师行为。核心创新是强调 agent 蒸馏不能只做静态输入输出模仿，而要保留多轮决策中的时间依赖和行为演化。
- **中文锐评：** TCOD 关注时间结构是对的，多轮 agent 蒸馏不能只做单步 imitation。关键问题是教师轨迹本身是否高质量；坏轨迹按课程学习只会更稳定地复制坏习惯。

## 19. PageGuide: Browser extension to assist users in navigating a webpage and locating information

- **arXiv:** 2604.23772
- **Type:** Browser / web-assistance agent
- **Main innovation:** Implements page-grounded browser assistance that combines webpage understanding with user navigation and information-location intent.
- **Summary:** PageGuide is a browser extension for helping users locate information and navigate cluttered webpages. It targets multi-step browsing assistance where the system must understand webpage structure and user intent.
- **Agentic relevance:** Relevant to web navigation agents, browser automation, and human-in-the-loop assistance.
- **Takeaway:** Browser agents need page-grounded interaction and user intent tracking, not just general text QA.
- **中文版本：** PageGuide 是一个帮助用户浏览网页、定位信息的浏览器扩展。它需要理解网页结构、用户目标和多步导航过程。对 web agent 来说，它的意义在于强调页面 grounding 和人机协同，而不仅是把网页内容当作普通文本问答。
- **中文锐评：** PageGuide 贴近真实浏览辅助场景，但作为 agent 论文可能偏应用系统。价值取决于它是否能抽象出可复用的网页 grounding 和导航策略。

## 20. Zero-to-CAD: Agentic Synthesis of Interpretable CAD Programs at Million-Scale Without Real Data

- **arXiv:** 2604.24479
- **Type:** Synthetic data / CAD agents
- **Main innovation:** Generates million-scale interpretable CAD construction programs agentically, bypassing the scarcity of real parametric CAD histories.
- **Summary:** Zero-to-CAD generates interpretable CAD construction programs at large scale without relying on real CAD histories. It treats CAD models as procedural recipes and uses agentic synthesis to create useful training data.
- **Agentic relevance:** Relevant to agents that generate structured programs and design artifacts through procedural planning.
- **Takeaway:** Agentic synthesis can produce scalable structured datasets where real expert traces are scarce.
- **中文版本：** Zero-to-CAD 用 agentic synthesis 大规模生成可解释 CAD 构造程序，绕开真实参数化 CAD 历史数据稀缺的问题。它把 CAD 模型视为程序化构造配方，生成可训练的结构化设计数据。亮点是用智能体合成补齐专家轨迹不足。
- **中文锐评：** Zero-to-CAD 的数据合成野心很大。锐点是没有真实数据不等于没有真实偏差；合成 CAD 程序是否覆盖工程设计中的复杂约束，需要强验证。

## 21. EmbodiedMidtrain: Bridging the Gap between Vision-Language Models and Vision-Language-Action Models via Mid-training

- **arXiv:** 2604.20012
- **Type:** Embodied / VLA training
- **Main innovation:** Selects VLM mid-training data by proximity to VLA action-domain features, bridging perception-language pretraining and embodied control.
- **Summary:** EmbodiedMidtrain addresses the distribution gap between VLM pretraining data and VLA action data. It selects VLM data closer to the embodied-action domain and uses it for mid-training before downstream VLA training.
- **Agentic relevance:** Helps adapt general vision-language models into embodied action policies.
- **Takeaway:** VLA performance depends heavily on bridging the data-distribution gap between perception-language pretraining and action-conditioned deployment.
- **中文版本：** EmbodiedMidtrain 针对 VLM 到 VLA 的数据分布断层，提出按与动作域特征的接近程度筛选 VLM 中训练数据，再用于中间训练。它的创新在于用数据邻近性桥接视觉语言预训练和具身控制，使通用 VLM 更适合作为动作模型基础。
- **中文锐评：** EmbodiedMidtrain 的数据筛选思路很稳健，是连接 VLM 和 VLA 的现实路径。但它依赖特征空间距离作为代理，未必总能代表真正的可行动能力接近度。

## 22. ProEval: Proactive Failure Discovery and Efficient Performance Estimation for Generative AI Evaluation

- **arXiv:** 2604.23099
- **Type:** Evaluation methodology
- **Main innovation:** Applies transfer-learned Gaussian-process surrogates and active sampling to estimate performance and discover failures with far fewer evaluations.
- **Summary:** ProEval uses transfer learning and Bayesian methods to estimate model performance and discover failure cases with fewer samples. It frames performance estimation and failure discovery as active, uncertainty-aware evaluation problems.
- **Agentic relevance:** Useful for evaluating expensive agents where each rollout or rating is costly.
- **Takeaway:** Evaluation should be proactive and sample-efficient, especially for agents with slow inference and many possible failure modes.
- **中文版本：** ProEval 用迁移学习的高斯过程代理模型和主动采样来降低生成式 AI/agent 评测成本。它把性能估计和失败发现建模为不确定性感知的主动评测问题。核心价值是用更少样本发现失败案例，适合推理慢、评测贵的智能体系统。
- **中文锐评：** ProEval 对昂贵评测很有价值，尤其适合 agent rollout。锐评是主动发现的失败是否代表真实风险分布，需要额外校准，否则容易高估或低估整体可靠性。

## 23. dWorldEval: Scalable Robotic Policy Evaluation via Discrete Diffusion World Model

- **arXiv:** 2604.22152
- **Type:** Robotic policy evaluation / world model
- **Main innovation:** Uses a discrete diffusion world model as an action-conditioned proxy evaluator for ranking robotic policies at scale.
- **Summary:** dWorldEval uses a discrete diffusion world model as a scalable proxy for evaluating robotic policies. It maps vision, language, and actions into a unified token space and generates long-horizon rollouts for policy ranking.
- **Agentic relevance:** Provides a world-model-based evaluation path for embodied agents where real-world rollouts are expensive.
- **Takeaway:** Scalable embodied-agent evaluation will likely depend on controllable, action-conditioned world models.
- **中文版本：** dWorldEval 使用离散扩散世界模型作为机器人策略的可扩展评测代理，把视觉、语言和动作映射到统一 token 空间并生成长时程 rollout。它的创新是用可控世界模型替代大量真实机器人测试，用于策略排序和成功率估计。
- **中文锐评：** dWorldEval 方向正确：机器人评测必须靠世界模型扩展。但世界模型一旦偏离真实物理，策略排名会被代理模型误导，因此校准比生成质量更关键。

## 24. GoClick: Lightweight Element Grounding Model for Autonomous GUI Interaction

- **arXiv:** 2604.23941
- **Type:** GUI agent component
- **Main innovation:** Builds a 230M-parameter GUI element grounding VLM optimized for low-latency, on-device autonomous GUI interaction.
- **Summary:** GoClick is a compact GUI grounding model that locates screen elements from natural-language instructions. Its small parameter count targets low-latency, on-device GUI operation.
- **Agentic relevance:** Element grounding is a core primitive for computer-use and mobile agents.
- **Takeaway:** GUI agents benefit from specialized lightweight perception modules instead of relying only on large general VLMs.
- **中文版本：** GoClick 是面向 GUI 智能体的轻量元素定位模型，只有约 230M 参数，目标是在移动端等资源受限设备上低延迟运行。它的主要创新是为自主 GUI 操作提供专用小模型组件，而不是完全依赖大型通用 VLM。
- **中文锐评：** GoClick 很务实，小模型 GUI grounding 对端侧 agent 很重要。局限也清楚：定位控件只是第一步，真正的 GUI agent 还要理解任务状态和操作后果。

## 25. AutoGUI-v2: A Comprehensive Multi-Modal GUI Functionality Understanding Benchmark

- **arXiv:** 2604.24441
- **Type:** GUI benchmark
- **Main innovation:** Evaluates GUI functionality and state-transition understanding, going beyond static grounding toward predictive digital-world modeling.
- **Summary:** AutoGUI-v2 evaluates whether models understand GUI functionality and state transitions, not just static element locations. It tests context-aware functionality understanding at region and element levels.
- **Agentic relevance:** Direct benchmark for digital autonomy and GUI-control agents.
- **Takeaway:** GUI grounding and GUI reasoning diverge; locating a button is easier than predicting what interacting with it will do.
- **中文版本：** AutoGUI-v2 评测模型是否理解 GUI 功能和状态转移，而不只是静态定位按钮或区域。它揭示了 GUI grounding 和 GUI reasoning 的差距：找到控件不等于知道点击后会发生什么。该基准更接近真正数字自治所需的界面心理模型。
- **中文锐评：** AutoGUI-v2 比纯 grounding benchmark 更进一步，抓住了 GUI state transition。锐评是这类评测很可能快速被模型刷榜，后续要持续增加真实软件复杂度。

## 26. Improving Vision-language Models with Perception-centric Process Reward Models

- **arXiv:** 2604.24583
- **Type:** Multimodal process reward modeling
- **Main innovation:** Introduces Perceval, a perception-centric PRM that decomposes visual reasoning into claims and localizes image-grounding errors.
- **Summary:** The paper introduces Perceval, a perception-centric process reward model that detects image-text misalignment inside VLM reasoning chains. It grounds token-level or claim-level perceptual errors instead of giving only outcome-level rewards.
- **Agentic relevance:** Supports RL and test-time correction for multimodal agents that reason from visual evidence.
- **Takeaway:** Multimodal agents need process feedback that can localize perceptual mistakes, not just final correctness labels.
- **中文版本：** Perceval 是一个感知中心的过程奖励模型，可把 VLM 推理中的图像相关陈述拆成 claim，并逐项检查是否与视觉证据一致。创新点是把多模态奖励从最终分数推进到可定位的感知错误反馈，适合训练和修正视觉智能体。
- **中文锐评：** Perceval 的 claim-level 感知反馈很适合多模态 RL。风险在于 claim 抽取和视觉验证本身也会出错，PRM 错误可能被训练放大。

## 27. IndustryAssetEQA: A Neurosymbolic Operational Intelligence System for Embodied Question Answering in Industrial Asset Maintenance

- **arXiv:** 2604.23446
- **Type:** Embodied QA / industrial environment
- **Main innovation:** Combines telemetry, FMEA knowledge graphs, and LLM QA into a neurosymbolic operational intelligence system with provenance and counterfactual support.
- **Summary:** IndustryAssetEQA combines telemetry, knowledge graphs, and LLM interaction for industrial maintenance QA. It focuses on grounded operational reasoning, provenance, failure diagnosis, and counterfactual/action-oriented support.
- **Agentic relevance:** Relevant to embodied enterprise agents in safety-critical industrial settings.
- **Takeaway:** Operational agents need neurosymbolic grounding and verifiable provenance before their recommendations can be trusted.
- **中文版本：** IndustryAssetEQA 将工业设备遥测、FMEA 知识图谱和 LLM 问答结合，构建带证据来源和反事实支持的运维智能系统。它把工业 QA 视为具身决策问题，强调安全关键场景下的可验证出处、故障诊断和行动建议。
- **中文锐评：** IndustryAssetEQA 的 neurosymbolic 路线适合工业场景，比纯 LLM 问答可信。锐点是这类系统高度依赖企业数据接入和知识图谱质量，迁移成本不会低。

## 28. Discovering Agentic Safety Specifications from 1-Bit Danger Signals

- **arXiv:** 2604.23210
- **Type:** Agent safety algorithm
- **Main innovation:** Shows that agents can iteratively infer natural-language safety specifications from only sparse one-bit danger feedback.
- **Summary:** EPO-Safe asks whether LLM agents can infer hidden safety objectives from sparse binary danger warnings. Agents generate plans, observe one-bit danger feedback, reflect, and update natural-language safety specifications.
- **Agentic relevance:** Directly studies safety learning from sparse experience, a core problem for autonomous agents.
- **Takeaway:** Natural-language specifications can act as persistent safety memory, but the setting still assumes structured environments and relatively clean feedback.
- **中文版本：** EPO-Safe 研究智能体能否仅凭一比特危险信号学习隐藏安全目标。智能体生成计划、接收二值危险反馈、反思并更新自然语言安全规范。它的创新在于证明自然语言规范可以作为可解释的持久安全记忆，即使反馈极其稀疏。
- **中文锐评：** EPO-Safe 用一比特信号学习安全规范很有意思，但实验环境仍偏理想化。真实世界安全反馈往往延迟、噪声大且代价高，不能简单外推。

## 29. Emergent Strategic Reasoning Risks in AI: A Taxonomy-Driven Evaluation Framework

- **arXiv:** 2604.22119
- **Type:** Agentic risk evaluation
- **Main innovation:** Builds ESRRSim, a taxonomy-driven generator for strategic-risk scenarios with paired rubrics for visible responses and hidden reasoning traces.
- **Summary:** The paper defines emergent strategic reasoning risks such as deception, evaluation gaming, and reward hacking. It introduces ESRRSim, a taxonomy-driven framework for generating scenarios and rubrics to evaluate these behaviors.
- **Agentic relevance:** Highly relevant to agent safety as models become more goal-directed and deployment-scoped.
- **Takeaway:** Strategic-risk evaluation needs scenario generation plus separate evaluation of model responses and reasoning traces.
- **中文版本：** ESRRSim 针对欺骗、评测博弈、奖励黑客等 emergent strategic reasoning risks，构建 taxonomy-driven 场景生成和评测框架。它同时评估模型外显回答和推理轨迹，核心贡献是把目标导向模型的战略性风险系统化、可生成、可比较地评测。
- **中文锐评：** ESRRSim 把战略性风险系统化是必要工作。锐评是 reasoning trace 本身未必可信；用模型生成的推理轨迹评估隐藏意图，需要非常谨慎。

## 30. AgriIR: A Scalable Framework for Domain-Specific Knowledge Retrieval

- **arXiv:** 2604.16353
- **Type:** Domain RAG / retrieval-agent infrastructure
- **Main innovation:** Decomposes domain RAG into declarative modules for query refinement, sub-query planning, retrieval, synthesis, citation grounding, and evaluation.
- **Summary:** AgriIR is a modular RAG framework for grounded domain-specific answers, demonstrated on Indian agricultural information access. It decomposes retrieval into query refinement, sub-query planning, retrieval, synthesis, and evaluation.
- **Agentic relevance:** Provides practical infrastructure for domain-specialized retrieval agents under low-compute constraints.
- **Takeaway:** Reliable domain agents need modular retrieval, citation grounding, and evaluation hooks more than monolithic large models.
- **中文版本：** AgriIR 是面向农业领域的模块化 RAG 框架，将流程拆成查询改写、子查询规划、检索、综合、引用 grounding 和评估。它用较小模型和可配置组件实现低成本、可追溯的领域问答，适合作为垂直领域检索智能体基础设施。
- **中文锐评：** AgriIR 的模块化 RAG 很适合低资源垂直领域。它不是追求炫技，而是强调可追溯和低成本；这反而更接近真实部署价值。

## 31. DiagramBank: A Large-scale Dataset of Diagram Design Exemplars with Paper Metadata for Retrieval-Augmented Generation

- **arXiv:** 2604.20857
- **Type:** Dataset / RAG support for AI-scientist agents
- **Main innovation:** Creates a retrieval-oriented corpus of scientific schematic diagrams linked to paper metadata for exemplar-based diagram generation.
- **Summary:** DiagramBank collects a large corpus of scientific diagram exemplars with paper metadata for retrieval-augmented diagram generation. It targets the gap where AI scientist systems can write text and code but struggle with publication-grade conceptual figures.
- **Agentic relevance:** Supports end-to-end scientific agents that must produce papers, diagrams, and explanatory artifacts.
- **Takeaway:** Scientific-agent pipelines need artifact-specific retrieval datasets, not just text-generation components.
- **中文版本：** DiagramBank 构建了带论文元数据的大规模科学示意图样例库，用于 retrieval-augmented diagram generation。它解决 AI scientist 系统能写论文和代码但难以生成高质量概念图的问题，强调科学智能体还需要面向图表等非文本产物的检索数据集。
- **中文锐评：** DiagramBank 补的是 AI scientist pipeline 中常被忽视的一环。锐点是示意图生成不仅是检索相似图，更需要理解论文贡献的视觉叙事结构。
