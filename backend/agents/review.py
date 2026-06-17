from typing import Any

from agents.groq_client import GroqClient

SYSTEM_PROMPT = """You are the Review Agent in a multi-agent research system.
Your job is to verify findings, remove duplicates, assess source quality,
identify gaps, and improve factual consistency.
Do NOT write the final report. Only validate and refine the research data."""


async def run_review(
    query: str,
    research_data: dict[str, Any],
    client: GroqClient | None = None,
) -> dict[str, Any]:
    groq = client or GroqClient()
    result = await groq.chat_json(
        SYSTEM_PROMPT,
        f"""Original Query: {query}

Research Data:
- Findings: {research_data.get('findings', [])}
- Sources: {research_data.get('sources', [])}
- Evidence: {research_data.get('evidence', [])}

Return JSON with this exact structure:
{{
  "validated_findings": ["deduplicated and verified findings"],
  "validated_sources": [{{"title": "string", "url": "string", "snippet": "string", "quality": "high|medium|low"}}],
  "gaps": ["list of missing information or areas needing more research"]
}}""",
    )

    return {
        "validated_findings": result.get("validated_findings", research_data.get("findings", [])),
        "validated_sources": result.get("validated_sources", research_data.get("sources", [])),
        "gaps": result.get("gaps", []),
    }
