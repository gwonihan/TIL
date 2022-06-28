# 달팽이는 올라가고 싶다
A, B, V = map(int,input().split())
up = 2
day = 1

while True:
    day += 1
    up += A

    if up <= V:
        up -= B

    else:
        break

print(day)