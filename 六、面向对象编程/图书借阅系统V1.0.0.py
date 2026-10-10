"""
湖北工程学院图书借阅系统
"""

# 导入ABC类和abstractmethod装饰器
from abc import ABC, abstractmethod
import json


# 图书实体类
class Book:
    def __init__(self, book_id, title, author, total_num):
        """
        初始化图书对象(实例属性)
        :param book_id:
        :param title:
        :param author:
        :param total_num:
        """
        # 图书编号
        self.book_id = book_id
        # 图书标题
        self.title = title
        # 图书作者
        self.author = author
        # 图书总数量
        self.total_num = total_num
        # 图书可用数量（私有属性:默认等于总数量，后续根据借阅记录更新）
        self.__available_num = total_num

    def get_available_num(self):
        """
        获取图书可用数量
        :return: 图书可用数量 （私有属性get方法）
        """
        return self.__available_num

    def borrowing_book(self):
        """
        借阅图书
        :return: True/False
        """
        if self.__available_num < 1:
            return False
        self.__available_num -= 1
        return True

    def returning_book(self):
        """
        归还图书
        :return: True/False
        """
        if self.__available_num >= self.total_num:
            return False
        self.__available_num += 1
        return True


# 会员类，继承抽象基类ABC， 抽象类不能被实例化，只能被子类继承，用于定义规范，让子类实现抽象方法
class Member(ABC):

    def __init__(self, member_id, name, pwd):
        """
        初始化会员对象(实例属性)
        :param member_id: 会员卡号
        :param name: 会员姓名
        :param pwd: 会员密码(私有属性)
        """
        self.member_id = member_id
        self.name = name
        self.__pwd = pwd
        self.__books = []

    def borrowing_book(self, book: Book) -> bool:
        """
        借阅图书
        :param book: 图书对象
        :return: True/False
        """
        # 会员不能重复借阅同样的书
        if book in self.__books:
            print(f"会员已借阅该图书:{book.title}")
            return False

        # 学生会员借阅的图书数量不能超过规则上限(普通会员3本，VIP会员=6+VIP等级)
        if len(self.__books) >= self.get_max_borrowing_num():
            print(f"会员{self.name}已借阅超过最大数量上限:{self.get_max_borrowing_num()}")
            return False

        # 开始借书
        if not book.borrowing_book():
            print(f"图书已借阅完:{book}")
            return False

        # 将图书添加到会员借阅图书列表
        self.__books.append(book)
        print(f"会员{self.name}借阅图书{book.title}成功")
        return True

    def returning_book(self, book: Book) -> bool:
        """
        归还图书
        :param book: 图书对象
        :return: True/False
        """
        # 如果学生会员压根没有借过该图书，则还书失败
        if book not in self.__books:
            print(f"会员{self.name}未借阅该图书:{book}")
            return False

        # 开始还书
        self.__books.remove(book)
        if not book.returning_book():
            print(f"图书已归还完:{book}")
            return False
        print(f"会员{self.name}归还图书{book.title}成功")
        return True

    @abstractmethod  # 抽象方法装饰器: 必须在子类中重写
    def get_max_borrowing_num(self) -> int:
        """
        获取会员最大借阅图书数量(普通会员类与VIP会员类重写此方法接口)
        :return: 会员最大借阅图书数量
        """
        pass

    def get_pwd(self):
        """
        获取会员密码(私有属性get方法)
        :return: 会员密码
        """
        return self.__pwd

    def get_books(self):
        """
        获取会员已借阅的图书列表(私有属性get方法)
        :return: 会员已借阅的图书列表
        """
        return self.__books


# 普通会员类
class OrdinaryMember(Member):
    def get_max_borrowing_num(self) -> int:
        """
        普通会员最大借阅图书数量为3本(重写父类方法)
        :return: 3
        """
        return 3

    pass


# VIP会员类
class VIPMember(Member):
    def __init__(self, member_id, name, pwd, vip_level):
        """
        初始化VIP会员对象(实例属性)
        :param member_id: 会员卡号
        :param name: 会员姓名
        :param pwd: 会员密码(私有属性)
        :param vip_level: VIP会员等级
        """
        Member.__init__(self, member_id, name, pwd)
        self.vip_level = vip_level

    def get_max_borrowing_num(self) -> int:
        """
        VIP会员最大借阅图书数量为6+VIP等级(重写父类方法)
        :return: 6+VIP等级
        """
        return 6 + self.vip_level


# 图示系统类
class LibrarySystem:
    def __init__(self):
        self.books = {}  # 图书字典: 键=图书编号, 值=图书对象
        self.members = {}  # 会员字典: 键=会员卡号, 值=会员对象
        self.login_member: Member | None = None  # 当前登录会员对象

        # 加载图书信息
        self.__load_books()

        # 加载会员信息
        self.__load_members()

    def __load_books(self):
        """
        加载图书信息
        :param f: 文件对象
        :return: None
        """
        with open('resources/books.json', 'r', encoding='utf-8') as f:
            books = json.load(f)
            for book in books:
                self.books[book['book_id']] = Book(**book)  # * 把可迭代对象拆成位置参数，** 把字典拆成关键字参数
            print("图书信息加载完成。")

    def __load_members(self):
        """
        加载会员信息
        :param f: 文件对象
        :return: None
        """
        with open('resources/members.json', 'r', encoding='utf-8') as f:
            members = json.load(f)
            for member in members:
                if member['member_id'].startswith('O'):
                    self.members[member['member_id']] = OrdinaryMember(**member)
                elif member['member_id'].startswith('V'):
                    self.members[member['member_id']] = VIPMember(**member)
            print("会员信息加载完成。")

    def login(self):
        """
        登录系统
        :return: True   登录成功
        """
        print("\n【欢迎来到登录页面】")

        while True:
            member_id = input("请输入会员卡号:")
            # 校验会员卡号
            if member_id is None or member_id not in self.members:
                print("登录失败！会员卡号不存在。")
                continue

            # 校验密码
            while True:
                pwd = input("请输入会员密码:")
                member: Member = self.members[member_id]
                if None is member or member.get_pwd() != pwd:
                    print("登录失败！密码错误。")
                    continue
                break

            self.login_member = member
            print(f"登录成功！欢迎{member.name}。")
            return True

    def borrowing_books(self):
        """
        借阅图书
        :return: None
        """
        print("\n【欢迎来到借阅页面】")

        # 展示图书馆所有图书
        for book in self.books.values():
            print(f"编号: {book.book_id}, 标题: {book.title}, 作者: {book.author}, 总数量: {book.total_num}, 可借数量: {book.get_available_num()}")

        # 获取用户选择的图书编号
        book_id = input("请输入图书编号:")

        #判断用户输入是否有误
        if book_id is None or book_id not in self.books:
            print("借阅失败！图书编号不存在。")
            return

        #开始借书
        if self.login_member:
            self.login_member.borrowing_book(self.books[book_id])
        else:
            print("借阅失败！请先登录。")
            return

    def returning_books(self):
        """
        归还图书
        :return: None
        """
        print("\n【欢迎来到归还页面】")

        if not self.login_member:
            print("归还失败！请先登录。")
            return

        # 展示用户已借阅的图书
        if len(self.login_member.get_books()) < 1:
            print("归还失败！您当前没有借阅任何图书。")
            return

        print("您已借阅的图书如下:")
        for book in self.login_member.get_books():
            print(f"编号: {book.book_id}, 标题: {book.title}")

        # 获取用户选择的图书编号
        book_id = input("请输入预归还的图书编号:")
        if book_id is None or book_id not in {bookObj.book_id for bookObj in self.login_member.get_books()}:
            print("归还失败！图书编号不存在。")
            return

        #归还图书
        self.login_member.returning_book(self.books[book_id])

    def query_borrowing(self):
        """
        查询借阅
        :return: None
        """
        print("\n【欢迎来到查询页面】")
        if not self.login_member:
            print("查询失败！请先登录。")
            return

        if len(self.login_member.get_books()) < 1:
            print("空空如也~")
            return

        print("您已借阅的图书如下:")
        for book in self.login_member.get_books():
            print(f"编号: {book.book_id}, 标题: {book.title}, 作者: {book.author}")

    def run(self):
        """
        运行系统
        :return: None
        """

        # 登录系统
        if not self.login():
            print("登录失败，程序退出。")
            return

        # 显示功能菜单
        while True:
            print(f"\n{'*' * 10} 欢迎来到图书借阅系统 {'*' * 10}")
            # 显示功能菜单
            print("\n1. 借阅图书")
            print("2. 归还图书")
            print("3. 查询借阅")
            print("5. 退出系统")

            # 获取用户选择
            choice = input("请输入你的选择:")
            match choice:
                case "1":
                    self.borrowing_books()
                case "2":
                    self.returning_books()
                case "3":
                    self.query_borrowing()
                case "5":
                    print("退出系统，程序结束。")
                    return
                case _:
                    print("无效的选择，请重新输入")


if __name__ == '__main__':
    library_system = LibrarySystem()
    library_system.run()
