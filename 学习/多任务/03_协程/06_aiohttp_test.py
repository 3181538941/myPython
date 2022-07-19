#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/7/17
# @file 06_aiohttp_test.py
import pprint
import time
import asyncio
from aiohttp import ClientSession

tasks = []
# url = "https://www.baidu.com/{}"
url = "https://m.tb.cn"


async def hello(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            print('Hello World:%s' % time.time())
            return await response.read()


def run():
    for i in range(5):
        # task = asyncio.ensure_future(hello(url.format(i)))
        task = asyncio.ensure_future(hello(url.format(i)))
        tasks.append(task)
    result = loop.run_until_complete(asyncio.gather(*tasks))
    # pprint.pprint(result)
    for res in result:
        print(res)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    run()
