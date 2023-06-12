from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from decouple import config
import logging

TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message) -> None:
    await bot.send_message(message.chat.id, f"hello {message.from_user.full_name}")


@dp.message_handler(commands=['mem'])
async def start_command(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSgBFI2PTnE5ay-YrWmswhbpBQ2RXZn6MVqzw&usqp=CAU")



@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message) -> None:
    markup = InlineKeyboardMarkup()
    next_button = InlineKeyboardButton("NEXT", callback_data="next_button_1")
    markup.add(next_button)

    quiestion = "сколько весит синий кит?"
    answers = [
        "16 тон",
        "14кг",
        "150 тон",
        "96 слонов",
        "56 тон",
        "я не знаю",
    ]

    # await bot.send_poll()
    await message.answer_poll(
        question=quiestion,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="да, можно было и не знать",
        open_period=4,
        reply_markup=markup
    )


@dp.callback_query_handler(text="next_button_1")
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


@dp.message_handler(content_types=['text'])
async def echo(message: types.Message) -> None:
    await bot.send_message(message.chat.id, message.text)


@dp.message_handler(content_types=['sticker'])
async def echo(message: types.Message) -> None:
    await bot.send_sticker(message.chat.id, message.sticker.file_id)


@dp.message_handler()
async def echo(message: types.Message):
    if type(message) == int:
        square = message ** 2
        await bot.send_message(square)
    await bot.send_message(message.from_user.id, message.text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)