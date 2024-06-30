import logging
from pyrogram import Client, filters
from pyrogram.types import Message
from youtube_search import YoutubeSearch
from VIPMUSIC import app

@app.on_message(filters.command(["ytsearch"]))
async def ytsearch(client: Client, message: Message):
    try:
        if len(message.command) < 2:
            await message.reply_text("ᴜꜱᴀɢᴇ: /ytsearch [Qᴜᴇʀʏ]")
            return
        
        query = message.text.split(None, 1)[1]
        m = await message.reply_text("✨")
        
        results = YoutubeSearch(query, max_results=4).to_dict()
        
        text = "\n\n".join(
            f"🎬 ᴛɪᴛʟᴇ: {result['title']}\n"
            f"⏳ ᴅᴜʀᴀᴛɪᴏɴ: {result['duration']}\n"
            f"👀 ᴠɪᴇᴡꜱ: {result['views']}\n"
            f"📺 ᴄʜᴀɴɴᴇʟ: {result['channel']}\n"
            f"🔗 https://youtube.com{result['url_suffix']}\n"
            "➖➖➖➖➖➖➖➖➖➖➖"
            for result in results
        )

        await m.edit(text, disable_web_page_preview=True)
    except Exception as e:
        logger.error(f"ᴇʀʀᴏʀ ɪɴ ʏᴛꜱᴇᴀʀᴄʜ: {e}")
        await message.reply_text("ᴀɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ ᴡʜɪʟᴇ ꜱᴇᴀʀᴄʜɪɴɢ. ᴘʟᴇᴀꜱᴇ ᴛʀʏ ᴀɢᴀɪɴ ʟᴀᴛᴇʀ.")
