a,b,c = map(int,input().split())

for i in range(a):
    for j in range(b):
        for f in range(c):
            print(i,j,f)
print(a*b*c)