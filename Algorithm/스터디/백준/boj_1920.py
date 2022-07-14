# 수 찾기
import sys

N = int(sys.stdin.readline())
N_li = list(map(int, sys.stdin.readline().split()))
N_li.sort()

M = int(sys.stdin.readline())
M_li = list(map(int, sys.stdin.readline().split()))

for i in M_li:
    start = 0
    end = N-1

    while start <= end:
        mid = (start + end) // 2  # 몫
        if i == N_li[mid]:
            print(1)
            break
        elif i > N_li[mid]:
            start = mid + 1
        else:
            end = mid - 1
    else:
        print(0)
        

