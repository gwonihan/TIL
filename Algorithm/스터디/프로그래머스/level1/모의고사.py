def solution(answers):
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt1, cnt2, cnt3 = 0, 0, 0
    
    for i in range(len(answers)):
        s1 = i % 5
        s2 = i % 8
        s3 = i % 10
        
        if supo1[s1] == answers[i]:
            cnt1 += 1
        if supo2[s2] == answers[i]:
            cnt2 += 1
        if supo3[s3] == answers[i]:
            cnt3 += 1
    
    k = max(cnt1,cnt2,cnt3)
    answer = []
    
    if k == cnt1:
        answer.append(1)
    if k == cnt2:
        answer.append(2)
    if k == cnt3:
        answer.append(3)
        
    return answer