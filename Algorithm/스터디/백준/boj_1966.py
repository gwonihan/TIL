# 프린터 큐
import sys

case = int(sys.stdin.readline())

for _ in range(case):
    n, m = map(int,sys.stdin.readline().split())
    d = list(map(int, sys.stdin.readline().split()))

    order = 0

    li = []
    for i in range(n):
        li.append((i, d[i]))
    
    print(li) 