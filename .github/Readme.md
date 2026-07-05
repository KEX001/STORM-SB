<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

<h1 align="center">
  <b>S T O R M &nbsp; SB</b>
</h1>

    
<p align="center">
  <b>ʟɪɢʜᴛɴɪɴɢ-ꜰᴀꜱᴛ • ʜɪɢʜʟʏ ᴄᴜꜱᴛᴏᴍɪᴢᴀʙʟᴇ • ᴜɴꜱᴛᴏᴘᴘᴀʙʟᴇ</b>
</p>


<p align="center">
    <a href="https://github.com/KEX001/STORM-SB/commits/main"><img src="https://img.shields.io/github/last-commit/KEX001/STORM-SB?color=ff69b4&logo=github&logoColor=ff69b4&style=for-the-badge" /></a>
    <a href="https://github.com/KKEX001/STORM-SB/issues"> <img src="https://img.shields.io/github/issues/KEX001/STORM-SB?color=blue&logo=github&style=for-the-badge" /></a>
    <a href="https://github.com/KEX001/STORM-SB"> <img src="https://img.shields.io/github/repo-size/KEX001/STORM-SB?logo=github&style=for-the-badge" /></a>
    <a href="https://github.com/KEX001/STORM-SB/network/members"> <img src="https://img.shields.io/github/forks/KEX001/STORM-SB?logo=github&style=for-the-badge" /></a>
    <a href="https://pypi.org/project/Telethon/"><img src="https://img.shields.io/pypi/v/Telethon?color=important&label=Telethon&logo=python&logoColor=brightgreen&style=for-the-badge" /></a>
    <img alt="PYTHON" src="https://img.shields.io/badge/PYTHON-v3.10.2-white?style=for-the-badge&logo=appveyor"/>
    <a href="https://t.me/Syphixlabs"><img src="https://img.shields.io/badge/Support%20Channel-blue.svg?style=for-the-badge&logo=Telegram"></a>
    <a href="https://t.me/SyphixHub"><img src="https://img.shields.io/badge/Support%20Group-blue.svg?style=for-the-badge&logo=Telegram"></a>
</p>

<p align="center">
  <b><img src="https://github.com/KEX001/STORM-SB/blob/main/res/Z30J.gif" width="20px"></b><br>
  <img src="https://count.getloli.com/get/@KEX001.github.STORM-SB" alt="visitors">
</p>

## 🚀 ꜰᴇᴀᴛᴜʀᴇꜱ

- **Multi-Bot Support**: Run anywhere from 1 to 50 bot clients simultaneously from a single server.
- **Spam & Media Spam**: Rapidly send texts or random media (`!spam`, `!pspam`).
- **Abuse & Flirt**: Dynamically tagged randomized databases (`!abuse`, `!flirt`).
- **Raid & Love Raid**: Tag users recursively with varied lines (`!raid`, `!hraid`, `!loveraid`, `!sraid`).
- **Protection System**: Block commands from being used against specific groups, the bot owner, or sudo users (`!protect`).
- **Premium Aesthetics**: Professional, small-caps, blockquote HTML formatting.
- **PaaS / Render Ready**: Configured with a lightweight Dockerfile, Gunicorn, Flask webserver, and Procfile for continuous 24/7 deployment.

---

## ☁️ ᴅᴇᴘʟᴏʏᴍᴇɴᴛ (ʀᴇɴᴅᴇʀ & ʜᴇʀᴏᴋᴜ)

This repository is optimized for deployment on PaaS providers like [Render](https://render.com/) or [Heroku](https://heroku.com/). The provided `Dockerfile` and `Procfile` run a web server concurrently to keep your deployment alive 24/7.

<p align="center">
  <a href="https://dashboard.heroku.com/new?template=https%3A%2F%2Fgithub.com%2FKEX001%2FSTORM-SB">
    <img src="https://img.shields.io/badge/Deploy%20On%20Heroku-purple?style=for-the-badge&logo=heroku" width="220" height="38.45"/>
  </a>
  <a href="https://render.com/deploy?repo=https://github.com/KEX001/STORM-SB">
    <img src="https://render.com/images/deploy-to-render-button.svg" alt="Deploy to Render" height="38.45">
  </a>
</p>

### ᴅᴇᴘʟᴏʏɪɴɢ ᴏɴ ʀᴇɴᴅᴇʀ:
1. **Create a Render Account**: Sign up or log in at [dashboard.render.com](https://dashboard.render.com).
2. **New Web Service**: Click the **New +** button and select **Web Service**.
3. **Connect Repository**: Connect your GitHub account and select your fork of this repository.
4. **Environment**: Render should automatically detect `Docker` as the environment.
5. **Set Environment Variables**: Input all your required configuration variables (see table below).
6. **Deploy**: Click **Create Web Service**. 
7. **Keep Alive**: Ping the generated Web Service URL every 10 minutes using [UptimeRobot](https://uptimerobot.com) to keep it running 24/7.

---

## 💻 ʀᴜɴɴɪɴɢ ʟᴏᴄᴀʟʟʏ

If you want to test or run the bot on your local macOS/Linux machine:

1. **Clone the repo & Enter directory:**
   ```bash
   git clone https://github.com/KEX001/STORM-SB.git
   cd STORM-SB
   ```
2. **Create a `.env` file:**
   Add your keys directly into a `.env` file based on `sample.env`.
3. **Run the start script:**
   ```bash
   ./start.sh
   ```

---

## ⚙️ ᴄᴏɴꜰɪɢ ᴠᴀʀɪᴀʙʟᴇꜱ

> **ᴍᴜʟᴛɪ-ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛ**: _ᴀ ᴍɪɴɪᴍᴜᴍ ᴏꜰ 1 ʙᴏᴛ ᴛᴏᴋᴇɴ ɪꜱ ʀᴇQᴜɪʀᴇᴅ (`BOT_TOKEN`). ʏᴏᴜ ᴄᴀɴ ᴀᴅᴅ ᴜᴘ ᴛᴏ ᴀ ᴍᴀxɪᴍᴜᴍ ᴏꜰ 50 ᴛᴏᴋᴇɴꜱ (`BOT_TOKEN50`) ᴛᴏ ʀᴜɴ ᴍᴜʟᴛɪᴘʟᴇ ᴄʟɪᴇɴᴛꜱ ꜱɪᴍᴜʟᴛᴀɴᴇᴏᴜꜱʟʏ!_

| Variable | Description |
|---|---|
| `API_ID` | Your Telegram API ID from [my.telegram.org](https://my.telegram.org) |
| `API_HASH` | Your Telegram API HASH from [my.telegram.org](https://my.telegram.org) |
| `BOT_TOKEN` | Your Bot Token from [@BotFather](https://t.me/BotFather) |
| `BOT_TOKEN2` to `BOT_TOKEN50` | (Optional) Additional Bot Tokens for multi-client. |
| `OWNER_ID` | Your Telegram User ID (Grants ultimate control over the bot) |
| `SUDO_USERS` | Space-separated User IDs of people you want to give access to. |

---

## 📋 ᴄᴏᴍᴍᴀɴᴅꜱ ʟɪꜱᴛ

Trigger commands using `!` (or your custom prefix). 
*Note: Use `!help` in-bot for an updated interactive menu.*

- `!ping` - Check bot latency.
- `!alive` - Check if bot is online.
- `!help` - Display the help menu.
- `!update` - Update the bot with the latest changes from your upstream repository.
- `!spam <count> <msg>` - Send a message multiple times.
- `!pspam <count>` - Send random media from the database.
- `!abuse <count> <@user>` - Tag a user with random abuse lines.
- `!flirt <count> <@user>` - Tag a user with random pickup lines.
- `!raid / !sraid / !hraid <count> <@user>` - Various intensities and styles of raid attacks.
- `!loveraid <count> <@user>` - Romantic/Punjabi raid messages.
- `!rraid <@user>` - Automatically replies to every message the target sends.
- `!drraid <@user>` - Disable auto-reply raid.
- `!protect / !unprotect` - Add/remove chats from the protected list.
- `!leave` - Leave the current group.

---

## ᴅɪꜱᴄʟᴀɪᴍᴇʀ

- ᴏᴜʀ ᴛᴇᴀᴍ ᴅɪꜱᴄʟᴀɪᴍꜱ ʀᴇꜱᴘᴏɴꜱɪʙɪʟɪᴛʏ ꜰᴏʀ ᴀɴʏ ᴄᴏɴꜱᴇQᴜᴇɴᴄᴇꜱ ᴛᴏ ʏᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛ.
ɪꜰ ɪꜱꜱᴜᴇꜱ ᴀʀɪꜱᴇ ᴅᴜᴇ ᴛᴏ ᴍɪꜱᴜꜱᴇ ᴏʀ ᴄᴏɴꜰʟɪᴄᴛꜱ, ᴀᴄᴄᴏᴜɴᴛᴀʙɪʟɪᴛʏ ʀᴇꜱᴛꜱ ᴡɪᴛʜ ᴛʜᴇ ᴜꜱᴇʀ.
ᴛʜᴇ ʙᴏᴛ ꜱᴇʀᴠᴇꜱ ꜰᴏʀ ʀᴇᴄʀᴇᴀᴛɪᴏɴᴀʟ ᴘᴜʀᴘᴏꜱᴇꜱ ᴀɴᴅ ᴀɪᴍꜱ ᴛᴏ ꜱᴛʀᴇᴀᴍʟɪɴᴇ ɢʀᴏᴜᴘ/ᴘʀᴏꜰɪʟᴇ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ.

- ᴡʜɪʟᴇ ꜰᴏʀᴋɪɴɢ ᴛʜᴇ ʀᴇᴘᴏꜱɪᴛᴏʀʏ ɪꜱ ᴘᴇʀᴍɪᴛᴛᴇᴅ, ᴡᴇ ᴡᴏɴ'ᴛ ꜱᴜᴘᴘᴏʀᴛ ᴇᴅɪᴛᴇᴅ ᴘʟᴜɢɪɴꜱ ᴏʀ ᴍᴏᴅɪꜰɪᴄᴀᴛɪᴏɴꜱ.

- ᴛʜɪꜱ ꜱᴇʀᴠɪᴄᴇ ᴅᴏᴇꜱ ɴᴏᴛ ᴘʀᴏᴠɪᴅᴇ ɪɴᴅɪᴠɪᴅᴜᴀʟɪᴢᴇᴅ ꜱᴜᴘᴘᴏʀᴛ.
ꜱʜᴏᴜʟᴅ ʏᴏᴜ ʀᴇQᴜɪʀᴇ ᴀꜱꜱɪꜱᴛᴀɴᴄᴇ, ᴋɪɴᴅʟʏ ᴇɴɢᴀɢᴇ ᴡɪᴛʜ ᴏᴜʀ ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ ꜰᴏʀ ᴄᴏᴍᴍᴜɴɪᴛʏ-ʙᴀꜱᴇᴅ ɢᴜɪᴅᴀɴᴄᴇ.

## ʟɪᴄᴇɴᴄᴇ 

[![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-127x51.png)](https://github.com/KEX001/STORM-SB/blob/main/LICENSE)  

## ᴄᴏɴᴛʀɪʙᴜᴛᴏʀꜱ

<a href="https://github.com/KEX001/STORM-SB/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=KEX001/STORM-SB" />
</a>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
