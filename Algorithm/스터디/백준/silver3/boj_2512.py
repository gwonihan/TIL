# 예산
import sys
input = sys.stdin.readline

n = int(input())
budgets = list(map(int, input().split()))
m = int(input())
start, end = 0, max(budgets)

# 이분탐색
while start <= end:
    mid = (start + end) // 2
    total = 0

    for i in budgets:
        if i > mid:
            total += mid
        else:
            total += i
    
    if total <= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)