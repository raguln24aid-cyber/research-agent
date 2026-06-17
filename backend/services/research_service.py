import asyncio
import logging

from agents.orchestrator import run_research_pipeline
from database.repositories.report_repository import ReportRepository
from database.repositories.session_repository import SessionRepository
from models.research import ResearchStatus
from schemas.research import (
    ResearchDetailResponse,
    ResearchHistoryItem,
    ResearchReportResponse,
    ResearchSessionResponse,
)
from utils.exceptions import ForbiddenError, NotFoundError

logger = logging.getLogger(__name__)


class ResearchService:
    def __init__(self):
        self.session_repo = SessionRepository()
        self.report_repo = ReportRepository()

    async def start_research(self, user_id: str, query: str) -> ResearchDetailResponse:
        session = await self.session_repo.create(user_id, query)
        session_id = session["_id"]

        asyncio.create_task(self._execute_pipeline(session_id, user_id, query))

        return ResearchDetailResponse(
            session=ResearchSessionResponse(
                id=session_id,
                user_id=session["user_id"],
                query=session["query"],
                status=ResearchStatus(session["status"]),
                created_at=session["created_at"],
                updated_at=session["updated_at"],
            ),
            report=None,
        )

    async def _execute_pipeline(self, session_id: str, user_id: str, query: str) -> None:
        try:
            await self.session_repo.update_status(session_id, ResearchStatus.RUNNING)
            result = await run_research_pipeline(query)
            await self.report_repo.create(
                session_id=session_id,
                user_id=user_id,
                title=result["title"],
                report=result["report"],
                sources=result["sources"],
            )
            await self.session_repo.update_status(session_id, ResearchStatus.COMPLETED)
        except Exception:
            logger.exception("Research pipeline failed for session %s", session_id)
            await self.session_repo.update_status(session_id, ResearchStatus.FAILED)

    async def get_history(
        self, user_id: str, search: str | None = None
    ) -> list[ResearchHistoryItem]:
        sessions = await self.session_repo.find_by_user(user_id)
        items: list[ResearchHistoryItem] = []

        for session in sessions:
            report = await self.report_repo.find_by_session_id(session["_id"])
            title = report["title"] if report else None

            if search:
                search_lower = search.lower()
                matches = (
                    search_lower in session["query"].lower()
                    or (title and search_lower in title.lower())
                )
                if not matches:
                    continue

            items.append(
                ResearchHistoryItem(
                    id=session["_id"],
                    query=session["query"],
                    status=ResearchStatus(session["status"]),
                    title=title,
                    created_at=session["created_at"],
                    updated_at=session["updated_at"],
                )
            )
        return items

    async def get_research(self, session_id: str, user_id: str) -> ResearchDetailResponse:
        session = await self.session_repo.find_by_id(session_id)
        if not session:
            raise NotFoundError("Research session not found")
        if session["user_id"] != user_id:
            raise ForbiddenError("Access denied")

        report_doc = await self.report_repo.find_by_session_id(session_id)
        report = None
        if report_doc:
            report = ResearchReportResponse(
                id=report_doc["_id"],
                session_id=report_doc["session_id"],
                user_id=report_doc["user_id"],
                title=report_doc["title"],
                report=report_doc["report"],
                sources=report_doc["sources"],
                created_at=report_doc["created_at"],
            )

        return ResearchDetailResponse(
            session=ResearchSessionResponse(
                id=session["_id"],
                user_id=session["user_id"],
                query=session["query"],
                status=ResearchStatus(session["status"]),
                created_at=session["created_at"],
                updated_at=session["updated_at"],
            ),
            report=report,
        )

    async def delete_research(self, session_id: str, user_id: str) -> None:
        session = await self.session_repo.find_by_id(session_id)
        if not session:
            raise NotFoundError("Research session not found")
        if session["user_id"] != user_id:
            raise ForbiddenError("Access denied")

        await self.report_repo.delete_by_session_id(session_id, user_id)
        await self.session_repo.delete(session_id, user_id)

    async def get_recent_reports(self, user_id: str, limit: int = 5) -> list[ResearchReportResponse]:
        reports = await self.report_repo.find_by_user(user_id, limit)
        return [
            ResearchReportResponse(
                id=r["_id"],
                session_id=r["session_id"],
                user_id=r["user_id"],
                title=r["title"],
                report=r["report"],
                sources=r["sources"],
                created_at=r["created_at"],
            )
            for r in reports
        ]
