def int_funk(my_line):
    """ фукнция трансформации регистра вводимых слов"""
    i = 0
    my_list = list()
    for el in my_line:
        if 97 <= ord(el) <= 122 or ord(el) == 32:
            pass
        else:
            print('Ошибка ввода')
            my_line = None
            break
    try:
        for el in my_line:
            if ord(el) != 32 and i == 0:
                i = 1
                my_list.append(chr(ord(el)-32))
            elif ord(el) != 32 and i == 1:
                my_list.append(el)
            elif ord(el) == 32:
                i = 2
                my_list.append(el)
            elif i == 2:
                my_list.append(chr(ord(el)-32))
                i = 1
        print("".join(my_list))
    except TypeError:
        pass
    return

int_funk(my_line = input('введите слова латинскими буквами в нижнем регистре через пробел: '))