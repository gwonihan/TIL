# DFS와 BFS
N, M, V = map(int,input().split())

graph =[[0]*(N+1) for _ in range(N+1)]
visited = [False] * (N+1)


for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

def dfs(V):
    visited[V] = True
    print(V, end=" ")
    for i in range(1, N+1):
        if not visited[i] and graph[V][i] == 1:
            dfs(i)

def bfs(V):
    visited[V] = False
    queue = [V]
    
    while queue:
        V = queue.pop(0)
        print(V, end=' ')
        for i in range(1, N+1):
            if visited[i] and graph[V][i] == 1:
                queue.append(i)
                visited[i] = False

dfs(V)
print()
bfs(V)
    