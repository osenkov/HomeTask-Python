name = input('Как Вас звать/величать? ')
age = int(input('Сколько Вам годков? '))
sex = input('Укажите Ваш пол, в формате м/ж, пожалуйста: ')
if sex == "м":
    print(f'Жил был {name}, да было ему {age} годков')
else:
    if sex == "ж":
        print(f'Жила была {name}, да было ей {age} годков')
    else:
        print('не выдумывай!')
