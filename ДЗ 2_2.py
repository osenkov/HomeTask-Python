x = input('введите последовательность: ')
lst = list(x)
s = len(lst) - 1
i = 0
while i < s:
    lst[i], lst[i + 1] = lst[i + 1], lst[i]
    i = i + 2
print(lst)
