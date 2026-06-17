from typing import Any

from agents.groq_client import GroqClient

SYSTEM_PROMPT = """You are the Report Agent in a multi-agent research system.
Create a professional, comprehensive research report in Markdown format.
Use clear headings, bullet points where appropriate, and cite sources.
Be objective, analytical, and thorough."""


async def run_report(
    query: str,
    plan: dict[str, Any],
    review_data: dict[str, Any],
    client: GroqClient | None = None,
) -> dict[str, str]:
    groq = client or GroqClient()
    report = await groq.chat(
        SYSTEM_PROMPT,
        f"""Create a professional research report for the following query.

Query: {query}

Research Plan:
- Main Goal: {plan.get('main_goal', query)}
- Research Questions: {plan.get('research_questions', [])}

Validated Findings:
{review_data.get('validated_findings', [])}

Validated Sources:
{review_data.get('validated_sources', [])}

Identified Gaps:
{review_data.get('gaps', [])}

Structure the report EXACTLY with these sections:

# Executive Summary

# Background

# Key Findings

# Analysis

# Risks

# Recommendations

# Conclusion

# Sources

Write in professional markdown. Include source URLs in the Sources section.
Also provide a concise title for this report on the first line as: TITLE: <title>""",
        temperature=0.4,
    )

    title = query[:80]
    if "TITLE:" in report:
        title_line = report.split("\n")[0]
        title = title_line.replace("TITLE:", "").strip()
        report = "\n".join(report.split("\n")[1:]).strip()

    return {"title": title, "report": report}
