# 최대공약수와 최소공배수
n,m = map(int,input().split())

# 유클리드호제법
def gcd(n,m):
    if m == 0:
        return n
    return gcd(m, n%m)

print(gcd(n,m), n*m//gcd(n,m))















# #최대공약수
# GCD = 1
# #최소공배수
# LCM = 1

# #나눌 수
# div = 2

# while True:
#     if n % div == 0 and m % div == 0:
#         LCM *= div

#     elif n % div != 0 or m % div != 0:
#         div += 1
    
#     elif div >= n or div >= m:
#         break

# print(LCM, GCD)
    
