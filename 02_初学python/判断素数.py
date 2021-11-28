w=0
n=input('请输入想要判断的数字:')
i=2
n=int(n)
while i<=(n**0.5) :
    r=n%i
    if r==0:
        w=1
    else:
        i+=1
    if w!=0 :break
if w==0:
    print(str(n)+'是素数')
else:
    print(str(n)+'不是素数')
