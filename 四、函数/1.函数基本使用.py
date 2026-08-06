"""
一、函数(实现代码复用)
    定义:
            del 函数名(形参列表):
                return 函数体

    函数调用: ret = 函数名(实参列表)

说明：
1、函数必须先定义后调用(*java无要求)
2、函数只有在调用时才会执行、定义时不会执行
3、python通过缩进来描述语句层级归属关系
4、python中的函数可以返回多个值以","分割，并以不可变元组的形式返回（java函数只能返回一个值）
5、在函数体的最前面使用一个三引号可以定义函数说明文档，函数在调用时鼠标悬停到函数名上可以查看其函数的说明文档，也可以通过内置函数help(函数名)查看其说明文档。
6、函数的嵌套调用执行流程类似于栈的数据结构（后进先出，先进后出）
"""


# #定义函数
# def funcName(arg1, arg2):
#     print(arg1, arg2)
#     return f"{arg1} + {arg2} = {arg1 + arg2}"
#
# #调用函数
# value = funcName(3,4)
# print(value)




#
# def circle_ops(redis):
#     """
#     根据圆半径计算圆的面积和周长（函数说明文档）
#     :param redis: 圆半径
#     :return: 圆面积，圆周长
#     """
#     return round(3.14 * redis ** 2, 2), round(3.14 * 2 * redis, 2)  # 多个返回值会以元组的形式返回
#
#
# acreage, perimeter = circle_ops(10)
# print(f"圆面积:{acreage}, 圆周长:{perimeter}")
# help(circle_ops)   #查看函数说明文档



# 1. 定义一个函数：根据传入的底和高计算三角形面积的函数（三角形面积=底*高/2）。
def area_triangle(low, high):
    """
    计算三角形面积
    :param low: 低
    :param high: 高
    :return: 三角形面积
    """
    return round(low * high / 2, 2)
print(area_triangle(2,3))



# 2. 定义一个函数:计算传入的字符串中元音字母的个数（元音字母为 aeiouAEIOU)。
def count_vowels(string):
    """
    计算传入字符串中元音字符个数
    :param string: 字符串
    :return: 字符串中的元音字母个数
    """
    count = 0
    for char in string:
        if char in 'aeiouAEIOU':
            count += 1
    return count

print(count_vowels("OrionGuan"))

# 3. 定义一个函数:计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分(保留1位小数)，并返回。
def calc_score(score_list):
    """
    计算传入数据中最高分、最低分、平均分
    :param score_list: 成绩列表
    :return: 最高分、最低分、平均分
    """
    max_score = max(score_list)
    min_score = min(score_list)
    avg_score = sum(score_list) / len(score_list)
    return max_score, min_score, avg_score

max_score1, min_score1, avg_score1 = calc_score([1, 2, 3, 4, 5])
print(max_score1, min_score1, avg_score1)