print('123')
print("456")

# python变量的命名规范(变量如何命名)
# 1. 变量名以字母开头，可以由字符、数字、下划线组成；
# 2. 变量名的命名需要遵循驼峰命名法；studentName和student_name；
# 3. 变量名的命名要有意义，不能使用a、b....等命名；
# 4. 变量属于弱类型的变量，变量前面不需要添加变量类型；

student_age = 20
student_name = '张三'

print(student_name, student_age)

# if 条件判断 (True/False)
# Python中规定：非0和非空(Null)的结果都是True，0或者Null的结果都是False

# 注意：
# 1. 冒号；2. 行与行之间的缩进关系；如果缩进错误会出现IndentationError: unexpected indent错误；
if student_age < 20:
    print('年龄小于20')
    print(student_name)
elif student_age == 20:
    print('年龄等于20')
else:
    print('年龄大于20')

# 多个判断条件可以使用and或or进行链接
if student_age == 20 and student_name == '张三':
    print('正确')
else:
    print('错误')

# for循环、while循环
# for...in...
# 字符串在Python属于可迭代对象，便可以for循环。
# break：终止/跳出整个循环；
# continue：终止/跳出某一次循环；
for char in student_name:
    if char == '张':
        break
        #continue
    print('----', char)

a = 1
while a < 20:
    # a < 20条件成立，执行循环体；条件不成立则终止循环，也支持break和continue关键字。
    print('a = ', a)
    a += 1

# 内置的类型转化方法：
# Python中支持的数据类型：字符串(str)、整数/小数(int/float)、列表(list)、元组(tuple)、字典(dict)、集合(set)、对象(object)
age = '22'
# type()：Python内置函数：用于判断一个变量的类型
print(type(age))
age_int = int(age)
print(type(age_int))

result = str(age_int)
print(type(result), result)

# Python中字符串的拼接方式：
#1. 通过"+"号拼接，所有拼接的数据都必须是 "str" 类型的才能使用+号；
#2. 通过 "%" 占位符进行拼接；
#3. 通过format()函数拼接；

# 方式1：
# res = '姓名：' + student_name + ', 年龄：' + str(student_age)
# print(type(res), res)

# 方式2：
# %s: 万能占位符，可以代表所有数据类型；
# %d: 整数类型占位符  %f: 小数类型占位符；
# res = '姓名是: %s' % student_name
# res1 = '姓名是：%s, 年龄是：%s' % (student_name, student_age)
# print(res, res1)

# 方式3：
# res = '姓名是: {}, 年龄是：{}'.format(student_name, student_age)
# print(res)

# Python中的异常捕获
# 断点调试
# Exception: Python中所有异常类的父类，这个类可以捕获所有的错误。
# try:
#     # 将你认为可能会出现异常的代码放在try语句中；
#     res = student_name + student_age
#     print('----', res)
# # except Exception as e:
# except TypeError as e:
#     # 当try抛出异常的时候，会执行except语句；如果try没有抛出异常，就不会执行except语句了。所以，except和try是互斥关系。
#     res = student_name + str(student_age)
#     print('----', res)

# input()函数：在控制台输入内容并获取相关结果的函数。
while True:
    number = input('请输入数字：')
    if number == '1':
        break
    print(number)



