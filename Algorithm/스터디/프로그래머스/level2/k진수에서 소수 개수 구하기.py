# k진수에서 소수 개수 구하기

# (1)
def solution(n, k):
    num = ''
    while n:
        num = str(n%k) + num
        n = n // k
    num = num.split('0')
    
    result = 0
    for i in num:
        if len(i) == 0 or int(i) == 1:
            continue
        
        for j in range(2, int(int(i)**0.5)+1):
            if int(i) % j == 0:
                break
        else:
            result += 1
            
    return result

# (2) 실패, 런타임에러
import math
def is_prime_num(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False

    return True

def trans_to_k(n, k):
    i = ''
    while n > k:
        i += str(n % k)
        n = n // k
    if n != 0:
        i += str(n)
    i = i[::-1]
    i = i.split('0')
    if '' in i:
        i.remove('')
    
    return i 

def solution(n, k):
    answer = 0
    number = range(2, 10001)
                   
    sosu_list = []
    for i in number:
        if is_prime_num(i):
            sosu_list.append(i)
            
    for j in trans_to_k(n, k):
        if int(j) in sosu_list:
            answer += 1
        
        
    return answer