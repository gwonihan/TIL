# 나는 요리사다

for _ in range(5) :
    sum_value =[sum(map(int, input().split()))]

print(sum_value.index(max(sum_value))+1, max(sum_value))