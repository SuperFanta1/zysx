# Python中的函数定义
# def sum():
#     print('123')
# sum()

# 参数类型：必传参数、关键字参数、缺省参数、万能参数。
# 必传参数：形参和实参的个数必须保持一致，不一致就会出现异常。
def sum(age, name):
    print(age, name)
sum(20, '张三')

def sum1(age, is_male=False, name=None):
    # is_male和name称为缺省参数：这两个参数可以传实参，也可以不传实参。相当于这两个参数有默认值。
    print(age, is_male, name)

sum1(40)
sum1(50, True, '张三')
# 关键字参数
sum1(age=10, name='张三')

def sum2(*args, **kwargs):
    # *args(元组)和**kwargs(字典)就是万能参数：可以传递任意参数，这两个形参都能接收
    print('args = ', args)
    print('kwargs = ', kwargs)

sum2(1, 2, 3)
sum2(name='张三', age=20, is_male=False)
sum2(1, 2, name='1', age=222)

# 函数内部返回值
def sum3():
    # 可以返回多个值
    return '123', 20, True
result = sum3()
print(type(result))
print(result)

# 局部变量和全局变量
# 局部变量：函数内部声明的变量是局部变量，局部变量的作用域是只能在当前函数内部使用，在函数执行完毕之后，这些局部变量所占用的内存空间会被系统回收，那么局部变量就不能使用了。
# 全局变量：在函数外部声明的变量一般称为全局变量，全局变量的作用域是整个.py文件都可以使用，在程序执行完毕之后，全局变量占用内存会被系统回收。


#
# def show():
#     # u_name和u_age就是局部变量。
#     u_name = '1'
#     u_age = 20
#     print(u_name, u_age)
#
# print(u_name)

u_name = 'a' # 全局变量
def show():
    # 如果在函数内部，只是引用这个全局变量的值，直接引用即可。
    # print(u_name)
    # res = '姓名是：' + u_name
    # print(res)

    # 如果需要在函数内部，修改这个全局变量u_name的值，需要使用global关键字声明
    global u_name
    u_name = 'abc'

show()
print(u_name)
