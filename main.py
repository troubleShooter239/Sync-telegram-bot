# ТГ Бот
# Умения
# - Парсирование Markdown
# Функции: 
# 1 - /start - Привет, {username} 
# 2 в кости играт
# 3 отправить рандомный стикер из набора
# 4 генератор рандомных чисел
# 5 скинуть ролик с ютуба по запросу
# Зависимости:
# - pytelegrambotapi

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.
from telebot.types import Message
import telebot

API_TOKEN = '7113390199:AAGl_FzJs1zyFtsYkelcK97IRjnRyTsWhaE'

bot = telebot.TeleBot(API_TOKEN, 'Markdown')

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message: Message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

@bot.message_handler(commands=['dice'])
def play_dice(message: Message):
    bot.send_dice(message.chat.id)
    if message.dice.value > 3:
        bot.send_message(message.chat.id, '>3')
    else: bot.send_message(message.chat.id, '<3')

@bot.message_handler(commands=['sticker'])
def send_random_sticker(message: Message):
    bot.send_sticker(
        message.chat.id, 
        "CAACAgIAAxkBAAJJD2Uv66EG9cvKyu9Y7S0q2aYKsWbuAAKwIgACYDwAAUqO67jfGdyGETAE"
    )

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
