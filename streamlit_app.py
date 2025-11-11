import streamlit as st
import json
import sys, os

# Ensure local imports work when running `streamlit run streamlit_app.py`
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
if THIS_DIR not in sys.path:
    sys.path.insert(0, THIS_DIR)

from src.graph import Workflow
from src.agents import ResearchAgent, SummarizeAgent, ReviewAgent

st.set_page_config(page_title="Multi-Agent Workflow Automation", page_icon="🕸️")
st.title("🕸️ Multi-Agent Workflow Automation")
st.write("Research → Summarize → Review pipeline (deterministic baseline, LLM-pluggable).")

with st.sidebar:
    st.header("Pipeline")
    st.caption("The graph is fixed for this demo: research → summarize → review.")
    st.code("research -> summarize -> review", language="text")

query = st.text_input("Enter a query", value="Explain RAG in simple terms")
run_btn = st.button("Run Agents")

if run_btn and query.strip():
    wf = Workflow()
    wf.add_node("research", ResearchAgent())
    wf.add_node("summarize", SummarizeAgent())
    wf.add_node("review", ReviewAgent())
    wf.add_edge("research", "summarize")
    wf.add_edge("summarize", "review")

    result = wf.run({"query": query.strip()})
    st.subheader("Result JSON")
    st.json(result)

    st.subheader("Trace")
    st.write(" → ".join(result.get("trace", [])) or "No steps executed")

    st.subheader("Research Notes")
    for i, b in enumerate(result.get("research", []), start=1):
        st.write(f"{i}. {b}")

    st.subheader("Summary")
    st.write(result.get("summary", ""))

    st.subheader("Review")
    review = result.get("review", {})
    st.write(f"**Approved:** {review.get('approved', False)}")
    notes = review.get("notes", [])
    if notes:
        st.write("**Notes:**")
        for n in notes:
            st.write(f"- {n}")
else:
    st.info("Enter a query and click **Run Agents**.")
