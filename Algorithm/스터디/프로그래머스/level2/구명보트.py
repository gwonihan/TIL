#구명보트

#이 문제처럼 최소의 숫자를 구하려면, 가장 작은 숫자 + 가장 큰 숫자
from collections import deque

def solution(people, limit):
    boat = 0
    people = sorted(people)
    
    # deque로 구성
    q = deque(people)
    
    while q:
        # deque에 최소 2명이상이 남아있을 때
        if len(q) >= 2:

            # 가장 무거운 사람 + 가장 가벼운 사람
            if q[0] + q[-1] <= limit:
                q.pop()
                q.popleft()
                boat += 1
            elif q[0] + q[-1] > limit:
                q.pop()
                boat += 1
        else:
            q.pop()
            boat += 1
    
    return boat