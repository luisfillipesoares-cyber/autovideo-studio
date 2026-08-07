from src.scene_planner import split_script, plan_scenes


def test_split_script():
    parts = split_script("Hello world. Second scene! Third?")
    assert len(parts) == 3


def test_plan_scenes_are_contiguous():
    scenes = plan_scenes("First scene. Second scene.")
    assert len(scenes) == 2
    assert scenes[0].start == 0
    assert scenes[0].end == scenes[1].start
    assert scenes[-1].end > 0
