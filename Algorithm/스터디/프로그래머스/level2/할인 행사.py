# 할인 행사
from collections import Counter

def solution(want, number, discount):
    answer = 0
    dic = dict()
    
    for i, j in zip(want, number):
        dic[i] = j
    
    for i in range(len(discount)):
        c = Counter(discount[i:i+10])
        
        if c == dic:
            answer += 1

    return answer