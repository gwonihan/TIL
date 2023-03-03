# 문자열 집합
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
n_se = set()

for _ in range(n):
    n_se.add(input())

m_li = [input() for _ in range(m)]

cnt = 0
for i in m_li:
    if i in n_se:
        cnt += 1

print(cnt)

# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# n_li = [input() for _ in range(n)]
# m_li = [input() for _ in range(m)]

# cnt = 0
# for i in m_li:
#     if i in n_li:
#         cnt += 1

# print(cnt)



# li = []

# for _ in range(n):
#     s = input()

#     li.append(s)

# cnt = 0
# for _ in range(m):
#     s = input()

#     if s in li:
#         cnt += 1

# print(cnt)