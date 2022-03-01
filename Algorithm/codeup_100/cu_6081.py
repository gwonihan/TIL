# 다시 풀어보기

n = int(input(), 16)

for i in range(1,16):
    print('%X'%n, '*%X'%i, '=%X'%(n*i), sep="")