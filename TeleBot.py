import telebot
from telebot import types,util
import os
import datetime
import sys

token = ''
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def choose_mod(message):
    if message.text in ["/start","/help"]:
        greeting(message)
    else:
        names_of_button = ['Текущее состояние картинок',
                           'Оставшееся время до конца',
                           'Пришли мне результаты измерения']
        keyboard = types.InlineKeyboardMarkup()
        for num,func in enumerate(names_of_button):
            keyboard.row(types.InlineKeyboardButton(text= func ,callback_data = 'func'+str(num)))
        bot.send_message(message.chat.id,text="Что желаете?",reply_markup=keyboard)

def greeting(message):
    text="Привет! Просто введи любое текстовое сообщение и получишь меню"
    bot.send_message(message.chat.id,text=text)

def choose_pics(message):
    global directory_of_measurements
    files=list()
    keyboard = telebot.types.InlineKeyboardMarkup()
    for file in os.listdir(directory_of_measurements):
        if file.split('.')[-1] in ["jpg","png"]:
            files.append(file)
    for file in files:
        keyboard.row(telebot.types.InlineKeyboardButton(text= file.split(".")[0],callback_data=file))
    bot.send_message(message.chat.id,text="Выберите картинку",reply_markup=keyboard)


def send_time(message):
    global directory_of_measurements
    for file in os.listdir(directory_of_measurements):
        if file == 'time.txt':
            f = open(directory_of_measurements+"/"+file, 'r')
            time=f.readline().split('\n')[0]
            bot.send_message(message.chat.id,text ="До конца измерений осталось: " + time)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    global directory_of_measurements
    functions = [choose_pics,send_time,send_result]
    numbers = ['func'+str(i) for i in range(len(functions))]
    if call.message:
        if call.data.split('.')[-1] in ["jpg","png"]:
            f = open(directory_of_measurements+"/"+call.data, 'rb')
            bot.send_photo(call.message.chat.id, f, caption= call.data)
        if call.data in numbers:
            functions[int(call.data.split('func')[1])](call.message)

def send_result(message):
    global directory_of_measurements
    # надо придумать что сюда
    bot.send_message(message.chat.id,text = "Конечно, как только, так сразу")


if __name__=='__main__':
    for variable in sys.argv:
        directory_of_measurements = variable
    bot.polling(none_stop=True)

"""контроль скрипта через ноутбук, нужен для bot=True
import subprocess
directory_name = '/home/ivan/pic'
args = ['python3','bot2.py',directory_name]
process= subprocess.Popen(args, stdout=subprocess.PIPE)
process.terminate()
"""
