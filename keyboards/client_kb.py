from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

b1 = KeyboardButton("/Режим_работы")
b2 = KeyboardButton("/Расположение")
b3 = KeyboardButton("/Меню")
#b4 = KeyboardButton('Поделиться номером', request_contact=True)
#b5 = KeyboardButton('Отправить где я', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b3).row(b2, b1)