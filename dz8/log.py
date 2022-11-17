import start

def loger1(res):
    with open('directory1.txt', 'a') as file:
        file.write(str(res))


def loger2(res):
    with open('directory_row.txt', 'a') as file:
        file.write(str(res))

