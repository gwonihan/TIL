#Four Squares
n = int(input())
count = 0

DP = [0] * (50001)

k = 1
while k**2 <= n:
    DP[k**2] = 1
    k += 1

for i in range(1, n + 1):
    if DP[i] != 0:
        continue
    j = 1
    while j*j <= i:
        if DP[i] == 0:
            DP[i] = DP[j*j] + DP[i - j*j]
        else:
            DP[i] = min(DP[i], DP[j*j] + DP[i - j*j])
        j += 1
print(DP[n])