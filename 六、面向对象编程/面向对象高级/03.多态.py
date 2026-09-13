"""
一、多态
调用同一个函数，传递的参数对象不同，函数的执行结果也不同（发生在继承场景：不同子类对象，相同方法，不同行为）
如：定义函数时，参数类型指定为父类类型，在执行的时候传入不同的子类对象，就具有不同的形态
def func(car:Car):
    car.info()

func(FuelCar('奔驰', '红色', 120, '汽油'))    # 调用子类的方法
func(ElectricCar('特斯拉', '白色', 120, '电池'))    # 调用子类的方法

"""

class Car(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    pass


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
    pass

class FuelCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
    pass

def info(car:Car):
    print(car.__dict__)  # 打印对象的属性字典
    pass


if __name__ == '__main__':
    """
    多态的测试(相同info方法，不同结果)
    """
    info(FuelCar('奔驰', '红色', 120))      # {'make': '奔驰', 'model': '红色', 'year': 120}
    info(ElectricCar('特斯拉', '白色', 120))     # {'make': '特斯拉', 'model': '白色', 'year': 120}
