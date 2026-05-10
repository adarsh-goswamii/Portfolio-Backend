from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.blog import Blog
from app.schemas.blog import BlogPostDetailOut, BlogPostOut

router = APIRouter(prefix="/api/blogs", tags=["blogs"])


@router.get("", response_model=list[BlogPostOut])
def list_blogs(db: Session = Depends(get_db)):
    return db.query(Blog).order_by(Blog.date.desc()).all()


@router.get("/{slug}", response_model=BlogPostDetailOut)
def get_blog(slug: str, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.slug == slug).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog post not found")
    return blog
