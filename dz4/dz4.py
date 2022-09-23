# 1) Вычислить число c заданной точностью d

d = str(input())
p = float(input())
length = len(d) - 2
print(length)
print(round(p,length))



# 2) Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

N = int(input('Введите натуральное число: '))
for i in range(1, N):
    if N%i==0:
        N/= i
        print(i, end=' ')



# 3) Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

row = [2,5,5,8,2,9,25,5]
row1 = []
for i in row:
    if i not in row1:
        row1.append(i)
print(row1)



# 4) Задана натуральная степень k. Сформировать случайным образом список коэффициентов
#  (значения от 0 до 100) многочлена и записать в файл многочлен степени k.


from random import randint
from unicodedata import digit
k = int(input())
res = ''
for i in range(k, -1, -1):
    if i == 0:
        m = randint(0, 100)
        res += f'{m}'
    if i == 1:
        m = randint(0, 100)
        res += f'{m}x+'
    if i>1:
        m = randint(0, 100)
        res += f'{m}x**{i}+'
print(res)

fname = input('файл')
f = open(fname, 'w')
f.write(res)
f.close()


# 5) Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

