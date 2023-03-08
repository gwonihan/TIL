# 주유소
import sys
input = sys.stdin.readline

n = int(input())
km = list(map(int,input().split()))
city = list(map(int,input().split()))

pay = 0
cost = city[0]

for i in range(n-1):
    if city[i] < cost:
        cost = city[i]
    pay += cost * km[i]

print(pay)



# city.pop()

# cost = 0
# min_city = min(city)
# sum_km = sum(km)
# for i in range(n-1):
#     if sum_km != 0:
#         if city[i] == min_city:
#             cost += sum_km * city[i]
#             sum_km = 0
#         else:
#             cost += km[i] * city[i]
#             sum_km -= km[i]
#     else:
#         break
# # print(km)
# # print(city)
# print(cost)