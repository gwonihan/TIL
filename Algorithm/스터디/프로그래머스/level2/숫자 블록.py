def solution(begin, end):

    answer = []
    MAX = 10000000

    for num in range(begin, end + 1):

        if num == 1:
            answer.append(0)
            continue
        
        else:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    if num // i >= MAX:
                        pass
                    else:
                        answer.append(num//i)
                        break
            
            else:
                answer.append(1)
    return answer