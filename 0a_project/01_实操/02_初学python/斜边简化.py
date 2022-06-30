length=input('请输入三角形的一条直角边:')
width=input('请输入三角形的另一条直角边:')
length=int(length)
width=int(width)
third_side=(length**2+width**2)**0.5
print('三角形的斜边是:'+str(third_side))