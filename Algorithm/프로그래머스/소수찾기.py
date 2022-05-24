# 소수 찾기
def solution(n):
    sosu = 0
    for i in range(2,n+1):
        for j in range(2, int(i**1/2)+1):
            if i % j == 0:
                break
        else:
            sosu += 1
    
    return sosu