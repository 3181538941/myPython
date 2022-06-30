#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/2/22
# @file termux_test.py
import json
path = r'D:\林深雾起\OneDrive\文档\0a.dataout\备用\en_words.json'
with open(path,'r',encoding='utf-8') as jsonFile:
    jsonPy = json.load(jsonFile)
for eachDic in jsonPy:
    eachDic["word"] = eachDic.pop("hitokoto")
    del eachDic['source']
    li = eachDic['word'].split()
    eachDic['word'] = li[0]
    eachDic['symbol'] = li[1]
    eachDic['mean'] = ' '.join(li[2:])

print(jsonPy)
# print(jsonPy)
# print(type(jsonPy))
# symbol mean
with open('test/jsonTest.json', 'w', encoding='utf-8') as f:
    json.dump(jsonPy,fp=f,ensure_ascii=False)
