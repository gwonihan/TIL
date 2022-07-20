# N과 M

N, M = map(int,input().split())

seq = []

def dfs():
    if len(seq) == M:
        print(" ".join(map(str,seq)))
        return
    
    for i in range(1, N+1):
        if i not in seq:
            seq.append(i)
            dfs()
            seq.pop()

        

