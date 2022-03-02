a = int(input())
b = input()
c = list(b)
for i in c[::-1]:
    print(a*int(i))
print(a*int(b))