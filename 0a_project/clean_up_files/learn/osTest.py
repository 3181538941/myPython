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
    os.makedirs('T/t/t/T/t/t/T/t/t/T/t/t/T/t/t')
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

# 如果 path 是 现有的 常规文件，则返回 True。本方法会跟踪符号链接，因此，对于同一路径，islink() 和 isfile() 都可能为 True。
os.path.isfile(path)
# 如果 path 是 现有的 目录，则返回 True。本方法会跟踪符号链接，因此，对于同一路径，islink() 和 isdir() 都可能为 True。
os.path.isdir(path)
# 如果 path 指向的 现有 目录条目是一个符号链接，则返回 True。如果 Python 运行时不支持符号链接，则总是返回 False。
os.path.islink(path)

def join():
    # 智能地拼接一个或多个路径部分。 返回值是 path 和 *paths 的所有成员的拼接，
    # 其中每个非空部分后面都紧跟一个目录分隔符，最后一个部分除外，这意味着如果最后一个部分为空，则结果将以分隔符结尾。
    # 如果某个部分为绝对路径，则之前的所有部分会被丢弃并从绝对路径部分开始继续拼接。
    os.path.join(path, *paths)

# 将路径 path 拆分为一对，即 (head, tail)，其中，tail 是路径的最后一部分，而 head 里是除最后部分外的所有内容。
# tail 部分不会包含斜杠，如果 path 以斜杠结尾，则 tail 将为空。
# 如果 path 中没有斜杠，head 将为空。如果 path 为空，则 head 和 tail 均为空。
# head 末尾的斜杠会被去掉，除非它是根目录（即它仅包含一个或多个斜杠）。
# 在所有情况下，join(head, tail) 指向的位置都与 path 相同（但字符串可能不同）。另请参见函数 dirname() 和 basename()。
os.path.split(path)

# 将路径 path 拆分为一对，即 (drive, tail)，其中 drive 是挂载点或空字符串。在没有驱动器概念的系统上，drive 将始终为空字符串。
# 在所有情况下，drive + tail 都与 path 相同。
os.path.splitdrive(path)


