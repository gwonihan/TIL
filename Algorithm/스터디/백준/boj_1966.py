# 프린터 큐
import sys

case = int(sys.stdin.readline())

for _ in range(case):
    n, m = map(int,sys.stdin.readline().split())
    imp = list(map(int, sys.stdin.readline().split()))
    idx = list(range(len(imp)))
    idx[m] = 'target'

    # 순서
    order = 0

    while True:
        if imp[0] == max(imp):
            order += 1

            if idx[0]=='target':
                print(order)
                break
            else:
                imp.pop(0)
                idx.pop(0)
        
        else:
            imp.append(imp.pop(0))
            idx.append(idx.pop(0))
           