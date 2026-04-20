from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.about import About
from app.schemas.about import AboutOut

router = APIRouter(prefix="/api/about", tags=["about"])


@router.get("", response_model=AboutOut)
def get_about(db: Session = Depends(get_db)):
    row = db.query(About).first()
    if not row:
        raise HTTPException(status_code=404, detail="About not found")
    return row
