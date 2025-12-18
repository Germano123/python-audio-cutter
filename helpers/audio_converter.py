import subprocess
from pathlib import Path

def convert_mp4_to_mp3(input_file: Path, output_file: Path):
    output_file.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        "ffmpeg",
        "-y",
        "-i", str(input_file),
        "-vn",
        "-acodec", "libmp3lame",
        "-ab", "192k",
        str(output_file),
    ]

    subprocess.run(cmd, check=True)
