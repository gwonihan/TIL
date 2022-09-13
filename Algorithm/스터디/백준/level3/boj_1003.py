# 피보나치 함수
def fibo(N):
    zeros=[1,0,1]
    ones=[0,1,1]

    if N >= 3:
        for i in range(2,N):
            zeros.append(zeros[i-1] + zeros[i])
            ones.append(ones[i-1] + ones[i])

    print(f"{zeros[N]} {ones[N]}")

T = int(input())
for _ in range(T):
    N = int(input())
    fibo(N)


# 숏코딩
T = int(input())

for _ in range(T):
    N = int(input())

    # zero : 0개수, one : 1개수
    zero,one = 1,0

    for i in range(N):
        zero, one = one, zero+one
    print(zero,one)

