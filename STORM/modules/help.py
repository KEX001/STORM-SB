from telethon import events, Button

from config import KEX1, KEX2, KEX3, KEX4, KEX5, KEX6, KEX7, KEX8, KEX9, KEX10, SUDO_USERS, CMD_HNDLR as hl


HELP_STRING = f"""
✨ **•─╼⃝𖠁 ʙᴏᴛ ʜᴇʟᴘ 𖠁⃝╾─•** ✨

**[ꜱᴛᴏʀᴍ  ꜱᴘᴀᴍ ʙᴏᴛ](https://t.me/Kexx_XD) ʜᴇʟᴘ ᴍᴇɴᴜ** 🥀

**ʜᴇʟᴘ ᴍᴇɴᴜ ᴘᴏᴡᴇʀᴇᴅ ʙʏ [ꜱᴛᴏʀᴍ](https://github.com/KEX001/STORM-SB)** ✨

**ᴄʜᴀɴɴᴇʟ: [ꜱᴛᴏʀᴍ ᴛᴇᴄʜ 🇮🇳](https://t.me/STORM_TECHH)**
**ꜱᴜᴘᴘᴏʀᴛ: [ꜱᴛᴏʀᴍ ᴄʜᴀᴛᴢ 🇮🇳](https://t.me/STORM_CHATZ)**
"""
HELP_BUTTON = [
    [
      Button.inline("• ꜱᴘᴀᴍ •", data="spam"),
      Button.inline("• ʀᴀɪᴅ •", data="raid")
    ],
    [
      Button.inline("• ᴇxᴛʀᴀꜱ •", data="extra"),
      Button.inline("• ᴏᴡɴᴇʀ •", data="owner")
    ],
    [
      Button.url("• ꜱᴜᴘᴘᴏʀᴛ •", "https://t.me/STORM_CHATZ")
    ]
  ]

@KEX1.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
        try:
          await event.client.send_file(event.chat_id,
              "https://graph.org/file/c3b279aee41f8bbe6466b.jpg",
              caption=HELP_STRING,
              buttons=HELP_BUTTON
              )
        except Exception as e:
            await event.client.send_message(event.chat_id, f"ᴀɴ ᴇxᴄᴇᴘᴛɪᴏɴ ᴏᴄᴄᴜʀᴇᴅ!\n\n**ᴇʀʀᴏʀ:** {str(e)}")

extra_msg = f"""
**•─╼⃝𖠁 ᴇ​🇽​ᴛʀᴀ ᴄᴏᴍᴍᴀɴᴅꜱ⦂ 𖠁⃝╾─•**

 ˣ ᴄʜᴇᴄᴋ ᴘɪɴɢ

👨‍💻 ᴜꜱᴀɢᴇ :
🔸 {hl}ᴘɪɴɢ

 ˣ ʀᴇꜱᴛᴀʀᴛ ʙᴏᴛ ɪᴛ ᴡɪʟʟ ᴛᴀᴋᴇ 5 ᴍɪɴ

👨‍💻 ᴜꜱᴀɢᴇ :
🔸 {hl}ʀᴇꜱᴛᴀʀᴛ

 ˣ ᴛᴏ ᴀᴄᴛɪᴠᴇ ᴇᴄʜᴏ ᴏɴ ᴀɴʏ ᴜꜱᴇʀ

👨‍💻 ᴜꜱᴀɢᴇ :
🔸 {hl}ᴇᴄʜᴏ (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)
🔸 {hl}ʀᴍᴇᴄʜᴏ (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)

 ˣ ᴛᴏ ʟᴇᴀᴠᴇ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ

👨‍💻 ᴜꜱᴀɢᴇ :
🔸 {hl}ʟᴇᴀᴠᴇ (ɢʀᴏᴜᴘ/ᴄʜᴀᴛ ɪᴅ)
🔸 {hl}ʟᴇᴀᴠᴇ (ʏᴘᴇ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ ʙᴏᴛ ᴡɪʟʟ ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ ᴛʜᴀᴛ ɢʀᴏᴜᴘ)

 ˣ ꜱᴘᴀᴍꜱ ʜᴀɴɢɪɴɢ ᴍᴇꜱꜱᴀɢᴇ ꜰᴏʀ ɢɪᴠᴇɴ ᴄᴏᴜɴᴛᴇʀ

👨‍💻 ᴜꜱᴀɢᴇ :
🔸 {hl}ʜᴀɴɢ (ᴄᴏᴜɴᴛᴇʀ)

 ˣ ꜱᴇɴᴅꜱ ᴇᴍᴏᴊɪ ᴡɪᴛʜ ᴛʜᴇ ɢɪᴠᴇ ᴄᴏᴜɴᴛᴇʀ ᴏɴ ᴜꜱᴇʀ

👨‍💻 ᴜꜱᴀɢᴇ :
🔸 {hl}ᴇᴍᴏᴊɪ (ᴄᴏᴜɴᴛᴇʀ) (ᴜꜱᴇʀɴᴀᴍᴇ)
🔸 {hl}ᴇᴍᴏᴊɪ (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)

 ˣ ʟᴏᴠᴇ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ

👨‍💻 ᴜꜱᴀɢᴇ :
🔸 {hl}ʟᴏᴠᴇʀᴀɪᴅ (ᴄᴏᴜɴᴛᴇʀ) (ᴜꜱᴇʀɴᴀᴍᴇ)
🔸 {hl}ʟᴏᴠᴇʀᴀɪᴅ (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)

 ˣ ꜰʟɪʀᴛꜱ ᴡɪᴛʜ ᴛʜᴇ ɢɪᴠᴇ ᴄᴏᴜɴᴛᴇʀ ᴏɴ ᴜꜱᴇʀ

👨‍💻 ᴜꜱᴀɢᴇ :
🔸 {hl}ꜰʟɪʀᴛ (ᴄᴏᴜɴᴛᴇʀ) (ᴜꜱᴇʀɴᴀᴍᴇ)
🔸 {hl}ꜰʟɪʀᴛ (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)

 ˣ ꜱʜᴀʏᴀʀɪ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ

👨‍💻 ᴜꜱᴀɢᴇ :
🔸 {hl}ꜱʀᴀɪᴅ (ᴄᴏᴜɴᴛᴇʀ) (ᴜꜱᴇʀɴᴀᴍᴇ)
🔸 {hl}ꜱʀᴀɪᴅ (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ) 

**© @KKEX_XD**
"""


owner_msg = f"""
**•─╼⃝𖠁 ᴏᴡɴᴇʀ ᴄᴏᴍᴍᴀɴᴅꜱ⦂ 𖠁⃝╾─•**

 ˣ ꜱᴜᴅᴏ

👨‍💻 ᴜꜱᴀɢᴇ :
🔸 {hl}ᴀᴅᴅꜱᴜᴅᴏ (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)

**© @KKEX_XD**
"""      
          
raid_msg = f"""
**•─╼⃝𖠁 ʀᴀɪᴅ ᴄᴏᴍᴍᴀɴᴅꜱ: 𖠁⃝╾─•**

 ˣ ꜱᴛᴀʀᴛ ᴛʜᴇ ʀᴀɪᴅ ɪɴ ᴛʜᴇ ᴄʜᴀᴛ.

👨‍💻 ᴜꜱᴀɢᴇ :
🔸 {hl}ʀᴀɪᴅ (ᴄᴏᴜɴᴛꜱ) (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)
🔸 {hl}ʀᴀɪᴅ (ᴄᴏᴜɴᴛꜱ) (ᴜꜱᴇʀɴᴀᴍᴇ)

 ˣ ᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀᴛ.

👨‍💻 ᴜꜱᴀɢᴇ :
🔸 {hl}ʀʀᴀɪᴅ (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)
🔸 {hl}ʀʀᴀɪᴅ (ᴜꜱᴇʀɴᴀᴍᴇ)

 ˣ ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ

👨‍💻 ᴜꜱᴀɢᴇ :
🔸 {hl}ᴅʀʀᴀɪᴅ (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)
🔸 {hl}ᴅʀʀᴀɪᴅ (ᴜꜱᴇʀɴᴀᴍᴇ)

**© @KKEX_XD**
"""

spam_msg = f"""
**•─╼⃝𖠁 ꜱᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅꜱ: 𖠁⃝╾─•**

 ˣ ꜱᴘᴀᴍꜱ ᴀ ᴍᴇꜱꜱᴀɢᴇ

👨‍💻 ᴜꜱᴀɢᴇ :
🔸 {hl}ꜱᴘᴀᴍ (ᴄᴏᴜɴᴛꜱ) (ᴀᴜᴛʜᴏʀ)
🔸 {hl}ꜱᴘᴀᴍ (ᴄᴏᴜɴᴛꜱ) (ʀᴇᴘʟʏɪɴɢ ᴀɴʏ ᴍᴇꜱꜱᴀɢᴇ)

 ˣ ᴘᴏʀᴍᴏɢʀᴀᴘʜʏ ꜱᴘᴀᴍ

👨‍💻 ᴜꜱᴀɢᴇ :
🔸 {hl}ᴘꜱᴘᴀᴍ (ᴄᴏᴜɴᴛꜱ)

 ˣ ꜱᴘᴀᴍ ᴛʜᴇ ᴄʜᴀᴛ ᴡɪᴛʜ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ

👨‍💻 ᴜꜱᴀɢᴇ :
🔸 {hl}ɢᴍ (ᴄᴏᴜɴᴛꜱ)
🔸 {hl}ɢᴍ (ᴄᴏᴜɴᴛꜱ) (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)
🔸 {hl}ɢᴍ -ᴜ
🔸 {hl}ɢᴍ -ᴜ (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)

 ˣ ꜱᴘᴀᴍ ᴛʜᴇ ᴄʜᴀᴛ ᴡɪᴛʜ ɢᴏᴏᴅ ᴀꜰᴛᴇʀɴᴏᴏɴ

👨‍💻 ᴜꜱᴀɢᴇ :
🔸 {hl}ɢᴀ (ᴄᴏᴜɴᴛꜱ) (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)
🔸 {hl}ɢᴀ -ᴜ (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ

 ˣ ꜱᴘᴀᴍ ᴛʜᴇ ᴄʜᴀᴛ ᴡɪᴛʜ ɢᴏᴏᴅ ɴɪɢʜᴛ

👨‍💻 ᴜꜱᴀɢᴇ :
🔸 {hl}ɢɴ (ᴄᴏᴜɴᴛꜱ) (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)
🔸 {hl}ɢɴ -ᴜ (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)

 ˣ ꜱᴘᴀᴍ ᴛʜᴇ ᴄʜᴀᴛ ᴡɪᴛʜ ʙᴅᴀʏ ᴍꜱɢꜱ

👨‍💻 ᴜꜱᴀɢᴇ :
🔸 {hl}ʙꜱᴘᴀᴍ (ᴄᴏᴜɴᴛꜱ) (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)
🔸 {hl}ʙꜱᴘᴀᴍ -ᴜ (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)

** © @KKEX_XD**
"""                                
           
@KEX1.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
    if event.query.user_id in SUDO_USERS:    
        await event.edit(
            HELP_STRING,
            buttons=[
              [
                Button.inline("• ꜱᴘᴀᴍ •", data="spam"),
                Button.inline("• ʀᴀɪᴅ •", data="raid")
              ],
              [
                Button.inline("• ᴇxᴛʀᴀꜱ •", data="extra"),
                Button.inline("• ᴏᴡɴᴇʀ •", data="owner")
              ],
              [
                Button.url("• ꜱᴜᴘᴘᴏʀᴛ •", "https://t.me/STORM_CHATZ")
              ]
            ]
          )
    else:
        await event.answer("ɴᴏᴏʙ ! ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ꜱᴛᴏʀᴍ ꜱᴘᴀᴍ ʙᴏᴛꜱ !! @KKEX_XD", cache_time=0, alert=True)


@KEX1.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
    if event.query.user_id in SUDO_USERS:    
        await event.edit(spam_msg,
              buttons=[[Button.inline("🔙 ʙᴀᴄᴋ", data="help_back"),],],
              ) 
    else:
        await event.answer("ɴᴏᴏʙ ! ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ꜱᴛᴏʀᴍ ꜱᴘᴀᴍ ʙᴏᴛꜱ !! @KKEX_XD", cache_time=0, alert=True)


@KEX1.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(raid_msg,
            buttons=[[Button.inline("🔙 ʙᴀᴄᴋ", data="help_back"),],],
          )
    else:
        await event.answer("ɴᴏᴏʙ ! ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ꜱᴛᴏʀᴍ ꜱᴘᴀᴍ ʙᴏᴛꜱ !! @KKEX_XD", cache_time=0, alert=True)


@KEX1.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(extra_msg,
            buttons=[[Button.inline("🔙 ʙᴀᴄᴋ", data="help_back"),],],
            )
    else:
        await event.answer("ɴᴏᴏʙ ! ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ꜱᴛᴏʀᴍ ꜱᴘᴀᴍ ʙᴏᴛꜱ !! @KKEX_XD", cache_time=0, alert=True)
