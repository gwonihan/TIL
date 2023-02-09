# n진수 게임
# 재귀함수

def convert(num, base):
    temp = "0123456789ABCDEF"
    q, r = divmod(num, base)
    
    if q == 0:
        return temp[r]
    else:
        return convert(q, base) + temp[r]
    
def solution(n, t, m, p):
    answer = ''
    test = ''
    
    for i in range(m*t):
        test += str(convert(i, n))
        
    for i in range(p-1, m*t, m):
        answer += test[i]
        
    return answer