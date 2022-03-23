# 접두사 배열
word = input()
li = []
for i in range(len(word)):
    li.append(word[i:])

dic = {string:i for i,string in enumerate(li)}
dic1 = sorted(dic.items())

for i in range(len(word)):
    print(dic1[i][1])