from datetime import datetime, timezone

from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorDatabase

from database.connection import get_db
from models.research import ResearchStatus


class SessionRepository:
    def __init__(self, db: AsyncIOMotorDatabase | None = None):
        self.collection = (db or get_db()).research_sessions

    async def create(self, user_id: str, query: str) -> dict:
        now = datetime.now(timezone.utc)
        doc = {
            "user_id": user_id,
            "query": query,
            "status": ResearchStatus.PENDING.value,
            "created_at": now,
            "updated_at": now,
        }
        result = await self.collection.insert_one(doc)
        doc["_id"] = str(result.inserted_id)
        return doc

    async def find_by_id(self, session_id: str) -> dict | None:
        if not ObjectId.is_valid(session_id):
            return None
        doc = await self.collection.find_one({"_id": ObjectId(session_id)})
        if doc:
            doc["_id"] = str(doc["_id"])
        return doc

    async def find_by_user(self, user_id: str, search: str | None = None) -> list[dict]:
        query: dict = {"user_id": user_id}
        cursor = self.collection.find(query).sort("created_at", -1)
        sessions = []
        async for doc in cursor:
            doc["_id"] = str(doc["_id"])
            sessions.append(doc)
        return sessions

    async def update_status(self, session_id: str, status: ResearchStatus) -> None:
        await self.collection.update_one(
            {"_id": ObjectId(session_id)},
            {"$set": {"status": status.value, "updated_at": datetime.now(timezone.utc)}},
        )

    async def delete(self, session_id: str, user_id: str) -> bool:
        result = await self.collection.delete_one(
            {"_id": ObjectId(session_id), "user_id": user_id}
        )
        return result.deleted_count > 0
