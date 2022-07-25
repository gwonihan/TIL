# 괄호
T = int(input())

# 입력 받은 정수 만큼 문자열을 받는다
for _ in range(T):
    s = input()
    
    
	# while 문을 사용하여 올바르게 짝지어진 괄호가 사라질 때까지
    # 반복하여 소거해 나간다
    while '()' in s:
        s = s.replace('()', '')
    
    # while문이 종료되고 문자열의 길이가 0 이라면, 괄호가 올바르게 짝지어져 있는 것 이므로
    # YES를 출력하고 아닐 경우 NO를 출력한다
    if len(s) == 0:
        print("YES")
    else:
        print("NO")