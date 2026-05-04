# Search Agent and Agentic RL Paper Summaries

Coverage window: 2025-11-04 to 2026-05-04.

Paper list: `2026-05-search-agent-agentic-rl.md`
Parsed assets: `2026-05-search-agent-agentic-rl-assets/`

This report focuses on method, main conclusions, innovation, and critical comments. Each paper was downloaded from arXiv and parsed locally; page counts and parse status are recorded below.

## Paper List

1. MemSearcher: Training LLMs to Reason, Search and Manage Memory via End-to-End Reinforcement Learning (2511.02805, 2025-11-04)
2. CriticSearch: Fine-Grained Credit Assignment for Search Agents via a Retrospective Critic (2511.12159, 2025-11-15)
3. SearchGym: Bootstrapping Real-World Search Agents via Cost-Effective and High-Fidelity Environment Simulation (2601.14615, 2026-01-21)
4. Agentic Search in the Wild: Intents and Trajectory Dynamics from 14M+ Real Search Requests (2601.17617, 2026-01-24)
5. PaperSearchQA: Learning to Search and Reason over Scientific Papers with RLVR (2601.18207, 2026-01-26)
6. SAGE: Steerable Agentic Data Generation for Deep Search with Execution Feedback (2601.18202, 2026-01-26)
7. Evaluating the Search Agent in a Parallel World (2603.04751, 2026-03-05)
8. VSearcher: Long-Horizon Multimodal Search Agent via Reinforcement Learning (2603.02795, 2026-03-03)
9. ORBIT: Scalable and Verifiable Data Generation for Search Agents on a Tight Budget (2604.01195, 2026-04-01)
10. ContextBudget: Budget-Aware Context Management for Long-Horizon Search Agents (2604.01664, 2026-04-02)
11. DR-MMSearchAgent: Deepening Reasoning in Multimodal Search Agents (2604.19264, 2026-04-21)
12. ProMMSearchAgent: A Generalizable Multimodal Search Agent Trained with Process-Oriented Rewards (2604.20486, 2026-04-22)
13. DRACULA: Hunting for the Actions Users Want Deep Research Agents to Execute (2604.23815, 2026-04-26)
14. Dont Stop Early: Scalable Enterprise Deep Research with Controlled Information Flow and Evidence-Aware Termination (2604.24978, 2026-04-27)
15. AEM: Adaptive Entropy Modulation for Multi-Turn Agentic Reinforcement Learning (2605.00425, 2026-05-01)
16. Rethinking Agentic Reinforcement Learning In Large Language Models (2604.27859, 2026-04-30)
17. Agent-R1: Training Powerful LLM Agents with End-to-End Reinforcement Learning (2511.14460, 2025-11-18)
18. SkyRL-Agent: Efficient RL Training for Multi-turn LLM Agent (2511.16108, 2025-11-20)
19. Stabilizing Off-Policy Training for Long-Horizon LLM Agent via Turn-Level Importance Sampling and Clipping-Triggered Normalization (2511.20718, 2025-11-25)
20. DynaWeb: Model-Based Reinforcement Learning of Web Agents (2601.22149, 2026-01-29)
21. WebArbiter: A Principle-Guided Reasoning Process Reward Model for Web Agents (2601.21872, 2026-01-29)
22. WebGym: Scaling Training Environments for Visual Web Agents with Realistic Tasks (2601.02439, 2026-01-05)
23. Demystifying Reinforcement Learning for Long-Horizon Tool-Using Agents: A Comprehensive Recipe (2603.21972, 2026-03-23)
24. RewardFlow: Topology-Aware Reward Propagation on State Graphs for Agentic RL with Large Language Models (2603.18859, 2026-03-19)
25. SLEA-RL: Step-Level Experience Augmented Reinforcement Learning for Multi-Turn Agentic Training (2603.18079, 2026-03-18)
26. Dynamic Dual-Granularity Skill Bank for Agentic RL (2603.28716, 2026-03-30)
27. OpenTinker: Separating Concerns in Agentic Reinforcement Learning (2601.07376, 2026-01-12)
28. ARL-Tangram: Unleash the Resource Efficiency in Agentic Reinforcement Learning (2603.13019, 2026-03-13)
29. Heddle: A Distributed Orchestration System for Agentic RL Rollout (2603.28101, 2026-03-30)

## 1. MemSearcher: Training LLMs to Reason, Search and Manage Memory via End-to-End Reinforcement Learning

- **arXiv:** [2511.02805](https://arxiv.org/abs/2511.02805)
- **Published:** 2025-11-04; **Updated:** 2025-11-04
- **Theme:** Search agent / memory RL
- **Authors:** Qianhao Yuan, Jie Lou, Zichao Li, Jiawei Chen, Yaojie Lu, Hongyu Lin, et al.
- **Pages parsed:** 16; **Parse status:** ok (downloaded)
- **Local PDF:** `2026-05-search-agent-agentic-rl-assets/pdfs/2511.02805.pdf`

### English Summary

- **Method:** MemSearcher keeps a compact task memory instead of concatenating the full interaction history. Multi-context GRPO jointly optimizes reasoning, search actions, and memory updates by sampling trajectory groups under different context views and propagating trajectory-level advantages across them.
- **Main conclusions:** On seven public benchmarks, it reports relative average gains of 11% for Qwen2.5-3B-Instruct and 12% for Qwen2.5-7B-Instruct, with the 3B MemSearcher surpassing several 7B baselines.
- **Innovation:** The key idea is to turn memory management itself into an RL-trained action inside the search loop, addressing context growth and search quality together.

### 中文版本

这篇论文把 search agent 的长上下文问题改写成“搜索、推理、记忆管理”联合学习问题。MemSearcher 每轮维护紧凑记忆，再结合当前问题生成推理轨迹、执行搜索并更新记忆；multi-context GRPO 用不同上下文下的轨迹组做优势传播，让模型学会保留关键信息而不是机械堆历史。主要结论是小模型也能通过更好的记忆策略获得明显收益，说明上下文组织本身是 search agent 能力的一部分。

### 中文锐评

亮点很明确，但风险也明显：记忆压缩一旦丢掉关键证据，后续搜索会被系统性带偏。论文的收益依赖 benchmark 中“关键信息可被压缩”的假设，在开放网页、噪声证据和多目标任务中，如何判断记忆是否真的保真仍然不够充分。

## 2. CriticSearch: Fine-Grained Credit Assignment for Search Agents via a Retrospective Critic

- **arXiv:** [2511.12159](https://arxiv.org/abs/2511.12159)
- **Published:** 2025-11-15; **Updated:** 2025-11-15
- **Theme:** Search agent / credit assignment
- **Authors:** Yaocheng Zhang, Haohuan Huang, Zijun Song, Yuanheng Zhu, Qichao Zhang, Zijie Zhao, et al.
- **Pages parsed:** 17; **Parse status:** ok (downloaded)
- **Local PDF:** `2026-05-search-agent-agentic-rl-assets/pdfs/2511.12159.pdf`

### English Summary

- **Method:** CriticSearch uses a frozen asymmetric retrospective critic that observes the full trajectory and gold answer, then assigns dense turn-level rewards to search-agent actions for RL optimization.
- **Main conclusions:** Across multi-hop reasoning benchmarks, the method improves convergence speed, training stability, and final performance over sparse-reward baselines.
- **Innovation:** It attacks search-agent credit assignment at the turn level, replacing final-answer-only rewards with privileged retrospective feedback.

### 中文版本

CriticSearch 解决搜索智能体中“最后答案奖励太稀疏”的问题。它让一个冻结的 critic 在训练时回看完整轨迹和标准答案，对每一步搜索与推理动作给出细粒度奖励，从而让策略知道哪些中间动作真正有贡献。主要结论是这种 dense reward 能提升收敛速度和稳定性。

### 中文锐评

最大问题是 critic 拥有训练时特权信息，这和真实部署环境不一致。它可能学到的是“贴合 gold answer 的轨迹评分”，而不是泛化的搜索策略；如果 critic 本身偏好某种表面推理风格，策略也会被带偏。

## 3. SearchGym: Bootstrapping Real-World Search Agents via Cost-Effective and High-Fidelity Environment Simulation

- **arXiv:** [2601.14615](https://arxiv.org/abs/2601.14615)
- **Published:** 2026-01-21; **Updated:** 2026-01-21
- **Theme:** Search agent environment
- **Authors:** Xichen Zhang, Ziyi He, Yinghao Zhu, Sitong Wu, Shaozuo Yu, Meng Chu, et al.
- **Pages parsed:** 39; **Parse status:** ok (downloaded)
- **Local PDF:** `2026-05-search-agent-agentic-rl-assets/pdfs/2601.14615.pdf`

### English Summary

- **Method:** SearchGym builds a controllable simulation environment from a verifiable knowledge graph and aligned document corpus, then trains search agents with a curriculum RL method called SearchGym-RL.
- **Main conclusions:** The authors report strong sim-to-real generalization; a Qwen2.5-7B model trained in SearchGym beats a web-enhanced ASearcher baseline by an average relative margin of 10.6% across nine benchmarks.
- **Innovation:** The paper frames high-fidelity, verifiable search simulation as a cheaper and safer substitute for live commercial search during RL.

### 中文版本

SearchGym 的核心是构造一个可验证的搜索模拟环境：知识图谱、文档语料和任务答案相互对齐，避免静态语料错配导致的错误奖励。它再用 curriculum RL 从基础交互逐步训练到长程规划。主要结论是，高质量模拟环境可以显著降低真实搜索 RL 的成本，并具备一定 sim-to-real 泛化。

### 中文锐评

模拟环境越干净，越可能低估真实网页中的脏数据、SEO 噪声、重复内容和时间漂移。SearchGym 证明了“对齐语料有用”，但还没有完全证明“模拟中学到的停止、质疑和交叉验证策略”能抵抗真实互联网的混乱。

## 4. Agentic Search in the Wild: Intents and Trajectory Dynamics from 14M+ Real Search Requests

- **arXiv:** [2601.17617](https://arxiv.org/abs/2601.17617)
- **Published:** 2026-01-24; **Updated:** 2026-04-28
- **Theme:** Agentic search analysis
- **Authors:** Jingjie Ning, João Coelho, Yibo Kong, Yunfan Long, Bruno Martins, João Magalhães, et al.
- **Pages parsed:** 12; **Parse status:** ok (downloaded)
- **Local PDF:** `2026-05-search-agent-agentic-rl-assets/pdfs/2601.17617.pdf`

### English Summary

- **Method:** This is a large-scale log analysis of 14.44M search requests and 3.97M sessions from DeepResearchGym. It uses LLM annotations for intent and query reformulation, and proposes CTAR to measure whether new query terms trace back to retrieved evidence.
- **Main conclusions:** Most multi-turn sessions have at most ten steps; intent shapes repetition and exploration; over half of newly introduced query terms are traceable to accumulated evidence.
- **Innovation:** Instead of proposing a model, it gives empirical telemetry for real agentic search behavior and suggests signals for stopping, budgeting, and cross-step evidence tracking.

### 中文版本

这篇论文不是训练新模型，而是分析真实 agentic search 日志。作者把 1444 万次请求按 session 组织，用 LLM 标注意图和查询改写类型，并提出 CTAR 衡量新查询词是否来自之前检索证据。结论显示，多数会话步数并不长，不同意图有不同探索/重复模式，后续查询常被前序证据驱动。

### 中文锐评

日志分析很有价值，但它依赖 LLM 标注和单一 API 的用户分布，结论更像行为画像而非因果机制。CTAR 只能说明词面可追溯，不等于 agent 真正理解或正确使用了证据。

## 5. PaperSearchQA: Learning to Search and Reason over Scientific Papers with RLVR

- **arXiv:** [2601.18207](https://arxiv.org/abs/2601.18207)
- **Published:** 2026-01-26; **Updated:** 2026-01-26
- **Theme:** Scientific search agent / RLVR
- **Authors:** James Burgess, Jan N. Hansen, Duo Peng, Yuhui Zhang, Alejandro Lozano, Min Woo Sun, et al.
- **Pages parsed:** 19; **Parse status:** ok (downloaded)
- **Local PDF:** `2026-05-search-agent-agentic-rl-assets/pdfs/2601.18207.pdf`

### English Summary

- **Method:** PaperSearchQA builds a 16M biomedical-abstract corpus and a 60K factoid QA dataset, then trains search agents with reinforcement learning with verifiable rewards over scientific-paper search.
- **Main conclusions:** RL-trained agents outperform non-RL retrieval baselines and show behaviors such as planning, reasoning, and self-verification.
- **Innovation:** It shifts RLVR search-agent training from general-domain QA to scientific literature search, making the environment more relevant to AI scientist workflows.

### 中文版本

PaperSearchQA 面向科学论文检索问答，构建 1600 万生物医学摘要语料和 6 万条可验证 factoid QA，并用 RLVR 训练 search agent。它的重点是让模型在科学语料中主动检索、推理和自我验证，而不是只做普通网页问答。实验显示 RL agent 优于非 RL 检索基线。

### 中文锐评

只用摘要会限制科学推理深度，很多关键结论、方法细节和实验设置在全文中。factoid QA 也容易把“科学研究能力”压缩成短答案检索，离真实科研综述、方法比较和证据冲突处理仍有距离。

## 6. SAGE: Steerable Agentic Data Generation for Deep Search with Execution Feedback

- **arXiv:** [2601.18202](https://arxiv.org/abs/2601.18202)
- **Published:** 2026-01-26; **Updated:** 2026-01-26
- **Theme:** Deep search data generation
- **Authors:** Fangyuan Xu, Rujun Han, Yanfei Chen, Zifeng Wang, I-Hung Hsu, Jun Yan, et al.
- **Pages parsed:** 24; **Parse status:** ok (downloaded)
- **Local PDF:** `2026-05-search-agent-agentic-rl-assets/pdfs/2601.18202.pdf`

### English Summary

- **Method:** SAGE uses a data generator and a search agent in a feedback loop: the generator proposes deep-search QA pairs, while the search agent attempts them and returns execution feedback to refine difficulty and correctness.
- **Main conclusions:** Synthetic data from SAGE improves agents by up to 23% relative on popular deep-search benchmarks and can transfer from fixed-corpus retrieval to Google Search at inference time.
- **Innovation:** The paper makes synthetic deep-search data steerable by target difficulty and grounded in execution feedback rather than pure prompt generation.

### 中文版本

SAGE 关注 deep search 训练数据昂贵的问题。它让数据生成器提出复杂问答，再让 search agent 实际执行搜索并反馈，经过多轮迭代得到难度可控、正确性更高的数据。主要结论是，用这种数据训练可以提升 deep search benchmark 表现，并在一定程度上迁移到 Google Search。

### 中文锐评

生成器和求解器互相反馈容易形成闭环偏差：agent 擅长的题会被保留，不擅长但真实重要的题可能被过滤。论文需要更强的外部人工审计来证明合成数据没有过度迎合当前 agent。

## 7. Evaluating the Search Agent in a Parallel World

- **arXiv:** [2603.04751](https://arxiv.org/abs/2603.04751)
- **Published:** 2026-03-05; **Updated:** 2026-04-27
- **Theme:** Search agent evaluation
- **Authors:** Jiawei Chen, Xintian Shen, Lihao Zheng, Lifu Mu, Haoyi Sun, Ning Mao, et al.
- **Pages parsed:** 32; **Parse status:** ok (downloaded)
- **Local PDF:** `2026-05-search-agent-agentic-rl-assets/pdfs/2603.04751.pdf`

### English Summary

- **Method:** Mind-ParaWorld creates future-like parallel-world scenarios with atomic facts and a controlled SERP engine, preventing benchmark leakage, temporal obsolescence, and search-engine variance.
- **Main conclusions:** MPW-Bench shows that search agents can synthesize evidence when information is complete, but struggle with evidence collection coverage, sufficiency judgment, and stopping decisions in unfamiliar environments.
- **Innovation:** It evaluates search capability in a controlled synthetic world beyond model cutoffs, separating search behavior from parametric memory.

### 中文版本

这篇论文提出在“平行世界”中评测 search agent：先用真实实体名合成未来情境，再由 Law Model 生成原子事实和唯一答案，评测时由引擎动态生成符合这些事实的 SERP。这样可以减少知识泄漏、网页变化和商业搜索引擎差异。结论指出，agent 的短板不只在综合证据，更在收集覆盖、判断证据是否足够以及何时停止。

### 中文锐评

平行世界解决了可控性，却可能牺牲真实网页的复杂性。SERP 由模型生成，可能过于规整；如果评测环境本身不像真实搜索，agent 在其中暴露的失败模式未必覆盖真实部署风险。

## 8. VSearcher: Long-Horizon Multimodal Search Agent via Reinforcement Learning

- **arXiv:** [2603.02795](https://arxiv.org/abs/2603.02795)
- **Published:** 2026-03-03; **Updated:** 2026-03-06
- **Theme:** Multimodal search agent / RL
- **Authors:** Ruiyang Zhang, Qianguo Sun, Chao Song, Yiyan Qi, Zhedong Zheng
- **Pages parsed:** 23; **Parse status:** ok (downloaded)
- **Local PDF:** `2026-05-search-agent-agentic-rl-assets/pdfs/2603.02795.pdf`

### English Summary

- **Method:** VSearcher trains multimodal models to use text search, image search, and browsing through an SFT-then-RL pipeline, supported by iterative multimodal QA synthesis and a new MM-SearchExam benchmark.
- **Main conclusions:** It reports stronger performance than recent multimodal search agents and several proprietary models on multimodal web-search tasks.
- **Innovation:** The paper brings long-horizon web search and RL into multimodal agents, not just text-only search agents.

### 中文版本

VSearcher 把静态多模态模型训练成能多轮调用文本搜索、图片搜索和浏览器的搜索智能体。它先用迭代式数据合成生成复杂多模态 QA，再通过 SFT+RL 训练，并提出 MM-SearchExam 评测。主要结论是，VSearcher 在多模态搜索任务上优于已有方法和若干闭源模型。

### 中文锐评

多模态搜索很容易受数据合成质量和实时网页波动影响。论文报告的强结果需要关注是否依赖特定搜索 API、特定题型和图像检索分布；否则模型可能只是学会了 benchmark 风格的工具调用。

## 9. ORBIT: Scalable and Verifiable Data Generation for Search Agents on a Tight Budget

- **arXiv:** [2604.01195](https://arxiv.org/abs/2604.01195)
- **Published:** 2026-04-01; **Updated:** 2026-04-02
- **Theme:** Search agent data generation
- **Authors:** Nandan Thakur, Zijian Chen, Xueguang Ma, Jimmy Lin
- **Pages parsed:** 34; **Parse status:** ok (downloaded)
- **Local PDF:** `2026-05-search-agent-agentic-rl-assets/pdfs/2604.01195.pdf`

### English Summary

- **Method:** ORBIT generates 20K reasoning-intensive, short-answer, web-verifiable queries through seed creation, QA generation, self-verification, and external verification, then trains Qwen3-4B with GRPO.
- **Main conclusions:** ORBIT-4B achieves strong sub-4B search-agent performance on Wikipedia QA tasks, supporting the usefulness of low-budget synthetic data.
- **Innovation:** It emphasizes frugal, open, verifiable data generation for search-agent RL without paid API dependence.

### 中文版本

ORBIT 试图用低成本方式生成 search agent 训练数据。它包含 2 万条需要 4-5 步推理、答案短且可验证的问题，并通过自验证和外部搜索验证控制质量；随后用 GRPO 训练 Qwen3-4B。结论是，小模型也能通过高质量合成数据获得不错的搜索能力。

### 中文锐评

“短答案可验证”有利于 RL，但也可能把 deep research 简化成多跳问答。真实搜索任务常常没有唯一短答案，包含观点冲突和证据权重，ORBIT 对这些开放式场景覆盖不足。

## 10. ContextBudget: Budget-Aware Context Management for Long-Horizon Search Agents

- **arXiv:** [2604.01664](https://arxiv.org/abs/2604.01664)
- **Published:** 2026-04-02; **Updated:** 2026-04-02
- **Theme:** Search agent context management
- **Authors:** Yong Wu, YanZhao Zheng, TianZe Xu, ZhenTao Zhang, YuanQiang Yu, JiHuai Zhu, et al.
- **Pages parsed:** 19; **Parse status:** ok (downloaded)
- **Local PDF:** `2026-05-search-agent-agentic-rl-assets/pdfs/2604.01664.pdf`

### English Summary

- **Method:** ContextBudget formulates context management as a sequential decision problem under a context-budget constraint and trains BACM-RL to decide when and how much interaction history to compress.
- **Main conclusions:** On long-horizon QA and web-browsing benchmarks, BACM-RL outperforms prior context-management methods and reports over 1.6x gains in high-complexity settings.
- **Innovation:** It treats context compression as an agent policy decision rather than a fixed summarization heuristic.

### 中文版本

ContextBudget 把长程 search agent 的上下文管理建模为带预算约束的序列决策问题。BACM-RL 让 agent 在加入新观察前评估剩余预算，并决定何时压缩、压缩多少历史。实验显示它在复杂任务和小预算下优于固定策略。

### 中文锐评

上下文压缩最大的风险是不可逆丢失证据。论文强调性能收益，但需要更细的错误分析：哪些信息被压掉后会造成错误停止、错误引用或重复搜索？没有这种分析，策略可能只是在特定 benchmark 上学会了节省 token。

## 11. DR-MMSearchAgent: Deepening Reasoning in Multimodal Search Agents

- **arXiv:** [2604.19264](https://arxiv.org/abs/2604.19264)
- **Published:** 2026-04-21; **Updated:** 2026-04-21
- **Theme:** Multimodal search agent / RL
- **Authors:** Shengqin Wang, Wentao Yan, Huichi Zhou, Yihang Chen, Kun Shao, Zhizhong Zhang, et al.
- **Pages parsed:** 15; **Parse status:** ok (downloaded)
- **Local PDF:** `2026-05-search-agent-agentic-rl-assets/pdfs/2604.19264.pdf`

### English Summary

- **Method:** DR-MMSearchAgent reshapes trajectory-level advantages using structural proximity across rollouts and adds differentiated Gaussian rewards to calibrate interaction tolerance and reduce redundant context.
- **Main conclusions:** With a 3,602-sample multi-step reasoning dataset, it reports state-of-the-art results and an 8.4% improvement over MMSearch-R1 on FVQA-test.
- **Innovation:** It directly targets premature interaction collapse in multimodal search-agent RL by rewarding useful exploration instead of only final-token success.

### 中文版本

DR-MMSearchAgent 针对多模态 search agent 过早停止和上下文冗余问题。它用 rollout 轨迹之间的结构接近性构造优势信号，让不同长度但正确的探索轨迹也能得到鼓励，并用差异化 Gaussian reward 动态调节交互容忍度。实验显示相比 MMSearch-R1 有明显提升。

### 中文锐评

方法中的 reward shaping 比较复杂，容易把性能提升和工程调参混在一起。训练集只有 3602 条高质量多步 QA，规模不大；是否能泛化到更开放、更脏的视觉搜索环境还需要更强证据。

## 12. ProMMSearchAgent: A Generalizable Multimodal Search Agent Trained with Process-Oriented Rewards

- **arXiv:** [2604.20486](https://arxiv.org/abs/2604.20486)
- **Published:** 2026-04-22; **Updated:** 2026-04-22
- **Theme:** Multimodal search agent / process rewards
- **Authors:** Wentao Yan, Shengqin Wang, Huichi Zhou, Yihang Chen, Kun Shao, Yuan Xie, et al.
- **Pages parsed:** 26; **Parse status:** ok (downloaded)
- **Local PDF:** `2026-05-search-agent-agentic-rl-assets/pdfs/2604.20486.pdf`

### English Summary

- **Method:** ProMMSearchAgent trains in a deterministic local sandbox and uses an introspective process-oriented reward that probes the model’s own knowledge boundaries to reward searching only when visual or factual uncertainty warrants it.
- **Main conclusions:** The locally trained policy transfers zero-shot to live Google Search and reports gains of 5.1% on FVQA-test, 6.3% on InfoSeek, and 11.3% on MMSearch over MMSearch-R1.
- **Innovation:** It combines sim-to-real training with process rewards for the cognitive decision of whether to search, not just whether the final answer is correct.

### 中文版本

ProMMSearchAgent 通过本地静态 sandbox 避免 live web 的不可控性，并用“内省式过程奖励”判断模型是否真的不确定、是否应该发起文本或多模态搜索。它训练出的策略可以零样本迁移到 Google Search，在多个多模态搜索 benchmark 上超过 MMSearch-R1。

### 中文锐评

“探测模型自身知识边界”很聪明，但也可能循环论证：模型不知道自己不知道什么。真实搜索中，错误自信往往比显式不确定更危险，因此这种 reward 是否能处理高置信错觉非常关键。

## 13. DRACULA: Hunting for the Actions Users Want Deep Research Agents to Execute

- **arXiv:** [2604.23815](https://arxiv.org/abs/2604.23815)
- **Published:** 2026-04-26; **Updated:** 2026-04-26
- **Theme:** Deep research agent feedback
- **Authors:** Nishant Balepur, Malachi Hamada, Varsha Kishore, Sergey Feldman, Amanpreet Singh, Pao Siangliulue, et al.
- **Pages parsed:** 40; **Parse status:** ok (downloaded)
- **Local PDF:** `2026-05-search-agent-agentic-rl-assets/pdfs/2604.23815.pdf`

### English Summary

- **Method:** DRACULA collects expert user preferences over intermediate actions proposed by deep-research agents and execution judgments on whether selected actions were applied successfully.
- **Main conclusions:** The dataset contains 8,103 action preferences and 5,230 execution judgments. User selection history improves action-prediction simulation, and personalized new actions are selected more often in follow-up studies.
- **Innovation:** It moves deep-research feedback from final-report scoring to intermediate action preferences, which is closer to how users steer long-horizon agents.

### 中文版本

DRACULA 关注 deep research agent 的中间动作该不该做，而不只是最终报告好不好。19 位 CS 研究者在 5 周内对系统提出的动作进行选择，并判断最终报告是否成功执行这些动作，形成 8103 条动作偏好和 5230 条执行判断。结论是，用户历史选择比自述偏好更能帮助预测用户想要的动作。

### 中文锐评

数据很珍贵，但样本人群很窄，主要是 CS 研究者；动作也是系统预先提出的，可能限制了真实用户会提出的修改空间。它解释了“用户想要什么动作”，但还没有解决 agent 如何可靠执行这些动作。

## 14. Dont Stop Early: Scalable Enterprise Deep Research with Controlled Information Flow and Evidence-Aware Termination

- **arXiv:** [2604.24978](https://arxiv.org/abs/2604.24978)
- **Published:** 2026-04-27; **Updated:** 2026-04-27
- **Theme:** Deep research agent architecture
- **Authors:** Prafulla Kumar Choubey, Kung-Hsiang Huang, Pranav Narayanan Venkit, Jiaxin Zhang, Vaibhav Vats, Yu Li, et al.
- **Pages parsed:** 15; **Parse status:** ok (downloaded)
- **Local PDF:** `2026-05-search-agent-agentic-rl-assets/pdfs/2604.24978.pdf`

### English Summary

- **Method:** The EDR architecture decomposes requests into coverage-driven objectives, uses dependency-guided execution and explicit information sharing, and enforces evidence-based completion criteria before stopping.
- **Main conclusions:** On an internal sales-enablement task and DeepResearch Bench, the design achieves the strongest overall performance among competitive baselines and reduces premature stopping.
- **Innovation:** It operationalizes controlled information flow and evidence-aware termination for enterprise deep research, where coverage and sufficiency matter more than a single answer.

### 中文版本

这篇论文针对企业 deep research 报告常见的覆盖不均、上下文爆炸和过早停止问题。系统先通过 outline/reflection 分解覆盖目标，再用依赖关系控制执行和信息共享，最后用证据充分性条件决定是否继续收集信息。主要结论是，这种设计能提升报告深度和一致性。

### 中文锐评

企业场景的真实价值很高，但内部 sales enablement 评测不够透明。证据充分性规则如果设计不好，可能诱导 agent 过度检索、堆砌引用，或者为了满足检查项而牺牲判断质量。

## 15. AEM: Adaptive Entropy Modulation for Multi-Turn Agentic Reinforcement Learning

- **arXiv:** [2605.00425](https://arxiv.org/abs/2605.00425)
- **Published:** 2026-05-01; **Updated:** 2026-05-01
- **Theme:** Agentic RL algorithm
- **Authors:** Haotian Zhao, Yuxin Zhang, Songlin Zhou, Stephen S. -T. Yau, Wenyu Zhang, Lun Tian, et al.
- **Pages parsed:** 28; **Parse status:** ok (downloaded)
- **Local PDF:** `2026-05-search-agent-agentic-rl-assets/pdfs/2605.00425.pdf`

### English Summary

- **Method:** AEM introduces supervision-free credit assignment by adaptively modulating entropy dynamics during RL. It analyzes entropy at the response level and uses a practical proxy based on advantage and relative response surprisal to shift exploration toward exploitation.
- **Main conclusions:** Across models from 1.5B to 32B and several benchmarks, AEM improves multi-turn agentic RL, including a reported 1.4 point gain when added to a strong SWE-bench-Verified baseline.
- **Innovation:** It avoids extra process reward models and instead uses entropy dynamics as the control knob for credit assignment and exploration.

### 中文版本

AEM 试图在不引入额外过程奖励模型的情况下改善多轮 agentic RL 的 credit assignment。它把熵分析从 token 层提升到 response 层，并根据 advantage 与相对 surprisal 的关系调节训练动态，使模型从探索自然过渡到利用。实验覆盖 1.5B 到 32B 模型，并在 SWE-bench-Verified 强基线上有增益。

### 中文锐评

1.4 个百分点的增益说明方法可能有效，但也提示收益并非压倒性。熵调制是间接信号，是否真的解决 credit assignment，还是只是更稳的探索调参，需要更多任务和失败案例验证。

## 16. Rethinking Agentic Reinforcement Learning In Large Language Models

- **arXiv:** [2604.27859](https://arxiv.org/abs/2604.27859)
- **Published:** 2026-04-30; **Updated:** 2026-04-30
- **Theme:** Agentic RL survey / position
- **Authors:** Fangming Cui, Ruixiao Zhu, Cheng Fang, Sunan Li, Jiahong Li
- **Pages parsed:** 17; **Parse status:** ok (downloaded)
- **Local PDF:** `2026-05-search-agent-agentic-rl-assets/pdfs/2604.27859.pdf`

### English Summary

- **Method:** This paper is a conceptual survey/position piece that frames agentic RL for LLMs around goal setting, long-term planning, strategy adaptation, self-reflection, and interactive reasoning in uncertain environments.
- **Main conclusions:** Its main contribution is a taxonomy of foundations, designs, challenges, and future directions rather than new benchmark results.
- **Innovation:** It attempts to distinguish LLM-based agentic RL from conventional episodic RL by emphasizing open-ended cognition-like loops.

### 中文版本

这篇文章更像综述和立场文，试图重新定义 LLM 时代的 agentic RL：不再只是固定环境中的策略优化，而是包括目标设定、长期规划、动态策略调整、自我反思和多步交互推理。它主要贡献是概念框架、方法脉络和未来挑战。

### 中文锐评

概念覆盖很广，但实证贡献弱。agentic RL 现在已经有很多系统、奖励和环境论文，单纯扩大定义容易变成“什么都算 agentic RL”；更需要可操作的边界、任务协议和失败诊断标准。

## 17. Agent-R1: Training Powerful LLM Agents with End-to-End Reinforcement Learning

- **arXiv:** [2511.14460](https://arxiv.org/abs/2511.14460)
- **Published:** 2025-11-18; **Updated:** 2025-11-18
- **Theme:** Agentic RL algorithm
- **Authors:** Mingyue Cheng, Jie Ouyang, Shuo Yu, Ruiran Yan, Yucong Luo, Zirui Liu, et al.
- **Pages parsed:** 13; **Parse status:** ok (downloaded)
- **Local PDF:** `2026-05-search-agent-agentic-rl-assets/pdfs/2511.14460.pdf`

### English Summary

- **Method:** Agent-R1 extends the MDP framing to LLM agents with tool/environment interaction and provides a modular framework for RL-based agent training across tasks.
- **Main conclusions:** Experiments on multihop QA provide initial evidence that the framework can train interactive LLM agents effectively.
- **Innovation:** It contributes a reusable formulation and training framework at a time when LLM-agent RL infrastructure is still fragmented.

### 中文版本

Agent-R1 从 MDP 角度重新定义 LLM agent 的状态、动作、环境和奖励，并提供一个模块化的端到端 RL 训练框架。它用多跳 QA 做初步验证，目标是让不同任务和交互环境能更容易接入 RL。

### 中文锐评

作为早期框架论文有价值，但验证场景偏窄。多跳 QA 不能代表真实长程 agent 的工具错误、环境变化和恢复能力；框架灵活性也需要更多第三方任务来证明。

## 18. SkyRL-Agent: Efficient RL Training for Multi-turn LLM Agent

- **arXiv:** [2511.16108](https://arxiv.org/abs/2511.16108)
- **Published:** 2025-11-20; **Updated:** 2025-11-20
- **Theme:** Agentic RL framework
- **Authors:** Shiyi Cao, Dacheng Li, Fangzhou Zhao, Shuo Yuan, Sumanth R. Hegde, Connor Chen, et al.
- **Pages parsed:** 16; **Parse status:** ok (downloaded)
- **Local PDF:** `2026-05-search-agent-agentic-rl-assets/pdfs/2511.16108.pdf`

### English Summary

- **Method:** SkyRL-Agent provides asynchronous dispatch, lightweight tool integration, and backend interoperability. It trains SA-SWE-32B with pure RL and an AST-based search tool for code navigation.
- **Main conclusions:** SA-SWE-32B reaches 39.4% Pass@1 on SWE-Bench Verified, with more than 2x cost reduction over comparable prior models, and transfers to Terminal-Bench, BrowseComp-Plus, and WebArena.
- **Innovation:** The paper makes rollout systems, tool integration, and code-navigation tools first-class pieces of efficient multi-turn agentic RL.

### 中文版本

SkyRL-Agent 是面向多轮长程 agent RL 的训练和评测框架，强调异步调度、轻量工具接入和兼容不同训练后端。作者用它训练 SA-SWE-32B，并加入 AST 搜索工具帮助代码定位，最终在 SWE-Bench Verified 上达到 39.4% Pass@1，同时降低成本。

### 中文锐评

结果很强，但复现门槛高：32B 模型、SWE 任务、工具设计和基础设施都可能贡献很大。论文需要更清楚拆分“RL 算法收益”和“工程系统/工具收益”。

## 19. Stabilizing Off-Policy Training for Long-Horizon LLM Agent via Turn-Level Importance Sampling and Clipping-Triggered Normalization

- **arXiv:** [2511.20718](https://arxiv.org/abs/2511.20718)
- **Published:** 2025-11-25; **Updated:** 2026-02-24
- **Theme:** Agentic RL stability
- **Authors:** Chenliang Li, Adel Elmahdy, Alex Boyd, Zhongruo Wang, Siliang Zeng, Alfredo Garcia, et al.
- **Pages parsed:** 29; **Parse status:** ok (downloaded)
- **Local PDF:** `2026-05-search-agent-agentic-rl-assets/pdfs/2511.20718.pdf`

### English Summary

- **Method:** SORL aligns optimization with turn-structured interactions using turn-level importance sampling and clipping-triggered normalization, instantiated as SO-PPO and SO-GRPO.
- **Main conclusions:** On multi-turn search benchmarks, SORL prevents collapse seen in standard PPO/GRPO, lowers clipping ratios, stabilizes trajectories, and matches or improves task performance.
- **Innovation:** It identifies token-level vs turn-level granularity mismatch as a root cause of off-policy instability in long-horizon LLM-agent RL.

### 中文版本

SORL 针对长程 LLM agent 离策略训练不稳定问题。作者认为标准 PPO/GRPO 的 token 级优化和多轮交互结构不匹配，同时 off-policy importance sampling 方差高。SORL 用 turn-level importance sampling 和 clipping-triggered normalization 构造 SO-PPO/SO-GRPO，降低训练崩溃风险。

### 中文锐评

论文抓住了一个真实痛点，但仍主要在搜索类 benchmark 上验证。turn-level 稳定化是否适用于 GUI、代码执行、机器人等动作空间更复杂的 agent，还需要跨环境测试。

## 20. DynaWeb: Model-Based Reinforcement Learning of Web Agents

- **arXiv:** [2601.22149](https://arxiv.org/abs/2601.22149)
- **Published:** 2026-01-29; **Updated:** 2026-04-17
- **Theme:** Web agent / model-based RL
- **Authors:** Hang Ding, Peidong Liu, Junqiao Wang, Ziwei Ji, Meng Cao, Rongzhao Zhang, et al.
- **Pages parsed:** 21; **Parse status:** ok (downloaded)
- **Local PDF:** `2026-05-search-agent-agentic-rl-assets/pdfs/2601.22149.pdf`

### English Summary

- **Method:** DynaWeb trains a web world model to predict naturalistic page representations after agent actions, then lets the policy generate imagined rollouts, interleaving them with expert trajectories for stability.
- **Main conclusions:** On WebArena and WebVoyager, DynaWeb consistently improves state-of-the-art open-source web-agent models.
- **Innovation:** It imports model-based RL into web agents, using learned web-environment imagination to reduce live-internet training cost and risk.

### 中文版本

DynaWeb 用 model-based RL 训练网页 agent。它先学习一个 web world model，根据 agent 动作预测自然网页表示，再让策略在这个合成环境中“做梦”生成大量 rollout，并混入专家轨迹稳定训练。实验在 WebArena 和 WebVoyager 上提升开源 web agent。

### 中文锐评

网页世界模型的保真度是核心风险。真实网站包含登录、异步状态、广告、反爬、动态 DOM 和不可逆操作，world model 一旦过于理想化，agent 可能学到模拟捷径而不是真实网页技能。

## 21. WebArbiter: A Principle-Guided Reasoning Process Reward Model for Web Agents

- **arXiv:** [2601.21872](https://arxiv.org/abs/2601.21872)
- **Published:** 2026-01-29; **Updated:** 2026-04-09
- **Theme:** Web agent process reward
- **Authors:** Yao Zhang, Shijie Tang, Zeyu Li, Zhen Han, Volker Tresp
- **Pages parsed:** 28; **Parse status:** ok (downloaded)
- **Local PDF:** `2026-05-search-agent-agentic-rl-assets/pdfs/2601.21872.pdf`

### English Summary

- **Method:** WebArbiter formulates web process reward modeling as structured text generation: it produces principle-guided reasoning, a verdict, and an action preference. Training uses reasoning distillation followed by RL alignment.
- **Main conclusions:** On WebPRMBench, WebArbiter-7B outperforms the strongest baseline reported in the abstract, and improves reward-guided trajectory search on WebArena-Lite.
- **Innovation:** It makes the reward model interpretable and principle-driven instead of a scalar progress score or brittle checklist.

### 中文版本

WebArbiter 是面向 web agent 的过程奖励模型。它不只输出分数，而是生成原则化推理、偏好判断和当前上下文下最有助于完成任务的动作。训练分两步：先做 reasoning distillation，再用 RL 修正教师偏差。它还发布 WebPRMBench 来系统评测 web PRM。

### 中文锐评

生成式 PRM 可解释性更好，但也更像一个“会写理由的 judge”。理由写得通顺不代表奖励因果正确；如果偏好标注覆盖不了真实网页状态变化，reward-guided search 仍可能奖励表面合理但实际错误的动作。

## 22. WebGym: Scaling Training Environments for Visual Web Agents with Realistic Tasks

- **arXiv:** [2601.02439](https://arxiv.org/abs/2601.02439)
- **Published:** 2026-01-05; **Updated:** 2026-02-26
- **Theme:** Web agent environment
- **Authors:** Hao Bai, Alexey Taymanov, Tong Zhang, Aviral Kumar, Spencer Whitehead
- **Pages parsed:** 39; **Parse status:** ok (downloaded)
- **Local PDF:** `2026-05-search-agent-agentic-rl-assets/pdfs/2601.02439.pdf`

### English Summary

- **Method:** WebGym provides nearly 300K realistic visual-web tasks with rubric-based evaluation and a high-throughput asynchronous rollout system for RL training.
- **Main conclusions:** Fine-tuning Qwen-3-VL-8B-Instruct on WebGym improves OOD website success from 26.2% to 42.9%, outperforming several proprietary-model agents reported in the abstract.
- **Innovation:** It scales both task diversity and rollout throughput for visual web-agent RL, treating environment breadth as a central training variable.

### 中文版本

WebGym 提供近 30 万个真实网站视觉任务和 rubric-based evaluation，并构建高吞吐异步 rollout 系统来支持 RL。作者用 WebGym 训练 Qwen-3-VL-8B-Instruct，使其在未见网站测试集上的成功率从 26.2% 提升到 42.9%。

### 中文锐评

WebGym 的规模很重要，但真实网站会持续变化，rubric 也可能无法捕捉任务完成的全部语义。大规模环境如果缺少持续维护，可能很快老化；如果 rubric 有偏，RL 会精准放大这种偏差。

## 23. Demystifying Reinforcement Learning for Long-Horizon Tool-Using Agents: A Comprehensive Recipe

- **arXiv:** [2603.21972](https://arxiv.org/abs/2603.21972)
- **Published:** 2026-03-23; **Updated:** 2026-03-23
- **Theme:** Tool-using agent RL recipe
- **Authors:** Xixi Wu, Qianguo Sun, Ruiyang Zhang, Chao Song, Junlong Wu, Yiyan Qi, et al.
- **Pages parsed:** 39; **Parse status:** ok (downloaded)
- **Local PDF:** `2026-05-search-agent-agentic-rl-assets/pdfs/2603.21972.pdf`

### English Summary

- **Method:** This empirical study uses TravelPlanner to vary reward shaping, model scale, data composition, RL algorithm, and environment stability, distilling a practical recipe for long-horizon tool-use RL.
- **Main conclusions:** It reports seven takeaways, including scale-dependent reward/algorithm choices, about 1K balanced samples as a useful sweet spot, and environment stability as critical for avoiding degradation.
- **Innovation:** Rather than proposing one trick, it maps the agentic RL design space with controlled experiments.

### 中文版本

这篇论文用 TravelPlanner 系统研究长程工具使用 agent 的 RL 配方，从奖励塑形、模型规模、数据组成、算法选择和环境稳定性五个维度做控制实验。结论包括：小模型更需要 staged rewards 和探索，大模型可用更简单 dense rewards；约 1K 难度均衡样本是有效甜点；环境稳定性对防止策略退化很关键。

### 中文锐评

这类 recipe 论文很实用，但也容易过拟合到 TravelPlanner。旅行规划的工具结构、约束类型和奖励可验证性相对明确，不能直接推出代码、网页、科研搜索等 agent 环境也遵循同一配方。

## 24. RewardFlow: Topology-Aware Reward Propagation on State Graphs for Agentic RL with Large Language Models

- **arXiv:** [2603.18859](https://arxiv.org/abs/2603.18859)
- **Published:** 2026-03-19; **Updated:** 2026-03-19
- **Theme:** Agentic RL reward propagation
- **Authors:** Xiao Feng, Bo Han, Zhanke Zhou, Jiaqi Fan, Jiangchao Yao, Ka Ho Li, et al.
- **Pages parsed:** 34; **Parse status:** ok (downloaded)
- **Local PDF:** `2026-05-search-agent-agentic-rl-assets/pdfs/2603.18859.pdf`

### English Summary

- **Method:** RewardFlow builds state graphs from reasoning trajectories and propagates success contribution over the graph topology to estimate dense state-level rewards without training a separate reward model.
- **Main conclusions:** When used as dense rewards, it substantially outperforms prior RL baselines across four agentic reasoning benchmarks with better robustness and training efficiency.
- **Innovation:** It derives process-like rewards from trajectory topology instead of extra annotations or costly PRM training.

### 中文版本

RewardFlow 试图在没有额外过程奖励模型的情况下得到 state-level dense rewards。它把推理轨迹中的状态组织成图，分析状态对成功的贡献，再通过拓扑传播形成奖励。作为 RL dense reward 后，在四个 agentic reasoning benchmark 上优于基线。

### 中文锐评

状态图的构造质量决定一切。语言状态和工具状态是否真的能用图拓扑表达贡献并不总是成立；如果相似状态被错误连边，奖励传播会把噪声系统性扩散。

## 25. SLEA-RL: Step-Level Experience Augmented Reinforcement Learning for Multi-Turn Agentic Training

- **arXiv:** [2603.18079](https://arxiv.org/abs/2603.18079)
- **Published:** 2026-03-18; **Updated:** 2026-03-18
- **Theme:** Agentic RL experience reuse
- **Authors:** Prince Zizhuang Wang, Shuli Jiang
- **Pages parsed:** 18; **Parse status:** ok (downloaded)
- **Local PDF:** `2026-05-search-agent-agentic-rl-assets/pdfs/2603.18079.pdf`

### English Summary

- **Method:** SLEA-RL retrieves relevant experiences at each decision step based on the current observation, using observation clustering, a self-evolving experience library, and step-level credit assignment.
- **Main conclusions:** On long-horizon multi-turn agent benchmarks, SLEA-RL outperforms multiple RL baselines.
- **Innovation:** It fixes the static-experience mismatch by making experience retrieval step-conditioned and updated across training.

### 中文版本

SLEA-RL 认为多轮 agent 训练不能只在 episode 开头检索一次经验，因为每步观察都会改变。它通过 step-level observation clustering、持续演化的经验库和细粒度 credit assignment，在每个决策点检索相关经验。实验显示它在长程多轮任务上优于普通 RL。

### 中文锐评

经验库方法很可能引入隐藏的数据污染或策略依赖：成功经验被反复检索会强化已有模式，失败但有探索价值的轨迹可能被淘汰。经验抽取和 admission 规则需要更严格的泛化测试。

## 26. Dynamic Dual-Granularity Skill Bank for Agentic RL

- **arXiv:** [2603.28716](https://arxiv.org/abs/2603.28716)
- **Published:** 2026-03-30; **Updated:** 2026-03-30
- **Theme:** Agentic RL skill memory
- **Authors:** Songjun Tu, Chengdong Xu, Qichao Zhang, Yaocheng Zhang, Xiangyuan Lan, Linjing Li, et al.
- **Pages parsed:** 12; **Parse status:** ok (downloaded)
- **Local PDF:** `2026-05-search-agent-agentic-rl-assets/pdfs/2603.28716.pdf`

### English Summary

- **Method:** D2Skill maintains a dual-granularity skill bank with task skills for high-level guidance and step skills for local decision support. Paired baseline and skill-injected rollouts produce hindsight utility signals for skill updating and policy optimization.
- **Main conclusions:** On ALFWorld and WebShop, it improves success rates by 10-20 points over skill-free baselines, with ablations showing both granularity levels and dynamic maintenance matter.
- **Innovation:** It turns reusable training experience into a maintained skill memory that co-evolves with the RL policy.

### 中文版本

D2Skill 把 agentic RL 中的可复用经验组织成双粒度技能库：task skill 提供高层指导，step skill 提供局部决策和纠错。它用同一策略下的 baseline rollout 和 skill-injected rollout 对比得到 hindsight utility，用于更新技能库和优化策略。实验在 ALFWorld 和 WebShop 上提升 10-20 个成功率点。

### 中文锐评

技能库越强，越要警惕 benchmark 特化。ALFWorld/WebShop 的任务结构相对固定，学到的 skill 可能更像任务模板；到开放网页或代码环境中，技能检索、冲突处理和过时技能删除会更难。

## 27. OpenTinker: Separating Concerns in Agentic Reinforcement Learning

- **arXiv:** [2601.07376](https://arxiv.org/abs/2601.07376)
- **Published:** 2026-01-12; **Updated:** 2026-01-12
- **Theme:** Agentic RL infrastructure
- **Authors:** Siqi Zhu, Jiaxuan You
- **Pages parsed:** 7; **Parse status:** ok (downloaded)
- **Local PDF:** `2026-05-search-agent-agentic-rl-assets/pdfs/2601.07376.pdf`

### English Summary

- **Method:** OpenTinker separates agent/environment protocols, inference execution, and training algorithms into composable components, with a centralized scheduler for LoRA, full-parameter RL, SFT, and inference workloads.
- **Main conclusions:** The paper demonstrates several practical RL use cases and discusses extensions to multi-agent training.
- **Innovation:** It addresses infrastructure modularity rather than proposing another monolithic agentic RL pipeline.

### 中文版本

OpenTinker 是 agentic RL 基础设施论文，核心思想是把算法设计、执行运行时、agent-environment 交互协议解耦。用户定义 agent、环境和协议，推理和训练交给统一运行时与调度器管理，支持 LoRA、全参 RL、SFT 和推理 workload。

### 中文锐评

工程抽象很重要，但论文的科学贡献取决于是否真能降低新任务接入和调试成本。框架论文常见问题是示例有效，但外部用户面对复杂工具、失败恢复和资源异构时仍要大量定制。

## 28. ARL-Tangram: Unleash the Resource Efficiency in Agentic Reinforcement Learning

- **arXiv:** [2603.13019](https://arxiv.org/abs/2603.13019)
- **Published:** 2026-03-13; **Updated:** 2026-03-13
- **Theme:** Agentic RL resource management
- **Authors:** Bangjun Xiao, Yihao Zhao, Xiangwei Deng, Shihua Yu, Yuxing Xiang, Huaqiu Liu, et al.
- **Pages parsed:** 25; **Parse status:** ok (downloaded)
- **Local PDF:** `2026-05-search-agent-agentic-rl-assets/pdfs/2603.13019.pdf`

### English Summary

- **Method:** ARL-Tangram introduces action-level orchestration for external resources such as CPUs for code execution and GPUs for reward models, with elastic scheduling and heterogeneous resource managers.
- **Main conclusions:** On real agentic RL workloads, it improves average action completion time by up to 4.3x, speeds RL steps by up to 1.5x, and saves up to 71.2% external resources.
- **Innovation:** It recognizes that agentic RL bottlenecks often sit outside the training GPU cluster, at tool/action execution granularity.

### 中文版本

ARL-Tangram 关注 agentic RL 的外部资源瓶颈，例如代码执行 CPU、奖励模型 GPU 等。它提出 action-level orchestration，用统一动作级抽象和弹性调度来共享异构资源，目标是缩短 action completion time。实验显示 ACT 最多提升 4.3 倍、RL step 加速 1.5 倍、外部资源节省 71.2%。

### 中文锐评

这是很现实的系统问题，但指标主要是资源效率，不直接证明模型能力提升。不同公司的工具调用、沙箱和资源拓扑差异巨大，ARL-Tangram 的部署收益可能高度依赖内部平台。

## 29. Heddle: A Distributed Orchestration System for Agentic RL Rollout

- **arXiv:** [2603.28101](https://arxiv.org/abs/2603.28101)
- **Published:** 2026-03-30; **Updated:** 2026-03-30
- **Theme:** Agentic RL rollout system
- **Authors:** Zili Zhang, Yinmin Zhong, Chengxu Yang, Chao Jin, Bingyang Wu, Xinming Wei, et al.
- **Pages parsed:** 14; **Parse status:** ok (downloaded)
- **Local PDF:** `2026-05-search-agent-agentic-rl-assets/pdfs/2603.28101.pdf`

### English Summary

- **Method:** Heddle uses trajectory-level scheduling, trajectory-aware placement, opportunistic migration during tool-call idle intervals, and adaptive model parallelism to reduce long-tail rollout bottlenecks.
- **Main conclusions:** Across agentic RL workloads, it reports up to 2.5x higher end-to-end rollout throughput than state-of-the-art baselines.
- **Innovation:** It shifts rollout optimization from step-centric execution to trajectory-centric orchestration, matching the long-tail structure of tool-using agents.

### 中文版本

Heddle 解决 agentic RL rollout 阶段的长尾问题。频繁工具调用让不同轨迹耗时差异很大，step-centric 系统会产生排队、干扰和 per-token 时间膨胀。Heddle 用轨迹级调度、轨迹感知放置、工具空闲期迁移和动态并行度调整来提升吞吐。

### 中文锐评

吞吐提升很有价值，但 rollout 更快不等于策略更好。系统引入运行时预测、动态规划放置和迁移，复杂度不低；如果负载分布变化或预测不准，收益可能下降。
