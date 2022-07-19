#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/7/17
# @file sort_time_test.py
import time
import bisect


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter_ns()
        ret = func(*args, **kwargs)
        end = time.perf_counter_ns()
        print(f'{func.__name__}耗时: ', end - start)
        return ret

    return wrapper


@timeit
def simple_sort(lst):
    return sorted(lst)


@timeit
def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        # 基准元素
        pivot = lst[0]
        left = [i for i in lst[1:] if i <= pivot]
        right = [i for i in lst[1:] if i > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == '__main__':
    # with open('data.txt', 'r') as f:
    #     lst = eval(f.read())
    lst = [1, 3, 4, 2, 5]
    sorted_lst = simple_sort(lst)
    print(sorted_lst)
    ind = bisect.bisect_left(sorted_lst, 5)
    print(ind)
    # quick_sort(lst)
