"""
一、set集合
    定义:     set1 = {1,2,4,5,"Orion",None, False}
             set2 = set()       #定义空集合

    特点: 元素无序（没有索引）且唯一，可修改

常用方法:
    set.add() -----向集合中添加元素
    set.remove()-----从集合中删除指定元素
    set.pop()-----从集合中随机删除元素
    set.clear()------清空集合元素

    set1.intersection(set2)-------求set1 与 set2的交集  或   set1 & set2
    set1.union(set2)-------求set1 与 set2 的并集 或 set1 | set2
    set1.difference(set2)-------求set1 与 set2 的差集（在set1中但不在set2中的元素) 或   set1 - set2

二、集合推导式（根据指定规则生成集合）
    变量名称 = {i表达式 for i in 列表}
    变量名称 = {i表达式 for i in 列表 if 条件}   #执行顺序 先中间----->在条件判断------>i表达式（最终落到集合中的元素）


"""


