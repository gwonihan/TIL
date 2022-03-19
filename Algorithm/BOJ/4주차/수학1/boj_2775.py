# 부녀회장이 될테야
n = int(input())

for _ in range(n):
    floor = int(input())
    room = int(input())
    floor_1 = [x for x in range(1, room+1)]

    for _ in range(floor):
        for j in range(1, room):
            floor_1[j] += floor_1[j-1]
    print(floor_1[-1])