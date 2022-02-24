from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters,ConversationHandler
from logging_sw import *
from random import randint

from enum import Enum

def hello_command(update: Update, context: CallbackContext):
    log_sw(update, context)
    update.message.reply_text(f'Hello {update.effective_user.first_name} press /start\n')



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
    if taken_sweets > max_sweets:
        return False
    sweets -= taken_sweets
    return True

def bot_action():
    global sweets
    global max_sweets
    bot_sweets = randint(1, max_sweets)
    sweets -= bot_sweets
    return bot_sweets

def input_handler(update: Update, context: CallbackContext):
    global sweets
    global max_sweets
    global state
    if state == State.WAIT_COMMAND_USER1:
        if not process_input_man(int(update.message.text)):
            update.message.reply_text(f"Too many sweets to take!")
            return
        if sweets <= 0:
            update.message.reply_text(f"You lost!")
            state = State.NONE
            sweets=100
        else:
            play_bot(update=update, context=context)
    elif state == State.NONE:
        update.message.reply_text(f"Enter you will start the game: man -/m\n or bot- /b\n")


def play_man(update: Update, context: CallbackContext):
    update.message.reply_text(f'We have now {sweets}\n How many sweets will you take?')
    global state
    state = State.WAIT_COMMAND_USER1

def play_bot(update: Update, context: CallbackContext):
    global sweets
    global state
    bot_sweets = bot_action()
    if sweets <= 0:
        update.message.reply_text(f'It took {bot_sweets} Bot lost!!')
        state =State.NONE
        sweets = 100
    else:
        update.message.reply_text(f'Ok, we have now {sweets},\n i took {bot_sweets}')        
        play_man(update, context)

