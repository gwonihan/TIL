def solution(s):
    answer = []
    zero = 0
    r = 0
    length = 0
    
    while len(s) != 1:
        for i in s:
            if i == 0:
                zero += 1
            else:
                length += 1
        
        new = ''
        while length != 0:
            new += str(length%2)
            length = length // 2
        
        r += 1
        s = new
    
    answer.append(r)
    answer.append(zero)
      
    return answer