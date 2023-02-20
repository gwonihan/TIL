def filters(skill, skills):
    s = ''
    for i in skills:
        if i in skill:
            s += i
    
    return s

def solution(skill, skill_trees):
    answer = 0
    
    for i in skill_trees:
        c = filters(skill, i)
        
        if skill[:len(c)] == c:
            answer += 1
        
    return answer