from src.models import Scene
from src.subtitles import scenes_to_srt


def test_srt_generation():
    scenes = [
        Scene(index=1, text="Hello", start=0, end=2, duration=2),
    ]
    srt = scenes_to_srt(scenes)
    assert "00:00:00,000 --> 00:00:02,000" in srt
    assert "Hello" in srt
