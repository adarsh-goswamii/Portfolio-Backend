from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.contact import ContactSubmission
from app.schemas.contact import ContactSubmissionIn, ContactSubmissionOut

router = APIRouter(prefix="/api/contact", tags=["contact"])


@router.post("", response_model=ContactSubmissionOut, status_code=201)
def submit_contact(payload: ContactSubmissionIn, db: Session = Depends(get_db)):
    submission = ContactSubmission(**payload.model_dump())
    db.add(submission)
    db.commit()
    db.refresh(submission)
    return submission
