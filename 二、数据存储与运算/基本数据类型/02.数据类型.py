# 基本数据类型
# 1、int float str bool NoneType
#     1.1字符串三种写法:   单引号''  双引号""  多行三引号"""str"""
#     1.2转义字符:  单引号\'   双引号\"    换行\n    tab缩进\t
#     1.3类型转换（原变量类型不变）: str()、int()、float()、bool()
#
# 2、type(args)----查看参数所属数据类型
#    isinstance(对象，二、数据存储与运算)----判断对象是否属于指定数据类型，是返回True，否返回False
#
# 3、字符串拼接
#     3.1 str1 + str2: 使用"+"可以进行字符串的拼接
#     注意： 在python中+只能进行字符串类型的拼接，而不能将其他类型与字符串进行拼接；而Java可以--因为其底层会自动将其它类型转化为字符串
#
#     3.2 %s占位符实现字符串拼接（字符串格式化）
#     占位符实现字符串拼接--%s其中%表示占位符，s表示将后面的数据转换为字符串放到占位符位置（一一对应、有几个占位符就需要有几个数据；多个数据需要括号包裹，在Java中占位符需要与欲填充数据类型保持一致）。
#     string = "我是%s, 今年%d岁，我的专业是%s." %(name,age,profession)
#
#     3.3 使用f"内容{变量}"-----推荐
#     string2 = f"我是{name},今年{age},我所学的专业是{profession}"
#
# 4、用户输入与输出
#     input("控制台提示信息:")
#     print(数据)










# print(type(888))
# print(isinstance(888, int))
#
#
# print(type(3.14))
# print(isinstance(3.14, float))
#
# print(type(True))
# print(isinstance(True, bool))
#
#
# print(type(False))
# print(isinstance(False, bool))
#
# print(type("Hello, Orion.Guan"))
# print(isinstance("Hello, Orion.Guan", str))
#
# print(type(None))
# print(isinstance(None, NoneType))


# print(type('单引号\"字符串\n'))
# print(type("\t双引号\'字符串"))
# print(type("""三引号
# 字符串"""))

name = "Orion"
age = 26
profession = "Python"

# print("我是"+name+"，今年"+str(age)+"岁"+"，学的专业是"+profession)  #str(变量)： 返回变量的字符串类型

# strConcat = "人生苦短，"   "我学java+Python+Vue3+JS"
# print(strConcat)

# 占位符实现字符串拼接--%s其中%表示占位符，s表示将后面的数据转换为字符串放到占位符位置（一一对应、有几个占位符就需要有几个数据；多个数据需要括号包裹）。
# string = "我是%s, 今年%d岁，我的专业是%s." % (name, age, profession)
# print(string)

# 字符串格式化
# string2 = f"我是{name},今年{age},我所学的专业是{profession}"
# print(string2)

# 获取用户键盘的输入并将其在屏幕上输出

amount = 1000
manay = float(input("请输入取款金额:"))
remainAmount = amount - manay
print(f"余额:{remainAmount}")
