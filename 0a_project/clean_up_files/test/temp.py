import os
from pprint import pprint


class ViewFile(object):
    def __init__(self, path, kwargs):
        self.allFile = {}
        self.path = path
        self.toMove = [] # 需要移动文件列表, [文件名, 所在目录, 绝对路径]
        self.clean1(path, kwargs)

    def viewTarget(self, dirPath):
        pass
        # todo view the goal dir and list files to judge
        fileList = os.listdir(dirPath)
        return fileList

    def clean_old(self, path, kwargs):
        fileList = os.listdir(path)
        for item in fileList:
            absPath = os.path.join(path, item)
            # todo walk
            if os.path.isdir(absPath):
                # todo append dirName
                self.clean(absPath, kwargs)
            else:
                for typ in kwargs.keys():
                    if item.endswith(typ):
                        if typ not in self.allFile.keys():
                            self.allFile[typ] = []
                        self.allFile[typ].append(item)
                        if item not in self.viewTarget(kwargs[typ]):
                            os.popen(rf'move {absPath} {kwargs[typ]}')
                            self.hasMoved.append(item)

    def clean1(self, path, kwargs):

        def isInKey(file, keyList):
            """
            判断文件是否在文件类型内
            :param file: 需要判断的文件名
            :param keyList: 文件类型, type: 用空格分隔的字符串
            :return: 在字符串内返回 True
            """
            for item in keyList.split():
                if file.endswith(item):
                    return 1
            return 0


        for typ in kwargs.keys():  # 按文件类型循环
            for dirPath, dirNames, fileNames in os.walk(path):
                for file in fileNames:  # 在dirPath文件夹内循环
                    if dirPath != kwargs[typ] and isInKey(file, typ):  # 要查找的文件类型不在选定文件夹内
                        self.toMove.append([file, dirPath,os.path.join(dirPath,file)])
                        # self.toMove.append(file)
                        if typ not in self.allFile.keys():
                            self.allFile[typ] = []
                        self.allFile[typ].append(file)
                    # pprint(dirPath)
                    # pprint(dirNames)
                    # pprint(fileNames)


# path = r'F:\03_Important\Python\0a_project\clear_up_files'
path = r'E:\Download\云盘缓存'

# dic = {'exe': r'E:\Download\exes',
#        'zip': r'E:\Download\Compressed',
#        'rar': r'E:\Download\Compressed'}
dic = {'exe'       : r'E:\Download\云盘缓存\exes',
       'zip rar 7z': r'E:\Download\云盘缓存\Compressed'}

list = ViewFile(path, dic)
pprint(list.allFile)
print('toMove')
pprint(list.toMove)
