n,m = input().split()

a = int(n[::-1])
b = int(m[::-1])

if a > b:
    print(a)
else:
    print(b)