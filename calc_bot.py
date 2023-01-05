import sys
import time
import telepot

from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.loop import MessageLoop

numbers = {}
cntr = 0
flagOfDo = 0
result = 1


def handle(msg):
    global flagOfLevel

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='*', callback_data='2')], [InlineKeyboardButton(text='%', callback_data='1')],
        [InlineKeyboardButton(text='+', callback_data='3')], [InlineKeyboardButton(text='-', callback_data='4')]
    ])
    content_type, chat_type, chat_id = telepot.glance(msg)
    #    print(msg)

    global flagOfDo
    global cntr
    global result

    if msg['text'] == '/start':
        bot.sendMessage(chat_id, 'Привет! Я простой калькулятор, написанный на Python. Введи первую цифру.')
        flagOfDo = 1
        cntr = 0
        return

    numbers[cntr] = int(msg['text'])

    if cntr == 1:
        bot.sendMessage(chat_id, 'выбери операцию', reply_markup=keyboard)
        cntr = 0
        result = 0

    if result == 1:
        if flagOfDo == 1:
            bot.sendMessage(chat_id, 'Введи вторую цифру ...')
            flagOfDo = 0
            cntr = 1
            return

        else:
            bot.sendMessage(chat_id, 'Введи первую цифру ...')
            flagOfDo = 1
            return


#     bot.sendMessage(chat_id, message)


def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    #    print(msg)
    global result
    global numbers

    if query_data == '0':
        bot.sendMessage(from_id, 'Нажми /start чтобы начать заново', reply_markup=keyboard)
        numbers = {}

    elif query_data == '1':
        bot.sendMessage(from_id, 'результат: ' + str(numbers[0]) + ' % ' + str(numbers[1]) + '=' + str(
            numbers[0] / numbers[1]))
        bot.sendMessage(from_id, 'Нажми /start чтобы начать заново')
        result = 1
        numbers = {}

    elif query_data == '2':
        bot.sendMessage(from_id, 'результат: ' + str(numbers[0]) + ' * ' + str(numbers[1]) + '=' + str(
            numbers[0] * numbers[1]))
        bot.sendMessage(from_id, 'Нажми /start чтобы начать заново')
        result = 1
        numbers = {}

    elif query_data == '3':
        bot.sendMessage(from_id, 'результат: ' + str(numbers[0]) + ' + ' + str(numbers[1]) + '=' + str(
            numbers[0] + numbers[1]))
        bot.sendMessage(from_id, 'Нажми /start чтобы начать заново')
        result = 1
        numbers = {}

    elif query_data == '4':
        bot.sendMessage(from_id, 'результат: ' + str(numbers[0]) + ' - ' + str(numbers[1]) + '=' + str(
            numbers[0] - numbers[1]))
        bot.sendMessage(from_id, 'Нажми /start чтобы начать заново')
        result = 1
        numbers = {}
    else:
        bot.sendMessage(from_id, 'попробуй заново !!!')
        result = 1
        bot.sendMessage(from_id, 'Нажми /start чтобы начать заново')


bot = telepot.Bot('5657707119:AAEsQLhS4WmdODy4ueFdKu-jAshCeSWjGPk')
MessageLoop(bot, {'chat': handle,
                  'callback_query': on_callback_query}).run_as_thread()
print('Listening ...')

while 1:
    time.sleep(10)