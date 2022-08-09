def my_func(var_1, var_2):
    """Функция возведения в степень"""
    x = var_1 ** (1 / (- var_2))
    return print('число ', var_1, 'в степени 1/', -var_2, ' = ', x)


try:
    a = float(input('введите положительное число: '))
    b = int(input('введите целое отрицательное число: '))
    if a > 0 and b < 0:
        my_func(a, b)
    else:
        print('ошибка ввода')
except ValueError:
    print('Ошибка ввода числа')
