<div align="center">

<br/>

# 🎬 HomeTube Hooked 🎣

<br/>

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.49+-red.svg)](https://streamlit.io)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://docker.com)
[![License](https://img.shields.io/badge/License-AGPL--3.0-green.svg)](LICENSE)

<br/>

**🌐 Universal Video Downloader with Webhook Integration**

*Enhanced fork with automation hooks and webhook support*

<br/>

</div>

<br/>
<br/>

<!-- --- -->

<!-- ## 🎯 What is HomeTube Enhanced? -->

🎬 **HomeTube Enhanced** is an advanced fork of the original HomeTube project, featuring powerful automation capabilities through **webhooks** and **lifecycle hooks**. Download, process and organize videos with seamless integration into your existing workflows and tools.

Perfect for automated video processing pipelines, media server integration, and custom workflow automation.

### 🚀 **Enhanced Features**

#### 🔗 **Webhook Integration** *(NEW)*
- **📡 HTTP API**: Trigger downloads via `POST /webhook` endpoint
- **🌐 URL Auto-fill**: Browser-compatible query parameters (`?url=...&filename=...`)
- **🔄 Real-time Updates**: Automatic UI synchronization
- **🛡️ CORS Support**: Cross-origin requests enabled

#### ⚙️ **Lifecycle Hooks** *(NEW)*
- **🎬 Download Start**: Execute custom scripts when download begins
- **✅ Success Actions**: Automated post-processing on completion  
- **❌ Failure Handling**: Custom error recovery workflows
- **🔧 Shell Integration**: Full shell command execution with variable substitution

#### 🏠 **HomeLab Integration**
- **🎬 Media Server Ready**: Direct integration with Plex, Jellyfin, Emby
- **📱 Network Access**: Web interface accessible from any device
- **🤖 Automation Ready**: Perfect for Home Assistant, n8n, Zapier workflows

### ⚡ **Core Features**
- **🎯 One-Click Downloads**: Paste URL → Get perfectly organized video
- **🚫 Ad-Free Content**: SponsorBlock integration for automatic ad removal
- **🎬 Advanced Processing**: Cut clips, embed subtitles, convert formats
- **🔐 Unlock Restricted Videos**: Cookie authentication for member-only content
- **📊 Quality Control**: Auto-select best quality or manual override
- **🎥 1800+ Video Sources**: YouTube, Reddit, Vimeo, Dailymotion, TikTok, Twitch, and more

<!-- ## ⚡ Technical Highlights

<div align="center">

| 🎯 **Easy to Use** | 🔧 **Powerful** | 🏠 **HomeLab Ready** |
|:---:|:---:|:---:|
| Web interface | 1800+ platforms | Docker deployment |
| One-click downloads | Advanced processing | Network accessible |
| Auto-organization | Cookie authentication | Plex/Jellyfin ready |

</div> -->

<!-- --- -->

<br/>
<br/>

![Application Demo](./docs/images/simple_ui_demo.gif)

<br/>
<br/>

<!-- --- -->

## � Enhanced Automation Features

### 🔗 Webhook Integration

**Remote download triggering via HTTP API**:

```bash
# Trigger download via webhook
curl -X POST http://localhost:8501/webhook \
  -H "Content-Type: application/json" \
  -d '{"url": "https://youtube.com/watch?v=example", "filename": "My Video"}'

# Browser-compatible URL auto-fill
http://localhost:8501/?url=https://youtube.com/watch?v=example&filename=My%20Video
```

**Perfect for automation tools**:
- **🏠 Home Assistant**: Trigger downloads from automations
- **🔗 n8n/Zapier**: Integrate with workflow automation
- **📱 Shortcuts/Tasker**: Mobile app integration
- **🤖 Custom Scripts**: API integration for any programming language

### ⚙️ Lifecycle Hooks

**Execute custom scripts at different download stages**:

```bash
# Environment variables for hooks
ON_DOWNLOAD_START="echo 'Started: {URL}' >> /data/logs/downloads.log"
ON_DOWNLOAD_SUCCESS="chmod 644 '{OUTPUT_PATH}' && notify-send 'Download Complete'"
ON_DOWNLOAD_FAILURE="echo 'Failed: {URL} - {STATUS}' >> /data/logs/errors.log"
```

**Available variables**:
- `{URL}` - Video URL
- `{FILENAME}` - Output filename  
- `{OUTPUT_PATH}` - Full path to downloaded file
- `{STATUS}` - Download status
- `{START_SEC}`, `{END_SEC}` - Section timestamps (if used)

**Use cases**:
- **📧 Notifications**: Email/Slack alerts on completion
- **🔧 Post-processing**: Automatic transcoding, thumbnail generation
- **📊 Logging**: Custom analytics and monitoring
- **🔄 Workflow Integration**: Trigger next steps in your pipeline

## �🛠️ HomeTube Options

### 🏠 HomeLab Integration

**Automatic integration with self-hosted setup**:

- **🐳 Docker Ready**: One-command deployment with Docker Compose
- **🎬 Media Server Integration**: Direct integration with media server thanks to well named video files automatically moved to chosen locations watched by media server such as Plex, Jellyfin, or Emby.
- **🆕 Create new folder from the UI**: Create organized new folder structures when necessary from the "🆕 Create New Folder" option at the bottom of the "Destination folder" field listing menu (e.g., `Tech/Python/Advanced`)
- **�📱 Network Access**: Web interface accessible from any device on your network
- **🔐 Secure**: No cloud dependencies, everything runs locally
- **⚙️ Configurable**: Extensive customization through environment variables

[Setup your HomeLab integration](docs/deployment.md).

### 🚫 SponsorBlock Integration

**Automatically skip sponsors, ads, and promotional content** with built-in SponsorBlock support. Just download your video and sponsors segments are automatically detected and marked.

- ✅ **Auto-detection**: Sponsors segments automatically identified
- ✅ **Manage sponsors to block**: Sponsors segments to block or mark can be managed in the UI
- ✅ **Community-driven**: Powered by SponsorBlock's crowd-sourced database
- ✅ **Zero configuration**: Works out of the box for YouTube videos

[Learn more about SponsorBlock features](docs/usage.md#-sponsorblock-integration).

### 🍪 Unlock restricted videos (Cookies)

Private content, age-restricted, or member-only videos are restricted without authentication on platforms like YouTube. We can unlock restricted content thanks to **cookies** authentication.

We can use **Browser cookies** if on a machine sharing a browser, otherwise **Cookies File** in HomeLab setup.

[More details about Cookies authentication setup](docs/usage.md#-authentication--private-content).

### ✂️ Advanced Video Processing

Transform your downloads with **powerful built-in video processing tools**:

- **🎬 Clip Extraction**: Cut specific segments from videos with precision timing
- **📝 Subtitle Embedding**: Automatically embed subtitles in multiple languages
- **🔄 Format Conversion**: Convert between video formats (MP4, MKV, WebM, etc.)
- **🎵 Audio Extraction**: Extract audio-only versions in high quality
- **📱 Mobile Optimization**: Optimize videos for mobile devices

[Explore all processing options](docs/usage.md#-video-processing).

### 🎯 Smart Download Management

**Intelligent download system** that adapts to your needs:

- **🏆 Quality Selection**: Auto-select best quality or manual override
- **📁 Auto-Organization**: Videos organized by channel/creator automatically
- **🎵 Playlist Downloads**: YouTube playlists and channels supported automatically
- **⚡ Resume Support**: Interrupted downloads automatically resume
- **💾 Storage Optimization**: Duplicate detection and space management

[Learn more about download features](docs/usage.md#-basic-video-download).

### 🌐 Universal Platform Support

**1800+ supported platforms** - way beyond just YouTube:

- **📺 Major Platforms**: YouTube, Twitch, Vimeo, Dailymotion, TikTok
- **🎭 Social Media**: Instagram, Facebook, Twitter, Reddit
- **🎓 Educational**: Coursera, Khan Academy, edX
- **🏢 Professional**: LinkedIn Learning, Udemy, Skillshare
- **📺 Streaming**: Netflix previews, Hulu trailers, Disney+ clips

[See complete platform list](docs/supported-platforms.md).


<br/>
<br/>

![Application Demo](./docs/images/options_ui_demo.gif)

<br/>
<br/>


## 🚀 Quick Start

### ⚙️ Essential Configuration

**📋 HomeTube Enhanced uses a `.env` file for all configuration**. This includes webhook settings, lifecycle hooks, download paths, and authentication.

```bash
# 1. Clone repository
git clone https://github.com/Pavarotty/hometube-personal.git
cd hometube-personal

# 2. Create your configuration file
cp .env.sample .env

# 3. Edit .env to customize your setup
# - Set VIDEOS_FOLDER for download location
# - Configure webhook and hook settings
# - Set up authentication and subtitles
```

💡 **The `.env` file will be automatically created from `.env.sample` on first run if missing!**

### 🐳 Docker (Recommended)

```bash
# Enhanced deployment with webhook support
docker run -p 8501:8501 \
  -e TZ=Europe/Paris \
  -v ./downloads:/data/Videos \
  -v ./cookies:/config \
  -v ./hooks:/app/hooks:ro \
  pavarotty/hometube:latest

# Access at http://localhost:8501
# Webhook endpoint: http://localhost:8501/webhook
```

### 🐳 Docker Compose

```yaml
# docker-compose.yml
version: '3.8'
services:
  hometube:
    image: pavarotty/hometube:latest
    ports:
      - "8501:8501"
    environment:
      - TZ=Europe/Paris      # Configure timezone
      - PORT=8501            # Web interface port
      # Webhook hooks (optional)
      - ON_DOWNLOAD_START=echo "Started: {URL}" >> /data/logs/downloads.log
      - ON_DOWNLOAD_SUCCESS=notify-send "Download Complete: {FILENAME}"
      - ON_DOWNLOAD_FAILURE=echo "Failed: {STATUS}" >> /data/logs/errors.log
    volumes:
      - ./downloads:/data/Videos    # Downloads folder
      - ./cookies:/config           # Cookies folder
      - ./hooks:/app/hooks:ro       # Custom hook scripts
      - ./logs:/data/logs           # Log files
    restart: unless-stopped
```

```bash
# Deploy
docker-compose up -d

# Access at http://localhost:8501
# Webhook endpoint: http://localhost:8501/webhook
```

### 🔗 Webhook Configuration Example

Create a `.env` file with webhook automation:

```bash
# Webhook hooks for automation
ON_DOWNLOAD_START=echo "$(date): START {URL}" >> /data/logs/download.log
ON_DOWNLOAD_SUCCESS=chmod 644 "{OUTPUT_PATH}" && echo "$(date): SUCCESS {OUTPUT_PATH}" >> /data/logs/download.log
ON_DOWNLOAD_FAILURE=echo "$(date): FAILED {URL} - {STATUS}" >> /data/logs/download.log

# Example: Plex library refresh after download
ON_DOWNLOAD_SUCCESS=curl -X POST "http://plex:32400/library/sections/1/refresh?X-Plex-Token=YOUR_TOKEN"

# Example: Home Assistant notification
ON_DOWNLOAD_SUCCESS=curl -X POST "http://homeassistant:8123/api/services/notify/mobile_app_phone" -H "Authorization: Bearer YOUR_TOKEN" -d '{"message":"Video downloaded: {FILENAME}"}'
```

### 🏠 Local Installation

**Prerequisites**: Python 3.10+, FFmpeg

**Option 1: Using pip (Recommended)**
```bash
# Create virtual environment
python -m venv hometube-env
source hometube-env/bin/activate  # On Windows: hometube-env\Scripts\activate

# Install dependencies including yt-dlp
pip install ".[local]"

# Run the application
streamlit run app/main.py
# OR
python run.py
```

**Option 2: Using conda**
```bash
# Create conda environment
conda create -n hometube python=3.10
conda activate hometube

# Install dependencies including yt-dlp
pip install ".[local]"

# Run the application
streamlit run app/main.py
```

**Option 3: Using uv (Fastest)**
```bash
# Install uv if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies including yt-dlp
uv pip install ".[local]"

# Run with uv
uv run streamlit run app/main.py
```

**Access at**: http://localhost:8501


## ⚙️ Configuration Guide

### 🔧 Environment Variables

HomeTube configuration is managed through the `.env` file:

| Variable | Purpose | Example |
|---------|---------|---------|
| `VIDEOS_FOLDER` | Where videos will be moved at the end of download | `./downloads` |
| `TMP_DOWNLOAD_FOLDER` | Temporary download location | `./tmp` |
| `YOUTUBE_COOKIES_FILE_PATH` | Authentication for private videos | `./cookies/youtube_cookies.txt` |
| `COOKIES_FROM_BROWSER` | Alternative browser auth | `chrome,firefox,brave` |
| `UI_LANGUAGE` | UI language. English (en) and French (fr) supported | `en` |
| `SUBTITLES_CHOICES` | Default subtitle languages | `en,fr,es` |
| `PORT` | Web interface port | `8501` |
| `TZ` | Timezone for Docker | `Europe/Paris` |
| `VIDEOS_FOLDER_DOCKER_HOST` | Videos folder in Docker context | `/downloads` |
| `TMP_DOWNLOAD_FOLDER_DOCKER_HOST` | Tmp download Videos folder in Docker context | `./tmp` |
| `YOUTUBE_COOKIES_FILE_PATH_DOCKER_HOST` | Youtube cookies file path in Docker context | `./cookies/youtube_cookies.txt` |



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

- ✅ **Enhanced Fork**: Based on the original HomeTube with automation improvements
- 🔄 **Active Development**: Focused on webhook integration and automation features
- 🧪 **Well Tested**: Core functionality tested and reliable
- 📦 **Production Ready**: Docker images available on Docker Hub
- 🏠 **HomeLab Optimized**: Designed for automated self-hosted environments
- 🤖 **Automation Ready**: Perfect for Home Assistant, n8n, and custom workflows

## � Original Project

This is an enhanced fork of the original [HomeTube project](https://github.com/EgalitarianMonkey/hometube) by EgalitarianMonkey.

**🆕 What's New in This Fork:**
- **🔗 Webhook API**: HTTP endpoint for remote download triggering
- **⚙️ Lifecycle Hooks**: Custom script execution at download stages
- **🌐 Browser Integration**: URL auto-fill via query parameters
- **🤖 Automation Ready**: Perfect for Home Assistant and workflow tools

**💝 Credits**: Huge thanks to [EgalitarianMonkey](https://github.com/EgalitarianMonkey) for creating the amazing foundation that made these enhancements possible.

## � Enhanced Features Roadmap

**Current enhancements:**
- ✅ Webhook endpoint implementation
- ✅ Lifecycle hooks system
- ✅ Browser query parameter support
- ✅ CORS and cross-origin request support

**Planned improvements:**
- 🔄 Advanced webhook authentication
- 🔄 Batch download via webhook
- 🔄 Real-time download progress API
- 🔄 Enhanced hook variable substitution

---

## 🤝 Contributing & Development

**For developers and contributors**, this enhanced fork welcomes contributions:

📖 **[Development Setup Guide](docs/development-setup.md)** - Environment setup  
🔄 **[Contributing Guidelines](docs/development.md)** - Workflow and best practices

**Focus areas for this fork:**
- Webhook API improvements
- Automation integrations
- Hook system enhancements
- Home Assistant/n8n connectors

---

## ☕ Support This Project

If you find HomeTube Enhanced useful, consider supporting both projects:

**Original Project Creator:**
<div align="center">
<a href="https://buymeacoffee.com/egalitarianmonkey" target="_blank">
  <img src="https://cdn.buymeacoffee.com/buttons/v2/default-orange.png" 
       alt="Buy Me A Coffee" 
       height="35" />
</a>
</div>

**This Enhanced Fork:**
<div align="center">
<a href="https://buymeacoffee.com/pavarotty" target="_blank">
  <img src="https://cdn.buymeacoffee.com/buttons/v2/default-blue.png" 
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

**⭐ Star this enhanced fork • 🍴 Fork for your own automation • 📖 [Documentation](docs/README.md) • 🐳 [Docker Hub](https://hub.docker.com/r/pavarotty/hometube)**

**⭐ Also consider starring the [original project](https://github.com/EgalitarianMonkey/hometube) that made this possible!**

---

**🎬 HomeTube Enhanced - Download, Automate, Integrate**

</div>