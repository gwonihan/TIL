# 시저 암호 (못품)
def solution(s, n):
    ord_list = []
    for alpa in list(s):
        ans = ord(alpa) - 64
        ans += n
        c = chr(ans)
        ord_list.append(c)
        
    answer = ord_list
    return answer