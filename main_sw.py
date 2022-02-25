from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from commands_sw import *



updater = Updater('5123962439:AAEtoNbq4uXEEiaxKuDThff6prH7gnQYpoA')

updater.dispatcher.add_handler(CommandHandler('hello', hello_command))
updater.dispatcher.add_handler(CommandHandler('m', play_man))
updater.dispatcher.add_handler(CommandHandler('b', play_bot))
updater.dispatcher.add_handler(MessageHandler(Filters.text, input_handler))


print('server start')

updater.start_polling()
updater.idle()
