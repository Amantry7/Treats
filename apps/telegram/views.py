from django.shortcuts import render
from django.conf import settings 
from telebot import TeleBot, types
from .models import TelegramUser
from config import token, admin

# Создаем объект бота и группу
bot = TeleBot(token, threaded=False)
admin = admin  # Переименовал переменную, чтобы избежать конфликта имен

@bot.message_handler(commands=['start'])
def start(message: types.Message):
    TelegramUser.objects.get_or_create(
        username=message.from_user.username,
        id_user=message.from_user.id,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
    )
    bot.send_message(message.chat.id, f'Салам {message.from_user.full_name}')

class Mail:
    def __init__(self):
        self.description = None

mail = Mail()

def get_text(message):
    bot.send_message(admin, message)  # Исправил на group_id

def get_text_doctor(message, id):
    bot.send_message(id, message)

@bot.message_handler(func=lambda message: True)
def echo(message: types.Message):
    bot.send_message(message.chat.id, "Я вас не понял")

# Добавим запуск бота
if __name__ == "__main__":
    bot.polling(none_stop=True)
