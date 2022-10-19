import sys
# 구간 합 구하기 4
n,m = map(int,sys.stdin.readline().split())
n_arr = list(map(int,sys.stdin.readline().split()))
# [5, 4, 3, 2, 1]

sum_arr = [0 for _ in range(n+1)]


for i in range(1, n+1):
    sum_arr[i] = sum_arr[i-1] + n_arr[i-1]


for _ in range(m):
    first, end = map(int, sys.stdin.readline().split())
    print(sum_arr[end]-sum_arr[first-1])

   

