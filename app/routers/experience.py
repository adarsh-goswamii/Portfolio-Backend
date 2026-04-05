from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.experience import Experience
from app.schemas.experience import ExperienceOut

router = APIRouter(prefix="/api/experience", tags=["experience"])


@router.get("", response_model=list[ExperienceOut])
def list_experience(db: Session = Depends(get_db)):
    return db.query(Experience).order_by(Experience.sort_order).all()
