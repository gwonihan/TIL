# 문자열 내 p와 y의 개수
def solution(s):
    cnt_p = 0
    cnt_y = 0
    
    for i in s:
        if i == 'p' or i == 'P':
            cnt_p += 1
        elif i == 'y' or i == 'Y':
            cnt_y += 1
        else:
            pass
    if cnt_p == cnt_y:
        return True
    else:
        return False

def numPY(s):
    return s.lower().count('p') == s.lower().count('y')