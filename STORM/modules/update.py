import os
import sys
import asyncio
from subprocess import getoutput as run
import config
from config import CMD_HNDLR as hl
from STORM.client_manager import on_cmd

UPSTREAM_REPO = config.UPSTREAM_REPO

@on_cmd("update")
async def update_bot(e):
    if e.sender_id in config.SUDO_USERS:
        status_msg = await e.reply("<blockquote><b>» ᴄʜᴇᴄᴋɪɴɢ ꜰᴏʀ ᴜᴘᴅᴀᴛᴇꜱ... ⌛</b></blockquote>", parse_mode='html')
        
        try:
            # Check if git is initialized
            is_git = run("git rev-parse --is-inside-work-tree")
            if "true" not in is_git.lower():
                run("git init")
                run("git branch -M main")
                run(f"git remote add origin {UPSTREAM_REPO}")
                await asyncio.sleep(1)
            
            # Fetch latest from upstream
            fetch_output = run("git fetch origin")
            if "fatal:" in fetch_output.lower() or "error:" in fetch_output.lower():
                await status_msg.edit(f"<blockquote><b>» ᴜᴘᴅᴀᴛᴇ ꜰᴀɪʟᴇᴅ:</b> <code>Upstream repository not found. Please set a valid UPSTREAM_REPO in your environment variables.</code></blockquote>", parse_mode='html')
                return
            
            # Identify default branch of upstream repository
            branch_output = run("git ls-remote --symref origin HEAD")
            default_branch = "main"
            if "refs/heads/" in branch_output:
                default_branch = branch_output.split("refs/heads/")[1].split()[0]
                
            # Reset hard to upstream default branch
            update_output = run(f"git reset --hard origin/{default_branch}")
            
            if "is up to date" in update_output or "HEAD is now at" in update_output:
                await status_msg.edit("<blockquote><b>» ᴜᴘᴅᴀᴛᴇ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟ! ʀᴇꜱᴛᴀʀᴛɪɴɢ ʙᴏᴛ... 🔄</b></blockquote>", parse_mode='html')
                
                # Restart the bot process
                args = [sys.executable, "main.py"]
                os.execle(sys.executable, *args, os.environ)
            else:
                await status_msg.edit(f"<blockquote><b>» ᴜᴘᴅᴀᴛᴇ ꜰᴀɪʟᴇᴅ:</b> <code>{update_output}</code></blockquote>", parse_mode='html')
                
        except Exception as err:
            await status_msg.edit(f"<blockquote><b>» ᴇʀʀᴏʀ ᴅᴜʀɪɴɢ ᴜᴘᴅᴀᴛᴇ:</b> <code>{str(err)}</code></blockquote>", parse_mode='html')
