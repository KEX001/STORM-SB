#!/usr/bin/env python3
import os
import logging
import signal
import sys
from typing import Optional, Dict, Any
from pathlib import Path
from flask import Flask, jsonify
from flask_restful import Api, Resource
from werkzeug.middleware.proxy_fix import ProxyFix


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('storm_server.log')
    ]
)
logger = logging.getLogger(__name__)

class HealthCheck(Resource):
    def get(self) -> Dict[str, Any]:
        return {
            "status": "operational",
            "version": "3.1.1",
            "system": "Storm AI",
            "message": "Cosmic systems nominal"
        }

class Greeting(Resource):
    def get(self) -> Dict[str, Any]:
        logger.info("Galactic greeting endpoint activated")
        return {
            "message": "Cosmic Storm initiated",
            "status": "ready",
            "features": [
                "interstellar communication",
                "quantum processing",
                "nebula navigation"
            ],
            "warning": "Do not point at event horizons"
        }

def create_app(test_config: Optional[Dict[str, Any]] = None) -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', 'dev_secret_key'),
        PREFERRED_URL_SCHEME=os.environ.get('PREFERRED_URL_SCHEME', 'https'),
        MAX_CONTENT_LENGTH=16 * 1024 * 1024,  # 16MB upload 
    )

    if test_config is None:

        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.update(test_config)

    api = Api(app, prefix='/api/v1')
    api.add_resource(HealthCheck, '/health')
    api.add_resource(Greeting, '/')

    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

    @app.route('/ping')
    def ping() -> Dict[str, str]:
        return jsonify({"status": "pong"})

    return app

def handle_shutdown(signum: int, frame: Any) -> None:
    logger.info(f"Received termination signal {signum}, initiating shutdown")
    sys.exit(0)

def register_signals() -> None:
    signals = [signal.SIGINT, signal.SIGTERM]
    for sig in signals:
        signal.signal(sig, handle_shutdown)

def main() -> None:
    register_signals()
    
    app = create_app()
    
    port = int(os.environ.get("PORT", 8080))
    host = os.environ.get("HOST", "0.0.0.0")
    debug = os.environ.get("DEBUG", "").lower() in ("true", "1", "t")
    
    logger.info(f"Launching Storm Server on {host}:{port} (Debug: {debug})")
    
    try:
        app.run(
            host=host,
            port=port,
            debug=debug,
            use_reloader=debug,
            threaded=True
        )
    except Exception as e:
        logger.critical(f"Failed to start server: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
