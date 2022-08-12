from functools import reduce

res = reduce(lambda mult, x: mult * x, [x for x in range(100, 1001, 2)])
print(res)
