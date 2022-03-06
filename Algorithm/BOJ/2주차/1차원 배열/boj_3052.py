num_list = []
d_list = []

for _ in range(10):
    n = int(input())
    num_list.append(n)

for i in range(10):
    a = num_list[i] % 42
    d_list.append(a)

print(len(set(d_list)))

# arr = []
# for i in range(10):
#     v = int(input())
#     arr.append(v % 42)
# setArr = set(arr)
# print(len(setArr))