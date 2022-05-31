# 서울에서 김서방 찾기
def solution(seoul):
    p = seoul.index("Kim")
    answer = '김서방은 ' + str(p) +'에 있다'
    return answer

def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))