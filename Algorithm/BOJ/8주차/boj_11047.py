# 동전
N, K = map(int,input().split())

coin_list = []
for _ in range(N):
    coin_list.append(int(input()))
coin_list.reverse()

cnt = 0
for coin in coin_list:
    if K >= coin:
        cnt += K // coin
        K = K % coin

        if K <= 0:
            break

print(cnt)

# i = 0
# coin = 0
# coin_list.reverse()

# while True:

#     if K - coin_list[i] < 0:
#         i += 1
    
#     elif K - coin_list[i] > 0:
#         K = K - coin_list[i]
#         coin += 1
    
#     else:
#         coin += 1
#         print(coin)
#         break

 

