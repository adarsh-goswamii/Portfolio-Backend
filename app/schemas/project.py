from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic import BaseModel

from app.models.project import DocumentStatus, DocumentType


class DocumentOut(BaseModel):
    id: UUID
    type: DocumentType
    title: str
    content: Any
    status: DocumentStatus
    sort_order: int
    updated_at: datetime

    model_config = {"from_attributes": True}


class ProjectCardOut(BaseModel):
    id: UUID
    slug: str
    name: str
    short_description: str
    icon_url: str | None
    github_url: str | None
    live_url: str | None
    tags: list[str]
    sort_order: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class ProjectDetailOut(ProjectCardOut):
    documents: list[DocumentOut]
