#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/7/15
# @file 01_生成器.py
def gen_test():
    for i in range(10):
        yield i


def gen_555(meet_yield):
    print('start')
    if meet_yield:
        print('meet yield')
        yield 555
        print('end')
    return 'finish'


if __name__ == '__main__':
    g = gen_test()
    print('test1''-' * 10)
    print(g)
    print(next(g))
    print(next(g))

    print('test2''-' * 10)
    try:
        print('******false')
        g555_false = gen_555(False)
        # 函数里有yield, 即使没执行, 也使得函数变成了一个生成器
        print(g555_false)
        # 生成器处于初始状态, 并未执行函数体, 需要调用next()才会执行函数体
        print(next(g555_false))
        # 生成器内并未执行到yield, 此时把返回值通过StopIteration抛出
    except StopIteration as e:
        print('StopIteration:', e.value, '\n')

    try:
        print('******true')
        g555_true = gen_555(True)
        # 生成器处于初始状态, 初次调用next()后, 执行到yield,
        # 并返回yield的值, 生成器停止在yield处
        print('first yield:', next(g555_true))
        # 再次调用next()后, 生成器从yield处继续执行,
        # 遇到return, 将返回值通过StopIteration抛出, 如果没有return, 将返回None
        print('second yield:', next(g555_true))
    except StopIteration as e:
        print('StopIteration:', e.value, '\n')
