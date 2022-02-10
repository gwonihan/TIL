# 나는 요리사다

sum_value =[sum(map(int, input().split())) for _ in range(5)]
print(sum_value.index(max(sum_value))+1, max(sum_value))