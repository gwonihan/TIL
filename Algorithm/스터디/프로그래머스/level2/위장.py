# 위장

def solution(clothes):
    answer = 1
    drawer = {}
    
    
    for i in clothes:
        key = i[1]
        value = i[0]
        
        if key in drawer:
            drawer[key].append(value)
        else:
            drawer[key] = [value]
    
    print(drawer)
    
    for key in drawer:
        answer *= len(drawer[key]) + 1
            
    # 아무것도 입지 않는 경우를 뺀다.    
    return answer -1