#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/7/16
# @file 05_Future.py

import itertools
import random
import threading
import time
import heapq
import collections


# 未来产生的结果
class Future:
    def __init__(self):
        self._result = None
        self._done = False
        self._callbacks = []

    def set_result(self, result):
        if self._done:
            raise RuntimeError('Future is done!')
        self._result = result
        self._done = True

        for callback in self._callbacks:
            callback()

    def add_done_callback(self, callback):
        if self._done:
            callback(self)
        else:
            self._callbacks.append(callback)

    def result(self):
        if not self._done:
            raise RuntimeError('Future is not done!')
        return self._result

    def __await__(self):
        yield self
        return self.result()


async def small_step_yf():
    global loop
    fut = Future()
    # 指派一个目标来执行 set_result
    # loop.call_later(random.random(), fut.set_result, 'ok')
    fake_io_read(fut)
    return await fut


def fake_io_read(future):
    def read():
        time.sleep(random.random())
        future.set_result(random.randint(1, 100))

    threading.Thread(target=read).start()


async def big_step_yf():
    print('    begin small_step: ')

    small_result = await small_step_yf()

    print(f'    end small_step with {small_result}')
    # return small_result * 1000
    return small_result


async def one_task_yf():
    print('begin task')
    print('  begin big_step: ')

    big_result = await big_step_yf()

    print(f'  end big_step with {big_result}')
    print('end_task')


task_id_counter = itertools.count(1)


class TaskDrive:
    def __init__(self, coro):
        self.coro = coro
        self._done = False
        self._result = None
        self._id = f'Task-{next(task_id_counter)}'

    def run(self):
        print('--' * 5, f' {self._id} ', '--' * 5)
        if not self._done:
            try:
                x = self.coro.send(None)
            except StopIteration as e:
                self._result = e.value
            else:
                global loop
                assert isinstance(x, Future)
                x.add_done_callback(self.run)
        else:
            print('task is done')
        print('--' * 10)


class EventHandler(object):
    def __init__(self):
        # 使用双向队列来存储对应的回调函数及其参数
        self._ready = collections.deque()
        # 存储定时任务
        self._schedule = []
        # 初始化标志位
        self.stopping = False

    def call_soon(self, callback, *args):
        self._ready.append((callback, args))

    def call_later(self, delay, callback, *args):
        """
        定时任务
        :param delay: 延迟时间
        :param callback: 回调函数
        :param args: 回调函数所需参数
        :return:
        """
        # 将相对时间转为绝对时间
        t = time.time() + delay
        # 将self._schedule作为小顶堆来存储数据, 延迟时间短的自动移到前面
        heapq.heappush(self._schedule, (t, callback, args))

    def stop(self):
        self.stopping = True

    def run_forever(self):
        while True:
            # 首先执行一遍任务
            self.run_once()
            if self.stopping:
                break

    def run_once(self):
        now = time.time()
        # 处理定时任务
        if self._schedule[0][0] < now:
            _, cb, args = heapq.heappop(self._schedule)
            self.call_soon(cb, *args)

        # 处理应该执行的任务
        # 首先获取任务数量, 防止处理过程中有任务添加到_ready内
        num = len(self._ready)
        for _ in range(num):
            cb, args = self._ready.popleft()
            cb(*args)


loop = None


def main():
    global loop
    loop = EventHandler()
    # 这10个任务总时间是大于1s的, 但是他们是并行执行的, 所以总时间是小于1s的
    for i in range(10):
        task = TaskDrive(one_task_yf())
        loop.call_soon(task.run)

    loop.call_later(1, loop.stop)
    loop.run_forever()


if __name__ == '__main__':
    main()
