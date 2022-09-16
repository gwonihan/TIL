def solution(s):
    answer = []
    
    # zero : 0의 갯수, r : 회차, length : 2진변환할 수
    zero = 0
    r = 0
    length = 0
    
    # 최초로 주어진 s가 1이 될 때까지 반복하는 while문
    while len(s) != 1:
        for i in s:
            if int(i) == 0:
                zero += 1
            else:
                length += 1
        
        # 0 제거 후 s의 길이를 이진 변환하는 while문
        new = ''
        while True:
            new += str(length%2)
            length = length // 2
            
            if length == 0:
                break
        
        # 회차 카운트와 이진변환 완료된 new를 s에 할당 
        r += 1
        s = str(new)[::-1]
    
    # 모든 while문이 종료되면, r(회차) 와 zero(0의 개수)를 answer에 append
    answer.append(r)
    answer.append(zero)
      
    return answer