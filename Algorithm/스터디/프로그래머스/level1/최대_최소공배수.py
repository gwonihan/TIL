# 유클리드 호제법

def solution(n, m):
    c, d = max(n,m), min(n,m)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(n*m/c)]

    return answer

