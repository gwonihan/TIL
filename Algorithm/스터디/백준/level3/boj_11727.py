# 2xn 타일링 2
n = int(input())

tiling = [0] * 1001
tiling[1] = 1
tiling[2] = 3
tiling[3] = 5

for i in range(4,n+1):
    tiling[i] = tiling[i-1] + 2*tiling[i-2]

print(tiling[n]%10007)