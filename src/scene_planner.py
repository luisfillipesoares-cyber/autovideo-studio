import re
from .models import Scene


_SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+")


def split_script(script: str) -> list[str]:
    cleaned = " ".join(script.strip().split())
    if not cleaned:
        return []

    parts = [p.strip() for p in _SENTENCE_SPLIT.split(cleaned) if p.strip()]
    return parts or [cleaned]


def estimate_duration(text: str, words_per_minute: int = 145) -> float:
    words = max(1, len(text.split()))
    seconds = words / words_per_minute * 60
    return max(1.8, round(seconds, 2))


def plan_scenes(script: str, words_per_minute: int = 145) -> list[Scene]:
    scenes: list[Scene] = []
    cursor = 0.0

    for index, text in enumerate(split_script(script), start=1):
        duration = estimate_duration(text, words_per_minute)
        start = round(cursor, 2)
        end = round(start + duration, 2)
        scenes.append(
            Scene(
                index=index,
                text=text,
                start=start,
                end=end,
                duration=duration,
            )
        )
        cursor = end

    return scenes
