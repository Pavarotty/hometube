<div align="center">

<br/>

# � HomeTube Hooked

<br/>

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.49+-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-AGPL--3.0-green.svg)](LICENSE)

<br/>

**🌐 Enhanced HomeTube Fork with Hooks & Webhooks**

*Fork of [EgalitarianMonkey/hometube](https://github.com/EgalitarianMonkey/hometube) with automation capabilities*

<br/>

</div>

<br/>
<br/>

## 🎯 What's New in HomeTube Hooked?

This fork extends the original [HomeTube](https://github.com/EgalitarianMonkey/hometube) with powerful automation features:

### 🎣 **Hook System**
Execute custom scripts at different download stages:
- **📋 ON_DOWNLOAD_START**: Triggered when download begins
- **✅ ON_DOWNLOAD_SUCCESS**: Triggered when download completes successfully  
- **❌ ON_DOWNLOAD_FAILURE**: Triggered when download fails

**Example use cases:**
- Send notifications to Discord/Slack/Telegram
- Update media server libraries automatically
- Log download analytics
- Trigger post-processing workflows

### 🔗 **Webhook Integration** 
Receive HTTP requests to auto-populate download fields:
- **POST endpoint**: `/webhook` accepts JSON payloads
- **GET parameters**: `?url=...&filename=...` for browser integration
- **Browser bookmarklets**: One-click download from any video page
- **External integration**: Connect with automation tools, browser extensions, mobile apps

### 🏠 **Original HomeTube Features**
- **🎯 One-Click Downloads**: Paste URL → Get perfectly organized video
- **🚫 Ad-Free Content**: Block videos' sponsors and ads  
- **🎬 Advanced Processing**: Cut clips, embed subtitles, convert formats
- **🔐 Cookie Authentication**: Access restricted/member-only videos
- **🎥 1800+ Video Sources**: YouTube, Reddit, Vimeo, TikTok, Twitch, etc.

For complete feature documentation, see the [original repository](https://github.com/EgalitarianMonkey/hometube).

<br/>

## 🎣 Hook System Configuration

Configure custom scripts in your `.env` file:

```bash
# Execute shell commands on download events
ON_DOWNLOAD_START=echo "Download started: {URL}" >> /data/logs/downloads.log
ON_DOWNLOAD_SUCCESS=curl -X POST https://your-webhook.com/notify -d '{"status":"success","file":"{OUTPUT_PATH}"}'
ON_DOWNLOAD_FAILURE=echo "Download failed: {STATUS} for {URL}" >> /data/logs/errors.log
```

**Available placeholders:**
- `{URL}` - Video URL
- `{FILENAME}` - Target filename
- `{OUTPUT_PATH}` - Full path to downloaded file
- `{STATUS}` - Download status/error message
- `{START_SEC}` / `{END_SEC}` - Section timestamps (if cutting)

<br/>

## 🔗 Webhook Usage

### Browser Integration
Create bookmarklets for one-click downloads:
```javascript
javascript:window.open('http://your-hometube:8501/?url='+encodeURIComponent(window.location.href));
```

### POST Endpoint
Send JSON data to auto-populate fields:
```bash
curl -X POST http://your-hometube:8501/webhook \
  -H "Content-Type: application/json" \
  -d '{"url": "https://youtube.com/watch?v=...", "filename": "My Video"}'
```

### GET Parameters  
Direct browser navigation:
```
http://your-hometube:8501/?url=https://youtube.com/watch?v=...&filename=My Video
```

<br/>

## 🚀 Quick Start

### Docker (Recommended)
```bash
# Clone this fork
git clone https://github.com/Pavarotty/hometube.git
cd hometube

# Configure hooks (optional)
cp .env.sample .env
# Edit .env with your hook commands

# Start with Docker
docker compose up -d

<!-- --- -->

<br/>
<br/>

![Application Demo](./docs/images/simple_ui_demo.gif)

<br/>
<br/>

<!-- --- -->

## 🛠️ HomeTube Options

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

# Access the interface
http://localhost:8501
```

<br/>

## 📚 Documentation

For detailed setup and usage instructions, refer to the original project documentation:
- **[Original Repository](https://github.com/EgalitarianMonkey/hometube)** - Complete documentation
- **[Installation Guide](https://github.com/EgalitarianMonkey/hometube/blob/main/docs/installation.md)** - Setup instructions
- **[Usage Guide](https://github.com/EgalitarianMonkey/hometube/blob/main/docs/usage.md)** - Feature documentation
- **[Docker Guide](https://github.com/EgalitarianMonkey/hometube/blob/main/docs/docker.md)** - Container deployment

### 📋 Quick Reference - Fork Documentation

- **[Hook Scripts via Files](docs/hooks-scripts.md)** - Running hook commands from mounted scripts
- **[Webhook API](docs/webhook.md)** - Webhook endpoint details

<br/>

## 🎣 Fork Differences

This fork adds:
- **Hook System**: Execute custom scripts on download events
- **Webhook Integration**: HTTP endpoints for automation  
- **Browser Integration**: Bookmarklets and GET parameter support

All original HomeTube features are preserved and fully compatible.

### 💭 Why This Fork?

I really loved the original HomeTube project and wanted to expand it with some automation features that I found useful for my personal use case. The hook system and webhook integration allow for better integration with home automation setups and make the download workflow much more streamlined.

<br/>

## 📄 License

This project is licensed under the GNU Affero General Public License v3.0 (AGPL-3.0).

See [LICENSE](LICENSE) file for details.

---

<div align="center">

**🎣 HomeTube Hooked** - *Enhanced fork of [EgalitarianMonkey/hometube](https://github.com/EgalitarianMonkey/hometube)*

</div>
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

- ✅ **Stable**: Core functionality tested and reliable
- 🔄 **Active Development**: Regular updates and improvements
- 🧪 **Test Coverage**: 84% on testable modules ([details](docs/testing.md))
- 📦 **Production Ready**: Docker images available on GHCR
- 🏠 **HomeLab Optimized**: Designed for self-hosted environments

## 📆 Coming Features

Check out the roadmap for upcoming features and enhancements:

**📋 See the complete roadmap**: [todo.md](todo.md)

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

This project is licensed under the GNU Affero General Public License v3.0 (AGPL-3.0).

See [LICENSE](LICENSE) file for details.

---

<div align="center">

**🎣 HomeTube Hooked** - *Enhanced fork of [EgalitarianMonkey/hometube](https://github.com/EgalitarianMonkey/hometube)*

</div>