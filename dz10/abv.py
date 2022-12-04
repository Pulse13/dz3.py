# from telegram import Bot
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# bot = Bot(token='5954216149:AAHzUirXLjojp9C1X4-FDTfIgnUI8oByA0E')
# updater = Updater(token='5954216149:AAHzUirXLjojp9C1X4-FDTfIgnUI8oByA0E')
# dispahather = updater.dispatcher 


# def start(update, context):
#     context.bot.send_message(update.effective_chat.id, 'Привет\nВведи текст, а я удалю все слова, содержащие абв')


# def abv(update, context):
#     text = update.message.text
#     if 'абв' in text:
#         text1 = list(filter(lambda x: not 'абв' in x, text.split()))
#         text1 = ' '.join(text1)
#         context.bot.send_message(update.effective_chat.id, text1)
#         context.bot.send_message(update.effective_chat.id, 'Готово!')
#     else:
#         context.bot.send_message(update.effective_chat.id, 'Введи текст, содержащий абв')
#         return
   

# start_handler = CommandHandler('Start', start) 
# message_handler = MessageHandler(Filters.text, abv )


# dispahather.add_handler(start_handler) 
# dispahather.add_handler(message_handler) 


# updater.start_polling()
# updater.idle()