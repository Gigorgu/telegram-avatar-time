import os
import asyncio
from PIL import Image, ImageDraw, ImageFont
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
from telethon import TelegramClient
from telethon.tl.functions.photos import DeletePhotosRequest, UploadProfilePhotoRequest

load_dotenv()

API_ID = int(os.getenv('API_ID'))
API_HASH = os.getenv('API_HASH')
SESSION_NAME = os.getenv('SESSION_NAME', 'session')

DEVICE_MODEL = os.getenv('DEVICE_MODEL', 'Android')
SYSTEM_VERSION = os.getenv('SYSTEM_VERSION', '14(31)')
SYSTEM_LANGUAGE = os.getenv('SYSTEM_LANGUAGE', 'en')
LANGUAGE_CODE = os.getenv('LANGUAGE_CODE', 'en_US')
APP_VERSION = os.getenv('APP_VERSION', '11.2.0')

gmt_offset = int(os.getenv('GMT', '0'))

try:
    font = ImageFont.truetype("arial.ttf", 100)
except IOError:
    font = ImageFont.load_default()

def generate_image(current_time):
    img = Image.new('RGB', (1000, 1000), color='black')
    draw = ImageDraw.Draw(img)
    text = current_time.strftime("%H:%M")
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    position = ((1000 - text_width) // 2, (1000 - text_height) // 2)
    draw.text(position, text, fill='white', font=font)
    img.save('current_time.png')


def get_current_time_with_gmt():
    current_time = datetime.now(timezone.utc) + timedelta(hours=gmt_offset)
    return current_time

async def update_telegram_avatar(client):
    photos = await client.get_profile_photos('me')
    if photos:
        await client(DeletePhotosRequest(photos))
    a_photo = await client.upload_file('current_time.png')
    await client(UploadProfilePhotoRequest(file=a_photo))



async def update_time_image(client):
    while True:
        current_time = get_current_time_with_gmt()
        generate_image(current_time)
        await update_telegram_avatar(client)
        await asyncio.sleep(60)

async def main():
    client = TelegramClient(
        SESSION_NAME,
        API_ID,
        API_HASH,
        device_model=DEVICE_MODEL,
        system_version=SYSTEM_VERSION,
        app_version=APP_VERSION,
        lang_code=LANGUAGE_CODE,
        system_lang_code=SYSTEM_LANGUAGE
    )
    
    await client.start()
    await update_time_image(client)
if __name__ == "__main__":
    asyncio.run(main())
