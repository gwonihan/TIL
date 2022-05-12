# 행렬곱셈
N, M = map(int,input().split())
A = []
B = []
for _ in range(N):
    A.append(list(map(int,input().split())))

M, K = map(int,input().split())

for _ in range(M):
    B.append(list(map(int,input().split())))

for i in len(A):
    for j in len(B):
        A[i] 