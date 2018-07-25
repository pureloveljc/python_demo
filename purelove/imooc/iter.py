# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "2018/7/17 下午10:18"


class User():
    def __init__(self, name, list1):
        self.list1 = list1
        self.name = name
        self.index = 0

    # def __getitem__(self, item):  # 支持切片
    #     return self.list1[item]

    def __str__(self):
        return self.name

    def __len__(self):
        return len(self.list1)

    def __iter__(self):  # 不支持切片
        return

    def __next__(self):  # 迭代器 但是原则上应该再定义一个对象 不要写在 这样写不符合编程规范
        try:
            word = self.list1[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word



if __name__ == '__main__':
    u1 = User('ljc', [0, 1, 2, 3, 4, 5, 6])
    print(next(u1))
    print(next(u1))
    print(next(u1))
    print(next(u1))
    print(next(u1))
    print(next(u1))
    print('数量:'+str(len(u1)))
    print('my name is '+str(u1))
    print(next(u1))
    print(u1)