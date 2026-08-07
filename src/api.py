from fastapi import FastAPI, HTTPException
from .models import ProjectRequest, VideoProject
from .pipeline import build_project

app = FastAPI(
    title="AutoVideo Studio",
    version="0.1.0",
    description="Open-source API for script-to-video automation.",
)


@app.get("/")
def root():
    return {
        "name": "AutoVideo Studio",
        "version": "0.1.0",
        "docs": "/docs",
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/projects", response_model=VideoProject)
def create_project(request: ProjectRequest):
    try:
        return build_project(
            title=request.title,
            script=request.script,
            words_per_minute=request.words_per_minute,
        )
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
