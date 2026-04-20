import uuid

from sqlalchemy import Boolean, Integer, String, Text
from sqlalchemy.dialects.postgresql import ARRAY, UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class About(Base):
    __tablename__ = "about"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(100))
    tagline: Mapped[str] = mapped_column(String(300))
    bio_paragraphs: Mapped[list[str]] = mapped_column(ARRAY(Text), default=list)
    is_available: Mapped[bool] = mapped_column(Boolean, default=True)
    years_exp: Mapped[int] = mapped_column(Integer, default=0)
    projects_count: Mapped[int] = mapped_column(Integer, default=0)
    oss_packages: Mapped[int] = mapped_column(Integer, default=0)
    avatar_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
