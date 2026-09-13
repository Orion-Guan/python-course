"""
图书实体类
"""
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
