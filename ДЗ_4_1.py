from sys import argv

script_name, var_1, var_2, var_3 = argv
print("РАСЧЕТ ЗАРАБОТНОЙ ПЛАТЫ СОТРУДНИКА")
print("выработка, ч.: ", var_1)
print("ставка, ч.: ", var_2)
print("премия. руб.: ", var_3)
try:
    print("З/П сотрудника, руб. = ", (int(var_1) * int(var_2) + int(var_3)))
except ValueError:
    print("Ошибка воода данных")
