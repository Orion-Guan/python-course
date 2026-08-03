"""
一、元组
方式一:   tuple = (1,3,32,4,3,1,"Hello",True,None)
方式二:   tuple1 = tuple(range(0,10,1))
方式三：  tuple2 =  1,2,445,23
注意: 定义单元素元组(需要在其元素后面加","号)： tuple1 = (1,)

特点：只读的、无法修改其元素； 元素有序可重复

1.1 内置方法
tuple1.count(40) -----  #查询指定元素在容器中出现的次数
tuple1.index(40) -----  #获取指定元素在容器中从左到右首次出现的索引

1.2 组包与解包
组包： 将多个值组合在一起放在容器里。如： tuple1 = (80, 40, 78, 34, "Hello", True, None, 40)
解包:  从容器中取出所有的各元素并赋值给新的变量
    基础解包:  a,b,x = 1,2,445  ----- 左边定义接收值的变量个数需要与右边元组容器的个数相同
    扩展解包:  a, *b, x = 1,2,4,5,6  ---- *变量:表示接收剩余的所有值,如a = 1, b = [2,4,5], x = 6
"""



# tuple1 = (80, 40, 78, 34, "Hello", True, None, 40)  # 定义元组并初始化
#
# print(tuple1.count(40))  # 查询指定元素在容器中出现的次数
#
# print(tuple1.index(40))  # 获取指定元素在容器中从左到右首次出现的索引
#
# tuple2 = ("定义单元素元组",)
# print(type(tuple2))
#
# tuple3 = tuple(range(0, 10, 1))
# print(type(tuple3))
#
# tuple4 = 1, 2, "Helo"
# print(type(tuple4))



#基础解包
tuple1 = (1,2,3,4,5,6)   #组包
first, *middle, last = tuple1   #扩展解包: *变量---表示收集容器中剩余的所有元素到列表中
print(first, middle, last)


#交换两个变量的值
a = 100
b = 254
x = 76

b,a = (a,b)  #简写: b,a = 1,b   过程:  1. (a,b)------组包      2. b,a = (a,b) ----- 做基础解包
print(b,a)


#交换三个变量的值
a,b,x = x,a,b
print(a, b, x)


a,b,x = 1,2,445