"""
一、继承
继承主要是为了解决在创建类时，对于多个类都需要的成员属性和方法，如果都写在每个类中，就会导致代码重复，不利于维护。为了解决成员属性和方法重复在每个类中编写，
我们就可以把这些每个类在创建时都需要的公共属性和方法抽取到一个父类中，然后让子类继承父类，这样子类就会拥有父类的成员属性和方法，而不用每个子类都编写相同的代码.

class 子类名(父类名):
    pass


说明:
1、定义的类如果没有显式使用括号指定要继承的父类，则默认继承自object类，即所有类都是object类的子类。
2、子类只能继承父类中所有公有的成员属性和方法，无法继承父类中的私有属性和方法。
"""





class Car:

    # 公共实例属性
    def __init__(self, name, color, speed, typenum):
        self.name = name
        self.color = color
        self.speed = speed
        self.typenum = typenum

    def info(self):
        """
        公共实例方法
        :return:
        """
        return f"{self.name} 汽车！"

    def run(self):
        print(f"{self.name}父类汽车开始启动")


class FuelCar(Car):
    """
    汽油车
    """
    def info(self):
        # 调用父类中的方法(方式一: super().父类方法名())
        string = super().info()
        print(string)

        # 调用父类中的方法(方式二: 父类名.方法名(self))
        string2 = Car.info(self)
        print(string2)
        return f"{self.name}的 {self.typenum} 汽车！"

    pass


class ElectricCar(Car):
    """
    电动汽车
    """
    def info(self):
        self.run()
        return f"{self.name}的 {self.typenum} 汽车！"
    pass

car1 = FuelCar("小米yu7", "灰白色", 45, "燃油车")
print(car1.info())

car2 = ElectricCar("特斯拉", "白色", 120, "电动汽车")
print(car2.info())