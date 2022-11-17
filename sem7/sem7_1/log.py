# Логирование результатов(логи чата)
import addNumbers

def logger(primer,result):
    with open('logi_scheta.txt', 'a') as file:
        reparse = ''.join(map(str, primer)) #Берёт список(primer) и поэлементно, '' указывают,через что соединять
                                            # добавляет к пустой строке после запятой(str,)
        # result = str(result)+';\n'
        file.write(str(reparse)+' = ')
        file.write(str(result) + ';\n')
    
    
