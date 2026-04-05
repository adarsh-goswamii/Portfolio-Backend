from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr


class ContactSubmissionIn(BaseModel):
    name: str
    email: EmailStr
    message: str


class ContactSubmissionOut(BaseModel):
    id: UUID
    name: str
    email: str
    message: str
    submitted_at: datetime

    model_config = {"from_attributes": True}
