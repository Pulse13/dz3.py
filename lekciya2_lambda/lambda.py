# def f(x):
#     return x**2

# g = f

# print(f(2))
# print(g(2))



# def calc1(x):
#     return x+10

# print(calc1(10))

# def calc2(x):
#     return x*10
# print(calc2(10))

# def math(op, x) # op -это функция
#     print(op(x))

# math(calc2, 10)



# def sum(x, y):
#     return x+y

# sum = lambda x, y: x+y # то же самое,что и выше

# def mylt(x, y):
#     return x*y

# def calc(op, a, b):
#     # print(op(a,b))
#     return op(a,b)

# calc(lambda x, y: x+y,4,5) #можно не передавать переменную, а сразу прописывать код


list = [1,2,3,5,8,15,23,38]
def f(x):
    return x**2
list1 = [(list[i],f(list[i])) for i in range(len(list)) if list[i]%2 == 0]
print(list1)