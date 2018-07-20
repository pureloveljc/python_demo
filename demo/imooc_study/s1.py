#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "18-7-16 下午1:43"


class User:
    def __init__(self, name, age, empl):
        self.name = name
        self.age = age
        self.empl = empl

    @property
    def shengao(self):
        return "170"

    def __str__(self):
        return '我的名字是%s' % (self.name)

    def __getitem__(self, item):
        return self.empl[item]

    def __len__(self):
        return len(self.empl)


if __name__ == '__main__':
    u1 = User('ljc', 18, ['a', 'b', 'c'])
    print(u1[0])
    print (u1)
    print(len(u1))
