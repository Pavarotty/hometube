# Docker Usage

Ce guide explique comment utiliser l'image Docker du hometube.

## Images disponibles

L'image est disponible sur GitHub Container Registry :
- `ghcr.io/EgalitarianMonkey/hometube:latest` - Version stable (branche main)
- `ghcr.io/EgalitarianMonkey/hometube:v1.0.0` - Version taguée spécifique
- `ghcr.io/EgalitarianMonkey/hometube:main` - Version de développement

## Usage rapide

### Avec docker run

```bash
# Utilisation basique
docker run -p 8501:8501 ghcr.io/EgalitarianMonkey/hometube:latest

# Avec volumes pour persistance des téléchargements
docker run -p 8501:8501 \
  -v ./downloads:/data/Videos \
  -v ./cookies:/config \
  ghcr.io/EgalitarianMonkey/hometube:latest

# Avec configuration complète
docker run -p 8501:8501 \
  -v ./downloads:/data/Videos \
  -v ./tmp:/data/tmp \
  -v ./cookies:/config \
  -e STREAMLIT_SERVER_PORT=8501 \
  ghcr.io/EgalitarianMonkey/hometube:latest
```

### Avec docker-compose

```yaml
version: '3.8'

services:
  hometube:
    image: ghcr.io/EgalitarianMonkey/hometube:latest
    ports:
      - "8501:8501"
    volumes:
      - ./downloads:/data/Videos
      - ./tmp:/data/tmp
      - ./cookies:/config
    environment:
      - STREAMLIT_SERVER_PORT=8501
      - STREAMLIT_SERVER_ADDRESS=0.0.0.0
    restart: unless-stopped
```

## Volumes

| Volume | Description | Obligatoire |
|--------|-------------|-------------|
| `/data/Videos` | Dossier de sortie des vidéos téléchargées | Recommandé |
| `/data/tmp` | Fichiers temporaires de traitement | Optionnel |
| `/config` | Fichiers de cookies et configuration | Optionnel |

## Variables d'environnement

| Variable | Valeur par défaut | Description |
|----------|------------------|-------------|
| `STREAMLIT_SERVER_PORT` | `8501` | Port d'écoute de l'application |
| `STREAMLIT_SERVER_ADDRESS` | `0.0.0.0` | Adresse d'écoute |

## Accès

Une fois le conteneur démarré, accédez à l'application via :
- http://localhost:8501

## Sécurité

### Pour un usage en production

```bash
# Avec authentification basique (à configurer dans un reverse proxy)
docker run -p 127.0.0.1:8501:8501 \
  -v ./downloads:/data/Videos \
  -v ./cookies:/config \
  ghcr.io/EgalitarianMonkey/hometube:latest
```

### Reverse proxy (nginx)

```nginx
server {
    listen 80;
    server_name videos.example.com;
    
    location / {
        proxy_pass http://localhost:8501;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # WebSocket support for Streamlit
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```

## Mise à jour

```bash
# Arrêter le conteneur
docker stop hometube

# Supprimer l'ancien conteneur
docker rm hometube

# Télécharger la nouvelle image
docker pull ghcr.io/EgalitarianMonkey/hometube:latest

# Redémarrer avec la nouvelle image
docker run -p 8501:8501 \
  -v ./downloads:/data/Videos \
  -v ./cookies:/config \
  --name hometube \
  ghcr.io/EgalitarianMonkey/hometube:latest
```

## Troubleshooting

### Logs du conteneur
```bash
docker logs hometube
```

### Accès au conteneur
```bash
docker exec -it hometube /bin/bash
```

### Vérifier les volumes
```bash
# Vérifier l'espace disque
docker exec hometube df -h

# Lister les fichiers téléchargés
docker exec hometube ls -la /data/Videos
```

## Construction locale

Pour construire l'image localement :

```bash
# Cloner le repository
git clone https://github.com/EgalitarianMonkey/hometube.git
cd hometube

# Construire l'image
docker build -t hometube:local .

# Lancer l'image locale
docker run -p 8501:8501 hometube:local
```