a = input().split()
list = []
for i in a:
    list.append(int(i))
list.sort()
list_s = set(list)

if len(list_s)==1:
    print(10000+list[0]*1000)
elif len(list_s) ==3:
    print(list[-1]*100)
else:
    print(1000+list[1]*100)
