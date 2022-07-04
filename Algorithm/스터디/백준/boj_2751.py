# 수 정렬하기 2
import sys
N = int(sys.stdin.readline())

num_li = [int(sys.stdin.readline()) for _ in range(N)]
num_li.sort()
print(*num_li, sep='\n')



# for _ in range(N):
#     num_li.append(int(sys.stdin.readline()))

