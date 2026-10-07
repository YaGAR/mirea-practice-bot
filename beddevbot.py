import asyncio
import os
from telegram import Bot
from telegram.error import TelegramError

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("Set the TELEGRAM_BOT_TOKEN environment variable")

RECIPIENTS = {
    "417338994": {
        "text": "Hello! This is your message.",
        "photo": None,
    },
    # "123456789": {
    #     "text": "A different message for this user",
    #     "photo": r"C:\images\photo.jpg",
    # },
}

async def main():
    bot = Bot(token=TOKEN)
    for chat_id, content in RECIPIENTS.items():
        try:
            if content["photo"]:
                with open(content["photo"], "rb") as photo:
                    await bot.send_photo(
                        chat_id=chat_id,
                        photo=photo,
                        caption=content["text"],
                    )
            else:
                await bot.send_message(
                    chat_id=chat_id,
                    text=content["text"],
                )
        except TelegramError as error:
            print(f"Could not send to chat {chat_id}: {error}")

asyncio.run(main())