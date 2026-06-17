from typing import Any

from agents.groq_client import GroqClient

SYSTEM_PROMPT = """You are the Planner Agent in a multi-agent research system.
Your job is to understand the user's research query and create a structured research plan.
Break the problem into subtopics, generate research questions, and create actionable subtasks.
Do NOT perform research or write the final report. Only plan."""


async def run_planner(query: str, client: GroqClient | None = None) -> dict[str, Any]:
    groq = client or GroqClient()
    result = await groq.chat_json(
        SYSTEM_PROMPT,
        f"""Research Query: {query}

Return JSON with this exact structure:
{{
  "main_goal": "string - the primary objective",
  "research_questions": ["list of specific questions to answer"],
  "subtasks": ["list of actionable research subtasks"]
}}""",
    )
    return {
        "main_goal": result.get("main_goal", query),
        "research_questions": result.get("research_questions", []),
        "subtasks": result.get("subtasks", []),
    }
