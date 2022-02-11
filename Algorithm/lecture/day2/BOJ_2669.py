#직사각형 네개의 합집합의 면적 구하기
paper = [[0] * 100 for i in range(100)]

for _ in range(4):
    a,b,c,d = map(int, input().split())
    for x in range (a,c):
        for y in range(b,d):
            paper[x][y] = 1
    

total = 0
for i in range(100):
    for j in range(100):
        total += paper[i][j]
print(total)



    # for i in range(x):
    #     for j in range