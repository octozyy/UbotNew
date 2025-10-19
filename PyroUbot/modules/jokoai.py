from PyroUbot import *
import random
import requests
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from pyrogram.types import Message

__MODULE__ = "Joko Ai"
__HELP__ = """
<blockquote><b>Bantuan Untuk joko-ai

perintah : <code>{0}joko</code>
    Ai unik yang berbahasa jawa</b></blockquote>
"""


@PY.UBOT("joko")
@PY.TOP_CMD
async def Boysz_gpt(client, message):
    try:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji>mohon gunakan format\ncontoh : .joko query"
            )
        else:
            prs = await message.reply_text(f"<emoji id=5319230516929502602>🔍</emoji>proccesing kingz....")
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://api.siputzx.my.id/api/ai/joko?content={a}')

            try:
                if "data" in response.json():
                    x = response.json()["data"]                  
                    await prs.edit(
                      f"<blockquote>{x}</blockquote>"
                    )
                else:
                    await message.reply_text("No 'results' key found in the response.")
            except KeyError:
                await message.reply_text("Error accessing the response.")
    except Exception as e:
        await message.reply_text(f"{e}")

@PY.BOT("joko")
async def Boysz_gpt(client, message):
    try:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji>mohon gunakan format\ncontoh : .joko query"
            )
        else:
            prs = await message.reply_text(f"<emoji id=5319230516929502602>🔍</emoji>proccesing kingz....")
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://api.siputzx.my.id/api/ai/joko?content={a}')

            try:
                if "data" in response.json():
                    x = response.json()["data"]                  
                    await prs.edit(
                      f"<blockquote>{x}</blockquote>"
                    )
                else:
                    await message.reply_text("No 'results' key found in the response.")
            except KeyError:
                await message.reply_text("Error accessing the response.")
    except Exception as e:
        await message.reply_text(f"{e}")
