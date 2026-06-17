from database.connection import get_db


async def create_indexes() -> None:
    db = get_db()

    await db.users.create_index("email", unique=True)

    await db.research_sessions.create_index("user_id")
    await db.research_sessions.create_index([("user_id", 1), ("created_at", -1)])

    await db.research_reports.create_index("session_id", unique=True)
    await db.research_reports.create_index("user_id")
    await db.research_reports.create_index([("user_id", 1), ("created_at", -1)])
    await db.research_reports.create_index([("user_id", 1), ("title", "text"), ("report", "text")])
