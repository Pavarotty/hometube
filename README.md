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

Note: The container includes `ssh`/`scp` (OpenSSH client) so hooks can securely copy files or execute remote commands on other machines using `ssh user@host` or `scp {OUTPUT_PATH} user@host:/path/`.

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