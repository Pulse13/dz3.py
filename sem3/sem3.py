# Создать файл,записать в него построчно данные, которые вводит пользователь. Окончанием ввода пусть служит пустая строчка.
fname = input('файл')
f = open(fname, 'w')
while True:
    s=input()
    if s=='':
        break
    f.write(s+'\n')
f.close()


# Создать текстовый файл,посчитать кол-во строк,опеределить в каждой строке кол-во символов и слов.

f = open('text1.txt', 'r')
countlines = 0
words = []
symbols = []
for line in f:
    countlines+=1
    if line !='\n':
        words.append(line.count(' ')+1)
    else:
        words.append(0)
    symbols.append(line.count('')-2)
f.close()
print(countlines)
print(words)
print(symbols)


#Создать список и определить если ни некоторое числа  в этом списке

# list = [1,4,3,5]
# num = input('Введите числ: ')
# if num in list:
#     print('yes')
# else:
#     print('no')



# Напишите прогу,которая определит позицию 2ого вхождения строки в списке,либо определит что её нет.
list = [1234,'kekis kek', 'kek','kek rofl']
str = 'kek'
count = 0
for i in len(list):
    if str in list[i]:
        count+=1
    if count == 1 and str in list[i]:
        print(i)
        break
    else:
        print('No')