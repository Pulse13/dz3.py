# Напишите программу, которая подсчитает и выведет сумму квадратов всех двузначных чисел, делящихся на 9.
# При решении задачи используйте комбинацию функций filter, map, sum.

# l = [i for i in range(10,100)]
# l1=  list(filter(lambda x:x%9 == 0, l))
# l2 = sum(list(map(lambda x: x**2,l1)))
# print(l2)



# Функция триангл(а,в,с) принимает 3 длины отрезков и определяет это треугольник или нет

# def Triangle(a,b,c):
#     return a+b >c and a+c >b and b+c>a

# a=1
# b=5
# c=5

# if Triangle(a,b,c):
#     print("da")
# else:
#     print('no')




# Программа для обработки текста.
# Нужно пронумеровать слова, а потом вывести только те слова,которые с большой буквы.
# Перед словом необходимо вывести номер первого вхождения слова в текст
# Слова пронумеровать в лексографическом порядке.
# Ехал Грека через реку.
# Видит Грека в реке рак.
# Сукул Грека руку в реку.
# Рак за руку Греку цап.

a = []
for i in range(4):
    a.extend(input().replace('.','').split())
b= list(enumerate(a))
sp = []
b.sort(key = lambda x:x[1])
for i in b:
    if i[1][0].isupper() and i [1] not in sp:
        print(*(i[0],'-',i[1]))
        sp.append(i[1])