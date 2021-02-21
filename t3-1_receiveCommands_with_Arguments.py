__autor__ = "Lautaro Linquiman"
"""
Descripcion: Creando un bot en telegram que recibe comandos con argumentos y envia respuestas.

www.tutorialdeprogramacion.com
Github: http://github.com/ymil
Curso: https://tutorialdeprogramacion.com/minicurso-crear-un-bot-de-telegram-con-python/
Entrada blog: https://tutorialdeprogramacion.com/creando-bot-de-telegram-comandos-con-argumentos/
Video tutorial: https://www.youtube.com/watch?v=2dkPyedcvtc

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

def argumentos(update, context):
    args = context.args
    chat_id = update.message.chat_id 
    if(len(args) > 0):
        if( args[0].lower() == "hola"):
            msg = 'Hola! ¿Como estas?'
        else:
            msg = 'Hola, no entendi! Prueba decirme hola!'
    else:
        msg = 'Debes pasarme un argumento'
    
    context.bot.sendMessage(chat_id=chat_id, text=msg)

stickers = {
    'chanchito': 'chanchito_sticker.png',
    'freddy': 'freddy-sticker.png'
}

def sticker(update, context):
    chat_id = update.message.chat_id
    args = context.args
    if len(args) == 0:
        msg = """
            Necesito que me digas que sticker quieres
            Utiliza /listaStickers
        """
        context.bot.sendMessage(chat_id=chat_id, text=msg)
        return

    name_sticker = args[0]
    if name_sticker in sticker:
        name_file = sticker[name_sticker]
        with open(name_file, 'rb') as sticker_file:
            context.bot.sendSticker(chat_id=chat_id, sticker=sticker_file,
            caption='Hola, te envio este sticker')
    else:
        msg = """
            Lo siento, no tengo ese sticker.
            Utiliza /listaStickers"""
        context.bot.sendMessage(chat_id=chat_id, text=ms)

def listaStickers(update, context):
    chat_id = update.message.chat_id
    msg = "Estos son mis stickers\n"
    for sticker_ in stickers.keys():
        msg += sticker_+"\n"
    msg += "Prueba con /sticker chanchito"
    context.bot.sendMessage(chat_id=chat_id, text=msg)

start_handler = CommandHandler('start', start)
argumentos_handler = CommandHandler('argumentos', argumentos)
sticker_handler = CommandHandler('sticker', sticker)
listaStickers_handler = CommandHandler('listaStickers', listaStickers)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(argumentos_handler)
dispatcher.add_handler(sticker_handler)
dispatcher.add_handler(listaStickers_handler)

updater.start_polling()