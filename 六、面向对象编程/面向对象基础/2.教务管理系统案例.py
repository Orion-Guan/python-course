# 定义学生实体类
class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def __str__(self):
        return f"姓名: {self.name} | 语文: {self.chinese} | 数学: {self.math} | 英语: {self.english}"

    def update_score(self, chinese=None, math=None, english=None):
        """
        更新学生成绩
        :param chinese:
        :param math:
        :param english:
        :return:
        """
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english




# 定义教务系统实体类
class EducationManage:
    # 定义类属性
    name = "湖工教务系统"
    version = "1.0.0"

    def __init__(self):
        self.student_list = []  # 存放学生对象

    # 新增学生信息
    def add_student(self):
        name = input("请输入学生姓名:")

        # 判断学生是否已存在系统
        stu_names = [stu.name for stu in self.student_list]
        if name in stu_names:
            print("抱歉! 该学生信息已录入系统。")
            return
        chinese_score = float(input("请输入语文成绩:"))
        math_score = float(input("请输入数学成绩:"))
        english_score = float(input("请输入英语成绩:"))

        # 判断学生成绩键入是否有误
        if not 0 <= chinese_score <= 150 or not 0 <= math_score <= 150 or not 0 <= english_score <= 150:
            print("抱歉! 学生成绩录入有误(0-150)")
            return

        # 保存学生成绩
        stu = Student(name, chinese_score, math_score, english_score)
        self.student_list.append(stu)
        print("学生信息录入成功!")

    # 修改学生信息
    def update_student(self):
        name = input("请输入学生姓名:")
        for stu in self.student_list:
            if stu.name == name:
                print(f"学生当前成绩: {stu}")
                chinese_score = float(input("请输入修改后的语文成绩:"))
                math_score = float(input("请输入修改后的数学成绩:"))
                english_score = float(input("请输入修改后的英语成绩:"))
                if 0 <= chinese_score <= 150 and 0 <= math_score <= 150 and 0 <= english_score <= 150:
                    stu.update_score(chinese_score, math_score, english_score)
                    print(f"修改后的学生成绩: {stu}")
                    return
                else:
                    print("抱歉! 学生成绩录入有误(0-150)")
                    return
        print(f"抱歉! 教务系统无{name}同学")

    # 删除学生信息
    def delete_student(self):
        name = input("请输入学生姓名:")
        for stu in self.student_list:
            if stu.name == name:
                self.student_list.remove(stu)
                print(f"{name} 同学删除成功")
                return
        print(f"抱歉! 教务系统无{name}同学")

    # 查询某学生信息
    def get_info(self):
        name = input("请输入学生姓名:")
        for stu in self.student_list:
            if stu.name == name:
                print(stu)
                return
        print(f"抱歉! 教务系统无{name}同学")

    # 查询所有学生信息
    def show_students(self):
        for stu in self.student_list:
            print(stu)

    # 运行教务系统
    def run(self):
        print(f"系统版本V{self.version}\n")
        while True:
            print("#" * 77)
            print("# 1. 添加学生  2. 修改学生  3. 删除学生  4. 查询单个学生  5. 查询所有学生  6. 退出系统 #")
            print("#" * 77)

            ops_num = input("\n请输入操作数字(1-6)/>")

            try:
                match ops_num:
                    case "1":
                        self.add_student()
                    case "2":
                        self.update_student()
                    case "3":
                        self.delete_student()
                    case "4":
                        self.get_info()
                    case "5":
                        self.show_students()
                    case "6":
                        break
                    case _:
                        print("请输入1-6之间的整数!")

            except TypeError:
                print("输入的数据类型有误，请重新操作!")
            except Exception as e:  #捕获一般通用的所有异常类型（异常兜底）
                print(f"程序异常出错: {e}\n请重新输入!")


# 测试
if __name__ == '__main__':
    edu_sys = EducationManage()
    edu_sys.run()
