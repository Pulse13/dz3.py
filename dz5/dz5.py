# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# string_input = 'кек ываол абв ылдвао абвар ы'
# string_output = list(filter(lambda x: not 'абв' in x, string_input.split()))
# string_output = ' '.join(string_output)

# print(string_output)



# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

list1 = [1,2,3,5,1,5,3,10,1,11,2]
# list_res = list(filter(lambda x: list1.count(x)==1, list1))
list_res1 = list(filter(lambda x: x not in list1[x:], list1))#2ое решение
print(list_res1)


