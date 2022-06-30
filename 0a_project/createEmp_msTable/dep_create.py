#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/4/19
# @file dep_create.py
# @description 新建部门表

import pymysql

Name = "财政部 人事部 市场部 生产部 信息部"
NameList = Name.split(" ")

if __name__ == '__main__':

    config = {
        'host'    : "localhost",
        'port'    : 3306,
        'user'    : "root",
        'passwd'  : "031214",
        'charset' : 'utf8',
        'database': 'learn',
    }
    connect = pymysql.connect(**config)
    # 获取游标对象
    cursor = connect.cursor()
    # 提交MySQL命令
    for i in range(len(NameList)):
        cursor.execute("insert into emp_ms.department (id, name, manager_id) values (%s,%s,%s)", (str(i + 1), NameList[i], str(i * 2 + 1)))
        # 提交事务
    connect.commit()
    print("新建部门表成功")
    data = cursor.execute("select * from emp_ms.department")
    print(cursor.fetchall())
    print(data)
    # 关闭游标
    cursor.close()
    # 关闭连接
    connect.close()
