def solution(n, arr1, arr2):
    li1 = []
    li2 = []
    
    for i in arr1:
        new = ''
        for _ in range(n):
            new += str(i%2)
            i = i//2
        li1.append((new[::-1]))
    
    for i in arr2:
        new = ''
        for _ in range(n):
            new += str(i%2)
            i = i//2
        li2.append((new[::-1]))
    
    answer = []
    for i in range(n):
        new = int(li1[i]) + int(li2[i])
        answer.append(str(new))
    
    answer2 = []
    for i in answer:
        print(i)
        # new = ''
        # for j in i:
        #     if j > 0:
        #         new += "#"
        #     else:
        #         new += " "
        # answer2.append(new)
    
    print(answer2)
            
    
    return answer