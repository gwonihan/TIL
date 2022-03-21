# 수 정렬하기
n = int(input())
num_list = []
for _ in range(n):
    number = int(input())
    num_list.append(number)

num_list.sort()

for i in num_list:
    print(i)