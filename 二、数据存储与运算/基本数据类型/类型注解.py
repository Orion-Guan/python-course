"""
一、类型注解（方便开发者发现程序潜在的问题，并不产生实际运行强制效果）
Python是动态类型语言，添加的类型注解只是在，赋值的类型与实际变量所属类型不一致时的提示，并不是强制约束!!!
变量: 数据类型     #常见的数据类型(int、float、str、bool、None、list、tuple、set、dict)
例如: hobbies: list[str | int] = ["吃饭","睡觉",2121]     # 列表中存放的元素可以是字符串或整型


二、类型推断
如果给变量赋值、变量运算等场景，python会自动根据赋值的字面量所属数据类型来推断出变量的数据类型，无需开发者在编码中手动声明类型注解。


三、函数类型注解
def 函数名(形参: 类型1, 形参: 类型1 | 类型2 = 默认值, *args: 只需指定元组中元素的数据类型即可) ->返回值类型:
    函数体


"""




# user_name = "Orion"
# age = 18
# isStrict = True
# isTeacher = None
# hobbies = ("唱歌","跑步", "睡觉", "打豆豆", 20001314)




# 类型注解
user_name: str = "Orion"
age: int = 18
isStrict: bool = True
isTeacher: None = None
hobbies: list[str | int] = ["吃饭", "睡觉", 2121]

print(age)
age = 25.65  # python类型注解只做提示说明，无强制约束。
print(age)
