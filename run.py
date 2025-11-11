import argparse, json
from src.graph import Workflow
from src.agents import ResearchAgent, SummarizeAgent, ReviewAgent

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--query", required=True, help="User query")
    args = p.parse_args()

    wf = Workflow()
    wf.add_node("research", ResearchAgent())
    wf.add_node("summarize", SummarizeAgent())
    wf.add_node("review", ReviewAgent())

    wf.add_edge("research", "summarize")
    wf.add_edge("summarize", "review")

    result = wf.run({"query": args.query})
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
