# 달팽이는 올라가고 싶다
A, B, V = map(int,input().split())

# A*day -B(day-1) = V
if (V-B) % (A-B) == 0:
    day = (V-B) // (A-B)

else:
    day = (V-B) // (A-B) +1

print(day)



# up = 2
# day = 1

# while True:
#     day += 1
#     up += A

#     if up <= V:
#         up -= B

#     else:
#         break

# print(day)