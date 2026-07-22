import asyncio
import logging
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command

TOKEN = "8869424579:AAGblPU6D0i7tu08RgE9FW3KqRZ2VUsmvdU"
CHANNEL_ID = -1004354334641

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()


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
        # Farq aniq 6 taga teng bo'lgani uchun - 6 ni yozamiz
        video_message_id = int(message.text) - 6

        try:
            await bot.copy_message(
                chat_id=message.chat.id,
                from_chat_id=CHANNEL_ID,
                message_id=video_message_id
            )
        except Exception as e:
            await message.answer("❌ Bunday raqamli video topilmadi yoki xatolik yuz berdi.")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
