FROM jauderho/yt-dlp:latest

# Add metadata
LABEL org.opencontainers.image.title="HomeTube"
LABEL org.opencontainers.image.description="Modern YouTube downloader with web interface for HomeLab and media servers"
LABEL org.opencontainers.image.url="https://github.com/EgalitarianMonkey/hometube"
LABEL org.opencontainers.image.source="https://github.com/EgalitarianMonkey/hometube"
LABEL org.opencontainers.image.licenses="AGPL-3.0-or-later"

# Install additional tools needed for HomeTube (Alpine packages)
RUN apk add --no-cache \
    tini \
    ca-certificates \
    curl

WORKDIR /app

# Copy only pyproject.toml first for better layer caching
COPY pyproject.toml ./

# Install Python dependencies (Alpine style with --break-system-packages)
RUN pip install --no-cache-dir --upgrade pip --break-system-packages

# Copy source code
COPY app/ ./app/

# Install the package (yt-dlp and ffmpeg already available!)
RUN pip install --no-cache-dir . --break-system-packages

# Copy Streamlit configuration for consistent UI theme
COPY .streamlit/ /app/.streamlit/

RUN mkdir -p /data/Videos /data/tmp /config

# Create non-root user for security (Alpine style)
RUN addgroup -g 1000 streamlit && \
    adduser -D -s /bin/sh -u 1000 -G streamlit streamlit && \
    chown -R streamlit:streamlit /app /data /config

USER streamlit

EXPOSE 8501
ENTRYPOINT ["/sbin/tini","--"]
CMD ["streamlit", "run", "app/main.py", "--server.enableCORS=false", "--server.enableXsrfProtection=false", "--server.address=0.0.0.0"]
