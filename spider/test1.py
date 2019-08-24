def show(num):
    res = num + 1
    return res

print(__name__)

# __name__：如果是运行当前文件，它的值就是__main__，如果是其它模块引入了当前模块的内容，它的值就是当前模块的名称。
# 通过这个判断，可以知道是在运行当前文件，还是被其它模块在引入。
if __name__ == '__main__':
    # show()
    # map()：Python中的高阶函数，可以将数据和函数进行关系映射。
    # 作用：可以将列表/字符串/元组中的每一个元素，依次传给show函数，并获取show函数的返回值。
    datas = map(show, [1,2,3,4,5])
    print(type(datas))

    for data in datas:
        print(data)

    # 列表生成式：语法：[简单的for循环语句]，作用是方便快捷生成一个列表。
    # for前面的变量是最终的结果
    print([x for x in range(1, 11) if x % 2 == 0])

    name = ['张三', '李四']
    new_name = []
    for char in name:
        first = char[0]
        if first == '张':
            new_name.append(char)
    print(new_name)

    print([n for n in name if n[0] == '张'])
