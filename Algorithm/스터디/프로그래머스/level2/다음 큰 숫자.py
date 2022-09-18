def solution(n):
    answer = 0
    
    # 숫자를 하나씩 증가시키기 위한 변수
    number = n
    
    # 최초의 n을 2진수로 변환한 후, 숫자 1 개수 세기
    ezin = ''
    while n != 0:
        ezin += str(n%2)
        n = n // 2
    
    one_count = ezin.count("1")
    one_count2 = 0
    
    # number를 1씩 증가시키면서 1의 갯수 확인
    while True:
        number += 1
        n = number
        ezin2 = ''
        while n != 0:
            ezin2 += str(n%2)
            n = n // 2
        
        one_count2 = ezin2.count("1")
        
        # 최초의 1의 개수와 숫자를 1씩 더해가며 만든 수의 1의 개수가 같을 경우 while문 종료
        if one_count == one_count2:
            break
    
    answer += number
    
    return answer