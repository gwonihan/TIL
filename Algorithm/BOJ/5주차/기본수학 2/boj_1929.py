# 소수 구하기
M,N = map(int,input().split())

res_list = []
for i in range(M,N+1):
    cnt = 0
    if i != 1:
        for j in range(2, i+1):
            if i % j ==0:
                cnt += 1
    
    if cnt == 1:
        print(i)


