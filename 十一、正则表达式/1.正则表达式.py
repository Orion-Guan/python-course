"""
一、正则表达式
定义：根据定义的规则去匹配或替换符合该规则的字符串


1.1 常用函数
re.match(pattern, string, flags=0)  从字符串的开始位置匹配
re.search(pattern, string, flags=0)  在字符串中搜索匹配的子串（只匹配一次）
re.findall(pattern, string, flags=0)  在字符串中搜索所有匹配的子串（全局匹配）
说明: 模式规则前的r，是为了让模式规则中的转义字符失效，如”\d“



"""

import re

text1 = '17613270756你是个大好人呢？15936958740，是吧'
text2 = '关山月17613270756你是个大好人呢？15936958740，是吧18066234881'

# match方法: 只匹配字符串的开始，如果完全匹配成功才返回Match对象，否则返回None
matchObj = re.match(r"1[3-9]\d{9}", text1)
print(matchObj)
print(matchObj.group())  # 取匹配到的值
print(matchObj.span())  # 取匹配到的索引位置
print(matchObj.start())  # 取匹配到的开始索引位置
print(matchObj.end())  # 取匹配到的结束索引位置(不包含本身)

# search方法: 在字符串任意位置搜索匹配的子串（只匹配一次），如果匹配成功则返回Match对象，否则返回None
searchObj = re.search(r"1[3-9]\d{9}", text2)
print(searchObj)
print(searchObj.group())
print(searchObj.span())
print(searchObj.start())
print(searchObj.end())

# findall方法: 在字符串中搜索所有匹配的子串（全局匹配），返回所有匹配的子串列表，如果没有匹配的子串，则返回空列表
findallObj = re.findall(r"1[3-9]\d{9}", text2)
print(findallObj)
