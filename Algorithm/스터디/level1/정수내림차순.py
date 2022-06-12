# 정수 내림차순으로 배치하기

def solution(n):
    li = list(str(n))
    li.sort(reverse=True)
    answer = ''.join(map(str,li))
    return int(answer)