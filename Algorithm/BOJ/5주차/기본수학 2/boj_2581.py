# 소수
m = int(input())
n = int(input())

resCnt = 0
res_list = []
for i in range(m,n+1):
    cnt = 0
    if i != 1:
        for j in range(2,i+1):
            if i % j == 0:
                cnt += 1
    if cnt == 1:
        res_list.append(i)
        resCnt += 1

if resCnt > 0:
    print(sum(res_list), min(res_list), end='\n')
else:
    print(-1)
