# 1) Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

nums = [3,4,3,6,2,3,9]
sum = 0
for i in range(len(nums)):
    if i%2>0:
        sum+=nums[i]
print(sum)



# 2) Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

nums = [1,5,-9,5,-3,3,7,5,6]
result = 0
for i in range (0,int(len(nums)/2)):
    result = nums[i]*nums[-i-1]
    print(result)



# 3) Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

nums = list(input().split())
print(nums)
maxi=nums[0]
mins=nums[0]
for i in range(len(nums)):
    if nums[i] > maxi:
        maxi = nums[i]
    if nums[i] < mins:
        mins = nums[i]
print(maxi,mins)

print(round((float(maxi)%1) - (float(mins)%1)), 2)



# 4) Напишите программу, которая будет преобразовывать десятичное число в двоичное.

num = int(input())
while num>0:
    print(num%2,end='')
    num//=2



