# 🎬 AutoVideo Studio

<p align="center">
  <strong>An open-source Python framework for AI-powered short-form video creation.</strong>
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-API-009688?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker)
![MIT License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

</p>

---

## 📖 Overview

AutoVideo Studio is an open-source toolkit built in Python to automate the creation of short-form videos from text scripts.

The project provides a modular pipeline capable of transforming plain text into structured video projects through scene planning, subtitle generation, rendering preparation and API integration.

It was designed to be easily extended with AI providers, text-to-speech engines, image generation services and video automation workflows.

---

# ✨ Features

Current features include:

- ✅ Script parsing
- ✅ Automatic scene planning
- ✅ Scene duration estimation
- ✅ Subtitle (SRT) generation
- ✅ JSON render plan generation
- ✅ FastAPI REST API
- ✅ Basic FFmpeg renderer
- ✅ Docker support
- ✅ GitHub Actions CI
- ✅ Unit tests
- ✅ Modular architecture

---

# 🚀 Roadmap

### Core

- ✅ Script Parser
- ✅ Scene Planner
- ✅ Subtitle Generator
- ✅ FastAPI API
- ✅ Docker Support
- ✅ FFmpeg Renderer

### AI Integrations

- 🚧 OpenRouter
- 🚧 Claude
- 🚧 OpenAI
- ⏳ Gemini
- ⏳ Ollama

### Media

- ⏳ Text-to-Speech
- ⏳ AI Image Generation
- ⏳ Stock Video Providers
- ⏳ Background Music
- ⏳ Audio Normalization

### Platform

- ⏳ Web Interface
- ⏳ MCP Server
- ⏳ Plugin System
- ⏳ Template Marketplace

---

# 🏗 Architecture

```
             TEXT SCRIPT
                  │
                  ▼
         Script Parser
                  │
                  ▼
         Scene Planner
                  │
                  ▼
      Subtitle Generator
                  │
                  ▼
        Render Planner
                  │
                  ▼
       FFmpeg Renderer
                  │
                  ▼
        Vertical MP4 Video
```

The architecture is intentionally modular, allowing each component to be replaced independently.

---

# 📂 Project Structure

```
autovideo-studio/

├── .github/
│   └── workflows/
│       └── python.yml
│
├── docs/
│
├── examples/
│
├── src/
│   ├── api.py
│   ├── cli.py
│   ├── models.py
│   ├── pipeline.py
│   ├── renderer.py
│   ├── scene_planner.py
│   └── subtitles.py
│
├── templates/
│
├── tests/
│
├── Dockerfile
├── pyproject.toml
├── requirements.txt
├── README.md
└── LICENSE
```

---

# ⚙ Installation

## Requirements

- Python 3.11+
- FFmpeg

Install FFmpeg:

https://ffmpeg.org/download.html

---

Clone the repository

```bash
git clone https://github.com/luisfillipesoares-cyber/autovideo-studio.git

cd autovideo-studio
```

Create a virtual environment

Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

Linux / macOS

```bash
python -m venv .venv

source .venv/bin/activate
```

Install dependencies

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

---

# 🖥 CLI Example

```bash
python -m src.cli \
    --title "Demo Video" \
    --script "Artificial intelligence is transforming video creation." \
    --output output/demo
```

To render:

```bash
python -m src.cli \
    --title "Demo Video" \
    --script "Artificial intelligence is transforming video creation." \
    --output output/demo \
    --render
```

---

# 📦 API Example

POST

```
/projects
```

Example request

```json
{
  "title": "My first short",
  "script": "Artificial intelligence is changing video production.",
  "words_per_minute": 145
}
```

Response

```json
{
  "title":"My first short",
  "scenes":[...],
  "subtitles":[...]
}
```

---

# 🔌 Future AI Providers

The project is designed to support:

- Claude
- OpenRouter
- OpenAI
- Gemini
- Ollama
- Local LLMs

without requiring architectural changes.

---

# 🧪 Testing

Run all tests

```bash
pytest
```

---

# 🐳 Docker

Build

```bash
docker build -t autovideo-studio .
```

Run

```bash
docker run autovideo-studio
```

---

# 🤝 Contributing

Contributions are welcome.

If you would like to improve AutoVideo Studio:

- Fork the repository
- Create a feature branch
- Submit a Pull Request

Please read:

```
CONTRIBUTING.md
```

before contributing.

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

and store credentials there.

---

# 📄 License

Distributed under the MIT License.

See

```
LICENSE
```

for details.

---

# 🌟 Vision

AutoVideo Studio aims to become a complete open-source framework for AI-powered short-form video automation.

Future versions will support multiple AI providers, advanced rendering pipelines, speech synthesis, image generation and extensible automation workflows.

---

<p align="center">

Made with ❤️ by the AutoVideo Studio community.

</p>
