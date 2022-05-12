# 한수

n = int(input())
num_li = list(range(1,n+1))

cnt=0

for i in num_li:
    if i < 100:
        cnt +=1
    else:
        li = list(map(int, str(i)))
        if li[0] - li[1] == li[1] - li[2]:
            cnt +=1

print(cnt)