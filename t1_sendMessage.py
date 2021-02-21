__autor__ = "Lautaro Linquiman"
"""
Descripcion: Creando bot de telegram envia mensages cada 5 segundos.

www.tutorialdeprogramacion.com
Github: http://github.com/ymil
Curso: https://tutorialdeprogramacion.com/minicurso-crear-un-bot-de-telegram-con-python/
Entrada blog: https://tutorialdeprogramacion.com/1-creando-bot-de-telegram-con-python-hola-mundo/
Video tutorial: https://www.youtube.com/watch?v=vcFYe-DyAyA

Gists con trampitas: https://gist.github.com/Ymil/3f6620db40ce7151f070d5e807eaa590
"""

import telegram
import time
bot_token = ''
chat_id = ''

bot = telegram.bot(token=bot_token)

print(bot.get_me())

while True:
    bot.send_message(chat_id=chat_id, text='Hola mundo, este es nuestro primer programa con la api de telegram')
    time.sleep(5)