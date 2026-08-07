from src.pipeline import build_project


def test_build_project():
    project = build_project("Test", "One scene. Another scene.")
    assert project.title == "Test"
    assert len(project.scenes) == 2
    assert project.total_duration > 0
    assert "One scene." in project.subtitles_srt
