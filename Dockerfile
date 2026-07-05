FROM python:3.10-slim

WORKDIR /app

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends git ffmpeg curl gcc g++ && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x start.sh

ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    PORT=8080

EXPOSE $PORT
HEALTHCHECK --interval=30s --timeout=3s \
    CMD curl -f http://localhost:${PORT:-8080}/api/v1/health || exit 1

CMD ["./start.sh"]
