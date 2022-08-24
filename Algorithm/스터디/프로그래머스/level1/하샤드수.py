# 하샤드수

num = int(input())
s = 0

for i in str(num):
    s += int(i)

if num % s ==0:
    print('true')
else:
    print('false')
