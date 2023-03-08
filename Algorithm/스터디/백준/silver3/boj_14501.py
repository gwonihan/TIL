# 퇴사
import sys
n = int(input())

schedule = [list(map(int, input().split())) for i in range(n)]
dp = [0 for i in range(n+1)]

for i in range(n):
    for j in range(i+schedule[i][0], n+1):
        if dp[j] < dp[i] + schedule[i][1]:
            dp[j] = dp[i] + schedule[i][1]

print(dp[-1])



# 1
# n = int(input())
# schedule = [[]]
# for _ in range(n):
#     schedule.append(list(map(int, input().split())))

# print(schedule)

# pay_list = []
# i = 1
# pay = 0
# day = i

# while i <= n:
#     if schedule[i][0] + day <= n+1:
#         pay += schedule[day][1]
#         day += schedule[day][0]
#     else:
#         pay_list.append(pay)
#         i += 1
#         day = i
#         pay = 0

# print(pay_list)
# print(max(pay_list))