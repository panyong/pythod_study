def trim(s):
    start = 0
    end = len(s)
    while True:
        if s[start:start + 1] != ' ' and s[end - 1:end] != ' ':
            break
        elif s[start:start + 1] == ' ':
            start = start + 1
        elif s[end - 1:end] == ' ':
            end = end - 1

    return s[start:end]


# def trim(s):
#     start = 0
#     end = 0
#     count = 0
#     for i, v in list(s):
#         count = count + 1
#         if v != ' ':
#             start = i
#         if v == ' ' and count > start:
#             end = end + 1
#             break
#
#     return s[start:end]
# 测试:
# if trim('hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello') != 'hello':
#     print('测试失败!')
# elif trim('  hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello  world  ') != 'hello  world':
#     print('测试失败!')
# elif trim('') != '':
#     print('测试失败!')
# elif trim('    ') != '':
#     print('测试失败!')
# else:
#     print('测试成功!')


def findMinAndMax(L):
    if len(L) == 0:
        return None, None
    minV, maxV = L[0], L[0]
    for v in L:
        minV = minV if minV < v else v
        maxV = maxV if maxV > v else v
    return minV, maxV


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')


def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[i] + L[i+1] for i in range(len(L) - 1)] + [1]

n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)


