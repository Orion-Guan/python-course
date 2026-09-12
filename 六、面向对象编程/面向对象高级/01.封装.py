"""
一、封装
封装就是将数据（成员属性）和 操作数据的方法（成员方法）放一起构成一个整体，这个整体就是一个类。

1.1 私有属性 和 私有方法
__属性名: 私有属性
__方法名: 私有方法

特点:
1、私有属性和私有方法只能在类的内部供类中的其他方法调用，不能在类的外部通过类的对象访问（在类内部使用）。
2、如果想在类的外部访问这些私有属性和方法，一般是通过在类中定义公共方法来实现间接访问，如：get、set方法

注意: Python是没有类似Java那样真正的私有机制，这些私有属性和方法之所以无法直接在类的外部访问，是因为Python内部通过改写属性和方法的名称来实现的，即在私有成员的名称前添加”_类名“。
"""


class Car:

    # 公共实例属性
    def __init__(self, name, color, speed, ower):
        self.name = name
        self.color = color
        self.speed = speed
        self.__ower = ower  # 私有属性

    def start(self):
        """
        公共实例方法
        :return:
        """
        return f"{self.name} 汽车 开始起步了！"

    def get_ower(self):
        """
        公共实例方法
        :return:
        """
        return self.__ower


    def __run(self):
        """
        私有方法
        :return:
        """
        return f"{self.name} 汽车 正在以每小时 {self.speed} 的速度行驶！"



car1 = Car("保时捷", "灰白色", 3.23, "Orion.Guan")

print(car1.name)
print(car1.start())

print(car1._Car__ower)
# print(car1.__ower)

# print(car1.__run())
print(car1._Car__run())

print(car1.get_ower())