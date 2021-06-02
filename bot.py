from telegram import *
from telegram.ext import *


bot = Bot("API Key")

updater=Updater("API Key",use_context=True)

dispatcher=updater.dispatcher

def test_function(update:Update,context:CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="",
    )

start_value=CommandHandler('motion_detection,test_function')

dispatcher.add_handler(start_value)

updater.start_polling()
