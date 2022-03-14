n = int(input())

for _ in range(n):
    li = list(input())
    score = 0
    sum_list = 0 

    for i in li:
        if i == 'O':
            score += 1
        elif i == 'X':
            score = 0
        sum_list += score
    print(sum_list)


