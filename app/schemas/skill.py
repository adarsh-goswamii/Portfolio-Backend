from uuid import UUID

from pydantic import BaseModel

from app.models.skill import SkillCategory


class SkillOut(BaseModel):
    id: UUID
    name: str
    category: SkillCategory
    sort_order: int

    model_config = {"from_attributes": True}
