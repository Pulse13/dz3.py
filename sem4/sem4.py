# 1) Набор чисел и прога покажет большее и меньшее число
numbers = '33 2 3 6 5 10'
lst = [int(i) for i in numbers.split()]
print(min(lst))
print(max(lst))

# 2ое решение
minimum = int(numbers[0])
maximum = int(numbers[0])
for i in numbers.split(sep = ' '):
    if int(i) < minimum:
        minimum = int(i)
    if int(i) > maximum:
        maximum = int(i)
print(minimum,maximum)



# 2) (а*х)**2 + b*x + c 
