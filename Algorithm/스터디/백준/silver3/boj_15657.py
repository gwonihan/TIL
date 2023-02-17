# N과 M(8)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
seq = list(map(int, input().split()))
seq.sort()

t = []

def dfs(start):
    if len(t) == m:
        print(*t)
        return
    
    for i in range(start, len(seq)):
        t.append(seq[i])
        dfs(i)
        t.pop()
   
dfs(0)