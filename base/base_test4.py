# 关于字典的练习
phone_info = [{'name':'vivox9', 'price':'1200', 'count':'30'}, {'name':'iphone6', 'price':'2000', 'count':'55'}, {'name':'iphone6s', 'price':'2200', 'count':'120'}, {'name':'iphone7', 'price':'4000', 'count':'80'}, {'name':'iphone7s', 'price':'4200', 'count':'90'}, {'name':'iphone8', 'price':'5200', 'count':'70'}]

def select_phone(is_detail):
    """
    查询手机品牌
    :param is_detail: bool类型的值，True就是手机品牌的详细信息；反之就是简要信息
    :return:
    """
    for index, p_dict in enumerate(phone_info):
        if is_detail:
            print('{}-名称：{}; 价格：{}; 库存：{};'.format(index+1, p_dict['name'], p_dict['price'], p_dict['count']))
        else:
            print('{}-名称：{};'.format(index + 1, p_dict['name']))

def detail_info_and_back():
    """
    根据产品序号查看详情
    :return:
    """
    print('1-选择产品序号查看详情')
    print('2-返回')
    number = int(input('请选择操作：'))
    if number == 1:
        product_id = int(input('输入产品编号：'))
        # 根据输入的产品id(就是产品编号)，从phone_info这个列表中获取对应的字典信息。
        p_dict = phone_info[product_id-1]
        print('{}-名称：{}; 价格：{}; 库存：{};'.format(product_id, p_dict['name'], p_dict['price'], p_dict['count']))
        # 是否购买，如果购买需要将p_dict中的库存数量相应的减少。
        buy_and_back(p_dict)
    else:
        return

def buy_and_back(p_dict):
    """
    购买或者返回
    :param p_dict: 就是根据用户输入的产品id(product_id)，获取的产品的详细信息。
    :return:
    """
    print('1-购买')
    print('2-返回')
    number = int(input('请选择操作：'))
    if number == 1:
        # 在购买产品之前，先查询以下这个手机的库存。
        count = int(p_dict['count'])
        print('当前商品剩余库存数量：{}台。'.format(count))
        buy_count = int(input('请输入购买数量：'))
        while buy_count <= 0 or buy_count > count:
            buy_count = int(input('请输入正确的购买数量：'))
        # 修改该产品的库存
        count = str(count - buy_count)
        p_dict['count'] = count
        # 如果剩余库存数量为0，可以将该产品l字典从列表中移除。
        if count == '0':
            phone_info.remove(p_dict)
        print('购买成功，数量：{}台。'.format(count))
    else:
        return

def add_and_update_phone():
    """
    添加或者更改产品的信息
    :return:
    """
    print('1-添加新产品')
    print('2-修改原有产品')
    number = int(input('请选择操作：'))
    if number == 1:
        new_phone_name = input('输入新产品名称：')
        new_phone_price = input('输入新产品价格：')
        new_phone_count = input('输入新产品库存：')
        # 将这些新产品的信息封装到字典中，再将这个字典添加到列表phone_info中即可。
        p_dict = {'name': new_phone_name, 'price': new_phone_price, 'count': new_phone_count}
        phone_info.append(p_dict)
        print('新产品添加成功。')
    else:
        # 修改之前，先查询所有产品信息，方便用户选择
        select_phone(is_detail=True)
        index = int(input('请输入产品编号：')) - 1
        p_dict = phone_info[index]
        p_dict['name'] = input('输入修改名称：')
        p_dict['price'] = input('输入修改价格：')
        p_dict['count'] = input('输入修改库存：')
        print('产品修改成功。')

def delete_phone():
    print('1-根据产品编号删除')
    print('2-删除所有产品')
    print('3-返回')
    number = int(input('请选择操作：'))
    if number == 1:
        product_id = int(input('输入产品编号：')) - 1
        del phone_info[product_id]
        print('删除产品成功。')
    elif number == 2:
        phone_info.clear()
        print('所有产品删除成功。')
    else:
        return

while True:
    print("""
    1-查看所有品牌
    2-添加或修改手机品牌信息
    3-删除手机品牌信息
    4-退出程序
    """)
    number = int(input('请选择操作：'))
    if number == 1:
        select_phone(False)
        detail_info_and_back()
    elif number == 2:
        add_and_update_phone()
    elif number == 3:
        select_phone(True)
        delete_phone()
    else:
        break

