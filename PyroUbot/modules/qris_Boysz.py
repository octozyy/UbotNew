from pyrogram import Client, filters
from PyroUbot import *

@PY.UBOT("nope")
async def _(client, message):
    try:
        if message.from_user.id != OWNER_ID:
            await message.reply_text("<blockquote><b>❌ Anda tidak memiliki izin untuk menggunakan perintah ini!</b></blockquote>")
            return

        args = message.text.split(" ")
        if len(args) < 2:
            await message.reply_text("<blockquote><b>Gunakan format: `/qris 10.000`</b></blockquote>")
            return

        nominal_str = args[1].replace(".", "")
        if not nominal_str.isdigit():
            await message.reply_text("<blockquote><b>Nominal harus berupa angka yang valid!</b></blockquote>")
            return

        nominal_formatted = f"{int(nominal_str):,}".replace(",", ".") 
        
        qris_link = "082123179079"

        caption = f"""
<blockquote><b><emoji id=5852827336705053876>⭐</emoji> **Dana Anda Siap!** <emoji id=5852827336705053876>⭐</emoji>
<emoji id=5213094908608392768>💰</emoji> Nominal: **Rp {nominal_formatted}**
<emoji id=6186224886021622832>📲</emoji> dana ini untuk melakukan pembayaran dengan mudah!
<emoji id=6122783674984303689>💰</emoji> Lebihkan Transfer Sebanyak 100p (seratus perak) jika tidak ada, pas kan saja dengan nominal yang mau dibeli
<emoji id=5787188704434982946>✅</emoji> Cepat, Aman, dan Praktis!</b></blockquote>
        """

        await message.reply_photo(photo=qris_link, caption=caption)
    
    except Exception as e:
        await message.reply_text(f"<blockquote><b>Terjadi kesalahan: {e}</b></blockquote>")