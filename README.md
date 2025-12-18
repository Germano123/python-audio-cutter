# Audio Chapter Cutter

Software em Python para **baixar músicas/sets longos** (ex: playlists do YouTube) e **recortar automaticamente faixas individuais** a partir de um arquivo `.csv` de chapters.

---

## 🎯 Objetivo

Dado:

- Um link de áudio (YouTube)
- Um arquivo `chapters.csv`

O sistema irá:

1. Ler o áudio em alta qualidade
2. Ler os timestamps do CSV
3. Recortar cada música
4. Salvar os arquivos finais separados, já nomeados

---

## 📂 Formato do arquivo chapters (.csv)

```csv
time,name
00:00,01.Snow Lights
01:59,02.Snow Parade
04:26,03.Frosty Groove
...
```

- `time`: início da música
- `name`: nome do arquivo final
- O fim da faixa é o início da próxima

---

## 🛠️ Tecnologias

- Python 3.10+

[Download Python](https://www.python.org/downloads/)

- yt-dlp (download)
- ffmpeg (cortes de áudio)

> Windows

```bash
Baixe: https://www.gyan.dev/ffmpeg/builds/
Extraia (ex: C:\ffmpeg)
Adicione C:\ffmpeg\bin ao PATH
```

> Linux (Ubuntu/Debian)

```bash
sudo apt update && sudo apt install ffmpeg
```

- Arquivos CSV padrão

---

## Como usar

1. Clone o repositório
   ```bash
   git clone
   ```
2. Rode o ambiente virtual

   ```bash
   python -m venv myvenv
   source myvenv/bin/activate  # Linux/Mac
   myvenv\Scripts\activate     # Windows
   ```

3. Instale dependências

   ```bash
   pip install -r requirements.txt
   ```

4. Prepare o arquivo `<music>.chapters.csv` com timestamps e nomes

5. Execute o script principal
   ```bash
   python src/main.py
   ```

---

## 🔄 Fluxo do sistema

1. Recebe link do YouTube ou seleciona música local
2. Converte vídeo para áudio `.mp3`, se necessário
3. Lê `chapters.csv` ou cria novo arquivo
4. Calcula duração de cada faixa
5. Executa cortes com ffmpeg
6. Exporta músicas individuais

---

## 📁 Estrutura

```
project/
├─ helpers/
│  ├─ audio_downloader.py
│  ├─ audio_cutter.py
├─ input/
│  ├─ music1.chapters.csv
├─ output/
│  ├─ 01.Snow Lights.mp3
│  ├─ 02.Snow Parade.mp3
├─ main.py
├─ requirements.txt
└─ README.md
```

---

## 🚧 Status

Projeto em fase de definição e arquitetura.

---

## ⚠️ Aviso legal

Use apenas para conteúdos com **direitos autorais permitidos** ou de sua propriedade.
