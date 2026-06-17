import asyncio
from typing import Any

from duckduckgo_search import DDGS

from agents.groq_client import GroqClient

SYSTEM_PROMPT = """You are the Research Agent in a multi-agent research system.
Your job is to analyze search results and extract factual findings with evidence.
Do NOT write the final report. Only gather and organize data, facts, and sources."""


def _search_web(query: str, max_results: int = 5) -> list[dict]:
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=max_results))
            return [
                {
                    "title": r.get("title", ""),
                    "url": r.get("href", r.get("link", "")),
                    "snippet": r.get("body", r.get("snippet", "")),
                }
                for r in results
            ]
    except Exception:
        return []


async def run_research(
    query: str,
    plan: dict[str, Any],
    client: GroqClient | None = None,
) -> dict[str, Any]:
    groq = client or GroqClient()
    subtasks = plan.get("subtasks", [query])
    research_questions = plan.get("research_questions", [query])

    search_queries = list(dict.fromkeys(subtasks + research_questions))[:6]
    all_sources: list[dict] = []
    seen_urls: set[str] = set()

    for sq in search_queries:
        results = await asyncio.to_thread(_search_web, sq, 4)
        for r in results:
            url = r.get("url", "")
            if url and url not in seen_urls:
                seen_urls.add(url)
                all_sources.append(r)

    sources_text = "\n\n".join(
        f"Source: {s['title']}\nURL: {s['url']}\nSnippet: {s['snippet']}"
        for s in all_sources[:20]
    )

    result = await groq.chat_json(
        SYSTEM_PROMPT,
        f"""Original Query: {query}

Research Plan:
- Main Goal: {plan.get('main_goal', query)}
- Questions: {plan.get('research_questions', [])}
- Subtasks: {plan.get('subtasks', [])}

Web Search Results:
{sources_text or 'No web results found. Use your knowledge cautiously and note limitations.'}

Return JSON with this exact structure:
{{
  "findings": ["list of factual findings with context"],
  "sources": [{{"title": "string", "url": "string", "snippet": "string"}}],
  "evidence": ["list of evidence supporting each finding"]
}}

Use the web search results as primary sources. Include all relevant sources.""",
    )

    findings = result.get("findings", [])
    evidence = result.get("evidence", [])
    sources = result.get("sources", all_sources)

    if not sources and all_sources:
        sources = all_sources

    return {
        "findings": findings,
        "sources": sources,
        "evidence": evidence,
    }
