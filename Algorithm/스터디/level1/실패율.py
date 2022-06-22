# 실패율
def solution(N, stages):
    user = len(stages)
    result = []
    ans = []
    
    for i in range(1, N+1):
        people = stages.count(i)
        if people == 0:
            result.append((0, i))
            continue
        fail = people / user
        result.append((fail,i))
        user -= people
    result.sort(key =lambda x:(-x[0], x[1]))
    
    for i in range(N):
        a,b = result[i]
        ans.append(b)
    return ans