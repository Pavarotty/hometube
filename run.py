#!/usr/bin/env python3
"""
Script de lancement simple pour l'application hometube
Usage: python run.py
"""

import os
import sys
import subprocess
from pathlib import Path


def main():
    # Get the directory where this script is located
    script_dir = Path(__file__).parent
    app_file = script_dir / "app" / "main.py"

    if not app_file.exists():
        print("❌ Error: app/main.py file not found!")
        sys.exit(1)

    # Check if streamlit is installed
    try:
        import streamlit

        print("✅ Streamlit trouvé!")
    except ImportError:
        print("❌ Streamlit n'est pas installé!")
        print("   Installez-le avec: pip install streamlit")
        sys.exit(1)

    # Check if yt-dlp is installed
    try:
        subprocess.run(["yt-dlp", "--version"], capture_output=True, check=True)
        print("✅ yt-dlp trouvé!")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ yt-dlp n'est pas installé ou n'est pas dans le PATH!")
        print("   Installez-le avec: pip install yt-dlp")
        sys.exit(1)

    # Load port from .env if available
    env_file = script_dir / ".env"
    port = "8502"  # default port

    if env_file.exists():
        print(f"✅ Fichier .env trouvé: {env_file}")
        with open(env_file, "r") as f:
            for line in f:
                if line.strip().startswith("STREAMLIT_PORT="):
                    port = line.split("=")[1].strip()
                    break
    else:
        print("⚠️  Fichier .env non trouvé, utilisation des valeurs par défaut")

    print(f"🚀 Lancement de l'application sur le port {port}")
    print(f"🌐 Ouvrez votre navigateur sur: http://localhost:{port}")
    print("   Appuyez sur Ctrl+C pour arrêter l'application")

    # Launch streamlit
    try:
        subprocess.run(
            [
                sys.executable,
                "-m",
                "streamlit",
                "run",
                str(app_file),
                "--server.port",
                port,
                "--server.headless",
                "true",
                "--browser.gatherUsageStats",
                "false",
            ]
        )
    except KeyboardInterrupt:
        print("\n👋 Application arrêtée")


if __name__ == "__main__":
    main()
