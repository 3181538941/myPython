#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/5/31
# @file copyContent.py
# clip
from pyperclip import copy

path = './data'
outFile = './content.txt'
encoding = 'utf-8'
fileType = 'java'


def viewPath(_path, _fileType):
    javaFile = []
    # 删除_fileType中的.
    _fileType = _fileType.replace('.', '')
    for dirPath, dirNames, fileNames in os.walk(_path):
        print('walk:', dirPath, dirNames, fileNames)
        for file in fileNames:  # 在dirPath文件夹内循环
            # 要查找的文件类型不在目标文件夹内, 文件类型符合要求, 文件不在排除的文件列表内
            if file.split('.')[-1] == _fileType:
                # toMove: 存储文件信息的二维列表, [[文件名, 文件类型, 文件父路径, 文件绝对路径, 文件目标路径], ]
                javaFile.append(dirPath + '/' + file)
    return javaFile


def readFiles(javaFile):
    _content: str = ''
    for file in javaFile:
        with open(file, 'r', encoding=encoding) as f:
            _content += ''.join(f.readlines())
    # 写入到文件以防万一
    with open(outFile, 'w', encoding=encoding) as f:
        f.write(_content)
    return _content


if __name__ == '__main__':
    print('leo 2022/5/31 构建')
    path = input('请输入路径: ')
    fileType = input('请输入后缀名: ')
    Files = viewPath(path, fileType)
    print('复制内容的文件: ', Files)
    content = readFiles(Files)
    copy(content)
    input('复制完成, 按任意键并回车退出')
    # input('写入文件完成, 请查看content.txt\n按任意键并回车退出')
