# 터렛
import math
n = int(input())

for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    
    # 두 원이 동심원이고 반지름 같을 때
    if distance == 0 and r1 == r2 :
        print(-1)
    
    # 내접, 외접일 때
    elif abs(r1-r2) == distance or r1 + r2 == distance:
        print(1)
    
    # 두 원이 서로 다른 두 점에서 만날 때
    elif abs(r1-r2) < distance < abs(r1+r2):
        print(2)
    
    # 어느 경우에도 속하지 않을 때
    else:
        print(0)