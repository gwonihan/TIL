# 패션왕 신해빈
import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    ans = 1
    passion = {}
    for _ in range(int(input())):
        c, e = input().split()
        if e not in passion:
            passion[e] = 1
        else:
            passion[e] += 1

    for e in passion:
        ans *= passion[e] + 1
    
    print(ans - 1)