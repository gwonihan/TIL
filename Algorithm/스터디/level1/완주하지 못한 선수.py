#완주하지 못한 선수

# 1번째 풀이(시간초과)
def solution(participant, completion):
    answer = ''
    
    for i in participant:
        if i in completion:
            completion.remove(i)
        else:
            answer += i
    return answer

# 2번째 참고 풀이
def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    
    for p, c in zip (participant, completion):
        if p != c:
            print(p)
            return p
    print(participant)
    
    return participant[-1]

# 3번째 참고 풀이

import collections

def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    result = collections.Counter(participant) - collections.Counter(completion)
 
    return list(result)[0]