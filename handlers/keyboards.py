from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    # row_width=1
)

start_button = KeyboardButton("/start")
quiz_button = KeyboardButton("/quiz")
mem_button = KeyboardButton("/mem")
share_location = KeyboardButton("share_location", request_location=True)
share_contact = KeyboardButton("share_contact", request_contact=True)

start_markup.add(
    start_button,
    quiz_button,
    mem_button,
    share_location,
    share_contact
)