# N과 M (1)
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

t = []

def dfs():
    if len(t) == m:
        print(*t)
        return
    
    for i in range(1, n+1):
        if i not in t:
            t.append(i)
            dfs()
            t.pop()

dfs()