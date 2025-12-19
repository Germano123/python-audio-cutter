from pathlib import Path
from helpers.audio_cutter import audio_cut
from helpers.audio_downloader import download_from_youtube


def download_music(input_dir: Path) -> str:
    url = input("URL do YouTube: ").strip()
    nome = input("Nome do arquivo (sem extensão): ").strip()

    output = Path(input_dir / f"{nome}.mp3")
    download_from_youtube(url, output)
    return nome


def select_music(input_dir: Path) -> str:
    musicas = [f.stem for f in input_dir.iterdir() if f.suffix in [".mp3", ".mp4"]]

    if not musicas:
        raise RuntimeError("Nenhuma música encontrada em inputs/")

    for i, nome in enumerate(musicas, 1):
        print(f"{i}. {nome}")

    escolha = int(input("Selecione a música: ")) - 1
    return musicas[escolha]


def main():
    input_dir = Path("inputs")
    input_dir.mkdir(exist_ok=True)

    print("1. Usar música existente")
    print("2. Baixar nova música")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "2":
        music_name = download_music(input_dir)
    else:
        music_name = select_music(input_dir)

    audio_cut(music_name)
    print("Processo finalizado.")


if __name__ == "__main__":
    main()
