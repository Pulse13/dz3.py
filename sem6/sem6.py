# 1.Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа. 
# Реализовать программу с использованием функции filter. Результат отобразить на экране в виде последовательности оставшихся чисел в одну строчку через пробел.
# пример - 8 11 0 -23 140 1 => 11 -23


# nums = [5,234,2332,23,2]

# print(list(filter (lambda x:9<abs(x)>100, nums)))


# 2.Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.



def parse(s):
    result = []
    digit = ''

    for elem in s:
        if elem.isdigit():
           digit+=elem
        else:
            result.append(int(digit))
            digit = ''
            result.append(elem)
    else:
        if digit:
            result.append(float(digit))
    return result

def calculate(lst):
    result= 0.0

    while '*' in lst:
        index=lst.index('*')
        result = lst[index-1]*lst[index+1]
        lst = lst[:index-1]+[result]+lst[index+2:] # заменяем список элементов по которым выполнили умножение на результат этого умножения(вырезаем нашу операцию).
        #  index-1 (НЕ ВКЛЮЧИАЕТСЯ НА ПЕРВОМ СРЕЗЕ)

    while '/' in lst:
        index=lst.index('/')
        result = lst[index-1]/lst[index+1]
        lst = lst[:index-1]+[result]+lst[index+2:]

    while '+' in lst:
        index=lst.index('+')
        result = lst[index-1]+lst[index+1]
        lst = lst[:index-1]+[result]+lst[index+2:]
    while '-' in lst:
        index=lst.index('-')
        result = lst[index-1]-lst[index+1]
        lst = lst[:index-1]+[result]+lst[index+2:]
    return result

s = '1+4*3/2'
result = parse(s)

print(result)
print(calculate(result))



# 3) ПОследовательность, получить уникальные элементы.



list1 = [1,1,2,2,3,10]
list2 = []
list3 = []

# lst2 = list(filter(lambda x: x not in list[x:], list1 ))#1st 

for el in list1:

    if el not in list2 and el not in list3:
        list2.append(el)
        list3.append(el)
    elif el in list2:
        list3.remove(el)
print(list3)    










