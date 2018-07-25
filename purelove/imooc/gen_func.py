# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "2018/7/17 下午10:48"
# 生成器 只要有yield关键字就是生成器


def gen_func():
    yield 1
    yield 2
    yield 3
# 惰性求值  延迟求职提供了可能
# 斐波那契  0 1 1 2 3 5 8

def gen():
    return 2


def fib1(index):
    if index <= 2:
        return 1
    else:
        return fib(index-1) + fib(index-2)

def fib(index):
    n = 0
    a = 0
    b = 1
    fib_list = [0]
    while n < index:
        fib_list.append(b)
        a, b = b, a+b
        n += 1
    return fib_list

def gen_fib(index):
    n = 0
    a = 0
    b = 1
    # fib_list = [0]
    while n < index:
        # fib_list.append(b)
        yield b
        a, b = b, a+b
        n += 1
    # return fib_list


if __name__ == '__main__':
    gen_func = gen_func()
    print(gen_func)  # 这是一个对象  生成器对象，python编译字节码的时候就产生了  ,实现了一个迭代协议
    for v in gen_func:
        print(v)
    gen1 = gen()
    print(gen1)  # return返回一个值
    print(fib(10))  # 如果index是300万  非常消耗内存  但是有生成器的话 如下 for 循环实现了迭代协议
    gen2 = gen_fib(10)
    for i in gen2:
        print(i)
