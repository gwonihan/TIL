# 단어 정렬
N = int(input())
dic = {}

for _ in range(N):
    M = input()
    dic[M] = len(M)

dic = sorted(dic.items(), key=lambda x:x[1])
print(dic)