# 模拟通讯录查询的练习。
# 晚上扩展练习：完全仿照手机通讯录，实现联系人的添加，删除，查询，注意首字母相同的归为一组。

phone_list = ['z1', 'a1', 'z2', 'a2', 'b1']

# 对phone_list原始数据先分类整理，首字母相同的归为一组，整理之后得到：
# {'z': ['z1', 'z2'], 'a': ['a1', 'a2'], 'b': ['b1']}
phone_dict = {}

for phone in phone_list:
    # 从字符串元素中，获取第一个字符，利用字符串的切片。‘z1’ : 集合，z是索引为0的元素，1是索引为1的元素。
    first_char = phone[0]
    # 要利用字符串的首字母生成字典中的键。先判断字典中是否已经存在这个键，如果已经存在了，不需要生成这个键，只需要将这个值保存到这个键对应的列表中即可。
    if first_char in phone_dict:
        # 如果字典存在这个键，只需要将这个键对应的list列表获取出来，将这个字符串保存在列表中即可。
        res_list = phone_dict[first_char]
        res_list.append(phone)
    else:
        phone_dict[first_char] = [phone]

print(phone_dict)

while True:
    print('1-查询')
    print('2-退出')
    number = input('选择操作编号：')
    while number != '1' and number != '2':
        # 输入不存在的编号，需要重新输入
        number = input('输入不存在的编号，需要重新输入编号：')
    if number == '1':
        char = input('输入查询首字母：')
        if char in phone_dict:
            res_list = phone_dict[char]
            # 如果遍历列表的时候，需要同时遍历出元素和元素的索引。
            for index, item in enumerate(res_list):
                # index是元素的索引值
                # item是列表中的元素值
                print(index+1, '.', item)
            print('\n')
        else:
            print('没有相关数据')
    else:
        break
