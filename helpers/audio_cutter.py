import csv
import subprocess
from pathlib import Path

from helpers.audio_converter import convert_mp4_to_mp3


def time_to_seconds(t: str) -> int:
    partes = list(map(int, t.split(":")))
    if len(partes) == 2:
        m, s = partes
        return m * 60 + s
    h, m, s = partes
    return h * 3600 + m * 60 + s


def audio_cut(music_name: str):
    input_dir = Path("inputs")
    output_dir = Path("output") / music_name
    output_dir.mkdir(parents=True, exist_ok=True)

    audio_mp4 = input_dir / f"{music_name}.mp4"
    audio_mp3 = input_dir / f"{music_name}.mp3"
    chapters_file = input_dir / f"{music_name}.chapters.csv"

    # verificar se o arquivo de áudio existe
    if not audio_mp3.exists():
        if not audio_mp4.exists():
            raise FileNotFoundError("Arquivo não encontrado.")
        convert_mp4_to_mp3(audio_mp4, audio_mp3)

    # verificar arquivo de cortes
    if not chapters_file.exists():
        raise FileNotFoundError("Arquivo de cortes não encontrado.")

    # ler cortes
    chapters = []
    with open(chapters_file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            chapters.append({
                "start": time_to_seconds(row["time"]),
                "name": row["name"]
            })

    print(f"Cortando áudios...")
    for i, chapter in enumerate(chapters):
        start = chapter["start"]
        end = chapters[i + 1]["start"] if i + 1 < len(chapters) else None

        output_file = output_dir / f"{chapter['name']}.mp3"

        cmd = [
            "ffmpeg",
            "-y",
            "-i", str(audio_mp3),
            "-ss", str(start),
        ]

        if end:
            cmd += ["-to", str(end)]

        cmd += ["-c", "copy", str(output_file)]

        subprocess.run(cmd, check=True)
