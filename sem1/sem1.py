# Напишите прогу которая принимает 2 числа и проверяет число в степени 2 равно числу 2ому

# a = int(input('a = '))
# b = int(input('b = '))

# if a**2==b:
#     print('--> yes')
# elif b**2 == a:
#     print('--> yes')
# else:
#     print('--> no')



# Прога которая принимает 5 чисел и находит наобольшее
# num = [int(i) for i in input().split()]
# print(num)
# max_num = num[0]
# for i in range(len(num)):
#     if num[i] > max_num:
#         max_num = num[i]
# print(max_num)




# Приём числа N, и вывод -N до N

# n = int(input('N = '))
# for i in range(-n, n+1):
#     print(i, end=' ,')




# Принимает дробь и показывает 1ую цифру этого числа после запятой

# n = float(input('дробь n = '))
# num = n*10
# f = num%10
# print(int(num%10))




# Прога которая проверяет кратно ли число 5 и 10 или 15,но не 30

n = int(input('n = ')) 
print(n%5 and n%10 == 0 or n%15 == 0 and n%30 != 0)