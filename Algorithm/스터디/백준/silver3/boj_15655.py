# N과 M(6)
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
seq = list(map(int, input().split()))
seq.sort()
t = []

def dfs(start):
    if len(t) == M:
        print(*t)
        return
    
    for i in range(start, len(seq)):
        if seq[i] not in t:
            t.append(seq[i])
            dfs(start)
            t.pop()
        start +=1
dfs(0)
    