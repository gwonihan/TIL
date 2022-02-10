#하얀 칸

board = [list(input()) for i in range(8)]
total = 0

#체스판을 돌아다니면서 조건 확인 8x8
for i in range(8):
    for j in range(8):
        
        #조건 짝짝/홀홀 and F
        if i % 2 == j % 2 and board[i][j] == 'F':
            total += 1

print(total)

#위의 코드를 한줄로 작성할 수도 있음
# print(sum(input()[i % 2 :: 2].count('F') for i in range(8)))

