# 이상한 문자 만들기
s = "try hello world"

word_li = list(s.split())
cng_list = []

for word in word_li:
    cng = ""
    for s in range(len(word)):
        if s == 0 or s % 2 == 0:
            cng += word[s].upper()
        else:
            cng += word[s].lower()
    cng_list.append(cng)

print(" ".join(cng_list))
