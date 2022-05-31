# 문자열 다루기 기본
def solution(s):
    try:
        int(s)
        i = 0
    except:
        i = 1
    
    if i == 0 and len(s) == 4 or len(s) == 6:
        answer = True
    else:
        answer = False
    return answer

# def alpha_string(s):
#     return s.isdigit() and len(s) in (4,6)