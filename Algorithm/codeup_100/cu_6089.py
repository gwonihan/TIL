a,d,n = map(int, input().split())
s = a

for _ in range(1,n):
    s *= d
    
print(s)