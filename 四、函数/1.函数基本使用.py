"""
一、函数(实现代码复用)
    定义:
            del 函数名(形参列表):
                函数体

    函数调用: 函数名(实参列表)

注意：
1、函数必须先定义后调用(*java无要求)
2、函数只有在调用时才会执行、定义时不会执行
3、python通过缩进来描述语句层级归属关系

"""



#定义函数
def funcName(arg1, arg2):
    print(arg1, arg2)
    return f"{arg1} + {arg2} = {arg1 + arg2}"

#调用函数
value = funcName(3,4)
print(value)