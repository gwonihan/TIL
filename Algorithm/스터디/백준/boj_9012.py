# 괄호
T = int(input())

for _ in range(T):
    s = input()

    while '()' in s:
        s = s.replace('()', '')
    
    if len(s) == 0:
        print("YES")
    else:
        print("NO")