def solution(arr):
    a = min(arr)
    arr.remove(a)
    if len(arr) > 0:
        answer = arr
    else:
        answer = [-1]
    return answer