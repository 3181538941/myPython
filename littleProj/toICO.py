# import sys
# from PIL import Image
#
# # from os import path
# argFile = sys.argv[1]
#
# img = Image.open(argFile).resize((64, 64))
# img.save(argFile.replace('.png', '.ico'), 'ico')

# # name = argFile.split('.')
# # name = '.'.join(name[:-1])
# # goalName = name + '.ico'
# # img.save(goalName)


import os
import PythonMagick as m

sourcePath = r'D:\林深雾起\OneDrive\图片\ico\win11ico'

fileList = os.listdir(sourcePath)


def ToICO(filePath):
    img = m.Image(filePath)
    img.sample('256x256')
    img.write(filePath.replace('.png', '.ico'))






if __name__ == '__main__':
    for file in fileList:
        if file.endswith('.png'):
            print(file, 'start')
            ToICO(os.path.join(sourcePath, file))
