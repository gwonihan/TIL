# 튜플
def solution(s):
    answer = 0
    
    n = ""
    li = []
    for i in s:
        if i.isdigit() or i==",":
            n += i
        elif i == "}":
            li.append(n)
            n = ""
    print(li)
    li2 = []
    
    for i in li:
        new = []
        n = ""
        for j in i:
            if j.isdigit():
                n += j
            elif j == ",":
                new.append(n)
                n = ""
        li2.append(new)
        
    
    print(li2)
            
    return answer