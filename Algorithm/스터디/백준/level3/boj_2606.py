# dfs
n=int(input())
m=int(input())

g = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    g[a].append(b); g[b].append(a)

print(g)

visit = [0]*(n+1)
def dfs(graph,s,visit):
    visit[s] = 1
    for i in graph[s]:
        if not visit[i]:
            dfs(graph,i,visit)
dfs(g,1,visit)
print(sum(visit)-1)

# 바이러스
# c = int(input())
# connect_c = int(input())

# virus = [1]
# for _ in range(connect_c):
#     v, c = map(int,input().split())

#     if v in virus:
#         if c not in virus:
#             virus.append(c)

# print(len(virus)-1)

