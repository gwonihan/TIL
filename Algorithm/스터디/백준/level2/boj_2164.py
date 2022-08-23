# 카드2
from collections import deque
N = int(input())


deq = deque()
for i in range(1,N+1):
    deq.append(i)

while len(deq) != 1:
    # 맨 앞 카드 삭제
    deq.popleft()

    # 두 번째 카드 맨 뒤로 보내기
    a = deq.popleft()
    deq.append(a)


print(*deq)