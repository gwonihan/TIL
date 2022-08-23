# 요세푸스 문제 0
import sys
N,K = map(int,sys.stdin.readline().split())
answer = []

li = list(range(1,N+1))

while True:
    for _ in range(K-1):
        a = li.pop(0)
        li.append(a)
    
    
    answer.append(li.pop(0))

    if len(answer) == N:
      break

print("<", end="")
for i in answer[:-1]:
    print(i, end=", ")
print(answer[-1], end="")
print(">", end="")