from pathlib import Path
from helpers.audio_cutter import audio_cut


def main():
    input_dir = Path("inputs")

    musicas = [f.stem for f in input_dir.iterdir() if f.suffix in [".mp3", ".mp4"]]

    if not musicas:
        print("Nenhuma música encontrada em inputs/")
        return

    print("Músicas disponíveis:")
    for i, nome in enumerate(musicas, 1):
        print(f"{i}. {nome}")

    escolha = int(input("Selecione a música: ")) - 1
    music_name = musicas[escolha]

    audio_cut(music_name)
    print("Processo finalizado.")


if __name__ == "__main__":
    main()
