#!/usr/bin/env python3
# -*-coding:utf-8-*-


class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')

from types import MethodType


def set_age(self, age):
    self.age = age


student = Student('Rambo')
student.set_age = MethodType(set_age, student)

student.set_age(27)

print(student.age)


class People(object):
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age


p = People()
p.age = 12
print(p.age)


class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def resolution(self):
        return self._width * self._height


class Fib(object):
    def __init__(self):
        self._a, self._b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self._a, self._b = self._b, self._a + self._b
        if self._a > 10000:
            raise StopIteration()
        return self._a


for a in Fib():
    print(a)


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, item):
        return Chain('%s/%s' % (self._path, item))

    def __str__(self):
        return self._path

    def users(self, name):
        return getattr(self, name)

    __repr__ = __str__


print(Chain('v1').name.age.users('ss').i)

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))


@unique
class Month(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
