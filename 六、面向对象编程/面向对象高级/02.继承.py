"""
一、继承
继承主要是为了解决在创建类时，对于多个类都需要的成员属性和方法，如果都写在每个类中，就会导致代码重复，不利于维护。为了解决成员属性和方法重复在每个类中编写，
我们就可以把这些每个类在创建时都需要的公共属性和方法抽取到一个父类中，然后让子类继承父类，这样子类就会拥有父类的成员属性和方法，而不用每个子类都编写相同的代码.

class 子类名(父类名):
    pass


说明:
1、定义的类如果没有显式使用括号指定要继承的父类，则默认继承自object类，即所有类都是object类的子类。
2、子类只能继承父类中所有公有的成员属性和方法，无法继承父类中的私有属性和方法。


1.1 多继承
多继承是指一个子类可以继承多个父类（Java中是单继承），从而拥有所有父类中的非私有的成员属性和方法。

class 子类名(父类名1,父类名2,父类名3):
    def __init__(self):
        super().__init__()      # 调用父类1的__init__方法
        父类名2.__init__(self)   # 调用父类2的__init__方法
        父类名3.__init__(self)   # 调用父类3的__init__方法
        self.fly = True         # 新增一个子类自己的实例属性fly
    pass

MRO方法解析顺序:
背景: 在多继承中，子类待调用的方法在自身以及多个父类中都有，优先使用哪个类中的方法？ 答：Python会遵循MRO原则。可以通过"类名.mro() | 类名.__mro__"方法查看。
顺序：
    1、子类自己的方法
    2、父类1的方法（不会向上找父类1的父类的方法）
    3、父类2的方法
    4、父类3的方法
    5、object类的方法



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

    def order(self):
        print("Car.order() 执行了!")


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

    def order(self):
        print("ElectricCar.order() 执行了!")
    pass


class HunDongCar(FuelCar,ElectricCar):
    """
    混动汽车
    """

# car1 = FuelCar("小米yu7", "灰白色", 45, "燃油车")
# print(car1.info())
#
# car2 = ElectricCar("特斯拉", "白色", 120, "电动汽车")
# print(car2.info())



# 测试在多继承中，多个父类都有相同的待调用方法，优先使用哪个类中的方法
hdc = HunDongCar('比亚迪','red',56,'A888')
# hdc.info()
print(HunDongCar.mro())    # 查看HRO方法解析顺序(方式一)
print(HunDongCar.__mro__)   # 查看MRO方法解析顺序(方式二)
print(hdc.__dict__)     # 查看hdc对象的所有属性

hdc.order()  # 调用的是ElectricCar中的order方法
