from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from AaruRobot import pbot as client


Aaru = "https://te.legra.ph/file/b016175f5537f279dc84f.jpg"

@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=Ayra,
        caption=f"""**ʜᴇʏ​ {message.from_user.mention()},\n\nɪ ᴀᴍ [ɴᴏʙɪᴛᴀ ✘ ʀᴏʙᴏᴛ-🇮🇳](t.me/its_Coder_xD)**

**» ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ :** [ɴᴏʙɪᴛᴀ_xᴅ](tg://user?id=5275980328)
**» ᴩʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{y()}`
**» ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{o}` 
**» ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{s}` 
**» ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{z}`

**ᴛʀɪsʜᴀ ✘ ʀᴏʙᴏᴛ sᴏᴜʀᴄᴇ ɪs ɴᴏᴡ ᴩᴜʙʟɪᴄ ᴀɴᴅ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ᴅᴇᴠᴇʟᴏᴘᴇʀ •", url="tg://user?id=5808223211"), 
                    InlineKeyboardButton(
                        "• sᴏᴜʀᴄᴇ •", url="https://github.com/CODER-XD143/AaruRobot")
                ]
            ]
        )
    )

__mod_name__ = "Rᴇᴩᴏ"
