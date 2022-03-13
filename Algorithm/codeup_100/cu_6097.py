a,b = map(int,input().split())
li = []

for i in range(a):
    li.append([])
    for j in range(b):
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

for i in range(a):
    for j in range(b):
        print(li[i][j], end=' ')
    print()