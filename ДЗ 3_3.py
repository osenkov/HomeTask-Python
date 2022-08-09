def my_func(var_1, var_2, var_3):
    """Функция поиска суммы наибольших аргументов"""
    x = (var_1, var_2, var_3)
    y = sorted(x, reverse=True)
    return print('Сумма двух наибольших аргументов = ', y[0] + y[1])


try:
    a = float(input('введите значение 1: '))
    b = float(input('введите значение 2: '))
    c = float(input('введите значение 3: '))
    my_func(a, b, c)
except ValueError:
    print('Ошибка ввода числа')
