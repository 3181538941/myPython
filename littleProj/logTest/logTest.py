#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/6/26
# @file logTest.py
import logging

# logging.basicConfig(filename='rec.log',
#                     filemode='w',
#                     datefmt="%Y-%M-%d %H:%M:%S",
#                     format='%(asctime)s %(name)s:%(levelname)s:%(message)s',
#                     level=logging.DEBUG)
# logging.debug('this is a debug message')
# logging.info('this is an info message')
# logging.warning('this is a warning message')
# logging.error('this is an error message')
# logging.critical('this is a critical message')

# 调试日志设置
# 设置log实例名称
logger = logging.getLogger('leoTest')
# 设置日志级别为ERROR，即只有日志级别大于等于ERROR的日志才会输出
# logger.setLevel(logging.ERROR)
logger.setLevel(logging.INFO)
# 创建一个格式化器
formatter = logging.Formatter(
    fmt="%(asctime)s [line:%(lineno)d] %(funcName)s %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
# 创建流处理器
console = logging.StreamHandler()
# 为处理器设置格式化器
console.setFormatter(formatter)
# 创建文件处理器
log_path = 'rec.log'
file_handler = logging.FileHandler(
    filename=log_path,
    mode='a',
    encoding='utf-8'
)
file_handler.setFormatter(formatter)
# 为实例添加处理器
logger.addHandler(file_handler)
logger.addHandler(console)


def test_raise():
    a = 5
    b = 0
    try:
        c = a / b
    except ZeroDivisionError as e:
        logger.exception(e)
    finally:
        logger.debug('Debug')
        logger.info('Info')
        logger.warning('Warn')
        logger.error('Error')
        logger.critical('Critical')


if __name__ == '__main__':
    test_raise()
