classmates = ['M', 'B', 'T']
print(len(classmates))

age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')

birth = input('birth: ')
if int(birth) < 2000:
    print('00-before')
else:
    print('00-after')

height = input('height(cm): ')
weight = input('weight(kg): ')
bmi = float(weight) / float(height) / float(height) * 10000
print('bmi: %.2f' % bmi)
if bmi < 18.5:
    print('过轻')
elif bmi <= 25:
    print('正常')
elif bmi <= 28:
    print('过重')
elif bmi <= 32:
    print('肥胖')
else:
    print('严重肥胖')

