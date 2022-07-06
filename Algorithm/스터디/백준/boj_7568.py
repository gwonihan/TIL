#덩치
n = int(input())
dungchi = []
answer = []

for _ in range(n):
    dungchi.append(list(map(int,input().split())))

for i in dungchi:
    ranking = 1
    for j in range(len(dungchi)):
        if i == dungchi[j]:
            pass
        elif i[0] >= dungchi[j][0] and i[1] >= dungchi[j][1]:
            pass
        elif i[0] >= dungchi[j][0] and i[1] <= dungchi[j][1]:
            pass
        elif i[0] <= dungchi[j][0] and i[1] >= dungchi[j][1]:
            pass
        else:
            ranking += 1s
        
    answer.append(ranking)

print(*answer)