h,m = map(int,input().split())
a = m-45
b = h-1
if a<0 and h-1<0:
    print(23,a+60)
elif a<0 and h-1>0:
    print(b,a+60)
    