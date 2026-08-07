import argparse
import json
from pathlib import Path

from .pipeline import build_project
from .renderer import render_placeholder_video


def main():
    parser = argparse.ArgumentParser(description="AutoVideo Studio CLI")
    parser.add_argument("--title", required=True)
    parser.add_argument("--script", required=True)
    parser.add_argument("--output", default="output/project")
    parser.add_argument("--wpm", type=int, default=145)
    parser.add_argument("--render", action="store_true")
    args = parser.parse_args()

    project = build_project(args.title, args.script, args.wpm)

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    (output_dir / "project.json").write_text(
        json.dumps(project.model_dump(), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    (output_dir / "subtitles.srt").write_text(
        project.subtitles_srt,
        encoding="utf-8",
    )

    if args.render:
        render_placeholder_video(project, output_dir / "video.mp4")

    print(f"Project created at: {output_dir.resolve()}")


if __name__ == "__main__":
    main()
