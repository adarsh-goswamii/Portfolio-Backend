from uuid import UUID

from pydantic import BaseModel


class AboutOut(BaseModel):
    id: UUID
    name: str
    tagline: str
    bio_paragraphs: list[str]
    is_available: bool
    years_exp: int
    projects_count: int
    oss_packages: int
    avatar_url: str | None

    model_config = {"from_attributes": True}
