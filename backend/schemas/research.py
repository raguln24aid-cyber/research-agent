from datetime import datetime

from pydantic import BaseModel, Field

from models.research import ResearchStatus


class ResearchStartRequest(BaseModel):
    query: str = Field(min_length=3, max_length=2000)


class ResearchSessionResponse(BaseModel):
    id: str
    user_id: str
    query: str
    status: ResearchStatus
    created_at: datetime
    updated_at: datetime


class ResearchReportResponse(BaseModel):
    id: str
    session_id: str
    user_id: str
    title: str
    report: str
    sources: list[dict]
    created_at: datetime


class ResearchDetailResponse(BaseModel):
    session: ResearchSessionResponse
    report: ResearchReportResponse | None = None


class ResearchHistoryItem(BaseModel):
    id: str
    query: str
    status: ResearchStatus
    title: str | None = None
    created_at: datetime
    updated_at: datetime
