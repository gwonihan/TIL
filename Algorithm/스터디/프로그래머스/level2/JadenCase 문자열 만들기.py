# JadenCase 문자열 만들기

def solution(s):
    answer = ''
    a = s.title()
    
    cnt = 0
    
    while True:
        if a[cnt].isdigit() == True:
            answer += a[cnt]
            answer += a[cnt+1].lower()
            cnt += 2
            
        else:
            answer += a[cnt]
            cnt += 1 
        
        if cnt == len(a):
            break
            
            
    return answer