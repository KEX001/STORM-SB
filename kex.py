import os
import logging
import signal
import sys
from flask import Flask
from flask_restful import Resource, Api

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def create_app():
    app = Flask(__name__)
    api = Api(app)

    class Greeting(Resource):
        def get(self):
            logger.info("[ꜱᴛᴏʀᴍ ᴀɪ] ɢᴀʟᴀᴄᴛɪᴄ ɢʀᴇᴇᴛɪɴɢ ᴇɴᴅᴘᴏɪɴᴛ ᴀᴄᴛɪᴠᴀᴛᴇᴅ 🌌")
            return {"message": "[ꜱᴛᴏʀᴍ ᴀɪ] ᴄᴏꜱᴍɪᴄ ꜱᴛᴏʀᴍ ɪɴɪᴛɪᴀᴛᴇᴅ. ʀᴇᴀᴅʏ ꜰᴏʀ ɪɴᴛᴇʀꜱᴛᴇʟʟᴀʀ ᴀᴅᴠᴇɴᴛᴜʀᴇꜱ. 🚀"}

    api.add_resource(Greeting, '/')

    return app

def signal_handler(sig, frame):
    logger.info("[ꜱᴛᴏʀᴍ ᴀɪ] ʀᴇᴄᴇɪᴠᴇᴅ ꜱʜᴜᴛᴅᴏᴡɴ ꜱɪɢɴᴀʟ, ɢʀᴀᴄᴇꜰᴜʟʟʏ ᴛᴇʀᴍɪɴᴀᴛɪɴɢ 🛑")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    app = create_app()

    port = int(os.environ.get("PORT", 8080))
    host = os.environ.get("HOST", "0.0.0.0")
    debug = bool(os.environ.get("DEBUG", False))

    logger.info(f"[ꜱᴛᴏʀᴍ ᴀɪ] ʟᴀᴜɴᴄʜɪɴɢ ɢᴀʟᴀᴄᴛɪᴄ ꜱᴇʀᴠᴇʀ 🌠 ᴏɴ {host}:{port} (Debug={debug})")

    try:
        app.run(host=host, port=port, debug=debug)
    except Exception as e:
        logger.error(f"[ꜱᴛᴏʀᴍ ᴀɪ] ꜰᴀɪʟᴇᴅ ᴛᴏ ꜱᴛᴀʀᴛ ᴀᴘᴘ ❌: {e}")
