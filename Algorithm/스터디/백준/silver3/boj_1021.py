# 회전하는 큐
import sys
from collections import deque
input = sys.stdin.readline

ans = 0
N, M = map(int, input().split())
deq = deque(range(1, N+1))
p = deque(map(int,input().split()))

for i in p:
    while True:
        if deq[0] == i:
            deq.popleft()
            break
        else:
            if deq.index(i) < len(deq) / 2:
                while deq[0] != i:
                    deq.append(deq.popleft())
                    ans += 1
            else:
                while deq[0] != i:
                    deq.appendleft(deq.pop())
                    ans += 1

print(ans)