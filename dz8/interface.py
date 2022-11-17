import add_info as info
import log
import start
import check_info

def button_click1():
    check = start.Check_value()
    if check == 1:
        f = int(input('Нажмите 1 чтобы сделать запись в столбец\n0, чтобы сделать запись в строку\n2, чтобы закончить запись\n'))
        while f == 1:
            res1 = info.list1()
            log1 = log.loger1(res1)
            f = int(input('Нажмите 1 чтобы продолжить запись в столбец\n0, чтобы продолжить запись в строку\n2, чтобы закончить запись\n'))
        while f == 0:
            res2 = info.list_row()
            log2 = log.loger2(res2)
            f = int(input('Нажмите 1 чтобы продолжить запись в столбец\n0, чтобы продолжить запись в строку\n2, чтобы закончить запись\n'))
        if f == 2:
            print('Запись завершена')

    if check == 2:
        check_info.Get_catalog()

        










