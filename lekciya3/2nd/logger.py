from datetime import datetime as dt

def temporature_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{}; temporature; {}'
                        .format(time,data))


def pressure_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{}; pressure; {}'
                        .format(time,data))


def wind_speed_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{}; wind speed; {}'
                        .format(time,data))