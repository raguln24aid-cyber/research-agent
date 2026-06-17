from typing import Any, TypedDict

from langgraph.graph import END, START, StateGraph

from agents.groq_client import GroqClient
from agents.planner import run_planner
from agents.report import run_report
from agents.research_agent import run_research
from agents.review import run_review


class ResearchState(TypedDict, total=False):
    query: str
    plan: dict[str, Any]
    research_data: dict[str, Any]
    review_data: dict[str, Any]
    report_data: dict[str, str]
    title: str
    report: str
    sources: list[dict]


async def planner_node(state: ResearchState) -> dict[str, Any]:
    client = GroqClient()
    plan = await run_planner(state["query"], client)
    return {"plan": plan}


async def research_node(state: ResearchState) -> dict[str, Any]:
    client = GroqClient()
    research_data = await run_research(state["query"], state["plan"], client)
    return {"research_data": research_data}


async def review_node(state: ResearchState) -> dict[str, Any]:
    client = GroqClient()
    review_data = await run_review(state["query"], state["research_data"], client)
    return {"review_data": review_data}


async def report_node(state: ResearchState) -> dict[str, Any]:
    client = GroqClient()
    report_data = await run_report(
        state["query"],
        state["plan"],
        state["review_data"],
        client,
    )
    review_data = state["review_data"]
    research_data = state.get("research_data", {})
    sources = review_data.get("validated_sources", research_data.get("sources", []))

    return {
        "report_data": report_data,
        "title": report_data["title"],
        "report": report_data["report"],
        "sources": sources,
    }


def build_research_graph():
    graph = StateGraph(ResearchState)

    graph.add_node("planner_agent", planner_node)
    graph.add_node("research_agent", research_node)
    graph.add_node("review_agent", review_node)
    graph.add_node("report_agent", report_node)

    graph.add_edge(START, "planner_agent")
    graph.add_edge("planner_agent", "research_agent")
    graph.add_edge("research_agent", "review_agent")
    graph.add_edge("review_agent", "report_agent")
    graph.add_edge("report_agent", END)

    return graph.compile()


_research_graph = None


def get_research_graph():
    global _research_graph
    if _research_graph is None:
        _research_graph = build_research_graph()
    return _research_graph


async def run_research_pipeline(query: str) -> dict[str, Any]:
    graph = get_research_graph()
    result = await graph.ainvoke({"query": query})

    return {
        "title": result["title"],
        "report": result["report"],
        "sources": result["sources"],
        "plan": result["plan"],
        "research": result["research_data"],
        "review": result["review_data"],
    }
