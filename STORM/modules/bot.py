from telethon import __version__, Button
import asyncio
import sys
import heroku3
from time import time
from datetime import datetime
from config import OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, CMD_HNDLR as hl, start_time, VERSION, PROTECTED_USERS, PROTECTED_GROUPS
from telethon.tl.functions.channels import LeaveChannelRequest
import os
from STORM.client_manager import on_cmd, CLIENTS
import random
from telethon.tl.functions import PingRequest

PIC = "https://graph.org/file/c3b279aee41f8bbe6466b.jpg"

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

async def measure_latency(client) -> float:
    try:
        t_start = datetime.now()
        await client(PingRequest(ping_id=random.getrandbits(31)))
        return (datetime.now() - t_start).total_seconds() * 1000.0
    except (Exception, asyncio.CancelledError):
        return None

async def resolve_user_id(event) -> int:
    parts = event.text.split()
    if len(parts) > 1:
        param = parts[1]
        try:
            arg = int(param) if param.isdigit() or (param.startswith('-') and param[1:].isdigit()) else param
            entity = await event.client.get_entity(arg)
            return entity.id
        except Exception as e:
            raise ValueError(f"Failed resolving target identifier: {e}")
    elif event.reply_to_msg_id:
        try:
            reply = await event.get_reply_message()
            return reply.sender_id
        except Exception as e:
            raise ValueError(f"Failed fetching message reply source: {e}")
    else:
        raise ValueError("Insufficient command arguments: target user identifier or reply target required.")

def update_env_sudo(target_id: int) -> bool:
    from pathlib import Path
    env_file = Path(".env")
    target_str = str(target_id)
    try:
        content = env_file.read_text() if env_file.exists() else ""
        lines = content.splitlines()
        updated = False
        for i, line in enumerate(lines):
            if line.startswith("SUDO_USERS="):
                current_users = line.split("=", 1)[1].strip().strip('"').strip("'").split()
                new_users = list(dict.fromkeys(current_users + [target_str]))
                lines[i] = f'SUDO_USERS="{" ".join(new_users)}"'
                updated = True
                break
        if not updated:
            lines.append(f'SUDO_USERS="{target_str}"')
        env_file.write_text("\n".join(lines) + "\n")
        return True
    except Exception:
        return False

def get_readable_time(seconds: int) -> str:
    periods = [('days', 86400), ('h', 3600), ('m', 60), ('s', 1)]
    parts = []
    for name, count in periods:
        value, seconds = divmod(seconds, count)
        if value:
            parts.append(f"{value}{name}")
    return ":".join(parts) if parts else "0s"

@on_cmd("alive")
async def alive(event):
    if event.sender_id in SUDO_USERS:
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
            
        uptime_str = get_readable_time(int(time() - start_time))
        owner_name = str(OWNER_ID)
        try:
            owner_entity = await event.client.get_entity(OWNER_ID)
            owner_name = owner_entity.first_name
        except Exception:
            pass

        text = (
            "<blockquote><b>❏ ꜱ ᴛ ᴏ ʀ ᴍ</b>\n"
            f"<b>├• ᴘʏᴛʜᴏɴ:</b> <code>{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}</code>\n"
            f"<b>├• ᴛᴇʟᴇᴛʜᴏɴ:</b> <code>{__version__}</code>\n"
            f"<b>├• ᴜᴘᴛɪᴍᴇ:</b> <code>{uptime_str}</code>\n"
            f"<b>├• ᴠᴇʀꜱɪᴏɴ:</b> <code>{VERSION}</code>\n"
            f"<b>├• ᴏᴡɴᴇʀ:</b> <a href='tg://user?id={OWNER_ID}'>{owner_name}</a>\n"
            "<b>└• ᴘᴏᴡᴇʀᴇᴅ ʙʏ:</b> <code>Ɵᴘᴜs 🤖</code>"
            "</blockquote>"
        )
        await event.client.send_file(
            event.chat_id,
            "https://envs.sh/Pa1.mp4",
            caption=text,
            parse_mode='html',
            buttons=[
                [
                    Button.url("• ʜᴜʙ •", "https://t.me/SyphixHub"),
                    Button.url("• ʟᴀʙꜱ •", "https://t.me/Syphixlabs")
                ],
            ]
        )

@on_cmd("logs")
async def logs(KEX):
    if KEX.sender_id == OWNER_ID:
        event_key = f"{KEX.chat_id}_{KEX.id}"
        my_id = getattr(KEX.client, "me_id", None)
        if my_id is None:
            try:
                me = await KEX.client.get_me()
                my_id = me.id
            except Exception:
                return
        if not await coordinator.resolve_responder(event_key, my_id):
            return

        fetch = await KEX.reply("<blockquote><b>❏ ꜱ ᴛ ᴏ ʀ ᴍ   ʟᴏɢꜱ</b>\n» ꜰᴇᴛᴄʜʜɪɴɢ ʟᴏɢꜱ ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ 📄...</blockquote>", parse_mode='html')
        if HEROKU_APP_NAME and HEROKU_API_KEY:
            try:
                Heroku = heroku3.from_key(HEROKU_API_KEY)
                app = Heroku.app(HEROKU_APP_NAME)
                logs_text = app.get_log()
                with open("Logs.txt", "w") as f:
                    f.write("ꜱᴛᴏʀᴍ 𝚇 🍷 [ Heroku Logs ]\n\n" + logs_text)
            except Exception as e:
                await fetch.edit(f"<blockquote><b>❏ ꜱ ᴛ ᴏ ʀ ᴍ   ʟᴏɢꜱ</b>\n» <b>ʜᴇʀᴏᴋᴜ ᴀᴘɪ ᴇʀʀᴏʀ:</b> <code>{e}</code></blockquote>", parse_mode='html')
                return
        else:
            local_log_path = "main.log"
            if os.path.exists(local_log_path):
                try:
                    with open(local_log_path, "r", encoding="utf-8", errors="ignore") as f:
                        lines = f.readlines()
                    tail_lines = lines[-1000:]
                    with open("Logs.txt", "w", encoding="utf-8") as f:
                        f.write("ꜱᴛᴏʀᴍ 𝚇 🍷 [ VPS/Local Logs ]\n\n" + "".join(tail_lines))
                except Exception as e:
                    await fetch.edit(f"<blockquote><b>❏ ꜱ ᴛ ᴏ ʀ ᴍ   ʟᴏɢꜱ</b>\n» <b>ʟᴏᴄᴀʟ ʟᴏɢ ʀᴇᴀᴅ ᴇʀʀᴏʀ:</b> <code>{e}</code></blockquote>", parse_mode='html')
                    return
            else:
                await fetch.edit("<blockquote><b>❏ ꜱ ᴛ ᴏ ʀ ᴍ   ʟᴏɢꜱ</b>\n» <b>ɴᴏ ʟᴏᴄᴀʟ ʟᴏɢ ꜰɪʟᴇ (ᴍᴀɪɴ.ʟᴏɢ) ᴏʀ ʜᴇʀᴏᴋᴜ ᴄᴏɴꜰɪɢᴜʀᴀᴛɪᴏɴ ꜰᴏᴜɴᴅ!</b></blockquote>", parse_mode='html')
                return

        try:
            await KEX.client.send_file(
                KEX.chat_id, 
                "Logs.txt", 
                caption=f"⚡ <b>ꜱᴛᴏʀᴍ ʙᴏᴛ ʟᴏɢꜱ 🍷</b> ⚡\n  » <b>ᴅᴇᴘʟᴏʏᴍᴇɴᴛ:</b> <code>" + ("ʜᴇʀᴏᴋᴜ ☁️" if HEROKU_APP_NAME and HEROKU_API_KEY else "ᴠᴘꜱ/ʀᴇɴᴅᴇʀ 🖥️") + "</code>",
                parse_mode='html'
            )
            await fetch.delete()
        except Exception as e:
            await fetch.edit(f"<blockquote><b>❏ ꜱ ᴛ ᴏ ʀ ᴍ   ʟᴏɢꜱ</b>\n» <b>ꜰᴀɪʟᴇᴅ ᴛᴏ ꜱᴇɴᴅ ʟᴏɢꜱ:</b> <code>{e}</code></blockquote>", parse_mode='html')
        finally:
            if os.path.exists("Logs.txt"):
                os.remove("Logs.txt")

    elif KEX.sender_id in SUDO_USERS:
        await KEX.reply("<blockquote><b>❏ ꜱ ᴛ ᴏ ʀ ᴍ   ʟᴏɢꜱ</b>\n» ɴᴏᴘᴇ, ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ 🤖</blockquote>", parse_mode='html')

@on_cmd("leave")
async def leave(e):
    if e.sender_id in SUDO_USERS:
        if len(e.text) > 7:
            event = await e.reply("<blockquote><b>» ʟᴇᴀᴠɪɴɢ ⌛...</b></blockquote>", parse_mode='html')
            mkl = e.text.split(" ", 1)
            try:
                await event.client(LeaveChannelRequest(int(mkl[1])))
            except Exception as e:
                await event.edit(f"<blockquote><b>» ᴇʀʀᴏʀ:</b> <code>{str(e)}</code></blockquote>", parse_mode='html')
        else:
             if e.is_private:
                  alt = f"<blockquote><b>» ʏᴏᴜ ᴄᴀɴ'ᴛ ᴅᴏ ᴛʜɪꜱ ʜᴇʀᴇ !!</b>\n\n» <code>{hl}ʟᴇᴀᴠᴇ</code> : ᴛʏᴘᴇ ᴛʜɪꜱ ɪɴ ɢʀᴏᴜᴘ</blockquote>"
                  await e.reply(alt, parse_mode='html')
             else:
                  event = await e.reply("<blockquote><b>» ʟᴇᴀᴠɪɴɢ ⌛...</b></blockquote>", parse_mode='html')
                  try:
                      await event.client(LeaveChannelRequest(int(e.chat_id)))
                  except Exception as e:
                      await event.edit(f"<blockquote><b>» ᴇʀʀᴏʀ:</b> <code>{str(e)}</code></blockquote>", parse_mode='html')        

@on_cmd("ping")
async def ping(e):
    if e.sender_id in SUDO_USERS:
        event_key = f"{e.chat_id}_{e.id}"
        my_id = getattr(e.client, "me_id", None)
        if my_id is None:
            try:
                me = await e.client.get_me()
                my_id = me.id
            except Exception:
                return

        if not await coordinator.resolve_responder(event_key, my_id):
            return
            
        KEX = await e.reply("🌩")
        uptime_str = get_readable_time(int(time() - start_time))
        
        owner_name = str(OWNER_ID)
        try:
            owner_entity = await e.client.get_entity(OWNER_ID)
            owner_name = owner_entity.first_name
        except Exception:
            pass

        latencies = await asyncio.gather(*(measure_latency(c) for c in CLIENTS))
        valid_latencies = [l for l in latencies if l is not None]
        
        if valid_latencies:
            avg_ping = round(sum(valid_latencies) / len(valid_latencies), 2)
            ping_display = f"{avg_ping} ᴍꜱ"
        else:
            ping_display = "Error"

        await KEX.edit(f"""
<blockquote><b>❏ ꜱ ᴛ ᴏ ʀ ᴍ </b>
<b>├• ꜱᴛᴀᴛᴜꜱ:</b> <code>ᴀᴄᴛɪᴠᴇ</code>
<b>├• ʀᴇꜱᴘᴏɴꜱᴇ ᴛɪᴍᴇ:</b> <code>{ping_display}</code>
<b>├• ᴜᴘᴛɪᴍᴇ:</b> <code>{uptime_str}</code>
<b>├• ᴏᴡɴᴇʀ:</b> <a href="tg://user?id={OWNER_ID}">{owner_name}</a>
<b>├• ᴠᴇʀꜱɪᴏɴ:</b> <code>{VERSION}</code>
<b>└• ᴘᴏᴡᴇʀᴇᴅ ʙʏ:</b> <code>Ɵᴘᴜs 🤖</code>
</blockquote>
""", parse_mode='html') 

@on_cmd("(?:add)?sudo")
async def addsudo(event):
    if event.sender_id == OWNER_ID:
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

        ok = await event.reply("<blockquote><b>❏ ꜱ ᴛ ᴏ ʀ ᴍ   ꜱᴜᴅᴏ</b>\n» ᴘʀᴏᴄᴇꜱ𝖘ɪɴɢ... ᴜꜱᴇʀ ᴀꜱ ꜱᴜᴅᴏ...</blockquote>", parse_mode='html')
        try:
            target = await resolve_user_id(event)
        except Exception as e:
            await ok.edit(f"<blockquote><b>❏ ꜱ ᴛ ᴏ ʀ ᴍ   ꜱᴜᴅᴏ</b>\n» <b>ᴇʀʀᴏʀ:</b> <code>{e}</code></blockquote>", parse_mode='html')
            return

        if HEROKU_APP_NAME is not None and HEROKU_API_KEY is not None:
            try:
                Heroku = heroku3.from_key(HEROKU_API_KEY)
                app = Heroku.app(HEROKU_APP_NAME)
                heroku_var = app.config()
                sudousers = getenv("SUDO_USERS", default="")
                if str(target) in sudousers:
                    await ok.edit("<blockquote><b>❏ ꜱ ᴛ ᴏ ʀ ᴍ   ꜱᴜᴅᴏ</b>\n» ᴛʜɪꜱ ᴜꜱᴇʀ ɪꜱ ᴀʟʀᴇᴀᴅʏ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ !!</blockquote>", parse_mode='html')
                else:
                    newsudo = f"{sudousers} {target}" if len(sudousers) > 0 else f"{target}"
                    if target not in SUDO_USERS:
                        SUDO_USERS.append(target)
                    await ok.edit(f"<blockquote><b>❏ ꜱ ᴛ ᴏ ʀ ᴍ   <b>ꜱᴜᴅᴏ</b></b>\n» <b>ɴᴇᴡ ꜱᴜᴅᴏ:</b> <code>{target}</code> ᴀᴅᴅᴇᴅ ᴅʏɴᴀᴍɪᴄᴀʟʟʏ! 🚀\n» ʀᴇꜱᴛᴀʀᴛɪɴɢ ʜᴇʀᴏᴋᴜ ᴀᴘᴘ ᴅʏɴᴏ...</blockquote>", parse_mode='html')
                    heroku_var["SUDO_USERS"] = newsudo
            except Exception as e:
                await ok.edit(f"<blockquote><b>❏ ꜱ ᴛ ᴏ ʀ ᴍ   ꜱᴜᴅᴏ</b>\n» <b>ʜᴇʀᴏᴋᴜ ᴇʀʀᴏʀ:</b> <code>{e}</code></blockquote>", parse_mode='html')
        else:
            if target in SUDO_USERS:
                await ok.edit("<blockquote><b>❏ ꜱ ᴛ ᴏ ʀ ᴍ   ꜱᴜᴅᴏ</b>\n» ᴛʜɪꜱ ᴜꜱᴇʀ ɪꜱ ᴀʟʀᴇᴀᴅʏ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ !!</blockquote>", parse_mode='html')
            else:
                SUDO_USERS.append(target)
                if update_env_sudo(target):
                    await ok.edit(f"<blockquote><b>❏ ꜱ ᴛ ᴏ ʀ ᴍ   ꜱᴜᴅᴏ</b>\n» <b>ɴᴇᴡ ꜱᴜᴅᴏ:</b> <code>{target}</code> ᴀᴅᴅᴇᴅ ᴅʏɴᴀᴍɪᴄᴀʟʟʏ! 🚀</blockquote>", parse_mode='html')
                else:
                    await ok.edit("<blockquote><b>❏ ꜱ ᴛ ᴏ ʀ ᴍ   ꜱᴜᴅᴏ</b>\n» <b>ꜰᴀɪʟᴇᴅ ᴜᴘᴅᴀᴛɪɴɢ ʟᴏᴄᴀʟ ᴄᴏɴꜰɪɢ ᴇɴᴠɪʀᴏɴᴍᴇɴᴛ ꜱᴛᴏʀᴀɢᴇ.</b></blockquote>", parse_mode='html')
    elif event.sender_id in SUDO_USERS:
        await event.reply("<blockquote><b>❏ ꜱ ᴛ ᴏ ʀ ᴍ   ꜱᴜᴅᴏ</b>\n» ꜱᴏʀʀʏ, ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴀᴄᴄᴇꜱṣ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.</blockquote>", parse_mode='html')

@on_cmd("sudolist")
async def sudolist(event):
    if event.sender_id in SUDO_USERS:
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

        import config
        ok = await event.reply("<blockquote><b>❏ ꜱ ᴛ ᴏ ʀ ᴍ   ꜱᴜᴅᴏꜱ</b>\n» ꜰᴇᴛᴄʜʜɪɴɢ ꜱᴜᴅᴏ ʟɪꜱᴛ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...</blockquote>", parse_mode='html')
        msg = "<blockquote><b>❏ ꜱ ᴛ ᴏ ʀ ᴍ   ꜱ ᴜ ᴅ ᴏ ꜱ</b>\n"
        total = len(config.SUDO_USERS)
        for i, user_id in enumerate(config.SUDO_USERS, start=1):
            name = "User"
            try:
                entity = await event.client.get_entity(user_id)
                name = entity.first_name
            except Exception:
                pass
            prefix = "└•" if i == total else "├•"
            role = " (Owner)" if user_id == OWNER_ID else " (Sudo)"
            msg += f"<b>{prefix} <a href='tg://user?id={user_id}'>{name}</a>:</b> <code>{user_id}</code>{role}\n"
        msg += "</blockquote>"
        await ok.edit(msg, parse_mode='html')

@on_cmd("restart")
async def restart(e):
    if e.sender_id in SUDO_USERS:
        event_key = f"{e.chat_id}_{e.id}"
        my_id = getattr(e.client, "me_id", None)
        if my_id is None:
            try:
                me = await e.client.get_me()
                my_id = me.id
            except Exception:
                return
        if not await coordinator.resolve_responder(event_key, my_id):
            return

        ok = await e.reply("<blockquote><b>❏ ꜱ ᴛ ᴏ ʀ ᴍ   ʀᴇꜱᴛᴀʀᴛ</b>\n» <code>ʀᴇꜱᴛᴀʀᴛɪɴɢ ꜱᴛᴏʀᴍ ⌛ ...</code></blockquote>", parse_mode='html')
        if HEROKU_APP_NAME and HEROKU_API_KEY:
            try:
                Heroku = heroku3.from_key(HEROKU_API_KEY)
                app = Heroku.app(HEROKU_APP_NAME)
                await ok.edit("<blockquote><b>❏ ꜱ ᴛ ᴏ ʀ ᴍ   ʀᴇꜱᴛᴀʀᴛ</b>\n» <b>ʀᴇꜱᴛᴀʀᴛɪɴɢ ʜᴇʀᴏᴋᴜ ᴅʏɴᴏ...</b> 🔄</blockquote>", parse_mode='html')
                app.restart()
                return
            except Exception as err:
                await ok.edit(f"<blockquote><b>❏ ꜱ ᴛ ᴏ ʀ ᴍ   ʀᴇꜱᴛᴀʀᴛ</b>\n» <b>ʜᴇʀᴏᴋᴜ ʀᴇꜱᴛᴀʀᴛ ᴇʀʀᴏʀ:</b> <code>{err}</code>. ꜰᴀʟʟɪɴɢ ʙᴀᴄᴋ...</blockquote>", parse_mode='html')
        
        for client in CLIENTS:
            try:
                await client.disconnect()
            except Exception:
                pass
        import os
        script_path = os.path.abspath(sys.argv[0])
        os.execl(sys.executable, sys.executable, script_path, *sys.argv[1:])

def update_env_list(var_name: str, target_id: int) -> bool:
    from pathlib import Path
    env_file = Path(".env")
    target_str = str(target_id)
    try:
        content = env_file.read_text() if env_file.exists() else ""
        lines = content.splitlines()
        updated = False
        for i, line in enumerate(lines):
            if line.startswith(f"{var_name}="):
                current_items = line.split("=", 1)[1].strip().strip('"').strip("'").split()
                new_items = list(dict.fromkeys(current_items + [target_str]))
                lines[i] = f'{var_name}="{" ".join(new_items)}"'
                updated = True
                break
        if not updated:
            lines.append(f'{var_name}="{target_str}"')
        env_file.write_text("\n".join(lines) + "\n")
        return True
    except Exception:
        return False

def remove_env_list(var_name: str, target_id: int) -> bool:
    from pathlib import Path
    env_file = Path(".env")
    target_str = str(target_id)
    try:
        if not env_file.exists():
            return False
        content = env_file.read_text()
        lines = content.splitlines()
        updated = False
        for i, line in enumerate(lines):
            if line.startswith(f"{var_name}="):
                current_items = line.split("=", 1)[1].strip().strip('"').strip("'").split()
                if target_str in current_items:
                    current_items.remove(target_str)
                    lines[i] = f'{var_name}="{" ".join(current_items)}"'
                    updated = True
                break
        if updated:
            env_file.write_text("\n".join(lines) + "\n")
            return True
        return False
    except Exception:
        return False

@on_cmd("protect")
async def protect(event):
    if event.sender_id in SUDO_USERS:
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

        ok = await event.reply("<blockquote><b>❏ ꜱ ᴛ ᴏ ʀ ᴍ   ᴘʀᴏᴛᴇᴄᴛ</b>\n» ᴘʀᴏᴄᴇꜱ𝖘ɪɴɢ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ... 🛡️</blockquote>", parse_mode='html')
        parts = event.text.split()
        target_user = None
        
        if len(parts) > 1:
            param = parts[1]
            try:
                if param.isdigit():
                    entity = await event.client.get_entity(int(param))
                else:
                    entity = await event.client.get_entity(param)
                target_user = entity.id
            except Exception as e:
                await ok.edit(f"<blockquote><b>❏ ꜱ ᴛ ᴏ ʀ ᴍ   ᴘʀᴏᴛᴇᴄᴛ</b>\n» <b>ᴄᴏᴜʟᴅ ɴᴏᴛ ꜰɪɴᴅ ᴜꜱᴇʀ:</b> <code>{e}</code></blockquote>", parse_mode='html')
                return
        elif event.reply_to_msg_id:
            try:
                reply = await event.get_reply_message()
                target_user = reply.sender_id
            except Exception as e:
                await ok.edit(f"<blockquote><b>❏ ꜱ ᴛ ᴏ ʀ ᴍ   ᴘʀᴏᴛᴇᴄᴛ</b>\n» <b>ᴇʀʀᴏʀ ꜰᴇᴛᴄʜɪɴɢ ʀᴇᴘʟʏ:</b> <code>{e}</code></blockquote>", parse_mode='html')
                return

        if target_user:
            if target_user not in PROTECTED_USERS:
                PROTECTED_USERS.append(target_user)
                update_env_list("PROTECTED_USERS", target_user)
            await ok.edit(f"<blockquote><b>❏ ꜱ ᴛ ᴏ ʀ ᴍ   ᴘʀᴏᴛᴇᴄᴛ</b>\n» <b>ᴜꜱᴇʀ:</b> <code>{target_user}</code> ɪꜱ ɴᴏᴡ ᴘʀᴏᴛᴇᴄᴛᴇᴅ! 🛡️</blockquote>", parse_mode='html')
        else:
            chat_id = event.chat_id
            if chat_id not in PROTECTED_GROUPS:
                PROTECTED_GROUPS.append(chat_id)
                update_env_list("PROTECTED_GROUPS", chat_id)
            await ok.edit(f"<blockquote><b>❏ ꜱ ᴛ ᴏ ʀ ᴍ   ᴘʀᴏᴛᴇᴄᴛ</b>\n» <b>ɢʀᴏᴜᴘ:</b> <code>{chat_id}</code> ɪꜱ ɴᴏᴡ ᴘʀᴏᴛᴇᴄᴛᴇᴅ! 🛡️</blockquote>", parse_mode='html')

@on_cmd("unprotect")
async def unprotect(event):
    if event.sender_id in SUDO_USERS:
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

        ok = await event.reply("<blockquote><b>❏ ꜱ ᴛ ᴏ ʀ ᴍ   ᴘʀᴏᴛᴇᴄᴛ</b>\n» ʀᴇᴍᴏᴠɪɴɢ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ... 🔓</blockquote>", parse_mode='html')
        parts = event.text.split()
        target_user = None
        
        if len(parts) > 1:
            param = parts[1]
            try:
                if param.isdigit():
                    entity = await event.client.get_entity(int(param))
                else:
                    entity = await event.client.get_entity(param)
                target_user = entity.id
            except Exception as e:
                await ok.edit(f"<blockquote><b>❏ ꜱ ᴛ ᴏ ʀ ᴍ   ᴘʀᴏᴛᴇᴄᴛ</b>\n» <b>ᴄᴏᴜʟᴅ ɴᴏᴛ ꜰɪɴᴅ ᴜꜱᴇʀ:</b> <code>{e}</code></blockquote>", parse_mode='html')
                return
        elif event.reply_to_msg_id:
            try:
                reply = await event.get_reply_message()
                target_user = reply.sender_id
            except Exception as e:
                await ok.edit(f"<blockquote><b>❏ ꜱ ᴛ ᴏ ʀ ᴍ   ᴘʀᴏᴛᴇᴄᴛ</b>\n» <b>ᴇʀʀᴏʀ ꜰᴇᴛᴄʜɪɴɢ ʀᴇᴘʟʏ:</b> <code>{e}</code></blockquote>", parse_mode='html')
                return

        if target_user:
            if target_user in PROTECTED_USERS:
                PROTECTED_USERS.remove(target_user)
                remove_env_list("PROTECTED_USERS", target_user)
            await ok.edit(f"<blockquote><b>❏ ꜱ ᴛ ᴏ ʀ ᴍ   ᴘʀᴏᴛᴇᴄᴛ</b>\n» <b>ᴜꜱᴇʀ:</b> <code>{target_user}</code> ɪꜱ ɴᴏᴡ ᴜɴᴘʀᴏᴛᴇᴄᴛᴇᴅ! 🔓</blockquote>", parse_mode='html')
        else:
            chat_id = event.chat_id
            if chat_id in PROTECTED_GROUPS:
                PROTECTED_GROUPS.remove(chat_id)
                remove_env_list("PROTECTED_GROUPS", chat_id)
            await ok.edit(f"<blockquote><b>❏ ꜱ ᴛ ᴏ ʀ ᴍ   ᴘʀᴏᴛᴇᴄᴛ</b>\n» <b>ɢʀᴏᴜᴘ:</b> <code>{chat_id}</code> ɪꜱ ɴᴏᴡ ᴜɴᴘʀᴏᴛᴇᴄᴛᴇᴅ! 🔓</blockquote>", parse_mode='html')
