a = int(input())
b = int(input())
c = int(input())
d = a*b*c
li = list(map(int, str(d)))

for i in range(10):
    print(li.count(i))
    