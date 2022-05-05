#문자열 압축
word = input()

word_list = list(word)
cnt_list = []

for alpa in word_list:
    cnt = 0
    for i in range(len(word)):
        if alpa == word_list[i]:
            cnt += 1
            print(cnt) 
        else:
            cnt_list.append(str(cnt)+alpa)
    


# aaaab

# aabbaccc

# 2a2ba3c