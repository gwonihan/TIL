#나는야 포켓몬 어쩌구
import sys
M,N = map(int,sys.stdin.readline().split())

poketmon = {}
for i in range(1,M+1):
    poketmon[i] = sys.stdin.readline()

covert_po = {v:k for k,v in poketmon.items()}


for i in range(N):
    answer = sys.stdin.readline()

    if answer.isdigit():
        print(poketmon[int(answer)])
    else:
        print(covert_po[answer])
        




# 시간초과
# M,N = map(int,sys.stdin.readline().split())

# poketmon = []

# for _ in range(M):
#     poketmon.append(sys.stdin.readline())


# for i in range(N):
#     answer = sys.stdin.readline()

#     try:
#         print((poketmon.index(answer))+1)
#     except:
#         print(poketmon[int(answer)-1])