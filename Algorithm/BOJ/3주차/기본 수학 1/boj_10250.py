num = int(input())

for _ in range(num):
    H,W,N = map(int,input().split())
    floor = N % H
    room = N // H + 1

    if floor == 0:
        room -= 1
        floor = H
    
    print(floor*100 + room)




# test = int(input())

# for _ in range(test):
#     H,W,N = map(int,input().split())

# hotel = []
# for i in range(H):
#     hotel.append([])
#     for j in range(1,W+1):
#         hotel[i].append((i+1)*100+j)        

# count = 1
# x,y = 0,0
# while N == count:
#     try:
#         x += 1
#         count +=1
#     except:
#         y += 1
#         count +=1
# print(hotel[x][y])

            
        
