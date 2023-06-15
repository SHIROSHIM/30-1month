from aiogram import types, Dispatcher
from config import bot


# @dp.message_handler(content_types=['text'])
async def echo_text(message: types.Message) -> None:
    bad_words = ['дурак', 'html', 'js']
    for word in bad_words:
        if word in message.text.lower().replace(" ", ""):
            await message.delete()
            await message.answer(
                f"Не матерись @{message.from_user.username}\n"
                f"сам ты {word}"
            )

    if message.text.startswith('.'):
        await message.pin()

    if message.text == "dice":  # 🎲🎯🎰🎳🏀⚽️
        a = await message.answer_dice()


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo_text, content_types=['text'])