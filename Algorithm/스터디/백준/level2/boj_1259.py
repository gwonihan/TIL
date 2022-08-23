# 팰린드롬수
N = int(input())

while N != 0:
    if N == int(str(N)[::-1]):
        print("yes")
    else: 
        print("no")
        
    N = int(input())
