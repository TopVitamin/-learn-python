# def 定义函数
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('Bad operand type')
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(123))
