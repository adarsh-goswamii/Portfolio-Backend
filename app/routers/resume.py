from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.resume import ResumeVersion
from app.schemas.resume import ResumeActiveOut

router = APIRouter(prefix="/api/resume", tags=["resume"])


@router.get("/active", response_model=ResumeActiveOut)
def get_active_resume(db: Session = Depends(get_db)):
    version = db.query(ResumeVersion).filter(ResumeVersion.is_active.is_(True)).first()
    if not version:
        raise HTTPException(status_code=404, detail="No active resume version")
    return ResumeActiveOut(s3_url=version.s3_key, version_label=version.version_label)
