# 类和对象
# 类：主要是将函数(方法)和变量(属性)封装到一个类中，方便引用和管理。
# 对象：它是类的实例，主要负责调用类中封装的属性和方法。

# 知识点：
# 1. self和super关键字的区别；
# 2. 一些内置的装饰器: @property、@classmethod、@staticmethod；
# 3. 指针和内存地址之间的关系；
# 4. 类中私有变量的设置；
# 5. 类的继承的作用、特点及使用；
# 6. 类中方法的重写；
# 7. 类的多继承；

# object是Python中类的根类、最底层的类，所有的类都最终继承于object类；
class People(object):
    """
    自定义类的描述
    """
    # 类属性
    name = '123'

    def __init__(self, u_name, u_age):
        """
        该方法就是对象的初始化方法，当对象被创建完成之后，会自动调用这个方法，用于给对象初始化一些属性。
        对象的创建使用的__new__(self)方法，该方法会给对象开辟内存空间。
        self: 表示当前类的对象，类似于this。

        当创建一个People对象p1，那么程序就会将类中的属性拷贝到对象p1的内存中；
        当创建一个People对象p2，那么程序就会将类中的属性拷贝到对象p2的内存中；

        所以，当p1对象去调用这些属性和方法的时候，self指的就是p1对象；
        所以，当p2对象去调用这些属性和方法的时候，self指的就是p2对象；

        总结：哪一个对象在调用类中的方法和属性，self指的就是这个对象；
        """
        # 给对象初始化属性，__init__()中的属性称为对象属性或者实例属性，这些属性主要就是用来保存数据的。
        # 而这些被保存的数据是放在对象的内存空间中的。
        self.u_name = u_name
        self.u_age = u_age

    def add_student(self):
        print('self = ', self)
        # self不需要我们给它传递实参，self的实参是由Python解释器传递的。自定义的参数可以写在self的后面。
        print(self.u_age, self.u_name)

    @classmethod
    def update_student(cls, number):
        print('----', cls, number)

People.name = 111

p1 = People('张三1', 20)
# print('p1 = ', p1.u_age)
# p1.add_student()
# p1.update_student(100)
print('----', p1.name)

p2 = People('张三2', 20)
# print('p2 = ', p2.u_age)
# p2.add_student()
# p2.update_student(200)
print('---', p2.name)

# 类属性：所有的对象公有的属性，如果类修改了类属性的值，其它对象在调用类属性的时候也会受到影响。
# 类属性既可以使用类名Poeple调用，也可以使用对象p1/p2调用。
# 对象属性：所有的对象都拥有自己的属性，放在自己的内存空间中，修改实例属性的值只对自己产生影响，
# 不会对别的对象的属性产生影响。对象属性(实例属性)只能由实例对象调用，不能使用类名People调用。
print(People.name, p1.name, p2.name)

# 静态方法：
# 类方法@classmethod def replceSpace(cls)：类方法既可以使用类名Poeple调用，也可以使用对象p1/p2调用。
# 对象方法(实例方法)def insert(self)：对象方法(实例方法)只能由实例对象调用，不能使用类名People调用。

# 工具类()/数据操作类
class DBTool(object):
    """
    处理数据库的工具类
    """
    # @classmethod：装饰器
    @classmethod
    def insert(cls):
        # cls指代的是当前类People，不能再使用self了。
        pass

    @classmethod
    def update(cls):
        pass

class StrTool(object):
    """
    处理字符串的工具类
    """

    @classmethod
    def removeSpace(cls):
        pass

    @classmethod
    def replceSpace(cls):
        pass

# db = DBTool() # 占用内存
# s = StrTool() # 占用内存

DBTool.insert()
DBTool.update()

# 练习：学员管理系统 将数据保存到本地数据库中进行持久化(sqlite3)
# 要求：
#     1. 一个工具类，主要封装数据库中表的增删该查方法；
#     2. 一个数据类，主要封装和数据相关的方法和属性；
# print('------------------')
# class P(object):
#     def show(self):
#         print('======',self.name)
#
# p = P()
# # 对象动态绑定属性。
# p.name = 120
# print(p.name)
# p.show()