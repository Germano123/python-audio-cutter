from yt_dlp import YoutubeDL
from pathlib import Path
import subprocess


def download_from_youtube(url: str, output_mp3: Path):
    temp_template = output_mp3.with_suffix(".%(ext)s")

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": str(temp_template),
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        temp_file = Path(ydl.prepare_filename(info))

    subprocess.run([
        "ffmpeg", "-y",
        "-i", str(temp_file),
        "-vn",
        "-acodec", "libmp3lame",
        "-ab", "192k",
        str(output_mp3)
    ], check=True)

    temp_file.unlink(missing_ok=True)
