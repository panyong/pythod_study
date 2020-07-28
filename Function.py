# from Abstest import my_abs


# def power(x):
#     return x * x


# print(power(5))


def power(x, n=2):
    ret = 1
    while n > 0:
        ret = ret * x
        n = n - 1
    return ret


print(power(5, 3))
print(power(5))


def enroll(name, gender, age=6, city='SH'):
    print('name:%s, gender:%s, age:%s, city:%s' % (name, gender, age, city))


enroll('Rambo', 'M', city='HZ')


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end())
print(add_end())


def calc(*nums):
    sum = 0
    for x in nums:
        sum = sum + x * x
    return sum


print(calc(1, 2, 3, 4))
nums = (1, 2, 3, 4)
nums2 = [1, 2, 3, 4]
print(calc(*nums))
print(calc(*nums2))


def person(name, age, **kw):
    print('name:', name, "age:", age, 'others:', kw)


person('Rambo', 28, job='Back-end engineer', Salary='25k/mon')

kw = {'job': 'Back-end engineer', 'Salary': '25k/mon'}

person('R', 29, **kw)


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(10))


def fact2(n):
    return fact2_iter(n, 1)


def fact2_iter(n, sum):
    if n == 1:
        return sum
    return fact2_iter(n - 1, n * sum)


print(fact2_iter(10, 1))


def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)
        print(a, '-->', c)
        move(n - 1, b, a, c)


move(5, 'A', 'B', 'C')
