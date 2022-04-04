# 베르트랑 공준
import math

while True:
    n = int(input())
    if n == 0:
        break

    cnt = 0

    for i in range(n+1,2*n+1):
        if i != 1:  
            for j in range(2, int(math.sqrt(i))+1):
                if i % j ==0:
                    break
            else:
                cnt += 1    
    print(cnt)
                    
        
        