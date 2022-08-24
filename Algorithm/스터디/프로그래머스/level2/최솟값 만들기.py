# 최솟값 만들기

# 시간초과
def solution(A,B):
    answer = 0

    while len(A) != 0:
        a = min(A)
        A.remove(a)
        
        b = max(B)
        B.remove(b)
        
        answer += a*b

    return answer


# 참고풀이
def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse=True)
    
    for a,b in zip(A,B):
        answer += a*b

    return answer


