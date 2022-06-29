N = int(input())
num_li = []

for _ in range(N):
    num_li.append(int(input()))

num_li.sort()
print(*num_li, sep="\n")