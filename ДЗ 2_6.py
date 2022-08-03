s = int(input('введите количество позиций Товара: '))
my_tuple = ()
my_list = []
for i in range(s):
    print('Товар', i + 1)
    name = input('введите наименование Товара: ')
    price = input('введите стоимость Товара: ')
    num = input('введите количество Товара: ')
    unit = input('введите единицу измерения Товара: ')
    d = {'название': name, 'цена': price, 'количество': num, 'eд': unit}
    my_tuple = (i + 1, d)
    my_list.append(my_tuple)
    i += 1
print(my_list)
