# from random import randint

# # 1) Игра в конфеты игрок против игрока 

def game():
    candies = 2021
    max_take = 28
    count = 0
    player1 = input('1st player name ')
    player2 = input('2nd player name ')

    a = randint(1,2)
    if a==1:
        start = player1
        finish = player2
        print('Player1 ur turn ')
    else:
        start = player2
        finish = player1
        print('Player2 ur turn ')


    while candies > 0:

        if count == 0:
            turn = int(input(f'{start} how much candies u want to take? '))
            if turn > max_take or turn > candies:
                candies+=turn
                print(f'Take {max_take} or less candies plz ')

            candies -= turn
            if candies == 0:
                print(f'{start} u won!') 
            else:
                print(f'{finish} ur turn and overall candies {candies} ')
                count == 1

        if count == 1:
            turn = int(input(f'{finish} how much candies u want to take? '))
            if turn > max_take or turn > candies:
                print(f'Take {max_take} or less candies plz ')

            candies -= turn
            if candies == 0:
                print(f'{finish} u won!') 
            else:
                print(f'{start} ur turn and overall candies {candies} ')
                count == 0

game()



# # 2) Игра в конфеты игрок против умного бота

def game():
    candies = 22
    max_take = 3
    count = 0
    bot = 'Bott'
    player = input('players name ')


    a = randint(1,2)
    if a==1:
        start = bot
        finish = player
        print('Bot start ')
    else:
        start = player
        finish = bot
        print('Player start ')


    while candies > 0:

        if count == 0:

            if start == bot:

                neeed_to_take = candies%(max_take+1)
                if neeed_to_take == 0:
                    candies = candies-1
                    print('Bot is taking 1 candies')
                    count == 1
                else:
                    candies = candies-neeed_to_take
                    print(f'Bot is taking {neeed_to_take} candies')
                    if candies == 0:
                        print(f'Bot won')
                    else:
                        print(f'Bot finish his turn and overrall candies{candies}')
                        count == 1

                


            else:
                turn = int(input(f'{start} how much candies u want to take? '))
                if turn > max_take or turn > candies:
                    candies+=turn
                    print(f'Take {max_take} or less candies plz ')

                candies -= turn
                if candies == 0:
                    print(f'{start} u won!') 
                else:
                    print(f'{finish} ur turn and overall candies {candies} ')
                    count == 1

        if count == 1:

            if finish == bot:

                neeed_to_take = candies%(max_take+1)
                if neeed_to_take == 0:
                    candies = candies-1
                    print('Bot is taking 1 candies')
                    count == 0
                else:
                    candies = candies-neeed_to_take
                    print(f'Bot is taking {neeed_to_take} candies')
                    if candies == 0:
                        print(f'Bot won')
                    else:
                        print(f'Bot finish his turn and overall candies{candies}')
                        count == 0


            else:
            
                turn = int(input(f'{finish} how much candies u want to take? '))
                if turn > max_take or turn > candies:
                    print(f'Take {max_take} or less candies plz ')

                candies -= turn
                if candies == 0:
                    print(f'{finish} u won!') 
                else:
                    print(f'{start} ur turn and overall candies {candies} ')
                    count == 0

game()




# 3) Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def coding(txt):
    count = 0
    words = txt[0]
    result = ''
    for element in txt:
        if element == words:
            count+=1
        else:
            result += str(count) + words
            count = 1
            words = element
    else:
        result += str(count) + words
    return result


def decoding(txt: str) -> str:
    num = ''
    result = ''
    for element in txt:
        if element.isdigit():
            num+= element
        else:
            for i in range(int(num)):
                result+= element
            else:
                num = ''
    return result

print(coding('aadddfffggfg'))
print(decoding('3b4g1b3v'))