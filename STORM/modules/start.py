from telethon import __version__, Button
from STORM.client_manager import on_message
from config import VERSION, OWNER_ID
import sys

START_OP = [
    [
        Button.url("• ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ •", "https://github.com/KEX001/STORM-SB"),
    ],
    [
        Button.url("• ʜᴜʙ •", "https://t.me/SyphixHub"),
        Button.url("• ʟᴀʙꜱ •", "https://t.me/Syphixlabs"),
    ],
]

@on_message(pattern="/start")
async def start(event):
    if event.is_private:
        KEX = await event.client.get_me()
        bot_name = KEX.first_name
        bot_id = KEX.id
        
        try:
            owner = await event.client.get_entity(OWNER_ID)
            owner_name = owner.first_name
        except Exception:
            owner_name = "ᴏᴡɴᴇʀ"
            
        TEXT = (
            "<blockquote><b>❏ ꜱ ᴛ ᴏ ʀ ᴍ</b>\n"
            f"<b>├• ꜱᴇɴꜱᴇɪ:</b> <a href='tg://user?id={OWNER_ID}'>{owner_name}</a>\n"
            f"<b>├• ᴠᴇʀꜱɪᴏɴ:</b> <code>{VERSION}</code>\n"
            f"<b>├• ᴘʏᴛʜᴏɴ:</b> <code>{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}</code>\n"
            f"<b>├• ᴛᴇʟᴇᴛʜᴏɴ:</b> <code>{__version__}</code>\n"
            f"<b>└• ᴘᴏᴡᴇʀᴇᴅ ʙʏ:</b> <code>Ɵᴘᴜs 🤖</code>"
            "</blockquote>"
        )
        await event.client.send_file(
            event.chat_id,  
            "https://envs.sh/Pa1.mp4",
            caption=TEXT, 
            parse_mode='html',
            buttons=START_OP
        )
