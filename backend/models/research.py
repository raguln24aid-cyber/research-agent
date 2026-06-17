from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class ResearchStatus(str, Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class UserModel(BaseModel):
    id: str = Field(alias="_id")
    name: str
    email: str
    hashed_password: str
    created_at: datetime

    model_config = {"populate_by_name": True}


class ResearchSessionModel(BaseModel):
    id: str = Field(alias="_id")
    user_id: str
    query: str
    status: ResearchStatus
    created_at: datetime
    updated_at: datetime

    model_config = {"populate_by_name": True}


class ResearchReportModel(BaseModel):
    id: str = Field(alias="_id")
    session_id: str
    user_id: str
    title: str
    report: str
    sources: list[dict]
    created_at: datetime

    model_config = {"populate_by_name": True}
