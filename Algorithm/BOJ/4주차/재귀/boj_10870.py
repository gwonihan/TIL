# 피보나치 수5
n = int(input())

pipo = [0,1]

for i in range(n):
    pipo.append(pipo[0+i]+pipo[1+i])

print(pipo[n])
