#!/usr/bin/env python
# coding: utf-8

import os
import hashlib
import pymysql
from time import time
from pprint import pprint
from lanzou.api import LanZouCloud

fileNameUrlDict = {}
md_path = r'D:\0a.dataout\test\lanzou\fileNameUrl.md'
cookie182 = {
    'ylogin'      : '1688674',
    'phpdisk_info': "U2YFMVI4AzcPOwRjDmADUAZiUVpbM1E%2BBDVXM1RhV2VVYwA0BWNVbwAwVw5dPlBpAjEFZg9lUzQGMQJjBGQLbVM0BWVSZANsDzwEYA5sA24GZlE1WzZRNQQ%2BVzBUMFcwVWYAZAU0VWsAYVdjXQ5QOwJqBTUPYlM3BjUCYAQ0Cz1TYQU1",
}

cookie131 = {
    'ylogin'      : '2678914',
    'phpdisk_info': 'AjRWYgdiATUAOwBhDGJTAAVhAAsKYlUxVGYCZQ44AzQENlJpA2EBPgE1AVgObQA5VWYEZwpgBWIDNFU0VzcKbAJlVjYHMQFuADMAZAxuUz4FZQBkCmdVMVRuAmUOagNkBDdSNgMyAT8BYAE1Dl0Aa1U2BDcKZAViAzVVM1doCjgCNVZi',
}
config = {
    'host'    : "localhost",
    'port'    : 3306,
    'user'    : "root",
    'passwd'  : "031214",
    'charset' : 'utf8',
    'database': 'mydata',
}
connect = pymysql.connect(**config)
# 获取游标对象
cursor = connect.cursor()

lzy = LanZouCloud()

lzy.login_by_cookie(cookie131)


def split_name_type(file_path):
    """分割文件路径, 返回文件类型, 文件名, 文件夹路径"""
    splitext = os.path.splitext(file_path)
    file_name = os.path.basename(splitext[0])
    file_type = splitext[1][1:]
    return file_name, file_type


def writeToMd(file_path, content):
    """将内容写入文件"""
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(content)
        print(content)


def isBigFile(file_path, size_limit=100):
    """
    判断文件大小是否大于size_limit
    :param file_path: 需要判断的文件路径
    :param size_limit: 大小限制
    :return: 大于size_limit返回-1, 否则返回文件大小
    """
    # 文件大于100MB
    file_bytes = os.path.getsize(file_path)
    file_size_MB = file_bytes / 1048576
    if file_size_MB > size_limit:
        with open('ignore.md', 'a', encoding='utf-8') as f:
            file_name = os.path.basename(file_path)
            f.write(f'[{file_name}]({file_path}) 大小: {file_size_MB:.2f}MB\n\n')
        return -1
    else:
        file_size_MB = f'{file_size_MB:.2f}'
        return file_size_MB


def getFileMd5(file_path):
    # 计算文件md5
    md5 = hashlib.md5()
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(4096)
            if not data:
                break
            md5.update(data)
    return md5.hexdigest()


def writeDictToMd():
    """将文件名和文件路径写入文件"""
    with open(md_path, 'a', encoding='utf-8') as f:
        for key, value in fileNameUrlDict.items():
            f.write(f"[{key}]({value})\n\n>\n\n")


def show_progress(file_name, total_size, now_size):
    """显示进度的回调函数"""
    percent = now_size / total_size
    bar_len = 40  # 进度条总长度
    bar_str = '#' * round(bar_len * percent) + '=' * round(bar_len * (1 - percent))
    print('\r{:.2f}%\t[{}] {:.1f}/{:.1f}MB | {} '.format(
        percent * 100, bar_str, now_size / 1048576, total_size / 1048576, file_name), end='')
    if total_size == now_size:
        print('')  # 下载完成换行


def handler(fid, is_file):
    """上传完成回调函数"""
    if is_file:
        lzy.set_passwd(fid, 'leo0')
        # 获取文件链接
        share_info = lzy.get_share_info(fid, is_file=True)
        # 存储文件名和链接
        file_name = split_name_type(share_info.name)[0]
        fileNameUrlDict[file_name] = share_info.url


def workingWithFolders(folder_path, passwd='leo0'):
    # 获取蓝奏云账号下所有文件夹信息
    all_dirs = lzy.get_move_folders()
    # 获取文件夹id, 不存在为None
    dir_info = all_dirs.find_by_name(folder_name)
    if dir_info:  # 文件夹存在, 获取文件夹id 并赋给dir_id
        dir_id = dir_info.id
        dir_share_info = lzy.get_share_info(dir_id, is_file=False)
        dir_url = dir_share_info.url
    else:  # 文件夹不存在, 新建文件夹
        dir_id = lzy.mkdir(parent_dir_id, folder_name)
        dir_url = lzy.get_share_info(dir_id, is_file=False).url
        lzy.set_passwd(dir_id, passwd, is_file=False)
    return dir_id, dir_url


def scanDir(dir_path, parent_dir_id=-1):
    """
    遍历文件夹, 并上传文件
    :param dir_path: 文件夹路径
    :param parent_dir_id: 文件夹id
    """
    # 获取目录名
    folder_name = os.path.basename(dir_path)
    dir_id, dir_url = workingWithFolders(folder_name)
    # dir_id = 1
    # dir_url = dir_path
    # 将父目录名写入markdown
    writeToMd(md_path, f'# [{folder_name}]({dir_url})\n\n')
    # 文件名-链接 字典初始化
    global fileNameUrlDict
    fileNameUrlDict = {}
    dir_list = []  # 待处理文件夹列表
    for _file in os.listdir(dir_path):
        # 处理文件路径
        file_path = os.path.join(dir_path, _file)
        # 文件, 大小合理 存储后上传
        if os.path.isfile(file_path):
            file_size = isBigFile(file_path)
            # 大文件 存储日志, 直接跳过
            if file_size == -1:
                continue
            # 获取文件md5
            file_md5 = getFileMd5(file_path)
            global cursor
            # 判断文件在数据库内是否已存在
            cursor.execute(f"select md5_value from mydata.tool_md5 where md5_value=%s", (file_md5))
            cursor_fetchall = cursor.fetchall()
            # 文件不存在, 将数据写入数据库
            if cursor_fetchall == ():
                cursor.execute(f"insert into mydata.tool_md5 (md5_value, tool_name, tool_size, tool_path)values(%s, %s, %s, %s)",
                               (file_md5, _file, file_size, dir_path))
                # lzy.upload_file(
                #     file_path,
                #     folder_id=dir_id,
                #     callback=show_progress,
                #     uploaded_handler=handler
                # )
                # leNameUrlDict[_file] = file_path
            else:
                print(f'{_file} 已存在')
                continue
            continue
        # 文件夹, 入队, 文件处理完成后统一处理
        if os.path.isdir(file_path):
            toDealDirPath = os.path.join(dir_path, _file)
            dir_list.append(toDealDirPath)
    # 文件上传完成后, 将数据写入markdown文件
    # for name in fileNameUrlDict:
    #     writeToMd(md_path, f'[{name}]({fileNameUrlDict[name]})\n\n')
    writeDictToMd()
    # 处理文件后处理文件夹
    for _dir_path in dir_list:
        # scanDir(_dir_path, parent_dir_id=dir_id)
        scanDir(_dir_path, dir_id)


# if 1==1:
#     print('上传完成')
#     print(lzy.get_file_list(5479523))
if __name__ == '__main__':
    scanDir(r'F:\01_软件,环境\01_工具', -1)
    # scanDir(r'F:\01_软件,环境\03_压缩', 5506472)
    ...
    # 提交MySQL命令
    # _cursor.execute("insert into mydata.soft(name, url) values(%s, %s)", (soft_name, soft_url))
    # _cursor.execute("select url from mydata.soft where name=%s", ('WinRAR',))
    # print(_cursor)
    # print(_cursor.fetchone()[0])
    # _cursor.execute("select url from mydata.soft where name=%s", ('Wi2nRAR',))
    # print(_cursor)
    # print(_cursor.fetchall())

    # 提交事务
    connect.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    connect.close()

# In[41]:


# dir_path = r'F:\01_软件,环境\01_工具'
# parent_folder_name = os.path.basename(os.path.dirname(dir_path))
# print(parent_folder_name)
# print(os.path.basename(dir_path))
# print(os.path.dirname(dir_path))

# In[35]:


# a = [1, 2, 3, 4, 5]
# while len(a) > 0:
#     print(a)
#     print(a.pop(0))

# # 之前处理逻辑
# ```python
# for root, dirs, files in os.walk(dir_path):
#     for _file in files:
#         file_path = os.path.join(root, _file)
#         # 上传文件, 在回调函数中获取链接, 存储到全局变量内
#         lzy.upload_file(
#             file_path,
#             folder_id=5479523,
#             callback=show_progress,
#             uploaded_handler=handler
#         )
# ```

# In[21]:


# for file in lzy.get_file_list(5479523):
#     print(file.name)

# createFlag = lzy.mkdir(-1, 'test')
# if createFlag == LanZouCloud.SUCCESS:
#     print('创建成功')
# else:
#     print('创建失败')

# lzy.rename_dir(5479523, '操作')
# print(lzy.get_dir_list())

# os.path.getsize(r'D:\0a.dataout\test\soft\soft.html') / 1024
# # lzy.upload_file()
