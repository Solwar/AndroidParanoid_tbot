import logging
import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

#proxy setting



#logs дата время--- уровень важности события -- само сообщение события
logging.basicConfig(format ='%(asctime)s - %(levelname)s - %(message)s',
                    #тип логирования:
                    level=logging.INFO, 
                    filename='bot.log'
                    )
'''
def greet_user(bot, update):
        print ('called /allo')
        update.message.reply_text('ALLO KISUN!! HOW ARE U?')


def echo(bot, update):
    print(update.message)
    user_text = update.message.text
    logging.info(f"User: {update.message.chat.first_name}, Chat ID: {update.message.chat.id}, Message: {update.message.text}")
    print(user_text)

    if user_text == 'genji':
        update.message.reply_text('ryujin no ken wo kurae!!!!')
    else:
        update.message.reply_text('DUPLICATING: '+user_text)
'''
def greet_user(update, context):
        print ('called /allo')
        update.message.reply_text('ALLO KISUN!! HOW ARE U?')


def echo(update, context):
    print(update.message)
    user_text = update.message.text
    logging.info(f"User: {update.message.chat.first_name}, Chat ID: {update.message.chat.id}, Message: {update.message.text}")
    print(user_text)

    if user_text == 'genji':
        update.message.reply_text('ryujin no ken wo kurae!!!!')
    else:
        update.message.reply_text('DUPLICATING: '+user_text)
#главная функция для взаимодейсвия с ботом
def main():
    #объект класс апдейтер который будет проверять сообщения боту по указанному ключу
    paranoidBot = Updater(settings.API_KEY, use_context=True, request_kwargs= settings.PROXY)

    
    #тупой препод не заметил что info нужно именно в lower case писать
    logging.info('Started bot')

    #диспетчер принимает сообщения, и распределяет их, например в команд хэндлер
    dp = paranoidBot.dispatcher

    # регистрируем процедуру start как обработчик команды start
    dp.add_handler(CommandHandler('allo', greet_user))
    # регистрируем процедуру echo как обработчик текстового сообщения
    dp.add_handler(MessageHandler(Filters.text, echo))
    
    
    paranoidBot.start_polling()# начать регулярную проверку сообщений боту
    paranoidBot.idle() #работа до принудительной остановки
# в ботах используется собыйтийная модель


main()