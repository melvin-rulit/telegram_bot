from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from translation import _
from aiogram import types


def main_menu(lang):
    button1 = InlineKeyboardButton(_('📱 Основное меню', lang), callback_data="main_menu_1")
    button2 = InlineKeyboardButton(_('📖 Правила&соглашения', lang), callback_data="button1")
    button3 = InlineKeyboardButton(_('🇷🇺', lang), callback_data="lang_ru")
    button4 = InlineKeyboardButton(_('🇺🇸', lang), callback_data="lang_en")

    row1 = [button1]
    row2 = [button2]
    row3 = [button3, button4]

    markup = InlineKeyboardMarkup(inline_keyboard=[row1, row2, row3])

    return markup


def dop_menu(lang):
    button1 = types.KeyboardButton(_('🛍 Товары', lang))
    button2 = types.KeyboardButton(_('📦 Категории', lang))
    button3 = types.KeyboardButton(_('📱 Контакты', lang))
    button4 = types.KeyboardButton(_('🛒 Мои покупки', lang))
    button5 = types.KeyboardButton(_('🔎 Поиск товаров', lang))
    button6 = types.KeyboardButton(_('📖 Правила&Соглашение', lang))
    button7 = types.KeyboardButton(_('💰 Баланс профиля', lang))
    button8 = types.KeyboardButton(_('📺 О боте', lang))
    button9 = types.KeyboardButton(_('🇷🇺', lang))
    button10 = types.KeyboardButton(_('🇺🇸', lang))

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    row1 = [button1, button2]
    row2 = [button3, button4]
    row3 = [button5, button6]
    row4 = [button7, button8]
    row5 = [button9, button10]

    keyboard.add(*row1)
    keyboard.add(*row2)
    keyboard.add(*row3)
    keyboard.add(*row4)
    keyboard.add(*row5)

    return keyboard


def tovar_list(lang):
    button1 = InlineKeyboardButton(_('Товар 1', lang), callback_data="main_menu")
    button2 = InlineKeyboardButton(_('Товар 1', lang), callback_data="button1")
    button3 = InlineKeyboardButton(_('Товар 1', lang), callback_data="lang_ru")
    button4 = InlineKeyboardButton(_('Товар 1', lang), callback_data="lang_en")
    button5 = InlineKeyboardButton(_('Товар 1', lang), callback_data="lang_en")
    button6 = InlineKeyboardButton(_('⬅', lang), callback_data="lang_en")
    button7 = InlineKeyboardButton(_('Страница 1/1', lang), callback_data="lang_en")
    button8 = InlineKeyboardButton(_('📱 Открыть меню', lang), callback_data="main_menu_1")

    row1 = [button1]
    row2 = [button2]
    row3 = [button3]
    row4 = [button4]
    row5 = [button5]
    row6 = [button6, button7]
    row7 = [button8]

    list_tovar = InlineKeyboardMarkup(inline_keyboard=[row1, row2, row3, row4, row5, row6, row7])
    return list_tovar
def category_list(lang):
    button1 = InlineKeyboardButton(_('📱 Открыть меню', lang), callback_data="main_menu_1")

    row1 = [button1]

    category_tovar = InlineKeyboardMarkup(inline_keyboard=[row1])
    return category_tovar

def contact(lang):
    button1 = InlineKeyboardButton(_('📱 Открыть меню', lang), callback_data="main_menu_1")

    row1 = [button1]

    contact_list = InlineKeyboardMarkup(inline_keyboard=[row1])
    return contact_list

def balance(lang):
    button1 = InlineKeyboardButton(_('📱 Открыть меню', lang), callback_data="main_menu_1")
    button2 = InlineKeyboardButton(_('🤑 Пополнить баланс', lang), callback_data="top_balance")

    row1 = [button1]
    row2 = [button2]

    balance_list = InlineKeyboardMarkup(inline_keyboard=[row1, row2])
    return balance_list

def top_balance(lang):
    button1 = InlineKeyboardButton(_('📱 Открыть меню', lang), callback_data="main_menu_1")
    button2 = InlineKeyboardButton(_('👀 Ввести ваучер-код', lang), callback_data="voucher")

    row1 = [button1]
    row2 = [button2]

    balance_list = InlineKeyboardMarkup(inline_keyboard=[row1, row2])
    return balance_list

def purchases(lang):
    button1 = InlineKeyboardButton(_('📱 Открыть меню', lang), callback_data="main_menu_1")

    row1 = [button1]

    balance_list = InlineKeyboardMarkup(inline_keyboard=[row1])
    return balance_list

def about_bot(lang):
    button1 = InlineKeyboardButton(_('Перейти к боту', lang), callback_data="df")

    row1 = [button1]

    balance_list = InlineKeyboardMarkup(inline_keyboard=[row1])
    return balance_list