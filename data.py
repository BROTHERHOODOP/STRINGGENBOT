from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("🙄 ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ 🙄", callback_data="generate")]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("❣️ Support ❣️", url="https://t.me/TBH_COUNCIL_SUPPORT"),
         InlineKeyboardButton("🥀 Updates 🥀", url="https://t.me/THE_BROTHERHOOD_COUNCIL"),
        ],
    ]

    START = """
Hᴇʏ {},

Tʜɪs ɪs {},
Aɴ ᴏᴩᴇɴ sᴏᴜʀᴄᴇᴅ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.

ꜱᴜᴩᴩᴏʀᴛ : [SUPPORT](https://t.me/TBH_COUNCIL_SUPPORT)
Mᴀᴅᴇ ᴡɪᴛʜ 🖤 ʙʏ : [BROTHERHOOD](https://t.me/THE_BROTHERHOOD_COUNCIL) !
    """
