import hashlib
import logging
import random

from aiogram import Bot, Dispatcher, executor
from aiogram.types import InlineQuery, \
    InputTextMessageContent, InlineQueryResultArticle, Message

API_TOKEN = '123:123'  # your telegram bot token

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.inline_handler()
async def inline_echo(inline_query: InlineQuery):
    phrases = ['yes.', 'no.', 'hohoho', 'aaagh']
    choice = random.choice(phrases)
    text = inline_query.query + '<b>\n{}</b>'.format(choice)
    input_content = InputTextMessageContent(text, parse_mode='HTML')
    result_id: str = hashlib.md5(text.encode()).hexdigest()
    thumb = 'https://memepedia.ru/wp-content/uploads/2022/02/hohoho-nou-mem-govorjashchij-ben-768x512.jpg'
    item = InlineQueryResultArticle(
        id=result_id,
        title=inline_query.query or "Ben's answer",
        description=choice,
        input_message_content=input_content,
        thumb_url=thumb
    )
    await inline_query.answer([item], is_personal=True)


@dp.message_handler()
async def any_message_handler(message: Message):
    botname = await bot.get_me()
    await message.answer(
        "This bot can help you find out the answers to your questions.\n"
        "It works automatically, you don't need to add it anywhere.\n"
        f"Simply open any of your chats and type @{botname['username']} + something in the message field. Then tap on a result to send..\n\n"
        f"For example, try <code>@{botname['username']} telegram is good?</code>\n"
        "My repo on github - https://github.com/l1v0n1/ben-talking-bot", parse_mode='HTML')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)