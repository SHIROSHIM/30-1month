from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text
from config import bot, dp
from keyboards import start_markup
from DataBase.database import sql_command_random
import parser
from aiogram.types import ParseMode

async def start_command(message: types.Message) -> None:
    await bot.send_message(message.chat.id,
                           f"Салалекум хозяин {message.from_user.full_name}",
                           reply_markup=start_markup)

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


# @dp.message_handler(commands=['mem'])
async def photo(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
            photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSgBFI2PTnE5ay-YrWmswhbpBQ2RXZn6MVqzw&usqp=CAU")

async def get_random_user(message: types.Message) -> None:
    random_user = await sql_command_random()
    await message.answer_photo(random_user[-1],
                                   caption=f"{random_user[3]} {random_user[4]} "
                                           f"{random_user[5]} {random_user[6]}"
                                           f"\n\n{random_user[2]}")


#@dp.message_handler()
async def echo(message: types.Message):
    if type(message) == int:
            square = message ** 2
            await bot.send_message(square)
    await bot.send_message(message.from_user.id, message.text)

async def get_news(message: types.Message) -> None:
    news = parser()
    for i in news:
        await message.answer_photo(
            i['image'],
            caption=f"<b>{i['time']}</b>\n"
                    f"<a href='{i['url']}'>{i['title']}</a>\n",
            reply_markup=InlineKeyboardMarkup().add(
                InlineKeyboardButton("Смотреть", url=i['url'])
            ),
            parse_mode=ParseMode.HTML
        )


def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(photo, commands=['mem'])
    dp.register_message_handler(get_random_user, Text(equals="get", ignore_case=True))
    dp.register_message_handler(get_news, commands=['news'])
