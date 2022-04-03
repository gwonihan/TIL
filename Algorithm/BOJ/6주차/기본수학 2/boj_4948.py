# 베르트랑 공준

while True:
    n = int(input())
    if n == 0:
        break
    num_list = []
    for i in range(n,2*n+1):
        if i != 1:
            for j in range(2,int(i**0.5)+1):
                if i % j !=0:
                    break
            else:
                num_list.append(i)
        
            
    print(len(num_list))
                    
        
        