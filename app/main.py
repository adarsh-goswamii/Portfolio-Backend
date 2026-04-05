from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import contact, experience, projects, resume, skills, social_links

app = FastAPI(title="Portfolio API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app.include_router(experience.router)
app.include_router(skills.router)
app.include_router(social_links.router)
app.include_router(projects.router)
app.include_router(resume.router)
app.include_router(contact.router)


@app.get("/health")
def health():
    return {"status": "ok"}
