#!/usr/bin/env python3
"""
Module principal de l'application hometube
Peut être importé comme module Python pour une utilisation programmatique
"""

import os
import subprocess
import time
from pathlib import Path


def setup_environment():
    """Configure l'environnement pour l'application"""
    # Try project root .env first, then app/.env as fallback
    app_dir = Path(__file__).parent
    project_root = app_dir.parent
    env_file = project_root / ".env"
    if not env_file.exists():
        env_file = app_dir / ".env"
    if env_file.exists():
        with open(env_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    key = key.strip()
                    value = value.strip().strip("\"'")
                    if key not in os.environ:
                        os.environ[key] = value


# --- Hooks helpers (duplicated lightweight version for programmatic API) ---
def _hook_format(template: str, ctx: dict) -> str:
    ctx = dict(ctx)
    def q(v: str) -> str:
        if v is None:
            return ""
        return '"' + str(v).replace('"', '\\"') + '"'
    for k, v in list(ctx.items()):
        ctx[f"{k}_Q"] = q(v)
    try:
        return template.format_map(ctx)
    except Exception:
        return template


def _run_hook(event: str, ctx: dict, timeout: int = 30):
    env_key = {
        "start": "ON_DOWNLOAD_START",
        "success": "ON_DOWNLOAD_SUCCESS",
        "failure": "ON_DOWNLOAD_FAILURE",
    }.get(event)
    if not env_key:
        return
    tpl = os.getenv(env_key, "").strip()
    if not tpl:
        return
    cmd = _hook_format(tpl, ctx)
    try:
        subprocess.run(cmd, shell=True, timeout=timeout, check=False)
    except Exception:
        pass


def run_app(port=8502, debug=False):
    """
    Lance l'application Streamlit

    Args:
        port (int): Port sur lequel lancer l'application
        debug (bool): Mode debug
    """
    import sys

    setup_environment()

    app_file = Path(__file__).parent / "app" / "main.py"

    cmd = [
        sys.executable,
        "-m",
        "streamlit",
        "run",
        str(app_file),
        "--server.port",
        str(port),
        "--server.headless",
        "true" if not debug else "false",
        "--browser.gatherUsageStats",
        "false",
    ]

    try:
        subprocess.run(cmd)
    except KeyboardInterrupt:
        print("\n👋 Application arrêtée")


def download_video(url, filename, **options):
    """
    Function to download a video directly (programmatic usage)

    Args:
        url (str): Video URL
        filename (str): Output filename
        **options: Additional options

    Returns:
        bool: True if success, False otherwise
    """
    setup_environment()

    # Import necessary modules
    from app.main import sanitize_url, ensure_dir
    import subprocess

    try:
        # Basic configuration
        videos_folder = Path(os.getenv("VIDEOS_FOLDER", str(Path.home() / "Downloads")))
        ensure_dir(videos_folder)

        clean_url = sanitize_url(url)

        # Basic yt-dlp command
        cmd = [
            "yt-dlp",
            "-o",
            str(videos_folder / f"{filename}.%(ext)s"),
            "--merge-output-format",
            "mp4",
            clean_url,
        ]

        print(f"📥 Downloading: {url}")
        print(f"📁 Destination: {videos_folder / filename}")

        # Hook: start
        hook_ctx = {
            "URL": clean_url,
            "FILENAME": filename,
            "DEST_DIR": str(videos_folder),
            "TMP_DIR": "",
            "OUTPUT_PATH": "",
            "STATUS": "start",
            "RUN_SEQ": "",
            "TS": str(int(time.time())),
            "START_SEC": "",
            "END_SEC": "",
        }
        _run_hook("start", hook_ctx)

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode == 0:
            print("✅ Download successful!")
            # Try find actual output file to pass to hook
            output_path = None
            try:
                matches = list(videos_folder.glob(f"{filename}.*"))
                if matches:
                    output_path = str(matches[0])
            except Exception:
                output_path = None

            hook_ctx.update({
                "STATUS": "success",
                "OUTPUT_PATH": output_path or str(videos_folder / filename),
                "TS": str(int(time.time())),
            })
            _run_hook("success", hook_ctx)
            return True
        else:
            print(f"❌ Error: {result.stderr}")
            hook_ctx.update({
                "STATUS": "download_failed",
                "TS": str(int(time.time())),
            })
            _run_hook("failure", hook_ctx)
            return False

    except Exception as e:
        print(f"❌ Error: {e}")
        try:
            hook_ctx.update({
                "STATUS": "exception",
                "TS": str(int(time.time())),
            })
            _run_hook("failure", hook_ctx)
        except Exception:
            pass
        return False


if __name__ == "__main__":
    # If the script is run directly, launch the Streamlit interface
    run_app()
