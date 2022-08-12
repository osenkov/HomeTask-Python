from sys import argv
from itertools import count, cycle

""" запуск в терминале по строке: python3 {filename}.py {x} {y} {z} {w}
    x - начальное значение генерирации целых чисел 
    y - конечное значение генерирации целых чисел
    z - повторяющиеся элементы списка 
    w - число циклов повторения
"""
script_name, x, y, z, w = argv

print('генерация целых чисел начиная с ', x, ' по ', y)
try:
    for el in count(int(x)):
        if el > int(y):
            break
        else:
            print(el)
except ValueError:
    print("Ошибка воода данных")

try:
    с = 0
    for el in cycle(z):
        if с > int(w):
            break
        print(el)
        с += 1
except ValueError:
    print("Ошибка воода данных")
