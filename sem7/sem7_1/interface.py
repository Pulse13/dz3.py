import split, addNumbers, log


def button_click():
    f = int(input('press 1 for complete\n'))
    while f == 1:
        primer = split.parse()
        result = split.calculate(primer)
        addNumbers.viev_data(result)
        log.logger(primer, result)
        f = int(input('press 1 for complete\n'))
    else:
        print('glhf')


