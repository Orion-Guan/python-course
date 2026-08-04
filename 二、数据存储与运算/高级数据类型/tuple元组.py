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



from time import process_time_ns

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


# 基础解包
# tuple1 = (1,2,3,4,5,6)   #组包
# first, *middle, last = tuple1   #扩展解包: *变量---表示收集容器中剩余的所有元素到列表中
# print(first, middle, last)
#
#
# #交换两个变量的值
# a = 100
# b = 254
# x = 76
#
# b,a = (a,b)  #简写: b,a = 1,b   过程:  1. (a,b)------组包      2. b,a = (a,b) ----- 做基础解包
# print(b,a)
#
#
# #交换三个变量的值
# a,b,x = x,a,b
# print(a, b, x)
#
#
# a,b,x = 1,2,445


#
# 根据如下提供的学生成绩单，完成如下需求：
# students = (
#     ("S001", "王林", 85, 92, 78),
#     ("S002", "李慕婉", 92, 88, 95),
#     ("S003", "十三", 78, 85, 82),
#     ("S004", "曾牛", 88, 79, 91),
#     ("S005", "周轶", 95, 96, 89),
#     ("S006", "王卓", 76, 82, 77),
#     ("S007", "红蝶", 89, 91, 94),
#     ("S009", "许木", 86, 89, 98),
#     ("S008", "徐立国", 75, 69, 82),
#     ("S010", "通天", 66, 59, 72)
# )
# 1.计算每个学生的总分、各科平均分，然后一并输出出来。
# 2.统计各科成绩的最低分、最高分、平均分，并输出。
# 3. 查找成绩优秀（平均分大于90）的学生，并输出。

students = (
    ("S001", "王林", 85, 92, 78),
    ("S002", "李慕婉", 92, 88, 95),
    ("S003", "十三", 78, 85, 82),
    ("S004", "曾牛", 88, 79, 91),
    ("S005", "周轶", 95, 96, 89),
    ("S006", "王卓", 76, 82, 77),
    ("S007", "红蝶", 89, 91, 94),
    ("S009", "许木", 86, 89, 98),
    ("S008", "徐立国", 75, 69, 82),
    ("S010", "通天", 66, 59, 72)
)

# 1.计算每个学生的总分、各科平均分，然后一并输出出来。
# 方式一:
# for student in students:
#     total_score = student[2] + student[3] + student[4]
#     avg_score = total_score / 3
#     print(f"{student[0]}\t{student[1]}\t{student[2]}\t{student[3]}\t{student[4]}\t{total_score}\t{avg_score:.2f}")
#
# 方式二:
for id, name, chinese, math, english in students:   #元组基本解包获取元组中每个元素
    total_score = chinese + math + english
    avg_score = total_score / 3
    print(f"{id}\t{name}\t{chinese}\t{math}\t{english}\t{total_score}\t{avg_score:.2f}")


# 2.统计各科成绩的最低分、最高分、平均分，并输出。
chinses_scores = [student[2] for student in students]
min_score = min(chinses_scores)
max_score = max(chinses_scores)
avg_score = sum(chinses_scores) / len(chinses_scores)
print(f"\n语文: {min_score}\t{max_score}\t{avg_score:.2f}")

math_scores = [student[3] for student in students]
min_score = min(math_scores)
max_score = max(math_scores)
avg_score = sum(math_scores) / len(math_scores)
print(f"\n数学: {min_score}\t{max_score}\t{avg_score:.2f}")

english_scores = [student[4] for student in students]
min_score = min(english_scores)
max_score = max(english_scores)
avg_score = sum(english_scores) / len(english_scores)
print(f"\n英语: {min_score}\t{max_score}\t{avg_score:.2f}")


# 3. 查找成绩优秀（平均分大于90）的学生，并输出。
for stu in students:
    total_score = stu[2] + stu[3] + stu[4]
    avg_score = total_score / 3
    if avg_score > 90:
        print(f"\n\n学生:{stu[1]}, 平均分:{avg_score:.2f}")  #.2f---保留小数前2位