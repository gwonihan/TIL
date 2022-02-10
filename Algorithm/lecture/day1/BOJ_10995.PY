# 별 찍기 3

n = int(input())

for i in range(n):
    # print("* " * n if i % 2 == 0 else " *" * n)
    # 한 줄로 작성 가능
    # / : 나눈 몫, % : 나머지
    
    if i % 2 == 0:
        print("* " * n)

    else:
        print(" *" * n)