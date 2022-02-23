from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from commands_sw import *



updater = Updater('5123962439:AAEtoNbq4uXEEiaxKuDThff6prH7gnQYpoA')


updater.dispatcher.add_handler(CommandHandler('Hello', hello_command))
updater.dispatcher.add_handler(CommandHandler('No', exit_command))
updater.dispatcher.add_handler(CommandHandler('Yes', game_command))
updater.dispatcher.add_handler(CommandHandler('newgame', set_play))
updater.dispatcher.add_handler(CommandHandler('1', play1_command))
updater.dispatcher.add_handler(CommandHandler('2', play2_command))


print('server start')

updater.start_polling()
updater.idle()