from start import Get_value

def list1():
    s = Get_value()
    result1 = str(s.replace(';', '\n'))
    result = str(result1 + '\n' + '\n')
    return result

def list_row():
    s = Get_value()
    result1 = s.replace(';', ',')
    result = str(result1+'\n')
    return result

