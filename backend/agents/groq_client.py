import json
import re
from typing import Any

from groq import Groq

from utils.config import settings


class GroqClient:
    def __init__(self):
        self.client = Groq(api_key=settings.groq_api_key)
        self.model = settings.groq_model

    async def chat(self, system_prompt: str, user_prompt: str, temperature: float = 0.3) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=temperature,
            max_tokens=4096,
        )
        return response.choices[0].message.content or ""

    async def chat_json(self, system_prompt: str, user_prompt: str) -> dict[str, Any]:
        content = await self.chat(
            system_prompt + "\n\nRespond ONLY with valid JSON. No markdown fences.",
            user_prompt,
            temperature=0.2,
        )
        return _parse_json(content)


def _parse_json(content: str) -> dict[str, Any]:
    content = content.strip()
    if content.startswith("```"):
        content = re.sub(r"^```(?:json)?\n?", "", content)
        content = re.sub(r"\n?```$", "", content)
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", content, re.DOTALL)
        if match:
            return json.loads(match.group())
        raise ValueError("Failed to parse JSON from model response")
