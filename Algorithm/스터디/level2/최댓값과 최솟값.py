#최댓값과 최솟값

def solution(s):
    answer = ''
    
    li = list(map(int, s.split()))
    max_num = max(li)
    min_num = min(li)
    
    answer += str(min_num)
    answer += " "
    answer += str(max_num)
    
    return answer