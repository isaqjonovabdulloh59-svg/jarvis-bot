"""Shaxsiy Telegram akkauntga BIR MARTA kirish.
Ishga tushiring: python tg_login.py
Telefon raqamingiz (+998...) va Telegram yuborgan kodni so'raydi.
Natijada jarvis_user.session fayli yaratiladi (uni hech kimga bermang!)."""
import os, asyncio
from dotenv import load_dotenv
from telethon import TelegramClient

load_dotenv("jarvis.env")

async def main():
    async with TelegramClient("jarvis_user",
                              int(os.environ["TELEGRAM_API_ID"]),
                              os.environ["TELEGRAM_API_HASH"]) as client:
        me = await client.get_me()
        print("Kirdi:", me.first_name, "- endi jarvis.py ni ishga tushirishingiz mumkin")

asyncio.run(main())
