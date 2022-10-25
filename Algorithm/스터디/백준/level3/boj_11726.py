# 2xn 타일링
n = int(input())

tiling = [0] * 1001
tiling[1] = 1
tiling[2] = 2
tiling[3] = 3

for i in range(4,n+1):
    tiling[i] = tiling[i-1] + tiling[i-2]
print(tiling[n]%10007)
