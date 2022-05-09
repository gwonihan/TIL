# 잃어버린 괄호

a = input().split('-')
num_li = []
for num in a:
    cnt = 0
    plus = num.split('+')
    for i in plus:
        cnt += int(i)
    num_li.append(cnt)

n = num_li[0]

for i in range(1,len(num_li)):
    n -= num_li[i]

print(n)