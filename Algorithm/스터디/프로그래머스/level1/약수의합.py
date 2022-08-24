# 약수의 합
def solution(n):
    divisor = 0
    for i in range(1,n+1):
        if n % i == 0:
            divisor += i
    return divisor

# 약수를 구할 때, 숫자의 절반만 계산해도 된다!