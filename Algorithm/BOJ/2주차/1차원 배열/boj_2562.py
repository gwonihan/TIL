li = []
for _ in range(9):
    n = int(input())
    li.append(n)
m = max(li)
print(m, int(li.index(m))+1)