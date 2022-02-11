# 색종이

# 1. 도화지를 만든다.(0으로)
paper = [[0]*100 for _ in range(100)]

# 2. 색종이 갯수받기
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            # 도화지가 빈칸이라면
            paper[i][j] = 1 #색칠

# 영역의 넓이 구하기(도화지에서 1인 부분 더하기)
total = 0
for i in range(100):
    for j in range(100):
        total += paper[i][j]

print(total)          
