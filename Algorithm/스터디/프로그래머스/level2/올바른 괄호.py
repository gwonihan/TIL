# 올바른 괄호
# 시간초과
def solution(s):
    
    while "()" in s:
        s = s.replace('()', '')
    
    if len(s) == 0:
        return True
    else:
        return False

# 참고풀이
def solution(s):
    cnt = 0
    for i in s:
        if i == "(":
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0:
                break
                return false
    
    if cnt == 0:
        return True
    else:
        return False        