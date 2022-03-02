a,b = map(int,input().split())
li = []

for i in range(a+1):
    li.append([])
    for j in range(b+1):
        li[i].append(0)

c = int(input())

for _ in range(c):
    q,w,e,r = map(int,input().split())
    
    if w == 0:
        for i in range(q):
            li[e][r+i] = 1
    elif w == 1:
        for j in range(q):
            li[e+j][r] = 1
    else:
        continue

for i in range(1,a+1):
    for j in range(1,b+1):
        print(li[i][j], end=' ')
    print()