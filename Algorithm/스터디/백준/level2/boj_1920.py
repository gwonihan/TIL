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


# 수 찾기
import sys


# set..을안해줘서 안됨..
N = int(sys.stdin.readline())
N_li = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
M_li = list(map(int, sys.stdin.readline().split()))

for i in range(M):
    if M_li[i] in N_li:
        print(1)
    else:
        print(0)
        

