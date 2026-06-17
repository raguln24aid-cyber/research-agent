from fastapi import APIRouter, Depends, HTTPException, Query

from api.deps import get_current_user
from schemas.auth import UserResponse
from schemas.research import (
    ResearchDetailResponse,
    ResearchHistoryItem,
    ResearchReportResponse,
    ResearchStartRequest,
)
from services.research_service import ResearchService
from utils.exceptions import AppException

router = APIRouter(prefix="/research", tags=["research"])


@router.post("/start", response_model=ResearchDetailResponse)
async def start_research(
    data: ResearchStartRequest,
    current_user: UserResponse = Depends(get_current_user),
):
    try:
        return await ResearchService().start_research(current_user.id, data.query)
    except AppException as exc:
        raise HTTPException(status_code=exc.status_code, detail=exc.message)


@router.get("/history", response_model=list[ResearchHistoryItem])
async def get_history(
    search: str | None = Query(None),
    current_user: UserResponse = Depends(get_current_user),
):
    return await ResearchService().get_history(current_user.id, search)


@router.get("/recent", response_model=list[ResearchReportResponse])
async def get_recent_reports(
    current_user: UserResponse = Depends(get_current_user),
):
    return await ResearchService().get_recent_reports(current_user.id)


@router.get("/{session_id}", response_model=ResearchDetailResponse)
async def get_research(
    session_id: str,
    current_user: UserResponse = Depends(get_current_user),
):
    try:
        return await ResearchService().get_research(session_id, current_user.id)
    except AppException as exc:
        raise HTTPException(status_code=exc.status_code, detail=exc.message)


@router.delete("/{session_id}")
async def delete_research(
    session_id: str,
    current_user: UserResponse = Depends(get_current_user),
):
    try:
        await ResearchService().delete_research(session_id, current_user.id)
        return {"message": "Research deleted successfully"}
    except AppException as exc:
        raise HTTPException(status_code=exc.status_code, detail=exc.message)
