"""
一、字符串容器
    特点：
    1、不可变性----无法修改字符串中字符元素的值
    2、有序性-----字字符串中的字符都是有序的
    3、可迭代-----可以循环遍历获取里面的字符元素

1.1 字符串索引
    1、正向索引-----从左到右(首元素索引为0)
    2、反向索引-----从右到左（首元素索引为-1）

1.2 字符串的切片
    语法：s[start:end:step]
    特点：
    start:开始索引，不指定默认为0(第一个元素的索引)
    end:结束索引，不指定则截取到最后
    step:步长，不指定默认为1(-1表示从后向前，start与end也需要使用反向索引)



二、常用方法
    s = "   Hello-Python-Hello-World     "

    print(s.find("Hello"))     #在字符串中查找指定字串首次出现的索引下标

    print(s.count("Hello"))   #统计字串在主串中出现的次数

    print(s.upper())    #转大写
    print(s.lower())    #转小写

    print(s.split("-"))   #按照指定字串来切割主串并以列表的形式返回

    print(s.strip())    #去除主串前后空格

    print(s.replace("Python", "Java"))   #将主串中的字串Python，替换为其他字符串Java

    print(s.startswith("Python"))   #判断主串是否以Python开头
    print(s.endswith(" "))      #判断主串是否以空格结尾

如何判断某个字符串是否已经出现在字符串中？
答： substr in str 如果substr出现在字符串中则返回True, 否则返回False



三、


"""

#字符串常用方法
# s = "   Hello-Python-Hello-World     "
#
# print(s.find("Hello"))     #在字符串中查找指定字串首次出现的索引下标
#
# print(s.count("Hello"))   #统计字串在主串中出现的次数
#
# print(s.upper())    #转大写
# print(s.lower())    #转小写
#
# print(s.split("-"))   #按照指定字串来切割主串并以列表的形式返回
#
# print(s.strip())    #去除主串前后空格
#
# print(s.replace("Python", "Java"))   #将主串中的字串Python，替换为其他字符串Java
#
# print(s.startswith("Python"))   #判断主串是否以Python开头
# print(s.endswith(" "))      #判断主串是否以空格结尾





# 邮箱合法性校验(基础校验)
mail = input("请输入合法邮箱:")

if mail.count("@") != 1  or "." not in mail:
    print("邮箱格式有误")
else:
    print(f"邮箱格式正确:{mail}")