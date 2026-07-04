#!/usr/bin/env bash
set -eo pipefail

DEFAULT_PORT=8080
DEFAULT_FLASK_APP="app:create_app()"
WORKERS=${WORKERS:-4}
LOG_FILE="main.log"

setup_logging() {
    exec > >(tee -a "$LOG_FILE") 2>&1
    echo "=== Storm Bot Startup $(date) ==="
}

validate_env() {
    if [ -f ".env" ]; then
        echo "📂 Loading environment variables from .env file..."
        set -a
        source .env
        set +a
    fi

    if [ -z "$PORT" ]; then
        echo "⚠️  PORT not set. Defaulting to $DEFAULT_PORT"
        export PORT=$DEFAULT_PORT
    fi

    if [ -z "$FLASK_APP" ]; then
        echo "⚠️  FLASK_APP not set. Defaulting to $DEFAULT_FLASK_APP"
        export FLASK_APP=$DEFAULT_FLASK_APP
    fi
}

cleanup() {
    echo "🛑 Initiating graceful shutdown..."
    kill -TERM "$gunicorn_pid" "$python_pid" 2>/dev/null || true
    wait "$gunicorn_pid" "$python_pid" || true
    echo "✅ Service shutdown complete"
}

main() {
    setup_logging
    validate_env

    trap cleanup SIGTERM SIGINT ERR

    echo "🚀 Starting Storm Spam Bot [Prime Version v3.1.1]"
    echo "🔌 Gunicorn serving on port $PORT with $WORKERS workers"
    
    GUNICORN_OPTS=(-w "$WORKERS" -b "0.0.0.0:${PORT:-$DEFAULT_PORT}" "$FLASK_APP")
    
    gunicorn "${GUNICORN_OPTS[@]}" &
    gunicorn_pid=$!
    
    python3 main.py &
    python_pid=$!

    echo "📌 Process IDs - Gunicorn: $gunicorn_pid, Python: $python_pid"
    echo "📝 Logging output to $LOG_FILE"
    
    wait "$gunicorn_pid"
}

main "$@"
