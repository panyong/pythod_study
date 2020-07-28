import math


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad type')
    if x >= 0:
        return x
    else:
        return -x


def nop():
    pass


my_abs(1)


def my_max(x, y):
    return max(x, y), min(x, y)


print(my_max(1, 2))


def qua(a, b, c):
    x = math.sqrt(b * b - 4 * a * c)
    return (-b + x) / 2, (-b - x) / 2


x, y = qua(2, 8, 5)
# print('%.2f, %.2f' % qua(2, 8, 5))
print('%dx^2 + %dx + %d = 0: %.2f, %.2f' % (2, 8, 5, x, y))
