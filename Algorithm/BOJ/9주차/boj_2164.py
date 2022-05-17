# 카드2
from collections import deque
N = int(input())

d = deque()

for i in range(1,N+1):
    d.append(i)

while len(d) != 1:
    # 맨 앞의 카드 삭제
    d.popleft()

    # 두 번째 카드 맨 뒤로 보내기
    x = d.popleft()
    d.append(x)

print(d[0])


# card_list = list(range(1,int(input())+1))

# while True:
    
#     if len(card_list) > 1:
#         card_list = card_list[1:]
#         card = card_list[0]
#         card_list = card_list[1:]
#         card_list.append(card)
    
#     else:
#         print(card_list[0])
#         break
