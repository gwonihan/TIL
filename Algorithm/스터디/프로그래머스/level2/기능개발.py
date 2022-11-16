# 기능개발 ( 이게 왜풀리노 )

def solution(progresses, speeds):
    answer = []
    cnt = 0
    
    while progresses:
        for i in range(len(speeds)):
            progresses[i] += speeds[i]
        
        for i in progresses:
            if i >= 100:
                cnt += 1
                
            else:
                break
    
        if cnt > 0:
            answer.append(cnt)
            for i in range(cnt):
                progresses.pop(0)
                speeds.pop(0)
            cnt = 0

    return answer