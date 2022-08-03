my_list = [7, 5, 3, 3, 2]
print('Список:', my_list)
try:
    x = int(input('введите целое число: '))
    my_list.append(x)
    my_list.sort(reverse=True)
    print(my_list)
except ValueError:
    print('Ошибка ввода')
