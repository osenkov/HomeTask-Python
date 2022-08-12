def fact(n):
    f = 1
    for i in range(n):
        f = f * (i + 1)
    yield f


n = int(input('введите n:'))
for el in fact(n):
    print(el)
