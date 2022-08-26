#나는야 포켓몬 어쩌구
import sys
M,N = map(int,sys.stdin.readline().split())

poketmon = []

for _ in range(M):
    poketmon.append(sys.stdin.readline())


for i in range(N):
    answer = sys.stdin.readline()

    try:
        print((poketmon.index(answer))+1)
    except:
        print(poketmon[int(answer)-1])