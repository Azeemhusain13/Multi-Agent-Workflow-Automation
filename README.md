# 🕸️ Multi-Agent Workflow Automation  
A lightweight, modular multi-agent system that runs a Research → Summarize → Review pipeline using a directed workflow graph.  
The project includes a CLI runner, a Streamlit UI, and a FastAPI backend — making it easy to test, extend, or integrate with LLMs.

---

## 🚀 Features
- Modular agent design (plug in LLMs or custom logic)
- Directed workflow graph (DAG) execution using topological order  
- Shared memory object passed across agents  
- Deterministic baseline (no LLM required)  
- Streamlit UI for interactive testing  
- FastAPI endpoint for programmatic use  
- Trace logging for observing execution flow  

---

## 🗂️ Project Structure
multi-agent-workflow-automation/
│
├── run.py # CLI runner
├── streamlit_app.py # Streamlit UI
├── requirements.txt # Dependencies
├── .gitignore
│
└── src/
├── init.py
├── graph.py # Workflow orchestration (DAG)
├── agents.py # Research, Summarize, Review agents
└── api.py # FastAPI server
