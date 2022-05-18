#통계학
import statistics

n = int(input())
num_li = []
for _ in range(n):
    num_li.append(int(input()))

# 산술 평균
print(round(sum(num_li)/len(num_li)))

# 중앙값
print(num_li[len(num_li)/2])

#최빈값 ???
print(statistics.mode(num_li))

# 범위
print(max(num_li)-min(num_li))