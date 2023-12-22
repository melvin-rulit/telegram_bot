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












if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
