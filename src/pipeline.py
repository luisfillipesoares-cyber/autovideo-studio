from .models import VideoProject
from .scene_planner import plan_scenes
from .subtitles import scenes_to_srt


def build_project(title: str, script: str, words_per_minute: int = 145) -> VideoProject:
    scenes = plan_scenes(script, words_per_minute)
    total_duration = scenes[-1].end if scenes else 0.0

    return VideoProject(
        title=title,
        script=script,
        total_duration=total_duration,
        scenes=scenes,
        subtitles_srt=scenes_to_srt(scenes),
    )
