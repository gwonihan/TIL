# 퇴사
import sys
input = sys.stdin.readline

n = int(input())
schedule = [[]]
for _ in range(n):
    schedule.append(list(map(int, input().split())))

print(schedule)

pay_list = []
i = 1
pay = 0
day = i

while i <= n:
    if schedule[i][0] + day <= n+1:
        pay += schedule[day][1]
        day += schedule[day][0]
    else:
        pay_list.append(pay)
        i += 1
        day = i
        pay = 0

print(pay_list)
print(max(pay_list))

