# N과 M (2)
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

t = []
def dfs(start):
    
    if len(t) == m:
        print(*t)
        return
    
    for i in range(start, n+1):
        if i not in t:
            t.append(i)
            dfs(i+1)
            t.pop()

dfs(1)