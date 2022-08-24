# N개의 최소 공배수

def solution(arr):
    
    LCM = 1
    while True: 
        for i in arr:
            if LCM % i != 0:
                LCM += 1
                break
        else:
            return LCM