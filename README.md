# 🎬 AutoVideo Studio

<p align="center">

**An open-source Python framework for AI-powered short-form video creation.**

Transform plain text into structured vertical videos using a modular pipeline that supports scene planning, subtitles, rendering, REST APIs and future AI integrations.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-API-009688?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker)
![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

</p>

---

# 📖 Overview

AutoVideo Studio is an open-source Python framework designed to automate the creation of AI-powered short-form videos.

Instead of manually editing every clip, creators can transform plain text into structured video projects through an extensible pipeline that handles:

- Scene planning
- Subtitle generation
- Render planning
- Video rendering
- API integration

The project was built with modularity in mind, making it easy to plug in new AI providers, image generators, text-to-speech engines, stock-media providers and automation workflows.

Its architecture allows developers to use only the components they need or replace individual modules without affecting the rest of the system.

---

# ✨ Features

## Current Features

- ✅ Script-to-scene parser
- ✅ Automatic scene duration estimation
- ✅ Subtitle (.SRT) generation
- ✅ JSON render plan
- ✅ FastAPI REST API
- ✅ Command-line interface
- ✅ FFmpeg renderer
- ✅ Docker support
- ✅ GitHub Actions CI
- ✅ Unit tests
- ✅ Modular architecture

---

# 🏗 Architecture

```
            User Script
                 │
                 ▼
        Scene Planner
                 │
                 ▼
     Duration Estimator
                 │
                 ▼
      Subtitle Generator
                 │
                 ▼
       Render Plan Builder
                 │
                 ▼
       FFmpeg Renderer
                 │
                 ▼
          Vertical MP4
```

Every module is independent and can be replaced or extended.

---

# 🚀 Quick Start

## Requirements

- Python 3.11+
- FFmpeg installed
- Git

---

## Clone the repository

```bash
git clone https://github.com/luisfillipesoares-cyber/autovideo-studio.git

cd autovideo-studio
```

---

## Create a virtual environment

Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the API

```bash
uvicorn src.api:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

Interactive Swagger documentation will be available automatically.

---

# 📦 API Example

### Request

```http
POST /projects
```

```json
{
  "title": "AI Revolution",
  "script": "Artificial intelligence is transforming the way people create videos. Modern tools automate repetitive editing tasks.",
  "words_per_minute": 145
}
```

---

### Response

```json
{
  "title":"AI Revolution",
  "duration":17.2,
  "scene_count":2,
  "subtitles":"subtitles.srt",
  "render_plan":"project.json"
}
```

---

# 💻 Command Line Interface

Generate a project

```bash
python -m src.cli \
--title "Demo" \
--script "Artificial intelligence is changing content creation." \
--output output/demo
```

Output

```
output/
└── demo/
    ├── project.json
    └── subtitles.srt
```

---

Generate and render

```bash
python -m src.cli \
--title "Demo" \
--script "Artificial intelligence is changing content creation." \
--output output/demo \
--render
```

Output

```
output/
└── demo/
    ├── project.json
    ├── subtitles.srt
    └── video.mp4
```

---

# 📁 Project Structure

```
autovideo-studio/

├── src/
│   ├── api.py
│   ├── cli.py
│   ├── models.py
│   ├── pipeline.py
│   ├── renderer.py
│   ├── scene_planner.py
│   ├── subtitles.py
│   └── utils.py
│
├── tests/
│
├── docs/
│
├── examples/
│
├── templates/
│
├── .github/
│   └── workflows/
│
├── Dockerfile
├── pyproject.toml
├── requirements.txt
├── LICENSE
└── README.md
```

---

# 🔌 Extensibility

AutoVideo Studio was designed as a modular framework.

Future integrations include:

- OpenRouter
- Anthropic Claude
- OpenAI
- Google Gemini
- ElevenLabs
- Coqui TTS
- Stability AI
- Flux
- Midjourney
- Pexels
- Pixabay
- Unsplash
- AssemblyAI
- Whisper
- FFmpeg filters
- MCP Server

New providers can be added without changing the core pipeline.

---

# 🛣 Roadmap

## Core

- [x] Script parser
- [x] Scene planner
- [x] Subtitle generation
- [x] FastAPI
- [x] Docker
- [x] Unit tests

## AI

- [ ] OpenRouter integration
- [ ] Claude scene planning
- [ ] GPT scene planning
- [ ] AI image generation
- [ ] AI voice generation
- [ ] Stock video providers

## Rendering

- [ ] Background music
- [ ] Automatic transitions
- [ ] Caption animations
- [ ] Motion graphics
- [ ] Template engine

## Platform

- [ ] Web Interface
- [ ] Desktop App
- [ ] MCP Server
- [ ] Plugin System

---

# 🤝 Contributing

Contributions are welcome.

If you would like to improve AutoVideo Studio:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Submit a Pull Request.

Please read:

```
CONTRIBUTING.md
```

before opening a pull request.

---

# 🔒 Security

Never commit API keys.

Copy

```
.env.example
```

to

```
.env
```

and store all credentials locally.

Example

```
OPENROUTER_API_KEY=
ANTHROPIC_API_KEY=
OPENAI_API_KEY=
```

---

# 📜 License

This project is licensed under the MIT License.

See

```
LICENSE
```

for details.

---

# ⭐ Support the Project

If you find AutoVideo Studio useful:

- ⭐ Star this repository
- 🍴 Fork it
- 🐞 Report issues
- 💡 Suggest new features
- 🤝 Contribute with pull requests

Every contribution helps make the project better.

---

<p align="center">

**Built with ❤️ using Python, FastAPI and FFmpeg**

</p>
