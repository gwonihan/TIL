# 좌표 정렬하기
N = int(input())

po = []

for _ in range(N):
    po.append(list(map(int,input().split())))

po.sort(key=lambda x: (x[0], x[1]))
# po.sort(key=lambda x: int(x[0]))

for i in po:
    print(*i)