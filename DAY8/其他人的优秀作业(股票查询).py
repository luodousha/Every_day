# 打开文件，模式为只读，字符编码为utf-8
file = open(file="stock_data.txt", mode="r+", encoding="utf-8")
# 股票信息列名，第一行为列名，单独读取
column = file.readline().strip().split(",")
# 用于条件查询的列名
query_column = ["最新价", "换手率", "涨跌幅"]
# 股票字典用于存储文本信息
stock_dict = {}
for line in file:
    # 每行划分为列表，字典格式：{ key: 股票名称, values: 每只股票信息}
    line = line.strip().split(",")
    index_name = column.index("名称")  # 查询股票名称所在列的索引
    stock_dict[line[index_name]] = line
while True:
    # 查询股票结果计数
    count = 0
    # 输入查询条件
    print("--------------------------------------------------------------------------------------------")
    print("命令：1.模糊股票名, 2.['最新价', '换手率', '涨跌幅'] > or < 数值(int or float), 3.exit(退出程序)")
    choose = input("查询>>>:").strip()
    # 防止空条件——""
    if not choose:
        print("输入条件为空，请重新输入")
        continue
    # 大于条件查询
    if ">" in choose:
        # 根据大于号分隔
        factor = choose.split(">")
        # 判断大于号右边是否是整数
        if not factor[1].isdigit():
            # 用"."分隔将大于号右边分隔为两部分
            factor_right = factor[1].split(".", maxsplit=1)
            # 判断大于号右边是否是浮点数
            if not factor_right[0].isdigit() or not factor_right[1].isdigit():
                print("数值输入错误")
                continue
        # 判断大于号左边是否为可查询列
        if factor[0] in query_column:
            # 打印股票列名，便于查看
            print(column)
            # 查询列名在股票信息列名的索引
            index = column.index(factor[0])
            for i in stock_dict:
                # 判断股票字典相应列数值（去除数值单位符号，例：%）中是否大于条件数值
                if float(factor[1]) < float(stock_dict[i][index].strip("%")):
                    # 打印符合条件的股票并将结果计数+1
                    print(stock_dict[i])
                    count += 1
        else:
            print("名称输入错误,请重新输入")
            continue
    # 小于条件查询
    elif "<" in choose:
        # 根据小于号分隔
        factor = choose.split("<")
        # 判断大于号右边是否是整数
        if not factor[1].isdigit():
            # 用"."分隔将大于号右边分隔为两部分
            factor_right = factor[1].split(".", maxsplit=1)
            # 判断大于号右边是否是浮点数
            if not factor_right[0].isdigit() or not factor_right[1].isdigit():
                print("数值输入错误")
                continue
        # 判断大于号左边是否为可查询列
        if factor[0] in query_column:
            # 打印股票列名，便于查看
            print(column)
            # 查询列名在股票信息列名的索引
            index = column.index(factor[0])
            for i in stock_dict:
                # 判断股票字典相应列数值（去除数值单位符号，例：%）中是否大于条件数值
                if float(factor[1]) > float(stock_dict[i][index].strip("%")):
                    # 打印符合条件的股票并将结果计数+1
                    print(stock_dict[i])
                    count += 1
        else:
            print("条件输入错误,请重新输入")
            continue
    # 退出程序
    elif choose.lower() == "exit":
        break
    # 名称条件查询
    else:
        # 打印股票列名，便于查看
        print(column)
        # 循环字典keys模糊查询
        for i in stock_dict:
            if choose in i:
                print(stock_dict[i])
                count += 1
        if count == 0:
            print("无效名称，请重新输入。")
            continue
    print("结果总计:", count)
    if count == 0:
        print("无符合结果。")