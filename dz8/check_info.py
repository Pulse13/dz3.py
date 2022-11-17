import re

def Get_catalog():
    with open('directory_row_result.txt', 'a+') as row_result:
        with open('directory_row.txt', 'r') as row:
            m = ''
            for x in row:
                m+=x
        l = re.split(r"[,\n]", m)

        for x in range(int(len(l)/4)):
            for i in range(4):
                if i == 0:
                    row_result.write('Female: '+ l[(i)+((x)*4)]+', ')
                    i+=1
                elif i == 1:
                    row_result.write('Name: '+ l[(i)+((x)*4)]+', ')
                    i+=1
                elif i == 2:
                    row_result.write('Phone: '+ l[(i)+((x)*4)]+', ')
                    i+=1
                elif i == 3:
                    row_result.write('Discription: '+ l[(i)+((x)*4)]+'\n')
                    i+=1





