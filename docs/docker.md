# Docker Usage

Ce guide explique comment utiliser l'image Docker du hometube.

## Images disponibles

L'image est disponible sur GitHub Container Registry :
- `ghcr.io/EgalitarianMonkey/hometube:latest` - Version stable (branche main)
- `ghcr.io/EgalitarianMonkey/hometube:v1.0.0` - Version taguée spécifique
- `ghcr.io/EgalitarianMonkey/hometube:main` - Version de développement

## Quick start

### With docker run

```bash
# Basic usage
docker run -p 8501:8501 ghcr.io/EgalitarianMonkey/hometube:latest

# With volumes for download persistence
docker run -p 8501:8501 \
  -v ./downloads:/data/Videos \
  -v ./cookies:/config \
  ghcr.io/EgalitarianMonkey/hometube:latest

# With complete configuration
docker run -p 8501:8501 \
  -v ./downloads:/data/Videos \
  -v ./tmp:/data/tmp \
  -v ./cookies:/config \
  -e STREAMLIT_SERVER_PORT=8501 \
  ghcr.io/EgalitarianMonkey/hometube:latest
```

### With docker-compose

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

| Volume | Description | Required |
|--------|-------------|----------|
| `/data/Videos` | Output folder for downloaded videos | Recommended |
| `/data/tmp` | Temporary processing files | Optional |
| `/config` | Cookie files and configuration | Optional |

## Environment variables

| Variable | Default value | Description |
|----------|---------------|-------------|
| `STREAMLIT_SERVER_PORT` | `8501` | Application listening port |
| `STREAMLIT_SERVER_ADDRESS` | `0.0.0.0` | Listening address |

## Access

Once the container is started, access the application via:
- http://localhost:8501

## Security

### For production use

```bash
# With basic authentication (to be configured in a reverse proxy)
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

## Update

```bash
# Stop the container
docker stop hometube

# Remove the old container
docker rm hometube

# Download the new image
docker pull ghcr.io/EgalitarianMonkey/hometube:latest

# Restart with the new image
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

### Container access
```bash
docker exec -it hometube /bin/bash
```

### Check volumes
```bash
# Check disk space
docker exec hometube df -h

# List downloaded files
docker exec hometube ls -la /data/Videos
```

## Local build

To build the image locally:

```bash
# Clone the repository
git clone https://github.com/EgalitarianMonkey/hometube.git
cd hometube

# Build the image
docker build -t hometube:local .

# Run the local image
docker run -p 8501:8501 hometube:local
```