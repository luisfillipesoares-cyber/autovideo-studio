# AutoVideo Studio

AutoVideo Studio is an open-source Python toolkit for automating short-form video creation from text scripts.

It provides a simple pipeline for:
- splitting a script into scenes;
- generating scene timing;
- generating SRT subtitles;
- preparing a render plan;
- rendering a basic vertical MP4 with FFmpeg;
- exposing the workflow through a FastAPI API.

The project is intentionally modular so that AI providers, text-to-speech engines, image generators and stock-media providers can be added later.

## Current features

- Script-to-scenes parser
- Automatic scene duration estimation
- SRT subtitle generation
- JSON render-plan generation
- FastAPI REST API
- Basic 1080x1920 vertical-video renderer using FFmpeg
- Docker support
- Unit tests
- GitHub Actions CI
- Optional OpenRouter/Anthropic configuration

## Quick start

### 1. Requirements

- Python 3.11+
- FFmpeg installed and available on PATH

### 2. Install

```bash
git clone https://github.com/YOUR_USERNAME/autovideo-studio.git
cd autovideo-studio

python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run the API

```bash
uvicorn src.api:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

## API example

POST `/projects`

```json
{
  "title": "My first short",
  "script": "Artificial intelligence is changing video production. Creators can automate repetitive editing tasks. Open tools make these workflows easier to build.",
  "words_per_minute": 145
}
```

The API returns a project containing scenes, timestamps and subtitles.

## CLI example

```bash
python -m src.cli \
  --title "Demo Video" \
  --script "This is the first scene. This is the second scene." \
  --output output/demo
```

This creates:

```text
output/demo/
├── project.json
└── subtitles.srt
```

To render a simple placeholder video:

```bash
python -m src.cli \
  --title "Demo Video" \
  --script "This is the first scene. This is the second scene." \
  --output output/demo \
  --render
```

## Project structure

```text
autovideo-studio/
├── src/
│   ├── api.py
│   ├── cli.py
│   ├── models.py
│   ├── pipeline.py
│   ├── scene_planner.py
│   ├── subtitles.py
│   └── renderer.py
├── tests/
├── examples/
├── docs/
├── templates/
├── .github/workflows/
├── Dockerfile
├── requirements.txt
├── pyproject.toml
├── .env.example
├── .gitignore
├── LICENSE
└── README.md
```

## Roadmap

- [x] Script parser
- [x] Scene timing
- [x] Subtitle generator
- [x] FastAPI API
- [x] Basic FFmpeg renderer
- [x] Docker
- [x] Tests and CI
- [ ] OpenRouter scene planning
- [ ] Claude scene planning
- [ ] Text-to-speech providers
- [ ] AI image generation
- [ ] Stock video providers
- [ ] Audio normalization
- [ ] Background music support
- [ ] Template system
- [ ] Web interface
- [ ] MCP server

## Security

Never commit API keys.

Copy `.env.example` to `.env` and store credentials only in `.env`.

## Contributing

Pull requests and issues are welcome.

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT
