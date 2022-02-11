# name = input().split()
# baseball = {}

# for i in name:
#     baseball[i] = 0
#     for key in baseball.keys():
#         if key == i:
#             baseball[i] += 1


# print(baseball) 
# Jay John John Jay Jack Jack John Jo Jo Jack

# 강사님 풀이
players = input().split()
fouls = {}

for player in players:
    # 이미 파울을 했니?
    if player in fouls:
        fouls[player] += 1

    # 파울 한번도 안했니?
    else:
        fouls[player] = 1

# 파울 가장 적게한 선수 뽑기
min_foul = min(fouls.values())

for player, foul in fouls.items():
    if foul == min_foul:
        print(player)

print(min_foul)