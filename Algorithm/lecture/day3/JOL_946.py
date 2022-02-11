n = int(input())
dic = {}
for _ in range(n):
    country, capital  = input().split()
    dic[country] = capital

c = input()

print(dic.get(c, "Unknown Country"))
