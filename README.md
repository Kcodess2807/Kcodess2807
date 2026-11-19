<p align="center">
  <img src="./header.svg" alt="Arush Karnatak, AI engineer. Agent infrastructure, memory for agents, and inference." width="820"/>
</p>

I'm an AI engineer and a B.Tech IT student (GGSIPU, class of 2027). Most of my work is the
infrastructure around a model: how an agent is orchestrated, what it remembers, and how you
check that it remembered the right thing.

<p align="center">
  <img src="./assets/stack.svg" alt="Where I work in the agent stack: orchestration and memory shipped, payments some, inference learning now." width="820"/>
</p>

## Featured work

<a href="https://github.com/Kcodess2807/graphsight">
  <img src="./assets/graphsight.svg" alt="Graphsight: a remembered fact is replaced, and the old one is ended and kept as history." width="820"/>
</a>

### [Graphsight](https://github.com/Kcodess2807/graphsight): project memory for coding agents

It turns a repo's GitHub history into a typed graph, then lets an agent add the team facts
GitHub doesn't hold. A tracer shows what the agent retrieved and what it actually used.

- **Memory an agent can correct.** Facts are stored as subject, relation, object. A changed
  fact ends the old one and keeps it as history, and a retracted fact stops being recalled.
- **A source on every fact.** The model is always told which facts were read from GitHub and
  which an agent was told.
- **Measured, with the misses published.** Tasks are written before any run and graded by
  exact match. On held-out tasks, memory took correct answers from 5 of 22 to 16 of 22.
- **Shipped.** The tracer and viewer are on PyPI, with an MCP server and a LangGraph adapter.

`Python` `LadybugDB` `LangGraph` `MCP` `FastAPI` `React`
&nbsp;[Code](https://github.com/Kcodess2807/graphsight) · [PyPI](https://pypi.org/project/graphsight/) · [Site](https://trace-rag.vercel.app/) · [Eval](https://github.com/Kcodess2807/graphsight/tree/main/backend/eval)

<br/>

<a href="https://saadho.arushk.tech">
  <img src="./assets/saadho.svg" alt="Saadho: a day-by-day interview prep plan, with a voice practice room." width="820"/>
</a>

### [Saadho](https://saadho.arushk.tech): AI/ML interview prep, day by day

Give it a role, an interview date and your daily hours, and it builds the plan. It's live,
and people use it.

- **A plan, in order.** 300+ vetted resources sequenced by prerequisite, with what to skip.
- **Company guides.** How 200+ companies interview, round by round, with sources.
- **A voice practice room.** A group discussion with four AI colleagues in English or
  Hinglish, then a scorecard that quotes your own words.
- **Next:** a native Android app that shares one account and one backend with the web.

`Next.js` `Supabase` `LLM agents` `Realtime voice`
&nbsp;[Live site](https://saadho.arushk.tech)

## More work

| Project | What it is |
|---|---|
| **[SmartFlow](https://smartflow-sigma.vercel.app/)** | A reinforcement-learning traffic-signal controller. Cuts average waiting time about 55% against a fixed-time controller, and extends to a multi-agent 2x2 grid with emergency-vehicle preemption. `SUMO` `PPO/DQN` · [Code](https://github.com/Kcodess2807/SMARTFLOW) |
| **[Bodhi](https://github.com/Kcodess2807/Bodhi)** | A voice-first AI mock interviewer: an adaptive pipeline, RAG over 10K+ chunks, and real-time proctoring. `LangGraph` `pgvector` `YOLOv8` |
| **[PADHO](https://github.com/Kcodess2807/PADHO)** | Agents with hierarchical orchestration and RAG, in pure Python with no framework. |
| **[venvctl](https://github.com/Kcodess2807/venvctl)** | A single-binary Windows CLI that manages Python virtual environments across PowerShell, CMD and Git Bash. `Go` |
| **[ReAct-CLI](https://github.com/Kcodess2807/ReaAct-CLI)** | A small command-line implementation of the ReAct loop: reason, act, observe. |

## Learning now: inference engineering

I'm working down the stack, from agents to how the model is actually served: batching,
quantization, KV caching, and serving engines like llama.cpp, TensorRT-LLM and SGLang.
Notes and experiments go in
[inference-engineering0to100](https://github.com/Kcodess2807/inference-engineering0to100).

## Background

- Built ML pipelines processing 10,000+ aerial images a day at Kanchan Drones.
- Built a real-time exam-proctoring system holding sub-200ms latency on GCP.
- Shipped a policy-aware RAG chatbot that answers in under a second.
- Taught an 8-week NLP course to 20+ students.
- 5 national hackathon finals, 2 first-place wins.

## Find me

<p align="left">
  <a href="https://www.linkedin.com/in/arush-karnatak-894bb52a1/"><img src="https://img.shields.io/badge/LinkedIn-0D1117?style=for-the-badge&logo=linkedin&logoColor=C8F169" alt="LinkedIn"/></a>
  <a href="https://x.com/Kcodess"><img src="https://img.shields.io/badge/X-0D1117?style=for-the-badge&logo=x&logoColor=C8F169" alt="X"/></a>
  <a href="https://arushk.vercel.app/"><img src="https://img.shields.io/badge/Portfolio-0D1117?style=for-the-badge&logo=googlechrome&logoColor=C8F169" alt="Portfolio"/></a>
  <a href="mailto:arushkarnatak1881@gmail.com"><img src="https://img.shields.io/badge/Email-0D1117?style=for-the-badge&logo=gmail&logoColor=C8F169" alt="Email"/></a>
</p>

![GitHub contribution graph](https://ghchart.rshah.org/34D399/kcodess2807)
