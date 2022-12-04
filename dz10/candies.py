from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from random import randint

bot = Bot(token='5823128192:AAE-XOkumH1yT1mgQ_2j-3htD4H2gnlTVpA')
updater = Updater(token='5823128192:AAE-XOkumH1yT1mgQ_2j-3htD4H2gnlTVpA')
dispahather = updater.dispatcher 


overall_candies = randint(20,150)
max_take = randint(5,10)
count = randint(1,2)


def start(update, context):
    context.bot.send_message(update.effective_chat.id, f'Привет\nВсего {overall_candies} конфет\nЗа ход можно взять не более {max_take} конфет')
    if count == 1:
        context.bot.send_message(update.effective_chat.id,'Я начну 1ым')
    else:
        context.bot.send_message(update.effective_chat.id,'Ты ходишь 1ым')



def game(update, context):
    while overall_candies > 0:

        if count == 2:
            context.bot.send_message(update.effective_chat.id,'Напиши,сколько конфет хочешь взять')
            players_take = update.message.text
            if players_take is int:

                if players_take <= max_take:
                    overall_candies = overall_candies - players_take
                    context.bot.send_message(update.effective_chat.id,'Теперь мой ход')
                    count = 1
                else:
                    context.bot.send_message(update.effective_chat.id,'Так много взять нельзя!')
                
                if overall_candies == 0:
                    context.bot.send_message(update.effective_chat.id,'Ты победил')
                else:
                    context.bot.send_message(update.effective_chat.id,'Теперь мой ход')
                    count = 1
            else:
                context.bot.send_message(update.effective_chat.id,'Введи число')

        if count == 1:
            smart_bot_take = overall_candies%(max_take+1)
            overall_candies = overall_candies - smart_bot_take
            context.bot.send_message(update.effective_chat.id,f'Я взял {smart_bot_take} конфет, осталось {overall_candies} конфет')
            if overall_candies == 0:
                context.bot.send_message(update.effective_chat.id,'Я победил')
            else:
                context.bot.send_message(update.effective_chat.id,'Теперь твой ход')
                count = 2




start_handler = CommandHandler('Start', start)
game_handler = MessageHandler(Filters.text, game)


dispahather.add_handler(start_handler)
dispahather.add_handler(game_handler)


updater.start_polling()
updater.idle()