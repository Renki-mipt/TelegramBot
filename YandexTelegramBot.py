# coding=windows-1251
import telebot
from telebot import types
import random

bot = telebot.TeleBot('6126305664:AAHZlwHK3DZElsv7G2-qQtuU39Iy1w_X3H0')

@bot.message_handler(commands = ['start'])
def start(message):
    try:
        markup = types.InlineKeyboardMarkup(row_width = 3)
        item1 = types.InlineKeyboardButton('Что такое GPT?', callback_data = 'gpt')
        item2 = types.InlineKeyboardButton('История первой любви', callback_data = 'love_story')
        item3 = types.InlineKeyboardButton('В чем разница между SQL и noSQL?', callback_data = 'sql')
        markup.add(item1, item2, item3)
        with open('Start.txt', encoding = 'utf-8', mode = 'r') as myfile:
            bot.send_message(message.chat.id, myfile.read(), reply_markup = markup)
    except Error as e:
        print('Somthing wrong')

@bot.message_handler(commands = ['photo'])
def give_photos(message):
    markup = types.InlineKeyboardMarkup(row_width = 2)
    item1 = types.InlineKeyboardButton('Мой создатель', callback_data = 'selfy')
    item2 = types.InlineKeyboardButton('А это его школа', callback_data = 'school')
    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'Выберите фото, которое хотите посмотреть.', reply_markup = markup)

@bot.message_handler(commands = ['git'])
def give_git(message):
    bot.send_message(message.chat.id, 'https://github.com/Renki-mipt/TelegramBot')

@bot.message_handler(commands = ['hobby'])
def give_hobby(message):
    try:
        with open('Hobby.txt', encoding = 'utf-8', mode = 'r') as myfile:
            bot.send_message(message.chat.id, myfile.read())
    except Error as e:
        print('Somthing wrong')


@bot.callback_query_handler(func = lambda call: True)
def callback(call):
    try:
        if call.message:
            if call.data == 'gpt':
                audio = open('GPT.mp3', 'rb')
                bot.send_audio(call.message.chat.id, audio)
                audio.close()
            elif call.data == 'sql':
                audio = open('SQL_noSQL.mp3', 'rb')
                bot.send_audio(call.message.chat.id, audio)
                audio.close()
            elif call.data == 'love_story':
                audio = open('FirstLove.mp3', 'rb')
                bot.send_audio(call.message.chat.id, audio)
                audio.close()
            elif call.data == 'school':
                photo = open('school.jpg', 'rb')
                bot.send_photo(call.message.chat.id, photo)
                photo.close()
            elif call.data == 'selfy':
                photo = open('selfy.jpg', 'rb')
                bot.send_photo(call.message.chat.id, photo)
                photo.close()
    except Error as e:
        print('Somthing wrong')


@bot.message_handler(content_types = ['text'])
def start(message):
    answers = ['А мне-то откуда знать!?', 'Вот вы лучше спросите это у Друзя - он точно должен знать',
                'Очень хотел бы вам помочь, но сейчас слишком занят. Спросите ещё раз через полчаса']
    texts = ['Как странно, мне такое в голову никогда не приходило', 'Я как раз это же хотел сказать!',
             'Вы так говорите, как будто все знаете', 'Вы поразительно умны!', 'Гениально! Мне тут нечего добавить']
    if message.text != '' and message.text[len(message.text) - 1] == '?':
        bot.send_message(message.chat.id, answers[random.randrange(3)])
    else:
        bot.send_message(message.chat.id, texts[random.randrange(5)])


bot.polling(none_stop = True)

    
