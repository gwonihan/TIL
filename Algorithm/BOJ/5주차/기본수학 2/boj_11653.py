# 소인수 분해
n = int(input())
i = 2
while True:
    if n % i ==0:
        n = n // i
        print(i)
    elif n ==1:
        break
    else:
        i += 1