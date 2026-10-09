import functools
"""
一、装饰器
装饰器是用于修改函数或方法行为的高级Python功能。装饰器本质上是一个函数或者是类的实例，它接受一个函数作为参数，并返回一个函数或者类的实例。
功能类似于Java中的 “注解 + AOP”实现方法的增强，装饰器可以用于日志记录、权限检查、事务处理等方面。

二、类型
1. 函数装饰器
2. 类装饰器

"""


#1. 函数装饰器
def log(name):
    def decorator(func):
        @functools.wraps(func)  # 保留被装饰函数singing()的元信息
        def wrapper(*args, **kwargs):
            print(f"{name}唱歌开始了。。。。")
            func(*args, **kwargs)   # 调用被装饰函数，这里是singing()函数
            print(f"{name}唱歌结束了。。。。")
        return wrapper
    return decorator



@log("魅友KTV")   #实际上该函数已经指向了wrapper函数
def singing():
    """唱歌测试"""
    print("关山月正在唱歌...")

singing()    #实际上调用的是wrapper函数

print(singing.__name__)
print(singing.__doc__)






#2. 类装饰器
class LogClass:
    def __init__(self, func):
        self.name = "魅友类超级KTV"
        self.__funcName = func
    #让类的实例可以像函数一样调用如： 实例对象()
    def __call__(self, *args, **kwargs):
        print("\nwrapper函数执行了。。。。")
        print(f"{self.name}唱歌开始了。。。。")
        self.__funcName(*args, **kwargs)   # 调用被装饰函数，这里是singing()函数
        print(f"{self.name}唱歌结束了。。。。")


@LogClass
def singingLogClass():    #该函数名已经变成 singingLogClass = LogClass(singingLogClass) 的类的实例对象了
    """singingClass唱歌测试"""
    print("singingClass关山月正在唱歌...")


singingLogClass()   # 此处实际调用的是LogClass类的实例对象中的__call__方法


