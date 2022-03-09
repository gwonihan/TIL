# 다시 풀기

# 개미집 만들기
ant = []
for i in range(10):
    ant.append(list(map(int, input().split())))

# 시작점
x, y = 1, 1

# 오른쪽, 아래 이동
while ant[x][y] != 2:
    if ant[x][y] == 0:
        ant[x][y] = 9
        y += 1
    else:
        x += 1
        y -= 1

# 2인 먹이를 9로 할당
ant[x][y] = 9

# 개미집 출력
for i in range(10):
    for j in range(10):
        print(ant[i][j], end=" ")
    print()