
import asyncio
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery
)

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

rules = """
📜 JEYZEBEL STORE QOIDALARI

1. Xariddan oldin admin bilan bog‘laning.
2. Narx va mahsulotni oldindan aniqlashtiring.
3. To‘lov chekini admin tasdiqlashi kerak.
4. Soxta chek yuborish taqiqlanadi.
5. Hurmat bilan muloqot qiling.
6. Muammo bo‘lsa, admin bilan bog‘laning.

💜 Bizni tanlaganingiz uchun rahmat!
"""

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="👨‍💻 Admin bilan bog‘lanish",
            url="https://t.me/uuuu_17"
        )
    ],
    [
        InlineKeyboardButton(
            text="📜 Qoidalar",
            callback_data="rules"
        )
    ]
])


@dp.message(CommandStart())
async def start(message: Message):
    name = message.from_user.first_name

    await message.answer(
        f"👑 JEYZEBEL STORE\n\n"
        f"Assalomu alaykum, {name}!\n\n"
        f"Botimizga xush kelibsiz! 💜\n\n"
        f"Bu yerda CS2 skinlari haqida ma'lumot "
        f"olishingiz mumkin.\n\n"
        f"Quyidagi tugmalardan foydalaning:",
        reply_markup=keyboard
    )


@dp.callback_query(F.data == "rules")
async def show_rules(callback: CallbackQuery):
    await callback.message.answer(rules)
    await callback.answer()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN topilmadi!")
    asyncio.run(main())
