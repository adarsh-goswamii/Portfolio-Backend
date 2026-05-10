from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class BlogPostOut(BaseModel):
    id: UUID
    slug: str
    title: str
    date: datetime
    tags: list[str]
    summary: str | None
    reading_time: int | None
    created_at: datetime
    created_by: str | None

    model_config = {"from_attributes": True}


class BlogPostDetailOut(BlogPostOut):
    content: str
