# 런타임 에러
def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        li = []
        for j in range(len(arr2[0])):
            num = 0
            for k in range(len(arr1[0])):
                num += arr1[i][k] * arr2[k][j]
            li.append(num)
        answer.append(li)
    
    return answer