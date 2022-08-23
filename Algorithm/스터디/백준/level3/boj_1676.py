# 팩토리얼 0의 개수
N = int(input())
facto = 1
for i in range(1,N+1):
    facto *= i

zero = 0
for i in str(facto)[::-1]:
    if i == '0':
        zero += 1
    else:
        break

print(zero)
