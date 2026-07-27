"""
一、条件判断语句（支持嵌套--注意缩进）
1. if 条件:
        代码块

2. if 条件:
        代码块
   else:
       代码块

3. if 条件:
        代码块
   elif 条件:
       代码块
   elif 条件:
       代码块
   else:
       代码块


二、结构模式匹配
4. match 变量:
        case 数据:
            代码块
        case 数据 | 数据:   # "|"表示或的关系
            代码块
        case 数据 if 条件表达式:  # 只有if条件成立才会去匹配判断
            代码块
        case _:         # "_"类似Java中switch中的default
            代码块
"""






# score = 700
#
# if score > 680:
#     print("恭喜进入清华大学")
#     print("你将开启新的人生")
# print("欢迎就业")



"""
#判断闰年还是平年
year = int(input("请输入年份:"))
if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
    print(f"{year}是闰年")
else:
    print(f"{year}是平年")
"""



"""
# 判断用户是否合法登录
user_name = input("请输入用户名:")
passwd = input("请输入密码:")

if user_name == "Orion.Guan" and passwd == "Root123":
    print("登录成功!")
elif user_name == "admin" and passwd == "admin123":
    print("登录成功!")
elif user_name == "root" and passwd == "root123":
    print("登录成功!")
else:
    print("登录失败")
"""




"""
#判断是否为三角形
a = int(input("请输入三角形第一个边:"))
b = int(input("请输入三角形第二个边:"))
c = int(input("请输入三角形第三个边:"))

if a + b > c  and a + c > b and b + c > a:
    if a == b and b == c:
        print(f"{a}, {b}, {c}构成等边三角形~")
    if a == b or a == c or b == c:
        print(f"{a}, {b}, {c}构成等腰三角形~")
    else:
        print(f"{a}, {b}, {c}构成普通三角形~")
    pass  #pass空语句: 代码占位标识（先空着，等会在补充该处代码）
else:
    print(f"{a}, {b}, {c}不是三角形!")
"""


#模式匹配match---case
a = float(input("请输入数字1:"))
b = float(input("请输入数字2:"))
operator = input("请输入操作符:")

match operator:
    case "+":
        print(f"{a} + {b} = {a + b}")
    case "-":
        print(f"{a} - {b} = {a - b}")
    case "*":
        print(f"{a} * {b} = {a * b}")
    case "/" | "//" if b != 0.0:            #只有if b != 0.0条件成立，才会去匹配判断
        if operator == "/":
            print(f"{a} / {b} = {a / b}")
        else:
            print(f"{a} // {b} = {a // b}")
    case "**":
        print(f"{a} ** {b} = {a ** b}")
    case _:
        print(f"{operator}操作符暂不支持，请待更新~")