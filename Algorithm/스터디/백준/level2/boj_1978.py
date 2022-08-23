# 소수 찾기
n = input()
sosu = list(map(int,input().split()))
answer = 0
print(sosu)

for i in sosu:
    cnt = 0

    if i != 1:
        for j in range(2,i+1):
            if i % j == 0:
                cnt += 1

        if cnt == 1:
            answer += 1
    

print(answer)
