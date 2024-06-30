from pyrogram import Client, filters
from bs4 import BeautifulSoup
from googlesearch import search
from VIPMUSIC import app
import requests
from pyrogram.types import Message

def googlesearch(query):
    co = 1
    returnquery = {}
    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
        url = str(j)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        site_title = soup.title.string if soup.title else "No Title"
        metas = soup.find_all("meta", attrs={"name": "description"})
        metadata = metas[0].get("content") if metas else "No description available"
        returnquery[co] = {"title": site_title, "metadata": metadata, "url": j}
        co += 1
    return returnquery

@app.on_message(filters.command("gsearch", ["/"]))
async def gs(client: Client, message: Message):
    Man = await message.reply_text("ᴘʀᴏᴄᴇꜱꜱɪɴɢ...")
    msg_txt = message.text
    query = msg_txt.split(" ", 1)[1] if " " in msg_txt else None
    
    if not query:
        await message.reply_text("ᴘʟᴇᴀꜱᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ Qᴜᴇʀʏ ᴛᴏ ꜱᴇᴀʀᴄʜ..")
        return
    
    results = googlesearch(query)
    returnmsg = ""
    
    for i in range(1, 11):
        presentquery = results.get(i, {})
        presenttitle = presentquery.get("title", "No Title")
        presentmeta = presentquery.get("metadata", "No description available")
        presenturl = presentquery.get("url", "")
        returnmsg += f"🎬 ᴛɪᴛʟᴇ: {presenttitle}\n🔗: {presenturl}\n📃 ᴅᴇꜱᴄʀɪᴘᴛɪᴏɴ: {presentmeta}\n➖➖➖➖➖➖➖➖➖➖➖\n\n"
    
    await Man.edit_text(returnmsg if returnmsg else "ɴᴏ ʀᴇꜱᴜʟᴛꜱ ꜰᴏᴜɴᴅ.....")
