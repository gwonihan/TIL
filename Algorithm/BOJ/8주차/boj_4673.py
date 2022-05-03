# 셀프 넘버
number = list(range(1,10001))
li = []

for num in number:
    for n in str(num):
        num += int(n)

    if num <= 10000:
        li.append(num)
    
for i in li:
    if i in number:
        number.remove(i)

for i in number:
    print(i)
