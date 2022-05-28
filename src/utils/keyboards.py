from typing import KeysView
import emoji
from telebot import types


def create_keyboard(*keys, row_width=2, resize_keyboard=True):
    """
    Create a keyboard with the given keys
    e.g. Keys= ['key1', 'key2', 'key3']
    """
    markup = types.ReplyKeyboardMarkup(
        row_width=row_width,
        resize_keyboard=resize_keyboard
        )
    keys=map(emoji.emojize,keys)
    buttons = map(types.KeyboardButton,keys)
    markup.add(*buttons)
    return markup
