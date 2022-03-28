# 블랙잭
N,M = map(int,input().split())
card_set =list(map(int,input().split()))
b = len(card_set)
max_sum = 0

for i in range(0, b-2):
    for j in range(i+1, b-1):
        for k in range(j+1, b):
            if card_set[i] + card_set[j] + card_set[k] > M:
                continue
            else:
                max_sum = max(max_sum,card_set[i] + card_set[j] + card_set[k])

print(max_sum)