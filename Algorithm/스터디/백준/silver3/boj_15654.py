# N과 M (5)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
n_li = list(map(int, input().split()))
n_li.sort()
# print(n_li)

t = []
def dfs():
    
    if len(t) == m:
        print(*t)
        return
    
    for i in n_li:
        if i not in t:
            t.append(i)
            dfs()
            t.pop()

dfs()