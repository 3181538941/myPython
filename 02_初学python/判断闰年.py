year=2000
while (year<=2500):
    a=year%4
    b=year%100
    c=year%400
    year=str(year)
    if (a!=0):
        print(year+'不是闰年')
    elif (b!=0):
        print(year+"是闰年")
    elif (c!=0):
        print(year+"不是闰年")
    else:
        print(year+"是闰年")
    year=int(year)
    year+=1
print('好啦ヾ(≧▽≦*)o')