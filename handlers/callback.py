from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#@dp.message_handler(commands=['quiz'])
async def quiz_2(callback: types.CallbackQuery):
    quiestion = "вы поставите 10?"
    answers = [
        "нет",
        "конечно",
    ]

    # await bot.send_poll()
    await callback.message.answer_poll(
        question=quiestion,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="сами сказали",
        open_period=10000000000000000,
    )

async def quiz_3(callback: types.CallbackQuery):
    await callback.message.answer("Это все!")


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="next_button_1")
    dp.register_callback_query_handler(quiz_3, text="next_button_2")