#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/7/15
# @file 03_协程_await.py
import time


class Awaitable:
    def __init__(self, obj):
        self.value = obj

    def __await__(self):
        yield self


async def small_step_yf():
    print('      工作中')
    # yield time.sleep(1)
    # 自身无法消除阻塞, 将阻塞传给上游, 注: 此处 time.sleep, 2是作为元组传递的
    print('      歇会')
    # 为了防止元组被当作可迭代对象来创造成一个生成器, 借助工具类YieldFromAble将元组统一进行返回
    await Awaitable((time.sleep, 2))
    print('      歇完了')
    return 666


async def big_step_yf():
    print('    begin small_step: ')

    small_result = await small_step_yf()

    print(f'    end small_step with {small_result}')
    return small_result * 1000


async def one_task_yf():
    print('begin task')
    print('  begin big_step: ')

    big_result = await big_step_yf()

    print(f'  end big_step with {big_result}')
    print('end_task')


class TaskDrive:
    def __init__(self, coro):
        self.coro = coro
        self._done = False
        self._result = None

    def run(self):
        print('--' * 10)
        if not self._done:
            try:
                x = self.coro.send(None)
            except StopIteration as e:
                self._result = e.value
            else:
                assert isinstance(x, Awaitable)
        else:
            print('task is done')
        print('--' * 10)


def main():
    t = TaskDrive(one_task_yf())
    t.run()
    # 程序分段执行, 在此处暂停, 等待两秒
    for _ in range(10):
        print(f'刷第{_ + 1}个视频 ...')
        time.sleep(0.2)
    t.run()


if __name__ == '__main__':
    main()
