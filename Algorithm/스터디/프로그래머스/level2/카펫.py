#카펫
def solution(brown, yellow):
    answer = []
    total = brown + yellow                  # a * b = total
    for b in range(1,total+1):
        if (total / b) % 1 == 0:            # total / b = a
            a = total / b
            if a >= b:                      # a >= b
                if 2*a + 2*b == brown + 4:  # 2*a + 2*b = brown + 4 
                    return [a,b]
            
    return answer


# 코드실행은 됬으나 실패
def solution(brown, yellow):
    answer = []
    
    import math
    total_grid = brown + yellow
    root = total_grid ** (1/2)
    
    width = math.ceil(root)
    vertical = math.floor(root)
    
    for i in range(width, total_grid+1):
        if len(answer) == 0:
            for j in range(vertical+1, 0,-1):
                if i * j == total_grid:
                    answer.append(i)
                    answer.append(j)
                    break
        else:
            break
    return answer