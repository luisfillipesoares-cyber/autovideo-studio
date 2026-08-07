from pydantic import BaseModel, Field


class ProjectRequest(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    script: str = Field(min_length=1)
    words_per_minute: int = Field(default=145, ge=80, le=220)


class Scene(BaseModel):
    index: int
    text: str
    start: float
    end: float
    duration: float


class VideoProject(BaseModel):
    title: str
    script: str
    total_duration: float
    scenes: list[Scene]
    subtitles_srt: str
