# 팩토리얼
number = int(input())
n = 1

if number != 0:
    for i in range(1,number+1):
        n *= i
    print(n)
else:
    print(1)