# 계단 오르기
n = int(input())
stairs = []

for _ in range(n):
    stairs.append(int(input()))


total_sum = 0
i = 0
while i <= n-2:
    if i == 0 or i == n:
        total_sum += stairs[i]
        
    
    if stairs[i+1] < stairs[i+2]:
        total_sum += stairs[i+2]
        i += 2
    else:
        total_sum += stairs[i+1]
        i += 1

print(total_sum)

    
