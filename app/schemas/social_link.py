from uuid import UUID

from pydantic import BaseModel

from app.models.social_link import Platform


class SocialLinkOut(BaseModel):
    id: UUID
    platform: Platform
    url: str
    label: str

    model_config = {"from_attributes": True}
