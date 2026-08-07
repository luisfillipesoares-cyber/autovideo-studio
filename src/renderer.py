from pathlib import Path
import subprocess
import shutil

from .models import VideoProject


def render_placeholder_video(
    project: VideoProject,
    output_file: str | Path,
    width: int = 1080,
    height: int = 1920,
    fps: int = 30,
) -> Path:
    """
    Render a basic vertical placeholder MP4.

    This renderer intentionally has no external media dependency.
    It creates a dark background and burns the generated subtitles
    into the output video. It is a foundation for future image,
    stock-video and TTS integrations.
    """
    if shutil.which("ffmpeg") is None:
        raise RuntimeError("FFmpeg was not found on PATH.")

    output_file = Path(output_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    subtitle_file = output_file.with_suffix(".srt")
    subtitle_file.write_text(project.subtitles_srt, encoding="utf-8")

    duration = max(project.total_duration, 1.0)

    subtitle_path = str(subtitle_file.resolve()).replace("\\", "/")
    # Escape colon for FFmpeg filter parsing on Windows drive letters.
    subtitle_path = subtitle_path.replace(":", r"\:")

    vf = (
        f"subtitles='{subtitle_path}':"
        "force_style='FontName=Arial,FontSize=18,"
        "PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,"
        "BorderStyle=1,Outline=2,Alignment=2,MarginV=120'"
    )

    cmd = [
        "ffmpeg",
        "-y",
        "-f", "lavfi",
        "-i", f"color=c=0x101014:s={width}x{height}:r={fps}:d={duration}",
        "-vf", vf,
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-movflags", "+faststart",
        str(output_file),
    ]

    subprocess.run(cmd, check=True)
    return output_file
