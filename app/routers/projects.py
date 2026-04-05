from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload

from app.core.database import get_db
from app.models.project import Document, Project
from app.schemas.project import ProjectCardOut, ProjectDetailOut

router = APIRouter(prefix="/api/projects", tags=["projects"])


@router.get("", response_model=list[ProjectCardOut])
def list_projects(db: Session = Depends(get_db)):
    return db.query(Project).order_by(Project.sort_order).all()


@router.get("/{slug}", response_model=ProjectDetailOut)
def get_project(slug: str, db: Session = Depends(get_db)):
    project = (
        db.query(Project)
        .options(joinedload(Project.documents))
        .filter(Project.slug == slug)
        .first()
    )
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    project.documents.sort(key=lambda d: d.sort_order)
    return project
