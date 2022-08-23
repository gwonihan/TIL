# 스택 수열
n = int(input())
stack = []
answer = []

error = 0
cnt = 1

for i in range(n):
    num = int(input())

    while cnt <= num:
        stack.append(cnt)
        answer.append("+")
        cnt += 1

    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    else:
        error += 1
        break

if error == 0:
    for i in answer:
        print(i)
else:
    print("NO")