from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token="5837924782:AAEfJW_Z5PFB1Ws9FrZoD1mzXztldcsFz4Y")
dp = Dispatcher(bot=bot, storage=storage)