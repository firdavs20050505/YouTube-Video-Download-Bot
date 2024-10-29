# ©️ LISA-KOREA | @LISA_FAN_LK | NT_BOT_CHANNEL | LISA-KOREA/YouTube-Video-Download-Bot

# [⚠️ Do not change this repo link ⚠️] :- https://github.com/LISA-KOREA/YouTube-Video-Download-Bot



from pyrogram import Client, filters
from Youtube.config import Config

# Create a Pyrogram client
app = Client(
    "my_bot",
    api_id=Config.28146502, 
    api_hash=Config.8d3b3a914c6404fabe143bb2156bae01, 
    bot_token=Config.7547467147:AAFPr2Cectnffj4K8yqi1n5QNlAWR6qs5qc,
    plugins=dict(root="Youtube")
)



# Start the bot
print("🎊 I AM ALIVE 🎊")
app.run()
