# 나무 자르기
N,M  =map(int,input().split())
namu = list(map(int,input().split()))


start, end = 1, max(namu)

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for tree in namu:
        if tree >= mid:
            cnt += tree - mid

    if cnt >= M:
        start = mid + 1
        
    else:
        end = mid -1
        
print(end)

