def calc():
    """ Функция суммирования с выходом по символу 'q' """
    x, s, exx = 0, 0, 0
    my_line = input('введите в строку целые числа, разделенные пробелом или введите "q" для выхода: ')
    my_list = my_line.split(' ')
    for el in my_list:
        if el == 'q':
            exx = 1
            break
        else:
            try:
                x = int(el)
                s = s + x
            except ValueError:
                pass
    return s, exx


ex = 0
summa = 0
while ex != 1:
    sum, ex = calc()
    summa = summa + sum
    print('сумма введенных значений равна:', summa)
