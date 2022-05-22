# 이상한 문자 만들기
s = "try hello world"

word_li = list(s.split())

for word in word_li:
    for j in range(len(word)):
        if j == 0 or j % 2 == 0:
            word[j] = word[j].upper()
            print(word)
        else:
            pass

