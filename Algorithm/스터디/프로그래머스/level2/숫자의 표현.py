def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        plus = 0
        
        while plus < n:
            plus += i
            i += 1
            
            if plus == n:
                answer += 1
                break
            
    return answer