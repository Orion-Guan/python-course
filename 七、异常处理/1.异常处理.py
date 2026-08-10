"""
一、异常捕获
1. 为什么要捕获异常？
当程序运行出现异常时提供预案来处理异常，而不是让其中止程序运行

2. 异常的传递
如果fun1()--->fun2()----->fun3(), 而在fun3()的方法体中出现了异常并且未被捕获，此时异常会层层原路返回向上抛出，如果
fun2()中也未捕获异常，则异常会向上返回给fun1()方法；如果fun1()方法也未定义捕获异常，则最终控制台会抛出异常信息、整个程序
终止运行。


3. 如何捕获异常，具体的语法?
    try:
        print("ABC".hello)

    except NameError as e:
        print("名称不存在，请检查，具体信息："，e)
    except ZeroDivisionError as e:
        print("0不能做被除数，请检查，具体信息："，e)
    except IndexError:
        print("索引错误，请检查，具体信息：")
    except Exception as e:
        print("其他错误，请检查，具体信息："，e)

    finally: #可有可无
        print("无论正常执行还是出现异常，都要释放资源~")




"""

try:
    print("##############")
    print(3 / 0)
    print("##############")

except ZeroDivisionError:
    print("被除数不能为零")

except Exception as e:   #异常捕获匹配机制是自上而下的，一旦匹配到后面定义的其他异常就不会执行了。 Exception: 要捕获的异常类型、 e: 异常信息
    print("异常信息: ",e)

finally:
    print("代码是否报错都会执行该代码块（释放资源）")
