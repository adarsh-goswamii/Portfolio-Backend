from uuid import UUID

from pydantic import BaseModel


class ExperienceOut(BaseModel):
    id: UUID
    role: str
    company: str
    description: str
    tech_tags: list[str]
    start_year: int
    end_year: int | None
    sort_order: int

    model_config = {"from_attributes": True}
