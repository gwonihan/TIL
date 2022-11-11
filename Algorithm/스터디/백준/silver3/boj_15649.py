# N과 M (1)
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

visit = [0] * (n+1)
t = []

def dfs(step):
    if step == m:
        print(*t)
        return
    
    for i in range(1, n+1):
        if not visit[i]:
            visit[i] = 1
            t.append(i)
            
            dfs(step+1)
            visit[i] = 0
            t.pop()

dfs(0)