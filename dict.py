#dict 字典 dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
dicts = {'Michael':80, 'Bob':89, 'Tony':98}
print(dicts)
print(dicts['Tony'])
print('vitamin' in dicts)
print('Michael' in dicts)
print('michael' in dicts)
print(dicts.get('Bob'))
print(dicts.get('vitamin',100))
print(dicts.get('vitamin',))

#***********************************#
# set  是一组key的集合，不存储value，key不能重复
s = set([1, 2, 3, 1, 3])
s.add(4)
s.remove(1)
print(s)



#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s1 = set([1 ,2, 3])
s2 = set([2, 4, 5])
result1 = s1 & s2 #与操作
result2 = s1 | s2 #或操作
print(result1)
print(result2)

#对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。
