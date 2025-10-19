from PyroUbot import *
import random
import requests
from pyrogram.enums import *
from pyrogram import *
from pyrogram.types import *
from io import BytesIO

__MODULE__ = "ᴡᴀʟʟᴘᴀᴘᴇʀ 2"
__HELP__ = """
<b>♛ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴡᴀʟʟᴘᴀᴘᴇʀ ♛</b>

<blockquote><b>perintah :
<code>{0}wallpp2</code> [Query]
ᴜɴᴛᴜᴋ ᴍᴇɴᴄᴀʀɪ ᴡᴀʟʟᴘᴀᴘᴇʀ/ɢᴀᴍʙᴀʀ

✮ Query ✮
   卍 ᴄᴏsᴘʟᴀʏ
   卍 pubg
   卍 cogan2   
   卍 cecan2   
   卍 motor
   卍 mobil     
   卍 mountain 
   卍 cyberspace 
   卍 darkjokes  
   卍 meme 
"""

URLS = {
    "cosplay": "https://api.betabotz.eu.org/api/wallpaper/cosplay?apikey=Btz-bxwol",
    "meme": "https://api.betabotz.eu.org/api/wallpaper/meme?apikey=Btz-bxwol",
    "darkjokes": "https://api.betabotz.eu.org/api/wallpaper/darkjokes?apikey=Btz-bxwol",
    "cyberspace": "https://api.betabotz.eu.org/api/wallpaper/cyberspace?apikey=Btz-bxwol",
    "mountain": "https://api.betabotz.eu.org/api/wallpaper/mountain?apikey=Btz-bxwol",
    "mobil": "https://api.betabotz.eu.org/api/wallpaper/mobil?apikey=Btz-bxwol",
    "motor": "https://api.betabotz.eu.org/api/wallpaper/motor?apikey=Btz-bxwol",
    "cecan2": "https://api.betabotz.eu.org/api/wallpaper/cecan2?apikey=Btz-bxwol",
    "cogan2": "https://api.betabotz.eu.org/api/wallpaper/cogan2?apikey=Btz-bxwol",
    "pubg": "https://api.betabotz.eu.org/api/wallpaper/pubg?apikey=Btz-bxwol",
    }


@PY.UBOT("wallpp2")
@PY.TOP_CMD
async def _(client, message):
    # Extract query from message
    query = message.text.split()[1] if len(message.text.split()) > 1 else None
    
    if query not in URLS:
        valid_queries = ", ".join(URLS.keys())
        await message.reply(f"<emoji id=5215204871422093648>❌</emoji> Query tidak valid. Gunakan salah satu dari: {valid_queries}.")
        return

    processing_msg = await message.reply("<emoji id=4943239162758169437>🤩</emoji> Processing...")
    
    try:
        await client.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
        response = requests.get(URLS[query])
        response.raise_for_status()
        
        photo = BytesIO(response.content)
        photo.name = 'image.jpg'
        
        await client.send_photo(message.chat.id, photo)
        await processing_msg.delete()
    except requests.exceptions.RequestException as e:
        await processing_msg.edit_text(f"<emoji id=5215204871422093648>❌</emoji> Gagal mengambil gambar anime Error: {e}")
