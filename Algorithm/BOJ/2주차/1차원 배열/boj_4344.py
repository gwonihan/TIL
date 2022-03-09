n = int(input())

for _ in range(n):
    numbers = list(map(int, input().split()))
    avg_nums = sum(numbers[1:])/numbers[0]
    up_nums = 0
    for score in numbers[1:]:
        if score > avg_nums:
            up_nums += 1
    
    rate = up_nums/numbers[0] * 100
    print(f'{rate:.3f}%')
