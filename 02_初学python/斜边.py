l=input('请输入三角形的一条直角边:')
w=input('请输入三角形的另一条直角边:')
def third_side (length,width):
    length=int(length)
    width=int(width)
    third=(length**2+width**2)**0.5
    return third
print('三角形的斜边是:'+str(third_side(l,w)))