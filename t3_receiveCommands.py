__autor__ = "Lautaro Linquiman"
"""
Descripcion: Creando bot de telegram recibe comandos y envia respuestas.

www.tutorialdeprogramacion.com
Github: http://github.com/ymil
Curso: https://tutorialdeprogramacion.com/minicurso-crear-un-bot-de-telegram-con-python/
Entrada blog: https://tutorialdeprogramacion.com/3-creando-bot-de-telegram-con-python-respondiendo-comandos/
Video tutorial: https://www.youtube.com/watch?v=4bbV7z96JJY

Gists con trampitas: https://gist.github.com/Ymil/3f6620db40ce7151f070d5e807eaa590
"""

from telegram.ext import Updater
from telegram.ext import CommandHandler

bot_token = ''

updater = Updater(token=bot_token, user_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    chat_id = update.message.chat_id

    first_name = update.message.from_user.first_name
    msg = f'Hola {first_name}, bienvenido a nuestro bot'

    context.bot.sendMessage(chat_id=chat_id, text=msg)

def sticker(update, context):
    chat_id = update.message.chat_id

    with open('sticker.png', 'rb') as sticker_file:
        context.bot.sendSticker(chat_id=chat_id, sticker=sticker_file,
        caption='Hola, te envio este sticker')

def photo(update, context):
    chat_id = update.message.chat_id

    with open('photo.png', 'rb') as photo_file:
        context.bot.sendPhoto(chat_id=chat_id, photo=photo_file,
            caption='Hola, te envio esta foto')

start_handler = CommandHandler('start', start)
sticker_handler = CommandHandler('sticker', sticker)
photo_handler = CommandHandler('photo', photo)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(sticker_handler)
dispatcher.add_handler(photo_handler)

updater.start_polling()