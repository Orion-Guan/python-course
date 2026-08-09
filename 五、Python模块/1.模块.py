"""
一、导入模块
模块就是一个.py文件。通过导入模块开发者可以复用模块中写好的已有变量、方法、类等；模块文件可以是官方内置或其他开发者写好的外部模块或者是自己本地定义的模块。
模块文件一但被其他模块文件当作模块导入并执行时，导入的模块中的代码就会被执行。

1.导入模块的常用语法(导入模块的语句，一般写在py文件的开头)
    • import 模块名 [as 别名]
    • from 模块名 import 功能名 [as 别名]
    • from 模块名 import *



二、自定义模块
__name__特殊内置变量: 当模块直接运行时：___name__的值为"__main__"(if__name__=="__main__")；当模块被导入时：__name__等于模块的文件名(不含.py后缀)

__all__特殊内置变量: 控制 import * 时导入哪些功能(其他模块: __all__ = ['get_area', "PI"])



三、软件包
包就是一个文件夹，里面可以存储很多Python模块(py文件)，通过包可以对模块进行归类。如果一个目录中包含"__init__.py"文件，那么此目录就是一个包。

3.1 __init__·py文件的作用?
• 标识这是一个包，而不是普通的文件夹
• 控制在 from 包名 import *时导入的模块列表( __all__ = ["custom_module2"]  )


3.2 如何使用包中所有模块中的某功能(导入包的方式)？
• import 包名.模块名
• from 包名 import 模块名
• from 包名 import *
• from 包名.模块名 import 功能名
• from 包名.模块名 import *

"""



# 导入模块
import random

print(random.randint(1, 100))

# 导入模块并通过别名使用模块中的功能
import random as rnd

print(rnd.randint(1, 100))

# 使用模块中具体功能
from random import randint

print(randint(1, 100))

# 通过给导入的模块功能起别名
from random import randint as rd

print(rd(1, 100))

# 导入模块中的所有功能
from random import *

print(randint(1, 100))

# 导入本地自定义模块
from custom_module import *

print(get_area(4))

# 导入包中的其他模块
import utils.custom_module3

print(utils.custom_module3.PI)

from utils import custom_module3, custom_module2

print(custom_module2.PI)

from utils import *

print(custom_module2.PI)

from utils.custom_module2 import *

print(get_area(PI))

from utils.custom_module2 import get_area, RADIUS

print(get_area(RADIUS))
