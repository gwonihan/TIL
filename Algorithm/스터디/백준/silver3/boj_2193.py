# 이친수

n = int(input())

pn = [0] * 91
pn[1] = 1
pn[2] = 1

for i in range(3, n+1):
    pn[i] = pn[i-1] + pn[i-2]


print(pn[n])