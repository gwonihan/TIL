#수 정렬하기

n = int(input())
numbers = [int(input()) for _ in range(n)]

sorted_numbers = sorted(numbers)
print(*sorted_numbers, sep="\n")

# 한줄로 리팩토링 가능하다!
# print(sorted([int(input()) for _ in range(int(input()))]), sep="\n")