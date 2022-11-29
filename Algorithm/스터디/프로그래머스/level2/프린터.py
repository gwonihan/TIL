# 프린터
def solution(priorities, location):
    answer = 0
    que = [ i for i in enumerate(priorities)]
    
    while True:
        num = que.pop(0)
        
        if any(num[1] < q[1] for q in que):
            que.append(num)
        else:
            answer += 1
            if num[0] == location:
                return answer