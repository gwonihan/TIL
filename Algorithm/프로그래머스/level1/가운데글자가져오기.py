def solution(s):
    answer = ''
    if len(s) % 2 == 0:
        a = len(s) // 2
        answer += s[a-1]
        answer += s[a]
    else:
        b = len(s) // 2
        answer += s[b]
    return answer
