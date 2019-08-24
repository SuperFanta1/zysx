# list+函数: 学员管理系统练习
# [['张三', ], [学员信息], [学员信息], [学员信息]]

# Python中的模块和包
# 模块：一个.py文件就称为一个模块，一个模块可以引入另外一个模块中的变量、函数、类等内容。
# 包：只要一个文件夹中含有__init__.py文件，那么这个文件夹就称为包文件夹，包主要是用于管理模块的。

# import os：将os.py中的所有内容都进行引入；
import os

# from os import read, write: 只引入os.py模块中的read()函数和write()函数，其它的不引入。
# from os import read, write


# 声明外层的列表，接下来会将每一个学员的信息封装成一个小列表，将每一个学员所在的小列表保存在all_stu_list这个外层的大列表中。
all_stu_list = []

def add_student():
    """
    该函数是用于添加学员信息的函数
    :return: None
    """
    s_name = input('输入学员姓名：')
    s_age = input('输入学员年龄：')

    s_list = [s_name, s_age]
    all_stu_list.append(s_list)

    print('\n学员信息添加完成\n')

def select_student():
    """
    查询学员信息的函数
    :return: None
    """
    for index, info_list in enumerate(all_stu_list):
        print(index+1, '.', info_list[0], info_list[1])
    print('\n学员信息查询完成\n')

def update_student():
    """
    修改学员信息的函数
    :return:
    """
    # 在修改学员信息之前，先查询所有学员信息，方便选择学员
    select_student()
    number = int(input('请输入修改学员的编号：'))
    while number < 1 or number > len(all_stu_list):
        number = int(input('没有该学员，请重新输入修改学员的编号：'))
    # 根据输入的编号转化成索引值，将学员对应的小列表获取出来
    info_list = all_stu_list[number - 1]
    re_name = input('请输入新的姓名(%s): ' % info_list[0])
    re_age = input('请输入新的年龄(%s): ' % info_list[1])

    info_list[0] = re_name
    info_list[1] = re_age

    print('\n学员信息修改完成\n')

def delete_student():
    """
    删除学员信息函数
    :return:
    """
    print('''
    1-根据序号删除学员信息
    2-根据学院名称删除学员信息
    3-删除所有学员信息
    ''')
    number = int(input('请选择操作：'))
    while number < 1 or number > 3:
        number = input('请重新选择操作：')
    if number == 1:
        select_student()
        num = int(input('请输入删除的学员编号：'))
        all_stu_list.pop(num-1)
    elif number == 2:
        select_student()
        name = input('请输入删除的学员姓名：')
        for index, info_list in enumerate(all_stu_list):
            # 判断输入的name的值，在info_list列表中是否存，如果存在，将这个小列表info_list删除，反之，不删除。
            if name in info_list:
                all_stu_list.pop(index)
            else:
                # print('没有这个学员')
                pass
    elif number == 3:
        # all_stu_list.clear()
        while len(all_stu_list):
            del all_stu_list[0]
        print('\n数据删除成功\n')

def save_data():
    """
    将增加、修改、删除之后的大列表中的数据，保存到本地文件中进行持久化存储。
    :return:
    """
    # 利用os模块生成一个.txt的文件
    # open()函数参数：1. 本地文件名称；2. 以哪种模式(r(read)，w(write))操作stu.txt文件；
    # 注意：如果open()函数使用的是 'w' 写入模式，当前目录下如果不存在stu.txt文件，os模块会自动创建这个文件；
    file = open('stu.txt', 'w')
    for idx, info_list in enumerate(all_stu_list):
        for info in info_list:
            # 说明是最后一个小列表
            file.write(info + ' ')
        # 判断：如果不是最后一条数据，写入完成，加入换行符；如果是最后一条数据，不加入换行符；
        if idx + 1 != len(all_stu_list):
            file.write('\n')

    # 关闭文件
    file.close()

def read_data():
    """
    读取本地txt文件中的内容
    :return:
    """
    # os.path.exists('文件路径')：判断当前目录下是否存在stu.txt文件，如果存在会返回True；反之则返回False.
    if os.path.exists('stu.txt'):
        f = open('stu.txt', 'r')
        # 将txt文件中的所有内容(字符串)获取出来
        # readlines(): 会读取文件中每一行内容，并且会将每一行数据作为一个单独的元素保存在列表中。所以这个函数的返回值是一个列表。
        info_list = f.readlines()
        print(info_list)
        # ['a 10 \n', 'b 20 \n', 'c 30 ']
        # 对info_list中的元素进行整理，整理成列表嵌套的结构[['a', 10], []]
        # 字符串相关方法：find()、findall()、index()、strip()、split()、replace()
        # strip()：去除字符串前后两端(不包含中间)的指定字符。
        # split()：根据指定字符对某一个字符串进行切割，该函数返回一个列表。
        for info in info_list:
            # 'a 10 \n' -> ['a', 10]
            res = info.strip('\n').strip(' ') # res = 'a 10'
            result = res.split(' ') # result = ['a', 10]
            all_stu_list.append(result)

read_data()

while True:
    print('''
    1-添加学员
    2-修改学员
    3-查询学员
    4-删除学员
    0-退出
    ''')
    number = input('请选择操作：')
    while number < '0' or number > '4':
        number = input('请重新选择操作：')
    if number == '1':
        add_student()
        save_data()
    elif number == '2':
        update_student()
        save_data()
    elif number == '3':
        select_student()
    elif number == '4':
        delete_student()
        save_data()
    elif number == '0':
        break
