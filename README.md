# Python基础速通笔记

---

## 一、基本数据类型

- `int` - 整数类型
- `float` - 浮点数类型
- `str` - 字符串类型
- `bool` - 布尔类型
- `NoneType` - 空类型

### 字符串格式化

```python
f'字符串文本{变量}'  # 模板字符串格式化
r'撸起袖子\n加油干'  # r 去除转义字符（\n）特殊含义，原样输出
```

### 1.1 算数运算符

```python
a // b  # 整除
a ** n  # a 的 n 次方
```

### 1.2 比较运算符

支持数学形式的比较，例如：`>`、`<`、`>=`、`<=`、`==`、`!=`

### 1.3 逻辑运算符

| 运算符 | 说明 | 特点 |
|--------|------|------|
| `and` | 逻辑与 | 全真即真，有假即假（短路） |
| `or` | 逻辑或 | 有真即真，全假为假（短路） |
| `not` | 逻辑非 | 取反 |

---

## 二、高级数据类型

### 2.1 list 列表

```python
list1 = [1, 2.4, True, 'Hello', 1]
```

**特点**：有序、可重复、可修改

**列表推导式**：
```python
[item for item in range(10) if item > 3]
```

**解包 & 组包**：
```python
list2 = [*list]
```

---

### 2.2 tuple 元组

```python
tuple1 = (1, 2.1, 1, 'str', False)
```

**特点**：有序、可重复、不能修改

**解包**：
```python
a, *b, c = (1, 2, 4, 5, 6)  # a=1, c=6, b=[2, 4, 5]
```

---

### 2.3 set 集合

```python
set1 = {1, 2, 'str', True}
```

**特点**：无序且唯一，不支持切片和索引访问

**集合推导式**：
```python
{item for item in range(10) if item > 5}
```

---

### 2.4 dict 字典

```python
dict1 = {key: value, key: value}
```

**特点**：
- 键必须是不可变类型
- 值可以任意类型
- 键若已存在则修改会覆盖原值

**字典推导式**：
```python
{key: key * 2 for key in range(10) if key < 8}
```

---

## 三、条件判断

### if-elif-else 结构

```python
if 逻辑表达式:
    代码块
elif 逻辑表达式:
    代码块
elif 逻辑表达式:
    代码块
else:
    代码块
```

### match-case 结构（Python 3.10+）

```python
match 变量:
    case 常量:
        代码块
    case 常量 | 常量:
        代码块
    case 常量 if 条件:
        代码块
    case _:
        其他默认情况代码块
```

---

## 四、循环语句

### for 循环

```python
for item in range(1, 10, 1):
    循环体
else:
    正常迭代完毕执行代码块（遇到 break 则不执行）
```

### while 循环

```python
while 逻辑表达式:
    循环体
else:
    正常迭代结束执行的代码块（遇到 break 则不执行）
```

### 循环控制关键字

| 关键字 | 说明 |
|--------|------|
| `break` | 退出本层循环 |
| `continue` | 结束本层的本轮循环，开始下轮循环 |

---

## 五、函数

### 5.1 函数定义

```python
def func(形参1, 形参2=默认值, *args, **kwargs):
    函数体
    return
```

**参数说明**：
- `*args` - 收集多个位置参数到元组
- `**kwargs` - 收集多个关键字参数到字典

### 5.2 传参方式

| 方式 | 说明 |
|------|------|
| 位置传参 | 一一对应，类似 Java |
| 关键字传参 | `func(key1=value1, key2=value2)` |

### 5.3 全局变量与局部变量

```python
global 变量名  # 在函数内声明为函数外的全局变量赋值
```

### 5.4 函数递归调用

- 递推 → 递归，必须有结束返回条件

### 5.5 lambda 表达式

```python
# 定义（自动返回表达式计算的结果）
func_address = lambda 形参1, 形参2: 表达式

# 调用
func_address(实参1, 实参2)
```

---

## 六、异常处理

> 默认方法报错后，异常信息会沿着调用链逐层向源头返回，并导致程序运行终止。一旦异常被捕获，则异常信息不会再向源头返回，也不会阻止程序正常执行。

```python
try:
    代码块
except Exception as error:
    处理异常代码块（try 中的代码块抛出异常后执行此方法）
finally:
    释放资源代码块（不管 try 中是否抛出异常都会执行）
```

---

## 七、模块与包

### 7.1 模块

> 一个 `xxx.py` 文件就是一个模块，模块中可以是变量、函数、类与对象。

```python
from 模块 import *  # 导入模块
```

### 7.2 包

> 如果一个目录下包含 `__init__.py` 文件，则此目录就是软件包，该文件中定义包的元信息。

**内建变量**：

| 变量名 | 说明 |
|--------|------|
| `__name__` | 在当前模块执行表示 `"__main__"`，作为其他模块导入执行时表示模块文件名字符串 |
| `__all__` | 定义软件包或者模块中对外导入该模块或包时，暴露给 `*` 通配符的成员有哪些 |

### 7.3 第三方包管理

```bash
pip install 软件包名  # 下载第三方软件包
```

---

## 八、类与对象

```python
class ClassName:
    # 类属性
    father_name = "Orion"
    father_age = 62
    father_gender = '男'

    # 魔术方法。定义实例属性（类似 Java 类中的构造器，创建对象时自动调用）
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 定义实例方法（self 表示类创建的每个实例对象，调用时不用赋值）
    def func(self, 参数):
        方法体
```

**说明**：以 `__函数名__()` 命名的方法都是魔术方法，魔术方法会在程序执行的特定时期自动调用。

### 类的使用

```python
personObj = ClassName('小关', 26, '男')  # 创建对象

personObj.name  # 访问实例属性
ClassName.father_name  # 访问类属性
personObj.func(实参)  # 调用实例方法
```

---

## 九、文件操作

### 9.1 操作普通文件

```python
with open("文件路径", "打开模式", encoding="utf-8") as fileObj:
    代码块
```

**使用步骤**：

1. 打开文件：`file = open("文件路径", "打开模式", encoding="utf-8")`
2. 读写操作：
   - `file.read()` - 读取全部内容
   - `file.write("内容")` - 写入全部内容
3. 关闭文件：`file.close()` - 关闭文件，刷新缓冲区并释放资源

### 9.2 操作 JSON 串

```python
import json

# 序列化字典数据到文件
json.dump(dict, file, ensure_ascii=False, indent=2)
# ensure_ascii=False 确保能打开文件能正确解析中文
# indent=2 确保序列化到文件中的 json 串是格式化后的

# 将文件中的 json 数据反序列化到字典变量
data = json.load(file)
```

### 9.3 操作 CSV 文件

```python
import csv

with open('文件路径', '打开方式', encoding='utf-8', newline='') as f:
    # 写入行数据
    writer = csv.DictWriter(f, fieldnames=['姓名', '年龄', '性别'])
    writer.writeheader()  # 写入表头
    writer.writerow({'姓名': '张三', '年龄': 20, '性别': '男'})

    # 读取 csv 文件内容
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
```

---

## 十、正则表达式

```python
import re
```

### 10.1 常用方法

| 方法 | 说明 | 返回值 |
|------|------|--------|
| `re.match(模式字符串, 文本)` | 开头匹配 | Match 对象 |
| `re.search(模式字符串, 文本)` | 任意位置匹配，只匹配一次 | Match 对象 |
| `re.findall(模式字符串, 文本)` | 全局匹配 | 所有匹配的字符串列表 |

**Match 对象方法**：

| 方法 | 说明 |
|------|------|
| `obj.group()` | 获取匹配的字符串 |
| `obj.span()` | 匹配到的字符串在文本中的索引位置（不包含结束索引） |
| `obj.start()` | 获取开始索引 |
| `obj.end()` | 获取结束索引 |

### 10.2 模式规则

| 符号 | 说明 |
|------|------|
| `.` | 匹配任意单个字符（除换行符外） |
| `[A-Za-z]` | 匹配单个英文字母（大小写） |
| `\d` | 匹配单个数字 |
| `\D` | 匹配非数字的单个字符 |
| `\s` | 匹配单个空白字符（空格、制表符、换行等） |
| `\S` | 匹配非空格单个字符 |
| `\w` | 匹配单个普通字符串（数字、字母、下划线） |
| `\W` | 匹配单个非普通字符即特殊字符 |
| `^字符串` | 目标文本必须以指定字符串开头 |
| `字符串$` | 目标文本必须以指定字符串结尾 |
| `str1 \| str2` | 目标字符串要么是 str1，要么是 str2 |

### 10.3 匹配次数

> 定义前个模式规则字符的匹配次数

| 符号 | 说明 |
|------|------|
| `*` | 前个字符匹配任意个数 |
| `+` | 前个字符至少匹配一次 |
| `?` | 前个字符至多匹配一次 |
| `{n}` | 前个字符必须匹配 n 次 |
| `{min,}` | 前个字符至少匹配 min 次 |
| `{min, max}` | 前个字符匹配 min 到 max 之间个次数 |