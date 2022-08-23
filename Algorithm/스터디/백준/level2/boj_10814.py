# # 나이순 정렬
# N = int(input())
# member = []

# for _ in range(N):
#     member.append(list(input().split()))

# member.sort(key=lambda x: int(x[0]))

# for age, name in member :
#     print(age,name,sep=' ')
    
import sys

N = int(sys.stdin.readline())
member = {}

for _ in range(N):
    age, name = sys.stdin.readline().split()
    member[name] = int(age)

print(member)

member = sorted(member.items(), key=lambda x:x[1])

print(member)

for name,age in member:
    print(age, name, sep=' ')