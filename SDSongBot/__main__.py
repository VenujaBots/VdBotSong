#SDBOTs <https://t.me/SDBOTs_Inifinity>

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from SDSongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from SDSongBot import SDbot as app
from SDSongBot import LOGGER

pm_start_text = """
π Hey [{}](tg://user?id={}), **I'm Vs Music Downloader Bot**
**Now send me the song name you want to download**
     
Syntax : ```/dsong Faded```
      
Powerd By @Venuja_Sadew π₯
"""

@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                     InlineKeyboardButton(
                        text="Channel πββοΈ", url="https://t.me/vndbotsupport"
                    ),
                    InlineKeyboardButton(
                        text="βAdd to Groupβ", url="http://t.me/TheVSMusicBot?startgroup=true"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)


app.start()
LOGGER.info("""

βββββββββββββββββββββββββββββββββββββββββββββββββ
βββββββββββββββββββββββββββββββββββββββββββββββββ
βββββββββββββββββββββββ¦ββββββββββββββββββββββββββ
βββββββββββββββββββββββββββββββββββββββββββββββββ
βββββββββββββββββββββββ¦ββββββββββββββββββββββββββ
βββββββββββββββββββββββββββββββββββββββββββββββββ SDSongBot is online.""")
idle()
