# 자연수 뒤집어 배열로 만들기

def solution(n):
    re = list(map(int, str(n)))
    re.reverse()
    answer = re
    return answer


# def digit_reverse(n):
#     return list(map(int, reversed(str(n))))