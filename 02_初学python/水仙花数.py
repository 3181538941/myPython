# m=int(input())
# n=int(input())
for i in range(100,999):
    a=i//100
    b=(i-a*100)//10
    c=(i-a*100-b*10)
    if (i==pow(a,3)+pow(b,3)+pow(c,3)):
        print(i)