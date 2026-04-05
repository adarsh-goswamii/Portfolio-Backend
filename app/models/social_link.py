import enum
import uuid

from sqlalchemy import Enum, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Platform(str, enum.Enum):
    GITHUB = "github"
    LINKEDIN = "linkedin"
    TWITTER = "twitter"
    EMAIL = "email"
    WEBSITE = "website"
    YOUTUBE = "youtube"
    OTHER = "other"


class SocialLink(Base):
    __tablename__ = "social_links"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    platform: Mapped[Platform] = mapped_column(Enum(Platform, name="platform", native_enum=True), unique=True)
    url: Mapped[str] = mapped_column(String(500))
    label: Mapped[str] = mapped_column(String(100))
