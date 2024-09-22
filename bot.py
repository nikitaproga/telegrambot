import config
import asyncio
from random import choice


from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot(config.token)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    text = 'Привет, я ТестБот! Напиши мне что-нибудь, и я это повторю!'
    await bot.reply_to(message, text)


@bot.message_handler(commands=['info'])
async def info_message(message):
    text = '''Команды: 
    /start - Запуск бота
    /fact - Интересный факт'''
    await bot.reply_to(message, text)

@bot.message_handler(commands=['fact'])
async def fact_handler(message):
    fact = choice(["Интересный факт, здесь когда-то был интересный факт", "Одиннадцать процентов людей на земле левши", "Виноград взрывается в микроволновой печи"])
    await bot.reply_to(message, fact)

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)


asyncio.run(bot.polling())