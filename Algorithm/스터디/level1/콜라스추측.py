colas = int(input())
cnt = 0

while colas != 1:
    if colas % 2 == 0:
        colas = colas // 2
        cnt += 1
    
    elif colas % 2 != 0:
        colas = (colas * 3) + 1
        cnt += 1
    
    if cnt > 500:
        break

if cnt <= 500:
    print(cnt)
else:
    print(-1)
