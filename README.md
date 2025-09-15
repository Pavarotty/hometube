<div align="center">

<br/>

# 🎬 HomeTube

<br/>

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.49+-red.svg)](https://streamlit.io)
[![Latest Release](https://img.shields.io/github/v/release/EgalitarianMonkey/hometube)](https://github.com/EgalitarianMonkey/hometube/releases)
[![Docker Image](https://ghcr-badge.egpl.dev/egalitarianmonkey/hometube/latest_tag?trim=major&label=Docker)](https://github.com/EgalitarianMonkey/hometube/pkgs/container/hometube)
[![License](https://img.shields.io/badge/License-AGPL--3.0-green.svg)](LICENSE)

<br/>

**🌐 Universal Video Downloader for Your HomeLab**

*Download, process and organize videos at Home*

<br/>

</div>

---

## 🎯 What is HomeTube?

HomeTube manages any video URL into perfectly organized content for your media library. Whether you're managing your self-hosted media servers or just downloading videos locally on your computer, HomeTube bridges the gap between online video platforms and your local self-hosted videos with a simple web application.

### 🏠 **HomeLab Integration**
- **🎬 Media server Ready**: Downloads videos directly in your Plex, Jellyfin library structure, automatically detected and ready to watch
- **🎞️ Emby Support**: Seamless integration with your existing setup
- **📱 Network Access**: Web interface accessible from any device on your network

### ⚡ **Smart Features**
- **🎯 One-Click Downloads**: Paste URL → Get perfectly organized video
- **🚫 Ad-Free Content**: SponsorBlock removes ads/sponsors (YouTube)
- **🎬 Advanced Processing**: Cut clips, embed subtitles, convert formats
- **🔐 Private Content**: Cookie support for member-only videos
- **📊 Quality Control**: Auto-select best quality or manual override

### 🌐 **Universal Platform Support**
**1800+ Video Sources** including:
- **🔥 Popular**: YouTube, Vimeo, Dailymotion, TikTok, Twitch
- **🎵 Audio**: SoundCloud, Bandcamp, Mixcloud  
- **📺 TV**: Arte, France TV, BBC iPlayer, ZDF
- **🎮 Gaming**: Twitch VODs, Kick streams
- **📱 Social**: Facebook, Instagram, Reddit videos
- **🔗 Many more**: [See complete list](docs/supported-platforms.md)

![Application Demo](./docs/images/simple_ui_demo.gif)

## ⚡ Technical Highlights

<div align="center">

| 🎯 **Easy to Use** | 🔧 **Powerful** | 🏠 **HomeLab Ready** |
|:---:|:---:|:---:|
| Web interface | 1800+ platforms | Docker deployment |
| One-click downloads | Advanced processing | Network accessible |
| Auto-organization | Cookie authentication | Plex/Jellyfin ready |

</div>

---

## 🚀 Quick Start

### ⚙️ Essential Configuration

**📋 HomeTube uses a `.env` file for all configuration**. This file controls download paths, authentication, subtitles, and more.

```bash
# 1. Clone repository (if not already done)
git clone https://github.com/EgalitarianMonkey/hometube.git
cd hometube

# 2. Create your configuration file
cp .env.sample .env

# 3. Edit .env to customize your setup
# - Set VIDEOS_FOLDER for download location
# - Configure YOUTUBE_COOKIES_FILE_PATH for authentication
# - Customize SUBTITLES_CHOICES for your languages
```

💡 **The `.env` file will be automatically created from `.env.sample` on first run if missing!**

### 🐳 Docker (Recommended)

```bash
# Simple deployment
docker run -p 8501:8501 \
  -e TZ=Europe/Paris \
  -v ./downloads:/data/Videos \
  -v ./cookies:/config \
  ghcr.io/egalitarianmonkey/hometube:latest

# Access at http://localhost:8501
```

### 🐳 Docker Compose

```yaml
# docker-compose.yml
version: '3.8'
services:
  hometube:
    image: ghcr.io/egalitarianmonkey/hometube:latest
    ports:
      - "8501:8501"
    environment:
      - TZ=Europe/Paris      # Configure timezone
      - PORT=8501            # Web interface port
    volumes:
      - ./downloads:/data/Videos    # Downloads folder
      - ./cookies:/config           # Cookies folder
    restart: unless-stopped
```

```bash
# Deploy
docker-compose up -d

# Access at http://localhost:8501
```


## ⚙️ Configuration Guide

### 🔧 Environment Variables

HomeTube configuration is managed through the `.env` file:

| Setting | Purpose | Example |
|---------|---------|---------|
| `VIDEOS_FOLDER` | Where videos are downloaded | `./downloads` |
| `YOUTUBE_COOKIES_FILE_PATH` | Authentication for private videos | `./cookies/youtube_cookies.txt` |
| `COOKIES_FROM_BROWSER` | Alternative browser auth | `chrome,firefox,brave` |
| `SUBTITLES_CHOICES` | Default subtitle languages | `en,fr,es` |
| `PORT` | Web interface port | `8501` |
| `TZ` | Timezone for Docker | `Europe/Paris` |

### 🍪 Authentication Setup (Highly Recommended)

For age-restricted, private, or member-only videos, choose one option:

**Option 1: Cookies File**
1. Install browser extension "Get cookies.txt LOCALLY"
2. Export cookies for youtube.com
3. Save to `./cookies/youtube_cookies.txt`
4. Configure in `.env`:
```env
YOUTUBE_COOKIES_FILE_PATH=./cookies/youtube_cookies.txt
```

**Option 2: Browser Cookies (Easiest)**
```env
# Add to your .env file:
COOKIES_FROM_BROWSER=chrome
```

### 🔄 Configuration Validation

Check your setup with this command:

```bash
DEBUG=1 python -c "import app.main" 2>/dev/null
```

Expected output:
```
🔧 HomeTube Configuration Summary:
📁 Videos folder: downloads
📁 Temp folder: tmp
✅ Videos folder is ready: downloads
🍪 Cookies file: ./cookies/youtube_cookies.txt
🔤 Subtitle languages: en, fr
✅ Configuration file: .env
```

---

## 📚 Documentation

**📋 Complete Documentation Hub: [docs/README.md](docs/README.md)**

### Core Guides
- **[Installation Guide](docs/installation.md)** - System setup and requirements
- **[Usage Guide](docs/usage.md)** - Complete feature walkthrough
- **[Docker Guide](docs/docker.md)** - Container deployment strategies

### Development & Operations
- **[Development Setup](docs/development-setup.md)** - Multi-environment development guide
- **[UV Workflow Guide](docs/uv-workflow.md)** - Modern dependency management
- **[Testing Documentation](docs/testing.md)** - Test framework and guidelines
- **[Deployment Guide](docs/deployment.md)** - Production deployment strategies

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Backend** | Python 3.10+, yt-dlp, FFmpeg | Core processing |
| **Frontend** | Streamlit | Web interface |
| **Container** | 🐳 jauderho/yt-dlp (Alpine + yt-dlp + FFmpeg) | Optimized deployment |
| **CI/CD** | GitHub Actions | Automation |
| **Testing** | pytest, coverage | Quality assurance |
| **Dependencies** | UV, conda, pip | Package management |

## 📊 System Requirements

| Requirement | Minimum | Recommended |
|-------------|---------|-------------|
| **Python** | 3.10+ | 3.11+ |
| **FFmpeg** | Latest | Latest |
| **Storage** | 2GB free | 10GB+ |
| **Memory** | 512MB | 2GB |
| **Network** | Broadband | High-speed |

## 📈 Project Status

- ✅ **Stable**: Core functionality tested and reliable
- 🔄 **Active Development**: Regular updates and improvements
- 🧪 **Test Coverage**: 84% on testable modules ([details](docs/testing.md))
- 📦 **Production Ready**: Docker images available on GHCR
- 🏠 **HomeLab Optimized**: Designed for self-hosted environments

---

## 🤝 Contributing & Development

**For developers and contributors**, comprehensive guides are available:

📖 **[Development Setup Guide](docs/development-setup.md)** - Environment setup  
🔄 **[Contributing Guidelines](docs/development.md)** - Workflow and best practices

**Quick Setup Options:**
- **Conda** (recommended for contributors)
- **UV** (fastest for developers) 
- **pip/venv** (universal)

**Includes:** Testing commands, workflows, code standards, and pull request process.

---

## ☕ Support This Project

If you find HomeTube useful, consider supporting the project to help with development costs.

<div align="center">
<a href="https://buymeacoffee.com/egalitarianmonkey" target="_blank">
  <img src="https://cdn.buymeacoffee.com/buttons/v2/default-orange.png" 
       alt="Buy Me A Coffee" 
       height="35" />
</a>
</div>

<div align="center">

Every contribution is appreciated! 🙏
</div>

## 📄 License

This project is licensed under the AGPL-3.0 License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **[yt-dlp](https://github.com/yt-dlp/yt-dlp)** - Universal video downloader supporting 1800+ platforms
- **[Streamlit](https://streamlit.io/)** - Excellent web app framework  
- **[SponsorBlock](https://sponsor.ajay.app/)** - Community-driven sponsor detection (YouTube)
- **[FFmpeg](https://ffmpeg.org/)** - Multimedia processing framework

---

<div align="center">

**⭐ If you find this project useful, please consider starring it!**

[⭐ Star on GitHub](https://github.com/EgalitarianMonkey/hometube) • [📖 Documentation](docs/README.md) • [🐳 Docker Hub](https://github.com/EgalitarianMonkey/hometube/pkgs/container/hometube) • [☕ Buy Me a Coffee](https://buymeacoffee.com/egalitarianmonkey)

</div>