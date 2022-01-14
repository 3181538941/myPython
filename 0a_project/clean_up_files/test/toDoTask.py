import os
import random


# 创建文件夹
def mkdir():
    # 读文件列表
    ls = os.popen('ls task_love_of_leo').readlines()
    for i in range(len(ls)):  # 处理文件(去除\n)
        ls[i] = ls[i][:-1]
    # 防止重复创建文件夹
    if 'train' not in ls and 'val' not in ls:
        os.system('mkdir task_love_of_leo/train')
        os.system('mkdir task_love_of_leo/val')


# 读取文件列表
def fileScanner():
    ls = os.popen('ls task_love_of_leo').readlines()
    fileList = []
    for i in range(len(ls)):  # 处理文件(去除\n)
        ls[i] = ls[i][:-1]
        if ls[i][-4:] == '.txt':  # 取需要的文件, 避免把文件夹当作文件打开
            fileList.append(ls[i])
    return fileList


# 通过文件内容移动文件
def moveByWord(fileList):
    wordList = set()  # 初始化集合变量
    print(fileList)
    for i in fileList:
        with open(rf"task_love_of_leo/{i}", "r") as fp:
            fp.seek(0)  # 将文件指针移到文件首部
            rec = fp.readline()  # 读取文件内容
        rec = rec[:-1]  # 处理内容(去掉\n)
        if rec != '':  # 判空
            if rec not in wordList:  # 读取的内容不在集合内
                # 新建文件夹
                os.system(rf'mkdir task_love_of_leo/{rec}')
                # 添加到集合, 也是防止重复创建文件夹
                wordList.add(rec)
            else:
                # 移动文件
                os.system(rf"mv task_love_of_leo/{i} task_love_of_leo/{rec}")


# 移动随机的10个文件
def moveRandom(fileList):
    randFile = random.sample(fileList, 10)  # 生成不重复的随机列表
    print(randFile)
    for i in randFile:
        os.system(rf"mv task_love_of_leo/{i} task_love_of_leo/val")


# 将剩余的文件移动到train文件夹内
def moveOthers(fileList):
    for i in fileList:
        os.system(rf"mv task_love_of_leo/{i} task_love_of_leo/train")


if __name__ == '__main__':
    mkdir()
    files = fileScanner()
    moveByWord(files)
    files = fileScanner()
    moveRandom(files)
    files = fileScanner()
    moveOthers(files)
    files = fileScanner()

# import os
#
# # for i in range(1, 101):
# #     os.system(f'touch {i:03d}.log')
#
# fileList = []
# for i in range(1, 100):
#     fileList.append(f'{i:03d}')
# for i in range(99):
#     if fileList[i][-1] == '2':
#         fileList[i] = f'e{fileList[i]}'
#     if fileList[i][-1] == '6':
#         fileList[i] = f'l{fileList[i]}'
#     if fileList[i][-1] == '7':
#         fileList[i] = f'q{fileList[i]}'
#     if fileList[i][-1] == '8':
#         fileList[i] = f'{fileList[i]}e'
#     if fileList[i][-1] == '9':
#         fileList[i] = f'{fileList[i]}n'
#     if fileList[i][-1] == '0':
#         fileList[i] = f'{fileList[i]}z'
#     if fileList[i][-2] == '3':
#         fileList[i] = f's{fileList[i]}t'
#     if fileList[i][-2] == '5':
#         fileList[i] = f'w{fileList[i]}f'
#     if fileList[i][-2] == '8':
#         fileList[i] = f'b{fileList[i]}e'
#     if fileList[i][-3] == '0':
#         fileList[i] = f'l{fileList[i]}'
# # print(fileList)
# # for i in fileList:
# #     print(f'"{i}"',end=',')
# #     os.system(f'touch {i}.txt')
#
# wordFile = ["l093", "b085e", "ll076", "w055f", "b078ee", "l013", "sq037t", "b018ee", "w054f", "lq007", "b038ee", "080z",
#             "le012", "079n", "l009n", "l003", "wl056f", "099n", "b098ee", "039n", "l005", "l011", "090z", "lq017",
#             "le042", "bl086e", "l041", "bq087e", "l004", "le092", "ll016", "l075", "lq077", "b008ee", "040z", "l074",
#             "b084e", "l091", "ll006", "010z"]
# print(len(wordFile))
#
# sum_num = 0
# sum_e =0
# for i in fileList:
#     # if '1' < i[-1] < '9':
#     #     os.system(f'echo "num" > {i}.txt')
#     #     sum_num += 1
#     if i[0] == '0':
#         os.system(f'echo "error" > {i}.txt')
#         sum_e += 1
#
# print(sum_e)

# toDoTask.py
