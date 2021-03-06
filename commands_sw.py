from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters,ConversationHandler
from logging_sw import *
from random import randint
from storage_users import*
import work_status_users as wsu
from enum import Enum




global sweets
sweets=100
max_sweets=28

class State(Enum):
    WAIT_COMMAND_USER1 = 1
    NONE = 3

global state 
state = State.NONE


def process_input_man(taken_sweets):
    global sweets
    global max_sweets
    if taken_sweets > max_sweets or taken_sweets> sweets:
        return False
    sweets -= taken_sweets
    return True
   

def bot_action():
    global sweets
    global max_sweets
    if sweets>max_sweets:
        bot_sweets = randint(1, max_sweets)
        sweets -= bot_sweets
        return bot_sweets
    else:
        bot_sweets = randint(1, sweets)
        sweets -= bot_sweets
        return bot_sweets

def input_handler(update: Update, context: CallbackContext):
    id = str(update.effective_user.id)
    global sweets
    global max_sweets
    global state
    if state == State.WAIT_COMMAND_USER1:
        if not process_input_man(int(update.message.text)):
            update.message.reply_text(f'Ты не можешь взять такое количество конфет')
            return

        if sweets <= 0:
            update.message.reply_text(f'Увы, я проиграл')
            state = State.NONE
            # сделал обновление статуса о текущем состоянии конфет
            sweets=100
            status = wsu.read_status(id)
            status['sweet'][0] = sweets
            wsu.change_status(status, id)
        else:
            play_bot(update=update, context=context)

def start(update: Update, context: CallbackContext):
    id = str(update.effective_user.id)
    user_base = read_storage()
    if (not (id in user_base)):
        add_new_user(id)
        wsu.new_user_status(id)

    log_sw(update, context)
    update.message.reply_text(f'Привет  {update.effective_user.first_name} для начала нажмите /start\n')
    global sweets
    if (wsu.check_status('sweet', id)):
        status = wsu.read_status(id)
        status['sweet'][0] = sweets
        wsu.change_status(status, id)
        update.message.reply_text(
            f'Правила игры:\n 1.У нас есть 100 конфет\n 2. Максимально можно взять {max_sweets}\n 3. Кто последний взял тот проиграл \n и последнее кто первый начнет игру, если человек нажмите  /m\n если бот нажмите  /b\n')

    else:
        status = wsu.read_status(id)
        sweets = int(status['sweet'][0])
        update.message.reply_text(f'У тебя есть неоконченная игра последнее количество конфет {sweets} \n'
                                  f'Кто продолжит игру, если человек нажмите  /m\n если бот нажмите  /b\n')


def play_man(update: Update, context: CallbackContext):
    update.message.reply_text(f'Сейчас {sweets}\n Сколько конфет возьмешь?')
    id = str(update.effective_user.id)
    status = wsu.read_status(id)
    status['sweet'][0] = sweets
    wsu.change_status(status, id)
    global state
    state = State.WAIT_COMMAND_USER1

def play_bot(update: Update, context: CallbackContext):
    id = str(update.effective_user.id)
    global sweets
    global state
    bot_sweets = bot_action()
    if sweets <= 0:
        update.message.reply_text(f'Я взял {bot_sweets}, Ты проиграл!')
        # сделал обновление статуса о текущем состоянии конфет
        state =State.NONE
        sweets = 100
        status = wsu.read_status(id)
        status['sweet'][0] = sweets
        wsu.change_status(status, id)
    else:
        update.message.reply_text(f'Хорошо, я взял  {bot_sweets}')        
        play_man(update, context)

