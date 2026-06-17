from datetime import datetime, timezone

from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorDatabase

from database.connection import get_db


class ReportRepository:
    def __init__(self, db: AsyncIOMotorDatabase | None = None):
        self.collection = (db or get_db()).research_reports

    async def create(
        self,
        session_id: str,
        user_id: str,
        title: str,
        report: str,
        sources: list[dict],
    ) -> dict:
        now = datetime.now(timezone.utc)
        doc = {
            "session_id": session_id,
            "user_id": user_id,
            "title": title,
            "report": report,
            "sources": sources,
            "created_at": now,
        }
        result = await self.collection.insert_one(doc)
        doc["_id"] = str(result.inserted_id)
        return doc

    async def find_by_session_id(self, session_id: str) -> dict | None:
        doc = await self.collection.find_one({"session_id": session_id})
        if doc:
            doc["_id"] = str(doc["_id"])
        return doc

    async def find_by_user(self, user_id: str, limit: int = 10) -> list[dict]:
        cursor = self.collection.find({"user_id": user_id}).sort("created_at", -1).limit(limit)
        reports = []
        async for doc in cursor:
            doc["_id"] = str(doc["_id"])
            reports.append(doc)
        return reports

    async def search_by_user(self, user_id: str, search: str) -> list[dict]:
        cursor = self.collection.find(
            {
                "user_id": user_id,
                "$or": [
                    {"title": {"$regex": search, "$options": "i"}},
                    {"report": {"$regex": search, "$options": "i"}},
                ],
            }
        ).sort("created_at", -1)
        reports = []
        async for doc in cursor:
            doc["_id"] = str(doc["_id"])
            reports.append(doc)
        return reports

    async def delete_by_session_id(self, session_id: str, user_id: str) -> bool:
        result = await self.collection.delete_one({"session_id": session_id, "user_id": user_id})
        return result.deleted_count > 0
