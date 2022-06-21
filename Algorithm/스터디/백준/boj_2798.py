# 블랙잭
N,M = map(int,input().split())
num_list= list(map(int,input().split()))
answer = 0

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if num_list[i] + num_list[j] + num_list[k] > M:
                continue
            else:
                answer = max(answer, num_list[i] + num_list[j] + num_list[k])

print(answer)