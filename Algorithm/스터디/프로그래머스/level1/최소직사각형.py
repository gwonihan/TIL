# 최소직사각형
def solution(sizes):
    new_sizes = []
    answer = 0
    for i in sizes:
        i.sort()
        new_sizes.append(i)
 
        
    w = []
    h = []
    
    for sizes in new_sizes:
        w.append(sizes[0])
        h.append(sizes[1])
    
    answer += max(w) * max(h)
            
    return answer

# 인정님 풀이
# def soulution(sizes):
#     w = []
#     h = []
    
#     for i in range(len(sizes)):
#         if sizes[i][0] >= sizes[i][1]:
#             w.append(sizes[i][0])
#             h.append(sizes[i][1])
        
#         else:
#             h.append(sizes[i][0])
#             w.append(sizes[i][1])
    
#     answer = max(h) * max(w)

#     return answer

# 지호님 풀이
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)