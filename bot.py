from aiogram.dispatcher.filters import Command, Text, CommandStart
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InputFile, Message

from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

from db import Database
import config as cfg


class ClientState(StatesGroup):
    StateDeleteMessage = State()


storage = MemoryStorage()

bot = Bot(token=cfg.TOKEN)
dp = Dispatcher(bot, storage=storage)
db = Database()
lang = 'ru'


# -------------------------------------------------------------------------------------------------

@dp.message_handler(CommandStart())
async def start(message: Message, state: FSMContext):
    db.connect()
    if not db.exit_user(message.from_user.id):
        db.connect()
        db.insert_user(message.from_user.id)
        global lang
    else:
        db.connect()
        lang = db.get_lang(message.from_user.id)

    with open('photo_2023-11-03_03-33-28.jpg', 'rb') as photo:
        await db.insert_state(state, await bot.send_photo(message.chat.id, InputFile(photo),
                                                          caption=_('Привет! Это бот шопа Fb аккаунтов Traffic Force',
                                                                    lang),
                                                          reply_markup=nav.main_menu(lang)), 'message_id_1')

@dp.callback_query_handler(text_contains="lang_")
async def lang_(callback: types.CallbackQuery, state: FSMContext) -> None:
    db.connect()
    if "lang_ru" in callback.data:
        save_lang = db.set_lang(callback.from_user.id, 'ru')
        await db.insert_state(state, await callback.message.answer(_('Вы выбрали русский язык', save_lang), ),
                              'message_id_0')
    else:
        save_lang = db.set_lang(callback.from_user.id, 'en')
        await db.insert_state(state, await callback.message.answer(_('You have chosen english language', save_lang), ),
                              'message_id_0')
    await bot.delete_message(callback.from_user.id, await db.get_state(state, 'message_id_1'))


# ---------------------------- dop_menu ---------------------------------------------------------------------
@dp.callback_query_handler(lambda callback_query: callback_query.data == "main_menu_1")
async def main_menu(callback: types.CallbackQuery, state: FSMContext) -> None:
    db.connect()
    await db.insert_state(state, await callback.message.answer(_('Воспользуйтесь меню', lang),
                                                               reply_markup=nav.dop_menu(
                                                                   db.get_lang(callback.from_user.id))), 'message_id_2')
    await bot.delete_message(callback.from_user.id, await db.get_state(state, 'message_id_1'))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
