"""
一、while循环语句
while 条件表达式:
    循环体
else:                #可选
    循环正常结束语句



二、for循环语句
for 元素 in 数据集:
    循环体
else:                #循环正常遍历完毕执行（可选）
    循环正常结束语句



三、字符序列生成器(通常配合for循环使用)
方式一：生成从0到end之间的数字序列，但不含end
range(end)

方式二： 生成从start到end之间的数字序列，但不含end
range(start, end)

方式三： 生成从start到end之间步长为step的所有数字序列, 但不含end
range(start, end, step)


四、break 与 continue关键字
break: 结束本层级的循环语句。如果本层级的循环结束语句有else，则else所处代码块不会执行。
continue: 跳过本层级的本轮循环，开始下轮循环。

"""




# num = 1
# while num <= 10:
#     print(f"{num}.Orion.Guan cheer up!")
#     num += 1
# else:  #可选
#     print("while循环语句正常结束!")





#计算1-100偶数之和
# sum = 0
# i = 1
# while i <= 100:
#     if i % 2 == 0:
#         sum += i
#     i += 1
# print(f"1-100之间的偶数之和:{sum}")





# msg = input("请输入字符串:")
# for char in msg:
#     print(f"{char}")
# else:
#     print("for循环轮询遍历完毕.")





#计算1-100之家奇数之和
# total = 0
# for num in range(1,101,2):
#     total += num
# else:
#     print(f"1-100奇数之和:{total}")




#计算300-500之间3的倍数之和
# sum = 0
# for item in range(100,501):
#     if item % 3 == 0:
#         sum += item
# print(f"100-500之间3的倍数之和:{sum}")



#星星点灯
# length = int(input("请输入长:"))
# witch = int(input("请输入宽:"))
# i = 0
# for row in range(witch):
#     while i < length:
#         print("*", end = "")   #在输出的字符串最后追加特定字符串,默认是换行符\n
#         i += 1
#     else:
#         print()
#         i = 0  #每行结束重置i的值为0




#打印99乘法表（规律：1.每行要打印的个数等于其所在的行数 2.总共要输出9行）
# for row in range(1, 10):
#     for col in range(1, row + 1):
#         print(f"{col} x {row} = {col * row}", end = "\t")
#     else:
#         print()
# else:
#     print("九九乘法表打印完毕~")




#模拟B站用户登录
while True:
    #等待用户输入
    username = input("请输入用户名:")
    passwd = input("请输入密码:")

    #对用户名和密码做非空校验
    if username == "" or passwd == "":
        print("用户名和密码不能为空")
        continue   #跳出本轮循环，继续下轮循环

    #校验用户名和密码
    if username == "admin" and passwd == "Root1213":
        print("恭喜登录成功!")
        break   #结束本层级的循环

    if username == "root" and passwd == "root123":
        print("恭喜登录成功!")
        break  # 结束本层级的循环

    if username == "admin" and passwd == "admin123":
        print("恭喜登录成功!")
        break  # 结束本层级的循环

    print("用户名和密码有误!")
else:
    print("欢迎进入B站首页~")   #因为登录成功是通过break关键字结束循环的而非正常循环退出，因此此处代码不可达