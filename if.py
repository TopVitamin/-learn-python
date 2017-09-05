# -*- coding: utf-8 -*-
#if if a > b:   elif a == b:
age = 10
if age < 10:
    print('this is a baby')
elif age == 10:
    print('this is a teenager')
else:
    print('this is a adult')
# 练习
height = 1.75
weight = 60.6
BMI = weight/height/height
if BMI < 18.5:
    print('过轻')
elif BMI < 25:
    print('正常')
elif BMI < 28:
    print('过重')
elif BMI < 35:
    print('肥胖')
else:
    print('严重肥胖')
