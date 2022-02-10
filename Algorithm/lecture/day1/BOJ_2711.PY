# 오타맨 고창영

for _ in range(int(input())):
    index, word = input().split()
    index = int(index)
    print(word[:index-1] + word[index:])
