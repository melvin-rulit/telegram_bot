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


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
