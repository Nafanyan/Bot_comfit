from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters,ConversationHandler
from logging_sw import *
from random import randint


# def mod_msg(Update, context: CallbackContext):
#     chat = update.effective_chat
#     text=Update.message.text
#     return text
  

def hello_command(update: Update, context: CallbackContext):
    # log_sw(update, context)
    update.message.reply_text(f'Hello {update.effective_user.first_name}\n''I am sweeting sweet bot, will we play \n/yes\n/no\n')
  

def exit_command(update: Update, context: CallbackContext):
    # log_sw(update, context)
    update.message.reply_text(f'Sorry,Bay')

def game_command(update: Update, context: CallbackContext):
   # log_sw(update, context)
    update.message.reply_text(f'Ok, \n/newgame\n/resume\n')


def set_play(update: Update, context: CallbackContext):
    update.message.reply_text(f'Who will start first\n if you press \n/1,\n if me press\n/2\n ')
    msg=update.message.text
    player=(msg)
    update.message.reply_text(f'We have now {sweets} sweets\n, you can take the maximum {max_sweets}')    

def play1_command(update: Update, context: CallbackContext):
    global sweets
    global max_sweets
    global sweets_count
    sweets=100
    max_sweets=28
    sweets_count=int()
    res_sweets=int()
    
    
    while sweets>=0:
        
        update.message.reply_text(f'How many sweets will you take')
        msg=(update.message.text)
        sweets_count=msg
        sweets-=sweets_count
        update.message.reply_text(f'There are some sweets left {sweets}')
        player=(play2_command(update, context))       
        
def play2_command(update: Update, context: CallbackContext):
    sweets=100
    max_sweets=28
    sweets_count=int()
    while sweets>=0:     
        
        sweets_count = randint(1, max_sweets)
        update.message.reply_text(f'Ok,i took {sweets_count}')
        sweets-=sweets_count
        update.message.reply_text(f'There are some sweets left {sweets}')
        player=(play1_command(update, context))





# def get_sweets(player):
#     while True:
#         if player == 1:
#             sweets_count = int(input(f'сколько взять конфет {player}:'))
#         else:
#             sweets_count = randint(1, sweets)
#             print(f' бот взял: {sweets_count}')
#         if sweets_count <= max_sweets:
#             return sweets_count


# while True:
#     print(f'сейчас конфет {sweets}')
#     sweets -= get_sweets(player)
#     if sweets <= 0:
#         if player==1:
#             print(f'Победил игрок{player}')
#             break
#         elif player==2:
#             print('Победил бот')
#     player = 2 if player == 1 else 1