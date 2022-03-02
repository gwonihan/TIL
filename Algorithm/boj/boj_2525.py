h,m = map(int,input().split())
t = int(input())

if 120 > m+t > 60 and h !=23:
    print(h+1, m+t-60)
elif m+t > 60 and h == 23:
    print(0, m+t-60)
elif m+t == 120 and h ==22:
    print(0, 0)
elif m+t == 120 and h ==23:
    print(1,0)
elif m+t == 120 and h !=22:
    print(h+2,0)
elif m+t < 60:
    print(h,m+t)
