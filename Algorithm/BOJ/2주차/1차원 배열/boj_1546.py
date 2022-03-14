n = int(input())

score = list(map(int,input().split()))
scores = 0
max_score = max(score)

for i in score:
    n = i / max_score * 100
    scores += n

print(scores/len(score))

