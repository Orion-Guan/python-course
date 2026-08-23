"""
一、文件读写
步骤:
1、打开文件
file = open(“文件名”, “读写模式”, encoding=“编码格式”)

2、读写文件
file.read() #读取全部内容
file.readline() #读取一行内容
file.readlines() #读取全部行内容，返回列表，元素是每一行内容
file.write() #写入内容

3、关闭文件
file.close()


二、不管文件读取中途是否出现异常，文件资源都会被正常释放
with open("Python文件操作", "r", encoding="utf-8") as file:
    content = file.read()  # 读取全部内容
    print(content)


三、 序列化字典对象为JSON串并保存到文件中
import json
json.dump(dict1, file, ensure_ascii=False, indent=2)   # ensure_ascii=False 中文正常显示，indent=2 格式化输出
json.load(file)  # 反序列化文件中的json串为python字典对象



"""

#
# #打开文件
# file = open("Python文件操作", "w", encoding="utf-8")
#
# #向文件写内容
# file.write("静夜思\n")
# file.write("床前明月光，\n")
# file.write("疑是地上霜。\n")
# file.write("举头望明月，\n")
# file.write("低头思故乡。\n")
#
# #关闭文件
# file.close()
#
#
#
#
# #打开文件
# file = open("Python文件操作", "r", encoding="utf-8")
#
# #读取文件内容
# content = file.read() #读取全部内容
# print(content)
#
# #关闭文件
# file.close()


# 即使在操作文件中程序出现异常资源依然能够被正常释放（方式一）
# try:
#     # 打开文件
#     file = open("Python文件操作", "r", encoding="utf-8")
#     # 读取文件内容
#     content = file.read()  # 读取全部内容
#     num = 1 / 0  # 模拟异常
#     print(content)
# except Exception as e:  # 捕获异常
#     print(e)
# finally:
#     file.close()  # 关闭文件,释放资源
#     print("文件关闭")


# 使用with语句自动关闭文件（方式二）
# with open("Python文件操作", "r", encoding="utf-8") as file:
#     content = file.read()  # 读取全部内容
#     print(content)


# 将python字典对象序列化为JSON字符串并保存到文件中(序列化)
import json

dict1 = {"name": "张三", "age": 20, "gender": "男"}
with open("resources/json_data.json", "w", encoding="utf-8") as file:
    json.dump(dict1, file, ensure_ascii=False, indent=2)


# 读取JSON字符串并反序列化为python字典对象(反序列化)
with open("resources/json_data.json", "r", encoding="utf-8") as file:
    dict2 = json.load(file)
    print(dict2)
    print(type(dict2))