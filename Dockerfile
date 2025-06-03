FROM nikolaik/python-nodejs:python3.10-nodejs19 as builder
WORKDIR /app
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    ffmpeg \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
FROM nikolaik/python-nodejs:python3.10-nodejs19-slim
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN groupadd -r storm && useradd -r -g storm storm && \
    mkdir -p /app && chown storm:storm /app
WORKDIR /app
USER storm
COPY --chown=storm:storm . .
RUN find /app -type d -exec chmod 755 {} \; && \
    find /app -type f -exec chmod 644 {} \; && \
    chmod +x start.sh
HEALTHCHECK --interval=30s --timeout=3s \
    CMD curl -f http://localhost:8080/api/v1/health || exit 1
ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    PIP_NO_CACHE_DIR=1 \
    NODE_ENV=production
EXPOSE 8080
ENTRYPOINT ["./start.sh"]
