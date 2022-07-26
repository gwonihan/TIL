import sys
K = int(sys.stdin.readline())
pay = []

for _ in range(K):
    money = int(sys.stdin.readline())
    if money != 0:
        pay.append(money)
    else:
        pay.pop()

print(sum(pay)) 