import logging
import os
from typing import List, Optional
from telethon import TelegramClient
from dotenv import load_dotenv
from strings.helpers import DEV

load_dotenv()

logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING
)
logger = logging.getLogger(__name__)

class BotConfig:

    API_ID: int = 18136872
    API_HASH: str = "312d861b78efcd1b02183b2ab52a83a4"
    
    CMD_HNDLR: str = os.getenv("CMD_HNDLR", "!")
    
    HEROKU_APP_NAME: Optional[str] = os.getenv("HEROKU_APP_NAME")
    HEROKU_API_KEY: Optional[str] = os.getenv("HEROKU_API_KEY")
    
    MBOT_USERNAME: Optional[str] = os.getenv("MBOT_USERNAME")

    BOT_TOKENS: List[Optional[str]] = [
        os.getenv("BOT_TOKEN"),
        os.getenv("BOT_TOKEN2"),
        os.getenv("BOT_TOKEN3"),
        os.getenv("BOT_TOKEN4"),
        os.getenv("BOT_TOKEN5"),
        os.getenv("BOT_TOKEN6"),
        os.getenv("BOT_TOKEN7"),
        os.getenv("BOT_TOKEN8"),
        os.getenv("BOT_TOKEN9"),
        os.getenv("BOT_TOKEN10")
    ]
    
    OWNER_ID: int = int(os.getenv("OWNER_ID", "6257927828"))
    SUDO_USERS: List[int] = list(map(int, os.getenv("SUDO_USERS", "6257927828").split()))
    
    def __init__(self):
        self.SUDO_USERS.extend(DEV)
        self.SUDO_USERS.append(self.OWNER_ID)
        self.validate_tokens()
        
    def validate_tokens(self):
        if not all(self.BOT_TOKENS[:5]):
            logger.error("Missing one or more compulsory bot tokens (1-5)")
            raise ValueError("Compulsory bot tokens not configured")

    def initialize_bots(self):
        bots = []
        for i, token in enumerate(self.BOT_TOKENS, 1):
            if token:
                try:
                    client = TelegramClient(f'STORM {i}', self.API_ID, self.API_HASH)
                    client.start(bot_token=token)
                    bots.append(client)
                    logger.info(f"Successfully initialized STORM {i}")
                except Exception as e:
                    logger.error(f"Failed to initialize STORM {i}: {str(e)}")
                    if i <= 5: 
                        raise
        return bots

try:
    config = BotConfig()
    KEX1, KEX2, KEX3, KEX4, KEX5, *optional_bots = config.initialize_bots()
    KEX6, KEX7, KEX8, KEX9, KEX10 = optional_bots + [None]*(5-len(optional_bots))
except Exception as e:
    logger.critical(f"Configuration failed: {str(e)}")
    raise
