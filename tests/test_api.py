
from app.models.experience import Experience
from app.models.project import Document, DocumentStatus, DocumentType, Project
from app.models.skill import Skill, SkillCategory
from app.models.social_link import Platform, SocialLink


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


# --- Experience ---

def test_list_experience_empty(client):
    r = client.get("/api/experience")
    assert r.status_code == 200
    assert r.json() == []


def test_list_experience(client, db):
    db.add(Experience(
        role="Engineer", company="Acme", description="Built stuff",
        tech_tags=["Python"], start_year=2022, sort_order=1,
    ))
    db.flush()

    r = client.get("/api/experience")
    assert r.status_code == 200
    data = r.json()
    assert len(data) == 1
    assert data[0]["role"] == "Engineer"
    assert data[0]["company"] == "Acme"
    assert data[0]["tech_tags"] == ["Python"]


# --- Skills ---

def test_list_skills_empty(client):
    r = client.get("/api/skills")
    assert r.status_code == 200
    assert r.json() == []


def test_list_skills(client, db):
    db.add(Skill(name="Python", category=SkillCategory.LANGUAGES, sort_order=1))
    db.flush()

    r = client.get("/api/skills")
    assert r.status_code == 200
    data = r.json()
    assert len(data) == 1
    assert data[0]["name"] == "Python"
    assert data[0]["category"] == "languages"


# --- Social Links ---

def test_list_social_links_empty(client):
    r = client.get("/api/social-links")
    assert r.status_code == 200
    assert r.json() == []


def test_list_social_links(client, db):
    db.add(SocialLink(platform=Platform.GITHUB, url="https://github.com/test", label="GitHub"))
    db.flush()

    r = client.get("/api/social-links")
    assert r.status_code == 200
    data = r.json()
    assert len(data) == 1
    assert data[0]["platform"] == "GITHUB"


# --- Projects ---

def test_list_projects_empty(client):
    r = client.get("/api/projects")
    assert r.status_code == 200
    assert r.json() == []


def test_list_projects(client, db):
    db.add(Project(
        slug="test-project", name="Test Project",
        short_description="A test", tags=["python"], sort_order=1,
    ))
    db.flush()

    r = client.get("/api/projects")
    assert r.status_code == 200
    data = r.json()
    assert len(data) == 1
    assert data[0]["slug"] == "test-project"


def test_get_project_not_found(client):
    r = client.get("/api/projects/does-not-exist")
    assert r.status_code == 404


def test_get_project(client, db):
    project = Project(
        slug="my-project", name="My Project",
        short_description="Details here", tags=[], sort_order=1,
    )
    db.add(project)
    db.flush()
    db.add(Document(
        project_id=project.id,
        type=DocumentType.PRD,
        title="PRD",
        content=[],
        status=DocumentStatus.PUBLISHED,
        sort_order=1,
    ))
    db.flush()

    r = client.get("/api/projects/my-project")
    assert r.status_code == 200
    data = r.json()
    assert data["slug"] == "my-project"
    assert len(data["documents"]) == 1
    assert data["documents"][0]["title"] == "PRD"


# --- Contact ---

def test_submit_contact(client):
    payload = {"name": "Alice", "email": "alice@example.com", "message": "Hello!"}
    r = client.post("/api/contact", json=payload)
    assert r.status_code == 201
    data = r.json()
    assert data["name"] == "Alice"
    assert data["email"] == "alice@example.com"


def test_submit_contact_missing_fields(client):
    r = client.post("/api/contact", json={"name": "Bob"})
    assert r.status_code == 422
