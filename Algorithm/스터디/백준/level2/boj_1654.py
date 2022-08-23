# 랜선자르기
import sys
K, N = map(int,sys.stdin.readline().split())
line = []

for _ in range(K):
    line.append(int(sys.stdin.readline()))
line.sort()

start = 1
end = max(line)

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for i in range(K):
        cnt += line[i] // mid

    if cnt >= N:
        start = mid + 1
        print(start)
    else:
        end = mid -1
        print(end)

print(end)


# 시간초과
# first_li = line[0]
# cnt = 0
# while N != cnt:
    
#     for i in line:

#         while i >= first_li:
#             i = i - first_li
#             cnt += 1
                
#     if N > cnt:
#         first_li -= 1
#         cnt = 0

# print(first_li)