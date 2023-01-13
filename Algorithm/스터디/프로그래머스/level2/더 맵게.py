# 더 맵게
from heapq import heappush, heappop, heapify

def solution(scoville, K):
    answer = 0
    heapify(scoville)
        
    while scoville[0] < K:
        
        dish = heappop(scoville)
        dish2 = heappop(scoville)
        new_dish = dish + (dish2 * 2)
        heappush(scoville, new_dish)
        answer += 1
        
        if len(scoville) < 2:
            break
    
    if scoville[0] >= K:
        return answer
    else:
        return -1