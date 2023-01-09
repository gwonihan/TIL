# 구간 합 구하기 4
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num_li = list(map(int, input().split()))

part_sum = [0] * (n + 1)

# s = 0
# for i in range(n):
#     s += num_li[i]
#     part_sum[i+1] = s

for i in range(1, n+1):
    part_sum[i] = part_sum[i-1] + num_li[i-1]


print(num_li, part_sum)

for _ in range(m):
    i, j = map(int, input().split())

    print(part_sum[j] - part_sum[i-1])