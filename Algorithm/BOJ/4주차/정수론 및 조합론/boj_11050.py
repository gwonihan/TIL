# 이항 계수 1
n,k = map(int,input().split())

ja = 1
mo = 1

if n >= k >= 0:
    for i in range(1,n+1):
        ja *= i
    
    for i in range(1,k+1):
        mo *= i
    
    for j in range(1,n-k+1):
        mo *= j

print(int(ja/mo))


# from math import factorial

# N, K = list(map(int, input().split()))

# print(factorial(N)//(factorial(K) * factorial(N-K)))