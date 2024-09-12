from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import *

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = KeyboardButton(text='Рассчитать')
button_2 = KeyboardButton(text='Информация')
button_3 = KeyboardButton(text='Купить')
button_4 = KeyboardButton(text='Регистрация')
kb.add(button_1)
kb.add(button_2)
kb.add(button_3)
kb.add(button_4)

inline_kb = InlineKeyboardMarkup()
inline_button_1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
inline_button_2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
inline_kb.add(inline_button_1)
inline_kb.add(inline_button_2)

buy_inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=product_list[0], callback_data='product_buying')],
        [InlineKeyboardButton(text=product_list[1], callback_data='product_buying')],
        [InlineKeyboardButton(text=product_list[2], callback_data='product_buying')],
        [InlineKeyboardButton(text=product_list[3], callback_data='product_buying')]
    ]
)
