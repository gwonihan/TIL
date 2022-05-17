arr = list(map(int,input().split()))
s = 0

for i in arr:
    s += i

print(s / len(arr))
