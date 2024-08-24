from telethon import __version__, events, Button
from config import KEX1, KEX2, KEX3, KEX4, KEX5, KEX6, KEX7, KEX8, KEX9, KEX10

START_OP = [
    [
        Button.url("ꜱᴇɴꜱᴇɪ 🥀", "https://t.me/Kexx_XD"),
        Button.url("ꜱᴜᴘᴘᴏʀᴛ 🧸", "https://t.me/TORNADO_TRIBE"),
    ],
    [
        Button.url("ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ❄️", "https://github.com/KEX001/STORM-SB"),
    ],
    [
        Button.url("ꜱᴜᴘᴘᴏʀᴛ ✨", "https://t.me/STORM_CHATZ"),
        Button.url("ᴄʜᴀɴɴᴇʟ ☁️", "https://t.me/STORM_TECHH"),
    ],
]

@KEX1.on(events.NewMessage(pattern="/start"))
@KEX2.on(events.NewMessage(pattern="/start"))
@KEX3.on(events.NewMessage(pattern="/start"))
@KEX4.on(events.NewMessage(pattern="/start"))
@KEX5.on(events.NewMessage(pattern="/start"))
@KEX6.on(events.NewMessage(pattern="/start"))
@KEX7.on(events.NewMessage(pattern="/start"))
@KEX8.on(events.NewMessage(pattern="/start"))
@KEX9.on(events.NewMessage(pattern="/start"))
@KEX10.on(events.NewMessage(pattern="/start"))
async def start(event):
    if event.is_private:
        KEX = await event.client.get_me()
        bot_name = KEX.first_name
        bot_id = KEX.id
        TEXT = f"**ʜᴇʏ [{event.sender.first_name}] 🌟**\n**ɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})​**\n➖➖➖➖➖➖➖➖➖➖➖\n"
        TEXT += f"» **ꜱᴇɴꜱᴇɪ : [⏤͟͞〲ᴋᴇx](https://t.me/kexx_xd)**\n"
        TEXT += f"» **ꜱᴛᴏʀᴍ :** `M3 [ᴘʀɪᴍᴇ ᴠᴇʀꜱɪᴏɴ]` \n"
        TEXT += f"» **ᴘʏᴛʜᴏɴ :** `3.11` \n"
        TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ :** `{__version__}`\n➖➖➖➖➖➖➖➖➖➖➖\n"
        TEXT += f"» **ᴘᴏᴡᴇʀᴇᴅ ʙʏ ꜱᴛᴏʀᴍ ᴀɪ** 🌟\n"
        TEXT += f"🔍 **ᴅɪsᴄᴏᴠᴇʀ ᴍᴏʀᴇ:-**\n"
        TEXT += f"   » **[ꜱᴛᴏʀᴍ ᴄʜᴀᴛᴢ](https://t.me/STORM_CHATZ)**\n"
        TEXT += f"   » **[ꜱᴛᴏʀᴍ ᴛᴇᴄʜ](https://t.me/STORM_TECHH)**\n"
        TEXT += f"   » **[ᴋᴇx](https://t.me/kexx_XD): ᴄᴏɴɴᴇᴄᴛ ᴡɪᴛʜ ᴛʜᴇ ᴅᴇᴠᴇʟᴏᴘᴇʀ.**\n"
        TEXT += f"**sᴜᴘᴘᴏʀᴛ: ɪꜰ ʏᴏᴜ ɴᴇᴇᴅ ᴀꜱꜱɪꜱᴛᴀɴᴄᴇ, ᴅᴏɴ'ᴛ ʜᴇꜱɪᴛᴀᴛᴇ ᴛᴏ ᴀꜱᴋ**\n➖➖➖➖➖➖➖➖➖➖➖"          
        await event.client.send_file(
                    event.chat_id,  
                    "https://graph.org/file/c3b279aee41f8bbe6466b.jpg",
                    caption=TEXT, 
                    buttons=START_OP
                )
