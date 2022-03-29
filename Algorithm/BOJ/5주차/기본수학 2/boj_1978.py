# 소수찾기

n = int(input())
resCnt = 0

num_li = list(map(int,input().split()))

for i in num_li:
    cnt = 0
    if i == 1:
        pass
    
    for j in range(2,i+1):
        if i % j == 0:
            cnt += 1
    
    if cnt == 1:
        resCnt +=1

print(resCnt)
