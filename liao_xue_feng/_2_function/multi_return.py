"""Sample of function returns multiple values"""


def func_returns_multiple(x, y, z):
    return x + 1, y + 1, z + 1


x2, y2, z2 = func_returns_multiple(1, 2, 3)
print(x2, y2, z2)
