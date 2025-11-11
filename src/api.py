from fastapi import FastAPI
from pydantic import BaseModel
from .graph import Workflow
from .agents import ResearchAgent, SummarizeAgent, ReviewAgent

app = FastAPI()

class Query(BaseModel):
    query: str

@app.post("/run")
def run(q: Query):
    wf = Workflow()
    wf.add_node("research", ResearchAgent())
    wf.add_node("summarize", SummarizeAgent())
    wf.add_node("review", ReviewAgent())
    wf.add_edge("research","summarize")
    wf.add_edge("summarize","review")
    result = wf.run({"query": q.query})
    return result
