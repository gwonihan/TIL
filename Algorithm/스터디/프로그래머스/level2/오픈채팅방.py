def solution(record):
    answer = []
    nickname = dict()
    for r in record:
        
        if len(r.split()) == 3:
            eol, d, name = r.split()
            nickname[d] = name
        else:
            eol, d = r.split()
    
    for r in record:
        
        if len(r.split()) == 3:
            eol, d, name = r.split()
        else:
            eol, d = r.split()
        
        if eol == 'Enter':
            answer.append("{}님이 들어왔습니다.".format(nickname[d]))
        elif eol == 'Leave':
            answer.append("{}님이 나갔습니다.".format(nickname[d]))
        else:
            pass      
            
        
    return answer