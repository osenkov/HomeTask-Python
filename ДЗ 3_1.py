def func(var_1, var_2):
    """Функция деления"""
    return var_1 / var_2


try:
    a = float(input('введите значение числителя: '))
    b = float(input('введите значение знаменателя: '))

    if b == 0:
        print('Делить на 0 нельзя')
    else:
        print(func(a, b))
except ValueError:
    print('Ошибка ввода')
