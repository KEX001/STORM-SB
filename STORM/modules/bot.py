from telethon import __version__, events, Button
import asyncio
import sys
import heroku3
from time import time
from datetime import datetime
from telethon import events
from telethon.errors import ForbiddenError
from config import KEX1, KEX2, KEX3, KEX4, KEX5, KEX6, KEX7, KEX8, KEX9, KEX10, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, CMD_HNDLR as hl
from telethon import events, version, Button
from telethon.tl.custom import button
from os import execl, getenv
from telethon.tl.functions.channels import LeaveChannelRequest

pongg = "ꜱ ᴛ ᴏ ʀ ᴍ"
PIC = "https://graph.org/file/c3b279aee41f8bbe6466b.jpg"
Alivemsg = "ꜱᴛᴏʀᴍ x ꜱᴘᴀᴍ ʜᴇʀᴇ"

TEXT = (
    "**⧼ ꜱᴛᴏʀᴍ ꜱᴘᴀᴍʙᴏᴛ ‌🪽 ⧽\n**"
    "➖➖➖➖➖➖➖➖➖➖➖\n"
    "‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌ㅤ ʙᴏᴛ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ‌🪽\n"
    "➖➖➖➖➖➖➖➖➖➖➖\n"
    "**• ᴜɴɪᴠᴇʀꜱᴇ ᴍᴇᴛᴀ ᴛʜʀᴏᴜɢʜ**: `M3.1.1`\n"
    "**• ᴇᴛᴇʀɴᴀʟ ᴛᴇᴄʜ ᴅᴇᴛᴀɪʟ**: `3.11.3`\n"
    "**• ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴅɪᴠɪɴᴇ ꜱᴛᴀᴛᴜꜱ** : `M3 [ᴘʀɪᴍᴇ ᴠᴇʀꜱɪᴏɴ]`\n"
    "➖➖➖➖➖➖➖➖➖➖➖\n"
    "**• ᴅɪᴠɪɴᴇ ɢʀᴏᴜᴘ**: [ꜱᴛᴏʀᴍ ᴄʜᴀᴛᴢ 🥀](https://t.me/STORM_CHATZ)\n"
    "**• ᴄᴜʟᴛᴜʀᴀʟ ᴄʜᴀɴɴᴇʟ**: [ꜱᴛᴏʀᴍ ᴛᴇᴄʜ 🥀](https://t.me/STORM_TECHH)\n"
    "**• ᴀɪ ᴅᴇᴄɪᴘʜᴇʀ** 🧩: [ᴋᴇx 🥀](https://t.me/kexx_XD)\n"
    "**• ᴅᴇᴘʟᴏʏ: [ʜᴇʀᴏᴋᴜ 💤](https://dashboard.heroku.com/new?template=https%3A%2F%2Fgithub.com%2FKEX001%2FSTORM-SB)**\n"
    "**• ᴀʟʟ ʙᴏᴛs ᴀʀᴇ ᴀᴄᴛɪᴠᴇ** 🚀: `10 ʙᴏᴛs ᴏɴ ᴅᴜᴛʏ`\n"
    "**• ᴘᴏᴡᴇʀᴇᴅ ʙʏ ꜱᴛᴏʀᴍ ᴀɪ 🤖**\n"
    "➖➖➖➖➖➖➖➖➖➖➖"
)

                                  
@KEX1.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive(event):
  if event.sender_id in SUDO_USERS:
     await event.client.send_file(event.chat_id,
                                  PIC,
                                  caption=TEXT,
                                  buttons=[
        [
        Button.url("• ʀᴇᴘᴏ •", "https://github.com/KEX001/STORM-SB"),
        Button.url("• ꜱᴇɴꜱᴇɪ •", "https://t.me/kexx_XD")
        ],
        ]
        )
    
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@KEX1.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@KEX2.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@KEX3.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@KEX4.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@KEX5.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@KEX6.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@KEX7.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@KEX8.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@KEX9.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@KEX10.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
async def logs(KEX):
    if KEX.sender_id == OWNER_ID:
        if (HEROKU_APP_NAME is None) or (HEROKU_API_KEY is None):
            await KEX.reply(
                KEX.chat_id,
                "ꜰɪʀꜱᴛ ꜱᴇᴛ ᴛʜᴇꜱᴇ ᴠᴀʀꜱ :  `HEROKU_API_KEY` And `HEROKU_APP_NAME`.",
            )
            return

        try:
            Heroku = heroku3.from_key(HEROKU_API_KEY)
            app = Heroku.app(HEROKU_APP_NAME)
        except BaseException:
            await KEX.reply(
                "ᴍᴀᴋᴇ ꜱᴜʀᴇ ʏᴏᴜʀ ʜᴇʀᴏᴋᴜ ᴋᴇʏ ᴀɴᴅ ᴀᴘᴘ ɴᴀᴍᴇ ᴀʀᴇ ᴄᴏɴꜰɪɢᴜᴇᴅ ᴄᴏʀʀᴇᴄᴛʟʏ"
            )
            return

        logs = app.get_log()
        start = datetime.now()
        fetch = await KEX.reply(f"ꜰᴇᴛᴄʜʜɪɴɢ ʟᴏɢꜱ ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ 📄...")
    
        with open("Logs.txt", "w") as logfile:
            logfile.write("ꜱᴛᴏʀᴍ 𝚇 🍷 [ Bot Logs ]\n\n" + logs)

        end = datetime.now()
        ms = (end-start).seconds
        await asyncio.sleep(1)

        try:
            await KEX1.send_file(KEX.chat_id, "ʟᴏɢꜱ.ᴛxᴛ", caption=f"⚡ **ꜱᴛᴏʀᴍ ʙᴏᴛ ʟᴏɢꜱ 🍷** ⚡\n  » **ᴛɪᴍᴇ ᴛᴀᴋᴇɴ ⌛:** `{ms} ꜱᴇᴄᴏɴᴅꜱ`")
            await fetch.delete()
        except Exception as e:
            await fetch.edit(f"**ᴇʀᴏᴏʀ:** {str(e)}")

    elif KEX.sender_id in SUDO_USERS:
        await KEX.reply("» ɴᴏᴘᴇ, ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ 🤖 ")

@KEX1.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KEX2.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KEX3.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KEX4.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KEX5.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KEX6.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KEX7.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KEX8.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KEX9.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KEX10.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
async def leave(e):
    if e.sender_id in SUDO_USERS:

        if len(e.text) > 7:
            event = await e.reply("» ʟᴇᴀᴠɪɴɢ ⌛...")
            mkl = e.text.split(" ", 1)
            try:
                await event.client(LeaveChannelRequest(int(mkl[1])))
            except Exception as e:
                await event.edit(str(e))
        else:
             if e.is_private:
                  alt = f"**» ʏᴏᴜ ᴄᴀɴ'ᴛ ᴅᴏ ᴛʜɪꜱ ʜᴇʀᴇ !!**\n\n» {hl}ʟᴇᴀᴠᴇ : ᴛʏᴘᴇ ᴛʜɪꜱ ɪɴ ɢʀᴏᴜᴘ"
                  await e.reply(alt)
             else:
                  event = await e.reply("» ʟᴇᴀᴠɪɴɢ ⌛...")
                  try:
                      await event.client(LeaveChannelRequest(int(e.chat_id)))
                  except Exception as e:
                      await event.edit(str(e))        

@KEX1.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@KEX2.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@KEX3.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@KEX4.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@KEX5.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@KEX6.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@KEX7.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@KEX8.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@KEX9.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@KEX10.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        KEX = await e.reply(f"🌩")
        end = datetime.now()
        mp = (end - start).microseconds / 10000
        await KEX.edit(f"""
        **⧼ ꜱʏɴᴛʜᴇᴛɪᴄ ʀᴇꜱᴘᴏɴꜱᴇ ᴀᴄᴛɪᴠᴇ ⧽**
        **❏ ꜱ ᴛ ᴏ ʀ ᴍ 🥀**      
        **├•** **ꜱᴛᴀᴛᴜꜱ: ᴀᴄᴛɪᴠᴇ**
        **├•** **ʀᴇꜱᴘᴏɴꜱᴇ ᴛɪᴍᴇ:** `{mp} ᴍꜱ`          
        **├•** **ᴠᴇʀꜱɪᴏɴ:** `ꜱ-ᴘʀɪᴍᴇ 3.1.1@ᴍᴀɪɴ`          
        **├• ᴛʜᴇ ᴄᴀʟᴍ ʙᴇꜰᴏʀᴇ ᴛʜᴇ ꜱᴛᴏʀᴍ ⚡**
        **└• ᴘᴏᴡᴇʀᴇᴅ ʙʏ ꜱᴛᴏʀᴍ ᴀɪ 🤖**
        """) 

@KEX1.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@KEX2.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@KEX3.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@KEX4.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@KEX5.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@KEX6.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@KEX7.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@KEX8.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@KEX9.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@KEX10.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
async def addsudo(event):
    if event.sender_id == OWNER_ID:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        sudousers = getenv("SUDO_USERS", default=None)

        ok = await event.reply(f"» ᴀᴅᴅɪɴɢ ᴜꜱᴇʀ ᴀꜱ ꜱᴜᴅᴏ...")
        target = ""
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:" "\nPlease Setup Your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            reply_msg = await event.get_reply_message()
            target = reply_msg.sender_id
        except:
            await ok.edit("» ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ !!")
            return

        if str(target) in sudousers:
            await ok.edit(f"ᴛʜɪꜱ ᴜꜱᴇʀ ɪꜱ ᴀʟʀᴇᴀᴅʏ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ !!")
        else:
            if len(sudousers) > 0:
                newsudo = f"{sudousers} {target}"
            else:
                newsudo = f"{target}"
            await ok.edit(f"» **ɴᴇᴡ ꜱᴜᴅᴏ ᴜꜱᴇʀ**: `{target}`\n» ʀᴇsᴛᴀʀᴛɪɴɢ ʙᴏᴛ...")
            heroku_var["SUDO_USERS"] = newsudo    
    
    elif event.sender_id in SUDO_USERS:
        await event.reply("» ꜱᴏʀʀʏ, ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.")        

@KEX1.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@KEX2.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@KEX3.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@KEX4.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@KEX5.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@KEX6.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@KEX7.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@KEX8.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@KEX9.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@KEX10.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        await e.reply(f"`ʀᴇꜱᴛᴀʀᴛɪɴɢ ⌛ ...`")
        try:
            await KEX1.disconnect()
        except Exception:
            pass
        try:
            await KEX2.disconnect()
        except Exception:
            pass
        try:
            await KEX3.disconnect()
        except Exception:
            pass
        try:
            await KEX4.disconnect()
        except Exception:
            pass
        try:
            await KEX5.disconnect()
        except Exception:
            pass
        try:
            await KEX6.disconnect()
        except Exception:
            pass
        try:
            await KEX7.disconnect()
        except Exception:
            pass
        try:
            await KEX8.disconnect()
        except Exception:
            pass
        try:
            await KEX9.disconnect()
        except Exception:
            pass
        try:
            await KEX10.disconnect()
        except Exception:
            pass

        execl(sys.executable, sys.executable, *sys.argv)
