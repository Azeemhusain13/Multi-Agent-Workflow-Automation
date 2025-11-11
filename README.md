# Multi-Agent Workflow Automation (LangGraph-style)

A minimal, production-friendly scaffold for multi-step agent workflows (Research → Summarize → Review).

## Highlights
- Declarative DAG of tasks
- Memory passed between nodes
- Deterministic local agents (easily swappable with LLMs)
- CLI & HTTP runner<img width="839" height="589" alt="Screenshot 2025-11-12 at 1 09 12 AM" src="https://github.com/user-attachments/assets/17a2bad9-b42e-4643-a428-15860c6b0648" />


## Quick Start
```bash
pip install -r requirements.txt
python run.py --query "Explain RAG in simple terms"
```
<img width="882" height="678" alt="Screenshot 2025-11-12 at 1 09 01 AM" src="https://github.com/user-attachments/assets/6c0330b3-cf74-4d0e-82ba-3914d5e362a0" />
