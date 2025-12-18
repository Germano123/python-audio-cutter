from yt_dlp import YoutubeDL

def baixar_audio_mp3(url: str, output: str = "%(title)s.%(ext)s") -> None:
    opcoes = {
        "format": "bestaudio/best",
        "outtmpl": output,
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
    }

    with YoutubeDL(opcoes) as ydl:
        ydl.download([url])
