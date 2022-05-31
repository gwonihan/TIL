# 문자열 내림차순으로 배치하기
def solution(s):
    answer = ''
    for alph in (sorted(s, reverse=True)):
        answer += alph

    return answer

# def solution(s):
#     return ''.join(sorted(s, reverse=True))