# 정수 제곱근 판별
def solution(n):
    loot = n ** (1/2)
    a = round(loot)
    if loot == a:
        answer = (loot+1) ** 2
    else:
        answer = -1
        
    return answer

