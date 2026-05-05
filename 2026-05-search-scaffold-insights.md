# Search Scaffold Optimization Insights from 2026-05 Search Agent / Agentic RL Papers

来源文件：`2026-05-search-agent-agentic-rl.md`

检查范围：清单中的 29 篇 search agent、deep research、web/multimodal agent、agentic RL、rollout infrastructure 论文，以及本地解析的 `2026-05-search-agent-agentic-rl-summaries.md` 和 `2026-05-search-agent-agentic-rl-assets/texts/`。

本文只提取对 search scaffold 直接有用的优化点，不逐篇复述。

## 优先优化点

| 优先级 | 优化点 | 对 search scaffold 的具体建议 | 简要理由 | 主要依据 |
|---|---|---|---|---|
| P0 | 把上下文管理做成一等组件 | 将原始轨迹、工作记忆、证据表、当前推理状态分开保存；每轮搜索后显式执行 `extract_evidence -> update_memory -> decide_next_action`。压缩时保留证据来源、时间、支持/反驳关系和未解决问题，不只保留自然语言摘要。 | 多篇论文显示，直接拼接完整历史会造成长而噪的上下文；但只看当前 turn 又会丢关键信息。可训练/可策略化的记忆与预算管理能同时改善效率和准确性。 | MemSearcher (2511.02805), ContextBudget (2604.01664), Agentic Search in the Wild (2601.17617) |
| P0 | 增加 evidence-aware termination gate | 不允许模型仅凭“感觉够了”停止。`finish` 前必须通过覆盖检查：核心子问题是否都有证据、关键结论是否有来源、是否处理冲突证据、是否存在新搜索可显著改变答案。 | search agent 的常见失败不是不会综合，而是证据收集覆盖不足、充分性判断差、过早停止。企业 deep research 也强调基于证据的完成条件。 | Evaluating the Search Agent in a Parallel World (2603.04751), Dont Stop Early (2604.24978), DR-MMSearchAgent (2604.19264) |
| P0 | 记录 turn-level / action-level 诊断信号 | 每个 action 记录结构化诊断：动作类型、意图、query、新证据数量、证据质量、是否重复、是否推进子目标、失败原因。即使暂时不训练 RL，也要让日志能回放和打分。 | final-answer-only 信号太稀疏，无法定位哪一步搜索、阅读、压缩或停止决策出了问题。过程奖励、回溯 critic 和用户动作偏好都指向中间动作监督的重要性。 | CriticSearch (2511.12159), WebArbiter (2601.21872), DRACULA (2604.23815), RewardFlow (2603.18859) |
| P0 | 引入 intent-adaptive budget | 开局先判别任务意图和难度：fact lookup、multi-hop、comparison、survey/deep research、time-sensitive、multimodal。不同意图使用不同 max steps、query breadth、source count、verification depth 和 stop threshold。 | 大规模真实日志显示，不同意图的重复、探索和步数分布不同；固定预算会同时导致简单问题过搜、复杂问题早停。 | Agentic Search in the Wild (2601.17617), Demystifying RL for Long-Horizon Tool-Using Agents (2603.21972), Dont Stop Early (2604.24978) |
| P0 | 把 query reformulation 纳入状态机 | 每次 query 改写标注为 broaden、narrow、disambiguate、verify、source-seeking、freshness-check 等类型；跟踪新 query 词是否来自已有证据，发现无来源漂移或重复 query 时触发纠偏。 | 真实 agentic search 中，后续 query 很多来自累积证据。显式 tracking 可以减少 query drift、重复搜索和无依据发散。 | Agentic Search in the Wild (2601.17617), SAGE (2601.18202), ORBIT (2604.01195) |
| P1 | 建立 claim/evidence graph | 把检索结果抽成 atomic claims，维护 `claim -> source -> support/refute/unknown -> confidence -> used_in_answer` 图。回答生成只引用图中可追溯证据，并对冲突 claim 做显式 resolution。 | controlled search benchmark 表明，信息完整时 agent 能综合，但覆盖和充分性差。图结构还能支持 reward propagation、重复检测和最终答案可审计。 | SearchGym (2601.14615), Evaluating the Search Agent in a Parallel World (2603.04751), RewardFlow (2603.18859), PaperSearchQA (2601.18207) |
| P1 | 做 search/no-search uncertainty gate | 在每轮前显式判断：内部知识是否可能过时、问题是否需要外部证据、现有证据是否能支持答案。对高置信但时效敏感/事实型问题强制触发 verification search。 | 多模态 search 论文显示，“何时搜索”本身是关键决策；只依赖模型自信会漏掉高置信错误，尤其是实时、长尾或视觉事实。 | ProMMSearchAgent (2604.20486), VSearcher (2603.02795), WebArbiter (2601.21872) |
| P1 | 构建离线可复现 search sandbox | 为训练和回归测试准备 aligned corpus、可验证答案、可控 SERP 或网页快照；live web 只用于最终 smoke/e2e，不作为唯一评测环境。 | live search 成本高、不可复现且时间漂移大；静态语料如果与答案不对齐会产生错误 reward。高保真模拟环境能降低成本并稳定评测。 | SearchGym (2601.14615), Evaluating the Search Agent in a Parallel World (2603.04751), ProMMSearchAgent (2604.20486), DynaWeb (2601.22149), WebGym (2601.02439) |
| P1 | 用 generator-solver-verifier 循环造训练/评测数据 | 数据生成不要只 prompt 一次。让 generator 出题，solver 实际搜索，verifier 用外部检索/规则/人工抽检验证答案和路径；按目标难度、推理步数、证据类型分桶。 | deep search 数据昂贵，合成数据只有经过执行反馈和外部验证才适合训练；难度均衡比单纯堆量更重要。 | SAGE (2601.18202), ORBIT (2604.01195), PaperSearchQA (2601.18207), VSearcher (2603.02795), Demystifying RL (2603.21972) |
| P1 | 设计 step-level experience / skill memory | 保存成功和失败轨迹中的可复用片段：有效 query 模板、验证策略、错误恢复动作、领域源选择。检索粒度应基于当前 observation/子目标，而不是只在任务开始时检索。 | 多轮任务每一步状态都变化，episode-level 经验容易失配；动态技能库和 step-level 经验检索能提升局部决策和纠错。 | SLEA-RL (2603.18079), Dynamic Dual-Granularity Skill Bank (2603.28716), DRACULA (2604.23815), MemSearcher (2511.02805) |
| P1 | 让 scaffold 支持 multimodal/tool-agnostic observation | 工具接口不要硬编码 text search。统一抽象 text search、image search、browser open、page read、document search、visual observation，并把每类 observation 归一化为 evidence items。 | search agent 正在从文本 QA 扩展到网页、图像、视觉浏览和科学论文检索；早期接口如果只面向文本 SERP，会限制后续扩展。 | VSearcher (2603.02795), DR-MMSearchAgent (2604.19264), ProMMSearchAgent (2604.20486), WebGym (2601.02439), PaperSearchQA (2601.18207) |
| P1 | 将 user preference 作为中间动作反馈 | 对 deep research/report 类任务，允许用户或 evaluator 对下一步 action 做选择/拒绝/补充，并把选择历史写入 preference memory。不要只收最终报告分。 | 长程研究任务中，用户真正控制的是中间研究动作；历史选择比用户自述偏好更能预测后续期望动作。 | DRACULA (2604.23815), WebArbiter (2601.21872), Dont Stop Early (2604.24978) |
| P2 | RL 训练时使用 turn-level 粒度和稳定性保护 | 如果 scaffold 用于 RL rollout，reward/advantage/logprob 统计应至少支持 turn-level 聚合；监控 clipping ratio、trajectory length、tool-call success、entropy drift，避免 token-level 优化和多轮 action 粒度错配。 | 长程 agent 的 action 是 turn-structured；标准 PPO/GRPO 的 token-level 信号在 off-policy 场景容易不稳定。熵调制和 scale-aware reward shaping 可改善探索到利用的过渡。 | SORL (2511.20718), AEM (2605.00425), Demystifying RL (2603.21972), Agent-R1 (2511.14460) |
| P2 | 异步化 tool execution 与 trajectory scheduling | 搜索、浏览、解析、reward model、代码/页面执行等外部动作统一进入 action queue；日志中记录 action latency 和资源类型；支持缓存、超时、重试、并发 rollout 和按轨迹调度。 | agentic RL 和 search rollout 的瓶颈常在外部工具，不在模型推理本身。工具调用有长尾延迟，step-centric 调度会浪费资源并拖慢训练。 | SkyRL-Agent (2511.16108), ARL-Tangram (2603.13019), Heddle (2603.28101), WebGym (2601.02439) |
| P2 | 保持 agent/environment/reward/runtime 解耦 | scaffold 的核心接口拆为 `AgentPolicy`、`SearchEnvironment`、`ToolExecutor`、`MemoryManager`、`Reward/Evaluator`、`RolloutLogger`。不同环境和 reward 可以替换，不把 prompt、工具、评测、训练循环揉在一起。 | 多篇 framework/infrastructure 论文强调可插拔协议和后端互操作。解耦能降低新任务接入、调试和从 inference scaffold 迁移到 RL scaffold 的成本。 | OpenTinker (2601.07376), Agent-R1 (2511.14460), SkyRL-Agent (2511.16108) |

## 推荐的最小可落地改动

如果只能先改一版 scaffold，建议按以下顺序落地：

1. **Trajectory schema**：为每步 action 记录 query、result ids、extracted evidence、memory diff、cost/latency、diagnostic label、stop decision。
2. **Evidence ledger**：新增结构化证据表，最终答案必须从 evidence ledger 引用，不直接从完整上下文自由生成。
3. **Termination checker**：在 `finish` 前运行 coverage/sufficiency/repetition/conflict 检查，失败则生成下一步搜索建议。
4. **Intent/budget policy**：用轻量 classifier 或规则设置 task budget，并允许根据新证据动态调整。
5. **Offline eval harness**：用本地可验证语料和固定 SERP/cache 回放相同任务，比较不同 scaffold 策略的步数、证据覆盖和答案质量。

## 需要避免的实现陷阱

| 陷阱 | 为什么危险 | 对应防护 |
|---|---|---|
| 只做自然语言 summary memory | 摘要不可逆，容易丢证据来源、否定信息和未解决子问题。 | memory 中必须保留结构化 evidence ids 和 open questions。 |
| 只用最终答案分数评估 scaffold | 无法定位坏 query、坏阅读、坏压缩、坏停止。 | 引入 turn/action 级日志和诊断标签。 |
| 固定 max steps / 固定 source count | 简单任务浪费成本，复杂任务过早停止。 | intent-adaptive budget + evidence-aware termination。 |
| live web 直接做训练或主评测 | 成本、漂移、不可复现都会污染 reward 和回归结果。 | 先用 sandbox/cache/controlled corpus，live web 只做外推测试。 |
| 技能库只存成功轨迹 | 会强化已有模式，忽略失败恢复和探索价值。 | 同时保存失败原因、纠错动作和 utility/pruning 记录。 |
| 工具接口只支持文本 SERP | 后续接图像、网页、PDF、代码搜索时会重构成本高。 | 用 modality-agnostic observation/evidence abstraction。 |

## 论文覆盖映射

- Memory/context: MemSearcher, ContextBudget.
- Credit/process reward: CriticSearch, WebArbiter, ProMMSearchAgent, DR-MMSearchAgent, RewardFlow, AEM.
- Stopping/budget/trajectory analysis: Agentic Search in the Wild, Evaluating the Search Agent in a Parallel World, Dont Stop Early.
- Data/environment/evaluation: SearchGym, PaperSearchQA, SAGE, ORBIT, VSearcher, DynaWeb, WebGym.
- Framework/RL/infrastructure: Agent-R1, SkyRL-Agent, SORL, Demystifying RL, SLEA-RL, D2Skill, OpenTinker, ARL-Tangram, Heddle, Rethinking Agentic RL.
- User/action preference: DRACULA.
