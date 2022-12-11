# 베르트랑 공준
import sys
input = sys.stdin.readline

n = int(input())

while n != 0:
    sosu = 0
    
    # n 보다 크고 2n 보다 작거나 같음
    for i in range(n+1, 2*n +1):
        
        # 1일 경우 생략
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                break
        else:
            sosu += 1
        
    print(sosu)

    n = int(input())


# # 베르트랑 공준
# import sys
# input = sys.stdin.readline

# def sosu(n):
#     if n == 1:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True

# num_list = list(range(2, 246912))
# sosu_list = []

# for i in num_list:
#     if sosu(i):
#         sosu_list.append(i)

# n = int(input())
# while n != 0:
#     cnt = 0
    
#     for i in sosu_list:
#         if n < i <= 2*n :
#             cnt += 1
    
#     print(cnt)
#     n = int(input())

