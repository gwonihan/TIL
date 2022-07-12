# 로또의 최고 순위와 최저 순위
# 천재의 풀이
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)    # lottos 안의 0의 개수를 반환
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
            
    return rank[cnt_0 + ans],rank[ans]

# 개가튼풀이
def solution(lottos, win_nums):
    answer = []
    zero_li = []
    c = []
    
    for i in lottos:
        if i == 0:
            zero_li.append(i)
        
        if i in win_nums:
            c.append(i)
    
    max_rank = len(c) + len(zero_li)
    min_rank = len(c)
    
    if max_rank == 6:
        answer.append(1)
    elif max_rank == 5:
        answer.append(2)
    elif max_rank == 4:
        answer.append(3)
    elif max_rank == 3:
        answer.append(4)
    elif max_rank == 2:
        answer.append(5)
    else:
        answer.append(6)
    
    if min_rank == 6:
        answer.append(1)
    elif min_rank == 5:
        answer.append(2)
    elif min_rank == 4:
        answer.append(3)
    elif min_rank == 3:
        answer.append(4)
    elif min_rank == 2:
        answer.append(5)
    else:
        answer.append(6)
    
        
    return answer