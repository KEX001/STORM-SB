import asyncio
from random import choice
from config import SUDO_USERS, OWNER_ID, CMD_HNDLR as hl, check_protection, get_delay
from STORMDB.emojidb import EMOJI
from STORMDB.flirtdb import FLIRT
from STORMDB.wishdb import GM
from STORMDB.lraiddb import LOVERAID
from STORMDB.sraiddb import SRAID
from strings.helpers import GROUP, DEV
from STORM.client_manager import on_cmd, on_message

ECHO = []

@on_cmd("echo")
async def echo(event):
    if event.sender_id in SUDO_USERS:
        if event.reply_to_msg_id:
            reply_msg = await event.get_reply_message()
            user_id = reply_msg.sender_id

            if await check_protection(event, user_id):
                return
            if user_id in DEV:
                await event.reply("<blockquote><b>» ɴᴏᴘᴇ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ❌</b></blockquote>", parse_mode="html")
            elif user_id == OWNER_ID:
                await event.reply("<blockquote><b>» ɴᴏᴘᴇ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ ❌</b></blockquote>", parse_mode="html")
            elif user_id in SUDO_USERS:
                await event.reply("<blockquote><b>» ɴᴏᴘᴇ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ꜱᴜᴅᴏ ᴜꜱᴇʀ ❌</b></blockquote>", parse_mode="html")
            else:
                global ECHO
                check = f"{user_id}_{event.chat_id}"
                if check in ECHO:
                    await event.reply("<blockquote><b>» ᴇᴄʜᴏ ɪꜱ ᴀᴄᴛɪᴠᴀᴛᴇᴅ ✅ !!</b></blockquote>", parse_mode="html")
                else:
                    ECHO.append(check)
                    await event.reply("<blockquote><b>» ᴇᴄʜᴏ ɪꜱ ᴀᴄᴛɪᴠᴀᴛᴇᴅ ✅ !!</b></blockquote>", parse_mode="html")
        else:
            await event.reply(f"```{hl}ᴇᴄʜᴏ <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>```")

@on_cmd("rmecho")
async def rmecho(event):
    if event.sender_id in SUDO_USERS:
        if event.reply_to_msg_id:
            global ECHO
            reply_msg = await event.get_reply_message()
            check = f"{reply_msg.sender_id}_{event.chat_id}"

            if check in ECHO:
                ECHO.remove(check)
                await event.reply("<blockquote><b>» ᴇᴄʜᴏ ɪꜱ ꜱᴛᴏᴘᴘᴇᴅ !! ✅</b></blockquote>", parse_mode="html")
            else:
                await event.reply("<blockquote><b>» ᴇᴄʜᴏ ɪꜱ ꜱᴛᴏᴘᴘᴇᴅ !! 👀</b></blockquote>", parse_mode="html")
        else:
            await event.reply(f"```{hl}ʀᴍᴇᴄʜᴏ <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>```")

@on_message(incoming=True)
async def echo_listener(e):
    global ECHO
    check = f"{e.sender_id}_{e.chat_id}"
    if check in ECHO:
        if await check_protection(e):
            try:
                ECHO.remove(check)
            except Exception:
                pass
            return
        if e.message.text or e.message.sticker:
            await e.reply(e.message)
            await asyncio.sleep(get_delay(e.chat_id, 0.1))

@on_cmd("emoji")
async def emoji(e):
     if e.sender_id in SUDO_USERS:
        xraid = e.text.split(" ", 2)
        if len(xraid) == 3:
            entity = await e.client.get_entity(xraid[2])
            uid = entity.id
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)
            uid = entity.id
        try:
            if await check_protection(e, uid):
                return
            if uid in DEV:
                await e.reply("<blockquote><b>» ɴᴏᴘᴇ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ʙᴏᴛ ᴏᴡɴᴇʀ ❌</b></blockquote>", parse_mode="html")
            elif uid == OWNER_ID:
                await e.reply("<blockquote><b>» ɴᴏᴘᴇ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ ❌</b></blockquote>", parse_mode="html")
            elif uid in SUDO_USERS:
                await e.reply("<blockquote><b>» ɴᴏᴘᴇ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ꜱᴜᴅᴏ ᴜꜱᴇʀ ❌</b></blockquote>", parse_mode="html")
            else:
                first_name = entity.first_name
            counter = int(xraid[1])
            username = f"[{first_name}](tg://user?id={uid})"
            for _ in range(counter):
                reply = choice(EMOJI)
                caption = f"{username} {reply}"
                await e.client.send_message(e.chat_id, caption)
                await asyncio.sleep(get_delay(e.chat_id, 0.1))
        except (IndexError, ValueError, NameError):
            await e.reply(f"```{hl}ᴇᴍᴏᴊɪ <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>```")
        except Exception as err:
            logger.error(f"Error in emoji: {err}")

@on_cmd("flirt")
async def flirt(e):
     if e.sender_id in SUDO_USERS:
        xraid = e.text.split(" ", 2)
        try:
            if len(xraid) == 3:
                entity = await e.client.get_entity(xraid[2])
                uid = entity.id
            elif e.reply_to_msg_id:             
                a = await e.get_reply_message()
                entity = await e.client.get_entity(a.sender_id)
                uid = entity.id
            else:
                await e.reply(f"```{hl}ꜰʟɪʀᴛ <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>```")
                return

            if await check_protection(e, uid):
                return
            if uid in DEV:
                await e.reply("<blockquote><b>» ɴᴏᴘᴇ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ʙᴏᴛ ᴏᴡɴᴇʀ ❌</b></blockquote>", parse_mode="html")
            elif uid == OWNER_ID:
                await e.reply("<blockquote><b>» ɴᴏᴘᴇ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ ❌</b></blockquote>", parse_mode="html")
            elif uid in SUDO_USERS:
                await e.reply("<blockquote><b>» ɴᴏᴘᴇ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ꜱᴜᴅᴏ ᴜꜱᴇʀ ❌</b></blockquote>", parse_mode="html")
            else:
                first_name = entity.first_name
                counter = int(xraid[1])
                username = f"<a href='tg://user?id={uid}'>{first_name}</a>"
                for _ in range(counter):
                    reply = choice(FLIRT)
                    caption = f"<blockquote><b>{username} {reply}</b></blockquote>"
                    try:
                        await e.client.send_message(e.chat_id, caption, parse_mode='html')
                    except FloodWaitError as err:
                        await asyncio.sleep(err.seconds)
                    await asyncio.sleep(get_delay(e.chat_id, 0.1))
        except (IndexError, ValueError, NameError):
            await e.reply(f"```{hl}ꜰʟɪʀᴛ <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>```")
        except Exception as err:
            logger.error(f"Error in flirt: {err}")

@on_cmd("gm")
async def gm(e):
     if e.sender_id in SUDO_USERS:
        xraid = e.text.split(" ", 2)
        try:
            if len(xraid) == 3:
                entity = await e.client.get_entity(xraid[2])
                uid = entity.id
            elif e.reply_to_msg_id:             
                a = await e.get_reply_message()
                entity = await e.client.get_entity(a.sender_id)
                uid = entity.id
            else:
                await e.reply(f"```{hl}ɢᴍ <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>```")
                return

            if await check_protection(e, uid):
                return
            if uid in DEV:
                await e.reply("<blockquote><b>» ɴᴏᴘᴇ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ʙᴏᴛ ᴏᴡɴᴇʀ ❌</b></blockquote>", parse_mode="html")
            elif uid == OWNER_ID:
                await e.reply("<blockquote><b>» ɴᴏᴘᴇ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ ❌</b></blockquote>", parse_mode="html")
            elif uid in SUDO_USERS:
                await e.reply("<blockquote><b>» ɴᴏᴘᴇ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ꜱᴜᴅᴏ ᴜꜱᴇʀ ❌</b></blockquote>", parse_mode="html")
            else:
                first_name = entity.first_name
                counter = int(xraid[1])
                username = f"[{first_name}](tg://user?id={uid})"
                for _ in range(counter):
                    reply = choice(GM)
                    caption = f"{username} {reply}"
                    try:
                        await e.client.send_message(e.chat_id, caption)
                    except FloodWaitError as err:
                        await asyncio.sleep(err.seconds)
                    await asyncio.sleep(get_delay(e.chat_id, 0.1))
        except (IndexError, ValueError, NameError):
            await e.reply(f"```{hl}ɢᴍ <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>```")
        except Exception as err:
            logger.error(f"Error in gm: {err}")

@on_cmd("loveraid")
async def loveraid(e):
    if e.sender_id in SUDO_USERS:
        xraid = e.text.split(" ", 2)
        try:
            if len(xraid) == 3:
                entity = await e.client.get_entity(xraid[2])
                uid = entity.id
            elif e.reply_to_msg_id:             
                a = await e.get_reply_message()
                entity = await e.client.get_entity(a.sender_id)
                uid = entity.id
            else:
                await e.reply(f"```{hl}ʟᴏᴠᴇʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>```")
                return

            if await check_protection(e, uid):
                return
            if uid in DEV:
                await e.reply("<blockquote><b>» ɴᴏᴘᴇ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ʙᴏᴛ ᴏᴡɴᴇʀ ❌</b></blockquote>", parse_mode="html")
            elif uid == OWNER_ID:
                await e.reply("<blockquote><b>» ɴᴏᴘᴇ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ ❌</b></blockquote>", parse_mode="html")
            elif uid in SUDO_USERS:
                await e.reply("<blockquote><b>» ɴᴏᴘᴇ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ꜱᴜᴅᴏ ᴜꜱᴇʀ ❌</b></blockquote>", parse_mode="html")
            else:
                first_name = entity.first_name
                counter = int(xraid[1])
                username = f"<a href='tg://user?id={uid}'>{first_name}</a>"
                for _ in range(counter):
                    reply = choice(LOVERAID)
                    caption = f"<blockquote><b>{username} {reply}</b></blockquote>"
                    try:
                        await e.client.send_message(e.chat_id, caption, parse_mode='html')
                    except FloodWaitError as err:
                        await asyncio.sleep(err.seconds)
                    await asyncio.sleep(get_delay(e.chat_id, 0.1))
        except (IndexError, ValueError, NameError):
            await e.reply(f"```{hl}ʟᴏᴠᴇʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>```")
        except Exception as err:
            logger.error(f"Error in loveraid: {err}")

@on_cmd("sraid")
async def sraid(e):
     if e.sender_id in SUDO_USERS:
        xraid = e.text.split(" ", 2)
        try:
            if len(xraid) == 3:
                entity = await e.client.get_entity(xraid[2])
                uid = entity.id
            elif e.reply_to_msg_id:             
                a = await e.get_reply_message()
                entity = await e.client.get_entity(a.sender_id)
                uid = entity.id
            else:
                await e.reply(f"```{hl}ꜱʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ> <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>```")
                return

            if await check_protection(e, uid):
                return
            if uid in DEV:
                await e.reply("<blockquote><b>» ɴᴏᴘᴇ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ʙᴏᴛ ᴏᴡɴᴇʀ ❌</b></blockquote>", parse_mode="html")
            elif uid == OWNER_ID:
                await e.reply("<blockquote><b>» ɴᴏᴘᴇ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ ❌</b></blockquote>", parse_mode="html")
            elif uid in SUDO_USERS:
                await e.reply("<blockquote><b>» ɴᴏᴘᴇ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ꜱᴜᴅᴏ ᴜꜱᴇʀ ❌</b></blockquote>", parse_mode="html")
            else:
                first_name = entity.first_name
                counter = int(xraid[1])
                username = f"<a href='tg://user?id={uid}'>{first_name}</a>"
                for _ in range(counter):
                    reply = choice(SRAID)
                    caption = f"<blockquote><b>{username} {reply}</b></blockquote>"
                    try:
                        await e.client.send_message(e.chat_id, caption, parse_mode='html')
                    except FloodWaitError as err:
                        await asyncio.sleep(err.seconds)
                    await asyncio.sleep(get_delay(e.chat_id, 0.1))
        except (IndexError, ValueError, NameError):
            await e.reply(f"```{hl}ꜱʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ> <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>```")
        except Exception as err:
            logger.error(f"Error in sraid: {err}")
