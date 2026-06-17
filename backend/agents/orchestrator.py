from typing import Any

from agents.groq_client import GroqClient
from agents.planner import run_planner
from agents.report import run_report
from agents.research_agent import run_research
from agents.review import run_review


async def run_research_pipeline(query: str) -> dict[str, Any]:
    client = GroqClient()

    plan = await run_planner(query, client)
    research_data = await run_research(query, plan, client)
    review_data = await run_review(query, research_data, client)
    report_data = await run_report(query, plan, review_data, client)

    sources = review_data.get("validated_sources", research_data.get("sources", []))

    return {
        "title": report_data["title"],
        "report": report_data["report"],
        "sources": sources,
        "plan": plan,
        "research": research_data,
        "review": review_data,
    }
