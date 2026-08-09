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


"""



#动态为对象添加字段（Python特有）
class User:  #定义类（对象的模板）
    pass

user1 = User()
user1.name = "Orion"
user1.age = 26
user1.address = "河南鹿邑"
print(user1.__dict__)   #__dict__: 是对象中内置的特有属性，它的一个字典里面存放了对象的所有属性。


#定义类和其实例字段属性（推荐）
class Animal:
    def __init__(self, a_name, a_age, a_address):  # self: 代表创建的实例对象
        self.name = a_name
        self.age = a_age
        self.address = a_address
        print("__init__: 对象的初始化方法，在创建对象时会被自动调用。用于给创建的实例对象的字段初始化赋值。(类似于Java中的全参构造器)")

animal = Animal("小黄", 8, "天堂")
print(animal.__dict__)