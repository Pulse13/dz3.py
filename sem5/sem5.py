# 1) Объявите анонимную (лямбда) функцию для определения вхождения в переданную ей строку фрагмента "plr". 
# То есть, функция должна возвращать True, если такой фрагмент присутствует в строке и False - в противном случае.

# print('plr' in str1)
# kek = lambda str, sample = 'plr': sample in str
# str = input()
# print(kek(str))



# 2) В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

# f = open('text2.txt', 'r')
# lst = [int(i) for i in f.readline().split()]
# for i in range(1, len(lst)):
#     if lst[i] - 1 != lst[i-1]:
#         print(lst[i]-1)



# 3) Напишите программу, удаляющую из текста все слова, содержащие "абв".

from os import remove


string1 = 'вжуходратутец кекис абва абвобус'
words = list(str(string1).split())
print(words)
for i in words:
    if 'абв' in i:
        words.remove(i)

print(words)