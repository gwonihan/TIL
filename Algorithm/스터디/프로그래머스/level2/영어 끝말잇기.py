# 영어끝말잇기
def solution(n, words):
    answer = []
    
    for j in range((len(words)-1)):
        if words[j][-1] != words[j+1][0]:
            answer.append(j//n)
            answer.append(j%n)
            break
   
    return answer