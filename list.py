# list 类似与其他语言的数组或者对象的形式，可以追加，删除，计算数量
classmates = ['Michael', 'Bob', 'Tracy']
newBody = 'vitamin'
classmates[0] = 'beautyGirl'
classmates.insert(1, 'bug')
classmates.append(newBody)
classmates.pop(-1)
print(len(classmates))
print('\n'+str(classmates))
print('\n'+classmates[0])
print('\n'+classmates[1])
print('\n'+classmates[2])
print('\n'+classmates[3])
print('\n'+classmates[-1])
print('\n'+classmates[-2])
print('\n'+classmates[-3])

# tuple（元组） 一旦初始化就不能修改

language = ('java', 'php', 'python')
print('\n')
print(len(language))
print('\n'+str(language))

# 练习

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])
