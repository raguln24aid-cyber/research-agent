from datetime import datetime, timezone

from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorDatabase

from database.connection import get_db


class UserRepository:
    def __init__(self, db: AsyncIOMotorDatabase | None = None):
        self.collection = (db or get_db()).users

    async def create(self, name: str, email: str, hashed_password: str) -> dict:
        now = datetime.now(timezone.utc)
        doc = {
            "name": name,
            "email": email.lower(),
            "hashed_password": hashed_password,
            "created_at": now,
        }
        result = await self.collection.insert_one(doc)
        doc["_id"] = str(result.inserted_id)
        return doc

    async def find_by_email(self, email: str) -> dict | None:
        doc = await self.collection.find_one({"email": email.lower()})
        if doc:
            doc["_id"] = str(doc["_id"])
        return doc

    async def find_by_id(self, user_id: str) -> dict | None:
        if not ObjectId.is_valid(user_id):
            return None
        doc = await self.collection.find_one({"_id": ObjectId(user_id)})
        if doc:
            doc["_id"] = str(doc["_id"])
        return doc
