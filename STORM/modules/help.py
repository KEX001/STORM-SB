from telethon import Button
import config
from config import CMD_HNDLR as hl
from STORM.client_manager import on_cmd, on_callback
import asyncio
import random

class EventCoordinator:
    def __init__(self):
        self._receivers = {}
        self._chosen = {}
        self._lock = asyncio.Lock()

    async def resolve_responder(self, event_key: str, client_id: int) -> bool:
        async with self._lock:
            if event_key not in self._receivers:
                self._receivers[event_key] = []
            if client_id not in self._receivers[event_key]:
                self._receivers[event_key].append(client_id)
        await asyncio.sleep(0.08)
        async with self._lock:
            if event_key not in self._chosen:
                self._chosen[event_key] = random.choice(self._receivers[event_key])
                async def _sweep():
                    await asyncio.sleep(5.0)
                    async with self._lock:
                        self._receivers.pop(event_key, None)
                        self._chosen.pop(event_key, None)
                asyncio.create_task(_sweep())
            return self._chosen[event_key] == client_id

coordinator = EventCoordinator()

HELP_STRING = f"""
<blockquote><b>❏ ʜ ᴇ ʟ ᴘ   ᴍ ᴇ ɴ ᴜ</b>
<b>├• ꜱʏꜱᴛᴇᴍ:</b> ꜱʏᴘʜɪx ꜱᴘᴀᴍ ʙᴏᴛ
<b>├• ᴠᴇʀꜱɪᴏɴ:</b> <code>{config.VERSION}</code>
<b>├• ᴄʜᴀɴɴᴇʟ:</b> <a href='https://t.me/Syphixlabs'>ꜱʏᴘʜɪx ʟᴀʙꜱ</a>
<b>└• ꜱᴜᴘᴘᴏʀᴛ:</b> <a href='https://t.me/SyphixHub'>ꜱʏᴘʜɪx ʜᴜʙ</a></blockquote>
<blockquote>» <i>ꜱᴇʟᴇᴄᴛ ᴀ ᴄᴀᴛᴇɢᴏʀʏ ʙᴇʟᴏᴡ ᴛᴏ ᴠɪᴇᴡ ᴄᴏᴍᴍᴀɴᴅꜱ.</i></blockquote>
"""

HELP_BUTTON = [
    [
      Button.inline("• ꜱᴘᴀᴍ •", data="spam"),
      Button.inline("• ʀᴀɪᴅ •", data="raid")
    ],
    [
      Button.inline("• ᴏᴡɴᴇʀ •", data="owner")
    ],
    [
      Button.url("• ꜱᴜᴘᴘᴏʀᴛ •", "https://t.me/SyphixHub")
    ]
]

@on_cmd("help")
async def help(event):
    if event.sender_id in config.SUDO_USERS:
        event_key = f"{event.chat_id}_{event.id}"
        my_id = getattr(event.client, "me_id", None)
        if my_id is None:
            try:
                me = await event.client.get_me()
                my_id = me.id
            except Exception:
                return
        if not await coordinator.resolve_responder(event_key, my_id):
            return

        try:
          await event.client.send_file(event.chat_id,
              "https://envs.sh/Pa1.mp4",
              caption=HELP_STRING,
              parse_mode='html',
              buttons=HELP_BUTTON
              )
        except Exception as e:
            try:
                await event.client.send_message(event.chat_id, f"<blockquote><b>❏ ʜ ᴇ ʟ ᴘ   ᴍ ᴇ ɴ ᴜ</b>\n» <b>ᴇxᴄᴇᴘᴛɪᴏɴ ᴏᴄᴄᴜʀʀᴇᴅ:</b> <code>{e}</code></blockquote>", parse_mode='html')
            except Exception:
                pass

owner_msg = f"""
<blockquote><b>❏ ᴏᴡɴᴇʀ ᴄᴏᴍᴍᴀɴᴅꜱ</b></blockquote>
<blockquote> • ᴄʜᴇᴄᴋ ᴘɪɴɢ: <code>{hl}ping</code>
 • ʟᴇᴀᴠᴇ ᴄʜᴀᴛ: <code>{hl}leave</code>

 • ᴍᴀɴᴀɢᴇ ꜱᴜᴅᴏ
 ᴜꜱᴀɢᴇ : <code>{hl}addsudo <ʀᴇᴘʟʏ></code> / <code>{hl}sudolist</code>
 
 • ᴍᴀɴᴀɢᴇ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ
 ᴜꜱᴀɢᴇ : <code>{hl}protect <ʀᴇᴘʟʏ/ɪᴅ></code> / <code>{hl}unprotect <ʀᴇᴘʟʏ/ɪᴅ></code>
 
 • ʀᴇꜱᴛᴀʀᴛ ʙᴏᴛ
 ᴜꜱᴀɢᴇ : <code>{hl}restart</code></blockquote>
"""      
          
raid_msg = f"""
<blockquote><b>❏ ʀᴀɪᴅ ᴄᴏᴍᴍᴀɴᴅꜱ</b></blockquote>
<blockquote> • ꜱᴛᴀʀᴛ ʀᴀɪᴅ
 ᴜꜱᴀɢᴇ : <code>{hl}raid <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ></code>
 
 • ᴀʙᴜꜱᴇ ʀᴀɪᴅ
 ᴜꜱᴀɢᴇ : <code>{hl}abuse <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ></code>
 
 • ʀᴇᴘʟʏ ʀᴀɪᴅ
 ᴜꜱᴀɢᴇ : <code>{hl}rraid <ᴜꜱᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ></code> / <code>{hl}drraid <ᴜꜱᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ></code>
 
 • ʟᴏᴠᴇ ʀᴀɪᴅ
 ᴜꜱᴀɢᴇ : <code>{hl}loveraid <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ></code>
 
 • ꜰʟɪʀᴛ ʀᴀɪᴅ
 ᴜꜱᴀɢᴇ : <code>{hl}flirt <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ></code>
 
 • ꜱʜᴀʏᴀʀɪ ʀᴀɪᴅ
 ᴜꜱᴀɢᴇ : <code>{hl}sraid <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ></code></blockquote>
"""

spam_msg = f"""
<blockquote><b>❏ ꜱᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅꜱ</b></blockquote>
<blockquote> • ꜱᴘᴀᴍ ᴍᴇꜱꜱᴀɢᴇ
 ᴜꜱᴀɢᴇ : <code>{hl}spam <ᴄᴏᴜɴᴛ> <ᴛᴇxᴛ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ></code>
 
 • ᴘᴏʀɴᴏɢʀᴀᴘʜʏ ꜱᴘᴀᴍ
 ᴜꜱᴀɢᴇ : <code>{hl}pspam <ᴄᴏᴜɴᴛ></code>
 
 • ʙɪʀᴛʜᴅᴀʏ ꜱᴘᴀᴍ
 ᴜꜱᴀɢᴇ : <code>{hl}bspam <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ></code>
 
 • ᴇᴍᴏᴊɪ ꜱᴘᴀᴍ
 ᴜꜱᴀɢᴇ : <code>{hl}emoji <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ></code>
 
 • ʜᴀɴɢ ꜱᴘᴀᴍ
 ᴜꜱᴀɢᴇ : <code>{hl}hang <ᴄᴏᴜɴᴛ></code>
 
 • ᴇᴄʜᴏ ᴜꜱᴇʀ
 ᴜꜱᴀɢᴇ : <code>{hl}echo <ʀᴇᴘʟʏ></code> / <code>{hl}rmecho <ʀᴇᴘʟʏ></code></blockquote>
"""                                
           
@on_callback(pattern=r"help_back")
async def helpback(event):
    if event.query.user_id in config.SUDO_USERS:    
        try:
            await event.edit(
                HELP_STRING,
                parse_mode='html',
                buttons=HELP_BUTTON
              )
        except Exception:
            pass
    else:
        try:
            await event.answer("ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴛᴏ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ.", cache_time=0, alert=True)
        except Exception:
            pass


@on_callback(pattern=r"spam")
async def help_spam(event):
    if event.query.user_id in config.SUDO_USERS:    
        try:
            await event.edit(spam_msg,
                  parse_mode='html',
                  buttons=[[Button.inline("🔙 ʙᴀᴄᴋ", data="help_back"),],],
                  ) 
        except Exception:
            pass
    else:
        try:
            await event.answer("ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴛᴏ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ.", cache_time=0, alert=True)
        except Exception:
            pass


@on_callback(pattern=r"raid")
async def help_raid(event):
    if event.query.user_id in config.SUDO_USERS:
        try:
            await event.edit(raid_msg,
                 parse_mode='html',
                 buttons=[[Button.inline("🔙 ʙᴀᴄᴋ", data="help_back"),],],
               )
        except Exception:
            pass
    else:
        try:
            await event.answer("ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴛᴏ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ.", cache_time=0, alert=True)
        except Exception:
            pass




@on_callback(pattern=r"owner")
async def help_owner(event):
    if event.query.user_id in config.SUDO_USERS:
        try:
            await event.edit(owner_msg,
                parse_mode='html',
                buttons=[[Button.inline("🔙 ʙᴀᴄᴋ", data="help_back"),],],
                )
        except Exception:
            pass
    else:
        try:
            await event.answer("ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴛᴏ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ.", cache_time=0, alert=True)
        except Exception:
            pass
