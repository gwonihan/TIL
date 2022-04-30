#문자열 압축

word = input()

word_list = list(word)
cnt_list = []
cnt = 0
for i in range(len(word_list)):
    if word_list[i] == word_list[i+1]:
        cnt +=1
    
    else:
        cnt_list.append(str(cnt) + word_list[i])

print(cnt_list)




# aaaab
# aabbaccc
# 2a2ba3c