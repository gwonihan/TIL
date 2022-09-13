#나는야 포켓몬 어쩌구
import sys
input = sys.stdin.readline

M,N = map(int,input().split())

poketmon_num = {}
poketmon_name = {}
for i in range(1,M+1):
    poketmon = input().strip()
    poketmon_num[i] = poketmon
    poketmon_name[poketmon] = i


for i in range(N):
    answer = input().strip()

    if answer.isdigit():
        print(poketmon_num[int(answer)])
    else:
        print(poketmon_name[answer])
        




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