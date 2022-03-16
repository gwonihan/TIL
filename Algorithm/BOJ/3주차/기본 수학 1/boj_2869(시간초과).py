# 시간초과해결?

A,B,V = map(int,input().split())
day = 1
C = A

while True:
    if V > C:
        C -= B
        C += A
        day += 1
    else:
        print(day)
        break