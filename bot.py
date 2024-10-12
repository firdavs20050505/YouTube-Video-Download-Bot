# ©️ LISA-KOREA | @LISA_FAN_LK | NT_BOT_CHANNEL | LISA-KOREA/YouTube-Video-Download-Bot

# [⚠️ Do not change this repo link ⚠️] :- https://github.com/LISA-KOREA/YouTube-Video-Download-Bot



from pyrogram import Client, filters
from Youtube.config import Config

# Create a Pyrogram client
app = Client(
    "my_bot",
    api_id=20326178, 
    api_hash=0a1a0c54f14667417c28a19138b8b9b5, 
    bot_token=7800543508:AAFbXwLF_zyYm3EoCBXFqkK66uwixvdOCrI,
    plugins=dict(root="Youtube")
)



# Start the bot
print("🎊 I AM ALIVE 🎊")
app.run()
