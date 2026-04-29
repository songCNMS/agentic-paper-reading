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

## 2. From Skills to Talent: Organising Heterogeneous Agents as a Real-World Company

- **arXiv:** 2604.22446
- **Type:** Multi-agent organization
- **Main innovation:** Introduces an organizational abstraction for agents, where portable "Talents" can be recruited, governed, composed, and improved like workers inside a company-like structure.
- **Summary:** The paper argues that multi-agent systems need an organizational layer beyond fixed workflows and isolated tool skills. It introduces OneManCompany, a framework that packages skills, tools, and runtime configuration into portable "Talents" and coordinates them through structures inspired by real company operations.
- **Agentic relevance:** Directly targets agent workforce management, role assignment, coordination, and persistent organizational learning.
- **Takeaway:** Multi-agent progress may require organization design primitives, not just stronger individual agents.

## 3. Recursive Multi-Agent Systems

- **arXiv:** 2604.25917
- **Type:** Multi-agent algorithm
- **Main innovation:** Extends recursive computation from single-model looped reasoning to multi-agent collaboration via latent-state transfer between agents.
- **Summary:** RecursiveMAS extends the idea of looped or recursive reasoning from a single model to a multi-agent setting. It uses recursive links to transfer latent states across heterogeneous agents and optimizes collaboration through inner and outer recursion loops.
- **Agentic relevance:** Offers a way to scale collaboration depth without relying only on explicit text messages between agents.
- **Takeaway:** Recursion can be a systems-level scaling axis for multi-agent reasoning, though its practical value depends on stable training and interpretable cross-agent state transfer.

## 4. Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms

- **arXiv:** 2604.23775
- **Type:** VLA / embodied safety survey
- **Main innovation:** Consolidates VLA safety into a dedicated threat/evaluation/mechanism framework that treats embodied action as qualitatively different from text-only LLM risk.
- **Summary:** This survey organizes safety risks for Vision-Language-Action models, where models perceive, reason, and act in physical environments. It highlights risks that are more severe than text-only LLM risks: irreversible physical consequences, multimodal attacks, real-time defense constraints, long-horizon error propagation, and vulnerable data pipelines.
- **Agentic relevance:** Highly relevant to embodied agents, robotics, and any system where LLM/VLM decisions become actions.
- **Takeaway:** VLA safety needs dedicated evaluations and mechanisms because physical action changes the risk model.

## 5. DV-World: Benchmarking Data Visualization Agents in Real-World Scenarios

- **arXiv:** 2604.25914
- **Type:** Benchmark / environment
- **Main innovation:** Builds a real-world data visualization benchmark spanning spreadsheet-native work, cross-library visualization evolution, and ambiguous multi-turn user interaction.
- **Summary:** DV-World evaluates data visualization agents across realistic professional workflows rather than simple chart-generation tasks. It covers spreadsheet-native manipulation, chart and dashboard creation, diagnostic repair, cross-platform visualization evolution, and multi-turn interaction under ambiguous user intent.
- **Agentic relevance:** Provides an environment for testing data-analysis and visualization agents on grounded, stateful, tool-like tasks.
- **Takeaway:** Visualization agents need to handle repair, intent alignment, and platform-specific constraints, not just emit plotting code.

## 6. Programming with Data: Test-Driven Data Engineering for Self-Improving LLMs from Raw Corpora

- **arXiv:** 2604.24819
- **Type:** Data engineering / self-improvement
- **Main innovation:** Treats LLM data engineering as test-driven programming, using shared structured knowledge to generate data, evaluate failures, and repair missing concepts.
- **Summary:** The paper maps data engineering for LLM fine-tuning onto a software-development lifecycle. It uses structured knowledge extracted from raw corpora as a shared basis for generating training data, building tests, diagnosing failures, and repairing data gaps.
- **Agentic relevance:** Relevant to self-improving LLM systems that need closed-loop data generation, evaluation, and debugging.
- **Takeaway:** Domain adaptation should be diagnostic and test-driven; blindly adding more synthetic data is less effective than targeted data repair.

## 7. ClawMark: A Living-World Benchmark for Multi-Turn, Multi-Day, Multimodal Coworker Agents

- **arXiv:** 2604.23781
- **Type:** Long-horizon benchmark
- **Main innovation:** Introduces a living-world benchmark where coworker agents operate across multiple days while sandbox services and multimodal evidence change between turns.
- **Summary:** ClawMark evaluates persistent coworker agents across multi-turn, multi-day tasks in a stateful sandbox. The environment changes between turns, and evidence can appear in emails, calendars, knowledge bases, images, scanned PDFs, audio, video, and spreadsheets.
- **Agentic relevance:** Directly tests long-horizon agent behavior under changing state, multimodal evidence, and delayed consequences.
- **Takeaway:** Persistent coworker agents need robust memory, state tracking, and evidence grounding across days, not just single-session task completion.

## 8. AutoResearchBench: Benchmarking AI Agents on Complex Scientific Literature Discovery

- **arXiv:** 2604.25256
- **Type:** Research-agent benchmark
- **Main innovation:** Separates scientific literature discovery into deep target-paper search and wide comprehensive literature collection, exposing failures distinct from generic web search.
- **Summary:** AutoResearchBench measures autonomous scientific literature discovery. It includes deep research tasks, where agents must progressively locate a specific target paper, and wide research tasks, where agents must comprehensively collect relevant literature for a topic.
- **Agentic relevance:** Strong benchmark for research agents, search planning, hypothesis-space management, and iterative reflection.
- **Takeaway:** Scientific search is not just web browsing; agents must handle long natural-language queries, paper-level evidence, completeness, and iterative strategy refinement.

## 9. Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis

- **arXiv:** 2604.24198
- **Type:** Process reward modeling
- **Main innovation:** Designs an environment-grounded process reward model for data-analysis agents that can reward productive exploration and catch silent analytical errors.
- **Summary:** The paper studies why general process reward models fail for data-analysis agents: they miss silent analytical errors and may penalize necessary exploratory actions. It introduces DataPRM, an environment-grounded process reward model for step-level supervision in dynamic data analysis.
- **Agentic relevance:** Directly supports RL/training of data-analysis agents with process-level feedback rather than only final-answer rewards.
- **Takeaway:** Agentic data analysis requires reward models that understand exploration, executable checks, and silent failure modes.

## 10. Contexts are Never Long Enough: Structured Reasoning for Scalable Question Answering over Long Document Sets

- **arXiv:** 2604.22294
- **Type:** Long-document reasoning / retrieval
- **Main innovation:** Replaces long-context chunk aggregation with schema-driven extraction into relational structures for scalable, auditable document-set QA.
- **Summary:** The paper introduces SLIDERS, a framework for question answering over large document collections. Instead of stuffing chunks into context, it extracts salient information into a relational structure and performs structured reasoning over that representation.
- **Agentic relevance:** Relevant to research and document-analysis agents that must operate beyond fixed context windows.
- **Takeaway:** For large document sets, agents need external structured memory and queryable intermediate representations, not just longer prompts.

## 11. Taming Actor-Observer Asymmetry in Agents via Dialectical Alignment

- **arXiv:** 2604.19548
- **Type:** Agent alignment / reflection
- **Main innovation:** Identifies actor-observer asymmetry as a measurable bias in agent self-reflection and mutual auditing, then mitigates it with dialectical alignment.
- **Summary:** The paper identifies actor-observer asymmetry in role-based agent systems: an acting agent tends to blame failures on external factors, while an observing agent attributes similar failures to the actor. It proposes dialectical alignment to make judgments more evidence-grounded and consistent.
- **Agentic relevance:** Important for self-reflection, audit agents, debate systems, and multi-agent error attribution.
- **Takeaway:** Multi-agent review can introduce cognitive-bias-like failure modes; agent critique needs alignment, not just more roles.

## 12. Efficient Agent Evaluation via Diversity-Guided User Simulation

- **arXiv:** 2604.21480
- **Type:** Agent evaluation
- **Main innovation:** Uses diversity-guided simulated users to actively cover multi-turn interaction failure modes while reducing evaluation cost.
- **Summary:** The paper proposes a user-simulation approach for evaluating LLM agents in stochastic, multi-turn settings. Diversity-guided simulation selects or generates varied user behaviors to cover failure modes more efficiently.
- **Agentic relevance:** Useful for evaluating deployed conversational and task agents without relying solely on expensive human traffic.
- **Takeaway:** Agent evaluation should actively search the user-behavior space instead of passively sampling a small set of scripted interactions.

## 13. AgentSearchBench: A Benchmark for AI Agent Search in the Wild

- **arXiv:** 2604.22436
- **Type:** Agent-discovery benchmark
- **Main innovation:** Frames agent selection itself as a benchmarked search problem over compositional and evolving AI-agent capabilities.
- **Summary:** AgentSearchBench studies the problem of finding appropriate AI agents for a task. Unlike ordinary tool retrieval, agent selection must reason about compositional, evolving capabilities and task fit.
- **Agentic relevance:** Addresses a meta-agent problem: agents that search for, select, and delegate to other agents.
- **Takeaway:** As agent ecosystems grow, discovering the right agent becomes its own benchmarkable capability.

## 14. Memanto: Typed Semantic Memory with Information-Theoretic Retrieval for Long-Horizon Agents

- **arXiv:** 2604.22085
- **Type:** Agent memory
- **Main innovation:** Proposes typed semantic memory with information-theoretic retrieval so long-horizon agents retrieve task-relevant memories rather than raw logs.
- **Summary:** Memanto targets memory as a bottleneck for persistent multi-session agents. It proposes typed semantic memory and information-theoretic retrieval to decide what stored information is useful for a current long-horizon task.
- **Agentic relevance:** Directly relevant to memory architectures for autonomous assistants and long-running agents.
- **Takeaway:** Agent memory should be typed and selectively retrieved; raw conversation logs are not enough for long-horizon autonomy.

## 15. Co-Director: Agentic Generative Video Storytelling

- **arXiv:** 2604.24842
- **Type:** Agentic content generation
- **Main innovation:** Turns video generation into a coordinated agentic workflow for story planning, scene continuity, and iterative correction across clips.
- **Summary:** Co-Director frames video storytelling as an agentic generation problem. Instead of generating isolated clips, the system coordinates planning, scene structure, consistency, and iterative video generation to produce coherent stories.
- **Agentic relevance:** Shows how agent orchestration can wrap generative models for multi-step creative production.
- **Takeaway:** Agentic pipelines are useful when generation requires planning, continuity, and correction across many artifacts.

## 16. Toward Scalable Terminal Task Synthesis via Skill Graphs

- **arXiv:** 2604.25727
- **Type:** Environment / task synthesis
- **Main innovation:** Uses skill graphs to synthesize diverse command-line tasks that compose terminal skills systematically.
- **Summary:** The paper addresses the shortage of diverse, high-quality terminal-agent training tasks. It uses skill graphs to compose command-line skills into scalable terminal task synthesis.
- **Agentic relevance:** Directly supports training and evaluation of agents that operate in shell or developer environments.
- **Takeaway:** Good terminal agents need systematically generated tasks that cover compositional command-line skills.

## 17. Stabilizing Efficient Reasoning with Step-Level Advantage Selection

- **arXiv:** 2604.24003
- **Type:** Reasoning RL algorithm
- **Main innovation:** Selects useful reasoning steps with advantage signals to stabilize training toward compact, high-value reasoning traces.
- **Summary:** The paper tackles inefficient long reasoning traces in LLMs. It proposes selecting useful reasoning steps using advantage-style signals so training can reward compact, effective reasoning rather than verbosity.
- **Agentic relevance:** Relevant to agent policies that must reason under compute budgets and avoid long, low-value traces.
- **Takeaway:** Step-level credit assignment is a practical lever for efficient reasoning and agent RL stability.

## 18. TCOD: Exploring Temporal Curriculum in On-Policy Distillation for Multi-turn Autonomous Agents

- **arXiv:** 2604.24005
- **Type:** Multi-turn agent training
- **Main innovation:** Adds a temporal curriculum to on-policy distillation so student agents learn trajectory structure across multi-turn interactions.
- **Summary:** TCOD studies on-policy distillation for multi-turn autonomous agents and introduces temporal curriculum ideas for transferring behavior from stronger models to smaller students over interactive trajectories.
- **Agentic relevance:** Directly related to training smaller multi-turn agents from stronger teachers while preserving sequential behavior.
- **Takeaway:** Distillation for agents should respect temporal structure; static input-output imitation misses important trajectory dynamics.

## 19. PageGuide: Browser extension to assist users in navigating a webpage and locating information

- **arXiv:** 2604.23772
- **Type:** Browser / web-assistance agent
- **Main innovation:** Implements page-grounded browser assistance that combines webpage understanding with user navigation and information-location intent.
- **Summary:** PageGuide is a browser extension for helping users locate information and navigate cluttered webpages. It targets multi-step browsing assistance where the system must understand webpage structure and user intent.
- **Agentic relevance:** Relevant to web navigation agents, browser automation, and human-in-the-loop assistance.
- **Takeaway:** Browser agents need page-grounded interaction and user intent tracking, not just general text QA.

## 20. Zero-to-CAD: Agentic Synthesis of Interpretable CAD Programs at Million-Scale Without Real Data

- **arXiv:** 2604.24479
- **Type:** Synthetic data / CAD agents
- **Main innovation:** Generates million-scale interpretable CAD construction programs agentically, bypassing the scarcity of real parametric CAD histories.
- **Summary:** Zero-to-CAD generates interpretable CAD construction programs at large scale without relying on real CAD histories. It treats CAD models as procedural recipes and uses agentic synthesis to create useful training data.
- **Agentic relevance:** Relevant to agents that generate structured programs and design artifacts through procedural planning.
- **Takeaway:** Agentic synthesis can produce scalable structured datasets where real expert traces are scarce.

## 21. EmbodiedMidtrain: Bridging the Gap between Vision-Language Models and Vision-Language-Action Models via Mid-training

- **arXiv:** 2604.20012
- **Type:** Embodied / VLA training
- **Main innovation:** Selects VLM mid-training data by proximity to VLA action-domain features, bridging perception-language pretraining and embodied control.
- **Summary:** EmbodiedMidtrain addresses the distribution gap between VLM pretraining data and VLA action data. It selects VLM data closer to the embodied-action domain and uses it for mid-training before downstream VLA training.
- **Agentic relevance:** Helps adapt general vision-language models into embodied action policies.
- **Takeaway:** VLA performance depends heavily on bridging the data-distribution gap between perception-language pretraining and action-conditioned deployment.

## 22. ProEval: Proactive Failure Discovery and Efficient Performance Estimation for Generative AI Evaluation

- **arXiv:** 2604.23099
- **Type:** Evaluation methodology
- **Main innovation:** Applies transfer-learned Gaussian-process surrogates and active sampling to estimate performance and discover failures with far fewer evaluations.
- **Summary:** ProEval uses transfer learning and Bayesian methods to estimate model performance and discover failure cases with fewer samples. It frames performance estimation and failure discovery as active, uncertainty-aware evaluation problems.
- **Agentic relevance:** Useful for evaluating expensive agents where each rollout or rating is costly.
- **Takeaway:** Evaluation should be proactive and sample-efficient, especially for agents with slow inference and many possible failure modes.

## 23. dWorldEval: Scalable Robotic Policy Evaluation via Discrete Diffusion World Model

- **arXiv:** 2604.22152
- **Type:** Robotic policy evaluation / world model
- **Main innovation:** Uses a discrete diffusion world model as an action-conditioned proxy evaluator for ranking robotic policies at scale.
- **Summary:** dWorldEval uses a discrete diffusion world model as a scalable proxy for evaluating robotic policies. It maps vision, language, and actions into a unified token space and generates long-horizon rollouts for policy ranking.
- **Agentic relevance:** Provides a world-model-based evaluation path for embodied agents where real-world rollouts are expensive.
- **Takeaway:** Scalable embodied-agent evaluation will likely depend on controllable, action-conditioned world models.

## 24. GoClick: Lightweight Element Grounding Model for Autonomous GUI Interaction

- **arXiv:** 2604.23941
- **Type:** GUI agent component
- **Main innovation:** Builds a 230M-parameter GUI element grounding VLM optimized for low-latency, on-device autonomous GUI interaction.
- **Summary:** GoClick is a compact GUI grounding model that locates screen elements from natural-language instructions. Its small parameter count targets low-latency, on-device GUI operation.
- **Agentic relevance:** Element grounding is a core primitive for computer-use and mobile agents.
- **Takeaway:** GUI agents benefit from specialized lightweight perception modules instead of relying only on large general VLMs.

## 25. AutoGUI-v2: A Comprehensive Multi-Modal GUI Functionality Understanding Benchmark

- **arXiv:** 2604.24441
- **Type:** GUI benchmark
- **Main innovation:** Evaluates GUI functionality and state-transition understanding, going beyond static grounding toward predictive digital-world modeling.
- **Summary:** AutoGUI-v2 evaluates whether models understand GUI functionality and state transitions, not just static element locations. It tests context-aware functionality understanding at region and element levels.
- **Agentic relevance:** Direct benchmark for digital autonomy and GUI-control agents.
- **Takeaway:** GUI grounding and GUI reasoning diverge; locating a button is easier than predicting what interacting with it will do.

## 26. Improving Vision-language Models with Perception-centric Process Reward Models

- **arXiv:** 2604.24583
- **Type:** Multimodal process reward modeling
- **Main innovation:** Introduces Perceval, a perception-centric PRM that decomposes visual reasoning into claims and localizes image-grounding errors.
- **Summary:** The paper introduces Perceval, a perception-centric process reward model that detects image-text misalignment inside VLM reasoning chains. It grounds token-level or claim-level perceptual errors instead of giving only outcome-level rewards.
- **Agentic relevance:** Supports RL and test-time correction for multimodal agents that reason from visual evidence.
- **Takeaway:** Multimodal agents need process feedback that can localize perceptual mistakes, not just final correctness labels.

## 27. IndustryAssetEQA: A Neurosymbolic Operational Intelligence System for Embodied Question Answering in Industrial Asset Maintenance

- **arXiv:** 2604.23446
- **Type:** Embodied QA / industrial environment
- **Main innovation:** Combines telemetry, FMEA knowledge graphs, and LLM QA into a neurosymbolic operational intelligence system with provenance and counterfactual support.
- **Summary:** IndustryAssetEQA combines telemetry, knowledge graphs, and LLM interaction for industrial maintenance QA. It focuses on grounded operational reasoning, provenance, failure diagnosis, and counterfactual/action-oriented support.
- **Agentic relevance:** Relevant to embodied enterprise agents in safety-critical industrial settings.
- **Takeaway:** Operational agents need neurosymbolic grounding and verifiable provenance before their recommendations can be trusted.

## 28. Discovering Agentic Safety Specifications from 1-Bit Danger Signals

- **arXiv:** 2604.23210
- **Type:** Agent safety algorithm
- **Main innovation:** Shows that agents can iteratively infer natural-language safety specifications from only sparse one-bit danger feedback.
- **Summary:** EPO-Safe asks whether LLM agents can infer hidden safety objectives from sparse binary danger warnings. Agents generate plans, observe one-bit danger feedback, reflect, and update natural-language safety specifications.
- **Agentic relevance:** Directly studies safety learning from sparse experience, a core problem for autonomous agents.
- **Takeaway:** Natural-language specifications can act as persistent safety memory, but the setting still assumes structured environments and relatively clean feedback.

## 29. Emergent Strategic Reasoning Risks in AI: A Taxonomy-Driven Evaluation Framework

- **arXiv:** 2604.22119
- **Type:** Agentic risk evaluation
- **Main innovation:** Builds ESRRSim, a taxonomy-driven generator for strategic-risk scenarios with paired rubrics for visible responses and hidden reasoning traces.
- **Summary:** The paper defines emergent strategic reasoning risks such as deception, evaluation gaming, and reward hacking. It introduces ESRRSim, a taxonomy-driven framework for generating scenarios and rubrics to evaluate these behaviors.
- **Agentic relevance:** Highly relevant to agent safety as models become more goal-directed and deployment-scoped.
- **Takeaway:** Strategic-risk evaluation needs scenario generation plus separate evaluation of model responses and reasoning traces.

## 30. AgriIR: A Scalable Framework for Domain-Specific Knowledge Retrieval

- **arXiv:** 2604.16353
- **Type:** Domain RAG / retrieval-agent infrastructure
- **Main innovation:** Decomposes domain RAG into declarative modules for query refinement, sub-query planning, retrieval, synthesis, citation grounding, and evaluation.
- **Summary:** AgriIR is a modular RAG framework for grounded domain-specific answers, demonstrated on Indian agricultural information access. It decomposes retrieval into query refinement, sub-query planning, retrieval, synthesis, and evaluation.
- **Agentic relevance:** Provides practical infrastructure for domain-specialized retrieval agents under low-compute constraints.
- **Takeaway:** Reliable domain agents need modular retrieval, citation grounding, and evaluation hooks more than monolithic large models.

## 31. DiagramBank: A Large-scale Dataset of Diagram Design Exemplars with Paper Metadata for Retrieval-Augmented Generation

- **arXiv:** 2604.20857
- **Type:** Dataset / RAG support for AI-scientist agents
- **Main innovation:** Creates a retrieval-oriented corpus of scientific schematic diagrams linked to paper metadata for exemplar-based diagram generation.
- **Summary:** DiagramBank collects a large corpus of scientific diagram exemplars with paper metadata for retrieval-augmented diagram generation. It targets the gap where AI scientist systems can write text and code but struggle with publication-grade conceptual figures.
- **Agentic relevance:** Supports end-to-end scientific agents that must produce papers, diagrams, and explanatory artifacts.
- **Takeaway:** Scientific-agent pipelines need artifact-specific retrieval datasets, not just text-generation components.
