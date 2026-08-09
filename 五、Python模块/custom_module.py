#__all__特殊内置变量: 定义其他模块使用"from custom_module import *" 时，*模式匹配到的当前模块哪些功能，即哪些功能可以被*导入使用。
__all__ = ['get_area', "PI"]


#定义常量(规范大写)
PI = 3.14159265358
RADIUS = 4


def get_area(radius: float|int) -> float|int:
    return PI * radius ** 2



# 此代码只在当前模块执行，被其他模块文件导入时不会执行（模块测试代码）
if __name__ == '__main__':     # __name__:Python的内置特殊变量。在当模块中表示'__main__'，若当前模块被其他模块导入并执行时该变量的值为模块名即'custom_module'
    print(get_area(RADIUS))