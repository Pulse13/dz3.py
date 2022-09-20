# Напишите прогу,которая определит позицию 2ого вхождения строки в списке,либо определит что её нет.
list = [1234,'kekis kek', 'kek','kek rofl']
str = 'kek'
count = 0
i = 0

if str in list[i]:
    count+=1
if count == 1 and str in list[i]:
    print(i)
else:
    print('No')