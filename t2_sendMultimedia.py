__autor__ = "Lautaro Linquiman"
"""
Descripcion: Creando bot de telegram envia contenidos multimedia.

www.tutorialdeprogramacion.com
Github: http://github.com/ymil
Curso: https://tutorialdeprogramacion.com/minicurso-crear-un-bot-de-telegram-con-python/
Entrada blog: https://tutorialdeprogramacion.com/python-telegram-bot-cap-2-como-enviar-un-archivos-multimedia-con-un-bot-de-telegram/
Video tutorial: https://www.youtube.com/watch?v=2719DPBL9ao

Gists con trampitas: https://gist.github.com/Ymil/3f6620db40ce7151f070d5e807eaa590
"""

import telegram
import time

bot_token = ''
chat_id = ''

bot = telegram.Bot(token=bot_token)

with open('photo.png', 'rb') as photo_file:
    bot.sendPhoto(chat_id=chat_id,
        photo=photo_file,
        caption='Hola, te envio esta imagen')

with open('audio.ogg', 'rb') as audio_file:
    bot.sendVoice(chat_id=chat_id,
        voice=audio_file,
        caption='Hola, te envio este audio, escuchalo!')

with open('video.mp4', 'rb') as video_file:
    bot.sendVideo(chat_id=chat_id,
        video=video_file,
        caption='Hola, te envio este video, miralo!')

