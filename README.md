# Portfolio Backend

FastAPI backend for [adarsh.dev](https://adarsh.dev). Exposes read-only REST endpoints consumed by the frontend. All writes go through the Portfolio MCP server.

## Stack

- **Python 3.12**, FastAPI, SQLAlchemy 2.0, Alembic
- **Database:** PostgreSQL 16
- **Storage:** S3 (resume PDFs)
- **Linting:** ruff | **Testing:** pytest + httpx

## Local Development

**Prerequisites:** Docker, pyenv

```bash
pyenv local 3.12.7
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt

docker compose up -d          # start postgres on port 5433
alembic upgrade head          # apply migrations
uvicorn app.main:app --reload # dev server → http://localhost:8000
```

## API Endpoints

| Method | Path | Description |
|---|---|---|
| GET | `/health` | Health check |
| GET | `/api/experience` | Ordered experience entries |
| GET | `/api/skills` | Skills ordered by category |
| GET | `/api/social-links` | Social links |
| GET | `/api/projects` | Project cards (no documents) |
| GET | `/api/projects/:slug` | Single project with all documents |
| GET | `/api/resume/active` | S3 URL of active resume |
| POST | `/api/contact` | Submit contact form |

## Database Migrations

```bash
alembic revision --autogenerate -m "description"  # generate
alembic upgrade head                               # apply
alembic downgrade -1                               # rollback one
```

## Linting & Tests

```bash
ruff check .
pytest
```

## Docker

```bash
docker build -t portfolio-backend .
docker run -p 8000:8000 \
  -e DATABASE_URL=postgresql://user:pass@host:5432/portfolio \
  -e S3_BUCKET=your-bucket \
  -e AWS_REGION=ap-south-1 \
  portfolio-backend
```

The image runs `alembic upgrade head` before starting uvicorn.

## CI/CD

Push to `master` triggers the GitHub Actions pipeline:

1. **Lint** — ruff
2. **Test** — spins up postgres:16, runs migrations + pytest
3. **Build & Deploy** — builds image, pushes to ECR, pulls and restarts on EC2

See `.github/workflows/deploy.yml` for required repository secrets.
