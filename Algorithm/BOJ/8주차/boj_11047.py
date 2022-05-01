# 동전
N, K = map(int,input().split())

coin_list = []
for _ in range(N):
    coin_list.append(int(input()))

coin_list.reverse()

while True:
    i = 0
    if K - coin_list[i] < 0:
        i += 1
    
    elif K - coin_list[i] > 0:
        i = i
    
    else:
        print(i)

# print(coin_list)

