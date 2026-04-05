from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.social_link import SocialLink
from app.schemas.social_link import SocialLinkOut

router = APIRouter(prefix="/api/social-links", tags=["social-links"])


@router.get("", response_model=list[SocialLinkOut])
def list_social_links(db: Session = Depends(get_db)):
    return db.query(SocialLink).all()
