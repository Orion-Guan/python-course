"""
一、list列表（类似Java中的List接口）
    定义： [1, 34, 54, 56, 34, "Orion", True, None]
    1.正向索引----从前往后，首个元素的索引下标为0
    2.反向索引----从后向前， 最后一个元素反向索引下标为-1
    3.列表中可以存放各种数据类型的元素在一起、元素可重复、列表元素有序可修改

1.1 切片
    描述：从容器序列中裁选出部分元素
    定义：容器名[开始索引（0）,结束索引（末尾）,步长（1）]

1.2 list列表常用方法函数
    list1.append(2)   #追加元素到列表末尾
    list1.insert(-1,888)   #在索引前插入元素

    list1.remove(34)   #删除首次出现的该值元素
    list1.pop(-1)    #删除指定索引的元素并返回

    list2.sort()     #同种类型的列表元素正向排序（默认）
    list1.reverse()   #逆序颠倒字符串


二、常用数据统计函数
    min(容器) ------最小值
    max(容器) ------最大值
    sum(容器) ------求和
    len(容器)------容器中元素个数即长度




三、如何快速合并两个列表？
    方式一： 遍历最短的列表元素然后将其元素追加到另个列表中
    方式二： 使用解包*获取容器中的每个独立日元素， 然后在将其组装到容器中   [*list1, *list2]
    方式三： 直接使用+号  list1 + list2 （推荐）




四、如何对容器中的元素去重？
    in运算符  + not逻辑非关键字
    语法： 元素  not in  容器
    元素在容器中返回False, 不在返回True


五、如何快速生成列表
    方式一： 循环遍历range(start,end,step)生成的数字序列并将其添加到空列表中


方式二： 列表推导式（推荐）
    语法格式1
    [最终添加的值  循环语句  条件判断语句]  #执行顺序是： 2循环语句----->3条件判断------>1最终添加到列表的值（*其中条件判断语句可省略）

    案例：
    new_numList = [num ** 2 for num in range(1,21,1) if num % 2 == 0]   #列表推导式：先循环遍历生成的数字序列， 然后判断是否为偶数，最后将是偶数的计算其平方根并将结果放入列表中
    print(f"new_numList={new_numList}")





"""




# 定义list列表
# list1 = [1, 34, 54, 56, 34, "Orion", True, None]

#读取元素
# print(list1[0],list1[-1])

#修改元素
# list1[2] = 34
# print(list1)

#删除元素
# del list1[1]
# print(list1)

# 列表切片
# print(list1[0:6:1])     #[1, 34, 54, 56, 34, 'Orion']
# print(list1[:6:1])      #开始索引不指定默认从正向索引0开始
# print(list1[5::1])      #结束索引不指定默认到容器末尾  ['Orion', True, None]
# print(list1[0:6:])      #步长不指定，默认为1
#







# 常用数据据统计函数
# print(min([56,2,45]))    #获取容器中的最小值
#
# print(max([56,2,45]))    #获取容器最大值
#
# print(sum([56,2,45]))     #容器元素求和
#
# print(len([56,2,45]))    #虎获取容器元素个数即长度
#
# type(list1)
#
# isinstance(list1, list)
# isinstance(list1, tuple)
# isinstance(list1, list)







#案例： 将两个列表合并成一个列表并对合并后的列表元素去重
# 步骤：
# 1、合并
# 方式一：遍历任意一个列表(通常选短的列表)，然后将其元素追加到另个列表中。
# 方式二：利用python的解包和组包机制
# 方式三：直接使用+号

# 2、去重
# 先定义一个空容器来存放去重后的元素。然后遍历列表元素，在将其追加到去重后的列表前先判断是否已经存在，只有不存在才追加；存在则说明是重复元素不添加。

#
# num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
# num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]

#合并集合元素
# 方式一：
# for item in num_list2:
#     num_list1.append(item)
# print(f"合并后num_list1 = {num_list1}")

# 方式二：
# sublist = [*num_list1, *num_list2]   # *表示解包即获取容器中的所有元素

# 方式三
# sublist = num_list1 + num_list2

#去重
# 方式一
# not_repeat = []
# for item in sublist:
#     if item not in not_repeat:
#         not_repeat.append(item)
# print(f"去重后not_repeat = {not_repeat}")





#将1-20之间的偶数的平方根收集到新的列表中并打印
new_numList = [num ** 2 for num in range(1,21,1) if num % 2 == 0]   #列表推导式：先循环遍历生成的数字序列， 然后判断是否为偶数，最后将是偶数的计算其平方根并将结果放入列表中
print(f"new_numList={new_numList}")


