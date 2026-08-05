"""
一、字典（Map接口）
    定义:  dict1 = {"Orion":23, "youran": 24, 1:"Hello", True:False, 2.3:3.1415926, (1,):"元组"}
    取值: dict1[key]
    修改值: dict1[key] = value

    特定:
    1、key只能是不可变类型，不能是list、set、dict类型
    2、key的值是唯一的，重复的key会覆盖之前的key:value
    3、字典无索引下标，只能根据key来获取value


二、常用内置方法
    # 新增键值对（左边的键存在则修改，不存在则新增元素）
    dict1["xiongda"] = 34.45

    # 修改字典的值（左边的键存在则修改，不存在则新增元素）
    dict1["Orion"] = 34

    # 删除键值对
    value = dict1.pop("xiongda")   #或者: del dict1["xiongda"]

    # 查询值
    dict1[(1,)]         根据key获取value
    dict1.get("Orion")  根据key获取value

    dict1.keys()        获取所有的key
    dict1.values()      获取所有的value
    dict1.items()       获取所有的键值对



"""

#
# #定义dict
# dict1 = {"Orion": 23, "youran": 24, 1: "Hello", True: False, 2.3: 3.1415926, (1,): "元组"}
#
# print(dict1, type(dict1))
#
# print(type({}), dict(dict1))
#
# #获取字典
# print(dict1["Orion"])
#
# #修改字典的值
# dict1["Orion"] = 34
# print(dict1)
#
#
#
# #新增键值对
# dict1["xiongda"] = 34.45
# print(dict1)
#
# #修改键值对
# dict1["xiongda"] = None
# print(dict1)
#
# #删除键值对
# value = dict1.pop("xiongda")   #或者: del dict1["xiongda"]
# print(value,dict1)
#
# #查询值
# print(dict1[(1,)])
# print(dict1.get("Orion"))
# print(f"{dict1.keys()} \n{dict1.values()}, \n{dict1.items()}")
# print(type(dict1.keys()), type(dict1.values()), type(dict1.items()))
#
#
# #循环遍历字典获取值
# for key in dict1:
#     print(f"{key}: {dict1[key]}",end = ", ")
#
#
# for key, value  in dict1.items():
#     print(f"{key}: {value}",end = ", ")




 

# 购物车案例
carts = {}
title = """
############ ~欢迎光临山月时光购物之旅~ ############     
#                  1. 添加购物车                #   
#                  2. 删除购物车                #   
#                  3. 修改购物车                #   
#                  4. 查询购物车                #   
#                  5. 退出购物车                #
############ ~欢迎光临山月时光购物之旅~ ############
"""

while True:
    print(title)
    opsnum = input("请选择操作(1-5):")
    match opsnum:
        case "1":
            good_name = input("请输入商品名称/>")
            # 校验商品是否已存在
            if good_name in carts:
                print("抱歉! 该商品已加入购1物车!")
                continue
            good_prices = input("请输入商品价格/>")
            good_quantity = input("请输入商品数量/>")
            carts[good_name] = {"prices": good_prices, "quantity": good_quantity}
            print("商品添加成功~")

        case "2":
            good_name = input("请输入要删除的商品名称/>")
            # 只删除存在的商品
            if good_name not in carts:
                print("抱歉! 该商品未加入购物车，无法删除!")
            else:
                del carts[good_name]
                print("商品删除成功~")
        case "3":
            good_name = input("请输入修改商品名称/>")
            # 校验商品是否已存在
            if good_name not in carts:
                print("抱歉! 该商品未加入购物车，无法修改!")
                continue
            good_prices = input("请输入最新商品价格/>")
            good_quantity = input("请输最新商品数量/>")
            carts[good_name] = {"prices": good_prices, "quantity": good_quantity}
            print("商品修改成功~")
        case "4":
            # 判断购物车是否为空
            if len(list(carts.keys())) < 1:
                print("购物车空空如也~")
                continue
            for good_name, good_info in carts.items():  # 元组基本解包
                print(f"商品名称:{good_name} \t商品价格:{good_info["prices"]} \t商品数量:{good_info["quantity"]}")
                print("购物车商品查询完毕~")
        case "5":
            print("goodbye 再见朋友🎈")
            break
        case _:
            print("操作数字输入有误!")
