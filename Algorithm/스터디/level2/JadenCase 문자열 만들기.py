# JadenCase 문자열 만들기

def solution(s):
    answer = ''
    for word in list(s.split()):
        word.lower()
        if word[0].isdigit() == True:
            answer += word
            answer += " "
        else:
            word = word.capitalize()
            answer += word
            answer += " "
    
    answer = answer[:-1]
            
    return answer