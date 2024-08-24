import logging
from telethon import TelegramClient
from os import getenv
from strings.helpers import DEV
from dotenv import load_dotenv

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

API_ID = 18136872
API_HASH = "312d861b78efcd1b02183b2ab52a83a4"
CMD_HNDLR = getenv("CMD_HNDLR", default="!")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
BOT_TOKEN = getenv("BOT_TOKEN", default=None)
BOT_TOKEN2 = getenv("BOT_TOKEN2", default=None)
BOT_TOKEN3 = getenv("BOT_TOKEN3", default=None)
BOT_TOKEN4 = getenv("BOT_TOKEN4", default=None)
BOT_TOKEN5 = getenv("BOT_TOKEN5", default=None)
BOT_TOKEN6 = getenv("BOT_TOKEN6", default=None)
BOT_TOKEN7 = getenv("BOT_TOKEN7", default=None)
BOT_TOKEN8 = getenv("BOT_TOKEN8", default=None)
BOT_TOKEN9 = getenv("BOT_TOKEN9", default=None)
BOT_TOKEN10 = getenv("BOT_TOKEN10", default=None)

SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="6257927828").split()))
for x in DEV:
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="6257927828"))
SUDO_USERS.append(OWNER_ID)

KEX1 = TelegramClient('ꜱ ᴛ ᴏ ʀ ᴍ 1', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
KEX2 = TelegramClient('ꜱ ᴛ ᴏ ʀ ᴍ 2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)
KEX3 = TelegramClient('ꜱ ᴛ ᴏ ʀ ᴍ 3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)
KEX4 = TelegramClient('ꜱ ᴛ ᴏ ʀ ᴍ 4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)
KEX5 = TelegramClient('ꜱ ᴛ ᴏ ʀ ᴍ 5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)
KEX6 = TelegramClient('ꜱ ᴛ ᴏ ʀ ᴍ 6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)
KEX7 = TelegramClient('ꜱ ᴛ ᴏ ʀ ᴍ 7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)
KEX8 = TelegramClient('ꜱ ᴛ ᴏ ʀ ᴍ 8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)
KEX9 = TelegramClient('ꜱ ᴛ ᴏ ʀ ᴍ 9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)
KEX10 = TelegramClient('ꜱ ᴛ ᴏ ʀ ᴍ 10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)
