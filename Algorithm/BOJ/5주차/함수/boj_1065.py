# 한수
n = int(input())
answer = []
hansu = 0

for i in range(1,n+1):
    num_list = list(map(int,str(i))) # 이렇게 한번에!
    if i < 100:
        hansu += 1
    elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
        hansu += 1

print(hansu)