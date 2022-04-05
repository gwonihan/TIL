# 골드바흐의 추측

def sosu(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i ==0:
            return False
    return True

all_list = list(range(2,100001))
res_list = []

for i in all_list:
    if sosu(i):
        res_list.append(i)

n = int(input())

for _ in range(n):
    idx = 0
    idx2 = 0
    number = int(input())

    while True:
        
        if res_list[idx] + res_list[idx2] < number:
            idx2 += 1
        elif res_list[idx] + res_list[idx2] > number:
            idx += 1
            idx2 -= 1
        elif res_list[idx] + res_list[idx2] == number:
            print(res_list[idx], res_list[idx+1])
            break