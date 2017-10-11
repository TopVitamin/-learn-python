# 函数接收可变参数
def calc (*numbers): # numbers前面加一个*可以动态的接收变化的参数
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

nums = [1, 2, 3] # 这个是一个list
mums = (2, 3, 4) # 这个是一个tuple
print(calc(1, 3, 4))
#print(calc(nums)) 不能直接传入list
print(calc(*nums))
#print(calc(mums)) 不能直接传入tuple
print(calc(*mums))
# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。
#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，
#kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
