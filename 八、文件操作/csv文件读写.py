"""
csv文件读写
csv是数据之间以逗号作为单元格分隔符的文件格式。
1、写操作
    writer = csv.DictWriter(f,fieldnames=['姓名','年龄','性别'])
    writer.writeheader()    #写入表头
    writer.writerow({'姓名':'张三','年龄':20,'性别':'男'})  #写入一行数据

2、读操作
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
"""

# 方式一: 传统方式读写csv
#创建csv文件
with open('resources/test.csv','w',encoding='utf-8') as f:
    f.write('姓名,年龄,性别\n')
    f.write('张三,20,男\n')
    f.write('李四,21,女\n')
    f.write('王五,22,男\n')
    f.write('赵六,23,女\n')

#读取csv文件
with open('resources/test.csv','r',encoding='utf-8') as f:
    print(f.read())




# 方式二: 使用csv模块读写csv文件
import csv
# 创建csv文件(newline=''避免写入的数据每行多个空行)
with open('resources/test2.csv','w',encoding='utf-8',newline='') as f:
    writer = csv.DictWriter(f,fieldnames=['姓名','年龄','性别'])
    writer.writeheader()  #写入表头
    writer.writerow({'姓名':'张三','年龄':20,'性别':'男'})
    writer.writerow({'姓名':'李四','年龄':21,'性别':'女'})
    writer.writerow({'姓名':'王五','年龄':22,'性别':'男'})
    writer.writerow({'姓名':'赵六','年龄':23,'性别':'女'})

#读取csv文件
with open('resources/test2.csv','r',encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)