# 프린터 큐
import sys

case = int(sys.stdin.readline())

for _ in range(case):
    n, m = map(int, sys.stdin.readline().split())
    workspace = list(map(int, sys.stdin.readline().split()))

    pnt = 1
    while True:
        max_number = max(workspace)

        if workspace[m] != max_number:
            pnt += 1
            workspace.remove(max_number)
        else:
            break
    
    print(pnt)
    
