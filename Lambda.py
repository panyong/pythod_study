from functools import reduce


def normalize(name):
    if not isinstance(name, str):
        return
    return name[0].upper() + name[1:].lower()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def prod(L):
    def f(x, y):
        return x * y

    return reduce(f, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


def is_palindrome(n):
    L = list(str(n))
    L1 = list(reversed(L))
    return L == L1


print(is_palindrome(121))

# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101,
                                                  111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_score(t):
    return t[1]


L2 = sorted(L, key=by_score, reverse=True)
print(L2)


def by_name(t):
    return t[0].lower()


L3 = sorted(L, key=by_name)
print(L3)
[].append(1)

def str2float(s):
    flag = True

    def f(x):
        if x == '.':
            return x
        return ord(x) - 48

    def f2(x, y):
        if y == '.':
            flag = False
            return
        if flag:
            return x * 10 + y
        else:
            return x + y / 10

    return reduce(f2, map(f, s))


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
