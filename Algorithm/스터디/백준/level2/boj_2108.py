# 통계학
import sys
from collections import Counter

n = int(sys.stdin.readline())
nums = []

for i in range(n):
    nums.append(int(sys.stdin.readline()))

nums.sort()
nums_s = Counter(nums).most_common()

# 1.산술평균
print(round(sum(nums) / n))

# 2.중앙값
print(nums[n // 2])

# 3.최빈값
if len(nums_s) > 1:
    if nums_s[0][1] == nums_s[1][1]:
        print(nums_s[1][0])
    else:
        print(nums_s[0][0])
else:
    print(nums_s[0][0])

# 4.범위
print(nums[-1] - nums[0])


#최빈값(삽질)
chobin = []
for i in set(n_li):
    chobin.append([i,0])

for i in n_li:
  for j in chobin:
    if i == j[0]:
      j[1] += 1

chobin.sort(key=lambda x: (x[1], x[0]))

if chobin[0][1] == chobin[1][1]:
  print(chobin[1][0])

else:
  print(chobin[0][0])




