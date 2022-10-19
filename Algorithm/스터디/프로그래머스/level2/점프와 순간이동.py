# 점프와 순간이동
def solution(n):
    ans = 0
    
    while n != 0:

        # n 이 짝수일 경우, n을 2로 나눈 몫으로 갱신(순간이동)
        if n % 2 == 0:
            n = n // 2
            
        # n 이 홀수일 경우, n에서 1을 빼고 점프 횟수 1을 더한다(점프)    
        else:
            n -= 1
            ans += 1
        
    return ans