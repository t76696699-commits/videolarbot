import asyncio
import logging
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command

TOKEN = "8869424579:AAGblPU6D0i7tu08RgE9FW3KqRZ2VUsmvdU"
CHANNEL_ID = -1004354334641


ot = Bot(token=TOKEN)
dp = Dispatcher()

# Har bir "Kod" va kanalning real xabar ID raqamini shu yerga to'g'ridan-to'g'ri yozib chiqamiz
VIDEO_MAPPING = {
    1: 9,   # Kod: 1 uchun kanalning xabar ID raqami
    4: 12,  # Kod: 4 uchun kanalning xabar ID raqami
    5: 13,
    6: 14,
    7: 15,
    8: 16,
    10: 18,
    14: 22,
    15: 23,
    # Qolgan kodlarni ham shunday ko'rinishda davom ettirib yozib qo'yasiz:
    # Kod : Telegram_Xabar_ID
}

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Salom! 🎬 Bu video qidirish boti.\n\n"
        "Menga videoning **raqamini (ID)** yuboring, "
        "men kanaldan o'sha videoni topib yuboraman."
    )

@dp.message(F.text)
async def send_video_from_channel(message: types.Message):
    if message.text.isdigit():
        code = int(message.text)
        
        # Agar kiritilgan kod lug'atda bo'lsa, uning real ID raqamini olamiz
        if code in VIDEO_MAPPING:
            video_message_id = VIDEO_MAPPING[code]
        else:
            await message.answer("❌ Bunday raqamli video topilmadi.")
            return
        
        try:
            await bot.copy_message(
                chat_id=message.chat.id,
                from_chat_id=CHANNEL_ID,
                message_id=video_message_id
            )
        except Exception as e:
            await message.answer("❌ Video topilmadi yoki xatolik yuz berdi.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
