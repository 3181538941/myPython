#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/4/19
# @file jobs_create.py
import pymysql

JOB_INFO = ['公共会计师', '会计经理', '行政助理', '总裁', '行政副总裁', '会计师',
            '财务经理', '人力资源代表', '程序员', '营销经理', '营销代表', '公关代表',
            '采购文员', '采购经理', '销售经理', '销售代表', '运输文员', '库存文员', '库存经理']

JOB_DICT = {
    1: ['行政副总裁', '首席财务官', '总会计师', '财务总监', '资金总监', '财务部经理', '审计主管', '会计', '助理'],
    2: ['人事部总监', '人事经理', '人事部主管', '公关代表', '行政助理', '行政总裁', ],
    3: ['采购文员', '采购经理', '销售经理', '销售代表', '运输文员', '库存文员', '库存经理'],
    4: ['生产经理', '车间主任', '机电组长', '生产管理员', '生产组长', '生产技术员', '生产技工'],
    5: ['运维员', '信息经理', '信息主管', '前端主管', '后端主管', '程序员', '网络工程师', '网络主管', '网络经理', '网络专员']
}

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
    for i in JOB_DICT.keys():
        for j in JOB_DICT[i]:
            cursor.execute("insert into emp_ms.job (name, dep_id) values (%s,%s)", (j, i))
    # 提交事务
    connect.commit()
    print("新建职位表成功")
    data = cursor.execute("select * from emp_ms.job")
    print(cursor.fetchall())
    print('新建了', data, '条职位信息')
    # 关闭游标
    cursor.close()
    # 关闭连接
    connect.close()
