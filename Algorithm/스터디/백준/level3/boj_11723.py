# 집합

import sys
m = int(sys.stdin.readline())
S = set()

for _ in range(m):
    order = sys.stdin.readline().split()

    if len(order) == 1:
        if order[0] == 'all':
            S = set([i for i in range(1,21)])
        else:
            S = set()
    
    else:
        order, num = order[0], order[1]
        num = int(num)

        if order == 'add':
            S.add(num)
        elif order =='remove':
            S.discard(num)
        elif order == 'check':
            print(1 if num in S else 0)
        elif order == 'toggle':
            if num in S:
              S.discard(num)
            else:
                S.add(num)
    
    


