from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.error import TelegramError
import telegram.ext
import logging
from uuid import uuid4
import os

TOKEN = os.environ['token']

# Construct Telegram updater and dispatcher objects
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
job_queue = updater.job_queue

# Set logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(update, context):
    text = "Hello fellow Garudian! I am still a work in progress, so please treat me nicely"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

def get_uhms_link(update, context):
    text = "Here is the uhms link: https://uhms.nus.edu.sg"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

def get_meal_credits_link(update, context):
    text = "Here is the link to check your meal credits: https://aces.nus.edu.sg/Prjhml/login.do" 
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

start_handler = CommandHandler('start', start)
uhms_link_handler = CommandHandler('get_uhms_link', get_uhms_link)
meal_credits_handler = CommandHandler('get_meal_credits_link', get_meal_credits_link)
unknown_handler = MessageHandler(Filters.command, unknown)

# Note to self: order of adding the handlers are important
dispatcher.add_handler(start_handler)
dispatcher.add_handler(uhms_link_handler)
dispatcher.add_handler(meal_credits_handler)
dispatcher.add_handler(unknown_handler)

PORT = int(os.environ.get('PORT', '8443'))

if __name__ == "__main__":
    # updater.start_polling() # Use on local
    updater.start_webhook(listen="0.0.0.0", # Use on web server
                        port=PORT,
                        url_path=TOKEN)
    updater.bot.set_webhook("https://hidden-anchorage-87038.herokuapp.com/" + TOKEN)
    updater.idle()