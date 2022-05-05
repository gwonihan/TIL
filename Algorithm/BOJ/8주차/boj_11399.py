# ATM
n = int(input())

wait = list(map(int,(input().split())))
wait.sort()
num = 0

for i in range(n):
    for j in range(i + 1):
        num += wait[j]
    
   
print(num)       

    


