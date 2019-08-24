# 个人所得税练习讲解
while True:
    gz = int(input('输入税前工资：'))
    # 计算三险一金，需要先获取基准工资的值
    base_gz = 0
    if gz > 7662:
        # 税前工资 > 7662，使用上限7662计算三险一金。
        base_gz = 7662
    else:
        # 税前工资 <= 7662，使用税前工资计算三险一金。
        base_gz = gz

    # 计算应纳税所得额
    sxyj = base_gz * 0.225
    ynsd = gz - sxyj - 5000

    # 根据所得额所在的范围，确定税率和扣除数
    sl = 0
    kcs = 0
    if ynsd <= 0:
        print('所得额<=0，不需要缴纳个人所得税')
    else:
        # 需要缴税
        if ynsd <= 3000:
            sl = 0.03
            kcs = 0
        elif ynsd <= 12000:
            sl = 0.1
            kcs = 210
        elif ynsd <= 25000:
            sl = 0.2
            kcs = 1410
        elif ynsd <= 35000:
            sl = 0.25
            kcs = 2660
        elif ynsd <= 55000:
            sl = 0.3
            kcs = 4410
        elif ynsd <= 80000:
            sl = 0.35
            kcs = 7160
        else:
            sl = 0.45
            kcs = 15160

        # 计算税额
        money = ynsd * sl - kcs
        print('需要缴税：', money)
