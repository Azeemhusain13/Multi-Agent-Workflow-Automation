from typing import Dict
import re

class ResearchAgent:
    def __call__(self, mem: Dict) -> Dict:
        q = mem.get("query","")
        # Deterministic pseudo-research (replace with web + LLM)
        bullets = [
            f"{q} involves combining retrieval with generation.",
            "Retriever fetches relevant chunks using embeddings or BM25.",
            "Generator (LLM) conditions on retrieved context to answer.",
            "Improves factuality vs. pure prompting."
        ]
        mem["research"] = bullets
        return mem

class SummarizeAgent:
    def __call__(self, mem: Dict) -> Dict:
        pts = mem.get("research", [])
        summary = " ".join(pts)
        mem["summary"] = summary
        return mem

class ReviewAgent:
    def __call__(self, mem: Dict) -> Dict:
        s = mem.get("summary","")
        issues = []
        if len(s.split()) < 30:
            issues.append("Summary may be too short; add detail or examples.")
        if not re.search(r"retriev|embed|index", s, re.I):
            issues.append("Consider mentioning embeddings/indexing explicitly.")
        mem["review"] = {"approved": len(issues)==0, "notes": issues}
        return mem
