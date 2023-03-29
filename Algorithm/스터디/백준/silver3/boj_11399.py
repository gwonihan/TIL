# ATM
import sys
input = sys.stdin.readline
N = int(input())
seq = list(map(int, input().split()))
seq.sort()

time = 0
for i in range(len(seq)):
    time += sum(seq[:i+1])

print(time)