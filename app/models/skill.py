import enum
import uuid

from sqlalchemy import Enum, Integer, String, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class SkillCategory(str, enum.Enum):
    LANGUAGES = "languages"
    FRAMEWORKS = "frameworks"
    DATABASES = "databases"
    CLOUD = "cloud"
    TOOLS = "tools"
    OTHER = "other"


class Skill(Base):
    __tablename__ = "skills"
    __table_args__ = (UniqueConstraint("name", "category", name="uq_skill_name_category"),)

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(100))
    category: Mapped[SkillCategory] = mapped_column(Enum(SkillCategory, name="skill_category", native_enum=True))
    sort_order: Mapped[int] = mapped_column(Integer, default=0)
