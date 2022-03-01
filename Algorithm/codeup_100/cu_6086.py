# 뭐임..

n = int(input())
s = 0

for i in range(1,n):
    s += i
    if s >= n:
        break
print(s)