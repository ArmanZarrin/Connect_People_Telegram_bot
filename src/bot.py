import os
import emoji
import telebot
from loguru import logger

from src.utils.io import write_json
from src.constants import keyboards
from telebot import types

markup = types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
itembtn1 = types.KeyboardButton('Connect')
itembtn2 = types.KeyboardButton('Setting')
itembtn3 = types.KeyboardButton('empty')
markup.add(itembtn1, itembtn2, itembtn3)


class Bot:
    """
    Template code for Telegram bot
    """
    def __init__(self):
        self.bot = telebot.TeleBot(os.environ['MyToken']) # You can set parse_mode by default. HTML or MARKDOWN
        self.send_welcome=self.bot.message_handler(commands=['start', 'help'])(self.send_welcome)
        self.echo_all=self.bot.message_handler(func=lambda message: True)(self.echo_all)

    def run(self):
        logger.info('Bot is running ...')
        self.bot.infinity_polling()

    def send_welcome(self,message):
    	self.bot.reply_to(message, "Howdy, how are you doing?")


    def echo_all(self,message):
        write_json(message.json,'src/data/message.json')
        print(emoji.demojize(message.text))
        self.bot.send_message(
            message.chat.id,message.text,
            reply_markup= keyboards.main
        )


if __name__ == '__main__':
    logger.info('Bot started!')
    bot=Bot()
    bot.run()
