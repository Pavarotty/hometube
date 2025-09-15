#!/bin/bash
# Script pour mettre à jour tous les fichiers requirements

echo "🔄 Mise à jour des dépendances avec UV..."

# Mettre à jour le lockfile
echo "📦 Mise à jour du lockfile..."
uv lock --upgrade

# Regénérer requirements.txt de production
echo "📝 Génération de requirements.txt..."
uv pip compile pyproject.toml -o requirements/requirements.txt

# Regénérer requirements-dev.txt
echo "🛠️ Génération de requirements-dev.txt..."
uv pip compile pyproject.toml --extra dev -o requirements/requirements-dev.txt

echo "✅ Fichiers requirements mis à jour !"
echo ""
echo "📋 Fichiers générés :"
echo "  - requirements/requirements.txt (production)"
echo "  - requirements/requirements-dev.txt (développement)"
echo "  - uv.lock (lockfile)"