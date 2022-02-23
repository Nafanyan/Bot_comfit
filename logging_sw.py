from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def log_sw(update: Update, context: CallbackContext):
    
    file = open ('users.csv','a')
    file.write(f'{update.effective_user.first_name},{update.effective_user.id},{update.message.text}\n')

    file.close()

