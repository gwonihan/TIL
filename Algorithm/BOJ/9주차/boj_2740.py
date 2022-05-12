# 행렬곱셈

# 행렬 A
N, M = map(int,input().split())
A = []
for _ in range(N):
    A.append(list(map(int,input().split())))

# 행렬 B
M, K = map(int,input().split())
B = []
for _ in range(M):
    B.append(list(map(int,input().split())))

for l in range(K):
    cnt = 0
    for i in range(N):
        for j in range(M):
            cnt += A[i][j] * B[j][l]
        print(cnt)