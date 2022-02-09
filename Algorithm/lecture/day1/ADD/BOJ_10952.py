# 입력의 마지막 어쩌고 하면 while
# 마지막 입력이 언젠지 알수있으면 for
while True:
    a,b = map(int,input().split())
    if(a,b) == (0,0):
        break
    else:
        print(a+b)
