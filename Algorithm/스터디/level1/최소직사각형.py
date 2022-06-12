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