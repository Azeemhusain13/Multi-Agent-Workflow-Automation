# Multi-Agent Workflow Automation (LangGraph-style)

A minimal, production-friendly scaffold for multi-step agent workflows (Research → Summarize → Review).

## Highlights
- Declarative DAG of tasks
- Memory passed between nodes
- Deterministic local agents (easily swappable with LLMs)
- CLI & HTTP runner

## Quick Start
```bash
pip install -r requirements.txt
python run.py --query "Explain RAG in simple terms"
```
