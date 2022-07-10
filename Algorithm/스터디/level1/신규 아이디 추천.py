# 신규아이디 추천
def solution(new_id):
    answer = ''
    #1
    new_id = new_id.lower()
    print(new_id)
    
    #2 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)
    # for i in new_id:
    #   if i.isalpha() or i.isdigit() or i in ['-', '_','.']:
    #       answer += i
    li =['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','1','2','3','4','5','6','7','8','9','0', '-', '_', '.']
    for i in new_id:
        if i in li:
            answer += i
    
    
    #3 마침표(.)
    while '..' in answer:
        answer = answer.replace('..', '.')
    
    
    #4 
    if answer[0] == '.':
        if len(answer) > 1:
            answer = answer[1:]
        else:
            answer = '.'
    
    if answer[-1] == '.':
        answer = answer[:-1]
    
    
    #5
    if answer =='':
        answer += 'a'
    
    
    #6
    if len(answer) >= 16:
        answer = answer[:15]
        
        if answer[-1] == '.':
            answer = answer[:-1]
    
    
    #7
    while len(answer) < 3:
        answer += answer[-1]
    
    
    return answer