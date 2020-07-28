import functools, time


def metric(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        start = time.time()
        f = func(*args, **kw)
        end = time.time()
        print('%s executed in %s ms' % (func.__name__, end - start))
        return f

    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')


def around(text='execute'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('%s begin call' % text)
            f = func(*args, **kwargs)
            print('%s end call' % text)
            return f

        return wrapper

    return decorator


@around()
def f():
    print('f')


@around('test')
def f2():
    print('f.test')


f()
f2()
