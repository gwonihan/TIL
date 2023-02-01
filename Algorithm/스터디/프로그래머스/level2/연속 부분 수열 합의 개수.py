# 연속 부분 수열 합의 개수
def solution(elements):
    answer = []
    length = len(elements)
    elements = elements * 2
    c = 1
    
    while c <= length:
        for i in range(len(elements)):
            if len(elements[i:i+c]) == c:
                answer.append(sum((elements[i:i+c])))
        
        c += 1
    answer = set(answer)
        
    return len(answer)