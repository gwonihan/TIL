# 영화감독 숌
# 10666 11666 12666 13666 14666 15666 16661 16662
# 16663 16664 16665 16666 17666 18666 19666
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18

n = int(input())

cnt = 0
num = 1
while True:
    if "666" in str(num):
        cnt = cnt+1

    if cnt == n:
        print(num)
        break

    num = num+1

