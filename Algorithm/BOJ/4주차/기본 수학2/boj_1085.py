# 직사각형에서 탈출
x, y, w, h = map(int, input().split())
min_list = []

min_list.append(x-0)
min_list.append(y-0)
min_list.append(w-x)
min_list.append(h-y)

print(min(min_list))

