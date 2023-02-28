# 모든 순열
import sys
input = sys.stdin.readline

n = int(input())
t = []

def dfs():
    if len(t) == n:
        print(*t)
        return
    
    for i in range(1, n+1):
        if i not in t:
            t.append(i)
            dfs()
            t.pop()

dfs()