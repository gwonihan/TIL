# 같은 숫자는 싫어
arr = [1,1,3,3,0,1,1]
print(len(arr))
for i in range(0,len(arr)-2):
    if arr[i] == arr[i+1]:
        arr.remove(arr[i])
    else:
        pass

# 0 1 2 3 4 5 6