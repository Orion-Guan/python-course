"""
一、函数变量作用域
    全局变量: 定义在函数之外的变量。可以在函数内外使用。
    局部变量: 在函数内定义的变量。只能在函数内部使用。
    注意：
    1、在函数内部对全局变量赋值实际上是在定义函数级别的局部变量，而非对全局变量赋值。
    2、如果想在函数内部对全局变量赋值，需要在赋值前使用 "global 全局变量名" 的形式声明。

二、函数传参
    2.1 位置参数: 实参与函数形参按位置顺序一一对应（类似Java、C）
    2.2 关键字参数: 给函数形参赋值时，采用"形参名 = 值"，对传参顺序无要求。
    2.3 位置&关键字参数混用: 必须位置参数在前、关键字参数在后。
            例如: function("Orion.Guan", "26", address="河南鹿邑", hobbies="唱歌、跑步、计算机")
    2.4 默认形参: 定义函数的时候其形参可以是"arg = 默认值"，如果调用函数没有为其赋值则使用默认值（*默认形参必须放在所有其他 形参之后）。
    2.5 可变参数:
            *args ------封装为元组、位置传参
            **kwargs ----封装为字典、关键字传参
        注意: 两者混用时，位置参数必须在关键字参数之前
    2.4 特殊参数: 将其他函数的函数名作为实参传递给某个函数的形参。形参就可以间接的调用另个函数（类似于函数的回调，Java中的方法引用）
                                        def plus(x,y):
                                            return x+y


                                        def calc(a,b,ops):
                                            return ops(a,b)    #函数回调

                                        calc(5,7,plus)

三、匿名函数
    定义:
        变量 = lambda 形参1, 形参2: 函数体(单行表达式)
        变量(实参1, 实参2)    #调用匿名函数

    说明:
    1、 lambda表达式会自动将函数体的结果值返回、不需要return。
    2、 如果无形参可以直接"lambda : 单行表达式"


"""

# play_switch = False
#
# print(f"1.{play_switch}")
#
# def play():
#     global play_switch  #告诉解释器函数内使用的此变量是全局变量，而不是定义的新局部变量
#     play_switch = True
#     print(f"2.{play_switch}")
#     pass
#
# play()
# print(f"3.{play_switch}")

#
# def function(name, age, address, hobbies = "默认形参，必须放在所有非默认形参后面"):
#     return name + age + address + hobbies
#
#
# rest = function("Orion.Guan", "26", "河南鹿邑", "唱歌、跑步、计算机")  # 位置传参
# print(rest)
#
# rest = function(age="26", address="河南鹿邑", hobbies="唱歌、跑步、计算机", name="Orion.Guan")  # 关键字传参
# print(rest)
#
# rest = function("Orion.Guan", "26", address="河南鹿邑", hobbies="唱歌、跑步、计算机")  # 混合传参
# print(rest)


# def func1(*args, **kwargs):
#     print(args, kwargs)
#     pass
#
# func1(1,None,False,2.34,"Orion", options1 = "少糖", options2 = 3.14)


#
# def plus(x,y):
#     return x+y
#
#
# def calc(a,b,ops):
#     return ops(a,b)    #函数回调
#
# calc(5,7,plus)


list1 = ["java", "Python", "C", "Go", "Sql"]

list1.sort(key=lambda str: len(str), reverse=False)  #手动指定排序规则: 根据字符串的长度对每个容器元素降序排序
print(list1)
