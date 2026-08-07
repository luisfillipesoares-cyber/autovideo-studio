from .models import Scene


def _srt_timestamp(seconds: float) -> str:
    milliseconds = int(round(seconds * 1000))
    hours, rem = divmod(milliseconds, 3_600_000)
    minutes, rem = divmod(rem, 60_000)
    secs, millis = divmod(rem, 1000)
    return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"


def scenes_to_srt(scenes: list[Scene]) -> str:
    chunks = []
    for scene in scenes:
        chunks.append(
            "\n".join(
                [
                    str(scene.index),
                    f"{_srt_timestamp(scene.start)} --> {_srt_timestamp(scene.end)}",
                    scene.text,
                ]
            )
        )
    return "\n\n".join(chunks) + ("\n" if chunks else "")
