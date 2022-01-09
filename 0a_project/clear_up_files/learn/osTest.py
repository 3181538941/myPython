#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/1/8
# @file osTest.py
import os,sys

# 获取当前工作路径, 返回表示当前工作目录的字符串
dir = os.getcwd()
# 将当前工作目录更改为 path : path应为目录路径, 不能是文件。
os.chdir(dir)

# 返回路径的文件系统表示。
path = os.fspath(sys.argv[0])

def mkdir():
    # 创建一个名为 path 的目录
    os.mkdir('temp')
    # 递归目录创建函数。与 mkdir() 类似，但会自动创建到达最后一级目录所需要的中间目录。
    os.makedirs('T/t/t')

def rmsth():
    # 移除（删除）文件 path。 如果 path 是目录，则会引发 IsADirectoryError。
    os.remove('t.py')
    # 移除（删除）目录 path。如果目录不存在或不为空，则会分别抛出 FileNotFoundError 或 OSError 异常。要删除整个目录树，可以使用 shutil.rmtree()。
    os.rmdir('temp')

def rename(old,new):
    # 将文件或目录 old 重命名为 new。如果 new 已存在，则下列情况下将会操作失败，并抛出OSError的子类
    os.rename(old,new)
    # 递归重命名目录或文件。工作方式类似 rename()，除了会首先创建新路径所需的中间目录。重命名后，将调用 removedirs() 删除旧路径中不需要的目录。
    os.renames(old, new)
    # 将文件或目录 src 重命名为 dst。如果 dst 是目录，将抛出 OSError 异常。如果 dst 已存在且为文件，则在用户具有权限的情况下，将对其进行静默替换。如果 src 和 dst 在不同的文件系统上，本操作可能会失败。如果成功，重命名操作将是一个原子操作（这是 POSIX 的要求）
    os.replace(src,dst)

# 查看路径下的文件, 默认参数为 ".", 参数应为目录
print(os.listdir(dir))

# 获取文件大小
def getsize(path):
    size = os.path.getsize(path)
    print(f'{size:,}')

getsize(path)

os.symlink('osTest.py','linkos')