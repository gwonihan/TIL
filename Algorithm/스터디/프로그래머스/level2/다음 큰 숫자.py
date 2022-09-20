# 주어진 숫자를 2진수로 변환한 후, 숫자 1 개수 세기
def ezin_one(s):
    to_ezin = ''
    
    while s != 0:
        to_ezin += str(s%2)
        s = s // 2
    
    return to_ezin.count('1')


def solution(n):
    one_count = ezin_one(n)
    
    one_count2 = 0
    while one_count != one_count2:
        n += 1
        one_count2 = ezin_one(n)
        
    answer = n
    
    return answer