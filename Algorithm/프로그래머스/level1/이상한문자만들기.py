# 이상한 문자 만들기
def solution(s):
    word_li = list(s.split(' '))
    
    cng = ""
    for word in word_li:
        for s in range(len(word)):
            if s % 2 == 0:
                cng += word[s].upper()
            else:
                cng += word[s].lower()
        cng += ' '
    
    return cng[0:-1]
