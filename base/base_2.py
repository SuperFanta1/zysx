# 讲解list和dict这两种数据类型。
# list: 列表，类似于数组的用法，可以进行增删改查的操作。

# l1 = []
# # l2这个列表中有6个元素，每一个元素都有一个索引值，索引值从0开始。
# l2 = [1, 10.5, '123',[1, 2, 3], True, False]
# print(type(l1))
#
# # 向l2列表中添加元素append(): 这个函数是向列表的末尾追加数据。
# l2.append('张三')
# l2.append(111)
# print(l2)
#
# # 向l2列表中添加元素insert()：这个函数可以通过索引指定数据保存的位置。
# l2.insert(0, '000')
# l2.insert(1, '哈哈哈')
# print(l2)
#
# # 查询l2列表中的单个元素或者多个元素
# print(l2[0], l2[3], l2[5])
# # 索引切片查询多个元素: [起始索引:终止索引]，切片取值时是不包含终止索引对应的元素的。
# print(l2[1:3], l2[1:], l2[:3])
# # 负索引按照倒序查询，正索引按照正序查询。
# print(l2[-1], l2[-2:])
#
# # 列表也属于可迭代对象，所以在获取所有元素时，可以使用for/while循环。
# for obj in l2:
#     print('---', obj)
#
# # 修改列表中某个元素的值。
# print(l2)
# l2[0] = '111'
# l2[1] = '嘿嘿嘿'
# print(l2)
#
# # 删除列表中的元素
# # 使用del删除l2列表中索引为0的元素
# del l2[0]
# print(l2)
#
# # pop(): 如果没有指定索引值，默认是从最后的元素开始删除；如果指定索引了，就删除指定索引的值；
# item = l2.pop()
# print(l2, item)
#
# # remove(): 直接删除列表中的元素值，需要指定这个值，不需要索引。
# l2.remove('嘿嘿嘿')
# print(l2)

# dict字典：增删改查的操作
# list列表在存储元素时，元素的排列是有先后顺序的；而字典存储数据是无序的，所以字典没有索引。
# 字典是通过键来操作一个值
d1 = {}
d2 = {'name': '张三', 'age': 20, 'is_male': False, 'attrs': [1, 2, 3]}
print(type(d1))
# 判断列表中元素个数，或者字典中键值对的个数，使用函数len()
print(len(d2))

# 向字典中添加键值对
# class/nums是键，'1班'和50是值
d2['class'] = '1班'
d2['nums'] = 50
print(d2)

# 获取字典中的值
# print(d2['class'], d2['age'], d2['a'])
# d2.get()在取值时，如果这个键不存在，则采用默认值。
cls = d2.get('a', '不清楚')
print(cls, d2.items())
# 通过循环可以将字典中的所有键值对遍历出来。
# d2.items()得到的是：[('name', '张三'), ('age', 20), ('is_male', False), ('attrs', [1, 2, 3]), ('class', '1班'), ('nums', 50)]
# ('name', '张三')就是元组类型tuple。
for key, value in d2.items():
    print('{}: {}'.format(key, value))

# 获取字典中所有的键
print(d2.keys())
# 获取字典中所有的值
print(d2.values())

# 修改字典中的值：方式和添加键值对的写法一样。如果字典中不存在class和age就是添加键值对；如果存在class和age就是修改值。
d2['class'] = '2班'
d2['age'] = 50
print(d2)

# 删除字典中的键值对
del d2['class']
print(d2)

d2.pop('age')
print(d2)
