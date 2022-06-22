# Hashing

L = int(input())
M = 1234567891
r = 31
str_ = list(input())
res = 0

for i in range(L):
    res += ((ord(str_[i])-96) * (r ** i))

print(res % M)