pass_num = 0

for _ in range(5):
    num = list(map(int, input().split()))
    avg = sum(num) / len(num)
    
    if avg >= 80:
        print('pass')
        pass_num +=1
    else:
        print('fail')
print("Successful:",pass_num)
    
#강사님풀이
score = [list(map(int, input().split())) for _ in range(5)]
success = 0

for i in range(5):
    total = 0
    for j in range(4):
        total += score[i][j]
    average = total / 4
    if average >=80:
        success += 1
        print('pass')
    else:
        print('fail')
print(f'Successful:{success}')