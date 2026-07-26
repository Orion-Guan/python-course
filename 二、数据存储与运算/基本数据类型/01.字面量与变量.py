# 字面量（二、数据存储与运算）: 在程序中书写的固定值


# 标识符： 给变量、函数、类等起的名字方便程序员辨别
# 说明：
# 1.由数字、字母、下划线组成
# 2.不能以数字开头、不能包含特殊符号和python关键字


# 变量---用来存放单个字面量值的容器、变量中的值是可以变化的，因此叫变量。
# 说明:
# 1. 在Java中定义变量需指定数据类型而python无需指定；在Java中一个变量只能存放同类型字面量而python可存放任意类型。
# 2. 在Java中打印输出语句入参只能是单个字符串而无法像python一样输出多个”，“分割的类型数据。
# 3. python中变量定义必须初始化赋值，而Java中允许变量为空值。







print(1314)  # 整数int
print(3.14259165358)  # 小数/浮点数float、double

print("人生苦短，我用python!")  # 字符串

# 布尔类型在设计到数学计算时会自动转换为对应数字
print(True)  # 布尔类型boolean---本质1
print(False)  # 布尔类型----本质0
print(True + 1)  # 输出2
print(False - 1)  # 输出-1

print(None)  # 空值类型-----java中是null





score = 100
print(score)

score = False
print(score)

name, sex, skills = "Orion.Guan", '男', """Java&python"""
print(name, sex, skills)

# 案例： 多个变量之间的值交换存储需要借助临时变量来暂存某个变量的值
a = 10
b = 20
c = 30
temp = a
a = b
b = c
c = temp
print(a, b, c)  # 20 30 10


