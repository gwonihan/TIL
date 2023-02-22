# 방문 길이
# 오답
def solution(dirs):
    answer = 0
    li_2 = [[0 for i in range(11)] for i in range(11)]
    x, y = 5, 5
    li_2[x][y] = 1
    
    for i in dirs:
        if i == 'U':
            x -= 1
            if x < 0:
                x += 1
            else:
                li_2[x][y] += 1

        elif i == 'L':
            y -= 1
            if y < 0:
                y += 1
            else:
                li_2[x][y] += 1  

        elif i == 'R':
            y += 1
            if y > 9:
                y -= 1
            else:
                li_2[x][y] += 1

        elif i == 'D':
            x += 1
            if x > 9:
                x -= 1
            else:
                li_2[x][y] += 1

        
    for i in li_2:
        for j in i:
            if j == 1:
                answer += 1
    
    
    return answer


# 2
def solution(dirs):

    visit = set()
    x, y = 0, 0
    
    for d in dirs:
        if d == 'U' and y < 5:
            visit.add(((x, y), (x, y+1)))
            y += 1
        
        elif d == 'D' and y > -5:
            visit.add(((x, y-1), (x, y)))
            y -= 1
        
        elif d == 'R' and x < 5:
            visit.add(((x, y), (x+1, y)))
            x += 1
            
        elif d == 'L' and x > -5:
            visit.add(((x-1,y), (x, y)))
            x -= 1

    
    return len(visit)


