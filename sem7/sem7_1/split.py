# Разделяем наше выражение
from addNumbers import getValue  #Импорт функции с другого файла


def parse():
    s = getValue()
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