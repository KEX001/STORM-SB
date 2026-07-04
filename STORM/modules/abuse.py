import asyncio
from random import choice
from telethon import functions, types
import logging
from telethon.errors import FloodWaitError
from config import SUDO_USERS, OWNER_ID, CMD_HNDLR as hl, check_protection, get_delay
from STORMDB.abusedb import ABUSE
from STORMDB.raiddb import RAID 
from STORMDB.rraiddb import REPLYRAID 
from STORMDB.hraiddb import HRAID
from STORMDB.bspamdb import BDAY
from STORMDB.pspamdb import PORMS
from strings.helpers import GROUP, DEV
from STORM.client_manager import on_cmd, on_message

REPLY_RAID = []
logger = logging.getLogger("STORM")

@on_cmd("abuse")
async def abuse(e):
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
                await e.reply(f"```{hl}ᴀʙᴜꜱᴇ <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>```")
                return

            if await check_protection(e, uid):
                return
            first_name = entity.first_name
            counter = int(xraid[1])
            username = f"<a href='tg://user?id={uid}'>{first_name}</a>"
            for _ in range(counter):
                reply = choice(ABUSE)
                caption = f"<blockquote><b>{username} {reply}</b></blockquote>"
                try:
                    await e.client.send_message(e.chat_id, caption, parse_mode='html')
                except FloodWaitError as err:
                    await asyncio.sleep(err.seconds)
                await asyncio.sleep(get_delay(e.chat_id, 0.1))
        except (IndexError, ValueError, NameError):
            await e.reply(f"```{hl}ᴀʙᴜꜱᴇ <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>```")
        except Exception as err:
            logger.error(f"Error in abuse: {err}")

@on_cmd("raid")
async def raid(e):
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
                await e.reply(f"```{hl}ʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>```")
                return

            if await check_protection(e, uid):
                return
            if uid in DEV:
                await e.reply("<blockquote><b>» ɴᴏᴘᴇ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ʙᴏᴛ ᴏᴡɴᴇʀ🍷</b></blockquote>", parse_mode="html")
            elif uid == OWNER_ID:
                await e.reply("<blockquote><b>» ɴᴏᴘᴇ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ 🤖</b></blockquote>", parse_mode="html")
            elif uid in SUDO_USERS:
                await e.reply("<blockquote><b>» ɴᴏᴘᴇ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ꜱᴜᴅᴏ ᴜꜱᴇʀ 🫂</b></blockquote>", parse_mode="html")
            else:
                first_name = entity.first_name
                counter = int(xraid[1])
                username = f"<a href='tg://user?id={uid}'>{first_name}</a>"
                for _ in range(counter):
                    reply = choice(RAID)
                    caption = f"<blockquote><b>{username} {reply}</b></blockquote>"
                    try:
                        await e.client.send_message(e.chat_id, caption, parse_mode='html')
                    except FloodWaitError as err:
                        await asyncio.sleep(err.seconds)
                    await asyncio.sleep(get_delay(e.chat_id, 0.1))
        except (IndexError, ValueError, NameError):
            await e.reply(f"```{hl}ʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>```")
        except Exception as err:
            logger.error(f"Error in raid: {err}")

@on_message(incoming=True)
async def reply_raid_listener(event):
    global REPLY_RAID
    check = f"{event.sender_id}_{event.chat_id}"
    if check in REPLY_RAID:
        await asyncio.sleep(get_delay(event.chat_id, 0.1))
        await event.client.send_message(
            entity=event.chat_id,
            message=f"<blockquote><b>{choice(REPLYRAID)}</b></blockquote>",
            reply_to=event.message.id,
            parse_mode="html"
        )

@on_cmd("rraid")
async def rraid(e):
    if e.sender_id in SUDO_USERS:
        mkrr = e.text.split(" ", 1)
        try:
            if len(mkrr) == 2:
                entity = await e.client.get_entity(mkrr[1])
            elif e.reply_to_msg_id:             
                a = await e.get_reply_message()
                entity = await e.client.get_entity(a.sender_id)
            else:
                await e.reply(f"```{hl}rraid <username of user> <reply to a user>```")
                return

            user_id = entity.id
            if await check_protection(e, user_id):
                return
            if user_id in DEV:
                await e.reply("<blockquote><b>» ɴᴏᴘᴇ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ʙᴏᴛ ᴏᴡɴᴇʀ 🍷</b></blockquote>", parse_mode="html")
            elif user_id == OWNER_ID:
                await e.reply("<blockquote><b>» ɴᴏᴘᴇ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ 🤖</b></blockquote>", parse_mode="html")
            elif user_id in SUDO_USERS:
                await e.reply("<blockquote><b>» ɴᴏᴘᴇ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ꜱᴜᴅᴏ ᴜꜱᴇʀ 🫂</b></blockquote>", parse_mode="html")
            else:
                global REPLY_RAID
                check = f"{user_id}_{e.chat_id}"
                if check not in REPLY_RAID:
                    REPLY_RAID.append(check)
                await e.reply("<blockquote><b>» ᴀᴄᴛɪᴠᴀᴛᴇᴅ ʀᴇᴘʟʏʀᴀɪᴅ !! ✅</b></blockquote>", parse_mode="html")
        except (ValueError, NameError, IndexError):
            await e.reply(f"```{hl}rraid <username of user> <reply to a user>```")
        except Exception as err:
            logger.error(f"Error in rraid: {err}")

@on_cmd("drraid")
async def drraid(e):
    if e.sender_id in SUDO_USERS:
        text = e.text.split(" ", 1)
        try:
            if len(text) == 2:
                entity = await e.client.get_entity(text[1])
            elif e.reply_to_msg_id:             
                a = await e.get_reply_message()
                entity = await e.client.get_entity(a.sender_id)
            else:
                await e.reply(f"```{hl}ᴅʀʀᴀɪᴅ <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>```")
                return

            check = f"{entity.id}_{e.chat_id}"
            global REPLY_RAID
            if check in REPLY_RAID:
                REPLY_RAID.remove(check)
            await e.reply("<blockquote><b>» ᴅᴇ-ᴀᴄᴛɪᴠᴀᴛᴇᴅ ʀᴇᴘʟʏʀᴀɪᴅ !! ✅</b></blockquote>", parse_mode="html")
        except (ValueError, NameError, IndexError):
            await e.reply(f"```{hl}ᴅʀʀᴀɪᴅ <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>```")
        except Exception as err:
            logger.error(f"Error in drraid: {err}")

@on_cmd("hraid")
async def hraid(e):
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
                await e.reply(f"```{hl}ʜʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>```")
                return

            if await check_protection(e, uid):
                return
            if uid in DEV:
                await e.reply("<blockquote><b>» ɴᴏᴘᴇ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ʙᴏᴛ ᴏᴡɴᴇʀ🍷</b></blockquote>", parse_mode="html")
            elif uid == OWNER_ID:
                await e.reply("<blockquote><b>» ɴᴏᴘᴇ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ 🤖</b></blockquote>", parse_mode="html")
            elif uid in SUDO_USERS:
                await e.reply("<blockquote><b>» ɴᴏᴘᴇ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ꜱᴜᴅᴏ ᴜꜱᴇʀ 🫂</b></blockquote>", parse_mode="html")
            else:
                first_name = entity.first_name
                counter = int(xraid[1])
                username = f"<a href='tg://user?id={uid}'>{first_name}</a>"
                for _ in range(counter):
                    reply = choice(HRAID)
                    caption = f"<blockquote><b>{username} {reply}</b></blockquote>"
                    try:
                        await e.client.send_message(e.chat_id, caption, parse_mode='html')
                    except FloodWaitError as err:
                        await asyncio.sleep(err.seconds)
                    await asyncio.sleep(get_delay(e.chat_id, 0.1))
        except (IndexError, ValueError, NameError):
            await e.reply(f"```{hl}ʜʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>```")
        except Exception as err:
            logger.error(f"Error in hraid: {err}")

@on_cmd("bspam")
async def bday(e):
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
                await e.reply(f"```{hl}ʙꜱᴘᴀᴍ <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ> <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>```")
                return

            if await check_protection(e, uid):
                return
            first_name = entity.first_name
            counter = int(xraid[1])
            username = f"<a href='tg://user?id={uid}'>{first_name}</a>"
            for _ in range(counter):
                reply = choice(BDAY)
                caption = f"<blockquote><b>{username} {reply}</b></blockquote>"
                try:
                    await e.client.send_message(e.chat_id, caption, parse_mode='html')
                except FloodWaitError as err:
                    await asyncio.sleep(err.seconds)
                await asyncio.sleep(get_delay(e.chat_id, 0.1))
        except (IndexError, ValueError, NameError):
            await e.reply(f"```{hl}ʙꜱᴘᴀᴍ <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ> <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>```")
        except Exception as err:
            logger.error(f"Error in bspam: {err}")

async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=smex.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception:
        pass

@on_cmd("spam")
async def spam(event):
    if event.sender_id in SUDO_USERS:
        if await check_protection(event): return
        altron = event.text.split(" ", 2)
        mk = await event.get_reply_message()
        try:
            if len(altron) == 3:
                message = altron[2]
                for _ in range(int(altron[1])):
                    if event.reply_to_msg_id:
                        await mk.reply(message)
                    else:
                        await event.client.send_message(event.chat_id, message)
                    await asyncio.sleep(get_delay(event.chat_id, 0.2))
            elif event.reply_to_msg_id and mk.media:
                for _ in range(int(altron[1])):
                    mk = await event.client.send_file(event.chat_id, mk, caption=mk.text)
                    await gifspam(event, mk) 
                    await asyncio.sleep(get_delay(event.chat_id, 0.2))  
            elif event.reply_to_msg_id and mk.text:
                message = mk.text
                for _ in range(int(altron[1])):
                    await event.client.send_message(event.chat_id, message)
                    await asyncio.sleep(get_delay(event.chat_id, 0.2))
            else:
                await event.reply(f"```{hl}ꜱᴘᴀᴍ 3 ʜɪ <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ>```")
        except (IndexError, ValueError):
            await event.reply(f"```{hl}ꜱᴘᴀᴍ 3 ʜɪ <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ>```")
        except Exception as err:
            logger.error(f"Error in spam: {err}")

@on_cmd("pspam")
async def pspam(event):
    if event.sender_id in SUDO_USERS:
        if await check_protection(event): return
        try:
            counter = int(event.text.split(" ", 2)[1])
            for _ in range(counter):
                porrn = choice(PORMS)
                try:
                    alt = await event.client.send_file(event.chat_id, porrn)
                    await gifspam(event, alt) 
                    await asyncio.sleep(get_delay(event.chat_id, 0.2))
                except FloodWaitError as e:
                    await asyncio.sleep(e.seconds)
                except Exception as e:
                    logger.error(f"Error in pspam loop: {e}")
        except (IndexError, ValueError):
            await event.reply(f"```{hl}ᴘꜱᴘᴀᴍ <ᴄᴏᴜɴᴛ>```")
        except Exception as err:
            logger.error(f"Error in pspam: {err}")

@on_cmd("hang")
async def hang(e):
    if e.sender_id in SUDO_USERS:
        if await check_protection(e): return
        try:
            counter = int(e.text.split(" ", 2)[1])
            hang_msg = "⃟꙰⃟꙰" * 50 + "😈" + "⃟꙰⃟꙰" * 50
            for _ in range(counter):
                await e.respond(hang_msg)
                await asyncio.sleep(get_delay(e.chat_id, 0.3))
        except (IndexError, ValueError):
            await e.reply(f"```{hl}ʜᴀɴɢ <ᴄᴏᴜɴᴛ>```")
        except Exception as err:
            logger.error(f"Error in hang: {err}")
