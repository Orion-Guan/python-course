"""
一、类与对象
__init__: 对象的初始化方法，在创建对象时会被自动调用。用于给创建的实例对象的字段初始化赋值。(类似于Java中的全参构造器)
self: 是类中定义方法的首个形参，代表基于类创建的实例对象（类似于Java和JS类中的this关键字）。

定义类：
    class 大驼峰类名:
        def __init__(self, 形参列表):
            pass

创建对象:
    obj = 大驼峰类名(实参列表)


访问对象属性:
    obj.字段属性名



二、实例方法

    def running(self):
        print(f"{self.name} {self.type} 正在行驶中...")

说明: 实例方法形参的首个self参数代表实例对象，在通过对象调用方法时无需为其传参。



三、魔法方法(自动调用的方法)
以 __XX__ 开后和结尾的方法就是魔法方法。魔法方法会在解释器执行某些操作代码时会自动调用。

3.1 常用的魔法方法有哪些，作用是什么？
    在创建对象实例时，会自动调用此初始化方法: __init__
    在输出对象时python解释器会自动调用此方法，作为输出结果: __str__
    在判断两个对象是否相等时会自动调用，作为判断依据: __eq__
    在判断两个对象大小时会自动调用: __lt__,__le__,__gt__,__ge__


四、属性
类属性（访问----->类名.属性名）: 类属性是属于类本身的属性。其属性各实例对象共享。定义在类的各方法之外。
实例属性（访问----->实例对象.属性名）: 各实例对象所独有的属性。无法通过类名.属性访问。定义在类的初始化方法内。


"""
from os import name


#
# #动态为对象添加字段（Python特有）
# class User:  #定义类（对象的模板）
#     pass
#
# user1 = User()
# user1.name = "Orion"
# user1.age = 26
# user1.address = "河南鹿邑"
# print(user1.__dict__)   #__dict__: 是对象中内置的特有属性，它的一个字典里面存放了对象的所有属性。
#
#
# #定义类和其实例字段属性（推荐）
# class Animal:
#     def __init__(self, a_name, a_age, a_address):  # self: 代表创建的实例对象
#         self.name = a_name
#         self.age = a_age
#         self.address = a_address
#         print("__init__: 对象的初始化方法，在创建对象时会被自动调用。用于给创建的实例对象的字段初始化赋值。(类似于Java中的全参构造器)")
#
# animal = Animal("小黄", 8, "天堂")
# print(animal.__dict__)


# # 实例方法
# class Car:
#     def __init__(self):
#         self.name = '保时捷'
#         self.type = 'Orion'
#         self.price = 569999
#
#     def running(self):
#         print(f"{self.name} {self.type} 正在行驶中...")
#
#     def getPrice(self, discount, exchange_rate):
#         """
#         实例方法
#         :param discount:
#         :param exchange_rate:
#         :return:
#         """
#         return self.price * discount  + self.price * exchange_rate
#
#
# car1 = Car()
#
# cost = car1.getPrice(0.95, 0.10)
# print(cost)
#
# car1.running()


# 魔法方法
class Person:
    # 定义类属性（类所有的属性--各实例共享）
    leg = 2
    hair = "black"

    def __init__(self, name, age):
        """
        定义实例属性： 每个实例对象所特有的属性。
        在创建对象实例时，会自动调用此初始化方法
        :param name:
        :param age:
        """
        self.name = name
        self.age = age

    def __str__(self):
        """
        在输出对象时python解释器会自动调用此方法，作为输出结果
        :return:
        """
        return f"{self.name} {self.age}"

    def __eq__(self, other):
        """
        在判断两个对象是否相等时会自动调用，作为判断依据
        :param other:
        :return:
        """
        return self.name == other.name and self.age == other.age

    def __lt__(self, other):
        """
        在判断两对象大小时，会自动调用作为判断依据
        :param other:
        :return:
        """
        return self.age < other.age


person1 = Person("Orion", 26)

person2 = Person("Leisr", 23)

print(person1)

print(person1 == person2)

print(person1 > person2)

print(person1 < person2)

print(person1.leg, Person.leg)
