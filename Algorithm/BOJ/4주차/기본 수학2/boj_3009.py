# 네 번째 점
x_list = []
y_list = []

for _ in range(3):
    x,y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

for i in range(3):
    if x_list.count(x_list[i]) == 1:
        need_x = x_list[i]

    if y_list.count(y_list[i]) == 1:
        need_y = y_list[i]

print(need_x, need_y)

