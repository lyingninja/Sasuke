from telegram.ext import Updater
from gtts import gTTS
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
updater = Updater(token='', use_context=True)
dispatcher = updater.dispatcher
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!I will copy all your text messages")
    dispatcher.add_handler(echo_handler)
from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()
def echo(update, context):
    #context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
    text = update.message.text
    tts = gTTS(text=text)
    tts.save('hello.mp3')
    context.bot.sendAudio(chat_id=update.effective_chat.id,audio = 'hello.mp3')

from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
#dispatcher.add_handler(echo_handler)
def stop(update,context):
   context.bot.send_message(chat_id=update.effective_chat.id, text="I won't say anything from now onwards")
   dispatcher.remove_handler(echo_handler)
stop_handler = CommandHandler('stop', stop)
dispatcher.add_handler(stop_handler)
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)
