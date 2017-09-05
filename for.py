# for循环
names = ['Michael', 'Bob', 'Tony']
for oneName in names:
    print(oneName)

# sum = 0
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
# for x in numbers:
#     sum += x
# print(sum)

sum = 0
lists = range(10)
for x in lists:
    sum += x
print(sum)
print(list(lists))

#**********************************************#
# while
sums = 0
n = 99
while n > 0:
    sums = sums + n
    n = n - 2
print(sums)

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
