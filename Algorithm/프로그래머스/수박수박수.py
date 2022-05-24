# 수박수박수박수박수박수?

def solution(n):
    answer = ''
    for i in range(1, n+1):
        if i % 2 != 0:
            answer += '수'
        else:
            answer += '박'
    return answer

# def water_melon(n):
#     s = "수박" * n
#     return s[:n]