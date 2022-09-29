# 영어끝말잇기
def solution(n, words):
    answer = []
    # 끝말 잇기 단어 리스트
    c_word = []
    c_word.append(words[0])
    
    for i in range(len(words)-1):
        # 다음에 나올 단어가 c_word 에 없다면
        if words[i+1] not in c_word:
            
            if words[i][-1] != words[i+1][0]:
                # 사람 순서, 회차
                answer = [(i+1)%n+1,(i+1)//n+1]
                break
            else:
                c_word.append(words[i+1])
        else:
            answer = [(i+1)%n+1,(i+1)//n+1]
            break
    else:
        answer = [0,0]     
    return answer